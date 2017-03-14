---
layout: default
title: Browse open-data policies by date
---

{% include base.html %}

These are all the open-data policies we have on this site, listed from oldest to newest:

<ul>
{% assign docs = site.documents | sort: "date" %}
{% for doc in docs %}
  {% assign the_place = site.places | where: "place", doc.place | first %}
  <li>
    <a href="{{ doc.url }}">{{ the_place.title }}, {{ the_place.states | join: '-' }} — {{ doc.legal_custom }} ({{ doc.date | date: "%b %-d, %Y" }})</a>
  </li>
{% endfor %}
</ul>
