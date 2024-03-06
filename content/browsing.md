# Copy and browse an existing project

The first thing most people do is **contribute to an existing
project**.  This, and following lessons, go over this.  We use an
an example recipe book on Github.

```{objectives}
* See a real git repository and understand what is inside of it.
* Understand how version control allows advanced inspection of a
  repository.
* See how git allows multiple people to take collaborate.
```

```{instructor-note}
Preparation:
- Create an exercise repository from
  <https://github.com/coderefinery/recipe-book-template> preserving history
  (this means not using "generating from template")
- Create one or two issues
- Create one or two pull requests
- Try to search for something in the recipe to trigger a search index update

Before starting the exercise session:
- Show how to fork the repository to own account
```


We will add to this page:
- intro
- screenshots
- tab on how to do this locally
- hints
- solution
- discussion
- summary


## Introduction

* You will probably interact with more repositories owned by other
  people than with your own
* It's easier to get to know your own repositories

## Exercise

Work on this by yourself.  The solution below goes over most of the
answers, but the hints should get you most of the way.  Refer to the
solution if you get stuck.

We offer **three different flows** of how to do this exercise.  For
the CodeRefinery workshop day 1, we use and demonstrate the **GitHub
flow** only and recommend you do that.

```{exercise} Exercise: Browsing an existing project (25 min)
First **make a copy** to your own account to work on **by forking**
<https://github.com/coderefinery/recipe-book>

Then browse the project and explore commits and branches. Take notes and prepare questions.

1. Browse the commit history: Are commit messages understandable?
   (Hint: "Commit history" (like "25 commits") above the file list.)
1. Compare the commit history with the network graph ("Insights" -> "Network"). Can you find the branches?
1. How can you find out when a recipe was last modified?
1. How many changes did the Guacamole recipe receive (you find it under "sides")?
   Try to click on some of the commits to see what changed.
   (Hint: "History" in the view of a single file.)
1. Which recipes include the ingredient "salt"?
   (Hint: the Github search.  From the repository view, it should offer
   the filter "repo:coderefinery/recipe-book" by default.  What if you
   add a search term?)
1. In the Guacamole recipe, find out who modified each line last and when
   (click on file, then click "Blame" button). Find out who added the cilantro
   and in which commit.
   (Hint: "Blame" view in the file view)
1. How many people have contributed to the repository?
   (Hint: under "Insights")
1. Can you use these recipes yourself? Are you allowed to share
   modifications?
   (Hint: look for a license file)
1. Browse issues and pull requests, any idea what these might be good
   for?
   (Hint: tabs in the repository view)
```


## Setup

```{note}

In the CodeRefinery workshop itself, we follow the **Github** flow.
**VSCode** and **Command line** are for reference, for people who
already know enough to follow.  They do not have full information and
screenshots, and may not be complete.
```

First, we need to make our own copy of the repository.  This will
become important later, when we make our own changes.

1. Go to the repository view on Github (everyone should do this,
   regardless of which flow you are using): <https://github.com/coderefinery/recipe-book>
1. First, on Github, click the button that says "Fork".
1. TODO.

`````{tabs}
````{group-tab} Github
You only need to open your own view.  The browser URL should look like
`https://github.com/USER/recipe-book`, where `USER` is your Github username.
````

````{group-tab} VSCode

We need to start by making a copy of this repository locally.

1. Start VSCode
1. If you don't have the default view (you already have a project
open), go to File → New Window
1. Under "Start" on the screen, select "Clone Git Repository..."
1. Paste in this URL: `https://github.com/USER/recipe-book`, where
   `USER` is your username.  You can copy this from the browser.
1. Browse and select the folder in which you want to clone the
   repository.
1. Say yes, you want to open this repository
1. Select "Yes, I trust the authors" (the other option works too).
````
````{group-tab} Command line

**This flow is advanced and we do not include all command line
information for a new person to do this: you need to be somewhat
comfortable with the command line already.**

We need to start by making a copy of this repository locally.

1. Start the terminal in which you use git (Terminal application, or
   Git-Bash).
1. Change to the directory where you would want the repository to be
   (`cd code` for example)
1. Run the following command: `git clone
   https://github.com/USER/recipe-book`, where `USER` is your
   username.  You might need to use a SSH clone command instead of
   HTTPS, depending on your setup.
1. Change to that directory: `cd recipe-book`
````
`````



## (1) Basic browsing

The most basic thing to look at is the history of commits.

* This is visible from a button in the repository view.  We see every
  change, when, and who has committed.
* Every change has a unique identifier, such as `554c187`.  This can
  be used to identify both this change, and the whole project's
  version as of that change.
* Clicking on a change in the view shows more.

`````{tabs}
````{group-tab} Github

Click on "History.
````
````{group-tab} VSCode

This can be done from "Timeline", in the bottom of explorer, but only
for a single file.
````
````{group-tab} Command line

Run `git log`.
````
`````

## (2) Compare commit history with network graph

## (3) When was a recipe last modified?

## (4) How many changes did the Guacamole recipe receive?

## (5) Which recipes include the ingredient "salt" ?

## (6) Who modified each line last?

## (7) How many people have contributed to the repository?

## (8) Can you use these recipes yourself?

* In all flows, look at the file `LICENSE`.
* It says it is "Creative Commons Zero 1.0", which is equivalent to
  public domain.  You can use them for anything.
* Note the Github view of the file `LICENSE` gives a nice summary of what it means.



## (9) Browse issues and pull requests

This can only be done through the Github view.  Go to the main
repository, the one of "CodeRefinery" (not your fork):
<https://github.com/coderefinery/recipe-book>.  Issues and Pull
Requests are different for each Github copy.

* Click on the Issues" tab.  These are notes that people have added,
  which allow discussion about the project.
* Click on the "Pull requests" tab.  This allows anyone to *propose
  changes*, but only the repository owners can accept.



## Summary
