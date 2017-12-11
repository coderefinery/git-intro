---
layout: episode
title: Using the Git staging area (EXTRA)
teaching: 0
exercises: 0
questions:
  - Why do we recommend to first add, then commit a change?
  - How can I reason about what to commit in a single commit?
objectives:
  - Try to demystify the Git staging area.
  - Enforce the concept of telling a story with your git repository.
  - Goal is to understand, not to remember (you can revisit this page later).
keypoints:
  - The staging area helps us to create well-defined commits.
---

## Commit history is telling a story about how your code came to be

Everybody says they write self-documenting code but the reality is seldom, if
ever that reading the code makes everything clear.

Documenting things from a user level or a library or interface user level is
recommended. However nobody in their right mind documents every little details
about their code in a separate wiki or text file. Even pedantic commenting can
in fact lead to the code being unreadable if the comments to code ratio is too
large.

What does this leave for the developer? Commits and version history. Why do we
call these best practices and teach them early on?

**If you make them habit now, the drain on your time and resources is minimal
in the future**

### It is useful to have a nice and readable history

Bad example:

```shell
b135ec8 now feature A should work
72d78e7 feature A did not work and started work on feature B
bf39f9d more work on feature B
49dc419 wip
45831a5 removing debug prints for feature A and add new file
bddb280 more work on feature B and make feature A compile again
72e0211 another fix to make it compile
61dd3a3 forgot file and bugfix
```

There are multiple things that are not so stellar in this version control
history.


- Very often you will be obliged to do archaeology in your code.
- Imagine that in few months you discover that feature B was a mistake.
- It is very difficult to find and revert B this in this example.


### Main development line should have a nice and readable history

Good example:

```shell
6f0d49f implement feature C
fee1807 implement feature B
6fe2f23 implement feature A
```

We want to have nice commits.  But we also want to "save often"
(checkpointing) - how can we have both?

We will now learn to fabricate nice commits using the staging area. Staging
addresses the issue of having two different functionalities in the same
commit.

The order of the commits can be made clear one way or another using branches
and branch design, that we'll get to later. Compressing all the work done in a
feature branch is a special case of refactoring called squashing and it is
relatively advanced material even though GitHub et al. will do it for you with
the push of a button.


## States of a file.

We recall that we have committed changes in two steps.
We have used `git add` and `git commit`:

![]({{ site.baseurl }}/img/file_states.png)

```shell
$ git add     # stages the change
$ git commit  # commits the staged change
$ git remove  # removes a file
$ git reset   # unstages staged changes
$ git diff    # see **unstaged** changes
$ git checkout <path> # check out the latest staged version ( or committed
                      # version if file has not been staged )
$ git add -p <path> # stages while letting you choose which lines to take
```


- `git add` every change that improves the code.
- `git checkout` every change that made things worse.
- `git commit` as soon as you have created a nice self-contained unit (not too large, not too small).
- Discuss/think about what is too large or too small.

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
- Using `git add -p` we can work holistically and filter only the changes that
  make sense as a single commit

There is an alternative workflow where you keep making small commits and
squash them before publishing your feature branch. Which one to use is a
matter of taste.

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
