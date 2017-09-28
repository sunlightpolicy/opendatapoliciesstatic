---
layout: default
title: Open Data Policy Guidelines
---

{% include base.html %}

Simple:

<ul>
{% for guideline in site.guidelines %}
  <li><a href="{{ guideline.url }}">({{ guideline.number }}) {{ guideline.name }}</a></li>
{% endfor %}
</ul>

Grouped:

{% assign guidelines_by_section = site.guidelines | group_by: "section" %}
{% assign sections = site.data.guideline-sections %}
{{ sections }}
{% for section in sections %}
  {{ section }}
{% endfor %}
{% for section in sections %}
  <h2>{{ sections[section] }}</h2>
  {% assign section_guidelines = site.guidelines | where: "section", section %}
  <ul>
  {% for guideline in section_guidelines %}
    <li><a href="{{ guideline.url }}">({{ guideline.number }}) {{ guideline.name }}</a></li>
  {% endfor %}
  </ul>
{% endfor %}
