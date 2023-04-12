#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDiction = {};
for (const key in dict) {
  if (newDiction[dict[key]] === undefined) {
    newDiction[dict[key]] = [key];
  } else {
    newDiction[dict[key]].push(key);
  }
}
console.log(newDiction);
