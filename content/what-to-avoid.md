# What to avoid


## When committing

**Commit messages that explain what has been changed but do not explain why it has been
changed**: This is as useful as code comments which describe the "obvious" such
as "this is a loop" instead of explaining why something is done this way.
But don't let perfect commit messages stop you from the most important point, committing often.

**Committing generated files**: Compiled and generated files are not
committed to version control. There are many reasons for this:

- These files can make it more difficult to run on different platforms.
- These files are automatically generated and thus do not contribute in any meaningful way.
- When tracking generated files you could see differences in the code although you haven't touched the code.

For this we use [.gitignore files](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files) where
you can list which files and paths should be ignored by Git. You can also use
wild-cards to ignore files with a certain extension or files in a certain
directory ([collection of .gitignore templates](https://github.com/github/gitignore)).

**Commit huge files**: Huge files get sometimes accidentally added and
committed which can significantly increase the repository size. Note that a
subsequent `git rm` does not remove the addition from the repository history.
Code review can help detecting accidental large file additions.
You can also add an automated test which checks for file sizes during a pull request or merge request.

**Postponing commits because the changes are "unfinished"/"ugly"**: It is
better to have many OK-ish commits than too few perfect commits.  Too few
perfect commits are probably too large and make undoing more difficult.  It is
also easier to combine too small commits than it is to split too large commits.
The longer you wait because of this, the harder it will be to
commit it at all.

**Commit unrelated changes together**: Makes it difficult to undo changes since
it can undo also the unrelated change.  But, in the end, it is probably better
to make big ugly commits than to never commit.  This is especially true in in
the chaotic early phases of small projects.


## When working with branches

**Not updating your branch before starting new work**: Few things are worse
than doing work and then noticing a lot of conflicts because
unrelated but conflicting work was done in the meantime or even before you started.  Or noticing that someone
else has already done it.  This problem is largest when you come back
to an active project weeks or months later.
So update your branch before adding new commits.

**Too ambitious branch which risks to never get completed**: The branch will
never merge back and be so big and so ambitious with too many/big features that
the risk is high that once it is really ready, there are conflicts everywhere.

**Over-engineering the branch layout and safeguards in small projects**: This
may prevent people from contributing (maybe even including yourself?). Add more
restrictions and safeguards only as the project and the group of collaborators
grows.

---

:::{discussion}
Question to all seasoned Git users: What are we missing on this page? Please
contribute improvements.
:::
