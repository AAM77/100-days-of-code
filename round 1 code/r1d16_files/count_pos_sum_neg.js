// Name: Count of positives / sum of negatives
// Difficulty: 8 kyu
//
// --- sources ---
// Website: CodeWars
// URL: https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives/train/javascript
//
//
//
////////////////////
//                //
//  Instructions  //
//                //
////////////////////

// Given an array of integers.
//
// Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
//
// If the input array is empty or null, return an empty array.
//
// Example
// For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

/////////////////
// PSEUDOCODE //
/////////////////

// # declare a variable count
// # declare a variable totalNeg
// # go through the array
//
// # if the number is positive (greater than 0)
//     # increment count by 1
// # if the number is negative
//     # add it to the total of negatives
//
// # return and array with the first element as the count and the second element as the sum of negatives



///////////////
// SOLUTIONS //
///////////////

//***********//
// Attempt 1 //
//***********//

function countPositivesSumNegatives(input) {
    if (input !== null && input.length > 0) {
      count = 0
      total = 0
      for(let i=0; i<input.length; i++) {
        if (input[i] > 0) {
          count += 1
        } else {
          total += input[i]
        }
      }
      return [count,total]
    } else {
      return []
    }

}
