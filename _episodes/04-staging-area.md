---
layout: episode
title: Using the Git staging area
teaching: 10
exercises: 10
questions:
  - What should be included in a single commit?
  - What is the git staging area?  What commands use it?
objectives:
  - Learn how to tell a story with your commit history.
  - Demystify the Git staging area.
keypoints:
  - The staging area helps us to create well-defined commits.
---


## Commit history is telling a story

Your *current code* is very important, but the *history* can be just
as important - it tells a story about how your code came to be.

- Each individual line of code rarely stands alone.
- You often want to see all the related changes together.
- But you also hardly ever do one thing at once.

Along with your code, git creates a *history* for you, and if your
history is clear then you are a long way to organized code.


> ## Discussion
>
> Here are four types of history.  What are the advantages and
> disadvantages of each, when you look at it later?
>
> Example 1 (newest commit is on top):
>
> ```shell
> b135ec8 add features A, B, and C
> ```
>
> Example 2 (newest commit is on top):
>
> ```shell
> 6f0d49f implement feature C
> fee1807 implement feature B
> 6fe2f23 implement feature A
> ```
>
> Example 3 (newest commit is on top):
>
> ```shell
> ab990f4 saving three months of miscellaneous work I forgot to commit
> ```
>
> Example 4 (newest commit is on top):
>
> ```shell
> 49dc419 wip (work in progress)
> 61dd3a3 forgot file and bugfix
> 72e0211 another fix to make it compile
> 72d78e7 feature A did not work and started work on feature B
> bddb280 more work on feature B and make feature A compile again
> 45831a5 removing debug prints for feature A and add new file
> bf39f9d more work on feature B
> b135ec8 now feature A should work
> ```
>
> Example 5 (newest commit is on top):
>
> ```shell
> 1949dc4 Work of 2020-04-07
> a361dd3 Work of 2020-04-06
> 1172e02 Work of 2020-04-03
> e772d78 Work of 2020-04-02
> ```
>
> Discuss these examples. Can you anticipate problems?
{: .challenge}

We want to have nice commits.  But we also want to "save often"
(checkpointing) - how can we have both?

- We will now learn to create nice commits using `git commit -p` and/or the staging area.
- Staging addresses the issue of having unrelated changes in the same
commit or having one logical change spread over several commits.
- The staging area isn't the only way to organize your history nicely, some alternatives are discussed at the end of the lesson.


---

## Interactive committing

- The simplest ways to solve this is to do **interactive commits**:
  the `git commit -p` option.
- It will present you with every change you have made individually,
  and you can decide which ones to commit right now.
- Reference and key commands
  - `git commit -p` to start the interactive commit
  - `y` to use the change
  - `n` to skip the change
  - `s` (split) if there are several changes grouped together, but
    separated by a blank line, split them into separate choices.
  - `q` aborts everything.
  - `?` for more options.
- The `-p` option is also available on `commit`, `checkout`, `reset`, and `add`.

> ## Exercise: Interactive committing
>
> One option to help us create nice logical commits is to stage *interactively*
> with `git commit -p`:
>
> 1. Make two changes in `instructions.txt`, at the top and bottom
>    of the file.
>    **Make sure that they are separated by at least several unmodified lines.**
> 2. Run `git commit -p`.  Using the keystrokes above, commit one of
>    the changes.
> 3. Do it again for the other change.
> 4. When you're done, inspect the situation with `git log`, `git status`, `git diff` and `git diff --staged`.
> 5. When would this be useful?
>
{: .challenge}


---

## The staging area

- The interactive commits above are great, but what if there are so
  many changes that you can't sort them out in one shot?
- What if you make progress and want to record it somehow, but it's
  not ready to be committed?
- The **staging area** is a place to record things before committing.

> ## Analogies to the staging area
>
> We give two examples and the instructor can pick one or both:
> - Analogy using moving boxes
> - Analogy using shopping receipts
>
>
> ### [Analogy using moving boxes](https://dev.to/sublimegeek/git-staging-area-explained-like-im-five-1anh)
>
> <img src="{{ site.baseurl }}/img/ikea_box.jpg" width="30%">
>
> - You're moving and you have a box to pack your things in.
> - You can put stuff into the box, but you can also take stuff out of the box.
> - You wouldn't want to mix items from the bathroom, kitchen and living room into the same box.
> - The box corresponds to the staging area of Git, where you can craft your commits.
> - Committing is like sealing the box and sticking a label on it.
> - You wouldn't want to label your box with "stuff", but rather give a more descriptive label.
>
>
> ### Analogy using shopping receipts
>
> - You need to go shopping and buy some stuff for work and for home.
>   You need two separate receipts.
> - Bad idea: go through the store get home stuff, pay, start at the
>   beginning and go through the store again.  This is inefficient and
>   annoying.
> - What you actually do:
>   - Go through the store and put everything you need in your shopping
>     basket.
>   - Get to the checkout.  Put your home stuff on the conveyor belt
>     (`git add`).  Check both the belt (`git diff --staged`) and your
>     basket (`git diff`) to make sure you got all your home stuff.
>   - Pay (`git commit`)
>   - Repeat for work stuff.
>
> In order to keep organized, you have to use multiple locations to
> stage things in sequence.
{: .discussion}

---

## Staging area commands

With the **staging area**, there is one middle point before commits.

![]({{ site.baseurl }}/img/staging-basics.svg)

Files can be untracked, modified, staged, or committed, and
we have a variety of commands to go between states:

```shell
$ git add <path>       # stages all changes in file
$ git add -p <path>    # stages while letting you choose which lines to take
$ git commit           # commits the staged change
$ git diff             # see **unstaged** changes
$ git diff --staged    # see **staged** changes
$ git rm               # removes a file
$ git reset            # unstages staged changes
                       # in latest Git: git restore --staged <path>
$ git checkout <path>  # check out the latest staged version ( or committed
                       # version if file has not been staged )
                       # in latest Git: git restore <path>
```

Usage 1: you do various things at once
- You do various things at once, you want to commit them separately.
- `git add` all the parts of each change.
- `git diff` and `git diff --staged` to ensure you have all the parts.
- `git commit`.
- Repeat.

Usage 2: you want to checkpoint
- You want to save in-progress work before you make a final commit.
- `git add` every change that improves the code.
- `git checkout` every change that made things worse.
- `git commit` as soon as you have created a nice self-contained unit (not too large, not too small).
- Discuss/think about what is too large or too small.

*Note: the "staging area" has also alternatively been referred to as
the index and the cache*.

### Example workflow

```shell
$ git add file.py                 # checkpoint 1
$ git add file.py                 # checkpoint 2
$ git add another_file.py         # checkpoint 3
$ git add another_file.py         # checkpoint 4
# ... further work on another_file.py ...
$ git diff another_file.py        # diff w.r.t. checkpoint 4
$ git checkout another_file.py    # oops go back to checkpoint 4
$ git commit                      # commit everything that is staged
```

> ## Exercise: Using the staging area
>
> 1. In your recipe example, make two different changes to
>   `ingredients.txt` and `instructions.txt` which do not go together.
> 2. Use `git add` to stage one of the changes.
> 3. Use `git status` to see what's going on, and use `git diff` and `git diff --staged` to see the changes.
> 4. Feel some regret and unstage the staged change.
{: .challenge}

---

> ## Test your understanding
>
> - When is it better to "save" a change as commit, when is it better to "save" it with `git add`?
> - Is it a problem to commit many small changes?
> - What types of problems can occur in other version control systems without a staging area?
{: .challenge}
