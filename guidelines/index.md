---
layout: default
title: Open Data Policy Guidelines
---

{% include base.html %}

{% assign guidelines_by_section = site.guidelines | group_by: "section" %}
{% assign sections = site.data.guideline-sections %}
{% for section in sections %}
  <h2>{{ section[1] }}</h2>
  {% assign section_guidelines = site.guidelines | where: "section", section[0] %}
  <ul>
  {% for guideline in section_guidelines %}
    <li><a href="{{ guideline.url }}">({{ guideline.number }}) {{ guideline.name }}</a></li>
  {% endfor %}
  </ul>
{% endfor %}
