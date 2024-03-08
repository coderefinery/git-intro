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

- What is VS Code and command line
- Command line still needed sometimes in VS Code.  Show how it can be
  accessed.



% This anchor used for linking from other lessons
(clone-method)=

## Authenticating to GitHub: SSH or HTTPS using VS Code?

**How does GitHub know who you are?** There are three options.

- **SSH** is the classic method, using [Secure Shell
  Protocol](https://en.wikipedia.org/wiki/Secure_Shell) remote connection
  keys.
- **HTTPS** works with the **Git Credential Manager**, which is an
  extra add-on that works easily in Windows and Mac.
- **VS Code** editor can authenticate with GitHub using its own
  authentication method.

Read how to install them from the [installation
instructions](https://coderefinery.github.io/installation/ssh/).

Test which one you should use:

:::::{tabs}
  ::::{group-tab} Command line: SSH
    Try this command:
    ```console
    $ ssh -T git@github.com
    ```

    If it returns `Hi USERNAME! You've successfully authenticated, ...`,
    then SSH is configured and the following steps will work with the SSH
    cloning.

    See our [installation
    instructions](https://coderefinery.github.io/installation/ssh/) to
    set up SSH access.

    **From now on, if you know that SSH works, you should always select
    SSH as the clone URL from GitHub, or translate the URL to start with
    the right thing yourself:** `git@github.com:` (with the `:`).
  ::::

  ::::{group-tab} Command line: HTTPS
    Try this command:
    ```console
    $ git config --get credential.helper
    ```

    If this shows something, then the credential manager is probably
    configured and HTTPS cloning will work (but you can't verify it until
    you try using it).

    From now on, **if you know that HTTPS works, you should always select
    HTTPS as the clone URL from GitHub, or translate the URL to start with
    the right thing yourself:** `https://github.com/`
  ::::

  ::::{group-tab} VS Code
    VS Code has its own authentication method and the editor will guide you
    through the process. If you are using VS Code, you can skip the SSH and
    HTTPS checks.
  ::::
:::::

If you do not have these configured, you can use HTTPS for cloning
(but not for pushing).  Please watch as we do this episode and you can
check the [installation
instructions](https://coderefinery.github.io/installation/ssh/) when
you have time.  We are sorry that things may not work perfectly.  Make
sure you work on the install instructions and before tomorrow's
[collaborative Git
lesson](https://coderefinery.github.io/git-collaborative/), where we
will need one of these set up.



## (1) Configuring Git command line and editor

There is some basic work to be done, which might have been done in the
[installation
instructions](https://coderefinery.github.io/installation/git-in-terminal/).
But for clarity, we will review the most important parts now.

The most basic configuration that is always needed is your name and
email address (instead of your email address, you could use
`YOUR_GITHUB_USERNAME@users.noreply.github.com`).

```
$ git config --global user.name "Your Name"
$ git config --global user.email yourname@example.com
```

We will now define an {term}`alias` in Git, to be able to nicely visualize
branch structure in the terminal without having to remember a long Git
command (more details about aliases are given in a later
section). This is extensively used in the rest of this and other
lessons.  The second line sets the default branch name:
```
$ git config --global alias.graph "log --all --graph --decorate --oneline"
$ git config --global init.defaultbranch main
```

Git sometimes needs to start a text editor for you to enter messages.
This may have already been set to something (like VS Code), but if not
`nano` is usually a safe choice:

```
$ git config --global core.editor nano
```



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
