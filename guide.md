---
layout: default
permalink: /guide/
---

# Instructor guide


## Optional sections

For a complete beginner exposed to version control the half day schedule is too
dense. The sections "Using the Git staging area" and "Git under the hood" can
be skipped if time is tight. "Using the Git staging area" can also be given as
a homework assignment.  The short section "Remotes and GitHub" is here because
we are exposed to GitHub in another lesson on the same afternoon. Otherwise it
can be skipped or moved to another module.


## Create a cheatsheet on the board

Create a "cheatsheet" on the board as you go (possibly similar to the online
visual git cheatsheet - I referred to this). After each command is introduced,
write it on the board. After each module, make sure you haven't forgotten
anything. Re-create and expand in future git lessons. We should try to make a
cheatsheet based on our git lessons, too.

You can get inspired by http://www.ndpsoftware.com/git-cheatsheet.html but
make clear there are far, far more commands on this one than
participants need to know, and it's probably too confusing to be useful at the
basic level.


## Repeat the following points

- Once you `git add` something, it's almost impossible to lose it.
- Always check `git status`, `git diff`, and `git graph` (our alias) before and
  after every command until you get used to things. These give you a clear view
  into what is going on, the key to knowing what you are doing. Also that `git graph`
  is a direct representation of what I am drawing on the board.


## Start from identical environment

Reminder to move .gitconfig and possibly .bashrc away before you start.
Environment should be identical to that which students have.
