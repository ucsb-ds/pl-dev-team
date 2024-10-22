---
title: "Week 03a - 10.15 Tue"
lecture_date: 2024-10-15
description: "Start jpa03 (Configure Full Stack Spring Boot with OAuth, Postgres)"
ready: true
layout: default
parent: lectures
jpa03: "[jpa03](https://ucsb-cs156.github.io/f24/lab/jpa03.html)"
---

# {{page.title}} - {{page.descripion}}

## From [Slack Post at 4:11pm](https://ucsb-cs156-f24.slack.com/archives/C07FDC0U6DS/p1729033915670989)

Class today: We’ll start {{page.jpa03}} which may be the last individual assignment before we start the first team assignment.  

Please note that while I’ve set the due date for this as this coming Sunday (in case you run into problems), my hope is that the majority of you will finish this in class today, or during discussion tomorrow, because we may be ready to start the team assignments as early as tomorrow in discussion.

So, please do not assume that tomorrow will be “just a work day” on jpa03.   We might be starting something new tomorrow, and it may required team participation.

You may start on jpa03 before class if you like.  If you complete it, you are still encouraged to come to class (or stay in class) to help others on yoru team, but at the very least, let your team know if you finished it before class are are choosing not to come.

## From [Later Slack Post (5:54pm)](https://ucsb-cs156-f24.slack.com/archives/C07FDC0U6DS/p1729040065164739)

In the instructions for jpa03 inside `oauth.md` when it refers to your “mentor”, please disregard that, and instead, add these emails: which are in the jpa03 instructions:

```
ADMIN_EMAILS=youremail@ucsb.edu,phtcon@ucsb.edu,sangitakunapuli@ucsb.edu,amey@ucsb.edu,jenilrajeshkumar@ucsb.edu,djensen@ucsb.edu,gracefeng@ucsb.edu,hongrui_su@ucsb.edu
```

Be sure not to use any spaces; just separate the emails with commas.

You should also add the emails for the members of your team.

## From [Later Even Slack Post (6:28pm)](https://ucsb-cs156-f24.slack.com/archives/C07FDC0U6DS/p1729040065164739)

if you are getting 404s on the Chromatic storybook and build pages, please try this:

```
git pull starter main
git push origin main
```

Then re-run workflow Github Actions workflow 02 (that rebuilds the web site).

Wait until all Github Actions are done including the one thats’ labelled pages build and deployment

Then try again and see if the links work.

If that still doesn’t work, let me know, but also, continue with the other steps of the lab, and we’ll circle back to this.

Fun fact: most of the parts of this lab are things we’ve been doing for several quarters now, but the Chromatic stuff is all brand new.  So I’m not surprised we are running into some issues.


Also, I got an email from Chromatic that our project is over it's monthly quota of snapshots.

So, it may very well be that we run into some other issues have to have pivot regarding the Chromatic thing…
We used to do this a different way, and we may have to return back to that.

I'll keep you updated.



