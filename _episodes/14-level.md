---
layout: episode
title: Start simple, later increase the level of complexity
teaching: 10
exercises: 0
questions:
  - What level of complexity is necessary for each project?
  - Is one branch enough?
keypoints:
  - There is no one size fits all - start simple and grow your project.
---

## What level of branching complexity is necessary for each project?


### Simple personal projects

- Typically start with just the `master` branch.
- Use branches for unfinished/untested ideas.
- Use branches when you are not sure about a change.


### Projects with few persons, you accept things breaking

- It might be reasonable to commit to the `master` branch and feature branches.


### Projects with few persons, changes are reviewed by others

- The `master` branch is write-protected.
- You create new feature branches for changes.
- Changes are reviewed before they are merged to the `master` branch
  (more about that in the [collaborative Git lesson](https://coderefinery.github.io/git-collaborative/)).


### When you distribute releases

- If you want to patch releases, you probably need release branches.
- The `master` branch and release branches are read-only.
- Many [branching models](https://coderefinery.github.io/git-branch-design/05-branching-models/) exist.

---

## How about staging?

- It is OK to start committing directly.
- If you are unsure about size of commits, rather create too many commits than too few:
  you can always combine commits later.
- Later you can start using the staging area.
- Later start using `git add -p`.
