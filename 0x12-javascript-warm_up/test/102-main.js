#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(65, function (nb) {
  console.log('New value: ' + nb);
});
