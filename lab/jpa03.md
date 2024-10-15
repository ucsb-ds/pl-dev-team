---
description: "Configuring Full Stack App (Frontend/Backend, OAuth, Database)"
assigned: 2024-10-15
due: 2024-10-21 23:59
layout: default
title: jpa03
nav_order: 100
ready: false
qxx: f24
layout: default
parent: lab
course_org: https://github.com/ucsb-cs156-f24
course_org_name: ucsb-cs156-f24
starter_repo: https://github.com/ucsb-cs156-f24/STARTER-jpa03
slack_help_channel: "[#help-jpa03](https://ucsb-cs156-f24.slack.com/archives/C07RY3BQPCZ)"
teams_url: https://bit.ly/cs156-f24-teams
example_running_app: https://jpa03-staff.dokku-00.cs.ucsb.edu/
office_hours_page: https://ucsb-cs156.github.io/f24/office-hours
software_install_url: https://ucsb-cs156.github.io/f24/info/software.html
staff_emails: "phtcon@ucsb.edu,sangitakunapuli@ucsb.edu,amey@ucsb.edu,jenilrajeshkumar@ucsb.edu,djensen@ucsb.edu,gracefeng@ucsb.edu,hongrui_su@ucsb.edu"
starter_storybook: "https://6709627038191f269c9a870b-waqkeiwvio.chromatic.com/"
canvas_link: https://ucsb.instructure.com/courses/21167/assignments/262241
---

<style>
  tt {white-space: pre}
  code {white-space: pre}
  pre {white-space: pre}
</style>

{% include drop_down_style.html %}

# NOT READY YET
# NOT READY YET
# NOT READY YET
# NOT READY YET

Please wait before starting this lab.  We are still adjusting the instructions for changes that resulted from the upgrades of the started code to Java 21, Node 20, and others changes.

For due date: see the jpa03 entry on Canvas: <{{page.canvas_link}}>

# Instructions for jpa03

If you run into problems, let us know on the {{page.slack_help_channel}} channel on the slack.

{% include drop_down_style.html %}

This is an **individual** lab on the topic of deploying
Java web apps that use OAuth and Databases, using Dokku.

You may cooperate with one or more pair partners from your team to help in debugging and understanding the lab, but each person should complete the lab separately for themselves.

## Goal

By the end of this lab, you'll have deployed your own copy of the starter code repo (<{{page.starter_repo}}>) on both localhost
and Dokku.

This app is a full-stack web app with:

