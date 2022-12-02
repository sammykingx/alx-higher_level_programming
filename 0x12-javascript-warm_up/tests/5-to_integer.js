#!/usr/bin/node
/*
  A JS script that prints My number: <first argument converted in integer>
  of the process.argv array.

  @value: A variable holding the value of the the process.argv at index
          2. then using the Number constructor to change the data type.

  This can be archived using isNaN() method or typeof() However isNaN is
  more suitable for this case.

  Handling float to int i used the bitwise Or operator However parseint()
  works and also the Math.trunc() works.
*/

const value = Number(process.argv[2]);
/* method 1
if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log('My number: ', value | 0);
}
*/

// Method 2

if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log('My number: ', Math.trunc(value));
}
