---
parent: Topics
layout: default
title: "Testing Center"
description:  "Setting up exams for the Testing Center"
---

# {{page.title}} - {{page.description}}

This page is currently just a collection of notes about things to watch out for when setting up quizzes or exams to be given in the testing center.

Eventually, it may be fleshed out into a more comprehensive guide.

## Make sure you have an access rule for the course instance

When you set up an exam in the testing center, you'll need to put the snippet the testing center gives you into the `access` element for your assessment.

As it turns out **this is necessary, but not sufficient**.  Also make sure that you have defined an access rule for the course.  

Otherwise, students will not be able to see the assessment; they will get "Access Denied" when they try to open the quiz. 

In order for the Prairie Test to have access to the course instance, there needs to be at least one access rule set 
up for the course instance (in addition to having the "examUuid" that allows the testing center to pull up the assessment).

Giving it a start date in `infoCourseInstance.json`
is sufficient, e.g. "2015-01-19T00:00:01"
as per the documentation: <https://prairielearn.readthedocs.io/en/latest/courseInstance/>

 
