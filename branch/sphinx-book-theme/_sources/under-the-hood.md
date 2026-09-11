# Git under the hood

```{objectives}
- Verify that branches are pointers to commits.
- Verify that branches are extremely lightweight.
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

total 44
-rw------- 1 bast users   36 May  7 11:47 COMMIT_EDITMSG
-rw------- 1 bast users   21 May  7 11:47 HEAD
drwx------ 2 bast users 4096 May  7 11:46 branches
-rw------- 1 bast users   92 May  7 11:46 config
-rw------- 1 bast users   73 May  7 11:46 description
drwx------ 2 bast users 4096 May  7 11:46 hooks
-rw------- 1 bast users  225 May  7 11:47 index
drwx------ 2 bast users 4096 May  7 11:46 info
drwx------ 3 bast users 4096 May  7 11:47 logs
drwx------ 8 bast users 4096 May  7 11:47 objects
drwx------ 4 bast users 4096 May  7 11:46 refs
```

Git stores everything under the .git folder in your repository. In fact, **the
.git directory is the Git repository.**

Previously when you wrote the commit messages using your text editor, they
were in fact saved to COMMIT_EDITMSG.

Each commit in Git is stored as a "blob". This blob contains information about
the author and the commit message. The blob references another blob that lists
the files present in the directory at the time and references blobs that record
the state of each file.

Commits are referenced by a SHA-1 hash (a 40-character hexadecimal string).

```{figure} img/commit-and-tree.png
:alt: A commit inside Git
:width: 100%

States of a Git file. Image from the [Pro Git book](https://git-scm.com/book/). License CC BY 3.0.
```

Once you have several commits, each commit blob also links to the hash of the
previous commit. The commits form a [directed acyclic
graph](http://eagain.net/articles/git-for-computer-scientists/) (do not worry
if the term is not familiar).

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
goal of this exercise is to hopefully create an "aha" moment and provide us a
good understanding of the underlying model.

We are starting from the `master` branch and create an `idea` branch:

```console
$ git status

On branch master
nothing to commit, working tree clean
```

```console
$ git checkout -b idea

Switched to a new branch 'idea'
```

```console
$ git branch

* idea
  master
```

Now let us go in:

```console
$ cd .git
$ cd refs/heads
$ ls -l

total 8
-rw------- 1 bast users 41 May  7 11:47 idea
-rw------- 1 bast users 41 May  7 11:47 master
```

Let us check what the `idea` file looks like
(do not worry if the hash is different):
```console
$ cat idea

7f3582dfbad6539cfa60f5b21bfad41d1b58a618
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
  master
```

```{discussion}
Discuss the findings with other course participants.
```
