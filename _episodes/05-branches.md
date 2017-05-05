---
layout: episode
title: "Branching and Merging"
teaching: 15
exercises: 15
questions:
  - How can I or my team work on multiple features in parallel?
  - How to combine the changes in parallel tracks of work?
  - What is branching and when should I do it?
  - How can I permanently reference a point in history, like a software
    version?
objectives:
  - Be able to create and merge branches.
  - Know the difference between a branch and a tag.
keypoints:
  - A branch is a division unit of work, to be merged with other units of work.
  - Creating branches is simple in Git.
  - Merging branches is often straightforward.
  - A tag is a pointer to a moment in the history of a project.
---

## Food for thought

- How do you work on two things in parallel?
- How often do you find yourself wanting to go into two directions at once?
- How do you patch a version of the code which is not the latest commit?

---

## Motivation for branches

Up until now our repository has only had one branch with one commit coming
after the other:

![Linear]({{ site.baseurl }}/img/gitink/git-branch-01.svg "Linear git
repository"){:class="img-responsive"}

However, software develompent is often not linear:

  - Maintenance of releases, bugfixes, and patches.
  - Collaborative work (everybody would be exposed to your bugs; you would be
    exposed to bugs of other people).
  - We do not have time to write perfect code immediately, it would be nice to
    have the possibility to experiment somewhere aside.
  - Interrupted work (we typically work on several longer term projects at the
    same time).

The strength of version control is that it permits the developers to isolate
different tracks of work. Developers can work on different things and merge
the changes they made to the source code files afterwards to create a composite
version that contains both the changes.

To enable collaborative work we wish to do something more like:

![Git collaborative]({{ site.baseurl }}/img/gitink/git-collaborative-work.svg
"description"){:class="img-responsive"}

A group of commits that create a single narrative are called a **branch**.
There are different branching strategies, but it's easy to think that a branch
tells the story of a feature. E.g. "new login workflow" or "fixing bug in
matrix inversion algoritm" might be logical branches.

---

## What is a commit

Before we exercise branching, a quick recap of what we got so far.

We have three commits and only one development line (branch) and this branch is
called "master":

![]({{ site.baseurl }}/img/gitink/git-branch-01.svg)

```shell
$ git log --stat

commit 7f3582dfbad6539cfa60f5b21bfad41d1b58a618
Author: Radovan Bast <bast@users.noreply.github.com>
Date:   Fri May 5 12:49:45 2017 +0200

    do not forget to enjoy

 instructions.txt | 1 +
 1 file changed, 1 insertion(+)

commit 64441c1934def7d91ff0b66af0795749d5f1954a
Author: Radovan Bast <bast@users.noreply.github.com>
Date:   Fri May 5 12:49:35 2017 +0200

    add onion

 ingredients.txt | 1 +
 1 file changed, 1 insertion(+)

commit d619bf848a3f83f05e8c08c7f4dcda3490cd99d9
Author: Radovan Bast <bast@users.noreply.github.com>
Date:   Fri May 5 12:48:36 2017 +0200

    adding ingredients and instructions

 ingredients.txt  | 3 +++
 instructions.txt | 5 +++++
 2 files changed, 8 insertions(+)
```

- Commits are changes.
- Characterized by a 40-character hash (checksum).
- We see branching points and merging points.
- Often we call the main line development `master`.
- Other than this convention there is nothing special about `master`, it is just a branch.
- Commits form a directed acyclic graph.

### Branches are pointers

- Branches are pointers that point to a commit.
- Branch `master` points to commit `c2`.
- Try this:

```shell
$ cat .git/refs/heads/master
```

- It will echo a long hash, for instance this one.

```shell
7f3582dfbad6539cfa60f5b21bfad41d1b58a618
```

- That is all there is: branch `master` is simply a pointer to a hash.
- `HEAD` is another pointer, it points to where we are right now (currently `master`).

### On which branch are we?

- To see where we are (where HEAD points to) use `git branch`

```shell
$ git branch

* master
```

- This command shows where we are, it does not create a branch.
- There is only `master` and we are on `master` (star is `HEAD`).
- In the following we will learn how to create branches,
  how to switch between them, how to merge branches,
  and how to remove them afterwards.

---

## Exercise: creating and working with branches

- Create a branch called `experiment` where you experiment adding
  cilantro to `ingredients.txt` (if you don't like cilantro, you can add
  another ingredient).
- Create another branch called `less-salt`
  where you reduce the amount of salt.
- Make sure you create both branches from the `master` branch.
- Commit your changes to the respective branches.

Use the following 3 commands:

```shell
$ git branch experiment    # create branch called "experiment" pointing to the present commit
$ git checkout experiment  # switch to branch "experiment"
$ git branch               # list all local branches and show on which branch we are
```

Once you have committed your changes, try:

```shell
$ git log experiment
$ git log less-salt
$ git log master
```

We now have three branches:

```shell
$ git branch

* experiment
  less-salt
  master
```

Here is a graphical representation of what we have created:

![]({{ site.baseurl }}/img/gitink/git-branch-01.svg)













## Basic merging

You can now check the status using **git log** or **git show-branch**

```
$ git log --oneline --decorate --graph --all
* 8afc9c7 (feature1) change hello.py
* ab9544c (HEAD -> master) add .gitignore to ignore temporary Python files
* 94b96db Split hello world functionality to two files.
* f2045a6 initial commit containing a simple hello world example.

$ git show-branch --all
! [feature1] change hello.py
 * [master] add .gitignore to ignore temporary Python files
 --
 +  [feature1] change hello.py
 +* [master] add .gitignore to ignore temporary Python files
```

Both look quite unexiting at the moment. This is because there are only
changes in one branch and that branch can be trivially merged using the *git
merge* command.

```
$ git checkout master
```

This moves the HEAD to point to the tip of the master branch.

![checkout master]({{ site.baseurl }}/img/gitink/git-branch-05.svg "checkout master"){:class="img-responsive"}

```
$ git merge feature1
Updating ab9544c..8afc9c7
Fast-forward
 hello.py | 1 +
  1 file changed, 1 insertion(+)
```

Git used the so-called **fast-forward** strategy. It simply moved the master
branch to point to the same commit as the pointer for feature1.

![ff merge]({{ site.baseurl }}/img/gitink/git-branch-06.svg "ff merge"){:class="img-responsive"}

```
 git log --oneline --decorate --graph --all
 * 8afc9c7 (HEAD -> master, feature1) change hello.py
 * ab9544c add .gitignore to ignore temporary Python files
 * 94b96db Split hello world functionality to two files.
 * f2045a6 initial commit containing a simple hello world example.
 suvileht@air13 test(master)$ git show-branch --all
 ! [feature1] change hello.py
  * [master] change hello.py
  --
  +* [feature1] change hello.py
```

Now that we are happy with the work we did in the branch and the branch it's
time to delete the branch. To do this we use the **-d** handle of git branch.

> ## Deleting branches safely
> git will warn you if you try to delete an unmerged branch with **-d**
>
> If you absolutely know you want to delete an unmerged branch you can do so
> with **-D** but you really need to know what you're doing. Even then your
> commits won't be lost but you may have a hard time finding them as there is
> no reference to them.
{: .callout :}

```
$ git branch
  feature1
* master
$ git branch -d feature1
Deleted branch feature1 (was 8afc9c7).
$ git branch
* master
```

This had the following effect
![git rm branch]({{ site.baseurl }}/img/gitink/git-branch-07.svg "rm branch"){:class="img-responsive"}


### Internals

What happens internally when you merge two branches is that git creates a new
commit, attempts to incorporate changes from both branches and records the
state of all files in the new commit. A merge commit is special in that while
commits typically only have one parent, a merge commit has two.

If the same file is changed in both branches, git attempts to incorporate both
changes into the merged file. If the changes overlap then the user has to
manually settle merge conflicts.

Sometimes only one of the branches has changes. In that case git by default
does something called a **fast-forward**. It only updates the tip of the branch
to be merged to point to the same commit as the branch merged from. This can
sometimes make it less clear when a branch has been merged but on the other
hand it reduces the number of commits in history.


## Another example

Next we will make a change that represents a more complex change. We make the
change in a so-called **feature branch** and when the feature is complete, we
will merge the results back to master.

Edit the files **hello.py** and **runner.py**

```python
def say_hello():
    print("Hello World!")
    print("Bye Bye World!")

def say_something(something):
    if something:
        print(" ".join(something))
    else:
        print("Hello World!")
```

```python
import sys
from hello import say_something

say_something(sys.argv[1:])
```

**Verify that the code works**

At this point you realize that you should have made a branch to isolate these
changes. This is quite common and usually easy to do even after editing. After
all, branching should be easy.

Create a branch called **say_whatever**

```
$ git branch say_whatever
$ git checkout say_whatever
M	hello.py
M	runner.py
Switched to branch 'say_whatever'
```

Now you want to step back and start thinking what kind of a story you will tell
about this feature. Normal features are often somewhat larger, but this serves
as a good training example.

Committing strategies vary. Back in the days of less versatile version control
it was common for an author to make a commit about their work in progress at
the end of the day. This typically lead to the commit messages being something
like "work in progress toward x" or "my work on Monday", which doesn't really
help the next reader to reason about changes.

Most open source projects and others prefer so called **microcommits**, where a
commit should be as small as possible but not smaller.

The opposite of **git commit -a** is **git add -p**. The p stands for patch and
it allows you to select exactly the changes you want to commit and leave other
changes uncommitted. If you want to tell a story then this is certainly
something that you want to make a habit of using.

Now you want to split this into two commits. The first one adds the new
function and the second one starts using it in runner.py.

```
$ git add -p
diff --git a/hello.py b/hello.py
index bef8bd3..e68b52d 100644
--- a/hello.py
+++ b/hello.py
@@ -1,4 +1,11 @@
+
 def say_hello():
     print("Good Morning World!")
     print("Bye Bye World!")
+
+def say_something(something):
+    if something:
+        print(" ".join(something))
+    else:
+        print("Hello World!")
Stage this hunk [y,n,q,a,d,/,s,e,?]?
```

Here git offers you the first **hunk** (a short mostly contiguous piece of
code) and asks if you wish to stage it. Typically the hunk is small enough that
you'd want to stage it entirely but not always.

Answer **y** to the first question. You should get.

```
diff --git a/runner.py b/runner.py
index bdab4ae..651d1a3 100644
--- a/runner.py
+++ b/runner.py
@@ -1,3 +1,5 @@
-from hello import say_hello
+import sys
+from hello import say_something
+
-say_hello()
+say_something(sys.argv[1:])
Stage this hunk [y,n,q,a,d,/,s,e,?]?
```

Answer *n* this time and commit the changes with the message "added function
say_something".

Now run git add -p again, stage the other changes and commit with a message
"started to use the function say_something".

Make a branch off of the **say_whatever** branch called **say_reversed**.

Edit the function say_something by adding the one line described by this git diff

```
git diff
diff --git a/hello.py b/hello.py
index e68b52d..2ae5426 100644
--- a/hello.py
+++ b/hello.py
@@ -6,6 +6,7 @@ def say_hello():

 def say_something(something):
     if something:
+        something.reverse()
         print(" ".join(something))
     else:
         print("Hello World!")
```

Effectively this will reverse the order of words printed.

Commit the changes with an optional message and go back to the branch
**say_whatever**.

Now you realize that the old say_hello function is not used at all and you
don't want it hanging around. It's just dead weight and it's not as if it will
be entirely gone. If you need to revert back to it the version containing
say_hello will still be available in the history of your project.

Edit **hello.py** so that it looks like this

```python

def say_something(something):
    if something:
        print(" ".join(something))
    else:
        print("Hello World!")
```

> ## Task
> Stage the file and commit the changes with the message "removed unused
> say_hello function".
{: .task :}

Now we're at a slightly different situation.

![branch ex3 1]({{ site.baseurl }}/img/gitink/git-branch-3-01.svg
"branch ex3 1"){:class="img-responsive"}


```
git log --graph --abbrev-commit --decorate --all
* commit 8a4950b (HEAD -> say_whatever)
| Author: Joe Example <joe@example.org>
| Date:   Mon Dec 12 10:10:46 2016 +0200
|
|     remove unused say_hello function
|
| * commit 8d3859e (say_reversed)
|/  Author: Joe Example <joe@example.org>
|   Date:   Mon Dec 12 09:57:10 2016 +0200
|
|       reverse order of words
|
* commit f1ba6f0
| Author: Joe Example <joe@example.org>
| Date:   Mon Dec 12 09:51:02 2016 +0200
|
|     added function say_something
|
* commit f1ba6f0
| Author: Joe Example <joe@example.org>
| Date:   Mon Dec 12 09:51:02 2016 +0200
|
|     added function say_something
|
*   commit c79ff2c (master)
|\  Merge: 2e69aab b3d5dd4
| | Author: Joe Example <joe@example.org>
| | Date:   Mon Dec 12 09:11:57 2016 +0200
| |

...
```

Graphically it looks like this

![branch 03 01]({{ site.baseurl }}/img/gitink/git-branch-3-01.svg
"git branch 03 01"){:class="img-responsive"}


There are two branches, **say_whatever** and **say_reversed** and they are both
ahead of the master branch.

There are several ways you could go about doing this:
* You could first merge **say_whatever** and then merge **say_reversed** to the master branch.
* You could merge **say_reversed** to **say_whatever** and then merge **say_whatever** to master.
* You could do something a bit more advanced called a [rebase but we will not cover it here and now

Let's use the second option this time.

```
$ git checkout say_whatever
$ git merge say_reversed
Auto-merging hello.py
Merge made by the 'recursive' strategy.
 hello.py  | 1 +
 runner.py | 6 ++++--
2 files changed, 5 insertions(+), 2 deletions(-)
```

First merge took place without a hitch. This was a so-called **recursive
merge**. This means that git found the common ancestor of both branches,
figured what has changed in both branches and combined the changes to create
the merge automatically. This is what usually happens unless two branches edit
the same code.

![branch 03 02]({{ site.baseurl }}/img/gitink/git-branch-3-02.svg
"git branch 03 02"){:class="img-responsive"}

Now for the second.

```
$ git checkout master
$ git merge say_whatever
Updating c79ff2c..dc39fc3
Fast-forward
 hello.py  | 10 +++++++---
 runner.py |  6 ++++--
 2 files changed, 11 insertions(+), 5 deletions(-)
$ git branch -d say_reversed
Deleted branch say_reversed (was 8d3859e).
$ git branch -d say_whatever
Deleted branch say_whatever (was dc39fc3).
$ git log --graph --abbrev-commit --decorate --all
*   commit dc39fc3 (HEAD -> master)
|\  Merge: 8a4950b 8d3859e
| | Author: Joe Example <joe@example.org>
| | Date:   Mon Dec 12 10:20:56 2016 +0200
| |
| |     Merge branch 'say_reversed' into say_whatever
| |
| * commit 8d3859e
| | Author: Joe Example <joe@example.org>
| | Date:   Mon Dec 12 09:57:10 2016 +0200
| |
| |     reverse order of words
| |
* | commit 8a4950b
|/  Author: Joe Example <joe@example.org>
|   Date:   Mon Dec 12 10:10:46 2016 +0200
|
|       remove unused say_hello function
...
```

Now that the changes didn't overlap that wasn't painful at all. The second
merge could be made with the fast-forward strategy so it didn't require a
merge commit.

![branch 03 03]({{ site.baseurl }}/img/gitink/git-branch-3-03.svg
"git branch 03 03"){:class="img-responsive"}

















---

## Tags

A branch is a pointer to a commit.

A tag is a pointer to a commit, too.

The difference between a branch and a tag is that a branch pointer moves
forward as we add commits, whereas a tag should always **point to the same
commit**.

We use tags to record particular states or milestones of a project at a given
point in time, like for instance versions (have a look at [semantic
versioning](http://semver.org)).

There are two basic types of tags: annotated and lightweight. **Use annotated
tags** since they contain the author and can be cryptographically signed using
GPG, timestamped and a message attached.

For more information about tags see for example
[the Pro Git book](https://git-scm.com/book/en/v2/Git-Basics-Tagging) chapter on the
subject.
