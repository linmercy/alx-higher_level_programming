#!/usr/bin/node

const { argv } = require('node:process');
const arg = argv[2];
const num = parseInt(arg);

if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
