---
parent: Topics
layout: default
title: "Local Development"
description:  "Developing with a local copy of PrairieLearn"
---

# {{page.title}} - {{page.description}}


Use these instructions to launch PrairieLearn on your local machine using Docker.

## Prerequisites 

These are one-time setup steps.

1. **Install Docker Desktop**
   - Download from: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
   - After installation, **start the Docker app** and ensure the whale 🐳 icon is running in your menu bar.

2. **Sign in to Docker**
   ```bash
   docker login
   ```

3. **Clone your course repo**

   Your course repo is, for example:
   * <https://github.com/PrairieLearn/pl-ucsb-cmpsc5a/>
   * <https://github.com/PrairieLearn/pl-ucsb-cmpsc8/>
   * <https://github.com/PrairieLearn/pl-ucsb-cmpsc110/>
   * <https://github.com/PrairieLearn/pl-ucsb-cmpsc156/>
   * etc.
     
   ```bash
   git clone git@github.com:PrairieLearn/pl-ucsb-cmpsc110.git
   cd pl-ucsb-cmpsc110
   ```


## Run PrairieLearn (no external grader)

* Note that many courses *do* use an external grader, including CMPSC 5A.
* For courses with an external grade, follow [these instrucitons instead of this step](https://ucsb-ds.github.io/pl-dev-team/topics/local_development/external_grader.html).

First, cd into the directory where you cloned the PrairieLearn course repo,
and update the main branch.

```bash
cd pl-ucsb-cmpsc110
git pull origin main
```

Then start docker:
```
docker run -it --rm -p 3000:3000 -v `pwd`:/course prairielearn/prairielearn
```

## Access PrairieLearn in Browser

Once you see this message:

```
info: PrairieLearn server ready, press Control-C to quit
info: Go to http://localhost:3000
```

* Open your browser and go to [http://localhost:3000](http://localhost:3000)
* Click the `Load from Disk` button upper right:

  <img width="112" height="34" alt="image" src="https://github.com/user-attachments/assets/497111be-5ce7-4a31-8339-dc2b3d29a69c" />

* After the course loads, click the `Back to Previous Page` button upper left:

  <img width="203" height="43" alt="image" src="https://github.com/user-attachments/assets/a3f6943a-9a82-43dd-9564-0f952cad24f6" />

* Then you should see your course, and be able to try questions.


## Common Error: Docker Daemon Not Running

If you see this error:

```
Cannot connect to the Docker daemon at unix:///Users/.../.docker/run/docker.sock
```

### Solution:
- **Open Docker Desktop** from Applications or Launchpad
- Wait for it to fully start (🐳 whale icon turns green)
- Then retry the `docker run` command


## Note About External Graders

You may see:

```
Running PrairieLearn without support for external graders and workspaces.
```

This is fine for most local testing. To enable full support (e.g., for custom Docker grader images), follow:

[https://prairielearn.readthedocs.io/en/latest/installing/#support-for-external-graders-and-workspaces](https://prairielearn.readthedocs.io/en/latest/installing/#support-for-external-graders-and-workspaces)
