.. _index:

Introduction to version control with Git
========================================

This is the introductory lesson to version control using
`Git <https://git-scm.com/>`__. It is assumed to be the very first thing
done in a course.

Our philosophy is that we start from own local repository, branching and
merging (locally), and a brief introduction to pushing to remotes. In
the separate `collaborative git
lesson <https://coderefinery.org/lessons/>`__, we teach more use of
remote repositories and good collaborative workflows. We try to stick to
simple workflows, just enough for researchers who are not obsessed with
Git to be able to work well. We try to avoid commands which might get
you into a confusing state.

The goals of the module as a whole are that the user will feel
comfortable about staging changes, committing them, merging, and
branching.


.. prereq::

   -  A reasonably recent version of Git is installed. For installation
      instructions see `the CodeRefinery installation
      instructions <https://coderefinery.github.io/installation/>`__.
   -  Being comfortable with the command line. No expertise is required,
      but the lesson will be mostly taken from the command line.
   -  Students should be familiar with using a text editor on their
      system. Emacs and Vim are excellent choices if you know how to use
      them but Nano or Notepad on Windows are sufficient.
   -  Git should be configured prior to the lesson following `our
      installation
      instructions <https://coderefinery.github.io/installation/>`__.
   -  A `GitHub <https://github.com>`__ user account (but alternatives
      exist, see below).


.. toctree::
   :maxdepth: 1
   :caption: Core episodes

   motivation
   basics
   branches
   conflicts
   remotes
   archaeology
   level


.. toctree::
   :maxdepth: 1
   :caption: Optional episodes

   staging-area
   recovering
   interrupted
   aliases
   under-the-hood


.. toctree::
   :maxdepth: 1
   :caption: Reference

   exercises
   guide
   reference
   customizing
   resources


.. note::

   **Why GitHub?**

   In this introduction we will mention and use
   `GitHub <https://github.com>`__ but also
   `GitLab <https://gitlab.com>`__ and
   `Bitbucket <https://bitbucket.org>`__ allow similar workflows and
   basically everything that we will discuss is transferable. With this
   material and these exercises we do not endorse the company
   `GitHub <https://github.com>`__. We have chosen to demonstrate a
   number of concepts using examples with
   `GitHub <https://github.com>`__ because it is currently the most
   popular web platform for hosting Git repositories and the chance is
   high that you will interact with
   `GitHub <https://github.com>`__-based repositories even if you choose
   to host your Git repository on another platform.

   Course participants are most welcome to use our `Nordic research
   software repository platform <https://source.coderefinery.org>`__
   instead, for more information see
   https://coderefinery.org/repository/.
