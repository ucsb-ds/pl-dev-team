---
title: Running PrairieLearn Locally with Docker
nav_order: 1
---

# Running PrairieLearn Locally with Docker

Use these instructions to launch PrairieLearn on your local machine using Docker.

---

## Prerequisites

1. **Install Docker Desktop**
   - Download from: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
   - After installation, **start the Docker app** and ensure the whale 🐳 icon is running in your menu bar.

2. **Sign in to Docker**
   ```bash
   docker login
   ```

3. **Clone your course repo**
   ```bash
   git clone https://github.com/YOUR-ORG/YOUR-COURSE-REPO.git
   cd YOUR-COURSE-REPO
   ```

---

## Run PrairieLearn

Use the following command to run PrairieLearn using your local course directory:

```bash
docker run -it --rm -p 3000:3000 -v `pwd`:/course prairielearn/prairielearn
```

> Example:
>
> ```bash
> docker run -it --rm -p 3000:3000 -v ~/iCloudDrive/PL/pl-ucsb-cmpsc5a:/course prairielearn/prairielearn
> ```

---

## Access PrairieLearn in Browser

Once you see this message:

```
info: PrairieLearn server ready, press Control-C to quit
info: Go to http://localhost:3000
```

→ Open your browser and go to [http://localhost:3000](http://localhost:3000)

---

## Common Error: Docker Daemon Not Running

If you see this error:

```
Cannot connect to the Docker daemon at unix:///Users/.../.docker/run/docker.sock
```

### Solution:
- **Open Docker Desktop** from Applications or Launchpad
- Wait for it to fully start (🐳 whale icon turns green)
- Then retry the `docker run` command

---

## Note About External Graders

You may see:

```
Running PrairieLearn without support for external graders and workspaces.
```

This is fine for most local testing. To enable full support (e.g., for custom Docker grader images), follow:

[https://prairielearn.readthedocs.io/en/latest/installing/#support-for-external-graders-and-workspaces](https://prairielearn.readthedocs.io/en/latest/installing/#support-for-external-graders-and-workspaces)
