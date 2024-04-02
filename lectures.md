---
layout: default
title: "lectures"
nav_order: 30
---

# {{page.title}}

| Lecture | Topic |
|---------|-------|
{% for lecture in site.lectures %} | [{{lecture.title}}]({{ lecture.url | relative_url}}) | {{lecture.description}} |
{% endfor %}
