# Cloning a Git repository and working locally

```{objectives}
- We are able to clone and modify a repository from the web.
- We get a feeling for remote repositories ([more later](https://coderefinery.github.io/git-collaborative/)).
```

```{instructor-note}
- 10 min introduction and setup
- 25 min exercise
- 15 min discussion
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


## Exercise

Work on this by yourself. The solution below goes over most of the
answers, but the hints should get you most of the way. Refer to the
solution if you get stuck.

We offer **two different flows** of how to do this exercise.

```{exercise} Exercise: Cloning a Git repository and working locally (25 min)
1. Configure Git command line and editor (see below).
1. Clone the recipe book.
1. Create a new branch and make a commit there.
1. Switch back to the `main` branch and create one or two commits there.
1. Merge the new branch into `main`.
1. Compare the graph locally and on GitHub and observe that the changes only exist locally on your computer.
```


## Configuring Git command line and editor

write me ...


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

`````{tabs}
  ````{group-tab} Command line: SSH
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
    the right thing yourself:** `git@github.com:` (with the trailing
    `:`).
  ````

  ````{group-tab} Command line: HTTPS
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
  ````

  ````{group-tab} VS Code
    VS Code has its own authentication method and the editor will guide you
    through the process. If you are using VS Code, you can skip the SSH and
    HTTPS checks.
  ````
`````

If you do not have these configured, please watch as we do this episode and you
can check the [installation
instructions](https://coderefinery.github.io/installation/ssh/)
before the next [collaborative Git
lesson](https://coderefinery.github.io/git-collaborative/), where we will need
one of these set up.



## Cloning a repository

Now other people can clone this repository and contribute changes. In the
[collaborative distributed version control](https://coderefinery.github.io/git-collaborative/) lesson
we will learn how this works.

At this point only a brief demo - if you copy the SSH or HTTPS address, you can clone repositories like this
(again adapt the `USER` in the "USER/repository.git" part):


`````{tabs}
````{group-tab} Command line: SSH
```console
$ git clone git@github.com:USER/recipe.git
```

**From now on, if you are using SSH, you should pay attention and make
sure your clone URLs start with `git@github.com:` now and in future
lessons.**
````
````{group-tab} Command line: HTTPS
```console
$ git clone https://github.com/USER/recipe.git
```

**From now on, if you are using HTTPS, you should pay attention and make
sure your clone URLs start with `https://github.com/` now and in future
lessons.**
````
`````

This creates a directory called "recipe" unless it already exists. You can also specify the target directory
on your computer:

`````{tabs}
````{group-tab} Command line: SSH
```console
$ git clone git@github.com:USER/recipe.git myrecipe
```
````
````{group-tab} Command line: HTTPS
```console
$ git clone https://github.com/user/recipe.git myrecipe
```
````
`````


## Creating commits locally



## Creating branches locally



## Merging branches locally



## How to compare the graph locally and on GitHub



## Summary
