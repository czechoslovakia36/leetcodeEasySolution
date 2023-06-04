// Birthday Cake Candles
// https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true


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
 * Complete the 'birthdayCakeCandles' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY candles as parameter.
 */

function birthdayCakeCandles(candles) {
    // Write your code here
    
    let count={}
    
    for(let i=0; i< candles.length;i++){
        let value= candles[i]
        
        if(count[value]=count[value]){
            count[value]=count[value]+1
        }
        else{
            count[value]=1
        }
        
    }
    
    let final=[]
    
    for (let key in count){
        final.push(count[key])
    }
    
    
    let max=final[0]
    
    
    for( let j=0; j< final.length;j++){
        if(final[j]>max){
            max=final[j]
        }
    }
    
    return max
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const candlesCount = parseInt(readLine().trim(), 10);

    const candles = readLine().replace(/\s+$/g, '').split(' ').map(candlesTemp => parseInt(candlesTemp, 10));

    const result = birthdayCakeCandles(candles);

    ws.write(result + '\n');

    ws.end();
}
