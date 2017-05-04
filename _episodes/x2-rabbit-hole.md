---
layout: episode
title: "Down the rabbit hole"
teaching: x min
exercises: y min
#questions:
#  - "How do I rename files in a git repository?"
#  - "How do I restructure my project?"
#objectives:
#  - "Student can restructure a project when the need arises"
#keypoints:
#  - "Remember to use **git rm** and **git mv** instead of the normal ones."
---

## Down the rabbit hole

Now that we've made a couple of commits let's look at what's happening under
the hood.

```
$ cd .git
$ ls
COMMIT_EDITMSG  description info        refs
HEAD        hooks       logs
config      index       objects
```

Git stores everything under the .git folder in your repository. In fact, **the
.git directory is the git repository.**

Previously when you wrote the commit messages using your text editor, they
were in fact saved to COMMIT_EDITMSG.

Look at the file HEAD, it contains a reference to the file refs/heads/master.
Check the content of that file. It contains an SHA-1 hash (a
40-characther hexadecimal string). An object corresponding to that character
string (called a blob) can be found under

Each commit in git is stored as a blob. This blob contains information about
the author and the commit message.  The blob references another blob that lists
the files present in the directory at the time and references blobs that record
the state of each file.

*Image CC BY 3.0 from the Pro Git book.*

![A commit inside git]({{ site.baseurl }}/img/commit-and-tree.png "States of a git file. License CC BY 3.0"){:class="img-responsive"}


Once you have several commits, each commit blob also links to the hash of the
previous commit. Up until now these commits have created a list but in the
next lessons they will create a [directed acyclic
graph](http://eagain.net/articles/git-for-computer-scientists/) (don't worry
if the term is not familiar).

*Image CC BY 3.0 from the Pro Git book.*

![A commit and it's parents]({{ site.baseurl }}/img/commits-and-parents.png "Commit and it's parents License CC BY 3.0"){:class="img-responsive"}

All branches and tags in Git are simply pointers to a commit. Basic branching and
merging is the topic of our next lesson.
