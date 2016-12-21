---
layout: default
title: List of all open-data policies
---

{% include base.html %}

These are all the open-data policies we have on this site:

<ul>
{% assign docs = site.documents | sort %}
{% for doc in docs %}
  {% assign the_place = site.places | where: "place", doc.place | first %}
  <li>
    <a href="{{ doc.url }}">{{ the_place.title }}, {{ the_place.states | join: '-' }} — {{ doc.legal_custom }} ({{ doc.year }})</a>
  </li>
{% endfor %}
</ul>
