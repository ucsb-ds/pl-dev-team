---
description: Intro to Spring Boot, junit, jacoco, pitest
assigned: 2024-10-02
due: 2024-10-07 23:59
layout: default
title: jpa02
nav_order: 100
ready: false
layout: default
parent: lab
course_org: https://github.com/ucsb-cs156-f24
course_org_name: ucsb-cs156-f24
starter_repo: https://github.com/ucsb-cs156-f24/STARTER-jpa02
software: https://ucsb-cs156.github.io/f24/info/software.html
install_check: https://ucsb-cs156.github.io/f24/info/install_check.html
---


# NOT READY YET
# NOT READY YET
# NOT READY YET
# NOT READY YET

# Please do not start this lab yet.
# Please do not start this lab yet.
# Please do not start this lab yet.
# Please do not start this lab yet.

# {{page.title}} - {{page.description}}

This lab is going to cover a lot of new concepts.

* **Spring Boot**: You'll see the complete code for a very small web application created with Spring Boot.
* **HTML**: The markup language used for web page content.
* **Spring Boot Controllers**: Java Methods that map a url such as `/`, `/info` `/team` to the code that returns the HTML for a web page.
* **Unit Testing, JUnit, Test Suite**: You'll see Junit, a unit test framework for Java, and we'll talk about the idea of a test suite (a collection of unit tests for a body of code).
* **Line Coverage**: You'll be introduced to the idea of "line coverage", a weak (but fast) way to check whether a test suite has gaps in it.
* **Jacoco**: You'll work with Jacoco, a line coverage testing framework for Java.
* **Mutation Coverage**: You'll be introduced to the idea of "mutation coverage", a better (but slower) way to check the strength of a test suite.
* **Pitest**: You'll work with Pitest, a mutation coverage framework for Java

In the Java code, you'll see:

* **String.format**: a very useful Java method for formatting strings
* **JSON (JavaScript Object Notation)**: a compact syntax for representing objects (used not only in Javascript, but in almost all modern web and mobile applications)
* **Jackson `ObjectMapper`**: a package providing an `ObjectMapper` object that converts between Java object and JSON objects
* **Java Bean**: A Java Bean is simply a basic Java class with a default (no-arg) constructor,  getters and setters for each data element that follow a specific naming convention, implementations of equals, hashCode, and toString
* **Lombok**: An alternative way to generate Java Bean classes efficiently
* **A Class with Only Static Methods**: The use case for a class with only static methods, and how you handle test coverages for such classes

It's a lot, especially if you haven't seen Java before.  But don't worry: we'll guide you through it.

## The programming is basic

Because there are so many new concepts here, the programming will again be pretty simple, and we'll walk you through most of the steps.  

**Don't worry; there will be plenty of difficult programming challenges ahead**.  Right now, while there is so much new stuff going on, I don't also want to
overwhelm you with tricky programming problems *on top* of all of that.

## What you are going to do

We've divided the work into these parts:

* Part 1: Get to know the app
  * In this part, you'll run the app on localhost
  * You'll also deploy it on dokku (as you did in jpa01)
  * You'll also run the test suite, and see that the tests are currently passing
  * You'll also start looking at the jacoco and pitest output to familiarize yourself with them
* Part 2: Customizing the app
  * In this step, you'll start putting in correct values, replacing the placeholders such as `Chris G.` with your own name
  * You'll do this *first* in the test code (the code under `/src/main/java`)
  * You'll see that the tests then fail
  * Then do this in the main code (the code under `src/test/java`)
  * You'll iterate until the tests pass
* Part 3: Test Coverage
  * Next, you'll try to get to 100% test coverage, both using jacoco and pitest
  * We'll show you two ways to cover the tests gaps in the `Team` class for the `equals`, `toString`, and `hashCode` methods: the hard way (by hand) and the easy way (using Lombok)
    


## Part 1: Get to know the app

### Step 1.1: Clone repo and run app locally

In this part, you'll run the app on localhost

### Step 1.2: Deploy on Dokku

Now deploy the app on dokku (as you did in jpa01)

### Step 1.3: Deploy on Dokku

