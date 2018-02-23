---
layout: episode
title: Basics
teaching: 25
exercises: 20
questions:
  - What is Git?
  - What is a repository?
  - How does Git operate?
  - How do I make commits?
  - How do I select what to commit?
  - How can I undo things?
objectives:
  - Learn to create Git repositories and make commits.
  - Get a grasp of the structure of a repository.
  - Learn how to inspect the project history.
  - Learn how to write useful commit log messages.
keypoints:
  - "Initializing a Git repository is simple: `git init`"
  - Commits should be used to tell a story.
  - Git uses the .git folder to store the snapshots.
---

## What is Git, and what exactly is a Git repository?

Git is used to track the content of a folder as it changes over time. When a file is tracked by Git, it is
possible to go back to any historical version of that file. More precisely, one can go back to any version
of the file which Git was told to keep a record of. Git is thus a *version control system*. 

For this time-travelling to work, Git needs to maintain records 
of all changes. These records and some associated information are what make up a Git repository.
The Git repository itself is a set of files kept inside a sub-folder called ".git"
located in the directory which has been put under Git version control.

- All the magic is under `.git`: all the history, all snapshot, all branches, everything
- When staging and committing files, we "copy" them into `.git`
- One file or track entire file trees can be tracked
- Git does not pollute subdirectories
- If we remove `.git`, we remove the repository (but keep the working directory!)
- It is very easy to create a Git repository to track something that you work on
- `.git` uses relative paths - you can move the whole thing somewhere else and it will still work

---


## A mental model of Git

It is useful to have a mental model of how Git operates before jumping in to the first example.

- Many version control systems store information as a list of file-based changes 
  - a set of files and the changes made to each file over time 
- Git instead thinks of its data more like a stream of snapshots 
  - for every *commit* (when the state of a project is saved), Git takes a picture (snapshot) of what all files look like at that moment and stores a reference to that snapshot
  - if some files have not changed, Git just stores a link to the previous identical file it has already stored
  - it's possible to take a particular file back in time to a previous snapshot, but by default all other files will be taken back in time as well

![Git snapshots]({{ site.baseurl }}/img/snapshots.png
"git as a filesystem"){:class="img-responsive"}

> Image from [the Pro Git book](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)

## Recording a snapshot

Git takes snapshots only if we request it. When taking a photo with a camera, we first focus on what we want to 
capture and shoot. Similarly, taking a Git snapshot is a two step process. 
- The focusing equivalent in Git is called *staging* 
  - if you want to include changes to a file in a snapshot then you should stage that file 
  - if you want many files then you should stage them all 
- The shooting equivalent Git is called a *commit*
  - this stores the snapshot to Git history

![Git staging]({{ site.baseurl }}/img/git_stage_commit.svg
"git staging and committing"){:class="img-responsive" style="max-width:70%"}


What do you think will be the outcome if you stage a file and then edit it and stage it again, do this
several times and at the end perform a commit? (think of focusing several scenes and pressing the shoot
button only at the end)

Here is another way to view the two-step snapshotting in Git from [the Pro Git book](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics).
![Git staging]({{ site.baseurl }}/img/file_states_2.png
"git staging and committing"){:class="img-responsive" style="max-width:70%"}

## Tracking a guacamole recipe with Git

We will learn how to initialize a Git repository, how to track changes, and how
to make delicious guacamole!

