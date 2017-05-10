---
layout: episode
title: "Using the Git staging area"
teaching: 10
exercises: 0
questions:
  - Why do we recommend to first add, then commit a change?
objectives:
  - Try to demystify the Git staging area.
  - Goal is to understand, not to remember (you can revisit this page later).
keypoints:
  - The staging area helps us to create well-defined commits.
---

## States of a file.

We recall that we have committed changes in two steps.
We have used `git add` and `git commit`:

```shell
$ git add     # stages the change
$ git commit  # commits the staged change
```

In general files can have one of 4 states inside a Git repository:

![States of a Git file]({{ site.baseurl }}/img/lifecycle.png "States of a Git file. License CC BY 3.0"){:class="img-responsive"}
(Image from the [Pro Git book](https://git-scm.com/book/), licensed under CC BY 3.0)

---

## Why the staging?

### It is useful to have a nice and readable history

Bad example:

```shell
b135ec8 now feature A should work
72d78e7 fix for parallel compilation
bf39f9d bugfix
49dc419 removed too much
45831a5 removing debug print
bddb280 more work on feature B
72e0211 another fix to make it compile
e2073c3 oops! forgot another file
61dd3a3 forgot file
a9f5172 save work on feature A
6fe2f23 save work on feature B
```

- Very often you will be obliged to do archaeology in your code.
- Imagine that in few months you discover that feature B was a mistake.
- It is very difficult to find and revert this in this example.

### Main development line should have a nice and readable history

Good example:

```shell
6f0d49f implement feature C
fee1807 implement feature B
6fe2f23 implement feature A
```

We want to have nice commits.
But we also want to "save often" (checkpointing) - how can we have both?

We will now learn to fabricate nice commits using the staging area.

---

## Checkpointing using the staging area

```
                   unmodified   modified    staged   committed
                        |          |          |          |
command                 |          |          |          |   English translation

git add file(s)         |          |--------->|          |   stage file
git commit              |          |          |--------->|   commit staged file(s)
git commit file(s)      |          |-------------------->|   commit file(s) directly

git diff                |          |<-------->|          |   between modified and staged
git diff --cached       |          |          |<-------->|   between staged and last commit
git diff HEAD           |          |<------------------->|   between modified and last commit
git diff                |          |<------------------->|   if nothing is staged

git reset               |          |<---------|          |   unstage
git reset --hard        |<---------|          |          |   discard
git reset --hard        |<--------------------|          |   discard
git reset --soft <hash> |          |<--------------------|   "uncommit" everything after <hash>
git reset --hard <hash> |<-------------------------------|   "uncommit" everything after <hash> and abandon changes

git checkout            |<---------|          |          |   undo unstaged modifications
```

- We will discuss what the `HEAD` is in the next section.
- `git add` every change that improves the code.
- `git checkout` every change that made things worse.
- `git commit` as soon as you have created a nice self-contained unit (not too large, not too small).
- Discuss/think about what is too large or too small.


### Compare with working without the staging area

```
                tracked     staged   committed
              but unstaged    |          |
command            |          |          |   English translation

git commit file(s) |-------------------->|   commit file(s)
git diff           |<------------------->|   between modified and last commit
git checkout       |<--------------------|   undo uncommitted modifications
```

### Example

```shell
$ git add file.py                 # checkpoint 1
$ git add file.py                 # checkpoint 2
$ git add another_file.py         # checkpoint 3
$ git add another_file.py         # checkpoint 4
$ git diff another_file.py        # diff w.r.t. checkpoint 4
$ git checkout another_file.py    # oops go back to checkpoint 4
$ git commit                      # commit everything that is staged
```

- `git diff` gives differences with respect to the staging area, this is very practical.
- Using `git add` we can fabricate very nice coherent commits.

---

## Staging everything

Sometimes you want to stage all modifications.
No need to stage them one by one:

```shell
$ git add -u
```

Also removals of tracked files are then automatically staged.

---

## Homework

- Prepare **one** nice commit to the guacamole recipe by staging **several** small changes.
- When doing this experiment with `git diff` and `git checkout <path>` to get a feel for checkpointing.
- Observe how `git diff` and `git checkout <path>` are with respect to *staged* changes.
- If you see a change with `git diff`, try also `git difftool`.

---

## Questions

- When is it better to "save" a change as commit, when is it better to "save" it with `git add`?
- Is it a problem to commit many small changes?
