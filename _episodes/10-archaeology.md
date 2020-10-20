---
layout: episode
title: "Inspecting history"
teaching: 15
exercises: 30
questions:
  - How can we find out when exactly a line of code was changed?
  - How can we navigate past versions of the code?
  - How can we find out which commit broke or changed a functionality?
objectives:
  - Quickly find a line of code, find out why it was introduced and when.
  - Quickly find the commit that changed a behavior.
keypoints:
  - "`git log/grep/annotate/show/bisect` is a powerful combination when doing archaeology in a project."
  - "`git checkout -b <name> <hash>` is the recommended mechanism to inspect old code."
  - "On newer Git you can use the more intuitive `git switch --create branchname somehash`."
---

> ## Preparation
>
> Please make sure that you do not clone repositories inside an already tracked folder:
>
> ```shell
> $ git status
> ```
>
> If you are inside an existing Git repository, step out of it.
> You need to find a different location since we will clone a new repository.
>
> If you see this message, this is good in this case:
>
> ```
> fatal: not a git repository (or any of the parent directories): .git
> ```
{: .discussion}

---

## Our toolbox for history inspection


First the instructor demonstrates few commands on a real life example
repository [https://github.com/networkx/networkx](https://github.com/networkx/networkx) (mentioned in the amazing site [The
Programming Historian](https://programminghistorian.org/)).
Later we will practice these in groups in an archaeology exercise (below).


### 1. `git grep` to search through the repository

With `git grep` you can find all lines in a repository which contain some string or regular expression.
This is useful to find out where in the code some variable is used or some error message printed:

```
$ git grep sometext
```

In the [networkx](https://github.com/networkx/networkx) repository you can try:

```
$ git clone https://github.com/networkx/networkx
$ cd networkx
$ git grep -i fixme
```


### 2. `git log -S` to search through the history of changes

While `git grep` searches the **current state** of the repository,
it is possible to search also through all changes for "sometext":

```
$ git log -S sometext
```

In the [networkx](https://github.com/networkx/networkx) repository you can try:

```
$ git log -S test_weakly_connected_component
```


### 3. `git show` to inspect commits

We have seen this one before already. Using `git show` we can inspect an individual commit if
we know its hash:

```
$ git show somehash
```

For instance:

```
$ git show 759d589bdfa61aff99e0535938f14f67b01c83f7
```


### 4. `git annotate` to annotate code with commit metadata

Try it out on a file - with `git annotate` you can see line by line who and **when** the line was modified
last. It also prints the precise hash of the last change which modified each line. Incredibly useful
for reproducibility.

```
$ git annotate somefile
```

Example:

```
$ git annotate networkx/convert_matrix.py
```

If you annotate in a terminal and the file is longer than the screen, Git by default uses the program `less` to
scroll the output.
Use `/sometext` `<ENTER>` to find "sometext" and you can cycle through the results with `n` (next) and `N` (last).
You can also use page up/down to scroll. You can quit with `q`.

> ## Discussion
>
> Discuss how these two affect the annotation:
> - wrapping long lines of text/code into shorter lines
> - autoformatting tools such as `black`
{: .discussion}


### 5. `git checkout -b` to inspect code in the past

We can create branches pointing to a commit in the past.
This is the recommended mechanism to inspect old code:

```shell
$ git checkout -b branchname somehash
```

Example:

```shell
  # create branch called "older-code" from hash 347e6292419b
$ git checkout -b older-code 347e6292419bd0e4bff077fe971f983932d7a0e9

  # now you can navigate and inspect the code as it was back then
  # ...

  # after we are done we can switch back to "master"
$ git checkout master

  # if we like we can delete the "older-code" branch
$ git branch -d older-code
```

On newer Git versions this is the preferred command:

```shell
$ git switch --create branchname somehash
```

> ## Exercise: basic archaeology commands
>
> Let us explore the value of these commands in an exercise.  Future
> exercises do not depend on this, so it is OK if you do not complete
> it fully.
>
> **In-person workshops**: We recommend that you
> do this exercise in groups of two and discuss with your neighbors.
>
> **Video workshops**: We will group you in breakout rooms of ~4 persons where you
> can work and discuss together. A helper or instructor will pop in to help out.
> In the group one participant can share their screen and others
> in the group help out, discuss, and try to follow along.
> Please write down questions in the collaborative notes.
> After 15-20 minutes we will bring you back into the main room and discuss.
>
> Exercise steps:
> - Clone this repository:
>   [https://github.com/tidyverse/rvest](https://github.com/tidyverse/rvest).
>   Then step into the new directory:
>   ```
>   $ git clone --branch v0.3.5 https://github.com/tidyverse/rvest.git
>   $ cd rvest
>   ```
>
> Then using the above 5 tools try to:
> - Find the code line which contains `'No links matched that expression'`
> - Find out when this line was last modified. Find the actual commit which modified that line.
> - Inspect that commit with `git show`.
> - Create a branch pointing to the past when that commit was created to be able to browse and use the code as it was back then.
> - How would can you bring the code to the commit precisely before that line was last modified?
{: .challenge}

---

## Finding out when something broke/changed with `git bisect`

> *But I am sure it used to work! Strange.*

- Sometimes you realize that something broke.
- You know that it used to work.
- You do not know when it broke.

> ## How would you solve this?
>
> Before we go on first discuss how you would solve this problem: You know that it worked
> 500 commits ago but it does not work now.
>
> - How would you find the commit which changed it?
> - Why could it be useful to know the commit that changed it?
>
> **Video workshops**: Write down ideas on how you would solve it in the collaborative
> note and we will discuss various approaches.
{: .discussion}

---

We will probably arrive at a solution which is similar to `git bisect`:

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

> ## Exercise: Git bisect
>
> In this exercise, we use `git bisect` on an example repository.  It
> is OK if you do not complete this exercise fully.
>
> Begin by cloning [https://github.com/coderefinery/git-bisect-exercise](https://github.com/coderefinery/git-bisect-exercise).
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
> - Clone or fork this repository and use `git bisect` to find the commit which
>   broke the computation
>   ([solution - spoiler alert!](https://github.com/coderefinery/git-bisect-exercise#solutions-spoiler-alert)).
> - Once you have found the offending commit, also practice navigating to the last good commit.
> - Bonus exercise:
>   Write a script that checks for a correct result and use `git bisect run` to
>   find the offending commit automatically
>   ([solution - spoiler alert!](https://github.com/coderefinery/git-bisect-exercise#solutions-spoiler-alert)).
>
> **Video workshops**: We will group you in breakout rooms of ~4 persons where you
> can work and discuss together. A helper or instructor will pop in to help out.
> Please write down questions in the collaborative notes.
> After 15-20 minutes we will bring you back into the main room and discuss.
>
>
> #### Hints
>
> Finding the first commit:
>
> ```
> $ git log --oneline | tail -n 1
> ```
>
> How to navigate to the parent of a commit with hash `somehash`:
>
> ```shell
>   # create branch pointing to the parent of somehash
> $ git checkout -b branchname somehash~1
>
>   # instead of a tilde you can also use this
> $ git checkout -b branchname somehash^
> ```
{: .challenge}
