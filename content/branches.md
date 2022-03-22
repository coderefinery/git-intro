# Branching and merging

```{objectives}
- Be able to create and merge branches.
- Know the difference between a branch and a tag.
```

```{instructor-note}
- 20 min teaching/type-along
- 15 min exercise
```


## Motivation for branches

In the previous section we tracked a guacamole recipe with Git.

Up until now our repository had only one branch with one commit coming
after the other:

```{figure} img/gitink/git-branch-1.svg
:alt: Linear Git repository
:width: 40%

Linear Git repository.
```

- Commits are depicted here as little boxes with abbreviated hashes.
- Here the branch `master` points to a commit.
- "HEAD" is the current position (remember the recording head of tape recorders?).
- When we talk about branches, we often mean all parent commits, not only the commit pointed to.


### Now we want to do this:

```{figure} img/octopus.jpeg
:alt: Branching explained with an octopus
:width: 100%

Source: <https://twitter.com/jay_gee/status/703360688618536960>
```

Software development is often not linear:

- We typically need at least one version of the code to "work" (to compile, to give expected results, ...).
- At the same time we work on new features, often several features concurrently.
  Often they are unfinished.
- We need to be able to separate different lines of work really well.

The strength of version control is that it permits the researcher to **isolate
different tracks of work**, which can later be merged to create a composite
version that contains all changes:

```{figure} img/gitink/git-collaborative.svg
:alt: Collaborative Git
:width: 100%

Collaborative Git.
```

- We see branching points and merging points.
- Main line development is often called `master` or `main`.
- Other than this convention there is nothing special about `master`, it is just a branch.
- Commits form a directed acyclic graph (we have left out the arrows to avoid confusion about the time arrow).

A group of commits that create a single narrative are called a **branch**.
There are different branching strategies, but it is useful to think that a branch
tells the story of a feature, e.g. "fast sequence extraction" or "Python interface" or "fixing bug in
matrix inversion algorithm".

````{note}
**A useful alias**

We will now define an *alias* in Git, to be able to nicely visualize branch
structure in the terminal without having to remember a long Git command
(more details about aliases are given
in a later section):

```console
$ git config --global alias.graph "log --all --graph --decorate --oneline"
```
````

Let us inspect the project history using the `git graph` alias:

```console
$ git graph

* dd4472c (HEAD -> master) we should not forget to enjoy
* 2bb9bb4 add half an onion
* 2d79e7e adding ingredients and instructions
```

- We have three commits and only
  one development line (branch) and this branch is called `master`.
- Commits are states characterized by a 40-character hash (checksum).
- `git graph` print abbreviations of these checksums.
- **Branches are pointers that point to a commit.**
- Branch `master` points to commit `dd4472c8093b7bbcdaa15e3066da6ca77fcabadd`.
- `HEAD` is another pointer, it points to where we are right now (currently `master`)


### On which branch are we?

To see where we are (where HEAD points to) use `git branch`:

```console
$ git branch

* master
```

- This command shows where we are, it does not create a branch.
- There is only `master` and we are on `master` (star represents the `HEAD`).

In the following we will learn how to create branches,
how to switch between them, how to merge branches,
and how to remove them afterwards.


## Creating and working with branches

```{instructor-note}
We do the following part together. Encourage participants to type along.
```

Let's create a branch called `experiment` where we add cilantro to `ingredients.txt`.

```shell
$ git branch experiment master   # create branch called "experiment" from master
                                 # pointing to the present commit
$ git checkout experiment        # switch to branch "experiment"
$ git branch                     # list all local branches and show on which branch we are
```

- Verify that you are on the `experiment` branch (note that `git graph` also
  makes it clear what branch you are on: `HEAD -> branchname`):

```console
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

```console
$ git graph

