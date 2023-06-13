

//https://www.hackerrank.com/challenges/reduced-string/problem?isFullScreen=true

'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'superReducedString' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function superReducedString(s) {
    // Write your code here
    
    s=Array.from(s)
    
    let result= []
    for(let i =0; i<s.length;i++){
    
    console.log(result)
      if(s[i]==result[result.length-1]){
          result.pop()
      }
      else if (result.length==0 || s[i]!=result[result.length-1]){
          result.push(s[i])
      }
    }    
    
   if(result.length==0){
       return "Empty String"
   }
   else{
       return result.join("")
   }

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const s = readLine();

    const result = superReducedString(s);

    ws.write(result + '\n');

    ws.end();
}
