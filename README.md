

# [Introduction to version control with Git](https://coderefinery.github.io/git-intro/)

- [Credit and license](https://coderefinery.github.io/git-intro/license/)


## Local development --Quick start

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

## Local development -- Detailed

The content here is rendered to produce a webpage using  Jekyll. Jekyll is a tool for transforming your plain text into static websites and blogs (https://jekyllrb.com/).  It is not an requirement to know Ruby or Jekyll to contribute. However, Jekyll need to be installed if you need to have a preview before pushing the changes.  


Jekyll has following requirements:

GNU/Linux, Unix, or macOS
Ruby (https://www.ruby-lang.org/) version 2.1 or above, including all development headers
RubyGems (https://rubygems.org/)
GCC and Make (in case your system doesn’t have them installed, which you can check by running gcc -v and make -v in your system’s command line interface)

The following example describe how to install and configure Jekyll on an Ubuntu 16.04.3 LTS laptop and start a preview.

### Install the dependencies
```
sudo apt-get install ruby ruby-dev make gcc g++ zlib1g-dev git
```

### Check the dependencies and a sample output
```
gcc --version  # gcc (Ubuntu/Linaro 6.3.0-18ubuntu2~16.04) 6.3.0 20170519
g++ --version # g++ (Ubuntu 5.4.1-2ubuntu1~16.04) 5.4.1 20160904
ruby --version  #ruby 2.3.1p112 (2016-04-26) [x86_64-linux-gnu]
```

### Prepare the path so the GEMs (Ruby packages)  can be installed without root privileges
```
export GEM_HOME=$HOME/.gem. 
export PATH=$PATH:$HOME/.gem/bin
```

### Install Jekyll and bundler (bundler used so that dependencies can be handles easily)
```
gem install jekyll bundler
```

### Clone the repo
```
makdir $HOME/mygit ;
git clone https://github.com/coderefinery/git-intro.git
```

### Prepare Jekyll 
```
cd $HOME/mygit/git-intro
```

### Create a file called "Gemfile" and include the following
```
source 'https://rubygems.org'
gem 'github-pages', group: :jekyll_plugins
gem 'github-linguist'
gem 'rouge', '~>1.11.1'
```

### Optional : Add the Gemfile to the .gitignore file so it will not be tracked by git

### Install the required dependencies
```
bundler install
```

### Start the Jekyll server
```
bundle exec jekyll serve

### Check the preview on your favorite browser by loading the following URL
http://127.0.0.1:4000/ 

### To stop the server user Ctrl + c


