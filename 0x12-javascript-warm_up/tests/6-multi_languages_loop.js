#!/usr/bin/node
/*
  Using for loop to print the elements of an array in a single line

  Method 1: Using for of variation of for loop
  Method 2: Using for in variation of for loop
*/
const lang = ['c programming', 'python programming', 'Javasript'];
for (const item of lang) {
  console.log(item);
}
for (const idx in lang) {
  console.log(lang[idx]);
}
