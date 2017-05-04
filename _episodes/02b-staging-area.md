---
layout: episode
title: "Using the Git staging area"
teaching: 20
exercises: 25
#questions:
#  - "What is Git?"
#  - "What is a repository?"
#  - "How do I make commits?"
#  - "How do I select what to commit?"
#  - "How can I undo things?"
#objectives:
#  - "Learn to create Git repositories and make commits."
#  - "Get a grasp of the structure of a repository."
#keypoints:
#  - "Commits should be used to tell a story."
#  - "Git uses the .git folder to store the snapshots."
---

### States of a file.

In general files can have one of 4 states inside a git repository. *Image CC BY 3.0 from the Pro Git book.*

![States of a git file]({{ site.baseurl }}/img/lifecycle.png "States of a git file. License CC BY 3.0"){:class="img-responsive"}

> ## Make a change
> Make a change to hello.py. You can add a comment or something similar, the
> nature of the change is not important.
>
{. :task :}

```
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   hello.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Now you can add the changes using **git add** as the message tells you. You
could also discard the changes with **git checkout --**.


> ## **git checkout --** behaviour
>
> The purpose of git checkout -- is to **erase** uncommitted changes you made
> to a file. This means that you will irrevocably lose those changes.
> Usually this is what you want but it is good to keep in mind so you don't lose what you don't want to.
>
> In the context of the state diagram above git checkout will move the file from modified to unmodified.
{: .callout :}

Let's instead move the file from modified to staged.

```
$ git add hello.py
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   hello.py

```

Now the file is staged, which means it will be committed when you make the commit.

Notice how git tells you what changes it will make with the commit and gives
you instructions on the things you might want to do.

You can move back, i.e. unstage the change with **git reset HEAD**

```
$ git reset HEAD hello.py
Unstaged changes after reset:
M	hello.py
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   hello.py

no changes added to commit (use "git add" and/or "git commit -a")
```

> ## Commit the change
> Go ahead and stage the change again and commit it with a descriptive message.
{: .task :}
