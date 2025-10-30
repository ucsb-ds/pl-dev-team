---
parent: "Local Development"
grand_parent: Topics
layout: default
title: "Local Development with an External Grader"
description:  "Extra Steps for using an external grader"
---


# {{page.title}} - {{page.description}}


These instructions are based on this guide:
* <https://prairielearn.readthedocs.io/en/latest/installing/#support-for-external-graders-and-workspaces>

## Support for external graders and workspaces¶

There are a few extra steps needed to run PrairieLearn locally with support for external graders and workspaces.

## One time setup: create a directory for sharing job data 

First, create an empty directory to use to share job data between containers. This directory can live anywhere, but needs to be created first and referenced in the Docker launch command. This directory only needs to be created once. 

* On Mac you can create this anywhere.
* If you are running Windows, you should set up WSL (Windows Subsystem for Linux), and then create the directory in the WSL partition.
  
You can create this directory using a command like:

```
mkdir -p "$HOME/pl_ag_jobs"
```

You also need to have done the one time setup steps described here:

* <https://ucsb-ds.github.io/pl-dev-team/topics/local_development/#prerequisites>

## Starting Docker 

Now, we can run PrairieLearn with additional options to allow the external grading or workspaces features. For example, if your course directory is in $HOME/pl-tam212 and 

Suppose the jobs directory created above is in `$HOME/pl_ag_jobs` as indicated above, we use this command to start the docker container. 

First, as with the normal setup, `cd` into the directory where you cloned the PrarieLearn repo, e.g. 


```bash
cd pl-ucsb-cmpsc110
git pull origin main
```

Then start docker with this command:
```
docker run -it --rm -p 3000:3000 \
  -v `pwd`":/course"  \
  -v "$HOME/pl_ag_jobs:/jobs"  \
  -e HOST_JOBS_DIR="$HOME/pl_ag_jobs" \
  -v /var/run/docker.sock:/var/run/docker.sock  \
  --add-host=host.docker.internal:172.17.0.1 
```
