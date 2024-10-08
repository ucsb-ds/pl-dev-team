---
description: Intro to Spring Boot, junit, jacoco, pitest
assigned: 2024-10-02
due: 2024-10-07 23:59
layout: default
title: jpa02
nav_order: 100
ready: false
qxx: f24
layout: default
parent: lab
course_org: https://github.com/ucsb-cs156-f24
course_org_name: ucsb-cs156-f24
starter_repo: https://github.com/ucsb-cs156-f24/STARTER-jpa02
software: https://ucsb-cs156.github.io/f24/info/software.html
install_check: https://ucsb-cs156.github.io/f24/info/install_check.html
slack_help_channel: "[#help-jpa02](https://ucsb-cs156-f24.slack.com/archives/C07RC2580UR)"
---

<style>
 code {white-space: nowrap;}
 tt {white-space: nowrap;}
</style>

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

## Do you need a Unix tutorial/refresher?

Throughout these labs, we'll assume a basic knowledge of Unix commands such as `ls`, `cd`, `mkdir`, `rm`, `mv`, `cp`, `chmod`, `pwd`, `cat`, `more`, `less`, and many others.

* [This video tutorial by Ryan He](https://youtu.be/1W5V4GHPO4E?si=aBcPXImlZIhethnz) was developed under the supervision of Prof. Ziad Matni, and is a nice introduction to basic Unix commands if you need a refresher, or if you are joining CS156 as a transfer student from a school where Unix was not used.
* [This PDF](https://github.com/ucsb-cs156/ucsb-cs156.github.io/blob/main/topics/unix/A-Basic-Linux-Workshop.pdf) goes along with the video.


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

### Step 1.1: Clone repo

Reviewing, from jpa00 and jpa01:

* In this course, you'll typically start with an empty repo, created by the staff.
* In this case, look for a repo under <{{page.course_org}}> with the name <tt>{{page.title}}-<i>yourGithubId</i></tt>.
* It will start as an empty repo
* You'll then find a place on your laptop to clone it (we suggest under the directory `~/cs156`, but that's up to you).
  <pre>
  cd ~/cs156 
  git clone {{page.title}}-<i>yourGithubId</i>
  cd {{page.title}}-<i>yourGithubId</i>
  </pre>

You will then have a local repo on your laptop that is a *clone* of the repo on Github.   


### Step 1.2: Pull in starter code

For this step, you need to be at a terminal prompt, and your current directory should be the one where you cloned the repo: [{{page.course_org}}/{{page.title}}-<i>yourGithubId</i>]({{page.course_org}}/{{page.title}}-yourGithubId)

If you type `git remote -v`, you should see that you have something like the following (with `%` representing the terminal shell prompt):

(If you get an error, be sure that you are in the correct directory, i.e. <tt>~/cs156/{{page.title}}-<i>yourGithubId</i></tt>.)

<pre>
% git remote -v
origin	git@github.com:{{page.course_org_name}}/{{page.title}}-<i>yourGithubId</i>.git (fetch)
origin	git@github.com:{{page.course_org_name}}/{{page.title}}-<i>yourGithubId</i>.git (push)
% 
</pre>

What this output signififies is the the name `origin` is the name of a *remote* repo that you can fetch branch information from, pull commits from, and push commits to.

* The `git` system works with both *branches*, which are multiple copies of code in the same repo, and *remotes*, which are the urls of other repos containing branches.
* In this assignment, we'll only work with a single branch in each repo, the `main` branch.
* In future assignments we'll work with multiple branches.
* But, we are working with multiple *remotes* in this assignment:
  * (1) `origin` which is the repo assigned to you,
    specifically, <tt>{{page.course_org}}/{{page.title}}-<i>yourGithubId</i></tt>, and
  * (2) `starter`, which is the repo containing the starter code, which is at <{{page.starter_repo}}>.

**To define the remote called `starter`**, do this:

<pre>
git remote add starter {{page.starter_repo}}
</pre>

(If you mess up the command, you can undo it by doing `git remote remove starter` and then adding it again.)

After you do this, try `git remote -v` again, and you should see the `starter` remote defined:

<pre>
% git remote -v
origin	 git@github.com:{{page.course_org_name}}/{{page.title}}-<i>yourGithubId</i>.git (fetch)
origin	 git@github.com:{{page.course_org_name}}/{{page.title}}-<i>yourGithubId</i>.git (push)
starter	{{page.starter_repo}} (fetch)
starter	{{page.starter_repo}} (push)
% 
</pre>

Now, to pull in your starter code, simply do:

```
git pull starter main
git push origin main
```

After you do this, you should have all of the starter code from <{{page.starter_repo}}> both:
* In your current directory, when you type `ls`
* On Github.com, when you look at this url (adjusting for your own githubid): <{{page.course_org}}/{{page.title}}-*yourGithubId*>

When you've completed those steps, you are ready to deploy your app on localhost.

### Step 1.3: Deploy on `localhost`

Now, to deploy the app on `localhost` (as you did in jpa01), we run the following command:

```
mvn spring-boot:run
```

You'll then need to open a browser on the same machine where you are running the `mvn spring-boot:run` command, and navigate to the url <http://localhost:8080>

You should see a web app come up that looks like this:

![image](https://github.com/user-attachments/assets/f054ff33-f9a2-4498-bc17-922a435887b8)

Note that the web app is only available while you are running the `mvn spring-boot:run` command in the terminal shell.
* If you terminate that shell by typing `CTRL/C`, then you'll see that the web browser no longer brings up the web app, but instead a message that the page is not reachable.

Explore the web app a bit, following the instructions in this table.  The box at the right shows what you should see.


| Instructions | Screenshot |
|--------------|------------|
| Find the Developer Info link on the home page, and click it.  It should take you to a new page at `/info`)  | ![image](https://github.com/user-attachments/assets/3c260e64-a03a-4f03-b0ac-c9580e693d11) |
| The page at `/info` should have information about a fictional developer named `Chris G.`, with their github being `cgaucho`, and their team being <tt>{{page.qxx}}-xx</tt>.  Click the `cgaucho` link | ![image](https://github.com/user-attachments/assets/3f6893ee-f09f-4835-b8b0-3fbcb2de01a4) |
| The `cgaucho` link should take you to the Github profile of github user `cgaucho`.  Click the back button to return to the `/info` page. | ![image](https://github.com/user-attachments/assets/3a7d13b3-9d3e-46d6-b10b-cbd2d129e815) |
| Now, back on the `/info` page, click the link for <tt>{{page.qxx}}-xx</tt> to go to the `/team` page | ![image](https://github.com/user-attachments/assets/892e630a-a3d1-4c9b-a41e-60b1daeecfd6) |
| Note that the page at the url `/team` looks different from the rest. This page is not encoded in HTML, but rather in JSON.  The exact format on the screen will depend on your browser, so it may be formatted with indentation, or may just be one big long string. There's a longer discussion of this below. | ![image](https://github.com/user-attachments/assets/a75d4d00-a6f7-4a1c-b879-60df40212f26) |

#### Let's talk about this JSON page

If you've followed the instructions above, you see that the page `/team` looks different from the You'll now see a different kind of page in your browser.  This page contains information in *JSON* format, which is short for *Javascript Object Notation*.

JSON is simply a way to represent the *data* portion of *objects*. Here, we mean *objects* in the *object-oriented programming* sense, though technically, we are only representing the *data* portion of object *instances*.

Here's the JSON content from the web app, formatted with indentation:

```text
{
 name: "f24-xx",
 members: [
   "Alice",
   "Bob",
   "Chris G.",
   "Danny",
   "Eve",
   "Frances"
   ]
}
```

Without indentation, it might look like this; it's harder to read, but equivalent in terms of what it represents.
```
{name: "f24-xx",members: ["Alice","Bob","Chris G.","Danny","Eve","Frances"]}
```

JSON is usually pronounced like this: "Jay Son", rhyming with the phrase "play on".

We'll talk a lot more about `json` as the course progresses, but for now, just notice that:
* The JSON object is surrounded by curly braces (`{}`)
* It is a set of key/value pairs.
* The keys are `name` and `team`.
* The value of `name is a string in *double quotes* (`"Chris G."`)
* The value of team is an array of strings, surrounded by square brackets (`[]`).
  
We'll come back to a discussion of JSON objects later on, and we'll look at the code that produces pages in either HTML or JSON format.

### Step 1.4: Deploy on Dokku

Now deploy the app on dokku (as you did in jpa01)


All steps require you to login to your dokku machine, i.e. the following series of `ssh` commands (replacing `xx` with your two digit team number).

```
ssh username@csil.cs.ucsb.edu
ssh username@dokku-xx.cs.ucsb.edu
```

<details markdown="1">
<summary markdown="1">
Click the triangle for a list of teams and dokku hostnames
</summary>
{% include dokkus.md %}
</details>

The steps to deploy the app are explained here: <https://ucsb-cs156.github.io/topics/dokku/deploying_simple_app.html> in detail, but here's the short version.

First time: 

| Explanation | Command(s) |
|-------------|------------|
| 1. Create dokku app | <tt>dokku apps:create {{page.title}}-<i>yourGithubId</i></tt> |
| 2. Sync the app with git repo, main branch | <tt>dokku git:sync {{page.title}}-<i>yourGithubId</i> {{page.course_org}}/{{page.title}}-<i>yourGithubId</i>.git main</tt>
| 3. Deploy the `http` version of the app | <tt>dokku ps:rebuild {{page.title}}-<i>yourGithubId</i></tt> |
| 4. Configure email for `https` support | <tt>dokku letsencrypt:set {{page.title}}-<i>yourGithubId</i> email <i>youremail</i>@ucsb.edu</tt> |
| 5. Enable https on your app | <tt>dokku letsencrypt:enable {{page.title}}-<i>yourGithubId</i></tt> |

To redeploy any time the repo changes (otherwise changes in the repo don't affect the running app):

| Explanation | Command(s) |
|-------------|------------|
| 1. Re-sync the app with git repo, main branch | <tt>dokku git:sync {{page.title}}-<i>yourGithubId</i> {{page.course_org}}/{{page.title}}-<i>yourGithubId</i>.git main</tt>
| 2. Re-deploy the `http` version of the app | <tt>dokku ps:rebuild {{page.title}}-<i>yourGithubId</i></tt> |

Once you have done these steps, you should be able to see your app running at *both* of these links (modifying them for your dokku/team number, and your github id):

* http (not secure): [http://dokku-xx.cs.ucsb.edu/{{page.title}}-<i>yourGithubId</i>](http://dokku-xx.cs.ucsb.edu/{{page.title}}-yourGithubId)
* https (secure): [https://dokku-xx.cs.ucsb.edu/{{page.title}}-<i>yourGithubId</i>](https://dokku-xx.cs.ucsb.edu/{{page.title}}-yourGithubId)

When that works, you're ready for the next step.

### Step 1.5: Run the test suite

Now return to the terminal command line.  You should `cd` into the directory where you cloned the repo (e.g. <tt>~/cs156/{{page.title}}-<i>yourGithubId</i></tt>)

You are now going to run a suite of tests.  There will be *lots* of output.  The main thing is that the last part of the output should look like this, indicating that the tests passed:

```
[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.327 s -- in edu.ucsb.cs156.spring.hello.HelloControllerTest
[INFO] 
[INFO] Results:
[INFO] 
[INFO] Tests run: 7, Failures: 0, Errors: 0, Skipped: 0
[INFO] 
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  4.257 s
[INFO] Finished at: 2024-10-08T11:56:18-07:00
[INFO] ------------------------------------------------------------------------
pconrad@Phillips-Mac-mini-2 jpa02-pconrad %
```

Here's what that looks like with screen highlighting:

![image](https://github.com/user-attachments/assets/b55781e5-37b1-4b49-9afb-38a8adfdae70)

The most important lines here are these:

```
[INFO] Tests run: 7, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

Later in this assignment, we'll make some changes to the app and we'll see these tests fail, but *not just yet*.  We want to look at something else first, and
that requires the test suite to be "green", meaning, that all tests pass.  For those that can see color, the words `BUILD SUCCESS` show up in green, indicating
that the tests passed.  If one or more did fail, it would look something like this instead:

```
[ERROR] Tests run: 7, Failures: 1, Errors: 0, Skipped: 0
[INFO] BUILD FAILURE
```

Or, with screen highlighting:

![image](https://github.com/user-attachments/assets/a84a86a1-a69f-4df4-b531-59985d9fd8dc)

The tests are located in the directory `/src/test/java/edu/ucsb/cs156/spring/hello`, in the files listed below (the links take you to the version of the code in the starter repo).  Look them over, and you'll see that there are some `TODO` items 
marked in comments.  *Later* in this assignment, you'll be addressing those `TODO` items, **but not yet**.   We need a green test suite before we look at this next step.

* [`ApplicationTest.java`]({{page.starter_repo}}/blob/main/src/test/java/edu/ucsb/cs156/spring/hello/ApplicationTest.java)
* [`DeveloperTest.java`]({{page.starter_repo}}/blob/main/src/test/java/edu/ucsb/cs156/spring/hello/DeveloperTest.java)
* [`HelloControllerTest.java`]({{page.starter_repo}}/blob/main/src/test/java/edu/ucsb/cs156/spring/hello/HelloControllerTest.java)
* [`TeamTest.java`]({{page.starter_repo}}/blob/main/src/test/java/edu/ucsb/cs156/spring/hello/TeamTest.java)

If you are familiar with the idea of writing unit tests for code, then you can just skim the test files above. But if this is a new concept to you, please look over the tests in some detail and try to understand what is happening in these tests.

The basic idea of unit tests is that we want to write some code that tests our "main" code.   In a Maven project, we keep all of our `main` code and our `test` code in entirely separate directory trees (there are several really good reasons for this but we won't go into those just now.)  

A few key points:
* Each of the tests is a single Java method annotated with `@Test`.
* A unit test, ideally, should test just one *unit* of code, i.e. a single method, not relying on any other code (This is not always entirely possible, but that's the goal; in practice you sometimes need to rely on the correctness of the constructor, for example, before you can test a method.)
* In a unit test, there are typically three parts:
  * Arrange: set up the context of the method you want to call
  * Act: call the method you want to test (or otherwise cause it to be invoked)
  * Assert: make one or more *assertions* that should be true if the code worked properly

Look for these in the test code. Note that not all of the test code follows this pattern *precisely*, which may lead you to have many questions.  That's good! Ask the questions on {{page.slack_help_channel}}, and we'll try to answer as many as we can.

But in the meantime, let's move on to discussing code coverage and mutation coverage.

### Step 1.6: Review Jacoco Report

The next two steps involves what may be a new concepts to you:

* *test coverage* in general: more specifically *line coverage* and *branch coverage*
* *mutation testing*

All of these are ways of *measuring the qualilty of a test suite*.  The main idea is:

* Our test suite (collection of unit tests) checks for bugs in the code (assuming that the tests are correct)
* Test Coverage and Mutation Testing *tests that tests themselves* to make sure that the test suite is as complete as possible.

Note that *no testing approach can guarantee 100% correctness*. (Pay attention to that previous sentence, because a misunderstanding of this is one way that students lose points on the final exam.)

Testing can only show the *presence* of bugs, never the *absence* of bugs.
* More specficially: failed tests show that a bug is present (either in the code, or the test).
* A purely green test suite does *not* show that your code is free of bugs; there might be some case you didn't test for!

That last part is the key here: we want to *minimize* the number of cases we didn't test for.

What *test coverage* and *mutation testing* do for us is exactly that: they help uncover parts of the code that are *not* being tested adequately, so that we can try to improve our test suite.

In this step, we focus on the first of these techniques, *test coverage*.

What test coverage does is very simple and fast:
* It runs the entire test suite once
* As it does, it keeps track of every line of code that was executed by at least one of the tests
* The lines left over (the ones that were never executed) are the *gaps in coverage*; lines of code for which you need to write a test.

Clearly, if a line of code was never executed by a test, then the test suite cannot possibly distinguish between whether that code is correct or incorrect.  So if the correctness of that line of code is important, we need to write a test for it.

A tool called `jacoco`, which is short for "Java Code Coverage" can check for line and branch coverage in Java:
* `line coverage` entire lines of code to see if they were run by at least one test
* `branch coverage` looks deeper into things like `if/else`, loops, conditional expressions, etc to ensure that if there is more than one *path* through the code (e.g. the `if` part and the `else` part), that *both* branches were covered.

#### Running `mvn test jacoco:report`

Let's run a line coverage report by typing:

```
mvn test jacoco:report
```

When you do, it will run the test suite, and then generate a jacoco line coverage report, which will be formatted as a web page.  Here's what the tail end of that output looks like:

```
[INFO] --- jacoco:0.8.12:report (default-cli) @ hello ---
[INFO] Loading execution data file /Users/pconrad/github/ucsb-cs156-f24/jpa02-pconrad/target/jacoco.exec
[INFO] Analyzed bundle 'hello' with 4 classes
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  3.968 s
[INFO] Finished at: 2024-10-08T12:32:52-07:00
[INFO] ------------------------------------------------------------------------
pconrad@Phillips-Mac-mini-2 jpa02-pconrad % 
```

There will be no particular indication of the outcome of the report, or where to find it; you just *have to know*.  

The place to look for it is under `target/site/jacoco/index.html`.
* On MacOS, you can open that file with the command `open target/site/jacoco/index.html`
* On Windows, one way to open it is to open the File Explorer, and navigate to the `index.html` file and double click it

In any case, once you open it, it should look like this:

![image](https://github.com/user-attachments/assets/2614fb23-f396-45d3-b0ff-a9dd6bd4c258)

Look over the report, and look for the red.  These are parts of the code that were not touched when you ran `mvn test`.

Let's zoom in on this part:
![image](https://github.com/user-attachments/assets/7970f262-6106-43a9-a677-607258b3e3a0)

It shows the package `edu.ucsb.cs156.spring.hello` and it shows that the code in this package has only 86% line coverage, and 56% branch coverage.  Our goal is to get that to 100%

* An aside: in most industry settings, 100% coverage is explictly **not** the goal; there are diminishing returns if you start chasing 100% coverage in very large legacy code bases.
* However, in this course, we've engineered things so that on these early assignments 100% coverage is definitely reasonable and possible.
* Further, in our large code bases, we adopt an approach of *identifying* the parts of the code that should be *reasonably* exempt from code coveage, and *excluding them* from the computation.
* Accordingly, while in many settings 100% coverage may not be a reasonable goal, in this course *it always is*.

So, how can we learn more?  Click on the package name  `edu.ucsb.cs156.spring.hello`; it's a link and it should open up a page that looks like this:

![image](https://github.com/user-attachments/assets/ff40860d-39af-4de9-b1d0-d83c1e0fcb30)

On *this* page, we see individual class names.  And we can see that all of the problems (lines not covered by tests) are in the `Team` class.

So, now we can click on the link for `Team` and it takes us to a page like this one, where we see statistics for individual constructors and methods:

![image](https://github.com/user-attachments/assets/d6677d54-14fc-4b10-9cd3-762ed873a28a)

From here, we can see that three methods, in particular, are the ones not tested:
* `hashCode`
* `toString`
* `equals`

Clicking on any of these three links takes us to a page with the source code, marked up with information about the line and branch coverages gaps.  Click on any one of these, and you'll be taken to a page that looks like this (I'm only showing the part from line 56 to the bottom, so you may need to scroll to see this view):

![image](https://github.com/user-attachments/assets/9d126368-40b2-48bd-b210-1f3212aeebcf)

A few things to notice:
* The green on lines 60-61 shows that the `setMembers` method is fully covered by tests (this is also true of all the methods and constructors earlier in the file; scroll up to verify)
* The mix of yellow, red and green in the `equals` method shows that some parts are covered by tests, but others are not.
  * Green means completely covered (the whole line was run by at least one test)
  * Red means not covered at all (none of this line was run during any test)
  * Yellow means partial branch coverage (some part of this line was run by at least one test, but at least part of this line was *not* run by *any* test).
* The solid red in the remaining two methods shows they are not covered by tests *at all*.
  
One note, especially for *red/green colorblind folks*, but really for everyone: `jacoco` here is violating an important priciple of accessiblity (sometimes abbreviated as [a11y](https://www.a11yproject.com/): don't depend solely on color (especially red/green) to indicate something in a user interface.   It's a [known issue with jacoco](https://github.com/jacoco/jacoco/issues/144); after the course is done, if you feel confident, you might submit a pull request to try to address it.  The link also has some suggested work arounds if it's a problem for you.

As we'll discuss later in the assignment, the three methods `hashCode`, toString` and `equals` are really important methods for a Java class; if they are not implemented correctly, many things can go wrong.
So testing them is important.

Later in the assignment, we'll show two ways to address this testing gap:
1. Write good tests for these methods
2. Rewrite the class so that these methods are generated automatically, and therefore don't need to be tested.

But for now, as long as you understand how to generate a line/branch coverage report (i.e. `mvn test jacoco:report`) and how to interpret the output, you are good to move on.

### Step 1.7: Review Pitest Report

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
    
