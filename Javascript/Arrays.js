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

/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/

function getSecondLargest(nums) {
    nums.sort(function(a, b){return b-a});
    var j;
    var first_largest_num, second_largest_num;
    for (j =0; j < nums.length; j++){
        //console.log(nums[j]);
        if(j == 0){
            first_largest_num = nums[j];
        }
        else{
            if(nums[j] < first_largest_num){
                second_largest_num = nums[j];
                break;
            }
        }

    }
    return second_largest_num;
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}