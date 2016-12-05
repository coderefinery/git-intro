---
layout: episode
title: "Introduction to version control"
teaching: 20
exercises: 25
questions:
  - "Why is version control important?"
  - "What is git?"
  - "What is a repository?"
  - "How do I make commits?"
  - "How do I select what to commit?"
  - "How can I undo things?"
objectives:
  - "Student learns to create git repositories and make commits"
  - "Student understands how the repository is structured."
keypoints:
  - "Initializing a git repository is simple"
  - "Commits should be used to tell a story."
  - "Git uses the .git folder to store the repository."
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


```python
def foo():
    print('foo!')
```


```
$ mkdir testrepo
$ cd testrepo
$ git init
```

That's it. Now you've created an empty git repository! Before we can start
committing files to it we need to set up a few very basic settings, though.

Sometimes the idea to version control your project comes as an afterthought.
You can run **git init** at the top-level folder whenever you feel like it. If
the folder is already a git repository version control you won't succeed,
though.

## Configuring git

### Configuring your personal details

First we need to tell git who you are. When you make commits git stores your
name and.

```
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

Create a file called **hello.py** with the following content in **testrepo/**

``` python
from __future__ import print_function
print("Hello World")
```

Verify that it works

``` 
$ python hello.py
Hello World!
```

Great, now you have your first script and want to commit the first version of
it. In git you can always check the status of files in your repository using
**git status**. It is always a safe command to run and in general a good idea to
do when you're trying to figure what to do next..

```
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
git hints and add the file using **git add**.

```

$ git add hello.py 
$ git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   hello.py

```

Now **git status** is telling us that the file hello.py will be committed as a
new file. Observe how git again tells you the command you would need to not
remove the file from the list of those being added.

Let's make the first commit by using **git commit** but before that let's check
the *man* page of that commit. The first command will work on Unix systems
that support man pages and the second one will work on both. Observe the dash
in the man call.

```

$ man git-commit 
$ git help commit

```

You should see a very long help page as the tool is very versatile. Do not
worry about this now but keep in mind that you can always read the help files
when in doubt. Googling is also acceptable, but often checking the relevant
help page is faster and those pages were written by the authors of the
program and not some random people on the internet.

Now let's make that first commit.

```
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


Check the status of your working tree with **git status**
```
$ git status
On branch master
nothing to commit, working tree clean
```

You can check the history of commits made with **git log**

```
$ git log
commit f2045a6e190ebd49b8d6d39ced4f2eec54d566f7
Author: Jyry Suvilehto <jyry.suvilehto@csc.fi>
Date:   Tue Nov 29 11:30:56 2016 +0200

    initial commit containing a simple hello world example.
```

Let's make the example more complicated

Edit the  file called **hello.py** to create the following

``` python
from __future__ import print_function
def say_hello():
	print("Hello World")
```

Now, create a new file called **runner.py** 

``` python
from hello import say_hello
if __name__ == "__main__":
	say_hello()
```

Test that it works
````
$ python runner.py 
Hello World!
```
Great! Now you have made changes and you want to record the status of the current state of the project you worked on. 

Check the current status of your working tree.

```
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	hello.pyc
	runner.py
```

Now we have a problem: the hello.pyc is a compiled Python file that is just a
transformed version of hello.py. If you're using Python 3 you will instead see
a new directory called **__pycache__**. __As a general rule compiled files are not
committed to version control.__ There are many reasons for this:

* your code could be run on different platforms
* the files are automatically generated and thus do not contribute in any meaningful way
* the number of changes to track per source code change can increase quickly

To help you on your way let's create a [**.gitignore**](https://git-scm.com/docs/gitignore) file with the following content:

```
# ignore compiled python 2 files
*.pyc
# ignore compiled python 3 files
__pycache__
```
This .gitignore file tells git to ignore files matching certain file name
globs. The file applies to this directory and subdirectories, but
subdirectories can have their own .gitignores. 

Now check the status of your working tree again:


```
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.gitignore
	runner.py
```

Here git tells you that there are two files that are not yet tracked by git and
that the one file tracked by git has changed.

Keep in mind that version control is about telling the story of how your project came to be. Let's commit the changes in two separate steps.

First, use **git add** to add the .gitignore file, check what happened with **git status** ~~and commit the changes. The -m handle gives **git commit** a commit message without opening your text editor.~~

```
$ git add .gitignore
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   .gitignore

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	runner.py
```

Notice how git tells you what changes it will make with the commit and gives you instructions on the things you might want to do. The `hello.py` file can moved to a staged state or unmodified state with either `git add` or `git checkout --`.
![States of hello.py](../assets/img/hw_state001.png){:class="img-responsive"}
### States of a file.

In general files can have one of 4 states inside a git repository. *Image CC BY 3.0 from the Pro Git book.*

![States of a git file](../assets/img/lifecycle.png "States of a git file. License CC BY 3.0"){:class="img-responsive"}

