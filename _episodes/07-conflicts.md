---
layout: episode
title: Conflict resolution
teaching: 10
exercises: 15
questions:
  - How can we resolve conflicts?
  - How can we avoid conflicts?
objectives:
  - Understand the system sufficiently to fix small merge conflicts.
keypoints:
  - Conflicts often appear because of not enough communication or not optimal branching strategy.
---

## Conflict resolution

![]({{ site.baseurl }}/img/conflict-resolution/mk1.jpg)

In most cases a `git merge` runs smooth and automatic.
Then a merge commit appears (unless fast-forward) without you even noticing.

Git is very good at resolving modifications when merging branches.

But sometimes the same line is modified on two branches and Git issues a conflict.
Then you need to tell Git which version to keep.

There are several ways to do that as we will see.

---

## Exercise: create a conflict

- Create two branches from `master`.
- On the two branches make **different modifications** to the amount of the **same ingredient**.

To view the modifications:
**Note: that we are using an Git alias called 'graph' we defined in ealier in our branches lesson**.
```shell
$ git graph
```

On the branch `like-cilantro` I have the following change:

```
$ git diff master..like-cilantro

diff --git a/ingredients.txt b/ingredients.txt
index 27a808c..5550d6d 100644
--- a/ingredients.txt
+++ b/ingredients.txt
@@ -2,4 +2,4 @@
 * 1 lime
 * 1 tsp salt
 * 1/2 onion
-* 1 tbsp cilantro
+* 2 tbsp cilantro
```

And on the branch `dislike-cilantro` we have the following change:

```
$ git diff master..dislike-cilantro

diff --git a/ingredients.txt b/ingredients.txt
index 27a808c..10eed42 100644
--- a/ingredients.txt
+++ b/ingredients.txt
@@ -2,4 +2,4 @@
 * 1 lime
 * 1 tsp salt
 * 1/2 onion
-* 1 tbsp cilantro
+* 0 tbsp cilantro
```

### What do you expect will happen when I try to merge these two?

```shell
$ git branch

* dislike-cilantro
  like-cilantro
  master

$ git merge like-cilantro

Auto-merging ingredients.txt
CONFLICT (content): Merge conflict in ingredients.txt
Automatic merge failed; fix conflicts and then commit the result.
```

Without conflict Git would have automatically created a merge commit,
but since there is a conflict, Git did not commit:

```shell
$ git status

On branch dislike-cilantro
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

* 2 avocados
* 1 lime
* 1 tsp salt
* 1/2 onion
<<<<<<< HEAD
* 0 tbsp cilantro
=======
* 2 tbsp cilantro
>>>>>>> like-cilantro
```

Git inserted resolution markers (the `<<<<<<<`, `>>>>>>>`, and `=======`).

Try also `git diff`:

```
$ git diff

diff --cc ingredients.txt
index 10eed42,5550d6d..0000000
--- a/ingredients.txt
+++ b/ingredients.txt
@@@ -2,4 -2,4 +2,8 @@@
  * 1 lime
  * 1 tsp salt
  * 1/2 onion
++<<<<<<< HEAD
 +* 0 tbsp cilantro
++=======
+ * 2 tbsp cilantro
++>>>>>>> like-cilantro
```

`git diff` now only shows the conflicting part, nothing else.

We have to resolve the conflict.
We will discuss 3 different ways to do this.

---

## Manual resolution

```
<<<<<<< HEAD
* 0 tbsp cilantro
=======
* 2 tbsp cilantro
>>>>>>> like-cilantro
```

- Manual resolution means that you have to edit the code/text between the resolution markers.
- Git stages all files without conflicts and leaves the files with conflicts unstaged.
- Decide what you keep (the one, the other, or both or something else).
- Then remove the resolution markers.
- Tell Git that you have resolved the conflict with `git add ingredients.txt`.
- Then verify with `git status`.
- Now commit the merge; this opens up a prepared commit message that you can keep or modify.
- It is good practice to keep the information that there was a conflict in the commit message.

---

## Resolution using mergetool

```shell
$ git mergetool
```

![]({{ site.baseurl }}/img/conflict-resolution/mergetool.png)

- Your current branch is left, the branch you merge is right, result is in the middle.
- After you are done, close and commit, `git add` is not needed when using `git mergetool`.

If you have not instructed Git to avoid creating backups when using mergetool, then to be on
the safe side there will be additional  temporary files created. To remove those  you can do
a git clean after the merging.

To view what will be removed
`git clean -n`

To remove
`git clean -f`

To configure Git to avoid creating backups at all:

`git config --global mergetool.keepBackup false`

---

## Using "ours" or "theirs" strategy

![]({{ site.baseurl }}/img/conflict-resolution/mk2.jpg)

- Sometimes you know that you want to keep "ours" version (version on this branch)
  or "theirs" (version on the merged branch).
- Then you do not have to resolve conflicts manually.
- See [merge strategies](https://git-scm.com/docs/merge-strategies).
- If "theirs" is things done by someone else consider how they will feel.

```shell
$ git checkout --theirs ingredients.txt  # take the version of the other branch
                                         # alternative would be --ours
$ git add ingredients.txt                # tell Git that you have resolved it
$ git commit
```

---

## Aborting a conflicting merge

- Imagine it is Friday evening, you try to merge but have conflicts all over
  the place.
- You do not feel like resolving it now and want to undo the half-finished
  merge.
- Or it is a conflict that you cannot resolve and only your colleague knows
  which version is the one to keep.
- There is no reason to panic and delete the whole repository.
- Simply reset the repository to `HEAD` (last committed state).

```shell
$ git reset --hard HEAD  # throws away everything that is not in HEAD
```

The repository looks exactly as it was before the merge.

---

## Exercise: Resolve the conflict 

- Use one of the methods described above to resolve the cilantro conflict

---

## Avoiding conflicts

- Conflicts can be avoided if you think and talk with your colleagues before committing.
- Think and plan to which branch you will commit to.
- Fortran people: modifying common blocks often causes conflicts.
- Modifying global data often causes conflicts.
- Monolithic entangled spaghetti-code maximizes risk of conflicts.
- Modular programming minimizes risk of conflicts.
- Ball-of-mud branches for "everything" maximize risk of conflicts.
- One branch for one task only.
- Resolve conflicts early.
- If the branch affects code that is likely to be modified by others:
  - the branch should be short-lived and/or merge often to the main development line
  - the branch should merge the main development line often to stay up-to-date
