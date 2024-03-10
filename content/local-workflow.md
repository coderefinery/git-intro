# Cloning a Git repository and working locally

If you've been following the main flow, you have just had interacted
with repositories on GitHub.  Of course, this isn't what you usually
do, so now we move to working on your own computer.

```{objectives}
- We are able to clone and modify a repository from the web.
- We can do the same things we did before (commit, branch, merge), but locally.
- We get a feeling for remote repositories ([more later](https://coderefinery.github.io/git-collaborative/)).
```

```{instructor-note}
- 10 min introduction and setup
- 25 min exercise
- 15 min discussion
```

```{highlight} console
```

## What is in a Git repository and what are we cloning?

**Git repository**:
- Contains all the files and directories of a project.
- Contains the complete history of all changes (commits) to these files and directories.
- Each commit is a snapshot of the entire project at a certain point in time and has a unique identifier ("hash").
- Sometimes it contains multiple branches and tags.

**Cloning**:
- Copying (downloading) the entire repository with all commits, branches, and tags to your computer.
- It is a full backup of the repository, including all history.
- You can then work on your local clone.
- Changes on local clone will not automatically appear in the original
  repository. We have to actively "push" them there (we will practice this in a
  later episode).


## Basics

- What is VS Code and what is the command line?
- How to choose.
- Command line still needed sometimes in VS Code.  Show how it can be
  accessed (for the most part you just paste in what you need).


## Exercise

Work on this by yourself or in your teams.  This should seem familiar,
from the browser-based exercises we did yesterday.

We offer the **Command Line and VS Code** flows for this exercise. (On
GitHub isn't an option here, since that is what we already
demonstrated in {doc}`commits` and {doc}`merging`.)

```{exercise} Exercise: Cloning a Git repository and working locally (25 min)
1. Configure Git command line and editor (see the "solution" above for instructions).
1. Clone the recipe book.
1. Create a new branch.
1. Make a commit on your new branch.
1. Switch back to the `main` branch and create one or two commits there.
1. Merge the new branch into `main`.
1. Compare the graph locally and on GitHub and observe that the changes only exist locally on your computer.
```

The solution below goes over most of the answer and should be used as
your guide (you can't figure it out just from the exercise instructions).



## Solution



### (2) Cloning a repository

Now other people can clone this repository and contribute changes. In the
[collaborative distributed version control](https://coderefinery.github.io/git-collaborative/) lesson
we will learn how this works.

At this point only a brief demo - if you copy the SSH or HTTPS address, you can clone repositories like this
(again adapt the `USER` in the "USER/repository.git" part):


:::::{tabs}
::::{group-tab} Command line: SSH
```console
$ git clone git@github.com:USER/recipe.git
```

**From now on, if you are using SSH, you should pay attention and make
sure your clone URLs start with `git@github.com:` now and in future
lessons.**
::::
::::{group-tab} Command line: HTTPS
```console
$ git clone https://github.com/USER/recipe.git
```

**From now on, if you are using HTTPS, you should pay attention and make
sure your clone URLs start with `https://github.com/` now and in future
lessons.**
::::
:::::

This creates a directory called "recipe" unless it already exists. You can also specify the target directory
on your computer:

:::::{tabs}
::::{group-tab} Command line: SSH
```console
$ git clone git@github.com:USER/recipe.git myrecipe
```
::::
::::{group-tab} Command line: HTTPS
```console
$ git clone https://github.com/user/recipe.git myrecipe
```
::::
:::::



### (3) Creating branches locally

:::::{tabs}
::::{group-tab} Command line
::::

::::{group-tab} VS Code
::::
:::::



### (4) Creating commits locally

:::::{tabs}
::::{group-tab} Command line
::::

::::{group-tab} VS Code
::::
:::::



### (5) Creating commits locally on `main`

:::::{tabs}
::::{group-tab} Command line
::::

::::{group-tab} VS Code
::::
:::::



### (6) Merging branches locally

:::::{tabs}
::::{group-tab} Command line
::::

::::{group-tab} VS Code
::::
:::::



### (7) How to compare the graph locally and on GitHub

:::::{tabs}
::::{group-tab} Command line
::::

::::{group-tab} VS Code
::::
:::::



## Summary
