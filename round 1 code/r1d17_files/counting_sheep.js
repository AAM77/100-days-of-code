// Name: Counting Sheep
// Difficulty: 8 kyu
//
// --- sources ---
// Website: CodeWars
// URL: https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/javascript
//
//
//
////////////////////
//                //
//  Instructions  //
//                //
////////////////////

// Consider an array of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
//
// For example,
//
// [true,  true,  true,  false,
//   true,  true,  true,  true ,
//   true,  false, true,  false,
//   true,  false, false, true ,
//   true,  true,  true,  true ,
//   false, false, true,  true]
// The correct answer would be 17.
//
// Hint: Don't forget to check for bad values like null/undefined

/////////////////
// PSEUDOCODE //
/////////////////




///////////////
// SOLUTIONS //
///////////////

//***********//
// Attempt 1 //
//***********//

function countSheeps(arrayOfSheep) {
  let count = 0;
  for(i=0;i<arrayOfSheep.length;i++) {
    if (arrayOfSheep[i] == true) {
      count +=1
    }
  }
  return count
}

//***********//
// Attempt 2 //
//***********//

function countSheeps(arrayOfSheep) {
  return arrayOfSheep.filter(sheep => sheep == true).length
}
