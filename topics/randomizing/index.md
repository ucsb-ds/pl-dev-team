---
parent: Topics
layout: default
title: "Randomizing"
description:  "Various techniques for randomizing questions"
---

# {{page.title}} - {{page.description}}

## Randomizing the target variable 

You may want to randomize the variable on the left hand side of an assignment statement.

For example, if the question is: 

> Assign the variable `x` to the result of calling the function `foo` with parameter `y`

then the correct answer is: 

```
x = foo(y)
```

But what if you want to randomize the variable on the left, i.e. to select from among `["result", "x", "answer", "a", "value"]`?

Here's an example that randomizes three variables in the solution.  The question is: 

<ul>
  <li>Assign the variable  <code>{{params.variable_2}}</code> to the sum of the variables <code>{{params.variable_0}}</code> and <code>{{params.variable_1}}</code> </li>
</ul>

To randomize these three variables, we use:

```
   variables = random.choice([
        ["a","b","c"],
        ["x","y","z"],
        ["num1","num2","result"],
        ["item1", "item2","total"],
        ["first","second","sum"],
        ["x1","x2","y"]
    ])

    data["params"]["variable_0"] = variables[0]
    data["params"]["variable_1"] = variables[1]
    data["params"]["variable_2"] = variables[2]

    data["params"]["names_from_user"] = [
        {
            "name": variables[0],
            "description": "first variable",
            "type": "int"
        },
        {
            "name": variables[1],
            "description": "second variable",
            "type": "int"
        },
        {
            "name": variables[2],
            "description": "third variable",
            "type": "int"
        },
    ]
    data["params"]["correct"] = f"""
    <pre>
    {variables[2]} = {variables[0]} + {variables[1]}
    </pre>
    """
