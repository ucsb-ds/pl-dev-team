---
title: "Week 09a - Tue 05/27"
lecture_date: 2025-05-27
description: "Release Notes, Videos"
ready: true
layout: default
parent: lectures
---

# {{page.title}} - {{page.descripion}}

## What to work on this week and next

* Release Notes
* Videos

You can read more about those below.

## But first

* If your team still has open PRs, get them mergable!
* If your team is done with PRs: Your "prod" site is linked in the table here in the `Dokku Prod` column.
* Make sure that all of the features work!
* Look for bugs. If you find bugs, create issues for them, and make PRs to fix them.
* *This is not a loophole to add new features*.  These are only bug fixes.
* Please also create the qa dokku instance if your team hasn't done that yet; those are linked in the `Dokku qa` column. 
* We will be using both the `dokku prod` and the `dokku qa` instances during the final product reviews.

| Team <br ><span style="font-size:80%">Links to Slack</span>| Project <br ><span style="font-size:80%">Links to Legacy Repo</span> | Team Repo | PRs | Github Pages | Kanban | Dokku Prod | Dokku qa |
|------|----|------|-----|--------------|--------|------------|----------|{% for team in site.teams %}{% capture repoName %}proj-{{team.legacy_project}}-{{team.team}}{% endcapture %}
|  [{{team.team}}]({{team.slack}}) | [{{team.legacy_project}}](https://github.com/ucsb-cs156/proj-{{team.legacy_project}}) | [ team repo ]({{page.githubOrgUrl}}/{{repoName}}) |   [ PRs ]({{page.githubOrgUrl}}/{{repoName}}/pulls) |  [ github pages ]({{page.githubPagesUrl}}/{{repoName}}) | [ kanban ]({{page.githubProjectsUrl}}/{{team.legacy_kanban}}) | [ dokku prod ](https://{{team.legacy_project}}.dokku-{{team.dokku}}.cs.ucsb.edu) | [ dokku qa ](https://{{team.legacy_project}}-qa.dokku-{{team.dokku}}.cs.ucsb.edu) |{% endfor %}


## Later this week

* Remember that you have reflections on Thursday (or Monday depending on your team's schedule).


# Final Class Meeting

{% include final_class_meeting.md %}

# Release Notes

{% include release_notes.md %}

# Final Presentation

{% include final_presentation.md %}

# Example Videos

{% include example_videos.md %}

# Final Exam

{% include final_exam.md %}



