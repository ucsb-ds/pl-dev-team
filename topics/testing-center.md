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

## Rebooking is possible but only up to 1 hour before the slot

Communicate this to students:

* If you book a quiz/exam slot, and it turns out you can't make it, you may cancel up until *one hour before* the scheduled slot.  Once you cancel, you can book a new time, assuming that times are available.
* If you wait until after 1 hour hour before the scheduled slot to try to cancel, you will not be able to. That slot *is now the only slot* in which you can take the exam. Missing it is just like missing a regular in-class exam; there is no make up at that point.

Exceptions are possible for "true emergencies".  True emergencies are the kind of thing that a student would be reporting to the Dean of Student's office such as "you were in a car accident and are in the hospital" or "you had to fly home to be at the beside of a dying relative", where you are missing all of your classes, for an extended time, for a signficant event beyond your control.  In this case, the testing center is able to delete a reservations, which allows a student to rebook a new session; however, the testing center generally won't do this unless it is a true emergency.

