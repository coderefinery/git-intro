# Committing changes

The first and most basic to do is *make changes*.  Making changes
means modifying the files.  In this part, we will make changes in two
ways: on a branch (which supports multiple lines of work at once), and
directly on the main branch.

:::{objectives}
* Add new changes to our own copy of the project.
* Understand adding changes in two separate branches.
* See how to compare different versions.
:::


:::{instructor-note}
Before starting the exercise session:
- Show how to verify whether we are on our fork and not on the original repository.
:::

```{highlight} console
```

We will add to this page:
- intro
- screenshots
- tab on how to do this locally
- hints
- solution
- discussion
- summary



## Background



## Exercise

We offer **three different flows** of how to do this exercise.  For
the CodeRefinery workshop day 1, we use and demonstrate the **GitHub
flow** only and recommend you do that.


:::{exercise} Exercise: Practice creating commmits and branches (20 min)
Make sure that you work now **on your fork** of the recipe-book repository.

1. First create a branch and then add a recipe to the branch and commit the change.
1. In a new commit, modify the recipe you just added.
1. Switch to the `main` branch and modify a recipe there.
1. Browse the network and locate the commits that you just created ("Insights" -> "Network").
1. Compare the branch that you created with the `main` branch. Can you find an easy way to see the differences?
1. Can you find a way to compare versions between two arbitrary commits in the repository?
1. Try to rename the branch that you created and then browse the network again.
:::

The solution below goes over most of the answers, and you are
encouraged to use it when the hints aren't enough - this is by
design.



## Solution and walk-through

### (1) Create a branch and add recipe to the branch

There is a {term}`main` branch that is default.  We want to create a
*different* branch for our new commit, because we will *merge* it
later.

{term}`commit` is the verb to describe recording more changes, and also
the name of the thing you make.  A commit is identified by something
such as `554c187`.

:::::{tabs}
::::{group-tab} GitHub
1. Make sure that you are in your fork (your username is in the URL).
1. Where it says "main" at the top left, click, enter a new branch
   name `new-recipe`, click on the offer to create the new branch
   ("Create branch new-recipe from main").
1. Change to some sub-directory, for example `sides`
1. Make sure you are still on the `new-recipe` branch (it should say
   it at the top), and click "Add file → Create new file" from the
   upper right.
1. Enter a filename where it says "Name your file...", with a `.md` at
   the end.  Example: `mixed-nuts.md`.
1. Enter the recipe.  You can use the template below.
1. Click "Commit changes"
1. Enter a message if you want, or leave it as default.  Click "Commit
   changes".

You should appear back at the file browser view, and see your new
recipe there.

::::
::::{group-tab} VS Code
::::
::::{group-tab} Command line
```
```
::::
:::::

A recipe template is below.  This format is called "Markdown", but it
doesn't matter right now.
```markdown
# Recipe name

## Ingredients
- ingredient 1
- ingredient 2

## Instructions
1. Step 1
2. Step 2
```



### (2) Modify the recipe again

:::::{tabs}
::::{group-tab} GitHub
This is similar to before, but we click on the existing file to
modify.

1. Click on your new recipe, for example `mixed-nuts.md`.
2. Click the edit button, the pencil icon at top-right.
3. Follow the "Commit changes" instructions as in the previous step.

::::
::::{group-tab} VS Code
::::
::::{group-tab} Command line
```
```
::::
:::::

### (3) Switch to the main branch and modify a recipe there

:::::{tabs}
::::{group-tab} GitHub
1. Go back to the main repository page (your user's page)
1. In the branch switch view (top left above the file view), switch to
   `main`.
1. Modify another recipe that already exists, following the pattern
from above.  Don't modify the one you just created (but it shouldn't
even be visible on the `main` branch).

::::
::::{group-tab} VS Code
::::
::::{group-tab} Command line
```
```
::::
:::::

### (4) Browse the commits you just made

Let's look at what we did.  Now, the `main` and `new-recipe` branches
have diverged: both have some modifications.

* {term}`branch`: One line of development

:::::{tabs}
::::{group-tab} GitHub
Insights tab → Network view (just like we have done before).
::::
::::{group-tab} VS Code
::::
::::{group-tab} Command line
```
```
::::
:::::

### (5) Compare the branches

Comparing changes is an important thing we need to do.  When using the
GitHub view only, this may not be so common, but we'll show it so that
it makes sense later on.

:::::{tabs}
::::{group-tab} GitHub

TODO: I can't find this.  Do we click on the defalt proposal there?

::::
::::{group-tab} VS Code
::::
::::{group-tab} Command line
```
```
::::
:::::

### (6) Compare two arbitrary commits

This is similar to above, but not only between branches.

:::::{tabs}
::::{group-tab} GitHub

TODO: can't find.
::::
::::{group-tab} VS Code
::::
::::{group-tab} Command line
```
```
::::
:::::

### (7) Try to rename the branch

:::::{tabs}
::::{group-tab} GitHub

Branch buton → View all branches → three dots at right side → Rename branch.

::::
::::{group-tab} VS Code
::::
::::{group-tab} Command line
```
```
::::
:::::


## Discussion

In this part, we saw how we can make changes to our files.  We can
track several lines of work at once ({term}`branches <branch>`), and can compare
their differences.

* You could commit directly to `main` if there is only one single line
  of work and it's only you.
* You could commit to branches if there are multiple lines of work at
  once, and you don't want them to interfere with each other.
