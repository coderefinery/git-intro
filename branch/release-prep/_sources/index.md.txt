# Introduction to version control with Git - Why we want to track versions and how to go back in time to a working version

:::{admonition} We rewrote this lesson in February and March 2024
If you are looking for the previous version, you can browse the
[2023 version of this lesson](https://coderefinery.github.io/git-intro/branch/2023-version/).
:::

This is the introductory lesson to version control using
[Git](https://git-scm.com/).

We start with an **existing repository on the web** to visually explain the basic
concepts of version control. We later move to a local
repository. Our goal there is not only to be able to apply changes to an
existing repository but to also be able to turn own projects into Git
repositories and to share them with others.

In the separate [collaborative Git
lesson](https://coderefinery.github.io/git-collaborative/), we focus more on
the collaboration and the use of remote repositories. We try to stick to simple
workflows, just enough for researchers who are not obsessed with Git to be able
to work well.

The goals of the module as a whole are that the learner will feel comfortable
about committing changes, branching, and merging.

:::{prereq}
We offer several options to go through the material: **on the web, in an editor,
or in the terminal**.
Please see the [installation instructions](https://coderefinery.github.io/installation/).
If you wish to follow in the terminal and are new to the command line, we
recorded a [short shell crash course](https://youtu.be/xbTTDLA3txI).

We recommend to have a [GitHub](https://github.com) account.
**Why GitHub?**
Also [GitLab](https://gitlab.com) and [Bitbucket](https://bitbucket.org) would
allow similar workflows and basically everything that we will discuss is
transferable. With this material and these exercises we do not implicitly
endorse the company [GitHub](https://github.com). We have chosen to demonstrate
a number of concepts using examples with [GitHub](https://github.com) because
it is currently the most popular web platform for hosting Git repositories and
the chance is high that you will interact with
[GitHub](https://github.com)-based repositories even if you choose to host your
Git repository on another service.
:::

```{toctree}
:maxdepth: 1
:caption: Getting started

motivation
configuration
```

```{toctree}
:maxdepth: 1
:caption: Modifying an existing project

browsing
commits
merging
local-workflow
```

```{toctree}
:maxdepth: 1
:caption: Studying an existing project

archaeology
```

```{toctree}
:maxdepth: 1
:caption: Sharing your work

sharing
```

```{toctree}
:maxdepth: 1
:caption: Finding the balance

level
what-to-avoid
```

```{toctree}
:maxdepth: 1
:caption: Older episodes

basics
branches
conflicts
```

```{toctree}
:maxdepth: 1
:caption: Optional episodes

staging-area
recovering
interrupted
aliases
under-the-hood
```

```{toctree}
:maxdepth: 1
:caption: Reference

Shell crash course <https://youtu.be/xbTTDLA3txI>
reference
customizing
resources
exercises
guide
PDF version <https://coderefinery.github.io/git-intro/lesson.pdf>
```

```{toctree}
:maxdepth: 1
:caption: About

All lessons <https://coderefinery.org/lessons/core/>
CodeRefinery <https://coderefinery.org/>
Reusing <https://coderefinery.org/lessons/reusing/>
```
