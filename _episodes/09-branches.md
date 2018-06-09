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

We have defined the `git graph` alias earlier using:

```shell
$ git config --global alias.graph "log --all --graph --decorate --oneline --abbrev-commit"
```

Let us inspect the project history using the `git graph` alias:

```shell
$ git graph

* dd4472c (HEAD -> master) we should not forget to enjoy
* 2bb9bb4 add half an onion
* 2d79e7e adding ingredients and instructions
```

- Commits are states characterized by a 40-character hash (checksum).
- `git graph` print abbreviations of these checksums.


### Branches are pointers

- Branches are pointers that point to a commit.
- Branch `master` points to commit `dd4472c8093b7bbcdaa15e3066da6ca77fcabadd`.

Try this:

```shell
$ cat .git/refs/heads/master
```

It will echo a long hash, for instance this one (in your case it will be different):

```shell
dd4472c8093b7bbcdaa15e3066da6ca77fcabadd
```

- That is all there is: branch `master` is simply a pointer to a hash.
- `HEAD` is another pointer, it points to where we are right now (currently `master`) - remember
  the tape recorder head.

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

- Verify that you are on the `experiment` branch:

```shell
$ git branch

* experiment
  master
```

- Then add 2 tbsp cilantro **on top** of the `ingredients.txt`:

```shell
* 2 tbsp cilantro
* 2 avocados
* 1 lime
* 2 tsp salt
* 1/2 onion
```

- Stage this and commit it with the message "let us try with some cilantro".
- Then reduce the amount of cilantro to 1 tbsp, stage and commit again with "maybe little bit less cilantro".

We have created **two new commits**:

```shell
$ git graph

* 6feb49d (HEAD -> experiment) maybe little bit less cilantro
* 7cf6d8c let us try with some cilantro
* dd4472c (master) we should not forget to enjoy
* 2bb9bb4 add half an onion
* 2d79e7e adding ingredients and instructions
```

- The branch `experiment` is two commits ahead of `master`.
- We commit our changes to this branch.


## Interlude: Different meanings of "checkout"

Depending on the context `git checkout` can do very different actions:

1) Switch to a branch:

```
$ git checkout <branchname>
```

2) Bring the working tree to a specific state (commit):

```
$ git checkout <hash>
```

3) Set a file/path to a specific state (**throws away all unstaged/uncommitted changes**):

```
$ git checkout <path/file>
```

This is unfortunate from the user's point of view but the way Git is implemented it makes sense.
Picture `git checkout` as an operation that brings the working tree to a specific state.
The state can be a commit or a branch (pointing to a commit).


## Exercise: branches

- Change to the branch `master`.
- Create another branch called `less-salt`
  where you reduce the amount of salt.
- Commit your changes to the `less-salt` branch.

Use the same commands as we used above.

We now have three branches (in this case `HEAD` points to `experiment`):

```shell
$ git branch

* experiment
  less-salt
  master

$ git graph

* bf59be6 (HEAD -> less-salt) reduce amount of salt
| * 6feb49d (experiment) maybe little bit less cilantro
| * 7cf6d8c let us try with some cilantro
|/
* dd4472c (master) we should not forget to enjoy
* 2bb9bb4 add half an onion
* 2d79e7e adding ingredients and instructions
```

Here is a graphical representation of what we have created (the commit hashes
will be different on your laptop):

![]({{ site.baseurl }}/img/gitink/git-branch-2.svg)

- Now switch to `master`.
- Add and commit the following `README.md` to `master`:

```markdown
# Guacamole recipe

Used in teaching Git.
```

Now you should have this situation:

```shell
$ git graph

* fdc8490 (HEAD -> master) draft a readme
| * bf59be6 (origin/less-salt, less-salt) reduce amount of salt
|/
| * 6feb49d (origin/experiment, experiment) maybe little bit less cilantro
| * 7cf6d8c let us try with some cilantro
|/
* dd4472c (origin/master) we should not forget to enjoy
* 2bb9bb4 add half an onion
* 2d79e7e adding ingredients and instructions
```

![]({{ site.baseurl }}/img/gitink/git-branch-3.svg)

