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

---

## List of aliases the instructors use

You are welcome to reuse, suggest, improve.

Common aliases:

```
$ git config --global alias.br branch
$ git config --global alias.ci "commit -v"
$ git config --global alias.co checkout
$ git config --global alias.di diff
$ git config --global alias.dic diff --cached --color-words
$ git config --global alias.diw "diff --color-words"
$ git config --global alias.dis "!git --no-pager diff --stat"
$ git config --global alias.fe fetch
$ git config --global alias.graph "log --all --graph --decorate --oneline"
$ git config --global alias.rem remote
$ git config --global alias.st status
$ git config --global alias.ap "add --patch"
$ git config --global alias.cip "commit --patch -v"
$ git config --global alias.cop "checkout --patch"
$ git config --global alias.cl "clone --recursive"
$ git config --global alias.su "submodule update --init --recursive"
```

Other aliases that may be too advanced, but you might want to know what is possible.

```
$ git config --global alias.cif "commit -v -p --fixup"

$ git config --global alias.rb "rebase --autosquash"
$ git config --global alias.rbi "rebase --interactive --autosquash"
$ git config --global alias.rbis "rebase --interactive --autosquash --autostash"
$ git config --global alias.rbs "rebase --autosquash --autostash"
$ git config --global alias.rec "!git --no-pager log --oneline --graph --decorate @{upstream}^^^..HEAD"
$ git config --global alias.ls-ignored "ls-files -o -i --exclude-standard"

$ git config --global alias.new "log HEAD..HEAD@{upstream}"
$ git config --global alias.news "log --stat HEAD..HEAD@{upstream}"
$ git config --global alias.newd "log --patch --color-words HEAD..HEAD@{upstream}"
$ git config --global alias.newdi "diff --color-words HEAD...HEAD@{upstream}"

$ git config --global alias.rec "!git --no-pager log --oneline --graph --decorate @{upstream}^^^..HEAD"
$ git config --global alias.reca "!git --no-pager log --oneline --graph --decorate -n10 --all"
$ git config --global alias.recd "log --decorate --patch @{upstream}^^^..HEAD"
$ git config --global alias.recs "!git --no-pager log --oneline --graph --decorate @{upstream}^^^..HEAD --stat"
```
