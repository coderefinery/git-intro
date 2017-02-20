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


---

### Creating an empty directory

Sometimes you might want to have an empty directory in your git repository.
Unfortunately that's not exactly possible, because git operates on files and a
directory is not a file.

Fortunately for most cases the directory doesn't have to be entirely empty and
it's permitted to have a so-called hidden file (starting with a .) in the
directory.

To create an empty directory that will be ignored (i.e. you won't accidentally
add build artefacts to your repository) add the following .gitignore to the
folder and then commit.

```
# Ignore everything in this directory
*
# Except this file
!.gitignore
```

### .gitignore glob syntax

.gitignore uses something called a
[shell glob syntax](https://en.wikipedia.org/wiki/Glob_(programming) for
determining file patterns to ignore. You can read more about the syntax
[in git documentation](https://git-scm.com/docs/gitignore)

An example from said documentation

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

As you noticed you can have .gitignore files in lower level directories for
fine-tuned control. If you reference paths all the paths will be interpreted
**relative to the location** of the .gitignore file, not the root of the
repository.

### Food for thought

* Why is it considered a bad idea to commit compiled binaries to version control?
