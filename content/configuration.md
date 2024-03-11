(configuration)=

# Configuring Git command line and editor

We have a longer version of this in the [installation
instructions](https://coderefinery.github.io/installation/git-in-terminal/).
But for clarity, we will review the most important parts here.

You don't need to set these if you work only through the GitHub web interface.
If you use VS Code, the editor might prompt you to set these up.

These configuration settings are saved in a file called `.gitconfig` in your
home directory. If this file exists, editors like VS Code will use this
configuration.

If you want to see your configuration settings, you can use the
command (`--show-origin` means it shows the file *where* each setting
is defined):
```console
$ git config --list --show-origin
```


## Name and email address for Git commit metadata

Git commits carry metadata about the author and two things you will always need
to define somewhere are:
```console
$ git config --global user.name "Your Name"
$ git config --global user.email yourname@example.com
```

For the email address we recommend to use the one you use for your GitHub account.
If you prefer to not use it, you can instead use
`YOUR_GITHUB_USERNAME@users.noreply.github.com` as the email address.
This means that nobody can write to this email address, but GitHub will still
be able to connect your contributions with your GitHub account.

(Note that these can, in theory, be anything: this is just data, not a
registration or identity requirement.)


## Default branch name

The default branch name in Git has been `master` for a long time, but it is
changing to `main` in many places.  We recommend to set it to `main`:
```console
$ git config --global init.defaultbranch main
```


## Useful alias for the command line

We recommend to define an {term}`alias` in Git, to be able to nicely visualize
branch structure in the terminal without having to remember a long Git command
(more details about aliases are given in a later section). This is extensively
used in the rest of this and other lessons:
```console
$ git config --global alias.graph "log --all --graph --decorate --oneline"
```

We have an own section about aliases: {ref}`aliases`.


## Default text editor for commit messages

Git sometimes needs to start a text editor for you to enter messages.
This may have already been set to something (like VS Code), but if not
`nano` is usually a safe choice:

```console
$ git config --global core.editor nano
```

See `the installation instructions text editor page
<https://coderefinery.github.io/installation/editors/>`__ gives ways
to set other editors, or do a web search for "git set editor to
[editor name]".


% This anchor used for linking from other lessons
(clone-method)=

## Authenticating to GitHub: SSH or HTTPS or VS Code?

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

    From now on, you should **Select HTTPS as the clone URL from
    GitHub, or translate the URL to start with the right thing
    yourself:** `https://github.com/`

    If you don't want VS Code to be connected to your GitHub account,
    set up and use the SSH method instead.
  ::::
:::::
