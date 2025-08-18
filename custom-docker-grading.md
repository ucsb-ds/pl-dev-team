---
title: Custom Docker Image
nav_order: 1
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
