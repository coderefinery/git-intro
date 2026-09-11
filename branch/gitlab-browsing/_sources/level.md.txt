# Practical advice: How much Git is necessary?

:::{instructor-note}
- 20 min teaching/discussion
:::


## Working on the command line? Use "git status" all the time

Unsure on which branch you are or what state the repository is in?  On the
command line, use `git status` frequently to get a quick overview.
The `git status` command is one of the most useful commands in Git
to inform about which branch we are on, what we are about to commit,
which files might not be tracked, etc.


## Writing useful commit messages

Useful commit messages summarize the change and provide context.

If you need a commit message that is longer than one line,
then the convention is: **one line summarizing the commit, then one empty line,
then paragraph(s) with more details in free form, if necessary**.

Good example:
```text
increase alpha to 2.0 for faster convergence

the motivation for this change is
to enable ...
...
(more context)
...
this is based on a discussion in #123
```

- **Why something was changed is more important than what has changed.**
- Cross-reference to issues and discussions if possible/relevant.
- Bad commit messages: "fix", "oops", "save work"
- Bad examples: [http://whatthecommit.com](http://whatthecommit.com)
- Write commit messages in English that will be understood
  15 years from now by someone else than you. Or by your future you.
- Many projects start out as projects "just for me" and end up to be successful projects
  that are developed by 50 people over decades.
- [Commits with multiple authors](https://help.github.com/articles/creating-a-commit-with-multiple-authors/) are possible.

Good references:

- ["My favourite Git commit"](https://fatbusinessman.com/2019/my-favourite-git-commit)
- ["On commit messages"](https://who-t.blogspot.com/2009/12/on-commit-messages.html)
- ["How to Write a Git Commit Message"](https://chris.beams.io/posts/git-commit/)

```{note}
A great way to learn how to write commit messages and to get inspired by their
style choices: **browse repositories of codes that you use/like**:

Some examples (but there are so many good examples):
- [SciPy](https://github.com/scipy/scipy/commits/main)
- [NumPy](https://github.com/numpy/numpy/commits/main)
- [Pandas](https://github.com/pandas-dev/pandas/commits/main)
- [Julia](https://github.com/JuliaLang/julia/commits/master)
- [ggplot2](https://github.com/tidyverse/ggplot2/commits/main),
  compare with their [release
  notes](https://github.com/tidyverse/ggplot2/releases)
- [Flask](https://github.com/pallets/flask/commits/main),
  compare with their [release
  notes](https://github.com/pallets/flask/blob/main/CHANGES.rst)

When designing commit message styles consider also these:
- How will you easily generate a changelog or release notes?
- During code review, you can help each other improving commit messages.
```

But remember: it is better to make any commit, than no commit. Especially in small projects.
**Let not the perfect be the enemy of the good enough**.


## What level of branching complexity is necessary for each project?

**Simple personal projects**:
- Typically start with just the `main` branch.
- Use branches for unfinished/untested ideas.
- Use branches when you are not sure about a change.
- Use tags to mark important milestones.
- If you are unsure what to do with unfinished and not working code, commit it
  to a branch.

**Projects with few persons: you accept things breaking sometimes**
- It might be reasonable to commit to the `main` branch and feature branches.

**Projects with few persons: changes are reviewed by others**
- You create new feature branches for changes.
- Changes are reviewed before they are merged to the `main` branch
  (more about that in the [collaborative Git lesson](https://coderefinery.github.io/git-collaborative/)).
- Consider to write-protect the `main` branch so that it can only be changed
  with pull requests or merge requests.


## How about staging and committing?

- Commit early and often: rather create too many commits than too few.
  You can always combine commits later.
- Once you commit, it is very, very hard to really lose your code.
- Always fully commit (or stash) before you do dangerous things, so that you know you are safe.
  Otherwise it can be hard to recover.
- Later you can start using the staging area (where you first stage and then commit in a second step).
- Later start using `git add -p` and/or `git commit -p`.


## How large should a commit be?

- Better too small than too large (easier to combine than to split).
- Often I make a commit at the end of the day (this is a unit I would not like to lose).
- Smaller sized commits may be easier to review for others than huge commits.
- Imperfect commits are better than no commits.
- A commit should not contain unrelated changes to simplify review and possible
  repair/adjustments/undo later (but again: imperfect commits are better than no commits).

---

:::{keypoints}
- There is no one size fits all - start simple and grow your project.
:::

:::{discussion}
How do you [plan to] use Git?

- Advanced users or beginners, please provide your input in the online collaborative document.
:::
