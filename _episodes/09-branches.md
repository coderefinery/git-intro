---
layout: episode
title: Branching and merging
teaching: 20
exercises: 15
questions:
  - How can I or my team work on multiple features in parallel?
  - How to combine the changes of parallel tracks of work?
  - How can I permanently reference a point in history, like a software
    version?
objectives:
  - Be able to create and merge branches.
  - Know the difference between a branch and a tag.
keypoints:
  - A branch is a division unit of work, to be merged with other units of work.
  - A tag is a pointer to a moment in the history of a project.
---

## Motivation for branches

In the previous section we tracked a guacamole recipe with Git.

Up until now our repository had only one branch with one commit coming
after the other:

![Linear]({{ site.baseurl }}/img/gitink/git-branch-1.svg "Linear git
repository"){:class="img-responsive"}

- Commits are depicted as little boxes with abbreviated hashes.
- The sequence of commits forms a **branch**.
- Here the branch is called "master".
- "HEAD" is the current position (remember the recording head of tape recorders?).

Software development is often not linear:

- We do not have time to write perfect code immediately, it would be nice to
  have the possibility to experiment somewhere aside.
- Interrupted work (we typically work on several longer term projects at the
  same time).
- Collaborative work on different features in the same project.
- Maintenance of releases, bug-fixes, and patches.

The strength of version control is that it permits the researcher to **isolate
different tracks of work**. Researchers can work on different things and merge
the changes they made to the source code files afterwards to create a composite
version that contains both the changes:

![Git collaborative]({{ site.baseurl }}/img/gitink/git-collaborative.svg
"description"){:class="img-responsive"}

- We see branching points and merging points.
- Main line development is often called `master`.
- Other than this convention there is nothing special about `master`, it is just a branch.
- Commits form a directed acyclic graph (we have left out the arrows to avoid confusion about the time arrow).

A group of commits that create a single narrative are called a **branch**.
There are different branching strategies, but it is useful to think that a branch
tells the story of a feature, e.g. "fast sequence extraction" or "Python interface" or "fixing bug in
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

## Creating and working with branches

Let's create a branch called `experiment` where we add cilantro to `ingredients.txt`.

```shell
$ git branch experiment    # create branch called "experiment" pointing to the present commit
$ git checkout experiment  # switch to branch "experiment"
$ git branch               # list all local branches and show on which branch we are
```

- The branch is created from the `master` branch.
- We commit our changes to this branch.
- Stage this and commit it with the message "let us try with some cilantro"

```shell
$ cat ingredients.txt

* 2 avocados
* 1 lime
* 1 tsp salt
* 1/2 onion
* 2 tbsp cilantro
```
- Edit ingredients.txt, to reduce the amount of cilantro to 1 tbsp. Stage this and commit it with the message "maybe little bit less cilantro"


## Different meanings of "checkout"

In Git the command "checkout" updates files in the working tree. However, depending on the context it is used, the way the changes are made are different. For example it it could switch to a different branch to get the versions of all the file corresponding to that branch, or it could retrieve a different version of a single file, while everything else is kept unchanged.

Some examples;

Switch to the less-salt branch
```shell
git checkout less-salt
```
Create a new branch called new_branch and switch to it,  all in one go.
```shell
git checkout -b new_branch
```
Inspect the version of a file in an older commit, using the commit hash
```shell
git checkout <HASH>
e.g.
git checkout 9c6c84e
```
Revert back to the last commited version of a file (lose all uncommitted changes), earlier in the lesson we got rid of the changes to the instructions.txt file using the following command
```shell
git checkout instructions.txt
```


## Exercise: branches

- Change to the branch `master`
- Create another branch called `less-salt`
  where you reduce the amount of salt.
- Commit your changes to the `less-salt` branch.

Use the same commands as we used above.

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

### Visualizing branches

Here is a graphical representation of what we have created (the commit hashes will be different on your laptop):

![]({{ site.baseurl }}/img/gitink/git-branch-2.svg)

Lets try to produce a visual representation of the branches using git commands.

Try the following

```shell
$ git log --all --graph --decorate --oneline --abbrev-commit
```

This was very nice way to visualise the branches and the commits. But the command has too many parameters and it is too
long to type. Fortunately Git has a solution for this using aliases:

```shell
$ git config --global alias.graph "log --all --graph --decorate --oneline --abbrev-commit"
```

Next time when we want this we will use the alias

```shell
$ git graph
```

---

## Merging branches

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

We can verify the result in the terminal.

```shell

$ git graph  #We defined this alias earlier

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

To view the branches that are merged we can use the command

```shell
$ git branch --merged
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
manually *settle merge conflicts* (we will do that later).


### Exercise: merge `experiment` into `master`

- How do the ingredients look on `master`?
- What do you expect to happen when you merge `experiment` into `master` (draw the result first)?
- **Verify** whether the result matches your expectation.

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

This is the result - discuss it with people around you:

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

Both are fine, the resulting code is the same, not the history:

![]({{ site.baseurl }}/img/gitink/no-ff.svg)

It is a matter of taste or convention.

---

## Deleting branches safely

Let us merge also the `less-salt` to `master`:

```shell
$ git checkout master
$ git merge less-salt
```

![]({{ site.baseurl }}/img/gitink/git-merge-4.svg)

Now that we are happy with the work we did in the branches, and
they have been merged into `master`, it is time to delete them:

```shell
$ git branch -d experiment
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
$ git branch -D <name>     # delete unmerged branch
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

- A tag is a pointer to a commit but in contrast to a branch it does not move.
- We use tags to record particular states or milestones of a project at a given
  point in time, like for instance versions (have a look at [semantic versioning](http://semver.org),
  v1.0.3 is easier to understand and remember than 64441c1934def7d91ff0b66af0795749d5f1954a).
- There are two basic types of tags: annotated and lightweight.
- **Use annotated tags** since they contain the author and can be cryptographically signed using
  GPG, timestamped, and a message attached.

Let's add an annotated tag to our current state of the guacamole recipe:

```shell
$ git tag -a nobel-2017 -m "recipe I made for the 2017 Nobel banquet"
```

As you may have found out already, `git show` is a very versatile command. Try this:

```shell
$ git show nobel-2017
```

For more information about tags see for example
[the Pro Git book](https://git-scm.com/book/en/v2/Git-Basics-Tagging) chapter on the
subject.

---

## Questions

- What is a detached `HEAD`?
- What are orphaned commits?
- What will happen to orphaned commits?
- How can you recover orphaned commits?
