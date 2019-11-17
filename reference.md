---
layout: default
permalink: /reference/
---

# git-intro quick reference

## Other cheatsheets

* [Interactive git cheatsheet](http://www.ndpsoftware.com/git-cheatsheet.html)
* [Very detailed 2-page git
  cheatsheet](https://users.aalto.fi/~darstr1/cheatsheets/git-for-normal-people-cheatsheet_1.0.pdf)

## Glossary

* **Working directory/Workspace**: the actual files you see and edit
* **Staging area**: Place files go after `git add` and before `git
  commit`
* **Hash**: unique reference of any commit or state
* **Branch**: One line of work.  Different branches can exist at the
  same time and split/merge.
* **HEAD**: Pointer to the most recent commit on the current branch.
* **Remote**: Roughly, another server that holds git.
* **origin**: Default name for a remote repository.
* **master**: Default name for main branch.




## Commands we use

* **git config**: edit configuration options
* **git init**: create new repository
* **git add**:
  - Add a new file
  - Add a file to staging
* **git commit**: record a version, add it to current branch
* **git commit --amend**: amend our last commit
* **git status**: see status of files - use often!
* **git log**: see history of commits and their messages, newest first
* **git diff**: show difference between working directory and last commit
* **git diff --staged**: show difference between staging area and last commit
* **git branch**: show which branch we're on
* **git branch &lt;name&gt;**: create a new branch &lt;name&gt;
* **git checkout &lt;file&gt;**: checkout last committed version of &lt;file&gt;, losing unstaged changes
* **git checkout -b &lt;branch-name&gt;**: create a new branch and switch to it
* **git revert abc123**: create a new commit which reverts commit abc123
* **git reset --soft abc123**: remove all commits after abc123, but keep their modifications as staged changes
* **git reset --hard abc123**: remove all commits after abc123, permanently throwing away their changes
* **git merge &lt;branch-name&gt;**: merge branch &lt;branch-name&gt; into current branch
* **git grep**: search for patterns in tracked files
* **git annotate**: find out when a specific line got introduced and by whom
* **git show**: inspect individual commits
* **git bisect**: find a commit which broke some functionality
