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

### Undo unstaged/uncommitted changes

This is a command that **permanently deletes** changes
that were unstaged/uncommitted!

Exercise: Modify without staging

- Make a silly change to a project, do not stage it or commit it.
- Inspect the change with `git status` and `git diff`.
- Now undo the change with `git checkout <file>`.
- Verify that the change is gone with `git status` and `git diff`.

Exercise: Modify after staging

- Make a reasonable change to a project, stage it.
- Make a silly change after you have staged the reasonable change.
- Inspect the situation with `git status`, `git diff`, `git diff --staged`, and `git diff HEAD`.
- Now undo the silly change with `git checkout <file>`.
- Inspect the new situation with `git status`, `git diff`, `git diff --staged`, and `git diff HEAD`.

---

### Questions

- What happens if you accidentally remove a tracked file with `git rm`, is it gone forever?
- What situations would justify to modify the Git history and possibly remove commits?
- Is it OK to modify commits that nobody has seen yet?
