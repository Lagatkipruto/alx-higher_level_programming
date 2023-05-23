#!/usr/bin/node
const fs = require('fs');

// Get the file path from command line arguments
const filePath = process.argv[2];

// Read the file asynchronously
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err); // Print the error object if an error occurred
  } else {
    console.log(data); // Print the file content
  }
});
