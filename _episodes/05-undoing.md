---
layout: episode
title: Undoing things
teaching: 10
exercises: 10
questions:
  - How can I undo things?
---

## Undoing things

- Commits that are part of any branch will not get lost.
- Files which were added and later removed can always be recovered.
- In Git we can modify, reorder, squash, and remove commits and also these actions can be undone.
- Some commands can permanently delete **uncommitted** changes. In doubt always commit first.
- Some commands **modify history**. This is OK for local commits but may not be OK for commits shared
  with others.

---

### Reverting commits

- Imagine we made a couple of commits.
- We realize that commit `f960dd3` was a mistake and we wish to undo it:

```
$ git log --oneline

52e5998 (HEAD -> master) another tasty ingredient
f960dd3 not sure this is a good idea
40fbb90 draft a readme
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
52e5998 another tasty ingredient
f960dd3 not sure this is a good idea
40fbb90 draft a readme
dd4472c we should not forget to enjoy
2bb9bb4 add half an onion
2d79e7e adding ingredients and instructions
```

Exercise:

- Create a commit.
- Revert the commit with `git revert`.
- Inspect the history with `git log --oneline`.
- Now try `git show` on both the reverted and the newly created commit.

---

### Adding to the previous commit

Sometimes we commit but realize we forgot something.
We can amend to the last commit:

```shell
$ git commit --amend
```

This can also be used to modify the last commit message.

Note that this **will change the commit hash**. This command **modifies the history**.
This means that we never use this command on commits that we have shared with others.

---

### Unstage a file.
We will edit the `instructions.txt` file to remove the text "enjoy!". Then stage
it. Then we want to unstage it so we can edit it more before committing.

Open the file  instructions.txt file and remove the line “enjoy !”

```shell
$ git status                # to confirm what has changed
$ git diff                  # to view what was changed
$ git add instructions.txt  # stage it
$ git status                # to confirm what has staging
$ git reset instructions.txt
$ git status                # will show the file as unstaged
```

**Effect**: `instructions.txt` gets unstaged (reverting the `git add` command), but our change is still there and we can keep
working.)

### Un-modify a file.
Let’s say we want to get rid of the changes we did to the `instructions.txt` file.

```shell
$ git diff #To view the differences
$ git checkout instructions.txt
$ git status # To view the effect on the status
```

**Effect**: This will replace the current version with the last committed version. This action
will result in loss of all the edits after the last commit and can not be undone.

There is much more to discuss on undoing things and we leave them for later after we
learn about branches.

## Exercise: undo unstaged changes

- Make some changes to `ingredients.txt` (e.g. add liquorice).
- Inspect the changes with `git status` and `git diff`.
- Undo the unstaged changes with `git checkout ingredients.txt`.
- Inspect the new situation with `git status` and `git diff`.


### Questions

- What happens if you accidentally remove a tracked file with `git rm`, is it gone forever?
- What situations would justify to modify the Git history and possibly remove commits?
- Is it OK to modify commits that nobody has seen yet?
