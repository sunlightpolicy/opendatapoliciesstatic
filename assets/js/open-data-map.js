---
---

// This code is generally a mess and needs cleanup
// It was adapted from a past version

var docs = {};
{% for doc in site.documents %}
  {% assign docplace = doc.place %}
  if (!('{{docplace}}' in docs)) {
    docs['{{docplace}}'] = [];
  }
  var doc_vars = {
    'year': '{{doc.year}}',
    'means': '{{doc.legal_custom}}',
    'doc_page_url': '{{doc.url}}',
    'external_url': '{{doc.policy_url}}'
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
        'place_url': '{{place.url}}'
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
  var wwcIcon = L.icon({ iconUrl: 'http://www.opendatapolicies.org/assets/images/pin-wwc.png', iconSize: [24, 38] });
  var odpIcon = L.icon({ iconUrl: 'http://www.opendatapolicies.org/assets/images/pin.png', iconSize: [24, 38]});

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
    // var mapPinLinkPolicyURL = "<a class=\"ref-map\" target=\"_blank\" href=\"" + locations[i]['properties']['Policy URL'] + "\">" + locations[i]['properties']['Legal Means'] + " <img class=\"ref-map-link\" src=\"{{base}}/assets//images/arrow-right-redx020.png\" alt=\"Go to WWC Reference Document\" /></a>";

    // List of documents for this place
    var place_docs = locations[i].properties.docs;
    place_docs.sort(function (a, b) {
      return b.year - a.year;
    });

    // Generate title and list of docs (and links) for this place's pop-up box
    var pin_title = '<h1 class="map-pin-h1">' + locations[i].properties.title + ', ' + locations[i].properties.states + '</h1>';
    var pin_list = '';
    for (var j = 0; j < place_docs.length; j++) {
      var doc = place_docs[j];
      pin_list += ('<p><a href="' + doc.doc_page_url + '">' + doc.means + ' (' + doc.year + ')</a></p>');
    }
    var pin_content = "<div class=\"map-pin-content\">" + pin_title + pin_list + "</div>";

    // create marker at specified coordinates (swapped to convert lat/lng to x/y) and add popup on click.
    // var marker = L.marker([coords[1], coords[0]], {icon: icon}).bindPopup('<a href="' + locations[i]['properties']['Policy URL'] + '">Policy Link</a>').addTo(map);
    var marker = L.marker([coords[1], coords[0]], {icon: icon}).bindPopup(pin_content).addTo(map);
  }
}

$(document).ready(function () {
/*
  // url to get geoJSON from
  var jsonURL = "{{base}}/assets/js/locations.geojson";
  // get the getJSON from url
  $.getJSON(jsonURL, show_map);
*/
show_map(data);
});
