# Introduction to version control with Git - Why we want to track versions and how to go back in time to a working version

This is the introductory lesson to version control using
[Git](https://git-scm.com/). It is assumed to be the very first thing
done in a course.

Our philosophy is that we start from own local repository, branching and
merging (locally), and a brief introduction to pushing to remotes. In
the separate [collaborative Git
lesson](https://coderefinery.github.io/git-collaborative/), we teach more use of
remote repositories and good collaborative workflows. We try to stick to
simple workflows, just enough for researchers who are not obsessed with
Git to be able to work well. We try to avoid commands which might get
you into a confusing state.

The goals of the module as a whole are that the user will feel
comfortable about staging changes, committing them, merging, and
branching.

```{prereq}
- A reasonably recent version of Git (ideal is 2.28 or newer but we
  recommend at least 2.23) is installed **and configured** ([installation
  instructions](https://coderefinery.github.io/installation/)). But also on older
  Git (2.0) the workshop will work and we will offer workarounds for Git below 2.28
  or 2.23.
- For one of the episodes we need a [GitHub](https://github.com) user
  account (but alternatives exist, see below).
- Being comfortable with the command line. No expertise is required, but
  the lesson will be mostly taken from the command line. For most commands, where reasonable,
  we also offer the possibility to participate through the browser.
- To edit files on the local computer, learners should be familiar with
  using a **text editor** on their system. If you are new to text editors,
  we recommend to start with Nano or VS Code.
```

```{toctree}
:maxdepth: 1
:caption: Core episodes

motivation
basics
branches
conflicts
remotes
archaeology
level
what-to-avoid
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

reference
customizing
resources
exercises
guide
```

```{toctree}
:maxdepth: 1
:caption: About

All lessons <https://coderefinery.org/lessons/core/>
CodeRefinery <https://coderefinery.org/>
Reusing <https://coderefinery.org/lessons/reusing/>
```

```{admonition} Why GitHub?
In this introduction we will mention and use
[GitHub](https://github.com) but also
[GitLab](https://gitlab.com) and
[Bitbucket](https://bitbucket.org) allow similar workflows and
basically everything that we will discuss is transferable. With this
material and these exercises we do not implicitly endorse the company
[GitHub](https://github.com). We have chosen to demonstrate a
number of concepts using examples with
[GitHub](https://github.com) because it is currently the most
popular web platform for hosting Git repositories and the chance is
high that you will interact with
[GitHub](https://github.com)-based repositories even if you choose
to host your Git repository on another platform.
```
