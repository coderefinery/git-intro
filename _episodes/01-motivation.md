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


## What is version control?

Version control is a system that records changes to a file or set of files over time
so that you can recall specific versions later.
For the examples if you are developing a software, you might change it over time and include
new features. All those points you made a change can be recorded and roll-back if needed if
you use a version control system

Version control system also make collaboration easier. Different collaborators can
contribute simultaneously without disturbing others and combine (merge) their
contributions at the end to for the final version.


## Why Git?

- Fast
- Distributed
- Powerful
- Huge traction
- Merging and branching is easy and simple
- Important platforms such as [GitHub](https://github.com), [GitLab](https://gitlab.com), and [Bitbucket](https://bitbucket.org) build on top of Git.
- Many platforms build on top of [GitHub](https://github.com).
- *"Git is a four-handle, dual boiler espresso machine, not instant coffee."*


## Why Git and not [Subversion](https://subversion.apache.org)?

- Subversion is centralized.
- Git is distributed and supports any workflow.
- Distributed version control enables to:
    - implement code review
    - decentralize access control
    - decentralize bug exposure
    - commit changes without network
    - edit changes after they have been committed


## Why Git and not [Mercurial](https://www.mercurial-scm.org)?

- Mercurial is a fine tool but less popular than Git.
- Even if you use Mercurial chances are high you need to contribute to a code tracked by Git.
