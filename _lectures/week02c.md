---
title: "Week 02b - 10.09 Wed"
lecture_date: 2024-10-09
description: "More on jpa02"
ready: true
layout: default
parent: lectures
---

# {{page.title}} - {{page.description}}

## Reminder about [`#help-lecture-discussion`]({{site.slack_help_lecture_discussion}}) 
Reminder that during class, you should use the [`#help-lecture-discussion`]({{site.slack_help_lecture_discussion}}) channel when you need help from the staff.   This allows us to get to everyone in a fair way (first-come, first served), and also to ensure that the member of the staff with the most knowledge about your issue is the one that comes over.

## Today's work: continue [jpa02](https://ucsb-cs156.github.io/s25/lab/jpa02.html)

See: <https://ucsb-cs156.github.io/s25/lab/jpa02.html>

## A few updates!

1. Everyone should do this *again this morning* (even if you already did it before):
   ```
   git pull starter main
   git push origin main
   ```

   Reason: there were some references to older Github Actions embedded in the Github Actions scripts; ones that have been *deprecated*.  The word *deprecated* means: you shouldn't be using this thing any more, even though it used to work just fine.

   We also fixed two things yesterday:
   * Problem with the `Dockerfile` deployment script (incorrect code for installing `nvm`, but it doesn't matter, because we aren't using `nvm` for this lab, so just removing it was easier than fixing.)
   * Outdated text in the `README.md` file.
    
2. There is an interesting problem that arises with the mutation testing for the `hashCode()` function; credit to [this student, who found and reported it on `#help-jpa02`](https://ucsb-cs156-s25.slack.com/archives/C07RC2580UR/p1728449151605459).   (The post is only available to members of the Slack; you are all encouraged to go read it, and Prof. Conrad's response.)

   Here's the question (without the student's identity, to protect their privacy on the public facing website):

   ```
   I'm assuming the choice to use the | operator instead of something like & is arbitrary
   (i.e. using it still maintains the property of a hash function). Mutation testing is complaining
   that using & in replacement should cause test suite to fail, but in fact doesn't.
   How would you test this code if theoretically & should work? Unless it shouldn't?
   ```

   Prof. Conrad's response:

   > Ah, Terrific! You've stumbled across something we call the "equivalent mutation" problem.
   > 
   > Mutation testing is a pretty darn good technique. But it's not perfect. There are a few cases where it runs into problems. They are rare, but they do occur.
   >
  > An equivalent mutation arises when:
  > * There is more than one correct way to write the code (call two of these a and b)
  > * The correctness doesn't really depend on which implementation you choose, so you chose a
  > * One of the mutations turns a into b
  > * Since it's also a correct implementation it passes all the tests

  Adding to this explanation from the Slack: 

  We have exactly the situation described in the slack post.  The `hashCode()` function is just trying to combine the hash codes of the two parts in some way.  That can be done with bitwise `&` or bitwise `|`, and either way, you get a hash function that satisfies the requirements.   So, a mutation that turns one into the other is not going to affect correctness.

  In this situation, there are at least two ways I know of to get around the problem to get full mutation coverage:
  
  1. Write a test that *depends on a particular implementation*.  This works, though it's kind of "overspecifying" the requirements, so it's not ideal. That is, you are adding requirements to your test suite that really aren't *strictly* necessary for the implementation to be "correct" in the sense of meeting the needs of the users.   This is a case where some comments to clarify this may be helpful. 
  2. Configure the mutation testing framework to just skip this mutation and/or this method.

  For this exercise, I'm going to recommend option 1, because it's easier to understand and implement.  Here's the trick:

  1. Write a test for the `hashCode` function something like this:
     ```
     // instantiate t as a Team object
     int result = t.hashCode();
     int expectedResult = 0;
     assertEquals(expectedResult, result);
     ```

  2. Run the test.  That test will fail the first time you run it.  But, you'll then learn what the actual value of the `hashCode()` function is on that object from the error message.
  3. Put that correct 
     value in for the `expectedResult`.  This is cheating, a little bit, so it's not a great idea to get into this habit.   But sometimes, it's the most expedient way.

