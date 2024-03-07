# Merging changes and contributing to the project

When different people do different things at the same time, it means we
have to somehow combine the changes later.  This part goes over that
**merging**.

```{objectives}
* Understand that merging is done throguh **pull requests** (= change proposal).
* Create and merge a pull request within your own repository.
* Understand (and optionally) do the same for the main public repository.
```

```{instructor-note}
Before starting the exercise session:
- Show how to open a pull request and how it can be accepted (merged).
```

## Terminology

* **upstream**:

## Exercise

In this exercise, we will show how we can *propose changes* and *merge
changes* within our own repository.  Optionally, you can propose a
recipe to the main recipe book - which shows the true purpose of this.

We offer **three different flows** of how to do this exercise.  For
the CodeRefinery workshop day 1, we use and demonstrate the **GitHub
flow** only and recommend you do that.  The exercise text below has
some Github-specific notes, but most is possibly with any flow.

:::{exercise} Exercise: Merging branches with pull requests (20 min)
We assume that in the previous exercise you have created a new branch
with a recipe.  In our previous example, it is called `new-recipe`.
If not, create it first and add a recipe to your new branch, see
{doc}`commits`.

As usual, this is basic hints.  You should refer to the solution as needed.

1. Navigate to your branch from the previous episode
   (Hint: the same branch view we used last time).

   Most of the next steps are only for the Github flow.  For VS Code /
   command line, the merge happens locally and you can do it without
   these intermediate steps.  In the future (day 2), we will see how
   you can work locally and then merge on Github.

1. This step is only for the Github flow.

   Begin a the pull request process.
   (Hint: There is a "Contribute" button in the branch view).

1. This step is only for the Github flow.

   Add or modify the pull request message, and verify the other data.

   In the pull request verify the target repository and the target
   branch. Make sure that you are merging within your own repository.
   **Github: By default, it will offer to make the change to the
   upstream repository, `coderefinery`.  You should change this**, you
   shouldn't contribute your test recipe upstream yet.  Where it says
   `base repository`, select your own user's repository.

1. This step is only for the Github flow.

   Create the pull request by clicking "Create pull request". Browse
   the network view to see if anything has changed yet.

1. Merge the pull request, or if you are not on GitHub you can merge
   the branch locally. Browse the network again. What has changed?

   (Github Hint: navigate to the pull request tab, and open it.)

1. Optional: Try to create a new branch with a new change, then open a pull
   request but towards the central repository. We will later merge few of
   those.

   (Hint: this is mostly the same as above, for the Github flow.  But,
   you set the base repository as CodeRefinery.  You might need to
   compare across forks.)
:::

Quiz:
- how to find out which branches are safe to delete?

Demo:
- conflict
- delete branches
- create release (or optional exercise step)

We will add to this page:
- intro
- screenshots
- tab on how to do this locally
- hints
- solution
- discussion
- summary
