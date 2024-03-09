# Copy and browse an existing project

In this episode, we will look at an **existing repository** to
understand how all the pieces work together. Along the way, we will make a copy
(a {term}`fork`) of the {term}`repository` for us, which will be used for our
own changes in the next episode.

- We used to start by directly going and creating a repository from scratch. This
  was abstract and hard to understand.
- Instead, we'll show you all the cool stuff in a Git repository
  first, and then start adding files.
- We use an example recipe book we created just for this course.
- By the end of the course, you'll know how to contribute your own
  recipes to it.

:::{objectives}
* See a real Git repository and understand what is inside of it.
* Understand how version control allows advanced inspection of a
  repository.
* See how Git allows multiple people to collaborate easily.
:::


## GitHub, VS Code, Command line, and more

We offer **three different paths** of how to do this exercise:
- **GitHub** (this is the one we will demonstrate)
- **VS Code** (if you prefer to follow along using an editor)
- **Command line** (for people comfortable with the command line)

In the future we'll add more paths, for example Jupyter and RStudio
(contributions welcome!).


## Creating a copy of the repository by "forking"

First, we need to make our own copy of the repository.
This will become important later, when we make our own changes.

1. Go to the repository view on GitHub: <https://github.com/coderefinery/recipe-book>
1. First, on GitHub, click the button that says "Fork".  It is towards
   the top-right of the screen:
   :::{figure} img/browsing/forking.png
   :alt: Screenshot on GitHub before clicking on "Fork"
   :width: 80%
   :class: with-border
   :::
1. You should shortly be redirected to your copy of the repository.

At all times you should be aware of if you looking at *your* repository
or the *CodeRefinery {term}`upstream`* repository.
* Your repository: https://github.com/**USERNAME**/recipe-book
* CodeRefinery upstream repository: https://github.com/**coderefinery**/recipe-book

:::::{tabs}
::::{group-tab} GitHub
You only need to open your own view, as described above.  The browser
URL should look like `https://github.com/USER/recipe-book`, where
`USER` is your GitHub username.
::::

::::{group-tab} VS Code
We need to start by making a copy of this repository locally.

1. Start VS Code.
1. If you don't have the default view (you already have a project
open), go to File → New Window.
1. Under "Start" on the screen, select "Clone Git Repository...".
1. Paste in this URL: `https://github.com/USER/recipe-book`, where
   `USER` is your username.  You can copy this from the browser.
1. Browse and select the folder in which you want to clone the
   repository.
1. Say yes, you want to open this repository.
1. Select "Yes, I trust the authors" (the other option works too).
::::

::::{group-tab} Command line
**This path is advanced and we do not include all command line
information: you need to be somewhat
comfortable with the command line already.**

We need to start by making a copy of this repository locally.

1. Start the terminal in which you use Git (terminal application, or
   Git Bash).
1. Change to the directory where you would want the repository to be
   (`cd ~/code` for example, if the `~/code` directory is where you
   store your files).
1. Run the following command: `git clone
   https://github.com/USER/recipe-book`, where `USER` is your
   username.  You might need to use a SSH clone command instead of
   HTTPS, depending on your setup.
1. Change to that directory: `cd recipe-book`
::::
:::::


## Exercise

Work on this by yourself or in your team.

:::{instructor-note}
Before starting the exercise session:
- Make sure you have shown how to fork the repository to own account
  (above).
:::

:::{exercise} Exercise: Browsing an existing project (25 min)

Then browse the project and explore commits and branches. Take notes and prepare questions.

1. Browse the **commit history**: Are commit messages understandable?
   (Hint: "Commit history", the timeline symbol, above the file list)
1. Compare the commit history with the **network graph** ("Insights" -> "Network"). Can you find the branches?
1. How can you find out when a recipe was **last modified**?
1. **How many changes** did the Guacamole recipe receive (you find it under "sides")?
   Try to click on some of the commits to see what changed.
   (Hint: "History" in the view of a single file)
1. **Which recipes include the ingredient "salt"**?
   (Hint: the GitHub search.  From the repository view, it should offer
   the filter "repo:coderefinery/recipe-book" by default.  What if you
   add a search term?)
1. In the Guacamole recipe, find out **who modified each line last and when**
   (click on file, then click "Blame" button). Find out who added the cilantro
   and in which commit.
   (Hint: "Blame" view in the file view)
1. Can you use these recipes yourself? **Are you allowed to share
   modifications**?
   (Hint: look for a license file)
1. **Browse issues and pull requests** in the {term}`upstream` repository (the
   repository you forked from). Any idea what these might be good for?
   (Hint: tabs in the repository view)
:::


The solution below goes over most of the answers, and you are
encouraged to use it when the hints aren't enough - this is by
design.


## Solution and walk-through

### (1) Basic browsing

The most basic thing to look at is the history of commits.

* This is visible from a button in the repository view.  We see every
  change, when, and who has committed.
* Every change has a unique identifier, such as `554c187`.  This can
  be used to identify both this change, and the whole project's
  version as of that change.
* Clicking on a change in the view shows more.

