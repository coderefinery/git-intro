

# [Introduction to version control with Git](https://coderefinery.github.io/git-intro/)

- [Credit and license](https://coderefinery.github.io/git-intro/license/)

This is the introductory lesson to version control using Git. It is
assumed to be the very first thing done in a course.


## For future users

This lesson has been designed so that the first 45 minutes are spent on
learning to make commits. After that the idea is to take baby steps to make
more complex arrangement.

The goals of the module as a whole are that the user will feel comfortable
about staging changes, committing them, merging and branching. Additionally
they should have some rudimentary understanding about remotes and a few best
practices like micro-commits and .gitignore files.


## Local development

The following Gemfile will permit you to run jekyll locally

```
source 'https://rubygems.org'
gem 'github-pages', group: :jekyll_plugins
gem 'github-linguist'
gem 'rouge', '~>1.11.1'
```

Write it as Gemfile under the repository root.

```shell
$ export GEM_HOME=$HOME/.gem
$ export PATH=$PATH:$HOME/.gem/bin
$ bundler install
$ bundle exec jekyll serve
```
