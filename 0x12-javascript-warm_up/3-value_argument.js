#!/usr/bin/node
/*
   A js script that only prints the first argument passed to it on the
   Terminal.

   Commandline arguments in js is made possible using the process.argv
   which is an array that contains all arguments of the CLI.

   process.argv[0] contains the absolute path to the node binary file

   process.argv[1] contains the absolute file path to the .js file in
   which the js engine runs.

   so process.argv[2] ... contains users passed in arguments.

   Author: Sammykingx
*/
const value = process.argv[2];
if (value === undefined) {
  console.log('No argument');
} else {
  console.log(value);
}
