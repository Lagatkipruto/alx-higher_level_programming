#!/usr/bin/node
function factorial (a) {
  return a === 0 || isNaN(a) ? 1 : a * factorial(a - 1);
}
console.log(factorial(Number(process.argv[2])));
