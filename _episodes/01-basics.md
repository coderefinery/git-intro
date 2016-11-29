---
layout: episode
title: "Introduction to version control"
teaching: 20
exercises: 25
questions:
  - "Why is version control important?"
  - "What is git?"
objectives:
  - "."
  - "This is another objective of this episode."
keypoints:
  - "This is an important key point."
  - "Another important key point."
  - "One more key point."
---

## Food for thought

- Have you ever had to work with other people on the same project in parallel?
  - What were the challenges? 
  - Did you end up doing overlapping things?
- Have you ever had to start working software written by others? 
  - Did you ever find yourself asking why?
- Have you ever had to maintain a production version of your code and work on
  new features at the same time?
- If you are already familiar with git, have you ever had to google for
  a magic command to solve your problem?

## What is version control?

Something something about telling a story.

Something something about being able to work in parallel.

---
## Creating a git repository

One of the basic principles of git is that it is easy to create repositories. 

```shell
$ mkdir testrepo
$ cd testrepo
$ git init
```

That's it. Now you've created an empty git repository! Before we can start
committing files to it we need to set up a few very basic settings, though.

Sometimes the idea to version control your project comes as an afterthought.
You can run *git init* at the top-level folder whenever you feel like it. If
the folder is already a git repository version control you won't succeed,
though.

## Configuring git

### Configuring your personal details

First we need to tell git who you are. When you make commits git stores your
name and.

```{r, engine='sh', count_lines}
$ git config --global user.name "Your Name"
$ git config --global user.email "your.name@example.org"
```

The "--global" handle sets this across
all your repositories on this machine. It is possible to override this in a
single repository, if for instance you want to use your work email for work
projects and personal email in your hobby projects.

### Configuring your editor

Git assumes you can use a text editor and have configured one you can use.
You can avoid using one  one by always passing messages on the command line,
but that limits you in the long run.

For Unix users git uses whatever you have set as your $EDITOR or defaults to
vi if nothing is set. 


For Windows users
```
$ git config core.editor notepad
$ git config format.commitMessageColumns 72
```

---

## Making a change and commiting it

Create a file called *hello.py* with the following content in **testrepo/**

``` python
from __future__ import print_function
print("Hello World"")
```

Verify that it works
``` shell
$ python hello.py
Hello World!
```

Great, now you have your first script and want to commit the first version of
it. In git you can always check the status of files in your repository using
*git status*. It is always a safe command to run and in general a good idea to
do when you're trying to figure what to do next..

``` shell
$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        hello.py
```

There is now an untracked file in the repository (the directory). You want to
add the file to the list of files tracked by git. By default git doesn't track
any files and you need make a conscious decision to add a file. Let's do what
git hints and add the file using *git add*.

``` shell
$ git add hello.py 
$ git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   hello.py
```

Now *git status* is telling us that the file hello.py will be committed as a
new file. Observe how git again tells you the command you would need to not
remove the file from the list of those being added.

Let's make the first commit by using *git commit* but before that let's check
the *man* page of that commit. The first command will work on Unix systems
that support man pages and the second one will work on both. Observe the dash
in the man call.

``` shell
$ man git-commit 
$ git help commit
```

You should see a very long help page as the tool is very versatile. Do not
worry about this now but keep in mind that you can always read the help files
when in doubt. Googling is also acceptable, but often checking the relevant
help page is faster and those pages were written by the authors of the
program and not some random people on the internet.

Now let's make that first commit.

``` shell
$ git commit
[master (root-commit) f2045a6] initial commit containing a simple hello world
example.
 1 file changed, 2 insertions(+)
  create mode 100644 hello.py
```

Git should show you an editor where you can edit your commit message. This
message will be associated and stored with the changes you made. This message
is your chance to explain what you've done and convince others (and your
future self) that the changes you made were justified.

Write a message and save and close the file. Git will store the commit and
tell you some information. Namely it created one file, into which two new
lines were inserted.

``` shell
$ git status
On branch master
nothing to commit, working tree clean
```

## Make some more commits

--- 

## Part were things get weird

Now that we've made a couple of commits let's look at what's happening under
the hood.

``` shell
$ cd .git
$ ls
```

Git stores everything under the .git folder in your repository. Everything
you've done is stored here.

