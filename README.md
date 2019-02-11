

# [Version control with Git for a single developer](https://coderefinery.github.io/git-solo/)

- [Credit and license](https://coderefinery.github.io/git-solo/license/)


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
