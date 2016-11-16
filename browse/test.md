---
layout: default
title: Open Data Policies
---

{% include base.html %}

{{ site.states.files }}
<ul>
{% for state in site.states %}
  1: {{ state[0] }}
  2: {{ state.path }}
  {% assign counter = 0 %}
  {% for place in site.places %}
    {% if place.states contains state %}
      {% assign counter = counter | plus: 1 %}
      {{ counter }}
    {% endif %}
  {% endfor %}
  <p>Final: {{ counter }}</p>
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
