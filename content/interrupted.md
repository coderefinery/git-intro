# Interrupted work

```{objectives}
- Learn to switch context or abort work without panicking.
```

```{instructor-note}
- 10 min teaching/type-along
- 15 min exercise
```

```{keypoints}
- There is almost never reason to clone a fresh copy to complete a task that
  you have in mind.
```


## Frequent situation: interrupted work

We all wish that we could write beautiful perfect code. But the real world is
much more chaotic:

- You are in the middle of a "Jackson-Pollock-style" debugging spree with 27 modified files
  and debugging prints everywhere.
- Your colleague comes in and wants you to fix/commit something right now.
- What to do?

Git provides lots of ways to switch tasks without ruining everything.


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

(exercise-stashing)=

### Exercise: Stashing

````{exercise} Interrupted-1: Stash some uncommitted work
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

```{solution}
5: Yes you can. With `git stash pop <index>` you can decie which stash
index to pop.

6: In this case Git will ask us to resolve the conflict the same way
when resolving conflicts between two branches.

7: It shows an additional commit hash with `refs/stash`.
```
````


## Option 2: Create branches

You can use branches almost like you have already been doing if you
need to save some work.  You need to do something else for a bit?
Sounds like a good time to make a feature branch.

You basically know how to do this:

```shell
$ git checkout -b temporary  # create a branch and switch to it
$ git add <paths>            # stage changes
$ git commit                 # commit them
$ git checkout main          # back to main
                             # do your work...
$ git checkout temporary     # continue where you left off
```

Later you can merge it to main or rebase it on top of main and resume work.


## Storing various junk you don't need but don't want to get rid of

It happens often that you do something and don't need it, but you don't want to
lose it right away.  You can use either of the above strategies to stash/branch
it away: using branches is probably better because branches are less easily
overlooked if you come back to the repository in few weeks.  Note that if you
try to use a branch after a long time, conflicts might get really bad but at
least you have the data still.
