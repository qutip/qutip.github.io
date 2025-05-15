Repository for QuTiP web pages
------------------------------

This repository contains the Jekyll source documents for building the
QuTiP and family packages website at [https://qutip.org](https://qutip.org).

Writing a Blog Post
-------------------

To add a posting to the [news](https://qutip.org/news) website you add a new file to the `_posts` folder.
There are already other files you can take inspiration from or you can [read the full documentation](https://jekyllrb.com/docs/step-by-step/08-blogging/) provided by Jekyll.

A few things to keep in mind:

- Make sure the file name is in `YYYY-MM-DD-filename.md` format, where `filename` can be of your choosing but unique.
- The `title` attribute at the top of the page will be the main header of the post and shown on the overview page.
- The first paragraph of your post will be shown on the overview page. It is advisable to put important links or a short and catchy introduction there.
- Using the `readmore` attribute, you can decide if your post should get its own page (set to `readmore: True`) or not (`readmore: False`).
See the difference of [this](https://qutip.org/news#new-website) and [this](https://qutip.org/news#qutip5-release) post.
- Assets like images are managed in the `assets` (*not* `images`) folder.

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

