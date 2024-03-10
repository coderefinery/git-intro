# Cloning a Git repository and working locally

If you've been following the main path, you have just had interacted
with repositories on GitHub. This might not be what you usually
do, so now we move to working on your own computer.

:::{objectives}
- We are able to clone and modify a repository from the web.
- We can do the same things we did before (commit, branch, merge), but locally.
- We get a feeling for remote repositories ([more later](https://coderefinery.github.io/git-collaborative/)).
:::

:::{instructor-note}
- 10 min introduction and setup
- 25 min exercise
- 15 min discussion
:::


## What is in a Git repository and what are we cloning?

**Git repository**:
- Contains all the files and directories of a project.
- Contains the complete history of all changes (commits) to these files and directories.
- Each commit is a snapshot of the entire project at a certain point in time and has a unique identifier ("hash").
- Sometimes it contains multiple branches and tags.

**Cloning**:
- Copying (downloading) the entire repository with all commits, branches, and tags to your computer.
- It is a full backup of the repository, including all history.
- You can then work on your local clone of the repository.
- Changes on local clone will not automatically appear in the repository where
  we cloned from. We have to actively "push" them there (we will practice this
  in a later episode: {ref}`sharing-repositories`).


## Exercise

Work on this by yourself or in your teams. Conceptually this episode should
seem familiar, from the browser-based exercises we did yesterday.

We offer the **Command Line and VS Code** paths for this exercise.
GitHub isn't an option in this episode, since that is what we already
demonstrated in {doc}`commits` and {doc}`merging` and since the point of this
episode is to work locally.

It is also possible to use the command line (terminal) from inside VS Code.

```{exercise} Exercise: Cloning a Git repository and working locally (25 min)
1. {ref}`Configure Git command line and editor <configuration>` if you haven't done that already.
1. **Decide which repository you want to clone**: your fork or the original repository? Both will work for this exercise.
   Then, **clone the recipe book**.
1. **Create a new branch**.
1. Make a **commit** on your new branch.
1. **Switch** back to the `main` branch and create one or two commits there.
1. **Merge** the new branch into `main`.
1. Compare the graph locally and on GitHub and observe that the **changes only exist locally on your computer**.
1. Where are the **remote branches**? Practice how you can see all remote branches
   also locally and how you can fetch them and make local changes to them.
```

The solution below goes over most of the answer and should be used as
your guide (you can't figure it out just from the exercise instructions).


## Solution and walk-through


### (1) Configure Git command line and editor

We have an own section for this: {ref}`configuration`.


### (2) Cloning a repository

Now you need to decide which repository you want to clone. All of these options will work for this exercise
since we don't plan to push changes back (for step 8 it might be easier to use the original repository):
- Clone the recipe book from your fork.
- Or clone the recipe book from the original repository: <https://github.com/coderefinery/recipe-book>
- Or first fork the original repository and then clone your fork.

The examples below assume you are cloning the original repository. If you are cloning your fork, you should
replace `coderefinery` with your GitHub username.

:::::::{tabs}
::::::{group-tab} Command line
If you are unsure whether you are using SSH or HTTPS, please read {ref}`clone-method`.
  :::::{tabs}
    ::::{group-tab} SSH
      ```console
      $ git clone git@github.com:coderefinery/recipe-book.git
      ```
    ::::

    ::::{group-tab} HTTPS
      ```console
      $ git clone https://github.com/coderefinery/recipe-book.git
      ```
    ::::
  :::::

This creates a directory called "recipe-book" unless it already exists. You can also specify the target directory
on your computer (in this case "my-recipe-book"):
  :::::{tabs}
    ::::{group-tab} SSH
      ```console
      $ git clone git@github.com:coderefinery/recipe-book.git my-recipe-book
      ```
    ::::

    ::::{group-tab} HTTPS
      ```console
      $ git clone https://github.com/coderefinery/recipe-book.git my-recipe-book
      ```
    ::::
  :::::
::::::

::::::{group-tab} VS Code
::::::
:::::::


### (3) Creating branches locally

:::::{tabs}
::::{group-tab} Command line
Create a new branch called `another-recipe` from `main` and switch to it:
```console
$ git switch --create another-recipe main
```
::::

::::{group-tab} VS Code
::::
:::::


### (4) Creating commits locally

:::::{tabs}
::::{group-tab} Command line
Create a new file. **After we have created it**, we can stage and commit
the change:
```console
$ git add new-file.md
$ git commit -m "Short summary of the change"
```

Make sure to replace "new-file.md" with the actual name of the file you created
and to replace "Short summary of the change" with a meaningful commit message.
::::

::::{group-tab} VS Code
::::
:::::


### (5) Switching branches and creating commits

:::::{tabs}
::::{group-tab} Command line
First switch to the `main` branch:
```console
$ git switch main
```

Then modify a file. Finally `git add` and then commit the change:
```console
$ git commit -m "Short summary of the change"
```
::::

::::{group-tab} VS Code
::::
:::::


### (6) Merging branches locally

:::::{tabs}
::::{group-tab} Command line
On the command line, when we merge, we always modify our current branch.

If you are not sure anymore what your current branch is, type:
```console
$ git branch
```

In this case we merge the `another-recipe` branch into our current branch:
```console
$ git merge another-recipe
```
::::

::::{group-tab} VS Code
::::
:::::


### (7) How to compare the graph locally and on GitHub

:::::{tabs}
::::{group-tab} Command line
```console
$ git log --graph --oneline --decorate --all
```

Compare this with the graph on GitHub: Insights tab → Network view (just like
we have done before).

The result is that we should not be able to see the new branch and the new
commits on GitHub.
::::

::::{group-tab} VS Code
::::
:::::


### (8) Browsing remote branches and creating local branches from them

:::::{tabs}
::::{group-tab} Command line
With `git branch` you can list all local branches:
```console
$ git branch

  another-recipe
* main
```

But where are the remote branches? We expect to see [a couple of
them](https://github.com/coderefinery/recipe-book/branches/all).

We can see them by asking for all branches (your output might vary depending on
where you cloned from):
```console
$ git branch --all

  another-recipe
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/alex/fruit-salad
  remotes/origin/main
  remotes/origin/radovan/lasagna
  remotes/origin/radovan/poke
```

You can create a local branch from a remote branch which will "track" the remote branch.
For instance, to create a local branch `alex/fruit-salad` from the remote branch `origin/alex/fruit-salad`
and switch to it, you can do:
```console
$ git switch --create alex/fruit-salad origin/alex/fruit-salad
```

This shortcut will do the same thing:
```console
$ git switch --track origin/alex/fruit-salad
```

Or even shorter:
```console
$ git switch alex/fruit-salad
```

If you want to create a branch and not switch to it, you can use `git branch`.
```console
$ git branch alex/fruit-salad
```
::::

::::{group-tab} VS Code
::::
:::::


## Summary

- When we clone a repository, we get a full backup of the repository, including all history.
- Yesterday we learned about branches and commits, and now we created and used them locally.
- Creating local branches and commits does not automatically modify the remote
  repository. To "push" our local changes to the remote repository, we have to actively
  "push" them there. We will practice this in a later episode:
  {ref}`sharing-repositories`
- Remote branches and local branches are not the same thing. If we want to
  create local commits, we always need to create a local branch first. But the local branch can
  "track" the remote branch and we can push and pull changes to and from the
  remote branch.
