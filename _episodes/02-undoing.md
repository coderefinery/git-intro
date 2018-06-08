---
layout: episode
title: Undoing things
teaching: 15
exercises: 20
questions:
  - How can I undo things?
---

## Undoing things

As emphasized above, Git can go back to any historical version of tracked files.
In this section we will learn the basics of the available methods.
In general, almost all Git actions *add* data and it's difficult to do anything
irreversible or to remove data permanently.
However, please be warned that *some* commands discussed below
will result in permanent data loss and should be used with caution. 

Without going into technical details, we will have a look at
selected examples to show how to undo or modify certain tasks. 
The diagram below shows what we did with the
guacamole recipe and we will see how to undo some changes.

![Git events]({{ site.baseurl }}/img/events.svg
"git events"){:class="img-responsive" style="max-width:70%"}

### Change the commit message

The comment we added in the last stage (3) had the message “added enjoy”.
Immediately after we committed and  before any file has been changed we want to
change this message to "do not forget to enjoy".  To achieve this we
issue the following command. Please note that you should not do this if you
have already pushed to a remote repository (will learn later).

```shell
$ git commit --amend
```

This will give you a chance to edit the commit message.

**Effect**: The new commit will replace the old one. It's as if the previous commit
never happened, and it won't show up in your repository history.

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


## Be considerate when modifying committed changes

Indeed, Git lets you do marvelous things with history. This is all fine and well as
long as you are modifying commits that you are not sharing with others. When
you start collaborating with other people it
will cause a lot of grief to others if you change things that are already
public and have been used.

In short: **if you change commits that other people depend on, you will lose friends!**

More in this after we learn Git remotes.

### Questions

- A safe way to undo past commits is to use `git revert`. What does it do? In doubt, try it.
- What happens if you accidentally remove a tracked file with `git rm`, is it gone forever?
- What situations would justify to modify the Git history and possibly remove commits?
- Is it OK to modify commits that nobody has seen yet?
