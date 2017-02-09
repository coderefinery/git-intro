---
layout: episode
title: "Branching and Merging"
teaching: 20
exercises: 25
questions:
  - "How can I or my team work on multiple features in parallel?"
  - "How to combine the changes in parallel tracks of work?"
  - "What is branching and when should I do it?"
  - "How can I permanently reference a point in history, like a software
    version?"
objectives:
  - "Student can create and merge branches"
  - "Student understand the system sufficiently to fix small merge conflicts"
  - "Student knows about tags"
  - "Students get to exercise making commits"
keypoints:
  - A branch is a division unit of work, to be merged with other units of
    work
  - Creating and merging branches is simple in git
  - Creating and merging branches is not always straightforward
  - A tag is a pointer to a moment in the history of the project

---

## Food for thought
- How do you work on two things in parallel?
- How often do you find yourself wanting to go into two directions at once?

---

## Branches

Software develompent isn't linear. The strength of version control is that it
permits the developers to isolate different tracks of work so that they can be
isolated from one another. Developers can work on different things and merge
the changes they made to the source code files afterwards to create a
composite version that contains both the changes.


Up until now our repository has only had one branch with one commit coming
after the other, as depicted in the following.

![Linear]({{ site.baseurl }}/img/gitink/git-branch-01.svg "Linear git
repository"){:class="img-responsive"}

To enable collaborative work we wish to do something more like

![Git collaborative]({{ site.baseurl }}/img/gitink/git-collaborative-work.svg
"description"){:class="img-responsive"}

A group of commits that create a single narrative are called a **branch**.
There are different branching strategies, but it's easy to think that a branch
tells the story of a feature. E.g. "new login workflow" or "fixing bug in
matrix inversion algoritm" might be logical branches.

## Branching

### Git branch

By default when you create a new repository git creates a branch called
**master**. You can check the branch you are on by calling the **git branch**
command without any parameters.

```
$ git branch
* master
```

This lists local branches and shows which one you are on using an asterisk
(\*).

Giving the command a branch name will create a new local branch.

```
$ git branch devel
$ git branch
  devel
  * master
```

Observe that creating a branch didn't automatically switch you to said branch.
To switch to another branch you checkout the branch using **git checkout**.

```
$ git checkout devel
Switched to branch 'devel'
$ git branch
* feature1
  master
```

Now, edit the hello world string in your hello.py to something else, e.g.

``` python
def say_hello():
    print("Hello World!")
    print("Bye Bye World!")
```


> ## Challenge
>
> Now add and commit this change using **git commit** and **git add**.
>
> What commands did you use?
>
> > ## Example solution
> >
> > ```
> > $ git add hello.py
> > $ git commit -m "change hello.py"
> > ```
> {: .solution }
{: .challenge :}


### Under the hood

Every commit in git is stored as a file and all but the first commit store a
reference to a previous commit to create the directed acyclic graph mentioned
earlier.

Branches are pointers to individual commits. When you create a new branch git
creates a new pointer to the commit that you're currently at. Then when you
make a new commit, the pointer for the branch you are on is updated to point to the new header.

HEAD is a file under .git/ and it points to the head of the current branch you
are on. When you switch branches, git finds the head of the branch under
.git/logs/heads and sets that as HEAD. Then it proceeds to ensure that all the
versioned files are in the version specified by the HEAD unless they have been
changed.

When you first created the branch the situation looked like this.

![Linear]({{ site.baseurl }}/img/gitink/git-branch-02.svg "Linear git
repository"){:class="img-responsive"}

Git had created a new pointer, feature1 to point to the same commit as master.

Running **git checkout feature1** changed the situation like this.

![Linear]({{ site.baseurl }}/img/gitink/git-branch-03.svg "Linear git
repository"){:class="img-responsive"}

Now HEAD points to another branch, which still points to the same commit.

After you made the commit the histories diverged.

![Linear]({{ site.baseurl }}/img/gitink/git-branch-04.svg "two branches with one
different commit"){:class="img-responsive"}

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

## Make conflicting changes in 2 branches

### Make a branch and create a commit

> ## task
> Make a new branch called **feature2**
> Edit the file so that the first print statement says. "Good Morning World!" and commit the changes.
{: .task :}

> ## Challenge
> What commands did you use?
>
> > ## Solution
> > ```
> > $ git branch feature2
> > $ git checkout feature2
> > [something to edit the file]
> > $ git add hello.py
> > $ git commit -m "changed hello string"
> > ```
> {: .solution }
{: .challenge :}

Now, check out the master branch with

```
$ git checkout master
```


> Repeat the above steps and create a branch called **feature3** with the
> text "Good Afternoon World!".
{: .task :}

## Merge conflicts

Now we face a typical situation called a merge conflict. We already know that
the two changes we made change the same line of code. Typically we would want
to avoid this, but it's never possible to entirely avoid merge conflicts.

```
git show-branch --all
! [feature2] edited hello.py with a morning message
 ! [feature3] edited hello.py with an afternoon message
  * [master] change hello.py
---
 +  [feature3] edited hello.py with an afternoon message
+   [feature2] edited hello.py with a morning message
++* [master] change hello.py
```
and

```
git log --oneline --decorate --graph --all
* b3d5dd4 (feature3) edited hello.py with an afternoon message
| * 2e69aab (feature2) edited hello.py with a morning message
|/
* 8afc9c7 (HEAD -> master) change hello.py
* ab9544c add .gitignore to ignore temporary Python files
* 94b96db Split hello world functionality to two files.
* f2045a6 initial commit containing a simple hello world example.
```

Both of the examples try to visualize the same situation. Feature 2 and feature
3 have ben branched off from master and have a commit with changes in them.

The end result looks something like this
![git merge 2 1]({{ site.baseurl }}/img/gitink/git-branch-2-01.svg "merge beginning"){:class="img-responsive"}

Let's merge the first branch

```
$ git checkout master
$ git merge feature2
Updating 8afc9c7..2e69aab
Fast-forward
 hello.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

OK that went without a problem. In fact git was able to use the **fast
forward** strategy so it was just able to move the pointer for master forward
to the tip of feature2 branch. No new merge commit needed.

The result looks like this
![git merge 2 2]({{ site.baseurl }}/img/gitink/git-branch-2-02.svg "merge first"){:class="img-responsive"}

Now let's try to merge the second branch.

```
$ git merge feature3
Auto-merging hello.py
CONFLICT (content): Merge conflict in hello.py
Automatic merge failed; fix conflicts and then commit the result.
```

Git is just a stupid program so in the case of two conflicting versions of the
same line it doesn't know which one to choose and you as a human must make the
choice.

Git is trying to create a new merge commit, m1 that would combine commits b1
and d1 but it can't, because they change the same line of code.

![git merge 2 3]({{ site.baseurl }}/img/gitink/git-branch-2-03.svg "merge first"){:class="img-responsive"}

Note how git again tells you exactly what you should do: you should fix
conflicts and then commit the result.

As always you can check your status with **git status**.

```
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")

Unmerged paths:
  (use "git add <file>..." to mark resolution)

        both modified:   hello.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Now look at the file hello.py with a text editor or **cat**

```
$ cat hello.py
def say_hello():
<<<<<<< HEAD
    print("Good Morning World!")
=======
    print("Good Afternoon World!")
>>>>>>> feature3
    print("Bye Bye World!")
```

The root of the problem here is that the changes made in the different branches
__overlap__, i.e. they change the same lines of code. Most of the time this
does not happen and there is no need to handle merge conflicts.  The working
practices and software structure are often designed with parallel work in mind
but this is the topic of other lessons.

Git has made a composite version of the file that contains both alternatives
for the same length of text. The one labeled HEAD is the version in the current
branch (i.e. master) and the one labeled feature3 is from that branch.

Now you need to manually edit the merge commit before it can be accepted.

> ## Merge the changes
> Edit the file and leave either of the print statements and edit out the
> lines with angle brackets and equals signs.
>
> Note that there is no requirement to leave either of
> the existing statements. You can edit the file freely to e.g. combine the
> functionality in both branches if you want.
{: .task :}

After you commit your changes the history will look like this
![git merge 2 4]({{ site.baseurl }}/img/gitink/git-branch-2-04.svg "merge fourth"){:class="img-responsive"}



Now since we made just one small commit we'll cut a corner and use **git commit
-a** to commit our merge.

```
$git commit -a -m "manually merge different hello statements"
[master c79ff2c] manually merge different hello statements

$ git status
On branch master
nothing to commit, working tree clean

$ git log --graph --abbrev-commit --decorate
*   commit c79ff2c (HEAD -> master)
|\  Merge: 2e69aab b3d5dd4
| | Author: Joe Example <joe@example.org>
| | Date:   Mon Dec 12 09:11:57 2016 +0200
| | 
| |     manually merge different hello statements
| |   
| * commit b3d5dd4 (feature3)
| | Author: Joe Example <joe@example.org>
| | Date:   Thu Dec 8 12:10:07 2016 +0200
| | 
| |     edited hello.py with an afternoon message
| |   
* | commit 2e69aab (feature2)
|/  Author: Joe Example <joe@example.org>
|   Date:   Thu Dec 8 12:08:26 2016 +0200
|   
|       edited hello.py with a morning message
|  
* commit 8afc9c7
| Author: Joe Example <joe@example.org>
| Date:   Thu Dec 8 11:47:36 2016 +0200
| 
|     change hello.py
...
```

The **-a** handle tells git commit to merely stage all the changed files that
are tracked by git. It's simple but if overused it can make the next person
somewhat surprised at what has happened. If you make more than one change then
the use of **-a** conflicts with the idea of telling a story about your project
to the next person maintaining it.

Now that you no longer need the old branches you can delete them.

> ## Task
> Delete the branches
> 
{: .task :}

> ## Challenge
> What commands did you use?
>
> > ## Example solution
> > ```
> > $git branch -d feature2
> > Deleted branch feature2 (was 2e69aab).
> > $ git branch -d feature3
> > Deleted branch feature3 (was b3d5dd4).
> > ```
> {: .solution }
{: .challenge :}

You don't have to delete branches immediately but at some point you should as
after merging they just take up useless screen space.

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

if __name__ == "__main__":
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
 if __name__ == "__main__":
-    say_hello()
+    say_something(sys.argv[1:])
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

## Tags

So far we have dealt with branches. A branch is semantically a line of of
develompent that can be updated as the work progresses. Internally it is
represented as a pointer to a commit file in the .git/log/ directory. The
commit references it's parent (or two parents if it's a merge commit) and so
on recursively untile the initial commit.

Another thing that we sometimes want to do is to record the exact state of the
project at a given point in time, like for instance versioning. (If in doubt
about how to version, check [Semantic Versioning](http://semver.org/)). The
main difference between tags and branches is that once created, a tag should
always point to the same commit.

The **git tag** command lets you do things with tags.

```
$ git tag
$
```

When used with no extra commands **git tag** lists existing tags. When given a
string it will create a tag with that string as the name of the tag.

```
$ git tag 0.1.0
$ git tag
0.1.0
```

So we created a tag. Now let's try checking out the tag.

```
$ git checkout 0.1.0
Note: checking out '0.1.0'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at dc39fc3... Merge branch 'say_reversed' into say_whatever
```

Now git is telling us that we checked out a particular commit but we are not on
any branch. The message really tells it rather nicely. One of the most
difficult things about using git is reading the messages it gives you.

Visually it looks like this

![detached head]({{ site.baseurl }}/img/gitink/git-detached-head.svg
"detached head"){:class="img-responsive"}

Detached HEAD means that HEAD doesn't point to a branch which points to a
commit but to a specific commit without any branch association.

```
$ git status
HEAD detached at 0.1.0
nothing to commit, working tree clean
```

Now edit the "Hello World" string in **hello.py**.

```
$ git status
HEAD detached at 0.1.0
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   hello.py

no changes added to commit (use "git add" and/or "git commit -a")
```

We can commit as we always would.

```
$ git add hello.py
$ git commit -m "test"
[detached HEAD c1a0c9d5] test
 1 file changed, 1 insertion(+), 1 deletion(-)
```

The challenge now is that if we check out another branch we will have a hard
time finding this commit that we just made. It will be recorded and stored
safely but you'd need to have stored the "c1a0c9d5" reference to it to be able
to check it out.

The best thing to do if you want to keep the change and be able to use it is to
make a branch, just as the help suggested.

```
$ git checkout -b change_hello
Switched to a new branch 'change_hello'
$ git branch
* change_hello
  master
```

Now you have the option of going back to the changes you made on top of tag
0.1.0 and merge them to master (or some other branch).

### Types of tags

There are two basic types of tags: annotated and lightweight. The example shown
previously was a lightweight tag. It's just a pointer like a branch object. An
annotated tag is stored as an object, it can be cryptographically signed using
GPG, timestamped and a message attached.

For more information about tags see for example
[the Pro Git book](https://git-scm.com/book/en/v2/Git-Basics-Tagging) chapter on the
subject.
