---
layout: default
title: Open Data Policies
---

{% include base.html %}
<ul>{% for document in site.documents %}
  <li>
    <a href="{{ base }}{{ document.permalink }}">{{ document.title }}</a>
  </li>
{% endfor %}</ul>