And for comparison this is how it looks [on GitHub](https://github.com/bast/recipe/network).

---

## Merging branches

**If you got stuck in the above exercises**:

- **Skip this unless you got stuck**.
- Step out of the current directory: `$ cd ..`
- `$ git clone https://github.com/bast/recipe.git recipe-branching`
- `$ cd recipe-branching`
- `$ git graph`


It turned out that our experiment with cilantro was a good idea.
Our goal now is to merge `experiment` into `master`.

First we make sure we are on the branch we wish to merge **into**:

```shell
$ git branch

  experiment
  less-salt
* master
```

Then we merge `experiment` into `master`:

```shell
$ git merge experiment
```

![]({{ site.baseurl }}/img/gitink/git-merge-1.svg)

We can verify the result in the terminal:

```shell
$ git graph

*   c43b24c (HEAD -> master) Merge branch 'experiment'
|\
| * 6feb49d (origin/experiment, experiment) maybe little bit less cilantro
| * 7cf6d8c let us try with some cilantro
* | fdc8490 draft a readme
|/
| * bf59be6 (origin/less-salt, less-salt) reduce amount of salt
|/
* dd4472c (origin/master) we should not forget to enjoy
* 2bb9bb4 add half an onion
* 2d79e7e adding ingredients and instructions
```

What happens internally when you merge two branches is that Git creates a new
commit, attempts to incorporate changes from both branches and records the
state of all files in the new commit. While a regular commit has one parent, a
merge commit has two (or more) parents.

To view the branches that are merged into the current branch we can use the command:

```shell
$ git branch --merged

  experiment
* master
```

We are also happy with the work on the `less-salt` branch. Let us merge that
one, too, into `master`:

```shell
$ git branch  # make sure you are on master
$ git merge less-salt
```

![]({{ site.baseurl }}/img/gitink/git-merge-2.svg)

We can verify the result in the terminal:

```shell
$ git graph

*   4f00317 (HEAD -> master) Merge branch 'less-salt'
|\
| * bf59be6 (origin/less-salt, less-salt) reduce amount of salt
* |   c43b24c Merge branch 'experiment'
|\ \
| * | 6feb49d (origin/experiment, experiment) maybe little bit less cilantro
| * | 7cf6d8c let us try with some cilantro
| |/
* | fdc8490 draft a readme
|/
* dd4472c (origin/master) we should not forget to enjoy
* 2bb9bb4 add half an onion
* 2d79e7e adding ingredients and instructions
```

Observe how Git nicely merged the changed amount of salt and the new ingredient **in the same file
without us merging it manually**:

```shell
$ cat ingredients.txt

* 1 tbsp cilantro
* 2 avocados
* 1 lime
* 1 tsp salt
* 1/2 onion
```

If the same file is changed in both branches, Git attempts to incorporate both
changes into the merged file. If the changes overlap then the user has to
manually *settle merge conflicts* (we will do that later).

---

## Deleting branches safely

Both feature branches are merged:

```shell
$ git branch --merged

  experiment
  less-salt
* master
```

This means we can delete the branches:

```shell
$ git branch -d experiment less-salt

Deleted branch experiment (was 6feb49d).
Deleted branch less-salt (was bf59be6).
```

This is the result:

![]({{ site.baseurl }}/img/gitink/git-deleted-branches.svg)

Compare in the terminal:

```shell
$ git graph

*   4f00317 (HEAD -> master) Merge branch 'less-salt'
|\
| * bf59be6 (origin/less-salt) reduce amount of salt
* |   c43b24c Merge branch 'experiment'
|\ \
| * | 6feb49d (origin/experiment) maybe little bit less cilantro
| * | 7cf6d8c let us try with some cilantro
| |/
* | fdc8490 draft a readme
|/
* dd4472c (origin/master) we should not forget to enjoy
* 2bb9bb4 add half an onion
* 2d79e7e adding ingredients and instructions
```

As you see only the pointers disappeared, not the commits.

Git will not let you delete a branch which has not been reintegrated unless you
insist using `git branch -D`. Even then your commits will not be lost but you
may have a hard time finding them as there is no branch pointing to them.

---

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
