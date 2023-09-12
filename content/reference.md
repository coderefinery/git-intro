# Quick reference

## Other cheatsheets

* [Interactive git cheatsheet](http://www.ndpsoftware.com/git-cheatsheet.html)
* [Very detailed 2-page git
  cheatsheet](https://aaltoscicomp.github.io/cheatsheets/git-the-way-you-need-it-cheatsheet.pdf)


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
* **master**: Default name for main branch on Git. Depending on the configuration and service,
              the default branch is sometimes **main**.
              In this lesson we configure Git so that the default branch is
              called **main** to be more consistent with GitHub and GitLab.
* **main**: Default name for main branch on GitLab and GitHub.
            In this lesson we configure Git so that the default branch is
            called **main** to be more consistent with GitHub and GitLab.


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
* `git show COMMIT`: inspect individual commits

General work:

* `git add FILE`:
  - Add a new file
  - Add a file to staging
* `git commit`: record a version, add it to current branch
* `git commit --amend`: amend our last commit
* `git branch`: show which branch we're on
* `git branch NAME`: create a new branch called "name"
* `git restore FILE`: restore last committed/staged version of FILE, losing unstaged changes
* `git switch --create BRANCH-NAME`: create a new branch and switch to it
* `git revert HASH`: create a new commit which reverts commit HASH
* `git reset --soft HASH`: remove all commits after HASH, but keep their modifications as staged changes
* `git reset --hard HASH`: remove all commits after HASH, permanently throwing away their changes
* `git merge BRANCH-NAME`: merge branch BRANCH-NAME into current branch
* `git grep PATTERN`: search for patterns in tracked files
* `git annotate FILE`: find out when a specific line got introduced and by whom
* `git bisect`: find a commit which broke some functionality
