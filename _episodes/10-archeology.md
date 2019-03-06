---
layout: episode
title: "Inspecting history"
teaching: 15
exercises: 20
questions:
  - How can we find out who introduced a line of code and when exactly?
  - How can we find out which commit broke or changed a functionality?
objectives:
  - Quickly find a line of code, find out who introduced it, when, and why.
  - Quickly find the commit that changed a behavior.
keypoints:
  - "`git log/grep/blame/show/bisect` is a powerful combination when doing archaeology in a project."
  - "`git checkout -b <name> <hash>` is the recommended mechanism to inspect old code"
---

Clone the repository of `git` itself from [here](https://github.com/git/git).

## Inspecting commits

At any moment we can inspect individual commits with `git show`:

```
$ git show e83c51633

commit e83c5163316f89bfbde7d9ab23ca2e25604af290
Author: Linus Torvalds <torvalds@ppc970.osdl.org>
Date:   Thu Apr 7 15:13:13 2005 -0700

    Initial revision of "git", the information manager from hell

...
diff --git a/README b/README
new file mode 100644
index 000000000..27577f768
--- /dev/null
+++ b/README
@@ -0,0 +1,168 @@
+
+       GIT - the stupid content tracker
+
+"git" can mean anything, depending on your mood.
+
+ - random three-letter combination that is pronounceable, and not
+   actually used by any common UNIX command.  The fact that it is a
+   mispronounciation of "get" may or may not be relevant.
+ - stupid. contemptible and despicable. simple. Take your pick from the
+   dictionary of slang.
+ - "global information tracker": you're in a good mood, and it actually
+   works for you. Angels sing, and a light suddenly fills the room.
+ - "goddamn idiotic truckload of sh*t": when it breaks
+
+This is a stupid (but extremely fast) directory content manager.  It
+doesn't do a whole lot, but what it _does_ do is track directory
+contents efficiently.
...
```

We see that the start of the hash is enough if it is unique.

Compare this with: [https://github.com/git/git/commit/e83c51633](https://github.com/git/git/commit/e83c51633)

---

## Grepping code

What if the combination of `git log` and `git show` is not enough?

```
$ git grep -i indexing

Documentation/config/add.txt:   added due to indexing errors. Equivalent to the `--ignore-errors`
Documentation/git-add.txt:      If some files could not be added because of errors indexing
Documentation/git-clone.txt:branch of some repository for search indexing.
builtin/index-pack.c:                           from_stdin ? _("Receiving objects") : _("Indexing objects"),
compat/nedmalloc/malloc.c.h:/* ---------------------------- Indexing Bins ---------------------------- */
compat/nedmalloc/nedmalloc.c:   if(bestsize!=size)      /* dlmalloc can round up, so we round down to preserve indexing */
diff-delta.c:   /* Determine index hash size.  Note that indexing skips the
hash.h: * Note that these constants are suitable for indexing the hash_algos array and
po/bg.po:msgid "read error while indexing %s"
po/bg.po:msgid "short read while indexing %s"
po/bg.po:msgid "Indexing objects"

```

- Greps entire repository below current directory.
- Super fast. Sometimes it is worth creating a Git repository just for one `git grep`.

---

## Finding out who introduced a modification and when

- `git blame` is a fun and useful command to find out when a specific line got introduced and by whom.
- This is important to judge the impact of a bug:
  - When was it introduced?
  - For how long has this bug been around?
  - Has this bug been released?
  - Has this buggy code been used by others?
  - Who introduced it? Not to blame people but to possibly get more information.

```shell
$ git blame <filename>
```

Example from real life:

```
$ git blame blame.c

072bf4321f (Jeff Smith              2017-05-24 00:15:34 -0500    1) #include "cache.h"
072bf4321f (Jeff Smith              2017-05-24 00:15:34 -0500    2) #include "refs.h"
cbd53a2193 (Stefan Beller           2018-05-15 16:42:15 -0700    3) #include "object-store.h"
072bf4321f (Jeff Smith              2017-05-24 00:15:34 -0500    4) #include "cache-tree.h"
b543bb1cdf (Jeff Smith              2017-05-24 00:15:35 -0500    5) #include "mergesort.h"
b543bb1cdf (Jeff Smith              2017-05-24 00:15:35 -0500    6) #include "diff.h"
b543bb1cdf (Jeff Smith              2017-05-24 00:15:35 -0500    7) #include "diffcore.h"
09002f1b31 (Jeff Smith              2017-05-24 00:15:36 -0500    8) #include "tag.h"
f5dd754c36 (Jeff Smith              2017-05-24 00:15:33 -0500    9) #include "blame.h"
14ba97f81c (Stefan Beller           2018-05-15 14:48:42 -0700   10) #include "alloc.h"
4e0df4e663 (Nguyễn Thái Ngọc Duy    2018-05-19 07:28:19 +0200   11) #include "commit-slab.h"
4e0df4e663 (Nguyễn Thái Ngọc Duy    2018-05-19 07:28:19 +0200   12)
4e0df4e663 (Nguyễn Thái Ngọc Duy    2018-05-19 07:28:19 +0200   13) define_commit_slab(blame_suspects, struct blame_origin *);
4e0df4e663 (Nguyễn Thái Ngọc Duy    2018-05-19 07:28:19 +0200   14) static struct blame_suspects blame_suspects;
4e0df4e663 (Nguyễn Thái Ngọc Duy    2018-05-19 07:28:19 +0200   15)
4e0df4e663 (Nguyễn Thái Ngọc Duy    2018-05-19 07:28:19 +0200   16) struct blame_origin *get_blame_suspects(struct commit *commit)
```

Rather typical timeline:

> *"Who the %&!@!!! wrote this crap?!? Oh, it was me."*

Who was the last to edit a specific line of the source file for `git blame` and when and why?

- [https://github.com/git/git/blame/master/blame.c](https://github.com/git/git/blame/master/blame.c)

---

## Grepping commit messages

- Another possible scenario is that you're looking for a particular commit, but can't
easily find it with `git blame`.
- You can however remember (or guess) some keywords from the commit message
- Commit messages can also be grepped!

Real-life example:
```
$ git log --oneline --grep "removed"

9a4cb8781 builtin/notes: remove unnecessary free
d1664e73a add: speed up cmd_add() by utilizing read_cache_preload()
bf1e6da79 compat: make sure git_mmap is not expected to write
2588f6ed8 shallow: offer to prune only non-existing entries
1dcd9f204 midx: close multi-pack-index on repack
```

Note that `git log --grep` will grep the whole commit message even if you use the `--oneline` option.

---

## Finding removed code

The day will come when you are in this situation:

> *I remember there used to be a line containing the word "the_repository".
> Now it is gone:*

```
$ git grep "the_repository" grep.c

[no output]
```
(You can also grep all files at once: `git grep "the_repository"`)

Sometimes also the log does not help because the commit messages are not helpful:

```
$ git log --oneline grep.c

4002e87cb grep: remove #ifdef NO_PTHREADS
acd00ea04 userdiff.c: remove implicit dependency on the_index
38bbc2ea3 grep.c: remove implicit dependency on the_index
6afaf8078 diff.c: remove the_index dependency in textconv() functions
87ece7ce1 Merge branch 'tb/grep-only-matching'
d036d667b Merge branch 'tb/grep-column'
00624d608 Merge branch 'sb/object-store-grafts'
...
```

What now?

We can figure out when it disappeared:

```
$ git log -S 'the_repository' grep.c

commit 38bbc2ea39372ce1b7eb494b31948f4a8a903f88
Author: Nguyễn Thái Ngọc Duy <pclouds@gmail.com>
Date:   Fri Sep 21 17:57:23 2018 +0200

    grep.c: remove implicit dependency on the_index
...
commit 6afaf807859bd671a3f8e9101952e648a1a5e1a9
Author: Nguyễn Thái Ngọc Duy <pclouds@gmail.com>
Date:   Fri Sep 21 17:57:22 2018 +0200

    diff.c: remove the_index dependency in textconv() functions
...
```

Now let us have a look at that commit:

```
$ git show 38bbc2e grep.c

commit 38bbc2ea39372ce1b7eb494b31948f4a8a903f88
Author: Nguyễn Thái Ngọc Duy <pclouds@gmail.com>
Date:   Fri Sep 21 17:57:23 2018 +0200

    grep.c: remove implicit dependency on the_index
...

diff --git a/grep.c b/grep.c
index e146ff20b..6c0eede3a 100644
--- a/grep.c
+++ b/grep.c
...
@@ -1741,7 +1744,7 @@ static int fill_textconv_grep(struct userdiff_driver *driver,
         * structure.
         */
        grep_read_lock();
-       size = fill_textconv(the_repository, driver, df, &buf);
+       size = fill_textconv(r, driver, df, &buf);
        grep_read_unlock();
        free_filespec(df);
```

Indeed! Thank you, Git!

---

## Finding a developer to talk to (large projects)

Example: you want to know who implemented a specific keyword/functionality.

- `git grep` for the keyword or screen message.
- Then with `git blame` find the person/commit that introduced it.
- With `git show` verify the commit that introduced the change.

---

## Going back in time

We do not have to branch from the tip of the branch (HEAD).
We can branch from arbitrary (earlier) hash:

```shell
$ git checkout -b <name> <hash>
```

This is the recommended mechanism to inspect old code (example: hash *abc123*):

```shell
$ git checkout -b museum abc123  # create branch called "museum" from hash abc123
  # do some archaeology ...
  # "What was I thinking back then!?"
  # "Aha! Hmm."
$ git checkout master            # after you are done switch back to "master"
$ git branch -d museum
```

Branches help us to keep the repository organized.

---

## Finding out when something broke

> *But I am sure it used to work! Strange.*

- Sometimes you realize that something broke.
- You know that it used to work.
- You do not know when it broke.
- First find out a commit in past when it worked.
- Then bisect your way until you find the commit that broke it.

```shell
$ git bisect start
$ git bisect good 89578ed  # this is a commit that worked
$ git bisect bad HEAD      # last commit is broken
  # now compile and/or run
  # after that decide whether
$ git bisect good
  # or
$ git bisect bad
  # now compile and/or run
  # after that decide whether
$ git bisect good
  # or
$ git bisect bad
  # iterate until commit is found
```

- This can even be automatized with `git bisect run <script>`.
- For this you write a script that returns zero/non-zero (success/failure).

---

## Git bisect exercise

Clone or fork it from [here](https://github.com/bast/git-bisect-exercise).


### Motivation

The motivation for this exercise is to be able to do archaeology with Git on a
source code where the bug is difficult to see visually. **Finding the offending
commit is often more than half the debugging**.


### Background

The script `get_pi.py` approximates pi using terms of the Nilakantha series. It
should produce 3.14 but it does not. The script broke at some point and
produces 3.57 using the last commit:

```
$ python get_pi.py

3.57
```

At some point within the 500 first commits, an error was introduced. The only
thing we know is that the first commit worked correctly.


### Your task

Use `git bisect` to find the commit which broke the computation.


### How to find the first commit

```
$ git log --oneline | tail -n 1
```


### Bonus exercise

Write a script that checks for a correct result and use `git bisect run` to
find the offending commit automatically.
