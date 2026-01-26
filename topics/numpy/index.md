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

## Passing a numpy.ndarray to question.html

If you want a numpy.ndarray to show up in `question.html`, if you try the ordinary thing:

```
data["params"]["values"] = values
```

You get this error:

```
TypeError: Object of type ndarray is not JSON serializable
```

The reason is that the `numpy` library doesn't have code to serialize `numpy.ndarray` objects, and PrairieLearn uses JSON serialization to pass data between `server.py` and `question.html`.

So instead, you can convert to text, and then render the text variable, like this:

```
data["params"]["values_as_text"] = repr(list(map(lambda x: float(x), values)))
```

This:
* converts every `np.float64` value to a regular native Python float value `map(lambda x:float(x), values)`
* converts the map to a list (`list()`)
* converts that list to it's text representation (`repr()`)

You can then use `{{params.values_as_text}}` to show the values in the array in your `question.html`

## Passing a numpy.ndarray to files in `tests`

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

