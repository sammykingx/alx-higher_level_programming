#!/usr/bin/node
/*
   Commandline arguments in js is made possible using the process.argv
   which is an array that contains all arguments of the CLI.

   process.argv[0] contains the absolute path to the node binary file

   process.argv[1] contains the absolute file path to the .js file in
   which the js engine runs.

   so process.argv[2] ... contains users passed in arguments.

   for (item in array) starts its count at process.argv[2] and holds the
   indexes

   for (item of process.argv) holds the actual values
*/
for (const element of process.argv) {
  console.log(element);
}
