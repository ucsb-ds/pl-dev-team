---
title: "Week 07a - Tue 05/13"
lecture_date: 2025-05-13
description: "Launch Legacy Code Project"
ready: true
layout: default
parent: lectures
retro_part_asn: TBD
canvas_retro_submission: TBD
team02: "[team02](https://ucsb-cs156.github.io/s25/lab/team02.html)"
team03: "[team03](https://ucsb-cs156.github.io/s25/lab/team03.html)"
js_hwk: TBD
---

# {{page.title}} - {{page.descripion}}

Please see: <https://ucsb-cs156.github.io/s25/lab/project.html>

## What you should do today

* Look over the issues with your team
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