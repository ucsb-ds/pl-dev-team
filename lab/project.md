---
title: project
desc: "Legacy Code Project instructions"
assigned: 2024-11-13 11:00
due: 2024-11-26 17:00
github_org: ucsb-cs156-s24
layout: lab
layout: default
parent: lab
num: project
nav_order: 500
proj_courses_slack_url: 
proj_happycows_slack_url: 
proj_rec_slack_url:
proj_dining_slack_url:

githubOrgUrl: https://github.com/ucsb-cs156-s25
githubProjectsUrl: https://github.com/orgs/ucsb-cs156-s25/projects
githubPagesUrl: https://ucsb-cs156-s25.github.io
sections:
  -
      time: 11am
      product: proj-courses
      productShort: courses
      teams:
        -
          num: "01"
          dokku: "01"
          kanban: 38
        -
          num: "02"
          dokku: "02"
          kanban: 39
        -
          num: "03"
          dokku: "03"
          kanban: 40
        -
          num: "04"
          dokku: "04"
          kanban: 41
  -
      time: 11am
      product: proj-rec
      productShort: rec
      teams:
        -
          num: "05"
          dokku: "05"
          kanban: 42
        -
          num: "06"
          dokku: "06"
          kanban: 43
        -
          num: "07"
          dokku: "07"
          kanban: 44
        -
          num: "08"
          dokku: "08"
          kanban: 45
  -
      time: 4pm
      product: proj-happycows
      productShort: happycows
      teams:
        -
          num: "09"
          dokku: "09"
          kanban: 46
        -
          num: "10"
          dokku: "10"
          kanban: 47
        -
          num: "11"
          dokku: "11"
          kanban: 48
        -
          num: "12"
          dokku: "12"
          kanban: 49
  -
      time: 4pm
      product: proj-dining
      productShort: dining
      teams:
        -
          num: "13"
          dokku: "13"
          kanban: 50
        -
          num: "14"
          dokku: "14"
          kanban: 51
        -
          num: "15"
          dokku: "15"
          kanban: 52
        -
          num: "16"
          dokku: "16"
          kanban: 53
---

<style>
  td, th { min-width: auto}
</style>

# s25 Legacy Project Launch

On {{ page.assigned | date: '%A %B %d %Y at %l:%M%p' }}, in section, we'll launch the legacy code projects.

This page describes how that will roll out.

# Due Date

The due date for getting PRs in, green on CI, and reviewed by a member of your student team is {{ page.due | date: '%A %B %d %Y at %l:%M%p'  }}, i.e. at the *start* of class that day (typically the last class day of week 9).

After that, you may only:
* Work on existing PRs to address issues raised by the staff in code review
* Add new PRs *if and only if* approved in advance by a staff member to address an issue raised during a code review of an already existing PR.

Taking on new work after that point is not permitted, since we need time for the staff to review the work already completed, and get it merged so that you can make your final release notes and final video presentation.


# Links


<details markdown="1">
<summary markdown="1">Open this section for links to the legacy code project resources
</summary>


{% for section in page.sections %}
## Section: {{ section.time }} ({{section.product}})

