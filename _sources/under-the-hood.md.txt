# Git under the hood

```{objectives}
- Verify that branches are pointers to commits and extremely lightweight.
```

```{instructor-note}
- 10 min teaching/type-along
- 15 min exercise
```

```{figure} img/stranger.jpg
:alt: Git under the hood
:width: 100%
```


## Down the rabbit hole

When working with Git, **you will never need to go inside .git**, but in this
exercise we will, in order to learn about how branches are implemented in Git.

For this exercise create a new repository and commit a couple of changes.

Now that we've made a couple of commits let us look at what is happening under
the hood.

```console
$ cd .git
$ ls -l

drwxr-xr-x   - user 25 Aug 15:51 branches
.rw-r--r-- 499 user 25 Aug 15:52 COMMIT_EDITMSG
.rw-r--r--  92 user 25 Aug 15:51 config
.rw-r--r--  73 user 25 Aug 15:51 description
.rw-r--r--  21 user 25 Aug 15:51 HEAD
drwxr-xr-x   - user 25 Aug 15:51 hooks
.rw-r--r-- 137 user 25 Aug 15:52 index
drwxr-xr-x   - user 25 Aug 15:51 info
drwxr-xr-x   - user 25 Aug 15:52 logs
drwxr-xr-x   - user 25 Aug 15:52 objects
drwxr-xr-x   - user 25 Aug 15:51 refs
```

Git stores everything under the .git folder in your repository. In fact, **the
.git directory is the Git repository.**

Previously when you wrote the commit messages using your text editor, they
were in fact saved to `COMMIT_EDITMSG`.

Each commit in Git is stored as an object. This object contains information about
the author and the commit message. A *commit object* references a *tree object* that lists
the files present in the directory at the time.
Tree objects reference *blob* objects (that record the state of each file)
or other tree objects.

Commits are referenced by a SHA-1 hash (a 40-character hexadecimal string).

```{figure} img/commit-and-tree.png
:alt: A commit inside Git
:width: 100%

States of a Git file. Image from the [Pro Git book](https://git-scm.com/book/). License CC BY 3.0.
```

Once you have several commits, each commit object also links to the hash of the
previous commit(s) (there is more than one previous commit for for merge commits).
The commits form a [directed acyclic graph](http://eagain.net/articles/git-for-computer-scientists/)
(do not worry if the term is not familiar).

```{figure} img/commits-and-parents.png
:alt: A commit and its parents
:width: 100%

A commit and its parents. Image from the [Pro Git book](https://git-scm.com/book/). License CC BY 3.0.
```

All branches and tags in Git are pointers to commits.


## Git is basically a content-addressed storage system

- CAS: ["mechanism for storing information that can be retrieved based on its content, not its storage location"](https://en.wikipedia.org/wiki/Content-addressable_storage)
- Content address is the content digest (SHA-1 checksum)
- Stored data does not change - so when we modify commits, we always create new
  commits.  Git doesn't delete these right away, which is why it is *very hard
  to lose data if you commit it once*.

Let us poke a bit into raw objects! Start with:

```console
$ git cat-file -p HEAD
```

Then explore the `tree` object, then the `file` object, etc. recursively using the hashes you see.


## Demonstration: experimenting with branches

Let us lift the hood and create few branches manually.  The
goal of this exercise is to hopefully create an "Aha!" moment and provide us a
good understanding of the underlying model.

We are starting from the `main` branch and create an `idea` branch:

```console
$ git status

On branch main
nothing to commit, working tree clean
```

```console
$ git switch --create idea

Switched to a new branch 'idea'
```

```console
$ git branch

* idea
  main
```

Now let us go in:

```console
$ cd .git
$ cd refs/heads
$ ls -l

.rw-r--r-- 41 user 25 Aug 15:54 idea
.rw-r--r-- 41 user 25 Aug 15:52 main
```

Let us check what the `idea` file looks like
(do not worry if the hash is different):
```console
$ cat idea

045e3db14740c60684d745e5fb891ae71e335611
```

Now let us replicate this file:
```console
$ cp idea idea-2
$ cp idea idea-3
$ cp idea idea-4
$ cp idea idea-5
```

Let us go up two levels and inspect the file `HEAD`:
```console
$ cd ../..
$ cat HEAD

ref: refs/heads/idea
```

Let us open this file and change it to:
```
ref: refs/heads/idea-3
```

**Now we are ready for the aha moment!**
First let us go back to the working area:
```console
$ cd ..
```

Now - on which branch are we?
```console
$ git branch

  idea
  idea-2
* idea-3
  idea-4
  idea-5
  main
```

## Demonstration: If you add it, you don't lose it (for a while)

A common way to (apparently) lose work
is to use `git add` indiscriminately.

You make some changes to a file, 
(let us call this version A)
you `git add` them,
then you make some other changes 
(let us call this version B)
and you `git add` those again.

Now version A is apparently lost,
and if we realize that we need it back
we typically click nervously on the "undo" arrow of our editor.

But fear not! Try this.
1. Create a file named `test-add` with the following command:
```
echo 'Once a file has been git added, it is hard to lose!' > test-add
```
1. Add it to the repository
```console
$ git add test-add
```
1. Now change the content of the file to be 
```
Ops
```
1. And repeat the add command
```console
$ git add test-add
```
1. Apparently we have lost the previous version of the file.
But it is actually there, stored in a *dangling* blob object
(which is not referenced by any other objects)
We can see this with the command `fsck`:
```console
$ git fsck
Checking object directories: 100% (256/256), done.
dangling blob dc3b15f60045eea7a87639436ed75021130579e0
```
We can see the content of that blob 
by passing its hash (shortened for convenience) 
to the `git cat-file -p` command:
```console
$ git cat-file -p dc3b
Once a file has been git added, it is hard to lose!
```


```{discussion}
Discuss the findings with other course participants.
```
