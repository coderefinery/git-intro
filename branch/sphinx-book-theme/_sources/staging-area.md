# Using the Git staging area

```{objectives}
- Learn how to tell a story with your commit history.
- Demystify the Git staging area.
```

```{instructor-note}
- 10 min teaching/type-along
- 10 min exercise
```


## Commit history is telling a story

Your *current code* is very important, but the *history* can be just
as important - it tells a story about how your code came to be.

- Each individual line of code rarely stands alone.
- You often want to see all the related changes together.
- But you also hardly ever do one thing at once.

Along with your code, Git creates a *history* for you, and if your
history is clear then you are a long way to organized code.

````{discussion}
  Here are five types of history.  What are the advantages and
  disadvantages of each, when you look at it later?

  **Example 1**:
  ```shell
  b135ec8 add features A, B, and C
  ```

  **Example 2** (newest commit is on top):
  ```shell
  6f0d49f implement feature C
  fee1807 implement feature B
  6fe2f23 implement feature A
  ```

  **Example 3**:
  ```shell
  ab990f4 saving three months of miscellaneous work I forgot to commit
  ```

  **Example 4** (newest commit is on top):
  ```shell
  bf39f9d more work on feature B
  45831a5 removing debug prints for feature A and add new file
  bddb280 more work on feature B and make feature A compile again
  72d78e7 feature A did not work and started work on feature B
  b135ec8 now feature A should work
  72e0211 another fix to make it compile
  61dd3a3 forgot file and bugfix
  49dc419 wip (work in progress)
  ```

  **Example 5** (newest commit is on top):
  ```shell
  1949dc4 Work of 2020-04-07
  a361dd3 Work of 2020-04-06
  1172e02 Work of 2020-04-03
  e772d78 Work of 2020-04-02
  ```

  Discuss these examples. Can you anticipate problems?
````

We want to have nice commits.  But we also want to "save often"
(checkpointing) - how can we have both?

- We will now learn to create nice commits using `git commit --patch` and/or the staging area.
- Staging addresses the issue of having unrelated changes in the same
commit or having one logical change spread over several commits.
- The staging area isn't the only way to organize your history nicely, some alternatives are discussed at the end of the lesson.


## Interactive commits

- The simplest ways to solve this is to do **interactive commits**:
  the `git commit --patch` option (or `git commit -p` for short).
- It will present you with every change you have made individually,
  and you can decide which ones to commit right now.
- Reference and key commands
  - `git commit --patch` to start the interactive commit
  - `y` to use the change
  - `n` to skip the change
  - `s` (split) if there are several changes grouped together, but
    separated by a blank line, split them into separate choices.
  - `q` aborts everything.
  - `?` for more options.
- The `-p` option is also available on `commit`, `checkout`, `reset`, and `add`.


(exercise-interactive-commits)=

## Exercise: Interactive commits

````{exercise} Staging-1: Perform an interactive commit
One option to help us create nice logical commits is to stage *interactively*
with `git commit --patch`:

1. Make two changes in `instructions.txt`, at the top and bottom
   of the file.
   **Make sure that they are separated by at least several unmodified lines.**
2. Run `git commit --patch`.  Using the keystrokes above, commit one of
   the changes.
3. Do it again for the other change.
4. When you're done, inspect the situation with `git log`, `git status`, `git diff` and `git diff --staged`.
5. When would this be useful?

  ```{solution}
  This can be useful if you have several modification in a file (or several
  files) but you decide that it would be beneficial to save them as two (or
  more) separate commits.
  ```
````


## The staging area

- The interactive commits above are great, but what if there are so
  many changes that you can't sort them out in one shot?
- What if you make progress and want to record it somehow, but it's
  not ready to be committed?
- The **staging area** is a place to record things before committing.

```{instructor-note}
We give two examples and the instructor can pick one or both:
- Analogy using moving boxes
- Analogy using shopping receipts
```

