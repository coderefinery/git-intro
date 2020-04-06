---
layout: episode
title: Undoing things
teaching: 10
exercises: 10
questions:
  - How can I undo things?
objectives:
  - Learn to undo changes safely
  - See when undone changes are permanently deleted and when they can be retrieved
---

## Undoing and recovering

One of the main points of version control is that you can *go back in
time to recover*.  Unlike this xkcd comic implies: https://xkcd.com/1597/

This lesson covers four types of undoing:

- Go back to your last commit, remove all latest changes.
- Selectively revert one commit, without modifying history (`git revert`).
- Change a commit *right* after it's been done (`git commit --amend`).
- Rewind in time to a previous commit (`git reset --hard`).

Your instructor will choose two to do two in this lesson.

> ## Discussion: undoing
>
> When have you made a change, and had to go through much more trouble
> to figure out what you did, or fix it?
>
{: .challenge}



---

## Undoing your recent, uncommitted changes

You do some work, and want to **undo everything** and go back to your
last commit.  You can always do that with:

* `git checkout -f master`: go back to master, no
  matter what.

Or, you can undo things selectively, as you have already learned:

* `git checkout -p` or `git checkout $file` (working dir)
* `git reset -p` or `git reset $file` (staging area)

> ## Clear your workspace
>
> - If you have unstaged changes from earlier sections, remove them
>   and get a clean working directory.
> - `git status` should report nothing.
>
{: .callout}

*Note: we've seen some time when `git checkout -f master` doesn't
work.  Can you figure out when?  If it doesn't work, try `git reset
--hard HEAD`.*



---

## Reverting commits

- Imagine we made a few commits.
- We realize that the latest commit `f960dd3` was a mistake and we wish to undo it:

```
$ git log --oneline

f960dd3 (HEAD -> master) not sure this is a good idea
dd4472c we should not forget to enjoy
2bb9bb4 add half an onion
2d79e7e adding ingredients and instructions
```

A safe way to undo the commit is to revert the commit with `git revert`:

```
$ git revert f960dd3
```

This creates a **new commit** that does the opposite of the reverted commit.
The old commit remains in the history:

```
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

> ## Exercise: Revert a commit
>
> - Create a commit.
> - Revert the commit with `git revert`.
> - Inspect the history with `git log --oneline`.
> - Now try `git show` on both the reverted and the newly created commit.
{: .challenge}






## (optional) Modifying history

Modifying history?  Isn't a "commit" permanent?

- No, you can modify old history.
- But if you have shared that history already, *modifying it will make
  a huge mess*.

The following two commands are dangerous if you use them without
being careful.  Use them only before you have pushed commits, until
you have more practice!



---

## (optional) Adding to the previous commit

Sometimes we commit but realize we forgot something.
We can amend to the last commit:

```shell
$ git commit --amend
```

This can also be used to modify the last commit message.

Note that this **will change the commit hash**. This command **modifies the history**.
This means that we never use this command on commits that we have shared with others.

> ## Exercise: Modify a previous commit
>
> 1. Make an incomplete change to the recipe or a typo in your change, `git add` and `git commit` the incomplete/unsatisfactory change.
> 2. Inspect the unsatisfactory but committed change with `git show`.  Remember the commit hash.
> 3. Now complete/fix the change but instead of creating a new commit, add to the previous commit with `git commit --amend`.  What changed?
{: .challenge}



---

## (optional) Rewind history

You can **reset branch history** to move your branch head back to some
point in the past.

* `git reset --hard $commit` will force a branch head to any other point.  All
  other changes are lost.
* Be careful if you do this - it can mess stuff up.  Use `git graph` a
  lot before and after.

> ## Exercise: Destroy our experimentation in this episode
>
> After we have experimented with reverts and amending, let us destroy
> all of that and get our repositories to a similar state.
>
> - First, we will look at our history (`git log`/`git graph`) and
>   find the last commit `$commit` before our tests.
> - Then, we will `git reset --hard $commit` to that.
> - Then, `git graph` again to see what happened.
>
> ```
> $ git log --oneline
>
> d62ad3e (HEAD -> master) Revert "not sure this is a good idea"
> f960dd3 not sure this is a good idea
> dd4472c we should not forget to enjoy
> 2bb9bb4 add half an onion
> 2d79e7e adding ingredients and instructions
>
> $ git reset --hard dd4472c
>
> HEAD is now at dd4472c we should not forget to enjoy
>
> $ git log --oneline
>
> dd4472c (HEAD -> master) we should not forget to enjoy
> 2bb9bb4 add half an onion
> 2d79e7e adding ingredients and instructions
> ```
>
{: .challenge}

---

> ## Test your understanding
>
> 1. What happens if you accidentally remove a tracked file with `git rm`, is it gone forever?
> 2. Is it OK to modify commits that nobody has seen yet?
> 3. What situations would justify to modify the Git history and possibly remove commits?
> 4. What is the difference between these commands?
>    ```shell
>    $ git diff
>    $ git diff --staged  # or git diff --cached
>    $ git diff HEAD
>    $ git diff HEAD^
>    ```
>
> > ## Solution
> >
> > 1. It is not gone forever since `git rm` creates a new commit. You can simply revert it!
> > 2. If you haven't shared your commits with anyone it can be alright to modify them.
> > 3. If you have shared your commits with others (e.g. pushed them to GitHub), only extraordinary
> >    conditions would justify modifying history. For example to remove sensitive or secret information.
> > 4. The different commands show changes between different file states:
> >    ```shell
> >    $ git diff          # Show what has changed but hasn't been staged yet via git add.
> >    $ git diff --staged # Show what has been staged but not yet committed.
> >    $ git diff HEAD     # Show what has changed since the last commit.
> >    $ git diff HEAD^    # Show what has changed since the commit before the latest commit.
> >    ```
> {: .solution}
{: .challenge}
