# Instructor guide

## Why we teach this lesson

Everyone should be using a version control system for their work, even if they're working alone.
There are many version control systems out there, but Git is an industry standard and even if one uses another
system chances are high one still encounters Git repositories.

Specific motivations:
- Code easily becomes a disaster without version control
- Mistakes happen - Git offers roll-back functionality and easy backup mechanism
- One often needs to work on multiple things in parallel - branches solve that problem
- Git enables people to collaborate on code or text without stepping on each other's toes
- Reproducibility: You can specify exact versions in publications enabling others to reproduce your work,
  and if bugs are found one can find out exactly when it was introduced

Many learners in a CodeRefinery workshop have developed code for a few years. A majority have
already encountered Git and have used it to some extent, but in most cases they do not yet feel
comfortable with it. They lack a good mental model of how Git operates and are afraid of making mistakes.
Other learners have never used Git before.
This lesson teaches how things are done in Git, which is useful for the newcomers,
but also how Git operates (e.g. what commits and branches really are) and what are some good
practices (e.g. how to use the staging area), which is useful for more experienced users.


## Intended learning outcomes

By the end of this lesson, learners should:
- realize that version control is very important and Git is a valuable tool to learn and use
- understand that Git is configurable and know how to set basic configurations
- be able to set up Git repositories and make commits
- understand that information on commits, branches etc. are stored under `.git/`, and have a
  mental model of how that relates to the working directory
- have a mental model of the different stages a file can have in Git (untracked, modified, staged, unmodified)
- know how to write good commit messages
- have an idea of how the staging area can be used to craft good commits
- know how to undo commits using `git revert` and discard changes using `git checkout`
- understand that `git checkout` can be dangerous if changes have not been staged
- know how to create branches and switch between branches
- have a mental model of how branches work and get used to thinking of branches in a graphical (tree-structure) way
- know how to merge branches and understand what that means in terms of combining different modifications
- know how to resolve conflicts, or to abort conflicting merges
- realize that conflicts are generally a good thing since they prevent incorrect merges
- be able to set up a repository on GitHub and connect it with local repository
- push changes to a remote repository
- know a few ways to search through a repository and its history
- know about the different meanings of `git checkout`, and realize how they're in fact similar


## How to teach this lesson

### Take first editor steps slowly

Some participants will be new to using a terminal text editor so please open,
edit, and close the editor (Nano) slowly in first type-along sessions and
exercises to avoid that participants will fall behind the instructor. At one
point a student did not follow the file edits of the instructor, and to correct
the mistake they had to do a manual merge, which they were not ready for.


### How to use the exercises

Most episodes have standard exercises followed by optional (often more advanced) exercises
for more experienced learners so they don't get bored waiting for the newcomers.
The instructor should briefly introduce the exercises and mention that after finishing the
standard exercise (and indicating that using the green sticky) the learners can move on to the
optional ones if they wish. When at least half of the learners have raised the green sticky
the instructor should go through the standard exercise to describe its most important take-home messages.
It's also fine to briefly go though important points from the optional exercises, but don't spend
too much time on it since everyone will not have attempted them.


### "Test your understanding" exercises

Some episodes have a "test your understanding" exercise at the end which is intended as *formative assessment*,
i.e. an activity that provides feedback to instructors and learners on whether learning objectives are being met.
The instructor should end each episode by posing the "test your understanding" multiple-choice question,
giving learners a minute to think about it, and then asking for the right answer or asking learners to raise their
hands to signal which answer they think is correct.


### Inspecting history

Key lesson is *how to find when something is broken or what commit has broken
the code*.

It can be useful to emphasize that it can be really valuable to be able to
search through the history of a project efficiently to find when bugs were
introduced or when something changed and why.  Also show that `git annotate`
and `git show` are available on GitHub and GitLab.

When discussing `git annotate` and `git bisect` the "when" is more important
than "who". It is not to blame anybody but rather to find out whether published
results are affected.

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


### Live better than reading the website material

It is better to demonstrate the commands live and type-along. Ideally connecting
to examples discussed earlier.


### Log your history in a separate window

The screencasting (shell window cheatsheet) hints have been moved to
the [presenting
manual](https://coderefinery.github.io/manuals/instructor-tech-setup/).


### Create a cheatsheet on the board

For in-person workshops, create a "cheatsheet" on the board as you go. After
each command is introduced, write it on the board. After each module, make sure
you haven't forgotten anything. Re-create and expand in future git lessons.
One strategy is:

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

```{figure} img/cheat-sheet.jpg
:alt: Example cheat sheet
:width: 100%

Example cheat sheet.
```

We also recommend to draw simple diagrams up on the board (e.g.: working
directory - staging area - repository with commands to move between) and keep
them there for students to refer to.


### Draw a graph on the board

Draw the standard commit graphs on the board early on - you know, the
thing in all the diagrams.  Keep it updated all the time.  After the
first few samples, you can basically keep using the same graph the
whole lesson.  When you are introducing new commands, explain and
update the graph first, then run `git graph`, then do the command,
then look at `git graph` again.


### Repeat the following points

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


### Start from identical environment

You probably have a highly optimized bash and git environment - one
that is different from students.  Move `.gitconfig` and `.bashrc` out
of the way before you start so that your environment is identical to
what students have.
