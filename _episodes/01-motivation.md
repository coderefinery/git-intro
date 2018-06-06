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

## Food for thought

- Have you ever had to work with other people on the same project in parallel? What were the challenges?
- Have you ever had to maintain a production version of your code and work on
  new features at the same time?
- How would you convince your colleague to use version control?
- If you are already familiar with Git, have you ever had to google for
  a command to solve your problem?

What is the problem with this kind of "version control"?

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

## Explain version control in one minute

- System which **records snapshots** of a project
- Implements **branching**:
  - you can work on several feature branches and switch between them
  - different people can work on the same code without interfering
  - you can experiment with an idea and discard it if it turns out to be a bad idea
- Implements **merging**:
  - tool to merge development branches for you (conflicts may appear)

---

## Why version control?

### Roll-back functionality

- Mistakes happen - with version control you can undo and go back to a working version.


### Feature branches

- Different development lines can be organized in distinct branches.
- Branches help keeping the project organized.


### Collaboration

- No more *"can you please send me the latest version?"*.
- Allows up to thousands of persons to work on the same project without stepping on each other's toes.
- Distributed version control enables to get contributions from people you
  don't know yet and contribute to projects maintained by people who don't know
  you.


### Reproducibility

- When you publish a paper you can indicate which version exactly was used so
  others can reproduce the results.
- When you find a bug, you can find out when precisely this bug was introduced
  (are published results affected? has the bug made it to the last release of your code?).

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
