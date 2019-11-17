---
layout: episode
title: "Inspecting history"
teaching: 15
exercises: 20
questions:
  - How can we find out who introduced a line of code and when exactly?
  - How can we find out which commit broke or changed a functionality?
objectives:
  - Quickly find a line of code, find out who introduced it, when, and why.
  - Quickly find the commit that changed a behavior.
keypoints:
  - "`git log/grep/blame/show/bisect` is a powerful combination when doing archaeology in a project."
  - "`git checkout -b <name> <hash>` is the recommended mechanism to inspect old code"
---


## Preparation
Please make sure that you do not clone repositories inside an already tracked folder.
Tip: issue the command
```shell
$ git status
```
Inside the folder and if it is an untracked location you will see the message
"fatal: not a git repository (or any of the parent directories): .git".
If you get an message starting with "On branch .. " then you should stop and
find a different location.

Clone the repository of an example project from
[https://github.com/coderefinery/git-archaeology-exercise](https://github.com/coderefinery/git-archaeology-exercise)
(we will also use this project in later lessons):

```shell
$ git clone https://github.com/coderefinery/git-archaeology-exercise
$ cd git-archaeology-exercise
```

This example project counts words in a given text file and writes as
output the frequency distribution. Example usage:
```shell
$ python source/wordcount.py data/abyss.txt output.dat
$ head output.dat
```

## Inspecting commits

At any moment we can inspect individual commits with `git show`.
Let's first find the earliest commits to this repository:
```shell
$ git log --reverse

commit 6b0d3ea13da63876a69c97abe3274d5a0aee711a
Author: Kjartan Thor Wikfeldt <ktwikfeldt@gmail.com>
Date:   Mon Oct 21 16:37:13 2019 +0200

    initial commit - readme

commit b3f33c5dfc8081eef746cf2d4c59fab2095d7c2e
Author: Kjartan Thor Wikfeldt <ktwikfeldt@gmail.com>
Date:   Mon Oct 21 16:40:22 2019 +0200

    add first step to read input file

...
```

and then use `git show` to display the changeset for the second commit:

```
$ git show b3f33c5d

commit b3f33c5dfc8081eef746cf2d4c59fab2095d7c2e
Author: Kjartan Thor Wikfeldt <ktwikfeldt@gmail.com>
Date:   Mon Oct 21 16:40:22 2019 +0200

    add first step to read input file

diff --git a/wordcount.py b/wordcount.py
new file mode 100644
index 0000000..55bdade
--- /dev/null
+++ b/wordcount.py
@@ -0,0 +1,14 @@
+import sys
+
+def load_text(filename):
+    """
+    Load lines from a plain-text file and return these as a list, with
+    trailing newlines stripped.
+    """
+    with open(filename, "r") as input_fd:
+        lines = input_fd.read()
+    return lines
+
+if __name__ == '__main__':
+    input_file = sys.argv[1]
+    lines = load_text(input_file)
```

We see that the start of the hash is enough if it is unique.

Compare this with: [https://github.com/coderefinery/git-archaeology-exercise/commit/b3f33c5d](https://github.com/coderefinery/git-archaeology-exercise/commit/b3f33c5d)

We can also check the git log of a single file:
```shell
$ git log --oneline source/wordcount.py

28287ac mv source files to source directory
```

Hmm, I'm sure there were more commits made to this file. Maybe it has been moved?

```shell
$ git log --oneline --follow source/wordcount.py

28287ac mv source files to source directory
5224a2e adding docstrings
55e951a mv writing of output file to function
a781e56 express in percentages instead
bba58cb filter by minimum word length
a177c8e sort the word count
9651983 write word count to given output filename
3cffe78 replace all delimiters with blank space
94cc9a6 mv update of word counts to separate function
ef9133d add functions to count words in given text file
bfea209 should split the lines on newlines
b3f33c5 add first step to read input file
```

---

## Grepping code

What if the combination of `git log` and `git show` is not enough to find what we need?

```shell
$ git grep -i percentage

data/abyss.txt:In 1886, and up to 1893, the percentage of pauperism to population was
data/abyss.txt:succeeding year, the percentage of pauperism to population has been
data/abyss.txt:                   Percentage of
data/abyss.txt:percentage of those in the lunatic asylums.  Among the males each year,
data/last.txt:large percentage of the floes is quite thin and even the heavier ice
data/last.txt:harm. During quite a large percentage of days, however, we had bright
data/last.txt:capacity with food from which he could derive only a small percentage
data/last.txt:at Cape Evans--the record shows an extraordinary large percentage
data/last.txt:described (titration, a colorimetric method of measuring the percentage
source/wordcount.py:    Save a list of [word, count, percentage] lists to a file, in the form
source/wordcount.py:    "word count percentage", one tuple per line.
source/wordcount.py:def calculate_percentages(counts):
source/wordcount.py:    percentage) where percentage is the percentage number of occurrences
source/wordcount.py:    save in a new file the words, counts and percentages of the total  in
source/wordcount.py:    percentage_counts = calculate_percentages(sorted_counts)
source/wordcount.py:    save_word_counts(output_file, percentage_counts)
```

- Greps entire repository below current directory.
- Super fast. Sometimes it is worth creating a Git repository just for one `git grep`.

---

## Finding out who introduced a modification and when

- `git blame` is a fun and useful command to find out when a specific line got introduced and by whom.
- This is important to judge the impact of a bug:
  - When was it introduced?
  - For how long has this bug been around?
  - Has this bug been released?
  - Has this buggy code been used by others?
  - Who introduced it? Not to blame people but to possibly get more information.

```shell
$ git blame source/wordcount.py

b3f33c5d wordcount.py (Kjartan Thor Wikfeldt 2019-10-21 16:40:22 +0200   1) import sys
b3f33c5d wordcount.py (Kjartan Thor Wikfeldt 2019-10-21 16:40:22 +0200   2)
3cffe784 wordcount.py (Kjartan Thor Wikfeldt 2019-10-21 17:51:54 +0200   3) DELIMITERS = ". , ; : ? $ @ ^ < > # % ` ! * - = ( ) [ ] { } / \" '".split()
3cffe784 wordcount.py (Kjartan Thor Wikfeldt 2019-10-21 17:51:54 +0200   4)
3cffe784 wordcount.py (Kjartan Thor Wikfeldt 2019-10-21 17:51:54 +0200   5)
b3f33c5d wordcount.py (Kjartan Thor Wikfeldt 2019-10-21 16:40:22 +0200   6) def load_text(filename):
b3f33c5d wordcount.py (Kjartan Thor Wikfeldt 2019-10-21 16:40:22 +0200   7)     """
b3f33c5d wordcount.py (Kjartan Thor Wikfeldt 2019-10-21 16:40:22 +0200   8)     Load lines from a plain-text file and return these as a list, with
b3f33c5d wordcount.py (Kjartan Thor Wikfeldt 2019-10-21 16:40:22 +0200   9)     trailing newlines stripped.
b3f33c5d wordcount.py (Kjartan Thor Wikfeldt 2019-10-21 16:40:22 +0200  10)     """
b3f33c5d wordcount.py (Kjartan Thor Wikfeldt 2019-10-21 16:40:22 +0200  11)     with open(filename, "r") as input_fd:
bfea209f wordcount.py (Kjartan Thor Wikfeldt 2019-10-21 16:40:47 +0200  12)         lines = input_fd.read().splitlines()
b3f33c5d wordcount.py (Kjartan Thor Wikfeldt 2019-10-21 16:40:22 +0200  13)     return lines
...
```

Rather typical timeline:

> *"Who the %&!@!!! wrote this crap?!? Oh, it was me."*

Who was the last to edit a specific line of the source file for `git blame` and when and why?

- [https://github.com/coderefinery/git-archaeology-exercise/blame/master/source/wordcount.py](https://github.com/coderefinery/git-archaeology-exercise/blame/master/source/wordcount.py)

---

## Grepping commit messages

- Another possible scenario is that you're looking for a particular commit, but can't
easily find it with `git blame`.
- You can however remember (or guess) some keywords from the commit message
- Commit messages can also be grepped!

Example:
```
$ git log --oneline  --grep "word count"

a177c8e sort the word count
9651983 write word count to given output filename
94cc9a6 mv update of word counts to separate function
```

Note that `git log --grep` will grep the whole commit message even if you use the `--oneline` option.

---

## Finding a developer to talk to (large projects)

Example: you want to know who implemented a specific keyword/functionality.

- `git grep` for the keyword or screen message.
- Then with `git blame` find the person/commit that introduced it.
- With `git show` verify the commit that introduced the change.

---

## Going back in time

We do not have to branch from the tip of the branch (HEAD).
We can branch from arbitrary (earlier) hash:

```shell
$ git checkout -b <name> <hash>
```

This is the recommended mechanism to inspect old code (example: hash *abc123*):

```shell
$ git checkout -b museum abc123  # create branch called "museum" from hash abc123
  # do some archaeology ...
  # "What was I thinking back then!?"
  # "Aha! Hmm."
$ git checkout master            # after you are done switch back to "master"
$ git branch -d museum
```

Branches help us to keep the repository organized.

---

> ## Archaeology exercise
>
> There used to be another test function in the git-archaeology-exercise repository,
> but now it's gone. You remember that the function started with "test".
> - Try to find the commits in which the function was introduced and later removed
> - Inspect the commits. What was the function called?
> - Create a new branch to point at the commit **before** the commit where that test
>   function was removed, and inspect the `source` folder.
>   Hint: To refer to a commit before a given commit hash, use `<HASH>~1`.
{: .task}

---

## Finding out when something broke

> *But I am sure it used to work! Strange.*

- Sometimes you realize that something broke.
- You know that it used to work.
- You do not know when it broke.
- First find out a commit in past when it worked.
- Then bisect your way until you find the commit that broke it.

```shell
$ git bisect start
$ git bisect good f0ea950  # this is a commit that worked
$ git bisect bad master    # last commit is broken
  # now compile and/or run
  # after that decide whether
$ git bisect good
  # or
$ git bisect bad
  # now compile and/or run
  # after that decide whether
$ git bisect good
  # or
$ git bisect bad
  # iterate until commit is found
```

- This can even be automatized with `git bisect run <script>`.
- For this you write a script that returns zero/non-zero (success/failure).

---

> ## Git bisect exercise
>
> Clone [https://github.com/coderefinery/git-bisect-exercise](https://github.com/coderefinery/git-bisect-exercise).
>
>
> #### Motivation
>
> The motivation for this exercise is to be able to do archaeology with Git on a
> source code where the bug is difficult to see visually. **Finding the offending
> commit is often more than half the debugging**.
>
>
> #### Background
>
> The script `get_pi.py` approximates pi using terms of the Nilakantha series. It
> should produce 3.14 but it does not. The script broke at some point and
> produces 3.57 using the last commit:
>
> ```
> $ python get_pi.py
>
> 3.57
> ```
>
> At some point within the 500 first commits, an error was introduced. The only
> thing we know is that the first commit worked correctly.
>
>
> #### Your task
>
> Clone or fork this repository and use `git bisect` to find the commit which
> broke the computation
> ([solution - spoiler alert!](https://github.com/coderefinery/git-bisect-exercise#solutions-spoiler-alert)).
>
>
> #### How to find the first commit
>
> ```
> $ git log --oneline | tail -n 1
> ```
{: .task}

> ## Bonus exercise
>
> Write a script that checks for a correct result and use `git bisect run` to
> find the offending commit automatically
> ([solution - spoiler alert!](https://github.com/coderefinery/git-bisect-exercise#solutions-spoiler-alert)).
{: .task}
