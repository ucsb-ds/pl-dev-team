---
title: Custom Docker Image
nav_order: 1
layout: default
---

# Custom Docker Images for PrairieLearn Grading

This page documents how to create and use custom Docker images for grading Python-based PrairieLearn questions using the PrairieLearn repository — with support for libraries like [`datascience`](https://www.data8.org), used in CMPSC 5A/5B.

---

## Why Use a Custom Docker Image?

The default PrairieLearn Python grading image does **not** include many libraries needed for data science courses (like `datascience`, `pandas`, etc.). To support these, we build a custom Docker image.

> [Link to list of preinstalled libraries goes here](https://github.com/PrairieLearn/PrairieLearn/blob/master/graders/python/requirements.txt)

---

## Setup Prerequisites

1. **Docker Hub account:** [Create here](https://hub.docker.com)
2. **Install Docker:**  
   - [Mac install guide](https://docs.docker.com/desktop/setup/install/mac-install/)  
   - [Windows install guide](https://docs.docker.com/desktop/setup/install/windows-install/)
3. **Log in via terminal:**

```bash
docker login
```

---

## Cloning & Editing the Grader

We use a forked version of PrairieLearn maintained under the UCSB GitHub organization:  
> But a fresh version can be used from the [PrairieLearn git repo](https://github.com/PrairieLearn/PrairieLearn.git) directly. 

```bash
git clone https://github.com/ucsb-ds/PrairieLearn.git
cd PrairieLearn/graders/python
```

### Modify Python Dependencies

Edit `requirements.txt` to include the libraries your autograders need.  
Make sure to add both the name and version, for example:

```text
datascience==0.10.6
```

If unsure about version, use:

```bash
pip install your-package
pip freeze
```

---

## 🔧 Build and Push the Docker Image

In the `graders/python` directory, run:

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t yourusername/grader-python:latest --push .
```

> 🔥 **Important:** The `--platform linux/amd64` flag is **required** for PrairieLearn compatibility.  
> The `linux/arm64` is optional for Apple Silicon (M1/M2) compatibility.

---

## 📦 Use the Image in PrairieLearn

In any PrairieLearn question that uses Python grading, update the `info.json` to include:

```json
"externalGradingOptions": {
  "enabled": true,
  "image": "yourusername/grader-python:latest",
  "entrypoint": "/python_autograder/run.sh",
  "timeout": 20
}
```

✅ This ensures PrairieLearn will use your custom image when grading.

---

## 👥 Sharing the Docker Image with Team

- Docker images are stored in a **Docker Hub repository**.
- Only the **owner** can manage collaborators.
- Public images can be pulled by anyone, but only collaborators can push.

To add collaborators:
1. Go to [Docker Hub](https://hub.docker.com)
2. Navigate to your image (e.g., `yourusername/grader-python`)
3. Click the **“Collaborators”** tab
4. Add team members by Docker Hub username

> 🧑‍💻 *Note:* Docker does **not** allow creating "Organizations" on free plans (unlike GitHub), so choose a stable personal account as the image owner.

---

## 📚 Background on UCSB Fork

This setup is maintained by the UCSB CS & PSTAT departments for courses like CMPSC 5A and 5B.  
It integrates the [`datascience`](https://www.data8.org) library from UC Berkeley's [Data 8](https://inferentialthinking.com/chapters/intro.html) curriculum.

> The forked repo: [https://github.com/ucsb-ds/PrairieLearn](https://github.com/ucsb-ds/PrairieLearn)


## Updating the custom image

We currently have two custom images that we've been maintaining:
* rachit182/grader-python
* phtcon/grader-python

The intent is to move eventually to one called `ucsb-ds/grader-python` managed by Prof. Conrad, but which he could ostensibly hand off to another faculty member at some point if needed, for continuity that doesn't depend on any single individual.

We needed to update this image because there was a new version of the `datascience` module from UC Berkeley that fixes a deprecation notice.   Here, we document the steps we took.
Later, our intent is to clean up this documentation and turn it into something that's more generic to "how do you keep the docker image up to date".  For today, this is just a brain dump and documenting what we did.

Steps:
1. Open a terminal on a machine where Docker is installed.
2. Do `docker login` to ensure you are logged in
3. cd into a directory where the https://github.com/ucsb-ds/PrairieLearn
4. Be sure that your `origin` remote points to `https://github.com/ucsb-ds/PrairieLearn` by doing `git remote -v`
   For example:
   ```
   % git remote -v
   origin	https://github.com/ucsb-ds/PrairieLearn (fetch)
   origin	https://github.com/ucsb-ds/PrairieLearn (push)
   % 
   ```
5. Be sure that you have a remote that points to the PrairieLearn original repo.  You can add one like this:
   ```
   git remote add PL https://github.com/PrairieLearn/PrairieLearn
   ```
   And then confirm that you have it by using `git remote -v` again.  If you had it already, you don't need to
   add it again.
   ```
   git remote -v
   ```
   % git remote -v
   PL	https://github.com/PrairieLearn/PrairieLearn (fetch)
   PL	https://github.com/PrairieLearn/PrairieLearn (push)
   origin	https://github.com/ucsb-ds/PrairieLearn (fetch)
   origin	https://github.com/ucsb-ds/PrairieLearn (push)
   %
   ```

6. Before making changes to the UCSB specific part of the grader, pull in all of the latest changes from the `PL`
   remote.  The idea is that our UCSB fork is a snapsnot of what the PL repo looked like at a certain point in time,
   but no doubt they continue to make upgrades and changes.  We want ours to stay in sync with those changes, while
   retaining the parts that make it distinct (specficially, maintaining `datascience` in the `requirements.txt` file.

   To start, update the local branch pointers both remotes by doing `git fetch origin` and `git fetch PL`. These
   commands don't touch the file system; they simply update the local repos "branch pointers" that keep track of
   what changes have been made on the remote repos.

   ```
   git fetch PL
   git fetch origin
   ```
7. Now put yourself on the default branch, which is still called `master` rather than `main`

   ```
   git checkout master
   git pull origin master
   ```

   Then, pull in the changes from the PL repo.  You may get merge conflicts, but it is not likely.
   If you do, they should only be in the parts of the repo that have been customized for UCSB, and
   it should be easy to resolve.

   ```
   git pull PL master
   ```
   This command might throw you into an editor such `vim` to enter a commit message.  If you end up in vim, the
   way to save an exit is to press `<esc>` then type `:wq` then press `<enter>`.

8. Now, be sure you know the correct version number for the custom
   requirements you want to include in `graders/python/requirements.txt`

   You can find the correct version number by going into a temporary directory,
   using a `venv`, doing `pip install datascience`, and then `pip freeze > requirements.txt`.  That will give you the
   exact syntax you need for the `requirement.txt` file.

   For example:

   ```
   mkdir temp
   cd temp
   python3 -m venv venv
   source venv/bin/activate
   pip install datascience
   pip freeze > requirements.txt
   cat requirements.txt
   ```

   That last command will display the contents of requirements.txt, and what you are looking for is a line like this:

   ```
   datascience==0.18.0
   ```
   
9. Find the file `datascience==0.18.0 and make the necessary edits in `graders/python/requirements.txt`
10. Make a commit for these edits and push it to the `origin` remote on the `master` branch:

    ```
    git add graders/python/requirements.txt
    git commit -m "pc - add datascience==0.18.0 to requirements.txt"
    git push origin master
    ```
11. Now, we need to create or update our docker images.  In these instructions, we'll update `phtcon/grader-python`.
    

    