:::::{tabs}

::::{group-tab} GitHub
Click on the timeline symbol in the repository view:
  :::{figure} img/browsing/history.png
  :alt: Screenshot on GitHub of where to find the commit history
  :width: 100%
  :class: with-border
  :::
::::

::::{group-tab} VS Code
This can be done from "Timeline", in the bottom of explorer, but only
for a single file.
::::

::::{group-tab} Command line
Run `git log`.
::::

:::::


### (2) Compare commit history with network graph

The commit history we saw above looks linear: one commit after
another.  But if we look at the network view, we see some branches and
merges.  We'll see how to do these later.

:::::{tabs}
::::{group-tab} GitHub
In a new browser tab, open the "Insights" tab, and click on "Network".
You can hover over the commit dots to see the person who committed and
how they correspond with the commits in the other view:
  :::{figure} img/browsing/network.png
  :alt: Screenshot on GitHub of the network graph
  :width: 100%
  :class: with-border
  :::
::::

::::{group-tab} VS Code
We don't know how to do this without an extension. Try starting a terminal and using the
"Command Line" option.
::::

::::{group-tab} Command line
You can view the network graph with:
```console
$ git log --graph --oneline --decorate --all
::::

:::::


### (3) When was a recipe last modified?

We see the history for the whole repository, but we can also see it
for a single file.

:::::{tabs}

::::{group-tab} GitHub
Navigate to the file view: Main page → sides directory →
guacamole.md. Click the "History" button near the top right:
  :::{figure} img/browsing/file-history.png
  :alt: Screenshot on GitHub showing the history of a single file
  :width: 100%
  :class: with-border
  :::
::::

::::{group-tab} VS Code
Open sides/guacamole.md file in the editor.  Under the file browser,
we see a "Timeline" view there.
::::

::::{group-tab} Command line
The `git log` command can take a filename and provide the log of only
a single file:

```
$ git log sides/guacamole.md
```
::::

:::::


### (4) How many changes did the Guacamole recipe receive?

According to the view above, it seems to have five changes (as of
2024-03-07).  This could change later on.


### (5) Which recipes include the ingredient "salt"

Version control makes it very easy to find all occurrences of a single
word. This is useful for things like finding where things are
defined.

:::::{tabs}
::::{group-tab} GitHub
We go to the main recipe book view.  We click the Search magnifying
class at the very top, type "salt", and click enter. We see every
instance, including the context:
  :::{figure} img/browsing/search.png
  :alt: Screenshot on GitHub performing a search
  :width: 100%
  :class: with-border
  :::
::::

::::{group-tab} VS Code
If you use the "Search" magnifying class on the left sidebar, and
search for "Salt" it shows the occurrences in every file. You can
click to see the usage in context.
::::

::::{group-tab} Command line
`grep` is the command line tool that searches for lines matching a term
```
$ git grep salt          # only the lines
$ git grep -C 3 salt     # three lines of context
$ git grep -i salt       # case insensitive
```
::::

:::::


### (6) Who modified each line last and when?

This is called the "annotate" or "blame" view. The name "blame"
is very unfortunate, but it is the standard term for historical reasons
for this functionality and it is not meant to blame anyone.

:::::{tabs}

::::{group-tab} GitHub
From a recipe view, change preview to "Blame" towards the top-left.
To get the actual commit, click on the commit message.
  :::{figure} img/browsing/annotate.png
  :alt: Screenshot on GitHub showing the "Blame" view
  :width: 100%
  :class: with-border
  :::
::::

::::{group-tab} VS Code
This requires an extension.  We recommend for now you use the command
line version, after opening a terminal.
::::

::::{group-tab} Command line
These two commands are similar but have slightly different output.
```
$ git annotate sides/guacamole.md
$ git blame sides/guacamole.md
```
::::

:::::


### (7) Can you use these recipes yourself? Are you allowed to share modifications?

* Look at the file `LICENSE`.
* It says it is "Creative Commons Zero 1.0", which is equivalent to
  public domain.  You can use them without conditions.
* Note the GitHub view of the file `LICENSE` gives a nice summary of what it
  means. Try it out:
  :::{figure} img/browsing/license.png
  :alt: Screenshot on GitHub summarizing license terms
  :width: 100%
  :class: with-border
  :::


### (8) Browse issues and pull requests in the {term}`upstream` repository

This can only be done through the GitHub view.  Go to the main
repository, the one of "CodeRefinery" (not your fork):
<https://github.com/coderefinery/recipe-book>.  Issues and Pull
Requests are different for each GitHub copy.

* Click on the "Issues" tab.  These are notes that people have added,
  which allow discussion about the project. Often they are used to communicate
  problems or ideas.
* Click on the "Pull requests" tab. This allows anyone to *propose
  changes*, but only the repository owners can accept.


## Summary

- Git allowed us to understand this simple project much better than we
  could, if it was just a few files on our own computer.
- It was also very easy to share the project with the course.
- By forking the repository, we created our own copy. This is
  important for the next episode, where we will make changes to
  our copy.