* 6feb49d (HEAD -> experiment) maybe little bit less cilantro
* 7cf6d8c let us try with some cilantro
* dd4472c (master) we should not forget to enjoy
* 2bb9bb4 add half an onion
* 2d79e7e adding ingredients and instructions
```

- The branch `experiment` is two commits ahead of `master`.
- We commit our changes to this branch.


(exercise-branches)=

## Exercise: Create and commit to branches

````{exercise} Branch-1: Create and commit to branches
  In this exercise, you will create another new branch and few more commits.
  We will use this in the next section, to practice
  merging.

  - Change to the branch `master`.
  - Create another branch called `less-salt`
    - Note! makes sure you are on master branch when you create the less-salt branch
    - A safer way would be to explicitly mention to create from the master branch
      as shown below
  ```console
  $ git branch less-salt master
  ```
  - Where you reduce the amount of salt.
  - Commit your changes to the `less-salt` branch.

  Use the same commands as we used above.

  We now have three branches (in this case `HEAD` points to `less-salt`):

  ```console
  $ git branch

    experiment
  * less-salt
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

  Here is a graphical representation of what we have created:

  ```{figure} img/gitink/git-branch-2.svg
  ```

  - Now switch to `master`.
  - Add and commit the following `README.md` to `master`:

  ```markdown
  # Guacamole recipe

  Used in teaching Git.
  ```

  Now you should have this situation:

  ```console
  $ git graph

  * 40fbb90 (HEAD -> master) draft a readme
  | * bf59be6 (less-salt) reduce amount of salt
  |/
  | * 6feb49d (experiment) maybe little bit less cilantro
  | * 7cf6d8c let us try with some cilantro
  |/
  * dd4472c we should not forget to enjoy
  * 2bb9bb4 add half an onion
  * 2d79e7e adding ingredients and instructions
  ```

  ```{figure} img/gitink/git-branch-3.svg
  ```

  And for comparison this is how it looks [on GitHub](https://github.com/coderefinery/recipe/network).
````


## Merging branches

It turned out that our experiment with cilantro was a good idea.
Our goal now is to merge `experiment` into `master`.

````{note}
  **If you got stuck in the above exercises** you can apply the commands below.
  But **skip this box if you managed to create branches**.

  ```console
  $ cd ..  # step out of the current directory

  $ git clone https://github.com/coderefinery/recipe.git recipe-branching
  $ cd recipe-branching

  $ git checkout experiment
  $ git checkout less-salt
  $ git checkout master

  $ git graph
  ```

  Or call a helper to un-stuck it for you.
````

First we make sure we are on the branch we wish to merge **into**:

```console
$ git branch

  experiment
  less-salt
* master
```

Then we merge `experiment` into `master`:

```console
$ git merge experiment
```

```{figure} img/gitink/git-merge-1.svg
```

We can verify the result in the terminal:

```console
$ git graph

*   c43b24c (HEAD -> master) Merge branch 'experiment'
|\
| * 6feb49d (experiment) maybe little bit less cilantro
| * 7cf6d8c let us try with some cilantro
* | 40fbb90 draft a readme
|/
| * bf59be6 (less-salt) reduce amount of salt
|/
* dd4472c we should not forget to enjoy
* 2bb9bb4 add half an onion
* 2d79e7e adding ingredients and instructions
```

What happens internally when you merge two branches is that Git creates a new
commit, attempts to incorporate changes from both branches and records the
state of all files in the new commit. While a regular commit has one parent, a
merge commit has two (or more) parents.

To view the branches that are merged into the current branch we can use the command:

```console
$ git branch --merged

  experiment
* master
```

We are also happy with the work on the `less-salt` branch. Let us merge that
one, too, into `master`:

```console
$ git branch  # make sure you are on master
$ git merge less-salt
```

```{figure} img/gitink/git-merge-2.svg
```

We can verify the result in the terminal:

```console
$ git graph

*   4f00317 (HEAD -> master) Merge branch 'less-salt'
|\
| * bf59be6 (less-salt) reduce amount of salt
* |   c43b24c Merge branch 'experiment'
|\ \
| * | 6feb49d (experiment) maybe little bit less cilantro
| * | 7cf6d8c let us try with some cilantro
| |/
* | 40fbb90 draft a readme
|/
* dd4472c we should not forget to enjoy
* 2bb9bb4 add half an onion
* 2d79e7e adding ingredients and instructions
```

Observe how Git nicely merged the changed amount of salt and the new ingredient **in the same file
without us merging it manually**:

```console
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


## Deleting branches safely

Both feature branches are merged:

```console
$ git branch --merged

  experiment
  less-salt
* master
```

This means we can delete the branches:

```console
$ git branch -d experiment less-salt

Deleted branch experiment (was 6feb49d).
Deleted branch less-salt (was bf59be6).
```

This is the result:

```{figure} img/gitink/git-deleted-branches.svg
```

Compare in the terminal:

```console
$ git graph

*   4f00317 (HEAD -> master) Merge branch 'less-salt'
|\
| * bf59be6 reduce amount of salt
* |   c43b24c Merge branch 'experiment'
|\ \
| * | 6feb49d maybe little bit less cilantro
| * | 7cf6d8c let us try with some cilantro
| |/
* | 40fbb90 draft a readme
|/
* dd4472c we should not forget to enjoy
* 2bb9bb4 add half an onion
* 2d79e7e adding ingredients and instructions
```

As you see only the pointers disappeared, not the commits.

Git will not let you delete a branch which has not been reintegrated unless you
insist using `git branch -D`. Even then your commits will not be lost but you
may have a hard time finding them as there is no branch pointing to them.


(exercise-branches-optional)=

## Optional exercises with branches

The following exercises are advanced, absolutely no problem to postpone them to a
few months later. If you give them a go, keep in mind that you might run into conflicts,
which we will learn to resolve in the next section.

````{exercise} (optional) Branch-2: Perform a fast-forward merge
1. Create a new branch from `master` and switch to it.
2. Create a couple of commits on the new branch (for instance edit `README.md`):
   ```{figure} img/gitink/git-pre-ff.svg
   ```
3. Now switch to `master`.
4. Merge the new branch to `master`.
5. Examine the result with `git graph`.
6. Have you expected the result? Discuss what you see.

  ```{solution}
  You will see that in this case no merge commit was created and Git merged the
  two branches by moving (fast-forwarding) the "master" branch (label) three
  commits forward.

  This was possible since one branch is the ancestor of the other and their
  developments did not diverge.

  A merge that does not require any merge commit is a fast-forward merge.
  ```
````

````{exercise} (optional) Branch-3: Rebase a branch (instead of merge)
As an alternative to merging branches, one can also *rebase* branches.
Rebasing means that the new commits are *replayed* on top of another branch
(instead of creating an explicit merge commit).
**Note that rebasing changes history and should not be done on public commits!**
1. Create a new branch, and make a couple of commits on it.
2. Switch back to `master`, and make a couple of commits on it.
3. Inspect the situation with `git graph`.
4. Now rebase the new branch on top of `master` by first switching to the new branch, and then `git rebase master`.
5. Inspect again the situation with `git graph`. Notice that the commit hashes have changed - think about why!

  ```{solution}
  You will notice two things:
  - History is now linear and does not contain merge commits.
  - All the commit hashes that were on the branch that got rebased, have
    changed. This also demonstrates that `git rebase` is a command that alters
    history. The commit history looks as if the rebased commits were all done
    after the `master` commits.
  ```
````


## Tags

- A tag is a pointer to a commit but in contrast to a branch it **does not ever move**.
- We use tags to record particular states or milestones of a project at a given
  point in time, like for instance versions (have a look at [semantic versioning](http://semver.org),
  v1.0.3 is easier to understand and remember than 64441c1934def7d91ff0b66af0795749d5f1954a).
- There are two basic types of tags: annotated and lightweight.
- **Use annotated tags** since they contain the author and can be cryptographically signed using
  GPG, timestamped, and a message attached.

Let's add an annotated tag to our current state of the guacamole recipe:

```console
$ git tag -a nobel-2020 -m "recipe I made for the 2020 Nobel banquet"
```

As you may have found out already, `git show` is a very versatile command. Try this:

```console
$ git show nobel-2020
```

For more information about tags see for example
[the Pro Git book](https://git-scm.com/book/en/v2/Git-Basics-Tagging) chapter on the
subject.


## Summary

Let us pause for a moment and recapitulate what we have just learned:

```console
$ git branch               # see where we are
$ git branch <name>        # create branch <name>
$ git checkout <name>      # switch to branch <name>
$ git merge <name>         # merge branch <name> (to current branch)
$ git branch -d <name>     # delete branch <name>
$ git branch -D <name>     # delete unmerged branch
```

Since the following command combo is so frequent:

```console
$ git branch <name>        # create branch <name>
$ git checkout <name>      # switch to branch <name>
```

There is a shortcut for it:

```console
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

````{challenge} Branch-4: Test your understanding
  Which of the following combos (one or more) creates a new branch and makes a commit to it?
  1. ```console
     $ git branch new-branch
     $ git add file.txt
     $ git commit
     ```
  2. ```console
     $ git add file.txt
     $ git branch new-branch
     $ git checkout new-branch
     $ git commit
     ```
  3. ```console
     $ git checkout -b new-branch
     $ git add file.txt
     $ git commit
     ```
  4. ```console
     $ git checkout new-branch
     $ git add file.txt
     $ git commit
     ```

  ```{solution}
  Both 2 and 3 would do the job. Note that in 2 we first stage the file, and then create the
  branch and commit to it. In 1 we create the branch but do not switch to it, while in 4 we
  don't give the `-b` flag to `git checkout` to create the new branch.
  ```
````

````{discussion} Different meanings of "checkout"
  Depending on the context `git checkout` can do very different actions:

  1) Switch to a branch:
     ```console
     $ git checkout <branchname>
     ```

  2) Bring the working tree to a specific state (commit):
     ```console
     $ git checkout <hash>
     ```

  3) Set a file/path to a specific state (**throws away all unstaged/uncommitted changes**):
     ```console
     $ git checkout <path/file>
     ```

  This is unfortunate from the user's point of view but the way Git is implemented it makes sense.
  Picture `git checkout` as an operation that brings the working tree to a specific state.
  The state can be a commit or a branch (pointing to a commit).

  In Git 2.23 (2019-08-16) and later this is much nicer:
  ```console
  $ git switch <branchname>  # switch to a different branch
  $ git restore <path/file>  # discard changes in working directory
  ```
````

```{keypoints}
- A branch is a division unit of work, to be merged with other units of work.
- A tag is a pointer to a moment in the history of a project.
```