* A front-end built in React (under the directory `./frontend`)
* A back-end built in Spring Boot (the code for this is under the directory `./src`, plus the `pom.xml` at the top level
* OAuth integration; this allows the app to have a "login/logout" feature based on Google Accounts (e.g. your UCSB Google Account)
* A SQL database, which runs using H2 (an in-memory database) on localhost, and using Postgres when running on Dokku.
* Automatic generation of javadoc and Storybook/Chromatic web pages for both
  the production code (`main` branch) and all branches that have
  open pull requests targetting the `main` branch.

This app is not intended as a coherent app to solve a real-world problem,
but as a code base that demonstrates many of the techniques you
would need in such an app.   The legacy code apps that we'll work
with in this course have a similar structure.

Here is an example of this app, up and running.  Try logging in with your UCSB Google Credentials:

* <{{page.example_running_app}}>

If the menu looks like this, click on the hamburger icon (☰) to expose the Login button:

<img width="799" alt="image" src="https://user-images.githubusercontent.com/1119017/235781737-648575ec-c095-4ecf-a218-12ec579d4d19.png">

It should then look like this, and you should be able to login:

<img width="732" alt="image" src="https://user-images.githubusercontent.com/1119017/235782012-7775743c-1880-4960-b99a-3417055f850e.png">

Once you are logged in, you'll see a navigation bar like this one (though you will not see the `Admin` menu):

<img width="1208" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/c6acd005-85fb-4907-b65e-cce203a61294">

None of the menus will do much of anything.  It turns out that the application is
a shell of an application that:

* allows users to login and logout using a Google account
* allows the developer to configure some users as "admins"
* allows admin users to see who has logged in to the app in the past (by storing
  each login in a database)

However, we need those basic functions as a basis to build more complex functions,
and every student in the class needs to know how to configure and deploy an app on
Dokku.  The configuration has several parts:

* Setting up SSL (https) for your dokku app
* Configuring Google OAuth (this can be tested on localhost first)
* Setting up the dokku app
* Connecting it to a Github repo
* Configuring https
* Configuring a postgres database on Dokku

So, let's get started.


## Step 1: Understanding what we are trying to do

## What are we trying to accomplish in this lab?

This lab has little to no programming.
The point of the lab is to walk you through the steps you need to
take to deploy full-stack Spring Boot/React apps on Dokku, configuring them for Google OAuth (for logins) and a Postgres database.

There are quite a few configuration steps that are needed,
and we want to get you used to those before we start
introducing the coding challenges as well.

## Step 2: Create your repo

There should already be a repo for you under the course organization
with a name in this format:

* <tt>https://github.com/{{page.github_org}}/{{page.title}}-<i>githubid</i></tt>

where <tt><i>github</i></tt> is your github id.

If not, create one for yourself following that naming convention;
it should initially be public, and empty (no `README`, license or
`.gitignore`.)

Clone that repo somewhere and cd into it.

Then add this remote:

<tt>git remote add starter {{page.starter_repo}}</tt>

That sets up `starter` as a remote with the code from this github repo:
* <{{page.starter_repo}}>

Then do:

```
git checkout -b main
git pull starter main
git push origin main
```

## Step 3: Configure Actions and Github Pages

In this step, we'll:
* Enable Github Actions if not already enabled
* Set up Github Pages
* Set up Chromatic Project Token
* Check that Storybook/Chromatic are building properly

### Step 3.1: Enable Github Actions (if not already enabled)

Go to the webpage for your repo on Github.  Find the `Actions` tab on your repo.  It should look like one of the images below

<table>
<thead>
<tr>
<th>
If GitHub Actions are not yet enabled:
</th>
<th>
If GitHub Actions are already enabled:
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<img width="476" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/a7d67508-1a03-4215-a1de-e63bc58cddd0">
</td>
<td>
<img width="984" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/1a60521f-474d-4bbd-a8eb-3c0c66dc134f">
</td>
</tr>
</tbody>
</table>

If it looks like the one on the left, click the green button that says "Enable Actions on this Repository".

### Step 3.2: Enable Github Pages

Next, visit the file [`docs/github-pages.md`]({{page.starter_repo}}/blob/main/docs/github-pages.md) on GitHub or in your repo and read what it says to do to configure the documentation for your repo on Github Pages.

When you've completed this step, on your main repo page on Github, the link at right under `About` should take you to the Github Pages for your repo; it should look like this:

<img width="341" alt="image" src="https://github.com/user-attachments/assets/04522e3a-3c27-4288-afa8-54b201fee266">

The link will be of the form: <tt>https://{{page.course_org_name}}.github.io/jpa03-<i>yourGithubId</i></tt>, where <tt><i>yourGithubId</i></tt> is replaced by your Github Id.   Click on the link, and you should see a page like this one:

<img width="300" alt="image" src="https://github.com/user-attachments/assets/32f4ca67-c0e0-4364-b5f5-12f266b90929">

If you don't:
* Look through the instructions again
* Try manually running the Github Action `/02-gh-pages-rebuild-part-1.yml` (note that it will automatically start `04-gh-pages-rebuild-part-2.yml` when it is finished.
* If any steps in workflows `02` or `04` completed with errors, try running them again.  It is not unusual for the "Deploy" step to fail; there are sometimes [race conditions](https://en.wikipedia.org/wiki/Race_condition) with multiple jobs trying to publish to the site at the same time, and we have not yet determined a way to prevent that.
* If the jobs fail repeatedly or on a step other than the "Deploy" step, you may need to ask the staff for help.


### Step 3.3: Enable Chromatic

In this step, we are setting up *Storybook*, which is software that allows us to document and test the frontend of our application, one component at a time, without needing the backend at all.  

As an example of Storybook, here is a link to the storybook for the starter code:
* {{page.starter_storybook}}

<details markdown="1">
<summary markdown="1">
Click the triangle to read more about why Storybook and Chromatic are useful when building a full-stack web applications.
</summary>

Storybook is helpful for several reasons:

* You can develop frontend components without depending on whether the backend part is working yet.  This is very helpful for team projects where you may want to have different team members working on the frontend and the backend. (Note, however, that it's *very* important to agree in advance on the interface between the frontend and the backend!).
* You can test the frontend components separately from the backend.  This is very helpful when debugging problems in the web app which are typically caused by one of three things (a) a problem in the backend, (b) a problem in the frontend (c) a error in communication between the front and backend.  Having a way to isolate the frontend makes it much easier to identify the root causes of such problems.
* It serves as a way of documenting the collection of user interface elements that a present in the code base.  This is helpful for being able to reuse user interface components, or identify the existing part of the user interface that's closest to the one you intend to build.
* It helps to be able to identify opportunities for refactoring the user interface code to make it more consistent.

Chromatic.com, in addition to providing web hosting for Storybook sites, offers: 
> "... a visual testing & review tool that scans every possible UI state across browsers to catch visual and functional bugs. Assign reviewers and resolve discussions to streamline team sign-off."

The idea is that the first time your Storybook is built, it takes a screenshot of each user element.  On subsequent builds, it again takes those screenshots, and if/when any of them change, it asks whether the change should be approved or rejected.  This is incorporated into the Github Action for Storybook which will remain marked with a yellow (i.e. unfinished, incomplete) until the developer reviews the changes in the user interface elements.
  
</details>

To configure your web app for Chromatic, you need to:
* Create a Chromatic.com account (using your Github login)
* Visit the page <https://ucsb-cs156.github.io/topics/chromatic> and follow the instructions to set up your repo as a Chromatic project.
* Once it is setup as a project, you'll be able to obtain a value for the `CHROMATIC_PROJECT_TOKEN`
* Then, you can set up the `CHROMATIC_PROJECT_TOKEN` as a repository level secret, accessible to the Github Actions scripts.

### Step 3.4: Check that Chromatic is building properly

Once you've set up the `CHROMATIC_PROJECT_TOKEN` value, you'll need to re-run the Github Actions scripts that publish the Storybook to the
repo's Github Pages site.

Go to the Github Actions page for your repo; you'll need to run the job `53-chromatic-main-branch.yml` again; it will likely have failed on the 
first run for lack of a value for  `CHROMATIC_PROJECT_TOKEN`.

<details markdown="1">
<summary markdown="1">
Click the triangle to read about how to re-run failed Github Actions
</summary>

Here's how to re-run failed Github Actions:

1. Go to the Github Actions tab of your repo
2. On the left side, in the list of workflows, if the one you are looking for is not listed, click `Show More Workflows`, as shown here:

   <img width="317" alt="image" src="https://github.com/user-attachments/assets/5a1b6386-460a-484a-a89b-ec8251a81504">

3. On a failed workflow, if you click it, there should be a button like this to re-run the failed workflow:

   <img width="278" alt="image" src="https://github.com/user-attachments/assets/c9740071-4941-40ba-9948-7ed492f9aaeb">

   Alternatively, find the button upper left that says "Run Workflow", click it, and then click the green `Run Workflow` button, as shown here:
   
   <img width="920" alt="image" src="https://github.com/user-attachments/assets/ef8c6b89-77fd-4d29-8367-09441ab8e5d1">

</details>

When you've re-run the Github Action `53-chromatic-main-branch.yml`, navigate to the Github Pages site for repo.

<img width="412" alt="image" src="https://github.com/user-attachments/assets/6190a217-87d4-4058-a0c1-45a799df4292">

And the links for `Storybook` and `build info` should take you to pages that looks like these:

| storybook | build info |
|-|-|
| <img width="500" alt="image" src="https://github.com/user-attachments/assets/eaa1b86d-cd8a-449d-81bc-4fa813f51a7d"> | <img width="500" alt="image" src="https://github.com/user-attachments/assets/061b53c9-9f07-47c1-9ea6-1f5df030e06b"> |


## Step 4: Configure your app for localhost as documented in the README.md

Before we start configuring your app, let's take just a moment to learn what OAuth is.

## About OAuth

OAuth is a protocol that allows you to delegate the login/logout
functionality (user authentication) to a third party such as
Google, Facebook, GitHub, Twitter, etc.  If you've ever used
a website that allows you to "Login with Google", "Login With Facebook", or "Login with Github" then chances are good that app was built using OAuth.

Indeed, you've already encountered an examples of GitHub OAuth earlier in the course when you used your GitHub account to log into the <https://ucsb-cs-github-linker.herokuapp.com>

When implementing a website that can store information and making it available on the public internet it's important to *secure the site;* otherwise, bad actors may fill your database with unsavory material.

One choice is to implement our own username/password authentication, but I want to strongly caution you: if you take on the responsibility of storing passwords, you are assuming a lot of risk.  The problem is that people reuse passwords, so even if you think that your site isn't that important, the problem is that the passwords you are storing might be the same ones folks are using for other sensitive apps.

Using OAuth sidesteps this issue:
* Your app never actually sees the password the user enters; it is entered on a page that is hosted by Google (or Facebook, or Github, or whoever is providing the OAuth service.)
* The user doesn't need to come up with a new username or password; they can use one they already have.

Implementing OAuth can be tricky at first, but once you get the hang of it, it's far easier than everything you would need to do to really work with usernames/passwords securely and safely.

## Steps to Configure your app

The next step is to read through the [`README.md`]({{page.starter_repo}}/blob/main/README.md) and configure your app as indicated there.

As shown in the [`README.md`]({{page.starter_repo}}/blob/main/README.md), these steps include the following.  Each of these is documented in files linked to from the [`README.md`]({{page.starter_repo}}/blob/main/README.md) file so we won't repeat those here; we'll just link to them.

1. [Configuring GitHub Pages for the documentation]({{page.starter_repo}}/tree/main#configuring-github-pages-for-the-documentation)
2. [Getting Started on localhost]({{page.starter_repo}}/tree/main#getting-started-on-localhost), which includes:
   - Setting up Google OAuth credentials
   - Entering those credential in the `.env` file
   - Learning how to run the backend and frontend in separate windows

## The `.env` file  should *not* be committed to GitHub

I already made this point, but I really, really want to emphasize it.

One of the values in the `.env` file is called a client *secret* for a reason.

If it leaks, it can be used for nefarious purposes to compromise the security of your account; so don't let it leak!

Never, ever, commit those to GitHub, and try to only share them in DMs on Slack (not in public channels).

Security starts with making smart choices about how to handle credentials and tokens. The stakes get higher when you start being trusted with credentials and tokens at an employer, so learning how to handle these with care now is a part of developing good developer habits.

The staff reserve the right to deduct points if we find that you have committed your `.env` file to GitHub.

## Green check ✅, not red X ❌

Once you've completed your setup, GitHub Actions should be running on the main branch with
a green check, not a red X.  If there are problems there,
address those as best you can before submitting.

# Step 5: Configure your app to run on Dokku

The steps to get your app up and running on Dokku are documented here:

* <https://ucsb-cs156.github.io/topics/dokku/deploying_an_app.html>

Note that there are are *more steps* than in the previous labs, since this app is more complex:
* It requires configuration variables
* It requires a Postgres database
* It requires a special `dokku git` setting (to keep the `.git` directory)
  
Once you've followed these instructions, try logging in to your app.

* You should see that you are logged in
* You should see an Admin menu, where you can see the names of everyone that has logged in

## What if it doesn't work?

If it doesn't work:

* Check on the Slack channel <tt>#help-{{page.num}}</tt> to see if there are any known issues.
* Ask folks on your own team for help first on your team's slack channel.
* Post a specific question on the <tt>#help-{{page.num}}</tt> slack channel—note what you were trying to do, what you expected, and what happened instead.  Screenshots or copy/pasted console output is helpful!
* Come to office hours (posted here: <{{page.office_hours_pages}}>)
* Ask during class on `#help-lecture-discussion`


## Step 6: Add link to running app to your README.md file

At the top of your README.md, you'll find this:

<img width="500" alt="image" src="https://user-images.githubusercontent.com/1119017/235758700-20b3d8cf-d0dc-4182-8e6d-5e6ef551956a.png">

Follow these instructions; i.e. put in the link to your running app on Dokku, and
remove the comment so that afterwards it looks something like this (but with your actual Dokku link,
not the example value shown here).

<img width="500" alt="image" src="https://user-images.githubusercontent.com/1119017/235759017-e48fdcf6-abb7-40e7-8ae8-71173113d4cd.png">


## Step 7: Submit on Canvas

Here's a checklist to look over before submitting on Canvas:

1. On the main page for the repo: is the app "green on CI"? i.e. does the `main` branch have a green check for the Github Actions scripts?
2. On the main page for the repo: is there a link to the apps Github Pages site on the main page for the repo?  (i.e. the site whose URL is something like `https://ucsb-cs156-s24.github.io/jpa03-cgaucho`)?
3. Does the Github Pages site link take you to a page with links to
   javadoc and storybook?
4. Do those javadoc and storybook links work?
5. In the README.md file: is there a link to the running app?
6. Does OAuth work on the running app, i.e. can I log in with my Google login?
7. Did you remember to add the staff(see emails in the rubric below), your teammates, and yourself to the `ADMIN_EMAILS` variable in your `config:set` on dokku?
8. Did you deploy a database? If so, for Admin users, the Users menu should show who has logged in recently (it uses the database to do this.)
If so, then you are ready to submit on Canvas.

* Submit the link to *your repo*, not the link to your running app.

## Grading Rubric:

* (10 pts) There is a repo with the correct name in the correct organization with the starter code for this lab
* (10 pts) There is a post on Canvas for this assignment that has the correct content (i.e. a link to the repo, not the running app on Dokku)
* (10 pts) README has a link to your running web app.
* (10 pts) There is a running web app at <tt>https://{{page.num}}-<i>githubid</i>.dokku-xx.cs.ucsb.edu</tt>
* (10 pts) Running web app has the ability to login with OAuth through a Google Account.
* (10 pts) The `ADMIN_EMAILS` variable is set to include all staff emails (see list below) plus your own email.
  - The correct setting is shown below, except with your email in place of <tt><i>youremail</i></tt>
  - <tt>ADMIN_EMAILS=<i>youremail</i>@ucsb.edu,{{page.staff_emails}}</tt>
* (10 pts) The link on your main repo page is set your Github Pages page (i.e. <tt>https://{{page.course_org_name}}.github.io/{{page.num}}-<i>yourGithubId</i></tt>, where <tt><i>yourGithubId</i></tt> is replaced by your Github Id.  ) 
* (10 pts) The Github Pages page shows a web page that looks like the example in the lab instructions and has the correct content.
* (10 pts) Chromatic is configured correctly, and the Github Pages site has a Storybook configured properly.
* (10 pts) GitHub Actions runs correctly and there is a green check (not a red X) on your main branch

Note that the Rubric above is subject to change, but if it does:

* You'll be notified during a class meeting
* You'll have an additional week from the date of the announced change to get your repo in shape with the new requirements.

## Instructor Resources


<details markdown="1">
<summary>
Click the triangle for a list of tasks the instructor should do prior releasing this lab.
</summary>

* Create {{page.num}} repos using the <https://ucsb-cs-github-linker.herokuapp.com>
* Set up starter code in the course organization, and update links
* Create a Canvas assignment for {{page.num}}
* Make sure the app <{{page.example_running_app}}> is up and running, and is sync'd with the starter code:

  i.e, on dokku-00 for example, do:
  <pre>
  dokku git:sync {{page.title}}-staff {{page.starter_repo}} main
  dokku ps:rebuild {{page.title}}-staff
  </pre>
  
* Remove older users from the database, e.g.
  ```
  dokku postgres:connect jpa03-staff-db
  select * from users;
  delete from users where id>2;
  \q
  ```
* Proofread the instructions in this file, and request that the staff (TAs/LAs do also)
* Consider assigning at least one TA/LA (preferably the one with the least prior experience with the course) to complete the lab in it's entirety to debug the starter code and instructions
* Be sure that the organization settings are set like this, in, for example, <https://github.com/organizations/ucsb-cs156-s24/settings/actions>

  This is needed so that the github actions scripts have write access to the directory.

  <img width="943" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/de8c9efe-7bcd-48a1-97d5-0c0aa68a68db">


  This setting is probabaly also a good idea:

  <img width="972" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/99fead23-d9d0-4373-a435-466c5ef9e752">


</details>
