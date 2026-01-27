---
parent: "Question Types"
grand_parent: Topics
layout: default
title: "External Grader"
description:  "When you want student to write code"
---


# {{page.title}}

<p><b>{{page.description}}</b></p>

We have written quite a few external grader questions for CMPSC 5A at UCSB.

Here's a screenshot of an example:

<img width="771" height="644" alt="image" src="https://github.com/user-attachments/assets/c2c4b87d-96f7-48d4-a3d2-743f4edd724a" />

## Documentation

The documentation for external graders comes in multiple parts:

* [External Grading](https://prairielearn.readthedocs.io/en/latest/externalGrading): High Level Overview
* [Python Autograder](https://prairielearn.readthedocs.io/en/latest/python-grader/): Explains External Grading for Python (we use this in CMPSC 5A)
* [C/C++ Autograder](https://prairielearn.readthedocs.io/en/latest/c-grader/): Explains External Grading for C/C++ (we have not yet used this at UCSB)
* [Java Autograder](https://prairielearn.readthedocs.io/en/latest/java-grader/): Explains External Grading for Java (we have not yet used this at UCSB)

## Structure of an external grader question

The parts that you will be familiar with from earlier PL questions are still here:

* `info.json` will have a new section in it where you specify that you are using an external grader, and what the docker container is that you are using.   For most standard Python questions that use only built-in python routines and `numpy`, you can use the standard external grader, which uses the following syntax in `info.json`:
  ```json
  "gradingMethod": "External",
  "externalGradingOptions": {
    "enabled": true,
    "image": "prairielearn/grader-python",
    "entrypoint": "/python_autograder/run.sh",
    "timeout": 20
  }
  ```
  You can also specify other docker containers here.  For CMPSC 5A/5B questions that use the `datascience` module from UC Berkeley,
  you may need a custom docker image such as this one, which starts with the `prairielearn/grader-python` images and adds the `datascience` library, as explained here: <https://ucsb-ds.github.io/pl-dev-team/topics/custom_docker_image/>
  ```
  "externalGradingOptions": {
    "enabled": true,
    "image": "phtcon/grader-python:latest",
    "entrypoint": "/python_autograder/run.sh",
    "timeout": 20
  }
  ```
