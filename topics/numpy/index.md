---
parent: Topics
layout: default
title: "numpy"
description:  "Working with numpy in PrairieLearn"
---

# {{page.title}} - {{page.description}}

One of the challenges in working with `numpy` in PrairieLearn is serializing numpy data structures such as `numpy.ndarray` instances.

Serializing is necessary when passing data through the `params["data"]` data structure,
this is stored in JSON format.

Here is an example of some code from a `server.py` file that generates a `numpy.ndarray` of `numpy.float64` values, and then serializes them:

```
import numpy as np
import random
import prairielearn

def get_array_of_values():
    return np.random.rand(random.randint(5, 10)) * random.randint(1, 10)

def generate(data):
    values = get_array_of_values()    
    data["params"]["values"] = prairielearn.to_json(values)
```

We need `values` inside the file `tests/setup_code.py`.   To get the values out, we can use this trick:

```
values = data["params"]["values"]["_value"]
```

