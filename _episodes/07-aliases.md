---
layout: episode
title: Aliases
teaching: 15
exercises: 0
questions:
  - How can I remember all these Git command options?
objectives:
  - Learn to use aliases for most common commands.
keypoints:
  - If you are frustrated about remembering a command, you should create an alias.
---

## What was that command again?

- Git can do many things for you if you just know the right command.
- The right command may not be intuitive and it may require multiple handles.
- If you like a command you are likely to want to use it repeatedly.

---

## Aliases

- Aliases are a simple way to improve the usability of Git.
- Aliases are based on simple string replacement in the command.
- Aliases can either be specific to a repository or global.
  - Global aliases help you do the things you are used to across Git projects.
  - Per-project aliases can also be created.


### Global aliases

A very useful shortcut which we will use a lot today:

```shell
$ git config --global alias.graph "log --all --graph --decorate --oneline"
$ cd your_git_repository
$ git graph
```

Global aliases are stored in `~/.gitconfig`.


### Using external commands

It is possible to call external commands using the exclamation mark character "!".
In this case we create a local alias which is
stored in `.git/config` and not synchronized with remotes:

```shell
$ cd your_git_repository
$ git config alias.hi '!echo hello'
$ git hi
```

---

## Food for thought: when to alias?

- How many times should you wait before aliasing a command?
- Do you believe a list of generic two-letter acronyms for common commands will
  save your time?
