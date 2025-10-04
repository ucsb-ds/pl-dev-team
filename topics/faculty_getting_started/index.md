---
parent: Topics
layout: default
title: "Faculty: Getting Started"
description:  "Information for faculty getting started with PrairieLearn"
---

# {{page.title}} - {{page.description}}

If you are a faculty member that's just getting started with PrairieLearn,
this page is the place to start.

I won't sugarcoat it: learning to use PrairieLearn is challenging.  The good news is that the payoff is worth it, but it's a long journey.

Here's an high level outline of the different kinds of things you'l need to learn, each of which has it's own complications:

1. Creating a Course.
2. Creating Questions
3. Creating a Course Instance
4. Creating an Assessment
5. Interacting with PrairieTest

Here's more information about each of these.

## 1. Creating a Course.

Note that a "course" in PrarieLearn is something that lasts "forever", meaning that you don't create a new "course" every term (quarter, semester, etc.).  Instead, you create a course like "CMPSC 8" or "MATH 3A" once, for all time.  Then, each time the course is offered, you create a "Course Instance" (e.g. "Fall 2025", "Winter 2026", etc are all course instances.)

## 2. Creating Questions

Once you have a course, you can start creating questions. You may think that the next step would be to create a course instance, but a course
instance is of no value whatsoever until you've created questions.

Questions are individual items that you would put on a practice quiz, homework assignment, or a real quiz/exam that you'd give in a supervised testing center.   

There are a *lot* of question types: multiple choice, fill in the blank, numeric answer, short answer, questions involving drawing graphs, and more.   

When you start with PrairieLearn, it makes sense to start with the simplest kind of question, the so-called *single variant* question, where the question is exactly the same every time (except, perhaps, for shuffling the options on a multiple choice question).

However, the real power of PrairieLearn comes when you, or someone you work with, writes computer code (in the Python programming language) to generate *question variants*, i.e. different versions of the question so that:
* on a practice quiz, students can practice over and over again with mutiple versions of the question
* on a homework, quiz or exam each student gets a different version of the question.

And unlike other systems that choose questions randomly from a fixed bank of questions, each of which has to be authored separately, the idea here is that the different versions are produced by Python code. 

(It is worth noting, since we writing this in 2025, that this is typically *not* an application of AI, but old fashioned "regular" programming; the system has existed for over 10 years, before the AI boom.)

In addition, for courses involving coding, you can give the students an opportunity to write code either in a simple editor, or a full computing environment such as a Jupyter Notebook, VS Code, RStudio, or a Unix command prompt, and coding questions can be autograded.

Nevertheless, even with all of this power available to you,the most important advice from the PrairieLearn team is to *start simple*.  Get to know PrairieLearn a bit at a time, starting with simple options, and then get more complex as you get more comfortable.  

As you develop questions, it's helpful to have some people (e.g. colleagues, teaching assistants or student helpers) that can test them and make sure that they are reasonable, especially if they involve random generation of different question variants.

Once you have enough questions for a practice quiz, homework, quiz or exam, you are ready to create your first Course Instance and your first Assessments.

## 3. Creating a Course Instance

Once you have a course, you can create questions, and you can test each question individually.   Questions belong to a *course*.

But to do anything with those questions in a real setting with students, you need to create an *assessment*, and assessments belong to a *course instance*.

* A course is something like "CMPSC 8" or "MATH 3A".  It is not necessarily connected to a particular student roster, and could even be shared among multiple instructors over multiple years.
* A course instance belongs to a course, and is something like "Fall 2025", or "W26 TR 2pm".  It is  associated with a specfic start end end date, specific instructor(s) of record and a roster of students. 

Once you have created a course instance, you can start creating assessments.

## 4. Creating an Assessment

Assessments are collections of questions that students attempt on a practice quiz, homework assignment, real quiz or real exam.

For practice quizzes, homework assignments, or quizzes given in class (i.e. not in a proctored test center outside of class), you do not need to interact with the software component known as PrairieTest.

But if you do want to administer quizzes or exams in a proctored testing center (such as the [UCSB Testing Center](https://testingcenter.ucsb.edu/)), you'll need to interact with PrairieTest as well.

## 5. Interacting with PrairieTest

PrairieTest is the platform for administering PrairieLearn assessments in a Computer Based Testing Center such as the [Testing Center](https://testingcenter.ucsb.edu/)) at UC Santa Barbara.

**Note**: The other sections of this guide may be useful for faculty outside of UCSB, but this section will be much more UCSB specific; while the PrarieTest software is the same at every campus, the policies and procedures for interacting with it and scheduling exams may vary.

You'll need to ask the testing center staff to set up your course on PrarieTest, which is at the url <https://us.prairietest.com>, as opposed to <https://us.prairielearn.com>.

Once they do that, you'll first ask your students to register for the course on PrairieTest by logging in, finding the link for your course instance, and clicking to join.


