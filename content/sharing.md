# How to turn your project to a Git repo and share it

```{objectives}
- We get a feeling for remote repositories ([more later](https://coderefinery.github.io/git-collaborative/)).
- We are able to publish a repository on the web.
- We are able to fetch and track a repository from the web.
```

```{instructor-note}
- 15 min demonstration/type-along
- 25 min exercise
```


## From our laptops to the web

We have seen that **creating Git repositories and moving them around is
relatively simple** and that is great.

So far, if you only worked in the command line, everything was local and all
snapshots, branches, and tags are saved under `.git`.

If we remove `.git`, we remove all Git history of a project.

```{discussion}
- What if the hard disk fails?
- What if somebody steals my laptop?
- How can we collaborate with others across the web?
```


## Remotes

We will learn how to work with remote repositories in detail in the
[collaborative distributed version control](https://coderefinery.github.io/git-collaborative/) lesson.

In this section we only want to get a taste to prepare us for other lessons
where we will employ GitHub.  Our goal is to publish our exercise guacamole recipe
which we prepared in the previous episodes on
the web. Don't worry, you will be able to remove it afterwards.

````{admonition} If you don't have the recipe repository from previous episodes
Maybe you joined the workshop later or got stuck somewhere? **No problem**!

**If you don't have the recipe repository from previous episodes**, you can
clone our version of the repository using (please **skip this if you have the recipe
repository on your computer already**):
```console
$ git clone https://github.com/coderefinery/recipe-before-merge.git recipe
$ cd recipe
$ git remote remove origin
```

Now you have a repository called `recipe` on your computer with a couple of
commits. Further down we will also clarify what `git clone` does.
````

To store your git data on another server, you use **remotes**.
A remote is a repository on its own, with its own branches
We can **push** changes to the remote and **pull**
from the remote.

You might use remotes to:
- Back up your own work.
- To collaborate with other people.

There are different types of remotes:
- If you have a server you can ssh to, you can use that as a remote.
- [GitHub](https://github.com) is a popular, closed-source commercial site.
- [GitLab](https://about.gitlab.com) is a popular, open-core
  commercial site.  Many universities have their own private GitLab servers
  set up.
- [Bitbucket](https://bitbucket.org) is yet another popular commercial site.
- Another option is [NotABug](https://notabug.org).
- We also operate a [Nordic
  research software repository
  platform](https://coderefinery.org/repository/).
  This is GitLab, free for researchers and allows private,
  cross-university sharing.

---

% This anchor used for linking from other lessons
(clone-method)=

## Authenticating to GitHub: SSH or HTTPS?

**How does Github know who you are?**  This is hard and there are two
options.

* **SSH** is the classic method, using Secure Shell remote connection
  keys.
* **HTTPS** works with the **Git Credential Manager**, which is an
  extra add-on that works easily in Windows and Mac.

Read how to install them from the [installation
instructions](https://coderefinery.github.io/installation/ssh/).

Test which one you should use:

`````{tabs}
  ````{group-tab} SSH
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
  ````{group-tab} HTTPS
    Try this command:
    ```console
    $ git config --get credential.helper
    ```

    If this shows something, then the credential manager is probably
    configured and HTTPS cloning will work (but you can't verify it until
    you try using it).

    From now on, **if you know that HTTPS works, you should always select
    HTTPS as the clone URL from Github, or translate the URL to start with
    the right thing yourself:** `https://github.com/`
  ````
`````

If you do not have these configured, please watch as we do this episode and you
can check the [installation
instructions](https://coderefinery.github.io/installation/ssh/)
before the next [collaborative Git
lesson](https://coderefinery.github.io/git-collaborative/), where we will need
one of these set up.

---

## Publishing an existing repository from laptop to GitHub

```{admonition} If you started in the browser and have nothing on your laptop yet
It is possible, that you already have a repository on GitHub if you followed
the examples and exercises in previous episodes in the browser. In this case,
please watch others publish their repository and try to clone your repository
to the laptop using instructions at the bottom of this page.
```

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

**Reload your GitHub project website** and - taa-daa - your commits should now be
online! What just happened? **Think of publishing a repository as uploading
the `.git` part online**.


```{admonition} Troubleshooting
**error: remote origin already exists.**
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
```

---

## Cloning a repository from GitHub to laptop

Now other people can clone this repository and contribute changes. In the
[collaborative distributed version control](https://coderefinery.github.io/git-collaborative/) lesson
we will learn how this works.

At this point only a brief demo - if you copy the SSH or HTTPS address, you can clone repositories like this
(again adapt the `USER` in the "USER/repository.git" part):


`````{tabs}
````{group-tab} SSH
```console
$ git clone git@github.com:USER/recipe.git
```

**From now on, if you are using SSH, you should pay attention and make
sure your clone URLs start with `git@github.com:` now and in future
lessons.**
````
````{group-tab} HTTPS
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
````{group-tab} SSH
```console
$ git clone git@github.com:USER/recipe.git myrecipe
```
````
````{group-tab} HTTPS
```console
$ git clone https://github.com/user/recipe.git myrecipe
```
````
`````

What just happened? **Think of cloning as downloading the `.git` part to your
computer**. After downloading the `.git` part, the default branch (the branch pointed to by HEAD) is
automatically checked out.

```{keypoints}
- A repository can have one or multiple remotes (we will revisit these later).
- Local branches often track remote branches.
- A remote serves as a full backup of your work.
- We'll properly learn how to use these in the
  [collaborative distributed version control](https://coderefinery.github.io/git-collaborative/).
```
