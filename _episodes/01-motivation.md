---
layout: episode
title: "Motivation"
teaching: 10
exercises: 0
questions:
  - "Why version control?"
  - "Why Git?"
objectives:
  - "Discuss the reasons why we advocate distributed version control."
---

## Food for thought

- Have you ever had to work with other people on the same project in parallel? What were the challenges?
- Have you ever had to maintain a production version of your code and work on
  new features at the same time?
- How would you convince your colleague to use version control?
- If you are already familiar with Git, have you ever had to google for
  a command to solve your problem?

---

## Explain what version control is in one minute

- System which records snapshots of a project.
- Implements branching:
  - you can work on several features and switch between them
  - different people can work on the same code without interfering
- Implements merging:
  - tool merges development branches for you (conflicts may appear)

---

## Why version control?

### Roll-back functionality

- Mistakes happen, with version control you can undo and go back to a working version.


### Feature branches

- Different development lines can be organized in distinct branches.
- Help keeping the project organized.


### Collaboration

- No more *"can you please send me the latest version?"*.
- Allows up to thousands of persons to work on the same project without stepping on each other's toes.
- Distributed version control enables to get contributions from people you don't know yet.


### Reproducibility

- When you publish a paper you can indicate which version exactly was used so
  others can reproduce the results.
- When you find a bug, you can find out when precisely this bug was introduced
  (are published results affected? has the bug made it to the last release of your code?).


---

## Why Git?

- Fast
- Distributed
- Powerful
- Huge traction
- Merging and branching is easy and simple
- Important platforms such as [GitHub](https://github.com), [GitLab](https://gitlab.com), and [Bitbucket](https://bitbucket.org) build on top of Git.
- Many platforms build on top of [GitHub](https://github.com).
- *"Git is a four-handle, dual boiler espresso machine, not instant coffee."*

---

## Why Git and not [Subversion](https://subversion.apache.org)?

- Subversion is centralized.
- Git is distributed and supports any workflow.
- Distributed version control enables to:
    - implement code review
    - decentralize access control
    - decentralize bug exposure
    - commit changes without network
    - edit changes after they have been committed

---

## Why Git and not [Mercurial](https://www.mercurial-scm.org)?

- Mercurial is a fine tool but less popular than Git.
- Even if you use Mercurial chances are high you need to contribute to a code tracked by Git.
