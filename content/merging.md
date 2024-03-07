# Merging changes and contributing to the project

When different people do different things at the same time, it means we
have to somehow combine the changes later.  This part goes over that
**merging**.

:::{objectives}
* Understand that merging is done throguh **pull requests** (= change proposal).
* Create and merge a pull request within your own repository.
* Understand (and optionally) do the same for the main public repository.
:::

:::{instructor-note}
Before starting the exercise session:
- Show how to open a pull request and how it can be accepted (merged).
:::

```{highlight} console
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
some GitHub-specific notes, but most is possibly with any flow.

:::::{tabs}
::::{group-tab} GitHub

:::{exercise} Exercise: Merging branches with pull requests (20 min)
We assume that in the previous exercise you have created a new branch
with a recipe.  In our previous example, it is called `new-recipe`.
If not, create it first and add a recipe to your new branch, see
{doc}`commits`.

As usual, this is basic hints.  You should refer to the solution as needed.

1. Navigate to your branch from the previous episode
   (Hint: the same branch view we used last time).

1. Begin a the pull request process.
   (Hint: There is a "Contribute" button in the branch view).

1. Add or modify the pull request message, and verify the other data.

   In the pull request verify the target repository and the target
   branch. Make sure that you are merging within your own repository.
   **Github: By default, it will offer to make the change to the
   upstream repository, `coderefinery`.  You should change this**, you
   shouldn't contribute your test recipe upstream yet.  Where it says
   `base repository`, select your own user's repository.

1. Create the pull request by clicking "Create pull request". Browse
   the network view to see if anything has changed yet.

1. Merge the pull request, or if you are not on GitHub you can merge
   the branch locally. Browse the network again. What has changed?

1. Optional: Try to create a new branch with a new change, then open a pull
   request but towards the central repository. We will later merge few of
   those.

   (Hint: this is mostly the same as above, for the GitHub flow.  But,
   you set the base repository as CodeRefinery.  You might need to
   compare across forks.)
:::
::::

::::{group-tab} Local (VS Code, Command line)

When working locally, it's easier to merge branches: we can just do
the merge, without making a pull request.

:::{exercise}

1. Navigate to the `main` branch that you want to merge the *other*
   branch into. (Note that this is the other way around from the
   GitHub flow).

Then:

5. Merge the other branch.

6. (optional, very advanced) Try to create a new branch, and make a
   GitHub pull request with your recipe, and contribute it to our
   upstream repository.  *This is very complex right now since your
   change has to get to GitHub, and we haven't shown that yet.  We
   don't give a solution for this.*


:::

::::

:::::
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



## Solution

### (1) Navigate to your branch

Before making the pull request, or doing a merge, it's important to
make sure that you are on the right branch.  Many people have been
frustrated because they forgot this!

:::::{tabs}
::::{group-tab} GitHub
::::

::::{group-tab} VS Code
Remember, you need to navigate to the `main` branch (different from)
the GitHub flow.
::::

::::{group-tab} Command line
Remember, you need to navigate to the `main` branch (different from)
the Github flow.
::::
:::::



### (2) Begin the pull request process

In GitHub, the pull request is the way we propose to merge two
branches together.  We start the process of making one.

:::::{tabs}
::::{group-tab} GitHub
::::

::::{group-tab} VS Code
n/a
::::

::::{group-tab} Command line
n/a
::::
:::::



### (3) Configure the pull request

We need to set some basic options.

:::::{tabs}
::::{group-tab} GitHub
::::

::::{group-tab} VS Code
n/a
::::

::::{group-tab} Command line
n/a
::::
:::::



### (4) Create the pull request

We actually create the pull request and see the effects.

:::::{tabs}
::::{group-tab} GitHub
::::

::::{group-tab} VS Code
n/a
::::

::::{group-tab} Command line
n/a
::::
:::::



### (5) Merge the pull request

Now, we do the actual merging.  We see some effects now.

:::::{tabs}
::::{group-tab} GitHub
::::

::::{group-tab} VS Code
::::

::::{group-tab} Command line
::::
:::::



### (6) Contribute to the original repository with a pull request

Remember, this is an advanced step.  If you do this, you are donating
a recipe to everyone.

:::::{tabs}
::::{group-tab} GitHub
::::

::::{group-tab} VS Code
(Not described, we will do this on day 2)
::::

::::{group-tab} Command line
(Not described, we will do this on day 2)
::::
:::::



## Discussion

Quiz:
- how to find out which branches are safe to delete?


* We were able to merge two branches together.
* When is this useful?
