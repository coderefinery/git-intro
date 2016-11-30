# Introduction to Version Control with Git

This is the the introductory lesson to version control using Git. It is
assumed to be the very first thing done in a course.


The lesson is licensed under the [Creative Commons Attribution license (CC
BY4.0)](https://creativecommons.org/licenses/by/4.0/).

The lesson Jekyll file structure and browsing layout is inspired by and derived from
work by [Software Carpentry](http://software-carpentry.org) licensed under the
[Creative Commons Attribution license (CC BY4.0)](https://creativecommons.org/licenses/by/4.0/).
We have kept the YAML structure in the episode Markdown files for future compatibility
but have heavily cut down and modified the layout and include files.

## ToDo

* if possible bring the challenges over from software carpentry, they look cool. Are they specialized markdown, though?
* determine what other features we could use

## Local development

The following Gemfile will permit you to run jekyll locally

        source 'https://rubygems.org'
        gem 'github-pages', group: :jekyll_plugins
        gem 'github-linguist'
        gem 'rouge', '~>1.11.1'

Write it as Gemfile under the repository root. 

        $ export GEM_HOME=$HOME/.gem
        $ export PATH=$PATH:$HOME/.gem/bin
        $ bundler install
        $ bundle exec jekyll serve

