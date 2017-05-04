---
layout: episode
title: "Extra: Moving stuff around"
teaching: x min
exercises: y min
questions:
  - "How do I rename files in a git repository?"
  - "How do I restructure my project?"
objectives:
  - "Student can restructure a project when the need arises"
keypoints:
  - "Remember to use **git rm** and **git mv** instead of the normal ones."
---

## Extra material

This is an extra section to cover if there is time. Everything in it can be
picked up in a short time if one wants.

## Moving files

In the Unix world there is no renaming of files. Files are simply moved. As an
example

```
$ cd /tmp/
$ touch file1
$ mv file1 file2
```

The git philosophy is similar.

Let's try it out

```
$ cd testrepo
$ mv hello.py say.py
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	deleted:    hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	say.py

```

This doesn't look too good. Git doesn't realize that we wanted to rename the
file. It thinks a file has been deleted and a new one created. If you were to
commit this change we would lose all version history from before the name was
changed.

Let's go back. We can check out the latest version of hello.py using **git
checkout --** (there are other ways as well but ignore those for now)

```
$ git checkout -- hello.py
$ rm say.py
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working tree clean
```

> ## Using git checkout may be dangerous
>
> git checkout will check out the last stored version of your file and discard
> any unsaved changes. Usually you use it because you want this exact
> behaviour but be aware that uncommitted changes will truly be lost.
{: .callout :}



Let's try the eponymous **git mv** command instead.

```
$ git mv hello.py say.py
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	renamed:    hello.py -> say.py
```

Now git understands what we want it to do.

To maintain the system functionality we must change runner.py so that we get the following **git diff**

```
$ git diff runner.py
diff --git a/runner.py b/runner.py
index 651d1a3..6f6f54b 100644
--- a/runner.py
+++ b/runner.py
@@ -1,5 +1,5 @@
 import sys
-from hello import say_something
+from say import say_something

 say_something(sys.argv[1:])
```

Go ahead and make the change and commit.

## Removing files and undoing commits

Unsurprisingly there's also a **git rm** command.

Go ahead and run

```
$ git rm say.py
rm 'say.py'
$ git commit -m "remove say.py"
[master 145ef1f] remove say.py
 1 file changed, 9 deletions(-)
 delete mode 100644 say.py

$ python runner.py
Traceback (most recent call last):
  File "runner.py", line 2, in <module>
    from say import say_something
ImportError: No module named say
```

Oh dear, we removed something that was essential to the working of the program! Fortunately that's why we're under version control. Reverting to the previous version is simple, especially since you havent **pushed** your changes anywhere yet and they aren't public.

To undo the act of making the commit just run

```
$ git reset HEAD~1
```

And the pointer to the head will be taken one step backwards (hence the ~1).
Now you can do the same steps as above to reset the state of the file by checking it out.

Alternatively you could have just run

```
$ git reset --hard HEAD~1
```

> ## Using reset --hard is dangerous!
> The --hard selector makes git restore the content of your working directory
> *exactly* as it was in the commit referenced. It will discard any local
> changes and you may lose unsaved work.
>
> You should always stop to think before using --hard.
{: .callout :}
