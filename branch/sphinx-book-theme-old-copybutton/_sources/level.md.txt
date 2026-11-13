# Practical advice: how much Git is necessary?

```{instructor-note}
- 10 min teaching/discussion
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

- The `main` branch is write-protected.
- You create new feature branches for changes.
- Changes are reviewed before they are merged to the `main` branch
  (more about that in the [collaborative Git lesson](https://coderefinery.github.io/git-collaborative/)).


### When you distribute releases

- If you want to patch releases, you probably need release branches.
- The `main` branch and release branches are read-only.
- Many [branching models](https://coderefinery.github.io/git-branch-design/05-branching-models/) exist.

---

## How about staging and committing?

- It is OK to start committing directly.
- Commit early and often: rather create too many commits than too few.
  You can always combine commits later.
- Once you commit, it is very, very hard to really lose your code.
- Always fully commit (or stash) before you do dangerous things, so that you know you are safe.
  Otherwise it can be hard to recover.
- Later you can start using the staging area.
- Later start using `git add -p` and/or `git commit -p`.

---

```{keypoints}
- There is no one size fits all - start simple and grow your project.
```
