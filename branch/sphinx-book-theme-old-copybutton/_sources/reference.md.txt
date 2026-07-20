# Quick reference

## Other cheatsheets

* [Interactive git cheatsheet](http://www.ndpsoftware.com/git-cheatsheet.html)
* [Very detailed 2-page git
  cheatsheet](https://aaltoscicomp.github.io/cheatsheets/git-for-normal-people-cheatsheet_1.0.pdf)


## Glossary

* **working directory/ workspace**: the actual files you see and edit
* **staging area**: Place files go after `git add` and before `git
  commit`
* **hash**: unique reference of any commit or state
* **branch**: One line of work.  Different branches can exist at the
  same time and split/merge.
* **HEAD**: Pointer to the most recent commit on the current branch.
* **remote**: Roughly, another server that holds .git.
* **origin**: Default name for a remote repository.
* **master**: Default name for main branch. Depending on the configuration and service,
              the default branch is sometimes **main**.


## Commands we use

Setup:

* `git config`: edit configuration options
* `git init`: create new repository

See our status:

* `git status`: see status of files - use often!
* `git log`: see history of commits and their messages, newest first
* `git graph`: see a detailed graph of commits.  Create this command
  with `git config --global alias.graph "log --all --graph --decorate --oneline"`
* `git diff`: show difference between working directory and last commit
* `git diff --staged`: show difference between staging area and last commit
* `git show <commit>`: inspect individual commits

General work:

* `git add`:
  - Add a new file
  - Add a file to staging
* `git commit`: record a version, add it to current branch
* `git commit --amend`: amend our last commit
* `git branch`: show which branch we're on
* `git branch <name>`: create a new branch called "name"
* `git checkout <file>`: checkout last committed version of &lt;file&gt;, losing unstaged changes
* `git checkout -b <branch-name>`: create a new branch and switch to it
* `git revert abc123`: create a new commit which reverts commit abc123
* `git reset --soft abc123`: remove all commits after abc123, but keep their modifications as staged changes
* `git reset --hard abc123`: remove all commits after abc123, permanently throwing away their changes
* `git merge <branch-name>`: merge branch &lt;branch-name&gt; into current branch
* `git grep`: search for patterns in tracked files
* `git annotate`: find out when a specific line got introduced and by whom
* `git bisect`: find a commit which broke some functionality
