---
layout: episode
title: "Inspecting history"
teaching: 15
exercises: 20
questions:
  - How can we find out when exactly a line of code was changed?
  - How can we find out which commit broke or changed a functionality?
objectives:
  - Quickly find a line of code, find out who introduced it, when, and why.
  - Quickly find the commit that changed a behavior.
keypoints:
  - "`git log/grep/annotate/show/bisect` is a powerful combination when doing archaeology in a project."
  - "`git checkout -b <name> <hash>` is the recommended mechanism to inspect old code"
---

## Preparation

Please make sure that you do not clone repositories inside an already tracked folder:

```shell
$ git status
```

If you are inside an existing Git repository, step out of it.
You need to find a different location since we will clone a new repository.

If you see this message, this is good in this case:

```
fatal: not a git repository (or any of the parent directories): .git
```


## We will use the following four commands

### `git grep`

With `git grep` you can find all lines in a repository which contain some string or regular expression.
This is useful to find out where in the code some variable is used or some error message printed.

Example:

```
$ git grep sometext
```

### `git show`

We have seen this one before already. Using `git show` we can inspect an individual commit if
we know its hash:

```
$ git show somehash
```

### `git annotate`

Try it out on a file - with `git annotate` you can see line by line who and **when** the line was modified
last. It also prints the precise hash of the last change which modified each line. Incredibly useful
for reproducibility.

Example:

```
$ git blame somefile
```

### `git checkout -b` to inspect code in the past

We can create branches pointing to a commit in the past.
This is the recommended mechanism to inspect old code:

```shell
$ git checkout -b branchname somehash
```

Example:

```shell
$ git checkout -b museum abc123  # create branch called "museum" from hash abc123
  # do some archaeology ...
  # "What was I thinking back then!?"
  # "Aha! Hmm."
$ git checkout master            # after you are done switch back to "master"
$ git branch -d museum
```


> ## Archaeology exercise
>
> Let us explore the value of these commands in an exercise. We recommend that you
> do this exercise in groups of two and discuss with your neighbors.
>
> 1. Clone this repository:
>    [https://github.com/tidyverse/rvest](https://github.com/tidyverse/rvest).
>    Then step into the new directory:
>    ```
>    $ git clone https://github.com/tidyverse/rvest.git
>    $ cd rvest
>    ```
> 2. Find the code line which contains `'No links matched that expression'`
> 3. Find out when this line was last modified. Find the actual commit which modified that line.
> 4. Inspect that commit with `git show`.
> 5. Bring the code to the state of that commit.
{: .challenge}

---

## Finding out when something broke with `git bisect`

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
>
>
> #### Bonus exercise
>
> Write a script that checks for a correct result and use `git bisect run` to
> find the offending commit automatically
> ([solution - spoiler alert!](https://github.com/coderefinery/git-bisect-exercise#solutions-spoiler-alert)).
{: .challenge}
