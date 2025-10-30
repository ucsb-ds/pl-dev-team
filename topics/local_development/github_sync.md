---
parent: "Local Development"
grand_parent: Topics
layout: default
title: "GitHub sync"
description:  "Syncing Your PrairieLearn Course with Remote Git"
---


# Running PrairieLearn Locally with Docker

We edit locally (via Docker) and push to GitHub. Before using PrairieLearn each time, pull the latest changes and then sync inside PL.


## Update your local clone
In your course repository folder:
   ```bash
   git status
   git pull
   ```
This ensures your local files match the remote (e.g., `origin/main`).


## Pull from remote in the PL UI

In the PrairieLearn web interface:
1. Go to your Course.
2. In the left side navigation, click Sync.
3. Confirm the Remote repository (e.g., `git@github.com:PrairieLearn/pl-ucsb-cmpsc5a.git`).
4. Click `Pull from remote git repository` (button next to the remote URL).

This refreshes the course view that PL serves from your mounted repo


## Notes & Tips 
- SSH vs HTTPS: If using `git@github.com:...`, make sure your machine has the right SSH keys set up. HTTPS works fine for public repos.