This example is inspired by [Byron Smith](http://blog.byronjsmith.com), for original reference, see
[this thread](http://lists.software-carpentry.org/pipermail/discuss/2016-May/004529.html).
The motivation for taking a cooking recipe instead of a program is that everybody can relate to cooking
but not everybody may be able to relate to a program written in e.g. Python or another language.

Let us start.
One of the basic principles of Git is that it is **easy to create repositories**:

```shell
$ mkdir recipe
$ cd recipe
$ git init
```

That's it! We have now created an empty Git repository.

We will use `git status` a lot to check out what is going on:

```shell
$ git status

On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

We will make sense of this information during this morning.

Let us now **create two files**.

One file called `instructions.txt`, containing:

```
* chop avocados
* chop onion
* squeeze lime
* add salt
* and mix well
```

And one file called `ingredients.txt`, containing:

```
* 2 avocados
* 1 lime
* 2 tsp salt
```

As mentioned above, in Git you can always check the status of files in your repository using
`git status`. It is always a safe command to run and in general a good idea to
do when you are trying to figure out what to do next:

```shell
$ git status

On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	ingredients.txt
	instructions.txt

nothing added to commit but untracked files present (use "git add" to track)
```

The two files are untracked in the repository (directory). You want to **add the files** (focus the camera)
to the list of files tracked by Git. Git does not track
any files automatically and you need make a conscious decision to add a file. Let's do what
Git hints at and add the files:


```shell
$ git add ingredients.txt
$ git add instructions.txt
$ git status

On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   ingredients.txt
	new file:   instructions.txt
```

Now the snapshot is *staged* and ready to be committed.

Before we make the first commit, let us check the help page for that command:

```shell
$ git help commit
```

You should see a very long help page as the tool is very versatile. Do not
worry about this now but keep in mind that you can always read the help files
when in doubt. Searching online can also be useful, but choosing search terms 
to find relevant information takes some practice and discussions in some
online threads may be confusing.
Note that help pages also work when you don't have a network connection!

Let us now commit the change to the repository:

```shell
$ git commit -m "adding ingredients and instructions"

[master (root-commit) aa243ea] adding ingredients and instructions
 2 files changed, 10 insertions(+)
 create mode 100644 ingredients.txt
 create mode 100644 instructions.txt
```

### Git history and log

Now try `git log`:

```shell
$ git log

commit d619bf848a3f83f05e8c08c7f4dcda3490cd99d9
Author: Radovan Bast <bast@users.noreply.github.com>
Date:   Thu May 4 15:02:56 2017 +0200

    adding ingredients and instructions
```

- We can browse the development and access each state that we have committed.
- The long hashes uniquely label a state of the code.
- They are not just integers counting 1, 2, 3, 4, ... (why?).
- We will use them when comparing versions and when going back in time.
- `git log --oneline` only shows the first 7 characters of the commit hash and is good to get an overview.
- If the first characters of the hash are unique it is not necessary to type the entire hash.
- `git log --stat` is nice to show which files have been modified.

---

## Exercise: record changes

Add 1/2 onion to `ingredients.txt` and also the instruction
to "enjoy!" to `instructions.txt`. Do not stage the changes yet.

When you are done editing the files, try `git diff`:

```shell
$ git diff
```

```
diff --git a/ingredients.txt b/ingredients.txt
index 2607525..ec0abc6 100644
--- a/ingredients.txt
+++ b/ingredients.txt
@@ -1,3 +1,4 @@
 * 2 avocados
 * 1 lime
 * 2 tsp salt
+* 1/2 onion
diff --git a/instructions.txt b/instructions.txt
index 6a8b2af..f7dd63a 100644
--- a/instructions.txt
+++ b/instructions.txt
@@ -3,3 +3,4 @@
 * squeeze lime
 * add salt
 * and mix well
+* enjoy!
```

Now first stage each change, then commit it (what happens when we leave out the `-m` flag?):

```shell
$ git add ingredients.txt
$ git commit -m "add onion"
$ git add instructions.txt
$ git commit                   # <-- we have left out -m "..."
```

When you leave out the `-m` flag, Git should open an editor where you can edit
your commit message. This message will be associated and stored with the
changes you made. This message is your chance to explain what you've done and
convince others (and your future self) that the changes you made were
justified.  Write a message and save and close the file.

When you are done committing the changes, experiment with
`git log`,
`git show`, and
`git diff`.

### Optional : difftool

This requires you to install an additional tool called Meld (or any of the following tools;
opendiff, kdiff3, tkdiff, xxdiff, kompare, gvimdiff, diffuse, diffmerge, ecmerge, p4merge, araxis, bc,
codecompare, emerge, vimdiff).  [Here is how to install and use Meld](http://meldmerge.org/). 
In short, on Ubuntu do `sudo apt-get install meld`, while on Windows use the installer from the above site. 
Meld is not officially supported on MacOSX yet, but can still be installed via pre-built binaries or from MacPorts, 
Fink or Brew.

Using difftools: 

`git difftool -t <Tool_name> `

To use Meld

 `git difftool -t meld -y`

---

## Undoing things

We have been advocating about how it is possible to use Git to go back to any
historical version and start over. In this section we will learn some basics
about this. Before we begin please be warned that some commands discussed here
will result in permanent data loss and should be used with prudence. As we
discussed Git preserves snapshots of folder content rather than history of files
and it is difficult to go into details on how navigation between snapshots takes
place in a basic course.  So instead of trying to explain details,here we
have selected some examples to show how to achieve certain undo tasks, untill we
learn more in the next sections. The diagram below shows what we did with the
guacamole recipe and we will see how to undo some changes.

![Git events]({{ site.baseurl }}/img/events.svg
"git events"){:class="img-responsive" style="max-width:70%"}

### Change the commit message

The comment we added in the last stage (3) had the message “added enjoy”.
Immediately after we committed and  before any file has been changed we want to
change this message to include your name as the author.  To achieve this we
issue the following command

```shell
 git commit --amend
```

This will give you a chance to edit the commit message.

Effect :The new commit will replace the old one. It’s as if the previous commit
never happened, and it won’t show up in your repository history.

### Unstage a file.
We will edit the instructions.txt file to remove the text “enjoy!”. Then stage
it. Then we want to unstage it so we can edit it more before committing.

Open the file  instructions.txt file and remove the line “enjoy !”

```shell
git status # to confirm what has changed
git add instructions.txt # stage it
git status # to confirm what has staging
git reset instructions.txt
git status # will show the file as unstaged
```

### Un-modify a file.
Let’s say we want to get rid of the changes we did to the  instructions.txt file.

```shell
git checkout instructions.txt
```

This will replace the current version with the last committed version. This action
will result in loss of all the edits after the last commit and can not be undone.

There are much more to discuss on undoing things and we leave them for later until we
learn about branches.

## Exercise: undo unstaged changes

- Make some silly changes to `ingredients.txt` (e.g. add liquorice).
- Inspect the changes with `git status` and `git diff`.
- Undo the unstaged changes with `git checkout ingredients.txt`.
- Inspect the new situation with `git status` and `git diff`.

## Be considerate when modifying committed changes

Indeed, Git lets you do marvelous things with history. This is all fine and well as
long as you are modifying commits that you are not sharing with others. When
you start collaborating with other people it is considered very bad form and
will cause a lot of grief to others if you change things that are already
public and have been used.

In short: **if you change commits that other people depend on, you will lose friends and
social contacts!**

In other words: **changing history is best left to expert time travelers.**

More in this after we learn git remotes.

### Questions

- A safe way to undo past commits is to use `git revert`. What does it do? In doubt, try it.
- What happens if you accidentally remove a tracked file with `git rm`, is it gone forever?
- What situations would justify to modify the Git history and possibly remove commits?
- Is it OK to modify commits that nobody has seen yet?


---


## Git best-practices


### Writing useful commit messages

Using `git log --oneline` we understand that the first line of the commit message is very important.

Good example:

```
increase threshold alpha to 2.0

the motivation for this change is
to enable ...
...
```

Convention: **one line summarizing the commit, then one empty line,
then paragraph(s) with more details in free form, if necessary**.

Not so good example (everything in one long line):

```
increase threshold alpha to 2.0, the motivation for this change is to enable ... [very long line]
```

This is also important for web based repository browsing.

Another bad example:

```
rbast:

fixed an important bug for contracted basis sets
...
```

- Other bad commit messages: "fix", "oops", "save work", "foobar", "toto", "qppjdfjd", "".
- [http://whatthecommit.com](http://whatthecommit.com)
- Write commit messages in English that will be understood
  15 years from now by someone else than you.
- Many projects start out as projects "just for me" and end up to be successful projects
  that are developed by 50 people over decades.

### Commit with preview of changes

It is possible to see the changes being commited

```shell
git commit -v
```


### Ignoring files and paths with .gitignore

- Should we add and track all files in a project?
- How about generated files?
- Why is it considered a bad idea to commit compiled binaries to version control?
- What types of generated files do you know?

As a general rule compiled files are not
committed to version control. There are many reasons for this:

- Your code could be run on different platforms.
- These files are automatically generated and thus do not contribute in any meaningful way.
- The number of changes to track per source code change can increase quickly.

For this we use `.gitignore` files. Example:

```
# ignore compiled python 2 files
*.pyc
# ignore compiled python 3 files
__pycache__
```

`.gitignore` uses something called a
[shell glob syntax](https://en.wikipedia.org/wiki/Glob_(programming)) for
determining file patterns to ignore. You can read more about the syntax in the
[documentation](https://git-scm.com/docs/gitignore).

An example taken from [documentation](https://git-scm.com/docs/gitignore):

```
# ignore objects and archives, anywhere in the tree.
*.[oa]
# ignore generated html files,
*.html
# except foo.html which is maintained by hand
!foo.html
# ignore everything under build directory
build/
```

You can have `.gitignore` files in lower level directories and they effect the paths
relatively.


### Clean working area

- Use `git status` a lot.
- Use `.gitignore`.
- Untracked files belong to .gitignore.
- **All files should be either tracked or ignored**.


### Questions

- Should we add and commit `.gitignore`?
- What will probably happen if we choose not to use `.gitignore` in our projects?

---


## Summary

Now we know how to save snapshots:

```shell
$ git add <file(s)>
$ git commit
```

And this is what we do as we program.

Every state is then saved and later we will learn how to go back to these "checkpoints"
and how to undo things.

```shell
$ git init    # initialize new repository
$ git add     # add files or stage file(s)
$ git commit  # commit staged file(s)
$ git status  # see what is going on
$ git log     # see history
$ git diff    # show unstaged/uncommitted modifications
$ git show    # show the change for a specific commit
$ git mv      # move tracked files
$ git rm      # remove tracked files
```

Git is not ideal for large binary files
(for this consider [http://git-annex.branchable.com](http://git-annex.branchable.com)).

---

