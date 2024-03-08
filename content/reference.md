# Quick reference

## Other cheatsheets

* [Detailed 2-page Git
  cheatsheet](https://aaltoscicomp.github.io/cheatsheets/git-the-way-you-need-it-cheatsheet.pdf)
* [Interactive Git cheatsheet](http://www.ndpsoftware.com/git-cheatsheet.html)


## Glossary

:::::{glossary}

version control system
   TODO

git
   TODO

commit
   As a verb, the process of recording more changes.
   As a noun, the name of the record of changes.
   A commit is identified by something such as `554c187`.

working directory
workspace
   the actual files you see and edit

staging area
   Place files go after `git add` and before `git commit`

hash
   unique reference of any commit or state

branch
   One line of work.  Different branches can exist at the same time and split/merge.

HEAD
   Pointer to the most recent commit on the current branch.

remote
   Roughly, another server that holds .git.

origin
   Default name for a remote repository.

repository
   One collection of files managed by Git.  It contains entire history
   of all files managed by git.

clone
   As a verb, the process of making a copy of a repository locally.
   It brings in all history and all files.  (As a noun, the copy that
   was made when cloning).

GitHub repository
   The files from the Git repository, but also other things from
   GitHub such as access permissions, issues, and pull requests.

upstream
   The original repository from which the code comes.  If you
   {term}`fork` the repository, it is your upstream and it is easy to
   send changes back to there.

fork
   As a noun: a one person's copy of a repository.
   As a verb: making that copy.
   As a verb on GitHub: Making a copy of a repository linked to the
   original.  It is easy to send changes to the original

pull request
   A GitHub concept: change proposal.  A proposal to merge one branch
   into another.  Usually used to contribute code back to
   {term}`upstream`.

push
   Moving changes from your local copy to another copy

pull
   Getting changes from another copy to your own copy.  `git pull`
   does this fetch, and also tries to automatically merge.

master
   Default name for main branch on Git. Depending on the configuration and service,
   the default branch is sometimes **main**.
   In this lesson we configure Git so that the default branch is
   called **main** to be more consistent with GitHub and GitLab.

main
   Default name for main branch on GitLab and GitHub.
   In this lesson we configure Git so that the default branch is
   called **main** to be more consistent with GitHub and GitLab.

merge
merging
   Bringing changes from one branch into another, either as a noun or
   verb.

:::::

## Commands we use

Setup:

* `git config`: edit configuration options
* `git init -b main`: create new repository with `main` as the default branch

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
