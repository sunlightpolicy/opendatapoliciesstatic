---
layout: default
title: Search
---

<div id="results"></div>

<script>
function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

var searchCallback = function() {
    google.search.cse.element.render();
    google.search.cse.element.getelement('search-content').execute( getParameterByName('q') );
};

(function() {
  var cx = '{{ site.google_search_code }}';
  var gcse = document.createElement('script');
  gcse.type = 'text/javascript';
  gcse.async = true;
  gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
  var s = document.getElementById('results');
  s.appendChild(gcse);
})();
</script>
<gcse:search gname="search-content"></gcse:search>