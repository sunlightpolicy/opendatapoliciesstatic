---
layout: default
title: Browse by state
---

{% include base.html %}

Browse the open-data policies listed by state:

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
<!-- The counter is really a counter of places, not docs. Doesn't matter now but could change in the future. -->
