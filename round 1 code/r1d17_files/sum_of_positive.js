// # Name: Sum of Positive
// # Difficulty: 8 kyu
// # --- sources ---
// # Website: CodeWars
// # URL: https://www.codewars.com/kata/sum-of-positive/train/javascript
// #
// #
// #
// ##################
// #                #
// #  Instructions  #
// #                #
// ##################
// #
// #
// # You get an array of numbers, return the sum of all of the positives ones.
// # Example [1,-4,7,12] => 1 + 7 + 12 = 20
// # Note: if there is nothing to sum, the sum is default to 0.
// #
// #
// #
// #
// #
// #
// #
// #
// ##############
// # PSEUDOCODE #
// ##############
// #
// #
// #
// #
// #
// #
// #
// #
// #
// #
//
// ########################
// # JAVASCRIPT SOLUTIONS #
// ########################
//
// #***********#
// # Attempt 1 #
// #***********#
  function positiveSum(arr) {
    total = 0
    for(i=0; i<arr.length; i++) {
      if (arr[i] > 0) {
        total += arr[i]
      }
    }
    return total
  }
