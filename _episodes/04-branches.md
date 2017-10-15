---
layout: episode
title: Branching and Merging
teaching: 15
exercises: 15
questions:
  - How can I or my team work on multiple features in parallel?
  - How to combine the changes of parallel tracks of work?
  - What is branching and when should I do it?
  - How can I permanently reference a point in history, like a software
    version?
objectives:
  - Be able to create and merge branches.
  - Know the difference between a branch and a tag.
keypoints:
  - A branch is a division unit of work, to be merged with other units of work.
  - Creating branches is simple in Git.
  - Merging branches is typically straightforward.
  - A tag is a pointer to a moment in the history of a project.
---

## Food for thought

- How do you work on two things in parallel?
- How often do you find yourself wanting to go into two directions at once?
- How often are you not sure which of two options is the right one?
- How do you patch a version of the code which is not the latest commit?

---

## Motivation for branches

Up until now our repository has only had one branch with one commit coming
after the other:

![Linear]({{ site.baseurl }}/img/gitink/git-branch-1.svg "Linear git
repository"){:class="img-responsive"}

However, software development is often not linear:

  - Maintenance of releases, bug-fixes, and patches.
  - Collaborative work (everybody would be exposed to your bugs; you would be
    exposed to bugs of other people).
  - We do not have time to write perfect code immediately, it would be nice to
    have the possibility to experiment somewhere aside.
  - Interrupted work (we typically work on several longer term projects at the
    same time).

The strength of version control is that it permits the developers to **isolate
different tracks of work**. Developers can work on different things and merge
the changes they made to the source code files afterwards to create a composite
version that contains both the changes.

To enable collaborative work we wish to do something more like:

![Git collaborative]({{ site.baseurl }}/img/gitink/git-collaborative.svg
"description"){:class="img-responsive"}

- We see branching points and merging points.
- Often we call the main line development `master`.
- Other than this convention there is nothing special about `master`, it is just a branch.
- Commits form a directed acyclic graph (we have left out the arrows to avoid confusion about the time arrow).

A group of commits that create a single narrative are called a **branch**.
There are different branching strategies, but it is useful to think that a branch
tells the story of a feature, e.g. "new login workflow" or "fixing bug in
matrix inversion algorithm".

---

## What is a commit?

Before we exercise branching, a quick recap of what we got so far.

We have three commits (we use the first two characters of the commits) and only
one development line (branch) and this branch is called "master":

![]({{ site.baseurl }}/img/gitink/git-branch-1.svg)

```shell
$ git log --stat

commit 7f3582dfbad6539cfa60f5b21bfad41d1b58a618
Author: Radovan Bast <bast@users.noreply.github.com>
Date:   Fri May 5 12:49:45 2017 +0200

    do not forget to enjoy

 instructions.txt | 1 +
 1 file changed, 1 insertion(+)

commit 64441c1934def7d91ff0b66af0795749d5f1954a
Author: Radovan Bast <bast@users.noreply.github.com>
Date:   Fri May 5 12:49:35 2017 +0200

    add onion

 ingredients.txt | 1 +
 1 file changed, 1 insertion(+)

commit d619bf848a3f83f05e8c08c7f4dcda3490cd99d9
Author: Radovan Bast <bast@users.noreply.github.com>
Date:   Fri May 5 12:48:36 2017 +0200

    adding ingredients and instructions

 ingredients.txt  | 3 +++
 instructions.txt | 5 +++++
 2 files changed, 8 insertions(+)
```

- Commits are states characterized by a 40-character hash (checksum).


### Branches are pointers

- Branches are pointers that point to a commit.
- Branch `master` points to commit `7f3582dfbad6539cfa60f5b21bfad41d1b58a618`.

Try this:

```shell
$ cat .git/refs/heads/master
```

It will echo a long hash, for instance this one:

```shell
7f3582dfbad6539cfa60f5b21bfad41d1b58a618
```

- That is all there is: branch `master` is simply a pointer to a hash.
- `HEAD` is another pointer, it points to where we are right now (currently `master`).

### On which branch are we?

To see where we are (where HEAD points to) use `git branch`:

```shell
$ git branch

* master
```

- This command shows where we are, it does not create a branch.
- There is only `master` and we are on `master` (star represents the `HEAD`).

In the following we will learn how to create branches,
how to switch between them, how to merge branches,
and how to remove them afterwards.

---

## Exercise: creating and working with branches

- Create a branch called `experiment` where you experiment adding
  cilantro to `ingredients.txt` (if you don't like cilantro, you can add
  another ingredient).
- Create another branch called `less-salt`
  where you reduce the amount of salt.
- Make sure you create both branches from the `master` branch.
- Commit your changes to the respective branches.

Use the following 3 commands:

```shell
$ git branch experiment    # create branch called "experiment" pointing to the present commit
$ git checkout experiment  # switch to branch "experiment"
$ git branch               # list all local branches and show on which branch we are
```

Once you have committed your changes, try:

```shell
$ git log experiment
$ git log less-salt
$ git log master
```

Examining the log on the `experiment` branch may now produce the following log:

```shell
$ git log --oneline experiment

f413c60 maybe little bit less cilantro
d541ee0 let us try with some cilantro
7f3582d do not forget to enjoy
64441c1 add onion
d619bf8 adding ingredients and instructions
```

And on the `less-salt` branch:

```shell
$ git log --oneline less-salt

e66edf3 reduce amount of salt
7f3582d do not forget to enjoy
64441c1 add onion
d619bf8 adding ingredients and instructions
```

We now have three branches (in this case `HEAD` points to `experiment`):

```shell
$ git branch

* experiment
  less-salt
  master
```

Here is a graphical representation of what we have created (do not worry if the commit hashes are different on your laptop):

![]({{ site.baseurl }}/img/gitink/git-branch-2.svg)


How do you interpret the following:

```
$ git show-branch

* [experiment] maybe little bit less cilantro
 ! [less-salt] reduce amount of salt
  ! [master] do not forget to enjoy
---
*   [experiment] maybe little bit less cilantro
*   [experiment^] let us try with some cilantro
 +  [less-salt] reduce amount of salt
*++ [master] do not forget to enjoy
```

---

## Exercise: merging branches

It turned out that our experiment with cilantro was a good idea.
Our goal now is to merge `experiment` into `less-salt`.

First we switch to the `less-salt` branch:

```shell
$ git checkout less-salt
$ git branch

  experiment
* less-salt
  master
```

![]({{ site.baseurl }}/img/gitink/git-merge-1.svg)

Then we merge `experiment`:

```shell
$ git merge experiment
```

![]({{ site.baseurl }}/img/gitink/git-merge-2.svg)

We can verify the result in the terminal:

```shell
$ git log --graph --decorate --pretty=oneline --abbrev-commit

*   265ee5d (HEAD -> less-salt) Merge branch 'experiment' into less-salt
|\
| * f413c60 (experiment) maybe little bit less cilantro
| * d541ee0 let us try with some cilantro
* | e66edf3 reduce amount of salt
|/
* 7f3582d (master) do not forget to enjoy
* 64441c1 add onion
* d619bf8 adding ingredients and instructions
```

Observe how Git nicely merged the changed amount of salt and the new ingredient **in the same file
without us merging it manually**:

```shell
$ cat ingredients.txt

* 2 avocados
* 1 lime
* 1 tsp salt
* 1/2 onion
* 1 tbsp cilantro
```

What happens internally when you merge two branches is that Git creates a new
commit, attempts to incorporate changes from both branches and records the
state of all files in the new commit. While a regular commit has one parent, a
merge commit has two (or more) parents.

If the same file is changed in both branches, Git attempts to incorporate both
changes into the merged file. If the changes overlap then the user has to
manually settle merge conflicts (we will do that later).


### Questions

- How do the ingredients look on `master`?
- What do you expect to happen when you merge `experiment` into `master` (draw the result first)?
- Verify whether the result matches your expectation.

**SPOILER BELOW**

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

This is the result - discuss it:

![]({{ site.baseurl }}/img/gitink/git-merge-3.svg)


### Fast-forward vs. non-fast-forward merges

To understand what just happened, it is useful to discuss the difference
between fast-forward vs. non-fast-forward merges.

To clarify what is meant by "fast-forward" imagine that you are on `master` and want to merge `experiment`
(the color change is to make clear that the two commits are not on the `master` branch yet):

![]({{ site.baseurl }}/img/gitink/pre-ff.svg)

What will happen if we `git merge experiment`?

If you now type `git merge experiment`, Git will recognize that it can simply move
the `master` pointer to `f4` without creating a merge commit.

This is a fast-forward merge:

![]({{ site.baseurl }}/img/gitink/ff.svg)

The default in Git is to fast-forward merge when possible.

If you do not like this you can tell Git to merge with no fast-forward:

```shell
$ git merge --no-ff experiment
```

Both is fine, the resulting code is the same, not the history:

![]({{ site.baseurl }}/img/gitink/no-ff.svg)

It is a matter of taste or convention. Discuss the advantages of both approaches.

---

## Deleting branches safely

Let us merge also the `less-salt` to `master`:

```shell
$ git checkout master
$ git merge less-salt
```

![]({{ site.baseurl }}/img/gitink/git-merge-4.svg)

Now that we are happy with the work we did in the branch and the branch it is
time to delete the feature branches:

```shell
$ git branch -d experimental
$ git branch -d less-salt
```

![]({{ site.baseurl }}/img/gitink/git-merge-5.svg)

As you see only the pointers disappeared, not the commits.

Git will not let you delete a branch which has not been reintegrated unless you
insist using `git branch -D`. Even then your commits will not be lost but you
may have a hard time finding them as there is no branch pointing to them.

---

## Summary

Let us pause for a moment and recapitulate what we have just learned:

```shell
$ git branch               # see where we are
$ git branch <name>        # create branch <name>
$ git checkout <name>      # switch to branch <name>
$ git merge <name>         # merge branch <name> (to current branch)
$ git branch -d <name>     # delete branch <name>
```

Since the following command combo is so frequent:

```shell
$ git branch <name>        # create branch <name>
$ git checkout <name>      # switch to branch <name>
```

There is a shortcut for it:

```shell
$ git checkout -b <name>   # create branch <name> and switch to it
```

### Typical workflows

With this there are two typical workflows:

```shell
$ git checkout -b new-feature  # create branch, switch to it
$ git commit                   # work, work, work, ...
                               # test
                               # feature is ready
$ git checkout master          # switch to master
$ git merge new-feature        # merge work to master
$ git branch -d new-feature    # remove branch
```

Sometimes you have a wild idea which does not work.
Or you want some throw-away branch for debugging:

```shell
$ git checkout -b wild-idea
                               # work, work, work, ...
                               # realize it was a bad idea
$ git checkout master
$ git branch -D wild-idea      # it is gone, off to a new idea
                               # -D because we never merged back
```

No problem: we worked on a branch, branch is deleted, `master` is clean.

---

## Tags

A branch is a pointer to a commit.

A tag is a pointer to a commit, too. The reason we use tags is that tags
can be given a semantic meaning to humans (it is difficult to remember and compare
hashes).

The difference between a branch and a tag is that a branch pointer moves
forward as we add commits, whereas a tag should always **point to the same
commit**.

We use tags to record particular states or milestones of a project at a given
point in time, like for instance versions (have a look at [semantic
versioning](http://semver.org)).

There are two basic types of tags: annotated and lightweight. **Use annotated
tags** since they contain the author and can be cryptographically signed using
GPG, timestamped and a message attached.

For more information about tags see for example
[the Pro Git book](https://git-scm.com/book/en/v2/Git-Basics-Tagging) chapter on the
subject.

---

## Questions

- What is a detached `HEAD`?
- What are orphaned commits?
- What will happen to orphaned commits?
- How can you recover orphaned commits?
