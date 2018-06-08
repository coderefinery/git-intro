---
layout: episode
title: In-browser session
teaching: 25
exercises: 0
objectives:
  - See an existing repository in action.
  - Browse the history.
  - See the big picture first before we dive into details.
---

# In-browser session

- We will explore and visualize an **existing Git repository** on GitHub and make small changes to it.
- The goal of this episode is not to teach GitHub.
- We will start out with a jam session on the web (work on existing repository).
- Then we will practice scales on our local instruments (practice Git on our laptops).
- Then (tomorrow) we regroup again and play orchestra music together.

---

## Why

- Often our first contact with Git is an existing repository.
- The existing repository is often on GitHub (but this demonstration applies equally well to GitLab or Bitbucket).
- See the big picture before we focus.
- Git commands that we will learn in the following session will make more sense.

---

## Do not worry

- If you are new to Git, many concepts will be new and a bit magic, we will revisit and explain them later.
- When browsing a GitHub repository we are looking at **two layers**. Later we will explain what is in the Git layer and
  what is in the GitHub layer.

---

## Demo

We start with an
[existing repository](https://github.com/coderefinery/example-project)
that contains a couple of commits and two
branches with some easy code.

The project contains several obvious issues (bug in code,
typo in documentation, missing license file, outdated usage example).

- Explore the [repository](https://github.com/coderefinery/example-project).
- Explore the [history](https://github.com/coderefinery/example-project/commits/master).
- Browse commit changesets.
- Note that there are [branches](https://github.com/coderefinery/example-project/network).
- Find a bug in [example.py](https://github.com/coderefinery/example-project/blob/master/example.py) and use annotation to check when precisely the bug got introduced.
- Discuss the enormous value of the annotation feature.
- Identify other issues (bug in code, misleading comment, typo in documentation, missing license file, outdated usage example).
- Instructors use the browser to create a branch and make a commit to an
  existing project: Instructors will make a change concurrently, one of them
  (the presenter) will do one change on the screen. Also experienced participants
  can already join.
- Make a merge request (it's easy in browser, and shows cool stuff).
- Explore the [history](https://github.com/coderefinery/example-project/commits/master) again.
- Browse the [network](https://github.com/coderefinery/example-project/network).
- See [contributors](https://github.com/coderefinery/example-project/graphs/contributors).
- Create a [release](https://github.com/coderefinery/example-project/releases).
