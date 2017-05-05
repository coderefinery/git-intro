---
layout: episode
title: "Remotes and GitHub"
teaching: 10
exercises: 15
questions:
  - How does version control scale from 1 to N users per repository?
  - How can I set up a public repository online
  - How can I set up a local repository for my computer?
objectives:
  - "Student understands the concept of remotes"
  - "Student can add an initialized repository to GitHub"
  - "Student can create a bare repository on a local machine"
keypoints:
  - "A repository can have one or multiple remotes"
  - "Local branches often track remote branches"
---

## Food for thought
- Who maintains the server that synchronizes all the changes?
- What happens if two or more people change the same things at the same time?
- How could a limited number of people work on a feature without bothering
  others about it just yet?
---



## Remotes

As we have seen the git repository is in fact a directory on your computer,
found under ".git". The files in the repository directory are a checked out
copy of the state you are currently working on. The state can be a loose
commit in detached HEAD mode or the head (or some other commit) in a branch.

It should not come as a surprise that as everything in git is stored in blobs
in a directory then synchronizing changes is about synchronizing those files.


## GitHub

GitHub is a for-profit service that hosts remote git repositories for you. It
offers a nice HTML user interface to browse the repositories and handles many
things very nicely.

It is free for public projects and hosting private projects costs a monthly
fee. The free part of the service has made it very popular with many open
source providers.

