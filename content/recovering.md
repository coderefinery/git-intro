# Undoing and recovering

```{objectives}
- Learn to undo changes safely
- See when undone changes are permanently deleted and when they can be retrieved
```

```{instructor-note}
- 10 min teaching/type-along
- 15 min exercise
```

One of the main points of version control is that you can *go back in
time to recover*.  Unlike this xkcd comic implies: <https://xkcd.com/1597/>

In this episode we show a couple of commands that can be used to undo mistakes.
We also list a couple of common mistakes and discuss how to recover from them.
Some commands preserve the commit history and some modify commit history.
Modifying history? Isn't a "commit" permanent?

- You can modify old commit history.
- But if you have shared that history already, *modifying it can make
  a huge mess*.

```{note}
As long as you commit something once (or at least `git add` it), you
can almost always go back to it, no matter what you do.
But you may need to ask Stack Overflow or your local
guru... *until that guru becomes you*.
```

---

## Undoing your recent, uncommitted and unstaged changes (preserves history)

You do some work, and want to **undo your uncommitted and unstaged modifications**.
You can always do that with:

- `git restore .`: (the dot means "here and in all folders below")

Or, you can undo things selectively:

- `git restore -p` (decide which portions of changes to undo) or `git restore <path>` (decide which path/file)

```{note}
In case the above does not work, your Git version might be older than from 2019.
On older Git it is `git checkout` instead of `git restore`.
```

If you have staged changes, you have at least two options to undo the staging:
- `git restore --staged .` followed by `git status` and `git restore .`
- `git reset --hard HEAD` throws away everything that is not in last commit (`HEAD`)

---

## Reverting commits (preserves history)

- Imagine we made a few commits.
- We realize that the latest commit `f960dd3` was a mistake and we wish to undo it:
```console
$ git log --oneline

f960dd3 (HEAD -> master) not sure this is a good idea
dd4472c we should not forget to enjoy
2bb9bb4 add half an onion
2d79e7e adding ingredients and instructions
```

A safe way to undo the commit is to revert the commit with `git revert`:
```console
$ git revert f960dd3
```

This creates a **new commit** that does the opposite of the reverted commit.
The old commit remains in the history:
```console
$ git log --oneline

d62ad3e (HEAD -> master) Revert "not sure this is a good idea"
f960dd3 not sure this is a good idea
dd4472c we should not forget to enjoy
2bb9bb4 add half an onion
2d79e7e adding ingredients and instructions
```

You can revert any commit, no matter how old it is.  It doesn't affect
other commits you have done since then - but if they touch the same
code, you may get a conflict (which we'll learn about later).

(exercise-revert)=

### Exercise: Revert a commit

```{exercise} Undoing-1: Revert a commit
- Create a commit.
- Revert the commit with `git revert`.
- Inspect the history with `git log --oneline`.
- Now try `git show` on both the reverted and the newly created commit.
```


## Adding to the previous commit (modifies history)

Sometimes we commit but realize we forgot something.
We can amend to the last commit:

```console
$ git commit --amend
```

This can also be used to modify the last commit message.

Note that this **will change the commit hash**. This command **modifies the history**.
This means that we avoid this command on commits that we have shared with others.

(exercise-amend)=

### Exercise: Modify a previous commit

````{exercise} Undoing-2: Modify a previous commit
1. Make an incomplete change to the recipe or a typo in your change, `git
   add` and `git commit` the incomplete/unsatisfactory change.
2. Inspect the unsatisfactory but committed change with `git show`. Remember
   or write down the commit hash.
3. Now complete/fix the change but instead of creating a new commit, add the
   correction to the previous commit with `git add`, followed by `git commit
   --amend`.  What changed?

  ```{solution}
  One thing that has changed now is the commit hash. Modifying the previous
  commit has changed the history. This is OK to do on commits that other people
  don't depend on yet.
  ```
````


## Rewinding branches (modifies history)

You can **reset branch history** to move your branch back to some
point in the past.

* `git reset --hard <hash>` will force a branch label to any other point.  All
  other changes are lost (but it is possible to recover if you force reset by mistake).
* Be careful if you do this - it can mess stuff up.  Use `git graph` a
  lot before and after.


(exercise-reset)=

### Exercise: Git reset

````{exercise} Undoing-3: Destroy our experimentation in this episode
  After we have experimented with reverts and amending, let us destroy
  all of that and get our repositories to a similar state.

  - First, we will look at our history (`git log`/`git graph`) and
    find the last commit `<hash>` before our tests.
  - Then, we will `git reset --hard <hash>` to that.
  - Then, `git graph` again to see what happened.

  ```console
  $ git log --oneline

  d62ad3e (HEAD -> master) Revert "not sure this is a good idea"
  f960dd3 not sure this is a good idea
  dd4472c we should not forget to enjoy
  2bb9bb4 add half an onion
  2d79e7e adding ingredients and instructions

  $ git reset --hard dd4472c

  HEAD is now at dd4472c we should not forget to enjoy

  $ git log --oneline

  dd4472c (HEAD -> master) we should not forget to enjoy
  2bb9bb4 add half an onion
  2d79e7e adding ingredients and instructions
  ```
````

---

## Recovering from committing to the wrong branch

It is easy to forget to create a branch or to create it and forget to switch to
it when committing changes.

Here we assume that we made a couple of commits but we realize they went to the
wrong branch.

**Solution 1 using git cherry-pick**:
1. Make sure that the correct branch exists and if not, create it. Make sure to
   create it from the commit hash where you wish you had created it from: `git
   branch <branchname> <hash>`
2. Switch to the correct branch.
3. `git cherry-pick <hash>` can be used to take a specific commit to the
   current branch. Cherry-pick all commits that should have gone to the correct
   branch, **from oldest to most recent**.
4. Rewind the branch that accidentally got wrong commits with `git reset --hard` (see also above).

**Solution 2 using git reset --hard** (makes sense if the correct branch should
contain all commits of the accidentally modified branch):
1. Create the correct branch, pointing at the latest commit: `git branch <branchname>`.
2. Check with `git log` or `git graph` that both branches point to the same, latest, commit.
3. Rewind the branch that accidentally got wrong commits with `git reset --hard` (see also above).


## Recovering from merging/pulling into the wrong branch

`git merge`, `git rebase`, and `git pull` modify the **current** branch, never
the other branch. But sometimes we run this command on the wrong branch.

1. Check with `git log` the commit hash that you would like to rewind the
   wrongly modified branch to.
2. Rewind the branch that accidentally got wrong commits with `git reset --hard <hash>` (see also above).


## Recovering from conflict after git pull

`git pull` can create a conflict since `git pull` always also includes a `git merge` (more about this
in the [collaborative Git lesson](https://coderefinery.github.io/git-collaborative/)).

The recovery is same as described in {ref}`conflict-resolution`. Either
resolve conflicts or abort the merge with `git merge --abort`.

---

````{challenge} Undoing-4: Test your understanding
  1. What happens if you accidentally remove a tracked file with `git rm`, is it gone forever?
  2. Is it OK to modify commits that nobody has seen yet?
  3. What situations would justify to modify the Git history and possibly remove commits?

  ```{solution}
  1. It is not gone forever since `git rm` creates a new commit. You can simply revert it!
  2. If you haven't shared your commits with anyone it can be alright to modify them.
  3. If you have shared your commits with others (e.g. pushed them to GitHub), only extraordinary
     conditions would justify modifying history. For example to remove sensitive or secret information.
  ```
````
