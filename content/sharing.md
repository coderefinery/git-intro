# How to turn your project to a Git repo and share it

:::{objectives}
- Turn our own coding project (small or large) into a Git repository.
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

1. Create a new directory with one or few files in it. This represents our
   own project. It is not yet a Git repository.
2. Turn this directory into a Git repository.
3. Share this repository on GitHub.

We offer **three different flows** of how to do this exercise.
::::{tabs}

:::{group-tab} Only using GitHub
:::

:::{group-tab} VS Code
To do:
- https://github.com/login/oauth/authorize
- add screenshot about authorizing
:::

:::{group-tab} Command line
### Put your project under version control

...


### Create an <u>empty</u> repository on GitHub

First log into GitHub, then follow the screenshots and descriptions below.

```{figure} img/basics/new-repo-plus.png
   :alt: Screenshot on GitHub before a new repository form is opened
   :width: 100%
   :class: with-border

   Click on the "plus" symbol on top right, then on "New repository".
```

Another way to create a new repository is to visit
<https://github.com/new> directly.

```{figure} img/remotes/new-bare-repo-form.png
   :alt: Screenshot on GitHub just before a new repository is created
   :width: 100%
   :class: with-border

   Choose a repository name, add a short description, but please **do not check** "Add a
   README file"**. For "Add .gitignore" and "Choose a license" also leave as "None". Finally "Create repository".
```

Once you click the green "Create repository", you will see a page similar to:
```{figure} img/remotes/bare-repo.png
   :alt: Screenshot on GitHub after a bare repository was created
   :width: 100%
   :class: with-border
```

What this means is that we have now an empty project with either an HTTPS or an
SSH address: click on the HTTPS and SSH buttons to see what happens.


### Push an existing repository from laptop to GitHub



We now want to follow the "**... or push an existing repository from the command line**:

1. Now go to your guacamole repository on your computer.
2. Check that you are in the right place with `git status`.
3. Copy paste the three lines to the terminal and execute those, in my case (**you
  need to replace the "USER" part and possibly also the repository name**):


`````{tabs}
  ````{group-tab} SSH
  See above for if SSH is the right option for you.
  ```console
  $ git remote add origin git@github.com:USER/recipe.git
  ```
  ````
  ````{group-tab} HTTPS
  See above for if HTTPS is the right option for you.
  ```console
  $ git remote add origin https://github.com/USER/recipe.git
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
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 221 bytes | 221.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:USER/recipe.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
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
on its own, with its own branches We can **push** changes to the remote and
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
