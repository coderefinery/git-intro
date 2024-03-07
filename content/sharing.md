# How to turn your project to a Git repo and share it

:::{objectives}
- Turn our own coding project (small or large, finished or unfinished) into a
  Git repository.
- Be able to share a repository on the web to have a backup or so that others
  can reuse and collaborate.
:::

:::{instructor-note}
- 10 min introduction and setup
- 25 min exercise
- 15 min discussion
:::


## Exercise

:::::{exercise} Exercise: Turn your project to a Git repo and share it (25 min)

1. Create a new directory called **myproject** with one or few files in it.
   This represents our own project. It is not yet a Git repository.
2. Turn this directory into a Git repository.
3. Share this repository on GitHub.

We offer **three different flows** of how to do this exercise.
::::{tabs}

:::{group-tab} Only using GitHub
### Create an repository on GitHub

First log into GitHub, then follow the screenshots and descriptions below.
```{figure} img/sharing/new-repository.png
:alt: Screenshot on GitHub before a new repository form is opened
:width: 60%
:class: with-border

Click on the "plus" symbol on top right, then on "New repository".
```

Then:
```{figure} img/sharing/create-repository-with-readme.png
:alt: Screenshot on GitHub just before a new repository is created
:width: 100%
:class: with-border

Choose a repository name, add a short description, and in this case **make sure to check** "Add a
README file". Finally "Create repository".
```


### Upload your files

Now that the repository is created, you can upload your files:
```{figure} img/sharing/upload-files.png
:alt: Screenshot on GitHub just before uploading files
:width: 100%
:class: with-border

Click on the "+" symbol and then on "Upload files".
```
:::

:::{group-tab} VS Code
In VS Code it only takes few clicks.

First, open the folder in VS Code. Then click on the source control icon:
```{figure} img/sharing/vscode-start.png
:alt: Screenshot of VS Code before clicking on the source control icon
:width: 100%
:class: with-border

Open the folder in VS Code. Then click on the source control icon.
```

```{figure} img/sharing/vscode-publish-to-github1.png
:alt: Screenshot of VS Code before publishing to GitHub
:width: 100%
:class: with-border

Choose "Publish to GitHub".
```

```{figure} img/sharing/vscode-publish-to-github2.png
:alt: Screenshot of VS Code before publishing to GitHub
:width: 100%
:class: with-border

In my case I chose to "Publish to GitHub public repository".
```

```{figure} img/sharing/vscode-authorize.png
:alt: Screenshot of VS Code asking for authorization
:width: 50%
:class: with-border

First time you do this you might need to authorize VS Code to access your GitHub account.
```

```{figure} img/sharing/vscode-publish-to-github3.png
:alt: Screenshot of VS Code after publishing to GitHub
:width: 100%
:class: with-border

After it is published, click on "Open on GitHub".
```
:::

:::{group-tab} Command line
### Make sure your Git is configured

First, make sure your Git is configured. If you haven't done this before, you
need to set your name and email address. This is used for the commits you make.

```console
$ git config --global user.name "Your Name"
$ git config --global user.email yourname@example.org
```


### Put your project under version control

My example project here consists of two files. Replace this with your own
example files:
```console
$ ls -l

.rw------- 19k user  7 Mar 17:36 LICENSE
.rw-------  21 user  7 Mar 17:36 myscript.py
```

I will first initialize a Git repository in this directory:
```console
$ git init -b main
```

For Git versions older than 2.28, use this instead (and your default branch will then be called `master`):
```console
$ git init
```

Now add and commit two two files to the Git repository:
```console
$ git add LICENSE myscript.py
$ git commit -m "putting my project under version control"
```

If you want to add all files without listing them one by one, you can use `git
add .` instead of `git add LICENSE myscript.py`.

Now you have a Git repository with one commit. Verify this with `git log`.
But it's still only on your computer. Let's put it on GitHub next.


### Create an <u>empty</u> repository on GitHub

First log into GitHub, then follow the screenshots and descriptions below.
```{figure} img/sharing/new-repository.png
:alt: Screenshot on GitHub before a new repository form is opened
:width: 60%
:class: with-border

Click on the "plus" symbol on top right, then on "New repository".
```

Then:
```{figure} img/sharing/create-repository.png
:alt: Screenshot on GitHub just before a new repository is created
:width: 100%
:class: with-border

Choose a repository name, add a short description, but please **do not check** "Add a
README file". For "Add .gitignore" and "Choose a license" also leave as "None". Finally "Create repository".
```

Once you click the green "Create repository", you will see a page similar to:
```{figure} img/sharing/bare-repository.png
:alt: Screenshot on GitHub after a bare repository was created
:width: 100%
:class: with-border
```

What this means is that we have now an empty project with either an HTTPS or an
SSH address: click on the HTTPS and SSH buttons to see what happens.


### Push an existing repository from your computer to GitHub


We now want to follow the "**... or push an existing repository from the command line**":

1. In your terminal make sure you are still in your myproject directory.
2. Copy paste the three lines to the terminal and execute those, in my case (**you
   need to replace the "USER" part and possibly also the repository name**):


`````{tabs}
  ````{group-tab} SSH
  ```console
  $ git remote add origin git@github.com:USER/myproject.git
  ```
  ````
  ````{group-tab} HTTPS
  ```console
  $ git remote add origin https://github.com/USER/myproject.git
  ```
  ````
`````

Then:
```console
$ git branch -M main
$ git push -u origin main
```

The meaning of the above lines:
- Add a remote reference with the name "origin"
- Rename current branch to "main"
- Push branch "main" to "origin"

You should now see:

```text
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 6.08 KiB | 6.08 MiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:USER/myproject.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

Reload your GitHub project website and your commits should now be
online!


### Troubleshooting

**error: remote origin already exists**
- Explanation: You probably ran a `git remote add origin ...` command, then changed your
  mind about HTTPS or SSH and then tried to run the other `git remote add
  origin ...` command but "origin" then already exists.
- Recovery:
  - First remove "origin" with `git remote remove origin`
  - Then run the correct `git remote add origin ...` command

**remote contains work that you do not have**
- Explanation: You probably clicked on "Add a README file" and now the
  repository on GitHub is not empty but contains one commit and locally you
  have a different history. Git now prevents you from accidentally overwriting
  the history on GitHub.
- Recovery:
  - Use `git push --force` instead of `git push`, which will force Git to overwrite the history on GitHub
  - Note that this is a powerful but also possibly dangerous option but here it
    helps us. If it's a brand new repo, it probably is fine to do this. For real
    repositories, don't do this unless you are very sure what is happening.
:::

::::
:::::


## Remote repositories

We will learn how to work with remote repositories in detail in the
[collaborative distributed version
control](https://coderefinery.github.io/git-collaborative/) lesson.  To store
your git data on another server, you use **remotes**.  A remote is a repository
on its own, with its own branches. We can **push** changes to the remote and
**pull** from the remote.

You might use remotes to:
- Back up your own work or make your work findable.
- To collaborate with other people.

There are different types of remotes:
- If you have a server you can SSH to, you can use that as a remote.
- [GitHub](https://github.com) is a popular, closed-source commercial site.
- [GitLab](https://about.gitlab.com) is a popular, open-core
  commercial site.  Many universities have their own private GitLab servers
  set up.
- [Bitbucket](https://bitbucket.org) is yet another popular commercial site.
- Another option is [NotABug](https://notabug.org).
- There are more ...
