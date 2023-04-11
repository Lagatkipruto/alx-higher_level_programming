#!/usr/bin/node
const args = process.argv.slice(2);
const allArgs = args.length;

if (allArgs === 0) {
  console.log('No argument');
} else if (allArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
