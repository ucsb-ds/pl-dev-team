---
title: "Week 07a - Tue 05/13"
lecture_date: 2025-05-13
description: "Launch Legacy Code Project"
ready: true
layout: default
parent: lectures
---

# {{page.title}} - {{page.descripion}}

Please see: <https://ucsb-cs156.github.io/s25/lab/project.html>

## What you should do today

1. Assign yourself your first issue
2. Clone the repo and get the app working on localhost
3. Create a dev deployment on dokku

## Assigning yourself your first issue

* Look over the issues with your team
* Read the Sprint Planning document (it's linked in the README of the repo.)
* Decide what your first issue will be
* Assign it to yourself and put it in the In Progress column on the Kanban board.
* If there are follow on issues that flow from the first one in an Epic, you might assign yourself those as well and drag them into "ToDo", but don't work *too* far ahead.  Let the team be *Agile* (i.e. it can move quickly from one plan to another).

# Be *careful and thoughtful* about assigning issues

Unlike the team01/team02/team03 projects,  the project is NOT "designed" to help you avoid merge conflicts (or create simple ones for you to practice on.)

There are many issues, and they may have complex dependencies on one another.  We *sometimes* point these out, but *not always*. And sometimes we get things wrong.

And unlike team01/team02/team03 that have been worked on by a few hundred studnets before you over a couple of years, the issues in the legacy code project have *literally never been attempted by anyone*.  

So it's entirely possible that some of them are:
* Incorrectly specified
* Contradictory

This is a *normal part of real world software development*.   
* We haven't laid traps for you *on purpose*.  
* But there are almost certainly some traps there!

One of them is dependencies:
* MAKE SURE that it doesn't depend on another issue being done first!
* DISCUSS with your team who is working on what.  
* Communicate early and often about this!

This is another one of the reasons that standup is so important.  Be sure you *know* what other people on the team are working on.

# IMPORTANT: Review this when you make a PR

* <https://ucsb-cs156.github.io/topics/pull_requests/>

If you have commented out code in your pull request, or put LGTM on a PR with commented out code in it, we'll forgive you *once*, *maybe*.  

If you do it a second time, we'll be really irritated.

Please read the document about PRs, and refer to it *often* when making and reviewing PRs.

# Setting up your app on localhost and dokku

Setting up the app on localhost and dokku is a little more complicated that with team01/team02/team03 unless you are working on proj-rec

* proj-rec setup is just like team01/team02/team03
* proj-dining also requires setting up the UCSB_API_KEY
* proj-courses also requires setting up UCSB_API_KEY and MongoDB
* proj-frontiers also requires Github configruation in *addition to* Google configuration.

