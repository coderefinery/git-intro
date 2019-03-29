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
[https://github.com/coderefinery/word-count](https://github.com/coderefinery/word-count) 
(we will also use this project in later lessons):
```shell
$ git clone https://github.com/coderefinery/word-count
$ cd word-count
```
## Inspecting commits

At any moment we can inspect individual commits with `git show`. 
Let's first find the earliest commits to this repository:
```shell
$ git log --reverse

commit c4a32caae2f0ddc4d85481f5adf61360198edc2f
Author: Kjartan Thor Wikfeldt <ktwikfeldt@gmail.com>
Date:   Tue May 8 15:15:48 2018 +0200

    initial commit

commit a0cc9e1d0ef853464cd0019479f6ac4eb4ba88c7
Author: Kjartan Thor Wikfeldt <ktwikfeldt@gmail.com>
Date:   Tue May 8 15:24:57 2018 +0200

    add license and credit to SWC

...
```

and then use `git show` to display the changeset for the second commit:

```
$ git show a0cc9e1d0

commit a0cc9e1d0ef853464cd0019479f6ac4eb4ba88c7
Author: Kjartan Thor Wikfeldt <ktwikfeldt@gmail.com>
Date:   Tue May 8 15:24:57 2018 +0200

    add license and credit to SWC

diff --git a/README.md b/README.md
index 8fe4059..d11eb04 100644
--- a/README.md
+++ b/README.md
@@ -1,8 +1,9 @@
-[![License](https://img.shields.io/badge/license-%20MPL--v2.0-blue.svg)](../master/LICENSE)
-
-
 # Word count example

+This example project is inspired by and derived from
+work by [Software Carpentry](http://software-carpentry.org) licensed under the
+[Creative Commons Attribution license (CC BY4.0)](https://creativecommons.org/licenses/by/4.0/).
+
 These programs will count words in a given text, plot a bar chart of the 10 mos
t common words,
 and test [Zipf's law](https://en.wikipedia.org/wiki/Zipf%27s_law) on the two mo
st common words.
...
```

We see that the start of the hash is enough if it is unique.

Compare this with: [https://github.com/coderefinery/word-count/commit/a0cc9e1d0](https://github.com/coderefinery/word-count/commit/a0cc9e1d0)

---

## Grepping code

What if the combination of `git log` and `git show` is not enough to find what we need?

```shell
$ git grep -i zipf

Makefile:# Test Zipf's law
Makefile:results/results.txt: processed_data/abyss.dat source/zipf_test.py
Makefile:       python source/zipf_test.py processed_data/abyss.dat > results/results.txt
Makefile_all:$(RESDIR)/results.txt: $(DATA) source/zipf_test.py
Makefile_all:   python source/zipf_test.py $(DATA) > $@
README.md:most common words, and test [Zipf's
README.md:law](https://en.wikipedia.org/wiki/Zipf%27s_law) on the two most common words.
Snakefile_all:        'zipf_analysis.tar.gz'
Snakefile_all:        rm -f zipf_analysis.tar.gz processed_data/* results/*
Snakefile_all:rule zipf_test:
Snakefile_all:        zipf='source/zipf_test.py',
Snakefile_all:    shell:  'python {input.zipf} {input.books} > {output}'
Snakefile_all:    output: 'zipf_analysis.tar.gz'
doc/exercises.rst:- Write a sentence or two about Zipf's law and link to Wikipedia
doc/purpose.rst:Zipf's law
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
$ git blame <filename>
```

Example from real life:

```shell
$ git blame README.md

73434d63 (Radovan Bast          2018-08-22 15:20:30 +0200  1)
73434d63 (Radovan Bast          2018-08-22 15:20:30 +0200  2)
^c4a32ca (Kjartan Thor Wikfeldt 2018-05-08 15:15:48 +0200  3) # Word count example
^c4a32ca (Kjartan Thor Wikfeldt 2018-05-08 15:15:48 +0200  4)
73434d63 (Radovan Bast          2018-08-22 15:20:30 +0200  5) These programs will count words in a given text, plot a bar chart of the 10
73434d63 (Radovan Bast          2018-08-22 15:20:30 +0200  6) most common words, and test [Zipf's
73434d63 (Radovan Bast          2018-08-22 15:20:30 +0200  7) law](https://en.wikipedia.org/wiki/Zipf%27s_law) on the two most common words.
73434d63 (Radovan Bast          2018-08-22 15:20:30 +0200  8)
9187d4be (Radovan Bast          2018-08-22 15:16:56 +0200  9) - Inspired by and derived from https://hpc-carpentry.github.io/hpc-python/
9187d4be (Radovan Bast          2018-08-22 15:16:56 +0200 10)   which is distributed under
9187d4be (Radovan Bast          2018-08-22 15:16:56 +0200 11)   [Creative Commons Attribution license (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
73434d63 (Radovan Bast          2018-08-22 15:20:30 +0200 12) - Documentation: https://word-count.readthedocs.io
a0cc9e1d (Kjartan Thor Wikfeldt 2018-05-08 15:24:57 +0200 13)
73434d63 (Radovan Bast          2018-08-22 15:20:30 +0200 14) We use this example in two [CodeRefinery](https://coderefinery.org/) lessons:
73434d63 (Radovan Bast          2018-08-22 15:20:30 +0200 15) - https://coderefinery.github.io/reproducible-research/
73434d63 (Radovan Bast          2018-08-22 15:20:30 +0200 16) - https://coderefinery.github.io/documentation/
```

Rather typical timeline:

> *"Who the %&!@!!! wrote this crap?!? Oh, it was me."*

Who was the last to edit a specific line of the source file for `git blame` and when and why?

- [https://github.com/coderefinery/word-count/blame/master/README.md](https://github.com/coderefinery/word-count/blame/master/README.md)

---

## Grepping commit messages

- Another possible scenario is that you're looking for a particular commit, but can't
easily find it with `git blame`.
- You can however remember (or guess) some keywords from the commit message
- Commit messages can also be grepped!

Real-life example:
```
$ git log --oneline --grep "remove"

707c200 remove trailing whitespace for more silent diffs
cc843ff Merge pull request #5 from coderefinery/radovan/encoding
bbf088e (origin/radovan/encoding, radovan/encoding) remove encoding="utf-8" arg to allow also python 2.7
```

Note that `git log --grep` will grep the whole commit message even if you use the `--oneline` option.

---

## Finding removed code

The day will come when you are in this situation:

> *I remember there used to be a function called "typeset_labels".
> Now it is gone:*

```shell
$ git grep 'typeset_labels' source/plotcount.py

[no output]
```
(You can also grep all files at once: `git grep 'typeset_labels`)

Sometimes also the log does not help because the commit messages are not helpful:

```shell
$ git log --oneline source/plotcount.py

7ef076e rm a lot of unused code; fixes #12
aa8cd8a clean up sources with pycodestyle
086715d rm outcommented code
707c200 remove trailing whitespace for more silent diffs
a362e23 python scripts do not need to be executable
6297979 add python command and rm shebangs
8738e1e call python scripts using py3 shebang
c4a32ca initial commit
```

What now?

We can figure out when it disappeared:

```
$ git log -S 'typeset_labels' source/plotcount.py

commit 7ef076eb516851f5f5e2be50d1fd1a1681294e6d
Author: Radovan Bast <bast@users.noreply.github.com>
Date:   Tue Aug 21 00:37:43 2018 +0200

    rm a lot of unused code; fixes #12

commit c4a32caae2f0ddc4d85481f5adf61360198edc2f
Author: Kjartan Thor Wikfeldt <ktwikfeldt@gmail.com>
Date:   Tue May 8 15:15:48 2018 +0200

    initial commit
```

Now let us have a look at that commit:

```shell
$ git show 7ef076eb source/plotcount.py

commit 7ef076eb516851f5f5e2be50d1fd1a1681294e6d
Author: Radovan Bast <bast@users.noreply.github.com>
Date:   Tue Aug 21 00:37:43 2018 +0200

    rm a lot of unused code; fixes #12

diff --git a/source/plotcount.py b/source/plotcount.py
index db7180f..268de5b 100644
--- a/source/plotcount.py
+++ b/source/plotcount.py
@@ -1,7 +1,6 @@
 import numpy as np
 import matplotlib.pyplot as plt
 import sys
-from collections import Sequence

 from wordcount import load_word_counts

@@ -23,67 +22,6 @@ def plot_word_counts(counts, limit=10):
     plt.bar(position, count_data, width, color='b')


-def typeset_labels(labels=None, gap=5):
-    """
-    Given a list of labels, create a new list of labels such that each label
-    is right-padded by spaces so that every label has the same width, then
-    is further right padded by ' ' * gap.
-    """
...
```

Indeed! Thank you, Git!

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

## Finding out when something broke

> *But I am sure it used to work! Strange.*

- Sometimes you realize that something broke.
- You know that it used to work.
- You do not know when it broke.
- First find out a commit in past when it worked.
- Then bisect your way until you find the commit that broke it.

```shell
$ git bisect start
$ git bisect good 89578ed  # this is a commit that worked
$ git bisect bad HEAD      # last commit is broken
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
> Clone [this repository](https://github.com/coderefinery/git-bisect-exercise).
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
> Use `git bisect` to find the commit which broke the computation.
> 
> 
> - But how to find the first commit? Either by `git log --reverse` or `git log --oneline | tail -n 1`
{: .task}

> ## Bonus exercise
> 
> Write a script that checks for a correct result and use `git bisect run` to
> find the offending commit automatically.
{: .task}
