# Recording changes

The first and most basic task to do in Git is **record changes** using
commits. In this part, we will record changes in two
ways: on a new branch (which supports multiple lines of work at once), and directly
on the "main" branch (which happens to be the default branch here).

:::{objectives}
* Record new changes to our own copy of the project.
* Understand adding changes in two separate branches.
* See how to compare different versions.
:::


## Background

- In the previous episode we have browsed an existing {term}`repository` and saw {term}`commits <commit>`
  and branches.
- Each commit is a snapshot of the entire project at a certain
  point in time and has a unique identifier ({term}`hash`) .
- A {term}`branch` is a line of development, and the `main` branch or `master` branch
  are often the default branch in Git.
- A branch in Git is like a sticky note that is attached to a commit. When we add
  new commits to a branch, the sticky note moves to the new commit.
- {term}`Tags <tag>` are a way to mark a specific commit as important, for example a release
  version. They are also like a sticky note, but they don't move when new
  commits are added.

:::{figure} img/gopher/gophers.png
:alt: Branching explained with a gopher
:width: 100%

What if two people, at the same time, make two different changes?  Git
can merge them together easily.  Image created using <https://gopherize.me/>
([inspiration](https://twitter.com/jay_gee/status/703360688618536960)).
:::


## Exercise

:::{figure} img/illustrations/branches.png
:alt: Illustration of what we want to achieve in this exercise
:width: 60%

Illustration of what we want to achieve in this exercise.
:::


We offer **four different paths** of how to do this exercise.  For
the CodeRefinery workshop day 1, we use and demonstrate the **GitHub
path** only and recommend you do that
(you can get experience with
the other paths on day 2).

:::{exercise} Exercise: Practice creating commits and branches (20 min)
1. Make sure that you now work **on your fork** of the recipe-book
   repository (`USER/recipe-book`, *not* `cr-workshop-exercises/recipe-book`)
1. First create a new branch and then add a recipe to the branch and commit the change.
1. In a new commit, modify the recipe you just added.
1. Switch to the `main` branch and modify a recipe there.
1. Browse the network and locate the commits that you just created ("Insights" -> "Network").
1. Compare the branch that you created with the `main` branch. Can you find an easy way to see the differences?
1. Can you find a way to compare versions between two arbitrary commits in the repository?
1. Try to rename the branch that you created and then browse the network again.
1. Try to create a tag for one of the commits that you created (on GitHub,
   create a "release").
:::

The solution below goes over most of the answers, and you are
encouraged to use it when the hints aren't enough - this is by
design.


## Solution and walk-through


### (1) Make sure you are on your fork

:::{figure} img/commits/fork.png
:alt: Screenshot on GitHub where we verify that we are on our fork.
:width: 60%
:class: with-border

You want to see your username in the URL and you want to see the "forked from
..." part.
:::


### (2) Create a branch and add a recipe to the branch

A recipe template is below.  This format is called "Markdown", but it
doesn't matter right now. You don't have to use this particular template.
```markdown
# Recipe name

## Ingredients

- Ingredient 1
- Ingredient 2


## Instructions

- Step 1
- Step 2
```

There is a {term}`main` branch that is default.  We want to create a
*different* {term}`branch` for our new commit, because we will *merge* it later.
{term}`Commit <commit>` is the verb to describe recording more changes, and also the
name of the thing you make.  A commit is identified by something such as
`554c187`.

:::::{tabs}
::::{group-tab} GitHub
1. Where it says "main" at the top left, click, enter a new branch
   name `new-recipe`, click on the offer to create the new branch
   ("Create branch new-recipe from main").
   :::{figure} img/commits/github-create-branch.png
   :alt: Screenshot on GitHub where we create a new branch.
   :width: 60%
   :class: with-border
   :::
1. Change to some sub-directory, for example `sides`.
1. Make sure you are still on the `new-recipe` branch (it should say
   it at the top), and click "Add file" → "Create new file" from the
   upper right.
1. Enter a filename where it says "Name your file...", with a `.md` at
   the end.  Example: `mixed-nuts.md`.
1. Enter the recipe.  You can use the template above.
1. Click "Commit changes"
1. Enter a commit message. Then click "Commit
   changes".

You should appear back at the file browser view, and see your new
recipe there.
::::

::::{group-tab} VS Code
1. Make sure that you are on the main branch.
1. Version control button on left sidebar → Three dots in upper right of source control → Branch → Create branch.
1. VS Code automatically switches to the new branch.

:::{figure} img/commits/vscode-create-branch.png
:width: 80%
:class: with-border
:alt: VS Code screenshot of create branch

Creating a new branch in VS Code.
:::

4. Create a new file, for example `sides/mixed-nuts.md`.
4. In the version control sidebar, click the `+` sign to add the file for the next commit.
4. Enter a brief message and click "Commit".

:::{figure} img/commits/vscode-add-and-commit.png
:alt: Screenshot of VS Code commit process
:width: 80%
:class: with-border

Committing a new file in VS Code.
:::
::::

::::{group-tab} Command line
Create a new branch called `new-recipe` from `main` and switch to it:
```console
$ git switch --create new-recipe main
```

Then create the new file. Finally add and commit the file:
```console
$ git add sides/mixed-nuts.md
$ git commit -m "Add mixed nuts recipe"
```
::::

::::{group-tab} RStudio
1. In the Git tab of the Environment panel (upper right), click New Branch.
1. In the pop-up fill in the branch name, e.g. "new-recipe", untick the box in front of Sync branch with remote
to avoid the branch to be pushed to GitHub right away.
1. Click Create and RStudio will automatically switch to the new branch.

    :::{figure} img/commits/rstudio-create-branch.png
    :width: 80%
    :class: with-border
    :alt: RStudio screenshot of create branch
    :::

1. Create a new file, for example `sides/mixed-nuts.md`. Remember to save any changes to your file before commiting.
1. In the Git tab in the Environment panel (upper right) check the box in front of the file you just created, then 
   click Commit in the tab menu-bar to open the Git Changes window.

    :::{figure} img/commits/rstudio-add-commit.png
    :alt: Screenshot of RStudio commit process in the main window
    :width: 80%
    :class: with-border
    :::

1. In the Changes window, check that your new file is selected (ticked), write a short commit message, and finally 
   click "Commit"
    
    :::{figure} img/commits/rstudio-commit-changes.png
    :alt: Screenshot of RStudio commit process in the changes window
    :width: 80%
    :class: with-border
    :::

::::

:::::


### (3) Modify the recipe with a new commit

:::::{tabs}
::::{group-tab} GitHub
This is similar to before, but we click on the existing file to
modify.

1. Click on your new recipe, for example `mixed-nuts.md`.
2. Click the edit button, the pencil icon at top-right.
3. Follow the "Commit changes" instructions as in the previous step.
::::

::::{group-tab} VS Code
Repeat as in the previous step.
::::

::::{group-tab} Command line
Modify the file. Then commit the new change:
```console
$ git add sides/mixed-nuts.md
$ git commit -m "Short summary of the change"
```

Make sure to replace "Short summary of the change" with a meaningful commit
message.
::::

::::{group-tab} RStudio
Make some changes to the recipe you created in the step above. Then follow the same instructions as above starting 
from step 5.
::::

:::::


### (4) Switch to the main branch and modify a recipe there

:::::{tabs}
::::{group-tab} GitHub
1. Go back to the main repository page (your user's page).
1. In the branch switch view (top left above the file view), switch to
   `main`.
1. Modify another recipe that already exists, following the pattern
   from above. Don't modify the one you just created (but it shouldn't
   even be visible on the `main` branch).
::::

::::{group-tab} VS Code
Use the branch selector at the bottom to switch back to the main branch.  Repeat the same steps as above.

:::{figure} img/commits/vscode-change-branch.png
:class: with-border
:width: 80%
:alt: VS Code screenshot

Switching branch via selector at bottom.
::::

::::{group-tab} Command line
First switch to the `main` branch:
```console
$ git switch main
```

Then modify a file. Finally `git add` and then commit the change:
```console
$ git commit -m "Short summary of the change"
```
::::

::::{group-tab} RStudio
In the Git tab of the Environment panel (upper right), click your current branch name, here "new-recipe" and then 
choose the "main" branch.

:::{figure} img/commits/rstudio-switch.png
:class: with-border
:width: 100%
:alt:  Screenshot showing how to switch branch in RStudio
::::

Modify another recipe and commit your changes.
:::::


### (5) Browse the commits you just made

Let's look at what we did.  Now, the `main` and `new-recipe` branches
have diverged: both have some modifications. Try to find the commits
you created.

:::::{tabs}
::::{group-tab} GitHub
Insights tab → Network view (just like we have done before).
::::

::::{group-tab} VS Code
This requires an extension.  Opening the VS Code terminal lets you use the command line method.

:::{figure} img/commits/vscode-open-terminal.png
:class: with-border
:width: 80%
:alt: VS Code screenshot as described

View → Terminal will open a terminal at bottom.  This is a normal command line interface and very useful for work.  (Note the git-aware prompt that shows the current branch.  This requires other setup.)
::::

::::{group-tab} Command line
```console
$ git graph
$ git log --graph --oneline --decorate --all  # If you didn't define git graph yet.
```

In my case I got:
```{code-block}
---
emphasize-lines: 1-3
---
* b4de93b (HEAD -> main) add spring onion to poke
| * dc5d6f0 (origin/new-recipe, new-recipe) adding chocolate to the mixed nuts recipe
| * b4035e3 add mixed nuts recipe
|/
*   554c187 (origin/main, origin/HEAD) Merge branch 'alex/fruit-salad'
|\
| * 89d5ef9 fruit salad: instructions
| * 3bd2468 fruit salad: ingredients
* | 8bcb766 a todo note to not forget the instructions
|/
* b950c5c just fixing capitalization
* d18035e fix formatting
* 7051cca add some cilantro
* ae19e81 add categories for easier browsing
* a6fe629 we also need salad
* 30b89c4 document what this is about
*   fd12dc1 Merge branch 'radovan/lasagna'
|\
| * 7753d43 vegetarian lasagna: instructions
| * aa0473e vegetarian lasagna: ingredients
* |   1e5a24a Merge branch 'radovan/poke'
|\ \
| * | 5aa6687 oh no! forgot onion - adding
| * | cc84e4f working on a poke recipe
| |/
* | 9500901 a classic pumpkin pie recipe - yum!
* | 34ce939 drafting a recipe for a pasta, so far only ingredients
* | 28e5f26 recipe for a mushroom soup
|/
* a550963 reduce amount of salt
* f2d6d58 don't forget to enjoy
* 1fde064 add half an onion
* 4c1873e drafting a guacamole recipe
* 2992443 this will be licensed under CC0
* 084a1ea starting with an almost empty readme
```
::::

::::{group-tab} RStudio
1. Open the history window like you did during the previous lesson.
2. Select "(All branches)" in the branch selector drop-down menu to see all the commits on all branches.
    :::{figure} img/commits/rstudio-history-all-branches.png
    :class: with-border
    :width: 80%
    :alt: Screenshot of the History window in RStudio showing all branches and all commits
> **NOTE:** If you don't see the branch selector when you first open the History window, try to switch from the History 
> view to the Changes view and back. 
::::

:::::


### (6) Compare the branches

Comparing changes is an important thing we need to do.  When using the
GitHub view only, this may not be so common, but we'll show it so that
it makes sense later on.

:::::{tabs}

::::{group-tab} GitHub
A nice way to compare braches is to add `/compare` to the URL of the repository,
for example (replace USER):
`https://github.com/USER/recipe-book/compare`
::::

::::{group-tab} VS Code
This seems to require an extension.  We recommend you use the command line method.
::::

::::{group-tab} Command line
```console
$ git diff main new-recipe
```

Try also the other way around:
```console
$ git diff new-recipe main
```

Try also this if you only want to see the file names that are different:
```console
$ git diff --name-only main new-recipe
```
::::

::::{group-tab} RStudio
This doesn't seem possible in RStudio without an add-in. We recommend that you use the Terminal in RStudio and follow 
the "Command line" path instructions.
::::

:::::


### (7) Compare two arbitrary commits

This is similar to above, but not only between branches.

:::::{tabs}
::::{group-tab} GitHub
Following the `/compare`-trick above, one can compare commits on GitHub by
adjusting the following URL:
`https://github.com/USER/recipe-book/compare/VERSION1..VERSION2`

Replace `USER` with your username and `VERSION1` and `VERSION2` with a commit hash or branch name.
Please try it out.
::::

::::{group-tab} VS Code
Again, we recommend using the Command Line method.
::::

::::{group-tab} Command line
First try this to get a short overview of the commits:
```console
$ git log --oneline
```

Then try to compare any two commit identifiers with `git diff`.
::::

::::{group-tab} RStudio
Again, this doesn't seem possible in RStudio without an add-in. We recommend that you use the Terminal in RStudio and 
follow the "Command line" path instructions.
::::

:::::


### (8) Renaming a branch

:::::{tabs}
::::{group-tab} GitHub

Branch button → View all branches → three dots at right side → Rename branch.

::::
::::{group-tab} VS Code
Version control sidebar → Three dots (same as in step 2) → Branch → Rename branch.  Make sure you are on the right branch before you start.
::::

::::{group-tab} Command line
Renaming the current branch:
```console
$ git branch -m better-recipe
```

Renaming a different branch:
```console
$ git branch -m new-recipe better-recipe
```
::::

::::{group-tab} RStudio
Again, this doesn't seem possible in RStudio without an add-in. We recommend that you use the Terminal in RStudio and 
follow the "Command line" path instructions.
::::

:::::


### (9) Creating a tag

Tags are a way to mark a specific commit as important, for example a release
version. They are also like a sticky note, but they don't move when new
commits are added.

:::::{tabs}
::::{group-tab} GitHub
Click on the branch switcher, and then on "Tags", then on "View all tags", then
"Create a new release":
   :::{figure} img/commits/github-create-tag.png
   :alt: Screenshot on GitHub where we create a new tag.
   :width: 60%
   :class: with-border
   :::

What GitHub calls releases are actually tags in Git with additional metadata.
For the purpose of this exercise we can use them interchangeably.
::::

::::{group-tab} VS Code
Version control sidebar → Three dots (same as in step 2) → Tags → Create tag.  Make sure you are on the expected commit before you do this.
::::

::::{group-tab} Command line
Creating a tag:
```console
$ git tag -a v1.0 -m "New manuscript version of my recipe for the pre-print"
```
::::

::::{group-tab} RStudio
Again, this doesn't seem possible in RStudio without an add-in. We recommend that you use the Terminal in RStudio and 
follow the "Command line" path instructions.
::::

:::::


## Discussion

In this part, we saw how we can make changes to our files.
With {term}`branches <branch>`, we can
track several lines of work at once, and can compare
their differences.

- You could commit directly to `main` if there is only one single line
  of work and it's only you.
- You could commit to branches if there are multiple lines of work at
  once, and you don't want them to interfere with each other.
- Tags are useful to mark a specific commit as important, for example a
  release version.
- In Git, commits form a so-called "graph". Branches are tags in Git function
  like sticky notes that stick to specific commits. What this means for us is
  that it does not cost any significant disk space to create new branches.
- Not all files should be added to Git. For example, temporary files or
  files with sensitive information or files which are generated as part of
  the build process should not be added to Git. For this we use
  `.gitignore` (more about this later: {ref}`what-to-avoid`).
- Unsure on which branch you are or what state the repository is in?
  On the command line, use `git status` frequently to get a quick overview.