```{discussion}
  **Analogy using moving boxes**

  - You're moving and you have a box to pack your things in.
  - You can put stuff into the box, but you can also take stuff out of the box.
  - You wouldn't want to mix items from the bathroom, kitchen, and living room
    into the same box.
  - The box corresponds to the staging area of Git, where you can craft your commits.
  - Committing is like sealing the box and sticking a label on it.
  - You wouldn't want to label your box with "stuff", but rather give a more
    descriptive label.
  - See also <https://dev.to/sublimegeek/git-staging-area-explained-like-im-five-1anh>


  **Analogy using shopping receipts**

  - You need to go shopping and buy some stuff for work and for home.
    You need two separate receipts.
  - Bad idea: go through the store get home stuff, pay, start at the
    beginning and go through the store again.  This is inefficient and
    annoying.
  - What you actually do:
    - Go through the store and put everything you need in your shopping
      basket.
    - Get to the checkout.  Put your home stuff on the conveyor belt
      (`git add`).  Check both the belt (`git diff --staged`) and your
      basket (`git diff`) to make sure you got all your home stuff.
    - Pay (`git commit`)
    - Repeat for work stuff.

  In order to keep organized, you have to use multiple locations to
  stage things in sequence.
```


## Staging area commands

The staging area is a middle ground between what you have done to your files
(the **working directory**) and what you have last committed (the **HEAD commit**).
Just like the name implies, it lets you prepare (**stage**) what the next commit will be and most importantly give you tools to easily know what is going on.
This adds some complexity but also adds more flexibility to selectively
prepare commits since **you can modify and stage several times before committing**.

**git add** stages/prepares for the next commit:
```text
                git add
 [project*]  <------------  project*
                               ^
                               | modify with editor
                               |
  HEAD            .         project
    |             .
    |             .
    |             .
  HEAD~1          .
    |             .
    |             .
    |             .
                  .
  .git            .     working directory
(history)         .      (files we see)
```

**git commit** creates a new commit:
```text

  HEAD            .         project
    |             .
    |             .
    |             .
  HEAD~1          .
    |             .
    |             .
    |             .
  HEAD~2          .
    |             .
    |             .
    |             .
                  .
  .git            .     working directory
(history)         .      (files we see)
```

**git reset \\--soft HEAD~1** (move HEAD back by one but keep changes and stage
them) would do the opposite of **git commit**.

Going back to the last staged version:
```text
              git restore
 [project*]  ------------>  project*



  HEAD            .
    |             .
    |             .
    |             .
  HEAD~1          .
    |             .
    |             .
    |             .
                  .
  .git            .     working directory
(history)         .      (files we see)
```

Unstaging changes with **git restore \\--staged**:
```text
          git restore --staged
             ------------>  project*



  HEAD            .
    |             .
    |             .
    |             .
  HEAD~1          .
    |             .
    |             .
    |             .
                  .
  .git            .     working directory
(history)         .      (files we see)
```

Discarding unstaged changes:
```text

                            project*
                               |
                               | git restore
                               v
  HEAD            .         project
    |             .
    |             .
    |             .
  HEAD~1          .
    |             .
    |             .
    |             .
                  .
  .git            .     working directory
(history)         .      (files we see)
```

Comparing:
```text
                git diff
 [project*]  <----------->  project*
    ^                          ^
    | git diff --staged        | git diff HEAD
    v                          v
  HEAD            .
    |             .
    |             .
    |             .
  HEAD~1          .
    |             .
    |             .
    |             .
                  .
  .git            .     working directory
(history)         .      (files we see)
```

```{figure} img/staging-basics.svg
:alt: Staging basics
:width: 100%

The different states of the repository and the commands to move from one to
another.
```

(exercise-staging-area)=

## Exercise: Using the staging area

```{exercise} Staging-2: Use the staging area to make a commit in two steps
1. In your recipe example, make two different changes to
  `ingredients.txt` and `instructions.txt` which do not go together.
2. Use `git add` to stage one of the changes.
3. Use `git status` to see what's going on, and use `git diff` and `git diff --staged` to see the changes.
4. Feel some regret and unstage the staged change.
```

```{discussion}
- When is it better to "save" a change as commit, when is it better to "save"
  it with `git add`?
- Is it a problem to commit many small changes?
```

```{keypoints}
- The staging area helps us to create well-defined commits.
```
