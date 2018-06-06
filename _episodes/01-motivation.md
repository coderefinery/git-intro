---
layout: episode
title: Motivation
teaching: 15
exercises: 0
questions:
  - Why version control?
  - Why Git?
objectives:
  - Make sure nobody leaves the workshop without starting to use some form of version control.
  - Discuss the reasons why we advocate distributed version control.
---

## The essence of version control in one minute

- System which **records snapshots** of a project
- Implements **branching**:
  - you can work on several feature branches and switch between them
  - different people can work on the same code without interfering
  - you can experiment with an idea and discard it if it turns out to be a bad idea
- Implements **merging**:
  - tool to merge development branches for you

---

## Why code becomes a disaster without version control


### Roll-back functionality

- Mistakes happen - without recorded snapshots you cannot easily undo mistakes and go back to a working version.


### Branching

- Often you need to work on several issues in one code - without branching this can be messy and confusing.
- You can simulate branching by copying the entire code to multiple places but also this will be messy and confusing.


### Collaboration

- *"I will just finish my work and then you can start with your changes."*.
- *"Can you please send me the latest version?"*.
- *"Where is the latest version?"*.
- *"Which version are you using?"*.
- *"Which version have the authors used in the paper I am trying to reproduce?"*.


### Reproducibility

- How do you indicate which version of your code you have used in your paper?
- When you find a bug, how do you know when precisely this bug was introduced
  (are published results affected? do you need to inform collaborators or users of your code?).


### What is the problem with this kind of "version control"?

Discuss the following directory listing:

```shell
mylib-1.2.4_18.3.07.tgz         somecode_CP_10.8.07.tgz
mylib-1.2.4_27.7.07.tgz         somecode_CP_17.5.07.tgz
mylib-1.2.4_29.4.08.tgz         somecode_CP_23.8.07_final.tgz
mylib-1.2.4_6.10.07.tgz         somecode_CP_24.5.07.tgz
mylib-1.2.5_23.4.08.tgz         somecode_CP_25.5.07.tgz
mylib-1.2.5_25.5.07.tgz         somecode_CP_29.5.07.tgz
mylib-1.2.5_6.6.07.tgz          somecode_CP_30.5.07.tgz
mylib-1.2.5_bexc.tgz            somecode_CP_6.10.07.tgz
mylib-1.2.5_d0.tgz              somecode_CP_6.6.07.tgz
mylib-1.3.0_4.4.08.tgz          somecode_CP_8.6.07.tgz
mylib-1.3.1_4.4.08.tgz          somecode_KT.tgz
mylib-1.3.2_22.4.08.tgz         somecode_PI1_2007.tgz
mylib-1.3.2_4.4.08.tgz          somecode_PI_2007.tgz
mylib-1.3.2_5.4.08.tgz          somecode_PI2_2007.tgz
mylib-1.3.3_1.5.08.tgz          somecode_PI_CP_18.3.07.tgz
mylib-1.3.3_20.5.08.tgz         somecode_11.5.08.tgz
mylib-1.3.3_tstrm_27.6.08.tgz   somecode_15.4.08.tgz
mylib-1.3.3_wk_10.8.08.tgz      somecode_17.6.09_unfinished.tgz
mylib-1.3.3_wk_11.8.08.tgz      somecode_19.7.09.tgz
mylib-1.3.3_wk_13.8.08.tgz      somecode-20.7.09.tgz
...
```

---

## Why Git?


- Distributed
- Other people use it
- Merging and branching is easy and simple.
- Important platforms such as [GitHub](https://github.com), [GitLab](https://gitlab.com), and [Bitbucket](https://bitbucket.org)
  build on top of Git.
- Many platforms build on top of [GitHub](https://github.com).
- Sharing software and data is getting popular and required in research context
  and [GitHub](https://github.com) is a popular platform for sharing software.
- Can start using now, no need to configure a server 
- *"Git is a four-handle, dual boiler espresso machine, not instant coffee."* [citation needed]

---

## Why Git and not [Subversion](https://subversion.apache.org)?

- Subversion is centralized (one server, many clients).
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
