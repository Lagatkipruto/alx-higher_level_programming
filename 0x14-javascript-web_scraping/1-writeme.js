#!/usr/bin/node
const fs = require('fs');

// Get the file path from command line arguments
const filePath = process.argv[2];

// Get the string to write from command line arguments
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
