(conflict-resolution)=

# Conflict resolution

```{objectives}
- Understand merge conflicts sufficiently well to be able to fix them.
```

```{instructor-note}
- 15 min teaching/type-along
- 15 min exercise
```


## Conflicts in Git and why they are good

Imagine we start with the following text file:
```{code-block}
2 avocados
1 tbsp cilantro
2 tsp salt
```

On branch A somebody modifies:
```{code-block}
---
emphasize-lines: 1, 3
---
1 lime
2 avocados
1/2 tbsp cilantro
2 tsp salt
```

On branch B somebody else modifies:
```{code-block}
---
emphasize-lines: 2, 4
---
2 avocados
2 tbsp cilantro
2 tsp salt
1/2 onion
```

When we try to merge Git will figure out that we want the lime and the onion
but does not know whether to reduce or increase the amount of cilantro:
```{code-block}
---
emphasize-lines: 3
---
1 lime
2 avocados
??????????????
2 tsp salt
1/2 onion
```

Git is very good at resolving modifications when merging branches and
in most cases a `git merge` runs smooth and automatic.
Then a merge commit appears (unless fast-forward) without you even noticing.

But sometimes the **same portion** of the code/text is modified on two branches**in two different ways** and Git issues a **conflict**.
Then you need to tell Git which version to keep (**resolve** it).

There are several ways to do that as we will see.

Please remember:

- It is good that Git conflicts exist: Git will not silently overwrite one of
  two differing modifications.
- Conflicts may look scary, but are not that bad after a little bit of
  practice. Also they are luckily rare.
- Don't be afraid of Git because of conflicts. You may not meet some conflicts
  using other systems because you simply can't do the kinds of things you do
  in Git.
- You can take human measures to reduce them.

---

```{discussion} The human side of conflicts
- What does it mean if two people do the same thing in two different ways?
- What if you work on the same file but do two different things in the different sections?
- What if you do something, don't tell someone from 6 months, and then try to combine it with other people's work?
- How are conflicts avoided in other work? (Only one person working at once?
  Declaring what you are doing before you start, if there is any chance someone
  else might do the same thing, helps.)
- Minor conflicts (two people revise spelling) vs semantic (two people rewrite
  a function to add two different new features). How did Git solve these in
  branching/merging easily?
```

Now we can go to show how Git controls when there is actually a conflict.


## Preparing a conflict

```{instructor-note}
We do the following together as type-along.
```

We will make two branches, make two conflicting changes (both increase and
decrease the amount of cilantro), and later we will try to merge them
together.

- Create two branches from `master`: one called `like-cilantro`, one called `dislike-cilantro`:
  ```console
  $ git branch like-cilantro master
  $ git branch dislike-cilantro master
  ```

- On the two branches make **different modifications** to the amount of the **same ingredient**:

- On the branch `like-cilantro` we have the following change:
  ```console
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

- And on the branch `dislike-cilantro` we have the following change:
  ```console
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


## Merging conflicting changes

What do you expect will happen when we try to merge these two branches into
master?

The first merge will work:

```console
$ git checkout master
$ git status
$ git merge like-cilantro

Updating 4b3e3cc..55d1ce2
Fast-forward
 ingredients.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

But the second will fail:

```console
$ git merge dislike-cilantro

Auto-merging ingredients.txt
CONFLICT (content): Merge conflict in ingredients.txt
Automatic merge failed; fix conflicts and then commit the result.
```

Without conflict Git would have automatically created a merge commit,
but since there is a conflict, Git did not commit:

```console
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

Git won't decide which to take and we need to decide.  Observe how Git gives
us clear instructions on how to move forward.

Let us inspect the conflicting file:

```console
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


## Manual resolution

```
<<<<<<< HEAD
* 2 tbsp cilantro
=======
* 0.5 tbsp cilantro
>>>>>>> dislike-cilantro
```

We have to edit the code/text between the resolution markers.  You
only have to care about what Git shows you: Git stages all files
without conflicts and leaves the files with conflicts unstaged.

```{note}
**Steps to resolve a conflict:**

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
```

(exercise-conflicts)=

## Exercise: Create and resolve a conflict

````{exercise} Conflict-1: Create another conflict and resolve
In this exercise, we repeat almost exactly what we did above with a
different ingredient.

1. Create two branches before making any modifications.
2. Again modify some ingredient on both branches.
3. Merge one, merge the other and observe a conflict, resolve the conflict and commit the merge.
4. What happens if you apply the same modification on both branches?
5. If you create a branch `like-avocados`, commit a change, then from this
   branch create another banch `dislike-avocados`, commit again, and try to
   merge both branches into `master` you will not see a conflict. Can you
   explain, why it is different this time?
```{solution}
4: No conflict in this case if the change is the same.

