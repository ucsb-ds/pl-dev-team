---
parent: Topics
layout: default
title: "Randomizing"
description:  "Various techniques for randomizing questions"
---

# {{page.title}} - {{page.description}}

## Randomizing the variables used in an answer? 

What if you want to randomize the variables that you are using in a solution?

Here's an example that randomizes three variables and two values in the solution.   

<ul>
   <li>Assign the value <code>{{params.value_0}}</code> to the variable <code>{{params.variable_0}}</code></li>
   <li>Assign the value  <code>{{params.value_1}}</code> to the variable <code>{{params.variable_1}}</code></li>
   <li>Assign the variable  <code>{{params.variable_2}}</code> to the sum of the variables <code>{{params.variable_0}}</code> and <code>{{params.variable_1}}</code> </li>
</ul>


The `server.py` file looks like this:

```
import random
import numpy as np

def generate(data):
    # Your usual variant generation code

    # Choose from among a random set of variable choices
    
    variables = random.choice([
        ["a","b","c"],
        ["x","y","z"],
        ["num1","num2","result"],
        ["item1", "item2","total"],
        ["first","second","sum"],
        ["x1","x2","y"]
    ])

    values = np.arange(1,10)
    np.random.shuffle(values)
    
    # Load up the params
    data["params"]["variable_0"] = variables[0]
    data["params"]["variable_1"] = variables[1]
    data["params"]["variable_2"] = variables[2]
    data["params"]["value_0"] = values.item(0)
    data["params"]["value_1"] = values.item(1)
    
    
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
    {variables[0]} = {values.item(0)}
    {variables[1]} = {values.item(1)}
    {variables[2]} = {variables[0]} + {variables[1]}
    </pre>
    """
```

Then, in `test.py`, we can do:

```
from code_feedback import Feedback
from pl_helpers import name, points
from pl_unit_test import PLTestCase

class Test(PLTestCase):
    
    def setUp(self):
      self.a_actual = getattr(self.st, self.data["params"]["variable_0"]) 
      self.b_actual = getattr(self.st, self.data["params"]["variable_1"])
      self.c_actual = getattr(self.st, self.data["params"]["variable_2"])
      self.a_name = self.data["params"]["variable_0"]
      self.b_name = self.data["params"]["variable_1"]
      self.c_name = self.data["params"]["variable_2"]
      self.a_expected = self.data["params"]["value_0"]
      self.b_expected = self.data["params"]["value_1"]
      self.c_expected = self.data["params"]["value_0"] + self.data["params"]["value_1"]
      Feedback.set_score(0)
    
    
    def check_value(self, name, actual, expected):
      if actual == expected:
        Feedback.set_score(1)
        Feedback.add_feedback(f"The variable {name} is assigned the value {expected}")
      else:
        Feedback.add_feedback(f"You must define a variable named {name} and assign it the value {expected}.")
        
    @points(1)
    @name("Check that the first variable is assigned correctly")
    def test_a(self):
      self.check_value(self.a_name, self.a_actual, self.a_expected)

    @points(1)
    @name("Check that the second variable is assigned correctly")
    def test_b(self):
      self.check_value(self.b_name, self.b_actual, self.b_expected)
      
    @points(3)
    @name("Check that the third variable is assigned correctly")
    def test_c(self):
      self.check_value(self.c_name, self.c_actual, self.c_expected)
```
