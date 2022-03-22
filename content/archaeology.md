# Inspecting history

```{objectives}
- Quickly find a line of code, find out why it was introduced and when.
- Quickly find the commit that changed a behavior.
```

```{instructor-note}
- 15 min teaching/type-along
- 30 min exercise
```

````{prereq} Preparation
Please make sure that you do not clone repositories inside an already tracked folder:

```shell
$ git status
```

If you are inside an existing Git repository, step out of it.
You need to find a different location since we will clone a new repository.

If you see this message, this is good in this case:

```shell
fatal: not a git repository (or any of the parent directories): .git
```
````


## Our toolbox for history inspection

```{instructor-note}
First the instructor demonstrates few commands on a real life example
repository <https://github.com/networkx/networkx> (mentioned in the amazing site [The
Programming Historian](https://programminghistorian.org/)).
Later we will practice these in groups in an archaeology exercise (below).
After demonstrating the command line tools, the instructor can also demonstrate searching, "show" and "annotate"
in the GitHub browser for this example project.
```


### Warm-up: ["Git History" browser](https://githistory.xyz/)

As a warm-up we can try the ["Git History" browser](https://githistory.xyz/)
on the README.rst file of the [networkx](https://github.com/networkx/networkx) repository:

- Visit and browse <https://github.githistory.xyz/networkx/networkx/blob/main/README.rst> (use left/right keys).
- You can try this on some of your GitHub repositories, too!


### git grep: to search through the repository

With `git grep` you can find all lines in a repository which contain some string or regular expression.
This is useful to find out where in the code some variable is used or some error message printed:

```console
$ git grep sometext
$ git grep "some text with spaces"
```

In the [networkx](https://github.com/networkx/networkx) repository you can try:

```console
$ git clone https://github.com/networkx/networkx
$ cd networkx
$ git grep -i fixme
```


### git log -S: to search through the history of changes

While `git grep` searches the **current state** of the repository,
it is also possible to search through all changes for "sometext":

```console
$ git log -S sometext
```

In the [networkx](https://github.com/networkx/networkx) repository you can try:

```console
$ git log -S test_weakly_connected_component
```


### git show: to inspect commits

We have seen this one before already. Using `git show` we can inspect an individual commit if
we know its hash:

```console
$ git show somehash
```

For instance:

```console
$ git show 759d589bdfa61aff99e0535938f14f67b01c83f7
```


### git annotate: to annotate code with commit metadata

Try it out on a file - with `git annotate` you can see line by line who and **when** the line was modified
last. It also prints the precise hash of the last change which modified each line. Incredibly useful
for reproducibility.

```console
$ git annotate somefile
```

Example:

```console
$ git annotate networkx/convert_matrix.py
```

If you annotate in a terminal and the file is longer than the screen, Git by default uses the program `less` to
scroll the output.
Use `/sometext` `<ENTER>` to find "sometext" and you can cycle through the results with `n` (next) and `N` (last).
You can also use page up/down to scroll. You can quit with `q`.

```{discussion}
Discuss how these two affect the annotation:
- wrapping long lines of text/code into shorter lines
- autoformatting tools such as `black`
```


### git checkout -b: to inspect code in the past

We can create branches pointing to a commit in the past.
This is the recommended mechanism to inspect old code:

```console
$ git checkout -b branchname somehash
```

Example (lines starting with "#" are only comments):

```shell
  # create branch called "older-code" from hash 347e6292419b
$ git checkout -b older-code 347e6292419bd0e4bff077fe971f983932d7a0e9

  # now you can navigate and inspect the code as it was back then
  # ...

  # after we are done we can switch back to "main"
$ git checkout main

  # if we like we can delete the "older-code" branch
$ git branch -d older-code
```

On newer Git versions this is the preferred command:

```console
$ git switch --create branchname somehash
```

(exercise-history)=

## Exercise: Basic archaeology commands

`````{exercise} History-1: Explore basic archaeology commands
  Let us explore the value of these commands in an exercise.  Future
  exercises do not depend on this, so it is OK if you do not complete
  it fully.

  **In-person workshops**: We recommend that you
  do this exercise in groups of two and discuss with your neighbors.

  **Video workshops**: We will group you in breakout rooms of ~4 persons where you
  can work and discuss together. A helper or instructor will pop in to help out.
  In the group one participant can share their screen and others
  in the group help out, discuss, and try to follow along.
  Please write down questions in the collaborative notes.
  After 15-20 minutes we will bring you back into the main room and discuss.

  Exercise steps:
  - Clone this repository:
    <https://github.com/networkx/networkx.git>.
    Then step into the new directory and create an exercise branch from the networkx-2.6.3 tag/release:
    ```
    $ git clone https://github.com/networkx/networkx.git
    $ cd networkx
    $ git checkout -b exercise networkx-2.6.3
    ```

  Then using the above toolbox try to:
  1. Find the code line which contains `"Logic error in degree_correlation"`.
  2. Find out when this line was last modified or added. Find the actual commit which modified that line.
  3. Inspect that commit with `git show`.
  4. Create a branch pointing to the past when that commit was created to be
     able to browse and use the code as it was back then.
  5. How would can you bring the code to the commit precisely before that line was last modified?

  ````{solution}
  1. We use `git grep`:
     ```console
     $ git grep "Logic error in degree_correlation"
     ```
     This gives the output:
     ```
     networkx/algorithms/threshold.py:                print("Logic error in degree_correlation", i, rdi)
     ```
  2. We use `git annotate`:
     ```console
     $ git annotate networkx/algorithms/threshold.py
     ```
     Then search for "Logic error" by typing "/Logic error" followed by Enter.
     The last commit that modified it was `90544b4fa` (unless that line changed since).
  3. We use `git show`:
     ```console
     $ git show 90544b4fa
     ```
  4. Create a branch pointing to that commit (here we called the branch "past-code"):
     ```console
     $ git branch past-code 90544b4fa
     ```
  5. This is a compact way to access the first parent of `90544b4fa` (here we
     called the branch "just-before"):
     ```console
     $ git checkout -b just-before 90544b4fa~1
     ```
  ````
`````

---

## Finding out when something broke/changed with git bisect

> *But I am sure it used to work! Strange.*

- Sometimes you realize that something broke.
- You know that it used to work.
- You do not know when it broke.

```{discussion} How would you solve this?
Before we go on first discuss how you would solve this problem: You know that it worked
500 commits ago but it does not work now.

- How would you find the commit which changed it?
- Why could it be useful to know the commit that changed it?

**Video workshops**: Write down ideas on how you would solve it in the collaborative
note and we will discuss various approaches.
```

We will probably arrive at a solution which is similar to `git bisect`:

- First find out a commit in past when it worked.
- Then bisect your way until you find the commit that broke it.

```shell
$ git bisect start
$ git bisect good f0ea950  # this is a commit that worked
$ git bisect bad main    # last commit is broken
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

(exercise-bisect)=

## Optional exercise: Git bisect

````{exercise} (optional) History-2: Use git bisect to find the bad commit
  In this exercise, we use `git bisect` on an example repository.  It
  is OK if you do not complete this exercise fully.

  Begin by cloning [https://github.com/coderefinery/git-bisect-exercise](https://github.com/coderefinery/git-bisect-exercise).


  **Motivation**

  The motivation for this exercise is to be able to do archaeology with Git on a
  source code where the bug is difficult to see visually. **Finding the offending
  commit is often more than half the debugging**.


  **Background**

  The script `get_pi.py` approximates pi using terms of the Nilakantha series. It
  should produce 3.14 but it does not. The script broke at some point and
  produces 3.57 using the last commit:

  ```
  $ python get_pi.py

  3.57
  ```

  At some point within the 500 first commits, an error was introduced. The only
  thing we know is that the first commit worked correctly.


  **Your task**

  - Clone this repository and use `git bisect` to find the commit which
    broke the computation
    ([solution - spoiler alert!](https://github.com/coderefinery/git-bisect-exercise#solutions-spoiler-alert)).
  - Once you have found the offending commit, also practice navigating to the last good commit.
  - Bonus exercise:
    Write a script that checks for a correct result and use `git bisect run` to
    find the offending commit automatically
    ([solution - spoiler alert!](https://github.com/coderefinery/git-bisect-exercise#solutions-spoiler-alert)).

  **Video workshops**: We will group you in breakout rooms of ~4 persons where you
  can work and discuss together. A helper or instructor will pop in to help out.
  Please write down questions in the collaborative notes.
  After 15-20 minutes we will bring you back into the main room and discuss.


  **Hints**

  Finding the first commit:

  ```
  $ git log --oneline | tail -n 1
  ```

  How to navigate to the parent of a commit with hash `somehash`:

  ```shell
    # create branch pointing to the parent of somehash
  $ git checkout -b branchname somehash~1

    # instead of a tilde you can also use this
  $ git checkout -b branchname somehash^
  ```
````

```{keypoints}
- git log/grep/annotate/show/bisect is a powerful combination when doing archaeology in a project.
- `git checkout -b <name> <hash>` is the recommended mechanism to inspect old code.
- On newer Git you can use the more intuitive `git switch --create branchname somehash`.
```