5: No conflict in this case since in Git history one change happened after the other. The two changes
   are related and linked by Git history and one is a Git ancestor of the
   other. Git will assume that since we applied one change after the other,
   we meant this. There is nothing to resolve.
```
````

(exercise-conflicts-optional)=

## Optional exercises with conflict resolution

````{exercise} (optional) Conflict-2: Resolve a conflict when rebasing a branch
1. Create two branches where you anticipate a conflict.
2. Try to merge them and observe that indeed they conflict.
3. Abort the merge with `git merge --abort`.
4. What do you expect will happen if you rebase one branch on top of the
   other? Do you anticipate a conflict? Try it out.
```{solution}
Yes, this will conflict. If it conflicts during a merge, it will also conflict
during rebase but the conflict resolution looks slightly different:
You still need to look for conflict markers but you tell Git that you resolved
a conflict with `git add` and then you continue with `git rebase --continue`.
Follow instructions that you get from the Git command line.
```
````

````{exercise} (optional) Conflict-3: Resolve a conflict using mergetool
  - Again create a conflict (for instance disagree on the number of avocados).
  - Stop at this stage:

    ```
    Auto-merging ingredients.txt
    CONFLICT (content): Merge conflict in ingredients.txt
    Automatic merge failed; fix conflicts and then commit the result.
    ```

  - Instead of resolving the conflict manually, use a visual tool
    (requires installing one of the [visual diff tools](https://coderefinery.github.io/installation/difftools/)):

    ```console
    $ git mergetool
    ```

    ```{figure} img/conflict-resolution/mergetool.png
    :alt: Conflict resolution using mergetool
    :width: 100%
    ```

  - Your current branch is left, the branch you merge is right, result is in the middle.
  - After you are done, close and commit, `git add` is not needed when using `git mergetool`.

  If you have not instructed Git to avoid creating backups when using mergetool, then to be on
  the safe side there will be additional temporary files created. To remove those  you can do
  a git clean after the merging.

  To view what will be removed:

  ```
  $ git clean -n
  ```

  To remove:

  ```
  $ git clean -f
  ```

  To configure Git to avoid creating backups at all:

  ```
  $ git config --global mergetool.keepBackup false
  ```
````

---

## Using "ours" or "theirs" strategy

- Sometimes you know that you want to keep "ours" version (version on this branch)
  or "theirs" (version on the merged branch).
- Then you do not have to resolve conflicts manually.
- See [merge strategies](https://git-scm.com/docs/merge-strategies).

Example:

```console
$ git merge -s recursive -Xours less-avocados  # merge and in doubt take the changes from current branch
```

Or:

```console
$ git merge -s recursive -Xtheirs less-avocados  # merge and in doubt take the changes from less-avocados branch
```

---

## Aborting a conflicting merge

Sometimes you get a merge conflict but realize that you can't solve it without
talking to a colleague (who created the other change) first. What to do?

You can abort the merge and postponing conflict resolution by resetting the
repository to `HEAD` (last committed state):

```console
$ git merge --abort
```

The repository looks then exactly as it was before the merge.

---

## Avoiding conflicts

- Human measures
  - Think and plan to which branch you will commit to.
  - Do not put unrelated changes on the same branch.
- Collaboration measures
  - Open an issue and discuss with collaborators before starting a long-living
  - branch.
- Project layout measures
  - Modifying global data often causes conflicts.
  - Modular programming minimizes risk of conflicts.
- Technical measures
  - **Push early and often** - this is one of the happy,
    rare circumstances when everyone doing the selfish thing (pushing as
    early as practical) results in best case for everyone!
  - Pull/rebase often to keep up to date with upstream.
  - Resolve conflicts early.

```{discussion}
Discuss how Git handles conflicts compared to the Google Drive.
```

```{keypoints}
- Conflicts often appear because of not enough communication or not optimal
  branching strategy.
```
