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

The parts that you will be familiar with from earlier PL questions are still here: `info.json`, `server.py`, `question.html`.  However, there are some new parts to these files, and some additional files that you need to be aware of.

### `info.json` has new params

For external graders, `info.json` will have a new section in it where you specify that you are using an external grader, and what the docker container is that you are using.   For most standard Python questions that use only built-in python routines and `numpy`, you can use the standard external grader, which uses the following syntax in `info.json`:

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

### `server.py` has new params

`server.py` as usual, will be the place that you do any randomization of the problem.  The purpose of `server.py`, as always, is nothing more and nothing less than loading up the `data["params"]` data structure.   What is different is that while in previous questions, these values were only used to fill in the template in `question.html`, now the values are also passed to the autograder code which is in some new files under a folder called `tests`.

It is important to know that the autograder code is running *in its own separate Python environment* inside the provided docker container.   

To get values from `server.py` to the code inside the `tests` directory, you need to place them inside the `data["params"]` data structure, which involves converting them to JSON and from JSON.   This can get tricky in the case of `numpy` and `datascience` objects; see for example: <https://ucsb-ds.github.io/pl-dev-team/topics/numpy/>

You also may need to define these two variables:

* `data["params"]["names_from_user"]`
* `data["params"]["names_for_user"]`

The `data["params"]["names_from_user"]` object defines names that you want to get from the user code and then test in autograder. For example, if the student is supposed to define a variable called `answer` whose type is a `datascience.Table`, you would write:

```python
data["params"]["names_from_user"] = [
        {
            "name": "answer",
            "description": "new table object with only specific columns",
            "type": "datascience.Table"
        }
    ]
```

On the other hand, if the user is supposed to define a variable called `answer` that is an integer, you might write:

```python
    data["params"]["names_from_user"] = [
        {
            "name": "answer",
            "description": "number of rows in the table",
            "type": "int"
        }
    ]
```

The variable `data["params"]["names_for_user"]` is used to define variables that you making available *to* the student to use in their code. For example, this sets up `cars` as a table they can access:

```python
   data["params"]["names_for_user"] = [
        {
            "name": "cars",
            "description": "variant Table object with all car data",
            "type": "datascience.Table"
        }
    ]
```

TODO: Write more, including an introduction to how to write tests, and also link to the most relevant parts of the PL documentation.
