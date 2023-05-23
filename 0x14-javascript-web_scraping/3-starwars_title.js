#!/usr/bin/node
const request = require('request');

// Retrieve the movie ID from the command-line argument
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    const title = movie.title;
    console.log(title);
  }
});
