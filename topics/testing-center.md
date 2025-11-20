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

## When students report "bugs"

It is not uncommon for students to report bugs with PrairieLearn problems.

It is also very common for these "bugs" to end up being student errors rather than PrarieLearn bugs. The student will claim that they put in a correct answer, and then PrairieLearn marked it incorrect.  Then they put in "exactly the same answer again", and it marked it correct.

The student often, in good faith *thinks* this is what happened.  But when you look at the submission, you see the error in their first answer.  So you may need to  patiently take a screenshot of their first answer (which is available; PrarieLearn saves this) and then point out their mistake.

Having said that, every now and then, there *is* a legitimate problem with the question.   In that case, you can apologize to the student, update the student's grade, and then fix the problem so it doesn't reoccur the next time.  But this is not as common as the case of students simply making errors and attributing it to PrairieLearn.

## Encourage student to report "bugs" using the `Report an error in this question` button

There is a button on each problem in PrairieLearn in the student facing interface that looks like this:

<img width="534" height="99" alt="image" src="https://github.com/user-attachments/assets/7f4f1694-3828-4707-a086-f9d2bb0d0c87" />

It may be helpful to communicate to students:

> Please use the `Report an error in this question` button if you perceive that there is a problem with the question or with the grading of the question. That is the *only* way that I can review the question and possibly give you credit if the question  was graded incorrectly.

When the student does that, you get a snapshot of everything going on with that question, as opposed to just disconnected emails 
where they "claim" something went wrong, but you have no easy way to look into, check the accuracy of their report, and give them credit if their report uncovers a legitimate problem.

## Reminding Students About Reservations

If you want to remind students that have not made a reservation yet to do so:

* Navigate to <https://us.prairietest.com>
* Select your course, e.g. at the link <img width="1170" height="124" alt="image" src="https://github.com/user-attachments/assets/fd05c923-eb24-4a4f-b30c-5f7e7126f19b" />
* Select your assessment, e.g. by clicking on "Final" in the screenshot: <img width="362" height="412" alt="image" src="https://github.com/user-attachments/assets/70c732a6-5202-4767-a473-cb13e17ab71e" />
* Select `Reservations` as shown here: <img width="895" height="439" alt="image" src="https://github.com/user-attachments/assets/f8c0e8c3-dddb-4a69-aa60-3c22ebc7efbc" />
* In tab at right hand side of page, click `Actions for all Students` then, `Export Reservations` <img width="322" height="298" alt="image" src="https://github.com/user-attachments/assets/d3a3a2aa-0b8a-49ac-aa7c-7aa05b95d986" />
* Now you can upload this CSV file to a spreadsheet program and sort to get the emails of the students that have not yet made a reservations, and contact them via bcc to remind them that if they do not make a reservation, they will be unable to take the exam, and will receive a zero, or however you want to phrase it.    Sending this out is "handholding", but it's also insurance; if they claim ignorance, you can point out that they "could have known, and should have known" that they needed to make a reservation.




