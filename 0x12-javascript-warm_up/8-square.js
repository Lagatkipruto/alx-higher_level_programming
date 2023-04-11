#!/usr/bin/node
const sizeSqr = Math.floor(Number(process.argv[2]));
if (isNaN(sizeSqr)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < sizeSqr; r++) {
    let row = '';
    for (let c = 0; c < sizeSqr; c++) row += 'X';
    console.log(row);
  }
}
