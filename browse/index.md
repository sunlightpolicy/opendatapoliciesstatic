---
layout: default
title: Open Data Policies
---

{% include base.html %}

<!-- {% for state in site.states %}
	{% assign state_places = site.places | place.states contains state %}
	{% if state_places.size > 0 %}
		<h3><a href="state.url">{{ state.title }} ({{ state_places.size }})</a></h3>
	{% endif %}
{% endfor %} -->

{% for state in site.states %}
	{% assign state_places = 0 %}
	{% for place in site.places %}
		{% if place.states contains state %}
			{% state_places = state_places + 1 %}
		{% endif %}
	{% endfor %}
	{% if state_places > 0 %}
		<h3><a href="state.url">{{ state.title }} ({{ state_places }})</a></h3>
	{% endif %}
{% endfor %}

<ul>
{% for doc in site.documents %}
  <li>
    <!--<a href="{{ base }}{{ doc.permalink }}">{{ doc.title }}</a>-->
    {% assign the_place = site.places | where: "place", doc.place | first %}
    <a href="{{ doc.url }}">{{ the_place.title }} ({{ doc.year }})</a>
  </li>
{% endfor %}
</ul>
