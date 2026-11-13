# Practical advice: how much Git is necessary?

```{instructor-note}
- 20 min teaching/discussion
```


## What level of branching complexity is necessary for each project?


### Simple personal projects

- Typically start with just the `main` branch.
- Use branches for unfinished/untested ideas.
- Use branches when you are not sure about a change.
- Use tags to mark important milestones.


### Projects with few persons: you accept things breaking sometimes

- It might be reasonable to commit to the `main` branch and feature branches.


### Projects with few persons: changes are reviewed by others

- You create new feature branches for changes.
- Changes are reviewed before they are merged to the `main` branch
  (more about that in the [collaborative Git lesson](https://coderefinery.github.io/git-collaborative/)).
- The `main` branch is write-protected and can only be changed with pull requests or merge requests.


### When you distribute releases

- If you want to patch releases, you probably need release branches.
- The `main` branch and release branches are read-only.
- Many [branching models](https://coderefinery.github.io/git-branch-design/05-branching-models/) exist.

---

## How about staging and committing?

- It is OK to start committing directly by doing `git commit SOMEFILE`.
- Commit early and often: rather create too many commits than too few.
  You can always combine commits later.
- Once you commit, it is very, very hard to really lose your code.
- Always fully commit (or stash) before you do dangerous things, so that you know you are safe.
  Otherwise it can be hard to recover.
- Later you can start using the staging area.
- Later start using `git add -p` and/or `git commit -p`.

---

## How large should a commit be?

- Better too small than too large (easier to combine than to split).
- Often I make a commit at the end of the day (this is a unit I would not like to lose).
- Smaller sized commits may be easier to review for others than huge commits.
- Imperfect commits are better than no commits.
- A commit should not contain unrelated changes to simplify review and possible
  repair/adjustments/undo later (but again: imperfect commits are better than no commits).

---

```{keypoints}
- There is no one size fits all - start simple and grow your project.
```

```{discussion}
How do you [plan to] use Git?

- Advanced users or beginners, please provide your input in the online collaborative document.
```

