---
layout: episode
title: Aliases and configuration
teaching: 15
exercises: 0
questions:
  - How can I remember all these Git command options?
  - Is there too much configuration?
objectives:
  - Learn to use aliases for most common commands.
keypoints:
  - If you are frustrated about remembering a command, you should create an alias.
---

Are you getting tired of typing so much?  Git can make aliases that can save you typing.

- These are great because they can save you time typing
- But it's easy to forget them, get confused, or be inconsistent with your colleagues.

There is plenty of other configuration for git, that can make it nicer.

This section

---

## Aliases

- Aliases are a simple way to improve the usability of Git: for
  example `git ci` instead of `git commit`.
- Aliases are based on simple string replacement in the command.
- Aliases can either be specific to a repository or global.
  - Global aliases help you do the things you are used to across Git projects.
  - Per-project aliases can also be created.


### Example alias

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

### Food for thought: when to alias?

- How many times should you wait before aliasing a command?
- Do you believe a list of generic two-letter acronyms for common commands will
  save your time?

---

### List of aliases the instructors use

You are welcome to reuse, suggest, improve.  If you are a beginner, we
suggest you copy and paste this into your terminal to define a bunch
of useful stuff.  Reading it (later) will help to understand what
common commands are - you can see your current aliases in `~/.gitconfig`

```shell
git config --global alias.ap "add --patch"
git config --global alias.br branch
git config --global alias.ci "commit -v"
git config --global alias.cip "commit --patch -v"
git config --global alias.cl "clone --recursive"
git config --global alias.co checkout
git config --global alias.cop "checkout --patch"
git config --global alias.di diff
git config --global alias.dic diff --cached --color-words
git config --global alias.diw "diff --color-words"
git config --global alias.dis "!git --no-pager diff --stat"
git config --global alias.fe fetch
git config --global alias.graph "log --all --graph --decorate --oneline"
git config --global alias.rem remote
git config --global alias.st status
git config --global alias.su "submodule update --init --recursive"
```

Here is what they do:
- `ap`: add, selecting parts individually, interactively.
- `br`: branch (obvious)
- `ci`: commit (check in), with `-v` option for clarity
- `cip`: commit, selecting parts individually, interactively.
- `cl`: clone, init submodules (submodules are an advanced topic)
- `co`: checkout (obvious)
- `cop`: checkout, selecting parts individually, interactively.
- `di`: diff (obvious)
- `dic`: diff of staging area vs last commit (what is about to be committed)
- `diw`: a word diff, color.  Useful for small changes.
- `dis`: a "diffstat": what files are changed, not contents
- `fe`: fetch (obvious)
- `graph`: show whole git graph (so useful, some of us call it `l`)
- `rem`: remote (obvious)
- `st`: status (obvious)
- `su`: submodule update (advanced)

`git config --global interactive.singlekey true` will be useful for
the `p` aliases.


---

## Advanced git config (advanced or home exercise)

These are advanced aliases and config options.  We won't explain them,
but if you are bored, have some time, or want to go deeper, try to
figure out what they do.  You might want to check the git manual
pages!

### Advanced aliases

```
git config --global alias.cif "commit -v -p --fixup"
git config --global alias.rb "rebase --autosquash"
git config --global alias.rbi "rebase --interactive --autosquash"
git config --global alias.rbis "rebase --interactive --autosquash --autostash"
git config --global alias.rbs "rebase --autosquash --autostash"
git config --global alias.rec "!git --no-pager log --oneline --graph --decorate @{upstream}^^^..HEAD"
git config --global alias.ls-ignored "ls-files -o -i --exclude-standard"
git config --global alias.new "log HEAD..HEAD@{upstream}"
git config --global alias.news "log --stat HEAD..HEAD@{upstream}"
git config --global alias.newd "log --patch --color-words HEAD..HEAD@{upstream}"
git config --global alias.newdi "diff --color-words HEAD...HEAD@{upstream}"
git config --global alias.rec "!git --no-pager log --oneline --graph --decorate @{upstream}^^^..HEAD"
git config --global alias.reca "!git --no-pager log --oneline --graph --decorate -n10 --all"
git config --global alias.recd "log --decorate --patch @{upstream}^^^..HEAD"
git config --global alias.recs "!git --no-pager log --oneline --graph --decorate @{upstream}^^^..HEAD --stat"
```

### Advanced git config

Besides aliases, you can do plenty of other configuration of `git`.
Here are some of the most common ones:

```shell
git config --global interactive.singlekey true
git config --global core.pager "less -RS"
git config --global core.excludesfile ~/.gitignore
git config --global merge.conflictstyle diff3
git config --global diff.wordRegex "[a-zA-Z0-9_]+|[^[:space:]]"
git config --global diff.mnemonicPrefix true
```

Do you get tired of typing and copying and pasting your remote names
all the time, like `git@github.com:myusername`?  You can create remote
aliases like this:

```shell
git config --global url.git@github.com:.insteadOf gh:
git config --global url.git@github.com:/username/.insteadOf ghu:
```

Then, when you add a remote `ghu:recipe`, it will automatically be
translated to `git@github.com:/username/recipe` using a simple prefix
matching.

### Git-aware bash prompt

You can make your shell (bash) display contextual information about
your git state even at all times.  If you are interested, find it on
[GitHub](https://github.com/jimeh/git-aware-prompt).
