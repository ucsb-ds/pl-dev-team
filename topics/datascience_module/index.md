---
parent: Topics
layout: default
title: "datascience module
description:  "The datascience module from Berkeley used in Data 8 style courses"
---


# {{page.title}} - {{page.description}}

CMPSC 5A at UCSB is based on Data 8 from UC Berkeley, which uses a specfic Python library called `datascience`.

That library is *not* part of the usual PrairieLearn (PL) python environment, 
so when you do `import datascience` in a regular question in PL, you typically get
an error message *unless* you are using a specific external grader.


## Warnings

If you see this code in a Python file or Jupyter notebook before the `import datascience` or `from datascience import *` line:

```
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
```

This likely comes from a period during Summer 2025 when the `datascience` library was throwing warnings
about deprecation.   We beleive that starting from version 0.18, this no longer happens, so these warnings can
be removed.