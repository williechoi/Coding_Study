'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function vowelsAndConsonants(s) {
    var vowels = "aeiou";
    var s_vowels = '';
    var s_consonants = '';
    for (let x of s) {
        if (vowels.includes(x)){
            s_vowels = s_vowels + x;
        }
        else {
            s_consonants = s_consonants + x;
        }
    }
    //console.log(s_vowels)
    //console.log(s_consonants)
    for (let x of s_vowels) {
        console.log(x);
    }
    for (let x of s_consonants) {
        console.log(x);
    }

    
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}