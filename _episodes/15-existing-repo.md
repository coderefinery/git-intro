---
layout: episode
title: (Optional) In-browser session
teaching: 20
exercises: 0
questions:
  - How can I contribute to repositories without command line?
objectives:
  - See an existing repository in action.
  - Browse the history.
  - See the big picture without going into command line details.
---

# In-browser session

- We will explore and visualize an **existing Git repository** on GitHub and make small changes to it.
- The goal of this episode is not to teach GitHub, but rather to get a glimpse of the
wider picture.

---

## Why

- Often our first contact with Git is an existing repository, and it is
  relatively easy to contribute to them.
- The existing repository is often on GitHub (but this demonstration applies
  equally well to GitLab or Bitbucket).
- Most of the Git commands we are about to learn can be done in the browser,
  which is a more intuitive way to get started.
- It's good to see the social aspect to know what our end goal is.

---

## Do not worry

- If you are new to version control, don't focus on what we do. Focus on what comes out of it.
- When browsing a GitHub repository we are looking at **two layers**. Later we
  will explain what is in the Git layer and what is in the GitHub layer.

---

## Demo

We start with an
[existing repository](https://github.com/coderefinery/example-project)
that contains a couple of commits and two
branches with some easy code.

The project contains several obvious issues (bug in code,
typo in documentation, missing license file, outdated usage example).

- History
  - Explore the [repository](https://github.com/coderefinery/example-project).
  - Explore the [history](https://github.com/coderefinery/example-project/commits/master).
  - Browse commit changesets.
  - Note that there are [branches](https://github.com/coderefinery/example-project/network).
- Reproducibility
  - Find a bug in
    [example.py](https://github.com/coderefinery/example-project/blob/master/example.py)
    and use annotation to check when precisely the bug got introduced.
  - Discuss the enormous value of the annotation feature.
- Collaboration
  - You can refer to [code portions](https://github.com/coderefinery/example-project/blob/master/example.py#L18-L19)
    (so much simpler to send a link rather than describe which file to open and where to scroll to).
  - Identify other issues (bug in code, misleading comment, typo in
    documentation, missing license file, outdated usage example).
  - Instructors use the browser to create a branch and make a commit to an
    existing project: Instructors will make a change concurrently, one of them
    (the presenter) will do one change on the screen. Also experienced participants
    can already join.
  - Make a merge request (it's easy in browser, and shows cool stuff).
  - Browse the [network](https://github.com/coderefinery/example-project/network).
  - See [contributors](https://github.com/coderefinery/example-project/graphs/contributors).
- Releases
  - Explore the [history](https://github.com/coderefinery/example-project/commits/master) again.
  - Create a [release](https://github.com/coderefinery/example-project/releases).

While some of these are GitHub features, it all can be done on other sites, or
by yourself without GitHub at all.
