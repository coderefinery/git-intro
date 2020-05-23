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

## Motivation

### The essence of version control

- System which **records snapshots** of a project
- Implements **branching**:
  - you can work on several feature branches and switch between them
  - different people can work on the same code/project without interfering
  - you can experiment with an idea and discard it if it turns out to be a bad idea
- Implements **merging**:
  - tool to merge development branches for you

---

### Why code can become a disaster without version control

Discuss the following directory listing. What possible problems
do you anticipate with this kind of "version control":

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

### Why version control

#### Roll-back functionality

- Mistakes happen - without recorded snapshots you cannot easily undo mistakes and **go back to a working version**.


#### Branching

- Often you need to work on **several issues/features in one code** - without branching this can be messy and confusing.
- You can simulate branching by copying the entire code to multiple places but also this will be messy and confusing.


#### Collaboration

- *"I will just finish my work and then you can start with your changes."*.
- *"Can you please send me the latest version?"*.
- *"Where is the latest version?"*.
- *"Which version are you using?"*.
- *"Which version have the authors used in the paper I am trying to reproduce?"*.


#### Reproducibility

- How do you indicate which version of your code you have used in your paper?
- When you find a bug, how do you know **when precisely** this bug was introduced
  (are published results affected? do you need to inform collaborators or users of your code?).


#### Compare with Dropbox or Google Drive

- Document/code is in one place, no need to email snapshots.
- How can you use an old version? Possible to get old versions but in a much less useful way - snapshots of files, not directories.
- What if you want to work on multiple versions at the same time? Do you make a copy? How do you merge copies?
- What if you don't have internet?

---

> ## Why Git?
>
> We will use [Git](https://git-scm.com) to record snapshots of our work:
> - Easy to set up - use even by yourself with no server needed.
> - Very popular: chances are high you will need to contribute to somebody else's code which is tracked with Git.
> - Distributed: good backup, no single point of failure, you can track and clean-up changes offline, simplifies collaboration model for open-source projects.
> - Important platforms such as [GitHub](https://github.com), [GitLab](https://gitlab.com), and [Bitbucket](https://bitbucket.org)
>   build on top of Git.
> - Many platforms build on top of [GitHub](https://github.com).
> - Sharing software and data is getting popular and required in research context
>   and [GitHub](https://github.com) is a popular platform for sharing software.
> - However, *"Git is a four-handle, dual boiler espresso machine, not instant coffee."* [citation needed].
>   Git isn't the most user friendly and has its design quirks but deep design
>   is great and is definitely the most popular and what you are most likely to
>   need to know. So we teach it.
>
>
> ### Why not [Subversion](https://subversion.apache.org)?
>
> - Subversion is centralized (one server, many clients) and requires setting up and maintaining a server.
> - You cannot easily clean-up your recorded snapshots (commits) before you share them.
> - Not easy to get contributions from external contributors.
>
>
> ### Why not [Mercurial](https://www.mercurial-scm.org)?
>
> - Mercurial: many Git concepts still apply. For that matter, most important
>   lesson is **how and why to use version control**, which applies to any system
>   with some changes.
> - Even if you use Mercurial chances are high you need to contribute to a code tracked by Git.
{: .discussion}

---

### A real-life example

Before we create a new repository from scratch and learn how to record changes
and create and merge branches, let us explore an **existing Git repository** on
GitHub.  The goal here is not to teach GitHub yet (we will explain some of the
concepts later), but rather to get a glimpse of the wider picture and see the
social aspect to know what our end goal is.

As an example we can explore a famous Git repository which was used
to produce the Event Horizon Telescope images: [https://github.com/achael/eht-imaging](https://github.com/achael/eht-imaging).

- History
  - Explore the [repository](https://github.com/achael/eht-imaging).
  - Explore the [history](https://github.com/achael/eht-imaging/commits/master).
  - Note that there are [branches](https://github.com/achael/eht-imaging/network).
- Reproducibility
  - Discuss the enormous value of the annotation feature: [example file](https://github.com/achael/eht-imaging/blame/master/ehtim/imaging/starwarps.py).
- Collaboration
  - You can refer to [code portions](https://github.com/achael/eht-imaging/blob/31361ab62c5718b08612fc75e409795f004f5071/ehtim/imaging/starwarps.py#L66-L75)
    (so much simpler to send a link rather than describe which file to open and where to scroll to).
  - Browse the [forks](https://github.com/achael/eht-imaging/network/members).
  - See [contributors](https://github.com/achael/eht-imaging/graphs/contributors).
- Releases
  - Explore the [release history](https://github.com/achael/eht-imaging/releases).

While some of these are GitHub features, it all can be done on other sites, or
by yourself without GitHub at all.
