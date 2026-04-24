---
parent: Topics
layout: default
title: "Github"
description:  "Using PrairieLearn with Github"
has_children: true
---

# {{page.title}} - {{page.description}}

Each PrairieLearn course has a github repo associated with it.

For example:

| Course | Repo |
|-|-|
| CMPSC 5A | <https://github.com/PrairieLearn/pl-ucsb-cmpsc5a> |
| CMPSC 5B | <https://github.com/PrairieLearn/pl-ucsb-cmpsc5b> |
| CMPSC 8 | <https://github.com/PrairieLearn/pl-ucsb-cmpsc8> |
| CMPSC 110 | <https://github.com/PrairieLearn/pl-ucsb-cmpsc110> 

The main branch of this repo is what PrairieLearn uses.   

Using the techniques explained in the topic ["Local Development"](https://ucsb-ds.github.io/pl-dev-team/topics/local_development/), you can work on PrairieLearn questions offline in a local clone of this repo, and then sync with PrairieLearn.

## Reviewing Pull Requests

A pull request to a PrairieLearn repo is made from a branch other than main.

To review the Pull Request:

* If you have not done so already, follow the steps [here](https://ucsb-ds.github.io/pl-dev-team/topics/local_development/#prerequisites) to get set up for PrairieLearn local development.  Note: they can take a while the first time you this because setting up Docker requires a lot of downloads to your computer; however, these are mostly cached so this is a one-time setup penalty.
* Clone the repo
* cd into the repo
* checkout the branch in the PR, i.e.
  ```
  git checkout some-branch-other-than-main
  ```
* Startup PrairieLearn locally: typically this means running the script `./ucsb-pl.sh` located in the main directory of the PrairieLearn repo.
* Click Load From Disk

Then, try the  questions that are added or modified in the Pull Request.

If the Pull Request is acceptable:

* Merge it into main
* Go back into the production PrairieLearn site, navigate to the sync page, and pull the changes into the PrairieLearn site.
* Test the changes again in production to make sure they still work.