Now you decide you actually want to commit the changes to the python files and only then add the .gitignore file. Let's use git reset to reset the staged file to it's previous state (untracked)

```
$ git reset HEAD hello.py
$ git reset HEAD .gitignore
```

What does HEAD mean here? It's a reference to the current committed state of the project. We'll get back to that in a bit.

Now add the files you want to commit again and commit them with an optional message.

```
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   hello.py
	new file:   runner.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.gitignore
$ git commit
```

Now add the .gitignore file and commit it too.

```
$ git add .gitignore
$ git commit -m ".gitignore"
```

Now you can check the commit history of your repository with *git log*

```
$ git log
commit 25cf1cb2dfd2830a85aa1da7a0a346af4991f808
Author: Joe Example <joe@example.com>
Date:   Wed Nov 30 14:34:49 2016 +0200

    .gitignore

commit 94b96dbc0c4008873d569505e59158cfc18e687a
Author: Joe Example <joe@example.com>
Date:   Wed Nov 30 14:33:26 2016 +0200

    Split hello world functionality to two files.

commit f2045a6e190ebd49b8d6d39ced4f2eec54d566f7
Author: Joe Example <joe@example.com>
Date:   Tue Nov 29 11:30:56 2016 +0200

    initial commit containing a simple hello world example.
```

*git log* shows the commits made in your repository. By default it uses a
paginator and you can follow the system all the way back to the initial commit.
The commit messages you write tell a story of what has been done at each stage
of the project.

### Food for thought

**ToDo: have special css for these pondering points**

Is the last commit message informative enough?

### Amending

Let's agree that the final commit message could be more verbose. It's possible
change the last commit before you publish it to others (more on this later).
One of the basic tenents of git is that __published commits remain unchanged__.
If you do not follow this you risk losing friends and social contacs!

Fortunately we haven't published anything yet so we can use the **--amend** handle for **git commit**

```
$ git commit --amend -m "add .gitignore to ignore temporary Python files"
$ git log
commit ab9544c3e5713e23e19586c29c8a3d802e361148
Author: Joe Example <joe@example.org>
Date:   Wed Nov 30 14:34:49 2016 +0200

    add .gitignore to ignore temporary Python files
```

### Undoing uncommitted changes

Remove the file hello.py

```
$ rm hello.py
$ git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	deleted:    hello.py
```

The file is gone and git tells you as much. However as you have committed the
file you don't need to worry. The old version is still accessible. The
instructions to access are clearly visible in the message.

Now edit the file hello.py so that it looks as follows (i.e. add a comment):

```python
# i am a comment
from hello import say_hello
if __name__ == "__main__":
    say_hello()
```

And run **git status again**.

```
$ git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	deleted:    hello.py
	modified:   runner.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Next we will use **git checkout** to undo the uncommitted changes to the local
working copy. __git checkout is a dangerous command__. If you make changes to a
file and run **git checkout** before committing, the changes will be lost!

Let us for now assume you are aware of this and this is actually what you want to do.

```
$ git checkout -- hello.py
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   runner.py

no changes added to commit (use "git add" and/or "git commit -a")
$ git checkout -- runner.py
$ git status
On branch master
nothing to commit, working tree clean
```

--- 

## Down the rabbit hole

Now that we've made a couple of commits let's look at what's happening under
the hood.

``` 
$ cd .git
$ ls
COMMIT_EDITMSG  description info        refs
HEAD        hooks       logs
config      index       objects
```

Git stores everything under the .git folder in your repository. In fact, **the
.git directory is the git repository.**

Previously when you wrote the commit messages using your text editor, they
were in fact saved to COMMIT_EDITMSG.

Look at the file HEAD, it contains a reference to the file refs/heads/master.
Check the content of that file. It contains an SHA-1 hash (a
40-characther hexadecimal string). An object corresponding to that character
string (called a blob) can be found under

Each commit in git is stored as a blob. This blob contains information about
the author and the commit message.  The blob references another blob that lists
the files present in the directory at the time and references blobs that record
the state of each file. 

*Image CC BY 3.0 from the Pro Git book.*

![A commit inside git](../assets/img/commit-and-tree.png "States of a git file. License CC BY 3.0"){:class="img-responsive"}


Once you have several commits, each commit blob also links to the hash of the previous commit. Up until now these commits have created a list but in the next lessons they will create a [directed acyclic graph](http://eagain.net/articles/git-for-computer-scientists/) (don't worry if the term is not familiar).

*Image CC BY 3.0 from the Pro Git book.*

![A commit and it's parents](../assets/img/commits-and-parents.png "Commit and it's parents License CC BY 3.0"){:class="img-responsive"}

All branches and tags in Git are simply pointers to a commit. Basic branching and
merging is the topic of our next lesson.

## Challenge example

> ## this is a challenge
> what does it do
> 
> > ## Solution
> > this is a solution
> {: .solution }
{: .challenge :}
