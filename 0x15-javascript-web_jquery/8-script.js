$(document).ready(function() {
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
      var movies = data.results;
      var listItems = '';
  
      for (var i = 0; i < movies.length; i++) {
        var movie = movies[i];
        listItems += '<li>' + movie.title + '</li>';
      }
  
      $('#list_movies').html(listItems);
    });
  });