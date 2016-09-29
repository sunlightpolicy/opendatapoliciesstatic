    $(document).ready(function(){
      // url to get geoJSON from
      var jsonURL = "https://raw.githubusercontent.com/sunlightpolicy/opendata/master/USlocalpolicylocations.geoJSON";
      // get the getJSON from url
      $.getJSON(jsonURL, function(data) {

        // gets the locations in the geoJSON that have a city property
        var locations = [];
        $.each(data['features'], function(key, val) {
          if (val['properties'].hasOwnProperty('City') && val['properties']['City'] != '') {
            locations.push(val);
          }
        });

        // set up map
        var map = L.map('mapid').setView([38, -97], 4);
        var mapLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';
        L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          attribution: '&copy; ' + mapLink + ' Contributors',
          maxZoom: 18
        }).addTo(map);

        // set up icons for markers
        var wwcIcon = L.icon({ iconUrl: 'img/pin-wwc.png', iconSize: [24, 38] });
        var odpIcon = L.icon({ iconUrl: 'img/pin.png', iconSize: [24, 38]});

        // iterate over locations in geoJSON which have cities (previously extracted above) and create markers
        // on the map. The coordinates are flipped because of translation from lat/lng to x/y coordinates.
        for (var i = 0; i < locations.length; i++) {
          // determine which icon to use based on property in geoJSON using ternary operator (shorthand if/else)
          var icon = locations[i]['properties']['WWC'] == 'True' ? wwcIcon : odpIcon;
          // get coordinates of location.
          var coords = locations[i]['geometry']['coordinates'];
          var mapPinDate = "<time class=\"leaflet-map-date\" datatime=\"" + locations[i]['properties']['Date'] + "\">" + locations[i]['properties']['Date'] + "</time>"; 
          var mapPinLinkPolicyURL = "<a class=\"ref-map\" target=\"_blank\" href=\"" + locations[i]['properties']['Policy URL'] + "\">" + locations[i]['properties']['Legal Means'] + " <img class=\"ref-map-link\" src=\"../img/arrow-right-redx020.png\" alt=\"Go to WWC Reference Document\" /></a>";
          var mapPinH1 = "<h1 class=\"map-pin-h1\">" + locations[i]['properties']['City'] + ", " + locations[i]['properties']['State'] + "</h1>";
          
          // var mapPinList01 = "<ul class\"xoxo map-pin-list\">";
          var mapPinList01 = "<ul class=\"xoxo map-pin-list\">";
          var mapPinList02 = "<li>" + mapPinH1 + "</li>";
          var mapPinList03 = "<li>" + mapPinDate + "</li>";
          var mapPinList04 = "<li>" + mapPinLinkPolicyURL + "</li>";
          // var mapPinList05 = "<li><b>Legal Means</b>: " + locations[i]['properties']['Legal Means'] + "</li>";
          var mapPinListClose = "</ul>";
          var mapPinListContent = mapPinList01 + mapPinList02 + mapPinList03 + mapPinList04 + mapPinListClose;
          var mapPinContent = "<div class=\"map-pin-content\">" + mapPinListContent + "</div>";
          
          // create marker at specified coordinates (swapped to convert lat/lng to x/y) and add popup on click.
          // var marker = L.marker([coords[1], coords[0]], {icon: icon}).bindPopup('<a href="' + locations[i]['properties']['Policy URL'] + '">Policy Link</a>').addTo(map);
          var marker = L.marker([coords[1], coords[0]], {icon: icon}).bindPopup(mapPinContent).addTo(map);
          
          
        }
      });
    });