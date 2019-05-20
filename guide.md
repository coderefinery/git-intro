---
layout: default
permalink: /guide/
---

# Instructor guide


## Things to prepare

In a typical workshop the optional in-browser episode is not taught.
**But if you intend to teach it:**

Mirror a fresh https://github.com/coderefinery/example-project
from https://github.com/bast/example-project.

Do not just fork it since it can confuse users sending pull requests.

## Different ways to present

The whole lesson covers why you would use git, how to use it, and
practical tips.  The earlier lessons are long, the later ones go quite
fast.

The "Basics" section is the core of how to use git, and from there
sections do just what they say.  "Basics", "Branching
and merging", and "Conflict resolution" are the shortest basics of git
(collaboration is another lesson).

"Motivation", "Basics" and "Sharing repositories online" is the
shortest path to a single-user Dropbox-like usage.

If your audience doesn't need to be taught the "how" and only the
"why", you can present sections "Motivation" and "Tips", which
should explain the high-level picture, and they should use git better,
if they already know the basics.


*Optional sections:*
For a complete beginner exposed to version control the half day schedule is too
long. These section can be skipped:

- "Using the Git staging area" can be skipped but is somewhat useful.
  It would also make a good homework or advanced assignment.

- "Git under the hood" can be skipped if time is tight - it is not
  important to typical use.

- The short section "Sharing repositories online GitHub" is here to
  give people a very simple taste of remote mirroring, and can be
  skipped we are exposed to GitHub in another lesson on the same
  afternoon. Otherwise it can be skipped or moved to another module.

- The "In-browser session" can be taught to audiences who need to be able to 
  commit to existing repositories (e.g. documentation, webpages, ...)
  but may not want to use command line.

## Conflict resolution

We use screenshots from a violent video game in the section on conflict resolution, but 
it should be emphasized that conflicts are a good thing since otherwise collaborators would 
overwrite each other's changes. Git saves us from this situation by producing conflicts.

## Inspecting history

Key lesson is *how to find when something is broken or what commit has broken the code*.

It can be useful to emphasize that it
can be really valuable to be able to search through the history of a project
efficiently to find when bugs were introduced or when something changed and
why.
Also show that `git blame` and `git show` are available
on GitHub and GitLab.

When discussing `git blame` and `git bisect` the "when" is more important than "who". It is not
to blame anybody but rather to find out whether published results are affected.

Discuss how one would find out this information without version control.

**Questions to involve participants:**

- Have you ever found a bug in your code and wondered whether it has affected published results?
- Have you ever wondered when, and by whom, a particular line of code was introduced?
- Have you ever found out that a code behaves differently than it used to but you are not sure when
  precisely this changed?


**Confusion during `git bisect` exercise:**

Learners may get stuck in the `git bisect` exercise if they incorrectly assign a commit
as *bad* or *good*.
To leave the bisect mode and return to the commit before `git bisect start` was issued,
one can do
```shell
$ git bisect reset
```
and start over if needed.


## Live better than reading the website material

It is better to demonstrate the commands live and type-along. Ideally connecting
to examples discussed earlier. 

## Log your history in a separate window

Set `PROMPT_COMMAND = "history -a"` and in another window, run `tail
-f -n 0 ~/.bash_history`  (these commands have not been checked).  Show a
few lines of the tail window at the top of the screen, above your main
shell window.  Now, the students can see your last few commands, even
if they scroll off the screen and without having to search for your
prompt.  The disadvantage is that the prompt is only written after the
command terminates.

These might work but needs debugging (there are lots of complexities
in extracting out the right parts), but will get commands as soon as
they are run and also will capture commands if you `ssh` to somewhere
else, etc.  Note: this begins working after the second line you type,
somehow.

```
script -f demos.out

# most general... prompt must end in '$ '.
tail -n 0 -f demos.out | awk '{ if (match($0,/^[^$ ]+ ?[^$ ]*[$][[:cntrl:]0-9m;[]{,10} (.*)/,m)) print m[1] }'

# Prompt format of [username@host]$
tail -n 1 -f demos.out | while read line; do [[ "$line" =~ \]\$\ ([^ ].+)$ ]] && echo  ${BASH_REMATCH[1]}; done

# Standard bash prompt of 'user@host$ ' (less likely to have false positives)
tail -n 0 -f demos.out | awk '{ if (match($0,/^[^@]+@[^$]+[$][^ ]* (.*)/,m)) print m[1] }'

# Prompt is $ ' alone on a line.
tail -n 0 -f demos.out | awk '{ if (match($0,/^[$] (.*)/,m)) print m[1] }'

# used for the fish shell (note: untested)
tail -f -n 0 ~/fish_history | sed -u -e s'/- cmd:/ \>/'
```


## Create a cheatsheet on the board

Create a "cheatsheet" on the board as you go . After each command is
introduced, write it on the board. After each module, make sure you
haven't forgotten anything. Re-create and expand in future git
lessons.  One strategy is:

- a common section for basic commands: `init`, `config``clone`, `help`, `stash`
- info commands, can be run anytime: `status`, `log`, `diff`, `graph`
- A section for all the commands that move code from different states:
  `add`, `commit`, etc.  See the visual cheat sheet below.

You can get inspired by http://www.ndpsoftware.com/git-cheatsheet.html
to make your cheatsheet, but if you show this make it clear there are
far, far more commands on there than you need to know right now., and
it's probably too confusing to use after this course.  But, the idea
of commands moving from the "working dir", "staging area", "commits",
etc is good.

Example:
![](../img/cheat-sheet.jpg)


## Draw a graph on the board

Draw the standard commit graphs on the board early on - you know, the
thing in all the diagrams.  Keep it updated all the time.  After the
first few samples, you can basically keep using the same graph the
whole lesson.  When you are introducing new commands, explain and
update the graph first, then run `git graph`, then do the command,
then look at `git graph` again.


## Repeat the following points

- Always check `git status`, `git diff`, and `git graph` (our alias) before and
  after every command until you get used to things. These give you a clear view
  into what is going on, the key to knowing what you are doing.  Even
  after you are used to things... anytime you do something you do
  infrequently, it's good to check.

- `git graph` is a direct representation of what we are drawing on the
  board and should constantly be compared to it.

- Once you `git add` something, it's almost impossible to lose it.
  This is used all the time, for example once you commit or even add
  it is hard to lose.  Commit before you merge or rebase. And so on.


## Start from identical environment

You probably have a highly optimized bash and git environment - one
that is different from students.  Move `.gitconfig` and `.bashrc` out
of the way before you start so that your environment is identical to
what students have.