> ## Alternatives exist
>
> CodeRefinery does not in any way endorse the use if GitHub. There are many
> commercial alternatives such as [GitLab](https://about.gitlab.com/),
>
{: .callout :}



### Set up GitHub account

By now you should already have set up a GitHub account but if you haven't,
please do so [here](https://github.com/join).


# Introduction to Git example project

This repository was created during the [introduction to
git](https://coderefinery.github.io/git-intro/) session at a
[CodeRefinery](http://coderefinery.org/) Workshop.

## Subsection


### Clone the repository from GitHub

A typical workflow starts with cloning a repository from GitHub.

As you have already noticed you can have multiple instances of the same
repository on your filesystem in different directories.

> ## Clone your repository
As an exercise we have created a repository for today's course and first we will add all participants as collaborators.
Repository location : https://github.com/Sabryr/coderefinery_git_intro2.git
>Get a copy locally

```
git clone --origin github https://github.com/Sabryr/coderefinery_git_intro2.git
```
Check your remotes
```
git remote -v
```
Create a branch
```
git branch user_additions
```
```
git checkout user_additions
```
Add your name and your git knowledge according to the comments provided on the file and
Commit your changes
```
git add git_competence.txt
```
```
git commit -m “Added new user to ..."
```
Check whether anyone else has made any changes while you were working locally
```
git fetch github
```
```
git diff user_additions..github/user_additions
```
Sync with the server with the corresponding branch(github in this case)
```
git config --global push.default matching
```
```
git push github user_additions
```
You might get a conflict if a colleague has pushed something while you were working
and you did not ferch that.
```
 ! [rejected]        user_additions -> user_additions (fetch first)
error: failed to push some refs to 'https://github.com/Sabryr/coderefinery_git_intro2.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

Then you need to resolve the conflict
```
git diff user_additions..github/user_additions
```
```
git fetch
```
```
git diff user_additions..github/user_additions
```
Make sure you are on the correct branch
```
git branch
```
```
git merge github/user_additions
```
Resolve the conflicts manually. That is to keep what you want to be permanent. Git gives you guidelines on what each versions are differing in.
Add and commit your changes

Push it again
```
git push github user_additions
```
If again if you encounter a conflict, follow the above procedure until you get out of it. You could use method of communication when working with central repositories, like a chat client.



>An alternative to this procedure and a more systematic one would be to fork the above repository, make and commit your changes, then request a pull request.
>We shall take about this and show an example and everyone could follow if we have time.
{: .task :}

#### Adding a README

It's always a good convention to add a README. GitHub supports many formats for
the README but we recommend MarkDown for easy entry at first.

Below is an example but feel free to expand on it.

```
Say something about the project here.

```

> ## Add the README
> Add the README to the root of the repository, commit the change and push it
> to GitHub
{: .task :}


### Creating a new repository

Now find the "New Repository" button and click it or go through
[here](https://github.com/new). Name the repository
coderefinery-git-example. Do _not_ initialize it with a readme or anything.

The next page will give you simple instructions. You just have to remember to choose the **SSH** version of the repository URL and not the HTTPS version GitHub gives by default.

```
$ git remote add origin git@github.com:jexample/coderefinery-git-example.git
$ git push -u origin master
Counting objects: 36, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (34/34), done.
Writing objects: 100% (36/36), 3.75 KiB | 0 bytes/s, done.
Total 36 (delta 9), reused 0 (delta 0)
remote: Resolving deltas: 100% (9/9), done.
To git@github.com:jexample/coderefinery-git-example.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
```

Now refresh the page in your browser you should see a HTML user interface that
shows the contents of your repository. Feel free to explore the things that can
be found there.


### Bare repositories

The checked out copy of some state in the repository is not at all needed. If
there is no working copy the repository is called *bare*. It is a common
convention to name such directories with a name that ends in .git.

Inside your test repository do the following, remembering to substitute the
path with one from your computer.

```
$ cd ..
$ git init --bare testrepo.git
Initialized empty Git repository in /Users/jexample/devel/testrepo.git/
$ cd testrepo
$ git remote add localbare /Users/jexample/devel/testrepo.git/
```

Now git knows that there is another repository on the same machine that is
referenced by the name localbare. In the good old Unix mainframe days this
would have been sufficient. You could have set up a group, set the right group
write permissions to that repository and you would have been set to
collaborate.

Git is quite smart about communication
protocols. The simplest example is a folder on the local computer, but git can
just as easily do things over an SSH connection on a remote machine or even
HTTP (not recommended) or HTTPS using basic authentication. We'll get to that
in a bit.

Once we have a remote repository what we can do is push certain branches to
the remote repository.

```
$ git checkout master
$ git push --set-upstream localbare master
Counting objects: 33, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (31/31), done.
Writing objects: 100% (33/33), 3.41 KiB | 0 bytes/s, done.
Total 33 (delta 8), reused 0 (delta 0)
To /Users/suvileht/devel/testrepo.git/
 * [new branch]      master -> master
 Branch master set up to track remote branch master from localbare.
```

Now we pushed the master branch to the empty repository and all the project
states associated with that branch.

### Hands-on

> ## Make a Change
> Change something in testrepo and commit the change to a new branch that you
> call "my_feature".
>
> (If you're out of ideas you can add a comment. Those begin with #)
{: .task :}



> ## Note
>
> Naming conventions are important, especially when collaborating with other
> people. The local branch names and remote branch names fortunately don't have
> to match.
{: .callout :}

To push your branch to the remote you can pass the name of both the local name
and you want to the branch to have.

```
$ git push --set-upstream localbare my_feature:joes_feature
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 354 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
To /Users/jexample/devel/testrepo.git/
 * [new branch]      my_feature -> joes_feature
 Branch my_feature set up to track remote branch joes_feature
 from localbare.
```

You can check what it looks like in the bare repository

```
$ (cd ../testrepo.git && git branch)
  joes_feature
  * master
$ git branch
  change_hello
  master
* my_feature
```

Now have a look at where git stored these configurations

```
$ cat .git/config
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[user]
	name = Joe Example
	email = joe@example.org
[remote "localbare"]
	url = /Users/jexample/devel/testrepo.git/
	fetch = +refs/heads/*:refs/remotes/localbare/*
[branch "master"]
	remote = localbare
	merge = refs/heads/master
[branch "my_feature"]
	remote = localbare
	merge = refs/heads/joes_feature
```

Git has stored information about which branches locally correspond to which
remote branches. It also keeps track of the state of local and remote branches
and tags.

```
$ find .git/refs/
.git/refs/
.git/refs//heads
.git/refs//heads/change_hello
.git/refs//heads/master
.git/refs//heads/my_feature
.git/refs//remotes
.git/refs//remotes/localbare
.git/refs//remotes/localbare/joes_feature
.git/refs//remotes/localbare/master
.git/refs//tags
.git/refs//tags/0.1.0
```

### Cloning

Now it's time to pretend we're another user using the same repository. For the
sake of simplicity let's not stray from the example we have created.

The command **git clone** clones a repository.

In your testrepo run the following

```
$ cd ..
$ git clone  /Users/jexample/devel/testrepo.git/ altrepo
$ cd altrepo
$ git log
```

And voilà! You have a clone of the repository in another directory.

Go ahead and make a change to the master branch and commit it. Once you have
made your commit you can **git push** the change to remote repository.

```
$ git push
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 391 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
To /Users/jexample/devel/testrepo.git/
   dc39fc3..f478420  master -> master
```

> ## Note
>
> Pushing to the master branch is not always a good strategy. It may work if
> you're working alone on a project but Better strategies for teams will be
> covered in collaborative git.
{: .callout :}


Now you're in a state where the old testrepo master branch is behind the master
in testrepo.git.

```
$ cd ../testrepo/
$ git status
On branch master
Your branch is up-to-date with 'localbare/master'.
nothing to commit, working tree clean
```

The git repository in testrepo is not yet aware of the changes in the remote
repository. Running **git fetch** will retrieve the objects associated with the
tracked branches from the remote repository.

```
$ git fetch
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0)
Unpacking objects: 100% (3/3), done.
From /Users/jexample/devel/testrepo
   dc39fc3..f478420  master     -> localbare/master
```

Now you can check again the status of the branch.

```
$ git status
On branch master
Your branch is behind 'localbare/master' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)
nothing to commit, working tree clean
```

Now the repository has the change from the remote and git is telling you that
there are more commits and they can be fast-forwarded. It even recommends the
correct command, i.e. *git pull* for updating the local branch.

```
$ git pull
Updating dc39fc3..f478420
Fast-forward
 hello.py | 1 +
 1 file changed, 1 insertion(+)
$ git log
```

And you should see the change you made in the other clone of the repository.


