---
layout: episode
title: Basics
teaching: 20
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

## What is Git and what exactly is a Git repository

Git is used to track the content of a folder as they are changed overtime. This could be files 
in a folder or files in one of the sub-folders. When a file is under the Git tracking, it is 
possible to go back to any historical version of that file. More precisely, back to any version 
of the file which we asked Git to keep a record of. As this is a navigation between versions we 
refer to Git as a version control system. Git need to maintain records to provide this 
time-travel functionality. These records and associated information are called a Git repository. 
The Git repository it self is a set of files and kept inside a sub-folder called ".git".     

## How Git operates and some terms.
Lets have an simplified overview on how Git operates before we jump in to our example. We said 
that Git can navigate back to an older version of a file using the information stored in the 
git-repository. In operational point of view, what Git actually does is to take the folder where 
the file reside back in time to the point where the file had the composition we requested.  We call 
this point a snapshot. This means that if some other file has a different composition in addition 
to our files of interest at this snapshot, we will loose the modifications done to that file as 
well. The following diagram from https://git-scm.com illustrated this point

![Git snapshots]({{ site.baseurl }}/img/snapshots.png
"git as a filesystem"){:class="img-responsive"}

In the diagram, we start with 3 files A,B and C in the same folder. The files A and C are modified 
in version 2 (second snapshot) and file B stays the same. Lets say we are in the fifth snapshot and 
we request Git to go back to the third snapshot with the intention of getting A1 version of the file A. 
Then we will end up with A1,C1(loose one edit) and unmodified B (loose both edits).

## Recording a snapshot 
Git takes snapshots only if we request it. Requesting a snapshot is a two step process, just as we 
take a snap with a camera, first we focus on what we want to catch then shoot. The focusing equivalent 
of Git is called staging. If you want to include changes to a file in a snapshot then you should stage 
that file, if you want many files then you should stage them all. As we know just focusing is not 
enough to capture the moment, we need to commit our selves to taking the photo by pressing the shoot 
button. In Git, after we stage the files, we commit to it using the command commit. This action is not 
surprisingly called a commit. 

![Git staging]({{ site.baseurl }}/img/git_stage_commit.svg
"git Vs taking a photo"){:class="img-responsive"}

What do you think will be the outcome if you stage a file and then edit it and stage it again,do this 
several time and at the end perform a commit ? (think of focusing several scenes and pressing the shoot 
button only at the end!)    


## Tracking a guacamole recipe with Git

We will learn how to create a Git repository, how to track changes, and we will also learn how
to create a delicious guacamole.

This example is inspired by [Byron Smith](http://blog.byronjsmith.com), for original reference, see
[this thread](http://lists.software-carpentry.org/pipermail/discuss/2016-May/004529.html).
The motivation for taking a cooking recipe instead of a program is that everybody can relate to cooking
but not everybody may be able to relate to a program written in e.g. Python or another language.

Let us start!
One of the basic principles of Git is that it is **easy to create repositories**:

```shell
$ mkdir recipe
$ cd recipe
$ git init
```

That's it! Now we have created an empty Git repository!

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
do when you are trying to figure what to do next:

```shell
$ git status

On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	ingredients.txt
	instructions.txt

nothing added to commit but untracked files present (use "git add" to track)
```

The two files are untracked in the repository (the directory). You want to **add the files**
to the list of files tracked by Git. By default Git does not track
any files and you need make a conscious decision to add a file. Let's do what
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

Now the snapshot is *staged* to be committed (saved).

Before we make the first commit, let us check the help page for that command:

```shell
$ git help commit
```

You should see a very long help page as the tool is very versatile. Do not
worry about this now but keep in mind that you can always read the help files
when in doubt. Googling is also acceptable, but often checking the relevant
help page is faster and those pages were written by the authors of the
program and not some random people on the internet. The help pages also work
when you don't have a network connection.

Let us now commit the change to the repository:

```shell
$ git commit -m "adding ingredients and instructions"

[master (root-commit) aa243ea] adding ingredients and instructions
 2 files changed, 10 insertions(+)
 create mode 100644 ingredients.txt
 create mode 100644 instructions.txt
```

Now try `git log`:

```shell
$ git log

commit d619bf848a3f83f05e8c08c7f4dcda3490cd99d9
Author: Radovan Bast <bast@users.noreply.github.com>
Date:   Thu May 4 15:02:56 2017 +0200

    adding ingredients and instructions
```

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


### Git history

- We can browse the development and access each state that we have committed.
- The long hashes uniquely label a state of the code.
- They are not just integers counting 1, 2, 3, 4, ... (why?).
- We will use them when comparing versions and when going back in time.
- `git log --oneline` only shows the first 7 characters of the commit hash and is good to get an overview.
- If the first characters of the hash are unique it is not necessary to type the entire hash.
- `git log --stat` is nice to show which files have been modified.


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

---

## Ignoring files and paths with .gitignore

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

## Where is the Git repository?

- All the magic is under `.git`, all the history, all snapshot, all branches (later), everything.
- When we staged and committed files, we "copied" them into `.git`.
- Here we only track one file but we can track entire file trees.
- Git does not pollute subdirectories.
- If we remove `.git`, we remove the repository (but of course keep the working directory).
- It is very easy to create (and remove) a Git repository to track something that you work on.
- `.git` uses relative paths (very convenient), you can move the whole thing somewhere else
  and it will still work.

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

## Exercise: undo unstaged changes

- Make some silly changes to `ingredients.txt` (e.g. add liquorice).
- Inspect the changes with `git status` and `git diff`.
- Undo the unstaged changes with `git checkout ingredients.txt`.
- Inspect the new situation with `git status` and `git diff`.

---

## Modifying committed changes

In Git it is possible to modify and even remove committed history with `git commit --amend`
or `git reset`. We will not demonstrate this at this stage.

Indeed, Git lets you do marvelous things with history. This is all fine and well as
long as you are modifying commits that you are not sharing with others. When
you start collaborating with other people it is considered very bad form and
will cause a lot of grief to others if you change things that are already
public and have been used.

In short: **if you change commits that other people depend on, you will lose friends and
social contacts!**

In other words: **changing history is best left to expert time travelers.**

### Questions

- A safe way to undo past commits is to use `git revert`. What does it do? In doubt, try it.
- What happens if you accidentally remove a tracked file with `git rm`, is it gone forever?
- What situations would justify to modify the Git history and possibly remove commits?
- Is it OK to modify commits that nobody has seen yet?
