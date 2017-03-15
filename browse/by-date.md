---
layout: default
title: Browse open-data policies by date
---

{% include base.html %}

These are all the open-data policies we have on this site, listed from oldest to newest:
<br>
{% assign docs_by_year = site.documents | group_by: "year" %}
{% for year in docs_by_year %}
  <h2>{{ year.name }} ({{ year.items | size }} policies)</h2>
  {% assign year_docs = year.items | sort: "date" %}
  <ul>
  {% for doc in year_docs %}
    <li><a href="{{ doc.url }}">{% include docname.html doc_page=doc %}</a></li>
  {% endfor %}
  </ul>
{% endfor %}
