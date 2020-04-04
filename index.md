---
layout: lesson
permalink: /
---

# Introduction to version control with Git

This is the introductory lesson to version control using
[Git](https://git-scm.com/). It is assumed to be the very first thing done in a
course.

Our philosophy is that we start from own local repository, branching and
merging (locally), and a brief introduction to pushing to remotes.  In the
separate [collaborative git lesson](https://coderefinery.org/lessons/), we
teach more use of remote repositories and good collaborative workflows.  We
try to stick to simple workflows, just enough for researchers who aren't
obsessed with git to be able to work well.  We try to avoid commands which
might get you into a confusing state.

Our general flow is 10 minutes on "why version control", followed by
about 45 minutes of the basics of how to make commits.  Then, there are
several small steps until we get to branching, merging, and conflict
resolution.

Investigating a past commit and going back in time are also introduced.
Great emphasis is made about the importance of not changing history of
shared repositories, when there is a need to undo commits.

Then, we see a little bit about sharing repositories online, how to
effectively dig into the history of a project,
and a few other random points before we conclude.

The goals of the module as a whole are that the user will feel comfortable
about staging changes, committing them, merging, and branching. The guacamole
example that we use is inspired by [Byron Smith](http://blog.byronjsmith.com),
for original reference, see [this
thread](https://carpentries.topicbox.com/groups/discuss/Tfe5ac909d5fb476b).
If you are teaching this lesson, see the [instructor's guide](guide)


> ## Prerequisites
>
> - A reasonably recent version of Git is installed. For installation
>   instructions see [the CodeRefinery installation instructions](https://coderefinery.github.io/installation/).
> - Being comfortable with the command line. No expertise is required, but the
>   lesson will be mostly taken from the command line.
> - Students should be familiar with using a text editor on their system. Emacs
>   and Vim are excellent choices if you know how to use them but Nano or Notepad
>   on Windows are sufficient.
> - Git should be configured prior to the lesson following
>   [our installation instructions](https://coderefinery.github.io/installation/).
> - A [GitHub](https://github.com) user account (but alternatives exist, see below).
>
>
> ### Why [GitHub](https://github.com)?
>
> In this introduction we will mention and use [GitHub](https://github.com) but also
> [GitLab](https://gitlab.com) and [Bitbucket](https://bitbucket.org) allow
> similar workflows and basically everything that we will discuss is transferable. With
> this material and these exercises we do not endorse the company
> [GitHub](https://github.com). We have chosen to demonstrate a number of
> concepts using examples with [GitHub](https://github.com) because it is
> currently the most popular web platform for hosting Git repositories and the chance is high
> that you will interact with [GitHub](https://github.com)-based repositories even if you
> choose to host your Git repository on another platform.
>
> Course participants are most welcome to use our new
> [Nordic research software repository platform](https://source.coderefinery.org) instead,
> for more information see
> [https://coderefinery.org/repository/](https://coderefinery.org/repository/).
{: .prereq}

If you are interested in the Git-aware prompt you can find it on
[GitHub](https://github.com/jimeh/git-aware-prompt).
