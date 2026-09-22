(configuration)=

# Configuring Git command line and editor

We have a longer version of this in the [installation
instructions](https://coderefinery.github.io/installation/git-in-terminal/).
But for clarity, we will review the most important parts here.

You don't need to set these if you work only through the GitHub or GitLab web interface.
If you use VS Code or other editors or integrated development environments,
the editor might prompt you to set these up. If you use RStudio, you can carry 
out the configuration in RStudio (see the RStudio tab in the section [Authenticating 
to GitHub or GitLab](clone-method)
below).

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

For the email address we recommend using the one associated with your GitHub
or GitLab account. If you prefer not to expose your personal email address,
you can instead use the privacy-preserving no-reply address provided by the
service:

- GitHub: Copy the exact address shown in your [email settings](https://github.com/settings/emails).
- GitLab: In your profile settings, select **Use a private email** as the commit email and copy the generated address.

The address may contain an account-specific ID, username, or other details, so
do not try to construct it yourself. This allows the service to connect your
contributions with your account without exposing your personal email address.

Note that these can, in theory, be anything: this is just data, not a
registration or identity requirement.


## Default branch name

The default branch name in Git has been `master` for a long time, but it is
changing to `main` in many places.  We recommend to set it to `main` for new
repositories that you create locally:
```console
$ git config --global init.defaultbranch main
```


## Useful alias for the command line

We recommend to define an {term}`alias` (shortcut) in Git, to be able to nicely visualize
branch structure in the terminal without having to remember a long Git command:
```console
$ git config --global alias.graph "log --all --graph --decorate --oneline"
```

We have an own section about aliases: {ref}`aliases`.


## Default text editor for commit messages

Git sometimes needs to start a text editor for you to enter messages (unless you create
commits from inside an editor or on the web).
This may have already been set to something (like VS Code), but if not
`nano` is usually a safe choice:

```console
$ git config --global core.editor nano
```

The [installation instructions text editor page](https://coderefinery.github.io/installation/editors/) gives ways
to set other editors, or do a web search for "git set editor to
[editor name]".


% This anchor used for linking from other lessons
(clone-method)=

## Authenticating to GitHub or GitLab: SSH or HTTPS or VS Code or RStudio?

**How does the hosting service know who you are?** We discuss here four options:
- **SSH** is the classic method, using [Secure Shell
  Protocol](https://en.wikipedia.org/wiki/Secure_Shell) remote connection
  keys.
- **HTTPS** works with the **Git Credential Manager**, which is an
  extra add-on that works easily in Windows and Mac.
- **VS Code** editor can authenticate with GitHub using its own
  authentication method.
- **RStudio** can handle authentication via HTTPS or SSH. 
    Here, the RStudio instructions cover using **HTTPS**.

Read how to install them from the [installation
instructions](https://coderefinery.github.io/installation/ssh/).

Test which one you should use:

:::::{tabs}
  ::::{group-tab} Command line: SSH
    Try one of these commands, depending on where your repository is hosted:

    **GitHub:**
    ```console
    $ ssh -T git@github.com
    ```

    If it returns `Hi USERNAME! You've successfully authenticated, ...`,
    then SSH is configured and the following steps will work with the SSH
    cloning.

    **GitLab:**
    ```console
    $ ssh -T git@gitlab.com
    ```

    If it returns `Welcome to GitLab, @USERNAME!`, then SSH is configured
    and the following steps will work with SSH cloning.

    From now on, **if you know that SSH works, select SSH as the clone URL
    from the service hosting your repository.** GitHub URLs start with
    `git@github.com:` and GitLab URLs start with `git@gitlab.com:`.

    See our [installation
    instructions](https://coderefinery.github.io/installation/ssh/) to
    set up SSH access.
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
    HTTPS as the clone URL from your hosting service, or translate the URL
    to start with the right thing yourself:** `https://github.com/` or
    `https://gitlab.com/`
  ::::

  ::::{group-tab} VS Code
    VS Code has its own authentication method for GitHub and GitLab
    integrations, and the editor or its extension will guide you through the
    process. If you are using VS Code, you can skip the SSH and HTTPS checks.

    From now on, you should **select HTTPS as the clone URL from
    GitHub or GitLab, or translate the URL to start with the right thing
    yourself:** `https://github.com/` or `https://gitlab.com/`

    If you don't want VS Code to be connected to your GitHub or GitLab account,
    set up and use the SSH method instead.
  ::::
  
  ::::{group-tab} RStudio
    See our [installation instructions](https://coderefinery.github.io/installation/ssh/)
    for how to configure SSH or HTTPS authentication. In RStudio, these steps
    can be run in the Terminal tab of the console panel.
    
    After the configuration, you should **select HTTPS as the clone URL from
    GitHub or GitLab, or translate the URL to start with the right thing
    yourself:** `https://github.com/` or `https://gitlab.com/`
    
    To set your default branch name in Git to `main` in RStudio, run
    
    ```r
    usethis::git_default_branch_configure()
    ```

    Any configuration steps above that are not covered in the RStudio instructions 
    can be run in the Terminal tab of RStudio's console panel.

  ::::
:::::
