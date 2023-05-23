#!/usr/bin/node
const request = require('request');

function getStatusCode (url) {
  request(url, (error, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}

// Usage: node script.js <url>
const url = process.argv[2];

getStatusCode(url);
