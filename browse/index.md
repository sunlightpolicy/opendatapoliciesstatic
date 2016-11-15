---
layout: default
title: Open Data Policies
---

{% include base.html %}
<ul>
{% for doc in site.documents %}
  <li>
    <!--<a href="{{ base }}{{ doc.permalink }}">{{ doc.title }}</a>-->
    <a href="{{ doc.url }}">{{ site.places[{{doc.place}}].title }} ({{ doc.year }})</a>
    2: {{ doc.place }}
    {% assign docplace = doc.place %}
    3: {{ docplace }}
    4: {{ site.places[docplace] }}
    5: {{ site.places['austin-tx'] }}
    6: {{ site.places['austin-tx'].title }}
  </li>
{% endfor %}
</ul>
