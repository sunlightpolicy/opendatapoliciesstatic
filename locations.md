---
layout: default
title: Locations
---

{% include base.html %}

update 11

<script>

var docs = {};
{% for doc in site.documents%}
  {% assign docplace = doc.place %}
  if (!('{{docplace}}' in docs)) {
    docs['{{docplace}}'] = [];
  }
  var doc_vars = {
    'year': '{{doc.year}}',
    'means': '{{doc.legal_custom}}',
    'url': '{{doc.path}}'
  };
  docs['{{docplace}}'].push(doc_vars);
{% endfor %}

console.log(docs);

var data = [];


{% for place in site.places %}
  {% if place.x && place.y && (place.type === 'local') %}
    data.push({
      properties: {
        'title': '{{place.title}}',
        'states': '{{place.states | join: '-' }}',
        'docs': docs['{{place.place}}'],
        'place_url': '{{place.path}}'
        // 'Year': '{{document.year}}',
        // 'Legal Means': '{{place.legal_custom}}',
        // 'Policy URL': '{{place.policy_url}}',
        // 'State': '',  // Temporary
        // // 'State': '{{document.map.properties.state}}',
        // // 'State Name': '{{document.map.properties.statename}}',
        // 'City': '{{place.place}}',  // Temporary
        // 'WWC': {{place.wwc}}
      },
      geometry: {
        type: 'Point',
        coordinates: [
          {{place.x}},
          {{place.y}}
        ]
      }
    });
  {% endif %}
{% endfor %}

function show_map(data) {
  console.log(data);

  // (This part isn't necessary anymore because we're not including state shapes)
  // // gets the locations in the geoJSON that have a city property
  // var locations = [];
  // $.each(data, function(key, val) {
  //   if (val['properties'].hasOwnProperty('City') && val['properties']['City'] != '') {
  //     locations.push(val);
  //   }
  // });
  var locations = data;

  // set up map
  var map = L.map('mapid').setView([38, -97], 4);
  var mapLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';
  L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; ' + mapLink + ' Contributors',
    maxZoom: 18
  }).addTo(map);

  // set up icons for markers
  var wwcIcon = L.icon({ iconUrl: '{{base}}/assets/images/pin-wwc.png', iconSize: [24, 38] });
  var odpIcon = L.icon({ iconUrl: '{{base}}/assets/images/pin.png', iconSize: [24, 38]});

  // iterate over locations in geoJSON which have cities (previously extracted above) and create markers
  // on the map. The coordinates are flipped because of translation from lat/lng to x/y coordinates.
  for (var i = 0; i < locations.length; i++) {
    // determine which icon to use based on property in geoJSON using ternary operator (shorthand if/else)
    // var icon = locations[i]['properties']['WWC'] ? wwcIcon : odpIcon;
    var icon = odpIcon;
    // get coordinates of location.
    var coords = locations[i]['geometry']['coordinates'];
    // var mapPinDate = "<time class=\"leaflet-map-date\" datatime=\"" + locations[i]['properties']['Date'] + "\">" + locations[i]['properties']['Date'] + "</time>";
    // var mapPinDate = locations[i]['properties']['Year'];
    var mapPinDate = 'year';  // placeholder
    // var mapPinLinkPolicyURL = "<a class=\"ref-map\" target=\"_blank\" href=\"" + locations[i]['properties']['Policy URL'] + "\">" + locations[i]['properties']['Legal Means'] + " <img class=\"ref-map-link\" src=\"{{base}}/assets//images/arrow-right-redx020.png\" alt=\"Go to WWC Reference Document\" /></a>";
    var mapPinLinkPolicyURL = locations[i].properties.place_url;  // placeholder
    // var mapPinH1 = "<h1 class=\"map-pin-h1\">" + locations[i]['properties']['City'] + ", " + locations[i]['properties']['State'] + "</h1>";
    var mapPinH1 = '<h1 class="map-pin-h1">' + locations[i].properties.title + ', ' + locations[i].properties.states + '</h1>';

    // var mapPinList01 = "<ul class\"xoxo map-pin-list\">";
    var mapPinList01 = "<ul class=\"xoxo map-pin-list\">";
    var mapPinList02 = "<li>" + mapPinH1 + "</li>";
    var mapPinList03 = "<li>" + mapPinDate + "</li>";
    var mapPinList04 = "<li><a href='" + mapPinLinkPolicyURL + "'Link</a></li>";
    // var mapPinList05 = "<li><b>Legal Means</b>: " + locations[i]['properties']['Legal Means'] + "</li>";
    var mapPinListClose = "</ul>";
    var mapPinListContent = mapPinList01 + mapPinList02 + mapPinList03 + mapPinList04 + mapPinListClose;
    var mapPinContent = "<div class=\"map-pin-content\">" + mapPinListContent + "</div>";

    // create marker at specified coordinates (swapped to convert lat/lng to x/y) and add popup on click.
    // var marker = L.marker([coords[1], coords[0]], {icon: icon}).bindPopup('<a href="' + locations[i]['properties']['Policy URL'] + '">Policy Link</a>').addTo(map);
    var marker = L.marker([coords[1], coords[0]], {icon: icon}).bindPopup(mapPinContent).addTo(map);
  }
}

$(document).ready(function(){
/*
  // url to get geoJSON from
  var jsonURL = "{{base}}/assets/js/locations.geojson";
  // get the getJSON from url
  $.getJSON(jsonURL, show_map);
*/
show_map(data);
});

</script>
<div style="padding:0 25px;"><div id="mapid" style="border:1px solid #fff; width:100%; height:500px;"></div></div>
