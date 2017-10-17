---
layout: episode
title: Interrupted work (EXTRA)
teaching: 10
exercises: 0
questions:
  - How can Git help us to deal with interrupted work and context switching?
objectives:
  - Learn to switch context or abort work without panicking.
keypoints:
  - There is almost never reason to clone a fresh copy to complete a task that you have in mind.
---

## Frequent situation: interrupted work

- Your supervisor comes in and wants you to fix/commit something right now.
- You are in the middle of a Jackson-Pollock-style debugging spree with 27 modified files
  and debugging prints everywhere.
- What to do?

---

## Option 1: Stashing

What to do with uncommitted code?

- Commit it. You can always edit local commits later.
- But sometimes you do not want to, sometimes you want to hide your changes for 5 minutes,
  do something else, then bring them back and continue.
- You can do this with `git stash`.
- It is a stack, you can stash several batches of modifications.

```shell
$ git stash      # stash your debug code away
$ git commit     # fix something for the boss, commit it
$ git stash pop  # your uncommitted modifications are back now you can continue
```

---

## Option 2: Create branches

```shell
$ git checkout -b temporary  # create a branch and switch to it
$ git add <paths>            # stage changes
$ git commit                 # commit them
$ git checkout master        # back to master
```

Later you can merge it to master or rebase it on top of master and resume work.

---

## Aborting a conflicting merge

- Imagine it is Friday evening, you try to merge but have conflicts all over the place.
- You do not feel like resolving it now and want to undo the half-finished merge.
- Or it is a conflict that you cannot resolve and only your colleague knows which version is the one to keep.
- What to do?
- There is no reason to delete the whole repository.
- You can undo the broken merge by resetting the repository to `HEAD` (last committed state).

```shell
$ git reset --hard HEAD  # throws away everything that is not in HEAD
```

The repository looks then exactly as it was before the merge.
