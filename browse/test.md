---
layout: default
title: Open Data Policies
---

{% include base.html %}

<ul>
{% for state in site.states %}
  {% assign counter = 0 %}
  {% for place in site.places %}
    {% if place.states contains state.state_code %}
      {% assign counter = counter | plus: 1 %}
    {% endif %}
  {% endfor %}
  {% if counter > 0 %}
    <li>
      <a href="{{ state.url }}">{{ state.title }} ({{ counter }})</a>
    </li>
  {% endif %}
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
