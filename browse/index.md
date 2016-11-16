---
layout: default
title: Open Data Policies
---

{% include base.html %}

<ul>
{% for state in site.states %}
  <li>
    <a href="{{ state.url }}">{{ state.title }}</a>
  </li>
{% endfor %}
</ul>

<!-- <ul>
{% for doc in site.documents %}
  <li>
    {% assign the_place = site.places | where: "place", doc.place | first %}
    <a href="{{ doc.url }}">{{ the_place.title }} ({{ doc.year }})</a>
  </li>
{% endfor %}
</ul> -->
