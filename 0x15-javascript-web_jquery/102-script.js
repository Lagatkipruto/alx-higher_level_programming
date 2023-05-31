$(document).ready(function() {
    $('#btn_translate').click(function() {
      var languageCode = $('#language_code').val();
      var url = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode;
  
      $.get(url, function(data) {
        $('#hello').text(data.hello);
      });
    });
  });