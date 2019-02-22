
/*

  Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

  The output should be two capital letters with a dot seperating them.

  It should look like this:

  Sam Harris => S.H

  Patrick Feeney => P.F

*/


# My Solution # 1
function abbrevName(name){
  return name.split(" ").map( w => w[0].toUpperCase() ).join('.')
}
