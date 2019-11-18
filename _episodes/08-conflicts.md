---
layout: episode
title: Conflict resolution
teaching: 15
exercises: 15
questions:
  - How can we resolve conflicts?
  - How can we avoid conflicts?
objectives:
  - Understand merge conflicts sufficiently well to be able to fix them.
keypoints:
  - Conflicts often appear because of not enough communication or not optimal branching strategy.
---

## Conflict resolution

<img src="{{ site.baseurl }}/img/conflict-resolution/conflict.png" width="60%">

In most cases a `git merge` runs smooth and automatic.
Then a merge commit appears (unless fast-forward) without you even noticing.

Git is very good at resolving modifications when merging branches.

But sometimes the same line or portion of the code/text is modified on two branches and Git issues a **conflict**.
Then you need to tell Git which version to keep (**resolve** it).

There are several ways to do that as we will see.

Please remember:

- Conflicts look scary, but are not that bad after a little bit of practice. Also they are luckily rare.
- Don't be afraid of Git because of conflicts. You may not meet some conflicts using other systems because you simply can't do the kinds of things you do in Git.
- You can take human measures to reduce them.

---

## Type-along: create a conflict

We will make two branches, make two conflicting changes (both increase
and decrease the amount of cilantro), and then try to merge them
together.  Git won't decide which to take for you, so will present it
to you for deciding.  We do that and commit again to resolve the
conflict.

- Create two branches from `master`: one called `like-cilantro`, one called `dislike-cilantro`:

```shell
$ git graph

*   4b3e3cc (HEAD -> master, like-cilantro, dislike-cilantro) Merge branch 'less-salt'
|\
| * bf59be6 reduce amount of salt
* |   80351a9 Merge branch 'experiment'
|\ \
| * | 6feb49d maybe little bit less cilantro
| * | 7cf6d8c let us try with some cilantro
| |/
* | 40fbb90 draft a readme
|/
* dd4472c we should not forget to enjoy
* 2bb9bb4 add half an onion
* 2d79e7e adding ingredients and instructions
```

- On the two branches make **different modifications** to the amount of the **same ingredient**:

```shell
$ git graph

* eee4b85 (dislike-cilantro) reduce cilantro to 0.5
| * 55d1ce2 (like-cilantro) please more cilantro
|/
*   4b3e3cc (HEAD -> master) Merge branch 'less-salt'
|\
| * bf59be6 reduce amount of salt
* |   80351a9 Merge branch 'experiment'
|\ \
| * | 6feb49d maybe little bit less cilantro
| * | 7cf6d8c let us try with some cilantro
| |/
* | 40fbb90 draft a readme
|/
* dd4472c we should not forget to enjoy
* 2bb9bb4 add half an onion
* 2d79e7e adding ingredients and instructions
```

On the branch `like-cilantro` we have the following change:

```
$ git diff master like-cilantro
```

```diff
diff --git a/ingredients.txt b/ingredients.txt
index a83af39..83f2f94 100644
--- a/ingredients.txt
+++ b/ingredients.txt
@@ -1,4 +1,4 @@
-* 1 tbsp cilantro
+* 2 tbsp cilantro
 * 2 avocados
 * 1 lime
 * 1 tsp salt
```

And on the branch `dislike-cilantro` we have the following change:

```
$ git diff master dislike-cilantro
```

```diff
diff --git a/ingredients.txt b/ingredients.txt
index a83af39..2f60e23 100644
--- a/ingredients.txt
+++ b/ingredients.txt
@@ -1,4 +1,4 @@
-* 1 tbsp cilantro
+* 0.5 tbsp cilantro
 * 2 avocados
 * 1 lime
 * 1 tsp salt
```

### What do you expect will happen when we try to merge these two branches into master?

The first merge will work:

```shell
$ git checkout master
$ git status
$ git merge like-cilantro

Updating 4b3e3cc..55d1ce2
Fast-forward
 ingredients.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

But the second will fail:


```shell
$ git merge dislike-cilantro

Auto-merging ingredients.txt
CONFLICT (content): Merge conflict in ingredients.txt
Automatic merge failed; fix conflicts and then commit the result.
```

Without conflict Git would have automatically created a merge commit,
but since there is a conflict, Git did not commit:

```shell
$ git status

On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)

	both modified:   ingredients.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

Observe how Git gives us clear instructions on how to move forward.

Let us inspect the conflicting file:

```
$ cat ingredients.txt

<<<<<<< HEAD
* 2 tbsp cilantro
=======
* 0.5 tbsp cilantro
>>>>>>> dislike-cilantro
* 2 avocados
* 1 lime
* 1 tsp salt
* 1/2 onion
```

Git inserted resolution markers (the `<<<<<<<`, `>>>>>>>`, and `=======`).

Try also `git diff`:

```
$ git diff
```

```diff
diff --cc ingredients.txt
index 83f2f94,2f60e23..0000000
--- a/ingredients.txt
+++ b/ingredients.txt
@@@ -1,4 -1,4 +1,8 @@@
++<<<<<<< HEAD
 +* 2 tbsp cilantro
++=======
+ * 0.5 tbsp cilantro
++>>>>>>> dislike-cilantro
  * 2 avocados
  * 1 lime
  * 1 tsp salt
```

