$(document).ready(function() {
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
      var translation = data.hello;
      $('#hello').text(translation);
    });
  });