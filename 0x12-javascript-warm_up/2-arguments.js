#!/usr/bin/node
/*
   Commandline arguments in js is made possible using the process.argv
   which is an array that contains all arguments of the CLI.

   process.argv[0] contains the absolute path to the node binary file

   process.argv[1] contains the absolute file path to the .js file in
   which the js engine runs.

   so process.argv[2] ... contains users passed in arguments.
*/
if (process.argv.length < 3) {
  console.log('No argument');
} else if (process.argv.length > 3) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
