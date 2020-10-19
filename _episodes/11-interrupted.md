---
layout: episode
title: (Optional) Interrupted work
teaching: 5
exercises: 10
questions:
  - How can Git help us to deal with interrupted work and context switching?
objectives:
  - Learn to switch context or abort work without panicking.
keypoints:
  - There is almost never reason to clone a fresh copy to complete a task that you have in mind.
---

## Frequent situation: interrupted work

We all wish that we could write beautiful perfect code. But the real world is much more chaotic:

- You are in the middle of a Jackson-Pollock-style debugging spree with 27 modified files
  and debugging prints everywhere.
- Your colleague comes in and wants you to fix/commit something right now.
- What to do?

Git provides lots of ways to switch tasks without ruining everything.

---

## Option 1: Stashing

The **stash** is the first and easiest place to temporarily "stash"
things.

- `git stash` will put working directory and staging area changes
  away.  Your code will be same as last commit.
- `git stash pop` will return to the state you were before. Can give it a list.
- `git stash list` will list the current stashes.
- `git stash save NAME` is like the first, but will give it a name.
  Useful if it might last a while.
- `git stash save [-p] [filename]` will stash certain files files
  and/or by patches.
- `git stash drop` will drop the most recent stash (or whichever stash
  you give).
- The stashes form a stack, so you can stash several batches of modifications.


### Exercise: stashes

1. Make a change.
2. Check status/diff, stash the change, check status/diff again.
3. Make a separate, unrelated change which doesn't touch the same
  lines.  Commit this change.
4. Pop off the stash you saved, check status/diff.
5. Optional: Do the same but stash twice.  Also check `git stash list`.
  Can you pop the stashes in the opposite order?
6. Advanced: What happens if stashes conflict with other changes? Make
  a change and stash it.  Modify the same line or one right above or
  below.  Pop the stash back.  Resolve the conflict.  Note there is no
  extra commit.
7. Advanced: what does `git graph` show when you have something
  stashed?

---

## Option 2: Create branches

You can use branches almost like you have already been doing if you
need to save some work.  You need to do something else for a bit?
Sounds like a good time to make a feature branch.

You basically know how to do this:

```shell
$ git checkout -b temporary  # create a branch and switch to it
$ git add <paths>            # stage changes
$ git commit                 # commit them
$ git checkout master        # back to master
                             # do your work...
$ git checkout temporary     # continue where you left off
```

Later you can merge it to master or rebase it on top of master and resume work.


### Exercise: interrupted work (optional)

Use one of the strategies above to interrupt some work (recommendation
if you don't know which: use stashing).  If you don't accomplish all
of these, it is OK.

1. Optional: Go through the process above.  Start a change, create new
  branch and store your changes.  Go back to master and fix something
  else.  Resume your work and merge the new branch.
2. Discuss how to resume your former work.  Can you git rid of a branch?
  Continue using it?  etc.

---

## Storing various junk you don't need but don't want to get rid of

It happens often that you do something and don't need it, but you don't want
to lose it right away.  You can use either of the above strategies to
stash/branch it away: using branches is probably better.  Note that if you
try to use a branch after a long time, conflicts might get really bad
but at least you have the data still.
