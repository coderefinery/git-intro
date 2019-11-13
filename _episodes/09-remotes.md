---
layout: episode
title: Sharing repositories online
teaching: 10
exercises: 10
questions:
  - How can I set up a public repository online?
  - How can I clone a public repository to my computer?
  - How does version control scale from 1 to N users per repository?
objectives:
  - We get a feeling for remote repositories (more later).
  - We are able to publish a repository on the web.
  - We are able to fetch and track a repository from the web.
keypoints:
  - A repository can have one or multiple remotes (we will revisit these later).
  - Local branches often track remote branches.
  - All this might be a bit nebulous but we will add clarity later this week.
  - A remote serves as a full backup of your work.
  - We'll properly learn how to use these in the next "git
    collaborative" lesson.
---

We will learn how to work with remote repositories in detail in the
[collaborative distributed version control](https://coderefinery.github.io/git-collaborative/) lesson.

In this section we only want to get a taste to prepare us for other lessons
where we will employ GitHub.

Our goal is to publish our guacamole recipe on the web. Don't worry, you will be able
to remove it afterwards.


## From our laptops to the web

We have seen that **creating Git repositories and moving them around is
simple** and that is great.

So far everything was local and all snapshots, branches, and tags are saved under `.git`.

If we remove `.git`, we remove all Git history of a project.

- What if the hard disk fails?
- What if somebody steals my laptop?
- How can we collaborate with others across the web?

---

## Remotes

To store your git data on another server, you use **remotes**.  A
remote is treated the same as a branch - most of the same concept
apply, but you can also **push** changes to the remote and **pull**
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
- Another option is [NotABug](https://notabug.org)
- **We especially encourage course participants to use our new [Nordic
  research software repository
  platform](https://source.coderefinery.org)**, for more information
  see
  [https://coderefinery.org/repository/](https://coderefinery.org/repository/).
  This is GitLab, free for researchers and allows private,
  cross-university sharing.

---

## GitHub

One option to host your repository on the web is [GitHub](https://github.com).

GitHub is a for-profit service that hosts remote git repositories for you. It
offers a nice HTML user interface to browse the repositories and handles many
things very nicely.

It offers unlimited public and private repositories free of charge and costs
a monthly fee if you want access to the pro-tools or need more than 3
collaborators for your private repos. These features had made GitHub very popular
with many open source providers

CodeRefinery does not in any way endorse the use of GitHub. There are many
commercial and open-source alternatives, just check the list above.  In the
end, it is a balance between control and visibility, and we use GitHub because
you are likely to have to use it for other software anyway.

---

## Set up GitHub account

By now you should already have set up a GitHub account but if you haven't,
please do so [here](https://github.com/join). But it is OK if you want to use
[GitLab](https://gitlab.com) or [Bitbucket](https://bitbucket.org) or
[NotABug](https://notabug.org) or another platform instead (although we
will practice collaborative Git on GitHub tomorrow).

---

## Type-along: Create a new repository on GitHub

For the rest of this page, we will make a new repository for our
guacamole recipe on Github, send our code to it, and then see how
others can get the code from it.

1. Login
2. Click on "Repositories"
3. Click on the green button "New"

On this page choose a project name (screenshot).

For the sake of this exercise **do not select**
"Initialize this repository with a README" (what will happen if you do?).

<img src="{{ site.baseurl }}/img/github/1.jpg" width="60%" style="border:2px solid #000000;">

Once you click the green "Create repository", you will see a page similar to:

<img src="{{ site.baseurl }}/img/github/2.jpg" width="60%" style="border:2px solid #000000;">

What this means is that we have now an empty project with either an HTTPS or an
SSH address: click on the HTTPS and SSH buttons to see what happens.

To push changes to the project you will either need SSH keys for the SSH
address (preferred) or you will have to use your GitHub username and password when
using the HTTPS address.  **If you don't know what to do, use HTTPS.**

---

## Pushing our guacamole recipe repository to GitHub

We now want to try the second option that GitHub suggests:

> **... or push an existing repository from the command line**

1. Now go to your guacamole repository on your computer.
2. Check that you are in the right place with `git status`.
3. Copy paste the two lines to the terminal and execute those, in my case (**you
  need to replace the "user" part and possibly also the repository name**):

```shell
$ git remote add origin https://github.com/user/recipe.git
$ git push -u origin master
```

You should now see:

```
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 259.80 KiB | 0 bytes/s, done.
Total 4 (delta 0), reused 0 (delta 0)
To github.com:bast/recipe.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
```

**Reload your GitHub project website and - taa-daa - your commits should now be
online!**

What just happened? **Think of publishing a repository as uploading the `.git` part online**.

---

## Cloning a repository

Now other people can clone this repository and contribute changes. In the
[collaborative distributed version control](https://coderefinery.github.io/git-collaborative/) lesson
we will learn how this works.

At this point only a brief demo - if you copy the SSH or HTTPS address, you can clone repositories like this
(again adapt the "namespace/repository.git" part):

```shell
$ git clone https://github.com/user/recipe.git
```

This creates a directory called "recipe" unless it already exists. You can also specify the target directory
on your computer:

```shell
$ git clone https://github.com/user/recipe.git myrecipe
```

What just happened? **Think of cloning as downloading the `.git` part to your
computer**. After downloading the `.git` part the branch pointed to by HEAD is
automatically checked out.