Now run the test suite with `mvn test`

Look over the tests.

### Step 1.4: Review Jacoco Report

Use `mvn test jacoco:report` to generate a line coveage report.

Then open the file `target/site/jacoco/index.html` in a browser
* On MacOS, you can just type `open target/site/jacoco/index.html`
* If anyone has an easy way to do this on WSL, please share it on `#help-lab02`, and we'll add it to the instructions here.

Look over the report, and look for the red.  These are parts of the code that were not touched when you ran `mvn test`.

This means the lines were *not covered* by the test suite.

Lines in yellow are lines that have a *branch* (i.e. an if/else type of construct).  The yellow signifies that at least one branch was covered, but at least one branch was not coverd.

At a later stage in this programming assignment, you'll need to write tests to address these gaps, but for now, just try to understand the output.

### Step 1.5: Review Pitest Report

Use `mvn test pitest:mutationCoverage` to generate a mutation coverage report.

Then open the file `target/pit-reports/index.html` in a browser

* On MacOS, you can just type `open target/pit-reports/index.html`
* If anyone has an easy way to do this on WSL, please share it on `#help-lab02`, and we'll add it to the instructions here.

Look over the report, and look for the red.  These are parts of the code where a mutant survived.

#### What does it mean that a mutant survived?

Here's how mutation coveage works:
* pitest starts with the assumption that your code is correct (after all, it passes your tests).
* Then, it makes many copies of your main code (usually dozens of copies), each with one "mutation" that is designed to break the code.
  * For example, if it finds `if (x < 0)` it mutates it to `if (x >= 0)`
  * If it finds `return result;` it changes it to `return null`
  * etc.
  These copies with mutations are called *mutants*.  Think of them like *mutants* in a science fiction film that are roaming the earth causing mayhem.
* It then runs your entire test suite on each of the mutants. (This is why it takes so long to run!)
* For each mutant, if at least one test fails, that means the *mutant was killed*.  That's *good*.  It means that your tests suite is powerful enough to detect when something has gone wrong in your code.
* But if there is a mutant where all of the tests pass, that means the *mutant survived*. That's usually *bad*.  It usually means your tests suite was not powerful enough to detect the problem.
  (There is a *rare* corner case where it might be a "false positive", meaning there's nothing wrong with your code or the test suite; we'll cover that case later as it arises).
* A third possibility is when the mutation causes one or more tests to go into an infinite loop.  This is called a "time out" and is a consequence of the *halting problem*, which is a topic of CMPSC 138.  In practice, we treat timeouts as "inconclusive" and ignore them; we focus only on trying to ensure that no mutants survive.

Notice which lines of code have mutant versions that survived the test suite.  At a later stage, you'll be asked to write tests to cover these mutation coverage gaps.
But for now, just make sure you are familiar with how to run pitest and look at the output.

## Part 2: Customizing the app

In this step, you'll start putting in correct values, replacing the placeholders such as `Chris G.` with your own name

You'll do this *first* in the test code (the code under `/src/main/java`)

You'll see that the tests then fail

Then do this in the main code (the code under `src/test/java`)

Iterate on this until the tests pass.

You should *also*, in parallel, actually run the application on localhost using `mvn spring-boot:run` to see that the output actually looks correct.

* Examine the contents of the home page (i.e. <https://localhost:8080/>)
* Example the contents when you click the link that takes you to <https://localhost:8080/info>
* Examine the contents when you click the link that takes you to <https://localhost:8080/team>

Make sure that every page has real information for you and your team, and that all of the placeholders are gone.

In addition, make sure that when you run `mvn test` all of the tests now pass.

When you are done with this step, make a commit with the following message, *replacing `xy` with your initials*:

```
git commit -m "xy - updated with actual developer name and team"
```

You are now ready to tackle the test coverage.

## Part 3: Test Coverage
  * Next, you'll try to get to 100% test coverage, both using jacoco and pitest
  * We'll show you two ways to cover the tests gaps in the `Team` class for the `equals`, `toString`, and `hashCode` methods: the hard way (by hand) and the easy way (using Lombok)
    
