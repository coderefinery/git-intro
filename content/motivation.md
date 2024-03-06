# Motivation

```{objectives}
- Make sure nobody leaves the workshop without starting to use some form of version control.
- Discuss the reasons why we advocate distributed version control.
```

```{instructor-note}
- 15 min teaching/demonstration
```


## Git is all about keeping track of changes

We will learn how to keep track of changes first in the web browser
([example repository](https://github.com/bast/runtest/commits/main/runtest/run.py)):
```{figure} img/git-log-github.png
:alt: Screenshot of a git log on GitHub
:width: 80%
:class: with-border
```
Later also using the terminal or the editor
([example repository](https://github.com/bast/runtest/commits/main/runtest/run.py)):
```{figure} img/git-log-terminal.png
:alt: Screenshot of a git log in terminal
:width: 80%
```


## Why do we need to keep track of versions?

Version control is an answer to these questions (do you recognize some of them?):

- "It broke ... hopefully I have a working version somewhere?"

- "Can you please send me the latest version?"

- "Where is the latest version?"

- "Which version are you using?"

- "Which version have the authors used in the paper I am trying to reproduce?"

- "Found a bug! Since when was it there?"

- "I am sure it used to work. When did it change?"

- "My laptop is gone. Is my thesis now gone?"


## Features: roll-back, branching, merging, collaboration

- **Roll-back**: you can always go back to a previous version and compare

- **Branching and merging**:
  - Work on different ideas at the same time
  - Different people can work on the same code/project without interfering
  - You can experiment with an idea and discard it if it turns out to be a bad idea

```{figure} img/gopher/gophers.png
:alt: Branching explained with a gopher
:width: 100%

Image created using <https://gopherize.me/>
([inspiration](https://twitter.com/jay_gee/status/703360688618536960)).
```

- **Collaboration**: review, compare, share, discuss

- [Example network graph](https://github.com/coderefinery/git-intro/network)


## Reproducibility

- How do you indicate which version of your code you have used in your paper?
- When you find a bug, how do you know **when precisely** this bug was introduced
  (Are published results affected? Do you need to inform collaborators or users of your code?).

With version control we can "annotate" code ([browse this example online](https://github.com/networkx/networkx/blame/main/networkx/algorithms/boundary.py)):

```{figure} img/git-annotate.png
:alt: Example of a git-annotated code with code and history side-by-side
:width: 100%
:class: with-border

Example of a git-annotated code with code and history side-by-side.
```


## Talking about code

Which of these two is more practical?
- "Clone the code, go to the file 'src/util.rs', and search for 'time_iso8601'".
  Oh! But make sure you use the version from August 2023."
- Or I can send you a [permalink](https://github.com/NordicHPC/sonar/blob/75daafc86582feb06299d6a47c82112f39888152/src/util.rs#L40-L44):

```{figure} img/code-portion.png
:alt: Screen-shot of a code portion
:width: 100%
:class: with-border

Permalink that points to a code portion.
```


## What we typically like to snapshot

- Software (this is how it started but Git/GitHub can track a lot more)
- Scripts
- Documents (plain text files much better suitable than Word documents)
- Manuscripts (Git is great for collaborating/sharing LaTeX or [Quarto](https://quarto.org/) manuscripts)
- Configuration files
- Website sources
- Data

````{discussion}
  In this example somebody tried to keep track of versions without a version
  control system tool like Git.  Discuss the following directory listing. What
  possible problems do you anticipate with this kind of "version control":
  ```shell
  myproject-2019.zip
  myproject-2020-February.zip
  myproject-2021-August.zip
  myproject-2023-09-19-working.zip
  myproject-2023-09-21.zip
  myproject-2023-09-21-test.zip
  myproject-2023-09-21-myversion.zip
  myproject-2023-09-21-newfeature.zip
  ...
  ```

  ```{solution}
  - Giving a version to a collaborator and merging changes later with own
    changes sounds like lots of work.
  - What if you discover a bug and want to know since when the bug existed?
  ```
````


## Difficulties of version control

Despite the benefits, let's be honest, there are some difficulties:

- One more thing to learn (it's probably worth it and will save you more time in the long run; basic career skill).
- Difficult if your collaborators don't want to use it (in the worst case, you can version control on your side and email them versions).
- Advanced things can be difficult, but basics are often enough (ask others for help when needed).


## Why Git and not another tool?

- **Easy to set up**: no server needed.
- **Very popular**: chances are high you will need to contribute to somebody else's code which is tracked with Git.
- **Distributed**: good backup, no single point of failure, you can track and
  clean-up changes offline, simplifies collaboration model for open-source
  projects.
- Important **platforms** such as [GitHub](https://github.com), [GitLab](https://gitlab.com), and [Bitbucket](https://bitbucket.org)
  build on top of Git.

However, any version control is better than no version control and it is OK to
prefer a different tool than Git such as
[Subversion](https://subversion.apache.org),
[Mercurial](https://www.mercurial-scm.org), [Pijul](https://pijul.org/), or others.
