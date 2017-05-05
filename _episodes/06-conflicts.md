---
layout: episode
title: "Conflict resolution"
teaching: 10
exercises: 10
#questions:
#  - "How can I or my team work on multiple features in parallel?"
#  - "How to combine the changes in parallel tracks of work?"
#  - "What is branching and when should I do it?"
#  - "How can I permanently reference a point in history, like a software
#    version?"
#objectives:
#  - "Student can create and merge branches"
#  - "Student understand the system sufficiently to fix small merge conflicts"
#  - "Student knows about tags"
#  - "Students get to exercise making commits"
#keypoints:
#  - A branch is a division unit of work, to be merged with other units of
#    work
#  - Creating and merging branches is simple in git
#  - Creating and merging branches is not always straightforward
#  - A tag is a pointer to a moment in the history of the project

---

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

In the case of two conflicting versions of the
same line Git doesn't know which one to choose and you as a human must make the
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
