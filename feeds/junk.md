{% assign sunlight_docs0 = site.documents | where_exp: "item", "item.sunlight == 'nonwwc'" | sort: "date" %}
{% for doc in sunlight_docs0 %}
{{ doc.id }}
{% endfor %}

yeah yeah

{% assign sunlight_docs1 = site.documents | where_exp: "item", "item.sunlight == 'wwc'" | sort: "date" %}
{% for doc in sunlight_docs1 %}
{{ doc.id }}
{% endfor %}

now for real

{% assign acceptable = "wwc,nonwwc" | split: "," %}
{{ acceptable }}
{{ acceptable[0] }}
{{ acceptable[1] }}
{% assign sunlight_docs2 = site.documents | where_exp: "item", "acceptable contains item.sunlight" | sort: "date" %}
{% for doc in sunlight_docs2 %}
{{ doc.id }}
{% endfor %}