`git diff` now only shows the conflicting part, nothing else.

We have to resolve the conflict.
We will discuss 3 different ways to do this.

---

## Manual resolution

```
<<<<<<< HEAD
* 2 tbsp cilantro
=======
* 0.5 tbsp cilantro
>>>>>>> dislike-cilantro
```

We have to edit the code/text between the resolution markers.  You
only have to care about what git shows you: Git stages all files
without conflicts and leaves the files with conflicts unstaged.

Simple steps:

- Check status with `git status` and `git diff`.
- Decide what you keep (the one, the other, or both or something
  else).  Edit the file to do this.
  - Remove the resolution markers, if not already done.
  - The file(s) should now look exactly how you want them.
- Check status with `git status` and `git diff`.
- Tell Git that you have resolved the conflict with `git add ingredients.txt`
  (if you use the Emacs editor with a certain plugin the editor may stage the
  change for you after you have removed the conflict markers).
- Verify the result with `git status`.
- Finally commit the merge with just `git commit` - everything is pre-filled.

---

> ## Exercise: Create another conflict and resolve
>
> 1. After you have merged `like-cilantro` and `dislike-cilantro` create again two branches.
> 2. Again modify some ingredient on both branches.
> 3. Merge one, merge the other and observe a conflict, resolve the conflict and commit the merge.
> 4. What happens if you apply the same modification on both branches?
{: .challenge}

---

> ## (Optional) Exercise: Conflicts and rebase
>
> 1. Create two branches where you anticipate a conflict.
> 2. Try to merge them and observe that indeed they conflict.
> 3. Abort the merge.
> 4. What you if you rebase one branch on top of the other? Do you anticipate a conflict? Try it out.
{: .challenge}

---

> ## (Optional) Resolution using mergetool
>
> - Again create a conflict (for instance disagree on the number of avocados).
> - Stop at this stage:
>
> ```
> Auto-merging ingredients.txt
> CONFLICT (content): Merge conflict in ingredients.txt
> Automatic merge failed; fix conflicts and then commit the result.
> ```
>
> - Instead of resolving the conflict manually, use a visual tool
>   (requires installing one of the [visual diff tools](https://coderefinery.github.io/installation/difftools/)):
>
> ```shell
> $ git mergetool
> ```
>
> <img src="{{ site.baseurl }}/img/conflict-resolution/mergetool.png" width="100%">
>
> - Your current branch is left, the branch you merge is right, result is in the middle.
> - After you are done, close and commit, `git add` is not needed when using `git mergetool`.
>
> If you have not instructed Git to avoid creating backups when using mergetool, then to be on
> the safe side there will be additional temporary files created. To remove those  you can do
> a git clean after the merging.
>
> To view what will be removed:
>
> ```
> $ git clean -n
> ```
>
> To remove:
>
> ```
> $ git clean -f
> ```
>
> To configure Git to avoid creating backups at all:
>
> ```
> $ git config --global mergetool.keepBackup false
> ```
{: .challenge}

---

## Using "ours" or "theirs" strategy

- Sometimes you know that you want to keep "ours" version (version on this branch)
  or "theirs" (version on the merged branch).
- Then you do not have to resolve conflicts manually.
- See [merge strategies](https://git-scm.com/docs/merge-strategies).

Example:

```shell
$ git merge -s recursive -Xours less-avocados  # merge and in doubt take the changes from current branch
```

Or:

```shell
$ git merge -s recursive -Xtheirs less-avocados  # merge and in doubt take the changes from less-avocados branch
```

---

## Aborting a conflicting merge

- Imagine it is Friday evening, you try to merge but have conflicts all over the place.
- You do not feel like resolving it now and want to undo the half-finished merge.
- Or it is a conflict that you cannot resolve and only your colleague knows which version is the one to keep.

What to do?

- There is no reason to delete the whole repository.
- You can undo the broken merge by resetting the repository to `HEAD` (last committed state).

```shell
$ git merge --abort
```

The repository looks then exactly as it was before the merge.

---

## Avoiding conflicts

- Human measures
  - Think and plan to which branch you will commit to.
  - Ball-of-mud branches for "everything" maximize risk of conflicts.
  - One branch for one task only.
- Collaboration measures
  - Conflicts can be avoided if you think and talk with your colleagues before committing.
  - Semantic conflicts that merge but don't work: Importance of talking!
- Project layout measures
  - Fortran people: modifying common blocks often causes conflicts.
  - Modifying global data often causes conflicts.
  - Monolithic entangled spaghetti-code maximizes risk of conflicts.
  - Modular programming minimizes risk of conflicts.
- Technical measures
  - **Push early and often** - this is one of the happy,
    rare circumstances when everyone doing the selfish thing (pushing as early as practical) results in best case for everyone!
  - Pull/rebase often to keep up to date with upstream.
  - Resolve conflicts early.

Discuss how Git handles conflicts compared to the Google Drive.