| Team | Repo | PRs | Github Pages | Kanban | Dokku Prod | Dokku qa |
|------|------|-----|--------------|--------|------------|----------|{% for team in section.teams %}{% capture teamName %}{{site.qxx}}-{{ team.num }}{% endcapture %}{% capture repoName %}{{section.product}}-{{teamName}}{% endcapture %}
|  {{teamName}} |  [ repo ]({{page.githubOrgUrl}}/{{repoName}}) |   [ PRs ]({{page.githubOrgUrl}}/{{repoName}}/pulls) |  [ github pages ]({{page.githubPagesUrl}}/{{repoName}}) | [ kanban ]({{page.githubProjectsUrl}}/{{team.kanban}}) | [ dokku prod ](https://{{section.productShort}}.dokku-{{team.dokku}}.cs.ucsb.edu) | [ dokku qa ](https://{{section.productShort}}-qa.dokku-{{team.dokku}}.cs.ucsb.edu) | {% endfor %}

{% endfor %}

</details>

# The Assignment, Briefly.

In this project:

* You will be assigned a legacy code base, and a set of issues
  (new features, refactorings, bug fixes)
* The list of issues contains more work than we expect you will need to complete
  in order to get a perfect score on the project, so don't worry that you have
  to finish them all; *you do not have to finish them all*.
* Some of the issues are "epics", which is a higher level than an issue: it's a group of related issues. It is the responsibility of the team members to take the epic and create smaller issues from it, copying/pasting the relevant parts and the editing the file to turn it into smaller single issues.  Each of those should usually be merged in its own separate small PR, not as one giant PR at the end.
* Each issue you complete earns points for your team after it is:
  * code reviewed and approved by a member of your team that didn't work on it
  * code reviewed and approved by a member of the course staff (instructor, TA, LA)
  * merged into the main branch of your repo.
* Issues earn different numbers of points: typically, 5, 10 or 20 depending on
  the complexity of the issue (more on this below).
* There may be a few issues that are marked as "must do".  You *must
  complete these* or their point values will be subtracted from the points you
  earn. These are assigned point values in advance.
* For other issues,
  points are assigned after completion. If you want to ask for a point
  estimate, you may do so, but keep in mind that actual points can differ
  from estimated points.
* Unlike in previous team projects, where your Issues list and
  Kanban board may have been
  pre-populated with issues by the staff,
  in the legacy code phase, populating the Kanban board
  is the responsibility of the team.  More on that below.
* The aim of the team is to earn 100 points before the deadline.  This forms the
  most important part of you project grade, which is 25% of your course grade.
* Another part of your project grade is your "CATME multiplier", which is a number
  based on your peer evaluations.  This number is typically 100 unless your team
  has rated you significantly below the team average
* Points beyond 100 can count as extra credit as explained below.

# Points beyond 100

If you accumulate more than 100 project points, the additional points may count as extra credit, at a rate of 1 extra credit point for each 10 points over 100 earned, up to a maximum project grade of 110.  For example:

| Points Earned | Project Grade |
|---------------|---------------|
|    80         |    80         |
|    90         |    90         |
|   100         |  100          |
|   105         |  100.5        |
|   110         |  101          |
|   115         |  101.5        |
|   150         |  105          |
|   180         |  108          |
|   ≥200        |  110          |

Your final project grade is maxed out at 110 total project points--any points in excess of 110 will not count towards your grade (though you'll probably learn a lot from having under taken the work to earn them.)


# Sprint Planning for Legacy Code project

Each team already has a Kanban board setup for the legacy code project (see links above).   However unlike in your team01, team02, and team03 projects, it's up to you to populate this yourself.

Populate your todo column with issues, start assigning them to your team, and start working.

You may not get through all of the Sprint planning today, but by the end of discussion section on Wednesday:
* Each of the six team members should be assigned to an issue in the todo column
* The previous bullet point should *remain true* until your team reaches 100 points
* This may require breaking issues out of an epic.  In some cases, you may need to assign different team members to work on backend and frontend issues from the same epic in parallel, or pair-program on some of the early issues.

Teams accumulate points when PRs are merged into main
* That is only done by the course staff for these projects.
* Each PR requires at least one code review from a team member, and at least one code review from a staff member
* The staff estimate points. Most issues are 5 to 10 points.
  - 5 points for very straightforward issues addressing a single concern
  - 10 points for issues that require a bit more work, but are nevertheless reasonably straightforward application of skills from team01, team02, team03.
  - 20 points is rare, and is reserved for issues that may be more complex, and/or require students to go significantly beyond the skills from previous course assignments.
* Note that breaking down issues into smaller chunks works to your benefit in multiple ways:
  - Easy to code review and merge (fewer merge conflicts), so faster point accumulation
  - Three 10 points issues and three 5 points issues adds up to 45 points; combining all of those together might only get you 20.
  - But the aim here should not be to "game the points". It should be to "get the issues implemented", in incremental "right sized" pieces.
  - If you do that, the points will take care of themselves.

Points belong to the whole team, not to individuals
* Work as a team, and help each other.
* We do want to see every team member contribute
* Ultimately, it's a team project and a team grade.
* Having said that, really low CATME scores might result in a grade reduction.


## Where do issues come from?

For issues, you'll need to do a bit more work that in the previous team projects.

Each of your repos is populated with an issues list (see the issues tab).

* These issues come in different sizes
  - A handful of these may be small easy issues.
  - However, many (most?) of these issue *may not translate one-to-one into issues for your Kanban board*.
  - Instead, you are encouraged to try to *break the larger ones down into smaller issues*, each of which could be a single PR; more on this below.
  - This Sprint Planning meeting is where you can do some of that.
  - You may even need to add "issues about issues", e.g. an issue that says: "break issue #34 from proj-happycows into multiple issues on our team's repo".  Such an issue doesn't result in a PR, but it can still be moved across the Kanban board from `To Do`, to `In Progress`, to `In Review`, to `Done`.
* Your team's own ideas for features; these should be vetted with a staff member before you get too far into working on them, to ensure that they are aligned with user needs.   **Issues that are not aligned with customer will not be merged into main and will not earn points** so be sure that you vet your issues with staff if they are ones you came up with yourself.

Staff may add to these issues over the course of the project; when we do, we'll post an announcement in the project slack channels.

## You are encouraged to keep each PR small.

For example, implementing a new feature may require
* A new React Component (with tests and storybook entries, and perhaps fixtures to support those)
* A new React Page
  - This page might start out with a simple PR that establishes a placeholder with text "New feature coming soon", and a trivial set of tests and a storybook entry
  - It might later get data from the backend and display it using a component, and be linked to from the navigation bar.
* A new database table (or a new column in an existing database table, requiring modifications to an `@Entity` and/or `@Repository` class
* New API backend endpoints, which require controller methods and tests.

Each of these could (and arguably should be) a separate PR!  This helps to keep PRs small, which makes code review easier, and also helps the team to divide up work among the team members.

Still, you may need to document in the issues what the dependencies are (e.g. "do issue 12 and 13 before starting 14").

# Setting up dokku prod and qa instances

The staff will work with you to set up dokku prod and qa instances; that will happen on Thursday Nov 14.

# What should we do today

* Start reading through the issues
* Start assigning first issues on the Kanban board


# Staff Information

Information in the dropdown below is intended for course staff.  Students are welcome to look at it, but it's really targetted at a different audience.

<details markdown="1">
<summary>
Staff information for legacy code phase
</summary>


## Creating the team repos



To set up repos for the legacy code project phase, use the <https://ucsb-cs-github-linker.herokuapp.com> tool.  The menu option you want is "Teams // Create Team Repos":


Team repos are created using the usual process, but the syntax is a little different.  Here's an example for S24:

<img width="453" alt="image" src="https://github.com/ucsb-cs156/s24/assets/1119017/3992fe71-2beb-45e2-8602-d88d4a407154">


Repeat for each group of teams and each project.

We assign `Write` permission rather than `Admin` permission so that the staff can control the `main` branch with branch protection rules.


## Preparing starter repos

Each of the starter repos needs the following preparation

### Set CODEOWNERS

Put the github ids of the instructor, TAs and LAs (anyone that can merge into main) into this file:

<img width="1094" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/1225e0ed-016d-45c7-a1ee-37b765b95a91">

* <https://github.com/ucsb-cs156/proj-courses/blob/main/.github/CODEOWNERS>
* <https://github.com/ucsb-cs156/proj-gauchoride/blob/main/.github/CODEOWNERS>
* <https://github.com/ucsb-cs156/proj-happycows/blob/main/.github/CODEOWNERS>
* <https://github.com/ucsb-cs156/proj-organic/blob/main/.github/CODEOWNERS>

### Set up branch protections

Instructions for setting up branch protections can be found here:

<https://ucsb-cs156.github.io/cs156-guide/1-legacy-code-projects/3-setting-up-projects.html#establishing-branch-protections>

### Be sure issues you want students to work on are tagged

Check the issues list. Make a tag (e.g. `S24`) for the issues you want the students to work on.

### Set variable to used used by workflow 99

In workflow 99, the tag gets its value from the organization variable QXX which should be set to match the tag (e.g. `S24`) that's 
applied to the issues you want to bulk copy over.

* Visit: <https://github.com/organizations/ucsb-cs156-s24/settings/variables/actions> to set that value, e.g. to `S24`

It should look like this:

<img width="1065" alt="image" src="https://github.com/ucsb-cs156/s24/assets/1119017/4882662f-407a-4e8a-9ad5-a40d21957799">


# Why we don't create team repos with a fork

We don't use the `fork` approach for this reason: If we created the team repos as forks, then every time students create a PR, the default would be a PR back to the main repo.  This would be
fine if each of the teams was working on an independent set of tasks, but if the design is to have each of the teams work on the *same* set of tasks, then their PRs would clash and be redundant.

So, instead, we create independent repos in the course organization for the class offering (e.g. <https://github.com/ucsb-cs156-f23>, or <https://github.com/ucsb-cs156-s24>, etc.) that are initially populated with the `main` branch of the repo from the <https://github.com/ucsb-cs156/> organization.

# Set up project channels

In the Slack workspace, set up channels for each project:

<img width="704" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/9a856d20-24e6-4f8e-b872-a84c2f47655b">

<img width="562" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/fcb80862-6fce-45f9-9fc2-105598137e5b">

<img width="559" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/f05d35ae-1ee0-49c0-8863-1024425b8168">

You can click "Skip for Now" and add folks to the channels later, or invite the students and staff to add themselves to the channels.

Then, update the links at the top of this page to the project slack channels (in the front matter):

Copy the link to the channel:

<img width="708" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/aa9a8129-336b-4932-a995-cefb34f093bf">

And then configure in the front matter of this page:

```
proj_courses_slack_url: https://ucsb-cs156-f23.slack.com/archives/C066057BBHA
```

Repeat for every project.

# Setting up Kanban boards

To set up Kanban boards for the legacy code project:

1. Make sure your github organization has a suitable template, i.e. a Kanban board set up with the
   views you want.  For example, this one: <https://github.com/orgs/ucsb-cs156-f23/projects/28/views/2>
2. Navigate to the template board so that your screen looks like this:

   <img width="1110" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/876a93c8-3561-4db3-990b-d12b9e37aee4">

3. For each team, click the `Use Template` button, and in the box that comes up, paste in the
   name of the repo for which you are creating a Kanban board; for example, pasting in `proj-happycows-f23-5pm-2` as shown here.  Also be sure that the owner is the github org for the course, e.g. `ucsb-cs156-f23`:

   <img width="608" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/7f49s250-f3c2-45b2-bb7d-8e9b0e6683e5">

   A kanban board will be created:

   <img width="663" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/579e7152-e75a-44d9-a7b8-6ea02cf41943">

   Repeat for each team.  To make this efficient, you may find that hitting the back button gets you back to the page where you can click `Use Template`; have the previous project name in your copy/paste buffer so that all you have to do is change the team number.

5. If you do these operations consecutively, in order from first to last team, you'll get a range of
   project numbers, e.g. twelve projects ranging in number from `43` to `54`.

## Add project numbers (kanban board numbers) to Front matter

Next, put these numbers in the front matter of this page.  For example (only a portion of the yml shown here):

   ```yml
      time: 7pm
      product: proj-courses
      productShort: courses
      teams:
        -
          num: 1
          dokku: "09"
          kanban: 51
        -
          num: 2
          dokku: "10"
          kanban: 52
        -
          num: 3
          dokku: "11"
          kanban: 53
        -
          num: 4
          dokku: "12"
          kanban: 54
   ```

## Link the kanban board to the repos

For each repo, visit the repo page and link the repo to the kanban board.

For example, on the repo page, click the `Projects` link:

<img width="1115" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/bdce9655-1d26-4ff4-8c3d-ad3668b8fbd6">

Find and click the `Link a Project` button:

<img width="276" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/2b65960d-0306-47cb-86ee-3b89bbe0de37">

Use the search box to find the project that matches the repo:

<img width="586" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/dfc5a7d8-80c0-4b96-b026-8ca0585ba951">

Click to link the repo to the project.

## Set access for teams to project

For each project you'll need to set the team to have access.

If you've already configured the kanban board links on this page (following the instructions above), you can use this process to do this efficiently:

1. Open the top of this page in its own browser window
2. Use the "Open link in new tab" to open up each kanban board in its own tab, until you have twelve tabs next to this page, one per kanban board.
3. For each kanban board, set the permissions, then close the tab.

Here's what opening all the tabs looks like:

![open-each-kanban-board](https://github.com/ucsb-cs156/f23/assets/1119017/8de1f0d6-c6c6-41f3-ad15-0b310db37e0a)


Here's what to do on each kanban board:

1. Click `Settings` (upper right)
2. Click `Manage Access` (left navbar)
3. Find the ``Invite Collaborators` search field;  (or copy/paste) the team name (e.g. `f23-5pm-1`) into it
4. Select the team, change `Role` to `Admin` in the dropdown, and click `Invite`

Here's what that looks like:

![set-each-kanban-board-permissions](https://github.com/ucsb-cs156/f23/assets/1119017/c8237706-30bb-4e44-a953-d8c3584f719d)

## Populate repos

Using a script such as the following, populate the repos from the starter code.  Repeat for each project and group of teams.

```sh
#!/bin/bash

teams=" \
 f23-7pm-1 \
 f23-7pm-2 \
 f23-7pm-3 \
 f23-7pm-4"

project=courses
starter=https://github.com/ucsb-cs156/proj-${project}.git

for t in $teams; do
  echo "******* team: $t start ********"
  r=proj-${project}-${t}
  git clone git@github.com:ucsb-cs156-f23/${r}.git
  cd $r
  git checkout -b main
  git pull origin main
  git remote add starter ${starter}
  git pull starter main
  git push origin main
  cd ..
  echo "******* ${t} end ********"
done
```
## Set up Github Pages

For the next step, we suggest opening each repo it its own tab (similar to how we opened a tab for each kanban board above).

For each repo:
* Go to the `Actions` tab
* Select the job `02-gh-pages-rebuild-part-1`
* Trigger it to run manually from the `main` branch

Here's what that looks like.  Note that as shown in the animation, **there is a short delay between when you click to run and when the job shows up**.  Don't make the mistake of being too impatient, and then ending up running the job twice.

![trigger-job-02](https://github.com/ucsb-cs156/f23/assets/1119017/c82ce0a8-9fb4-44e6-b472-a32adb47c46c)

Job 02 should trigger job 04 to run, to build the gh-pages branch; you'll then need to manually enable github pages (which we will do in the next step.)

It is not unusual to have a few failures on the first few runs of job 02 or job 04; just re-run the job if that happens.   If it fails repeatedly, you may have a real problem, but typically just re-running takes care of these as long as the repo is in good shape.

## Enabling github pages

As soon as jobs 02/04 complete (even partially), a gh-pages branch will be established.  You can then enable github pages for each repo by following these steps:

1. Go to `Settings` for the repo (top nav, right most link)
2. Go to `Pages` (left nav, halfway down)
3. Under `Source` select `Deploy from a branch`
4. Under branch select `gh-pages` and for directory select `root`.  If `gh-pages` is not present, wait for job 02 and job 04 to run and establish the branch.

Here's what that looks like:
![setup-github-pages](https://github.com/ucsb-cs156/f23/assets/1119017/e3a7f87c-afe2-4544-9170-9d378d0f7bbc)

## Set link to github pages on repo

For each repo, select the checkbox on the main page to set up a link to the github pages site by following these steps:

1. Navigate to main page of the repo
2. Click the Gear icon at right near top of page next to `About`
3. Click the checkbox on the form next to `Use your GitHub Pages website`

Here's what that looks like:

![link-to-gh-pages-from-home-page](https://github.com/ucsb-cs156/f23/assets/1119017/75c12efc-b94a-466c-95d9-7fc2bf4bbedb)

## Populate the issues

First, check that the issue for the project are the ones you want, i.e. that you've marked
the issues in the starter repo (e.g. <https://github.com/ucsb-cs156/proj-happycows> ) that you want
the students to work on with a tag such as `f23`.

Second, check that workflow 99 has the correct tag in it (near the top).  (We should probably do this before we populate the repos!  If you find that you didn't do this, there's a script below to fix this; or you can just fix it manually in each cloned repo):

Finally, run workflow 99 to populate the issues list:

<img width="1093" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/3d55bbc8-03e8-43e4-84fb-50d29aa3b989">

When it finishes, the issues that were tagged with for example `f23` should appear in the issues list.  Student can then add them to the Kanban board as they see fit.

## Updating the repos

If it's necessary to pull code from the starter repo a second time, this script can be used:

```sh
#!/bin/bash

teams=" \
 f23-5pm-1 \
 f23-5pm-2 \
 f23-5pm-3 \
 f23-5pm-4"

project=happycows
starter=https://github.com/ucsb-cs156/proj-${project}.git

for t in $teams; do
  echo "******* team: $t start ********"
  r=proj-${project}-${t}
  cd $r
  git checkout main
  git pull origin main
  git pull starter main
  git push origin main
  cd ..
  echo "******* ${t} end ********"
done
```
## Special steps per project

#### For courses

You will need to generate a UCSB_API_KEY for each of the teams and share it with them on their slack channel.  They will need this key in order to set up their localhost deployment and their dokku instances.

To create a UCSB_API_KEY, you'll need an account at <https://developer.ucsb.edu>.  To create the key, follow these steps:

First, navigate to the apps page:

<img width="764" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/a718f282-1da5-4584-b2e8-db39f1d8e8fe">

Click `Add App`

Fill in the team name.  You can leave the rest blank, then scroll down to the APIs checkboxes.

<img width="987" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/69b9ba66-bc7d-497a-963c-3f65a3d8b2bf">

Click to choose the APIs to enable.

<img width="916" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/79008e02-2674-40bd-a8b1-639466fc39ee">

Then click "Add App" at the bottom:

<img width="947" alt="image" src="https://github.com/ucsb-cs156/f23/assets/1119017/9a336302-351e-48d7-8785-3663326d1db0">

You will also need to set up a MongoDB database instance (or else give them instructions on how to do it themselves.)


## Updating Slack Channel topics

For each team channel, update the "Topic" to be initially this (changing the link in each case).  This gives you a place to keep track of the total points assigned, and a convenient link to
check the PR queue:
e
```
0/100 pts - PR Queue: https://github.com/ucsb-cs156-f23/proj-happycows-f23-5pm-1/pulls
```

## Cycling through the team channels

Throughout the legacy code phase, the staff should cycle through the 12 to 16 team channels, checking the PR queues.

The pseudocode for the (manual) procedure is something like this:
```
for team in teams:
  From team's slack channel, click link to team's PRs
  for PR in PRS:
     check(PR) (see process below)

def check(PR):
  if PR (is not green on CI) or (does not have a peer code review) or (has other problem preventing staff review)
    add red warning labels as needed; return
  perform code review
  if code review passes:
    assign points (using a gold colored label)
    merge PR
    update topic on team channel
```

When updating the topic of the team channel, add the points in to the `0/100 pts` part.

If it's the first time that the team had a merged PR, add a link to the PRs that were merged (e.g. `https://github.com/ucsb-cs156-m23/proj-gauchoride-m23-9am-1/pulls?q=is%3Apr+is%3Amerged+`, and add a bookmark to the full PR queue on the team channel.

## Setting up Dokku Deployments

We typically set up the following deployments as staff:

* Prod and qa deployments on dokku-00 for the repos in <https://github.com/ucsb-cs156>, e.g.
  * <https://github.com/ucsb-cs156/proj-happycows> as <https://happycows.dokku-00.cs.ucsb.edu> and <https://happycows-qa.dokku-00.cs.ucsb.edu>
  * <https://github.com/ucsb-cs156/proj-organic> as <https://organic.dokku-00.cs.ucsb.edu> and <https://organic-qa.dokku-00.cs.ucsb.edu>
  * <https://github.com/ucsb-cs156/proj-courses> as <https://courses.dokku-00.cs.ucsb.edu> and  <https://courses-qa.dokku-00.cs.ucsb.edu>
* One prod and qa deployment per team
  * The prod deployments are intended to track the main branch.  It would be desirable, if possible, to set up a cron job to automatically deploy these periodically, or a github action that redeploys them whenever a PR is merged to main, if either or both of those can be done without creating a security issue.  The names are, for example:
    *  <https://happycows.dokku-01.cs.ucsb.edu>
    *  <https://happycows.dokku-02.cs.ucsb.edu>
    *  etc.
* The qa deployments are intended for staff use when reviewing PRs.
    *  <https://happycows-qa.dokku-01.cs.ucsb.edu>
    *  <https://happycows-qa.dokku-02.cs.ucsb.edu>
    *  etc.

The students are then encouraged to set up personal deployments using the project name and their github id for personal dev testing, and demoing PRs under review. For example:
*  <https://happycows-cgaucho.dokku-01.cs.ucsb.edu>
*  <https://happycows-ldelplaya.dokku-01.cs.ucsb.edu>
*  etc.

Students may create additional deployments if needed.

## Staff Links

{% for section in page.sections %}
### Section: {{ section.time }} ({{section.product}})

| Team | Repo | Merged PRs |  Open PRs |Github Pages | Kanban | Dokku Prod | Dokku qa | Wf 82 |
|------|------|-----|-----|--------------|--------|------------|----------|----|{% for team in section.teams %}{% capture teamName %}{{site.qxx}}-{{ team.num }}{% endcapture %}{% capture repoName %}{{section.product}}-{{teamName}}{% endcapture %}
|  {{teamName}} |  [ repo ]({{page.githubOrgUrl}}/{{repoName}}) |   [ Merged PRs ]({{page.githubOrgUrl}}/{{repoName}}/pulls?q=is%3Apr+is%3Amerged) |   [ Open PRs ]({{page.githubOrgUrl}}/{{repoName}}/pulls?q=?q=is%3Aopen+is%3Apr) |  [ github pages ]({{page.githubPagesUrl}}/{{repoName}}) | [ kanban ]({{page.githubProjectsUrl}}/{{team.kanban}}) | [ dokku prod ](https://{{section.productShort}}.dokku-{{team.dokku}}.cs.ucsb.edu) | [ dokku qa ](https://{{section.productShort}}-qa.dokku-{{team.dokku}}.cs.ucsb.edu) | [wf 82]({{page.githubOrgUrl}}/{{repoName}}/actions/workflows/82-kanban-slack-update.yml) |{% endfor %}

{% endfor %}





</details>
