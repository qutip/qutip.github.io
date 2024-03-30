Repository for QuTiP web pages
------------------------------

This repository contains the Jekyll source documents for building the
QuTiP and family packages website at [https://qutip.org](https://qutip.org).

Testing locally
---------------

Complete instructions for testing changes locally can be found in the
[GitHub documentation](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll).

The short version of the instructions is:

 - Install Ruby and Bundler usings the appropriate tools for your platform.
 - Run `bundle install` which installs the dependencies listed in the `Gemfile`.
 - Run `bundle exec jekyll serve` which will build the site and serve it locally.

Deploying changes
-----------------

Push changes to master triggers the default GitHub pages build action which
runs Jekyll and deployes the updated website.

