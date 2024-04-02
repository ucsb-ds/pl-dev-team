---
layout: default
title: "Homework/Participation"
nav_order: 10
---

# {{page.title}}

| Assignment | Description |
|---------|-------|
{% for h in site.hwk %} | [{{h.title}}]({{ h.url | relative_url}}) | {{h.description}} |
{% endfor %}
