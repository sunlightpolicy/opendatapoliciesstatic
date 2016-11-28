---
layout: default
title: List of all open-data policies
---

{% include base.html %}

These are all the open-data policies we have on this site:

<ul>
{% for doc in site.documents %}
  <li>
    <a href="{{ doc.url }}">{{ doc.title }}, {{ doc.states | join: '-' }} — {{ doc.legal_custom }} ({{ doc.year }})</a>
  </li>
{% endfor %}
</ul>
