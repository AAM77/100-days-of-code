# Name:  stop-gninnips-my-sdrow
# Difficulty: 6 kyu
#
# --- sources ---
# Website: CodeWars
# URL: https://www.codewars.com/kata/stop-gninnips-my-sdrow/train/ruby
#
#

##################
#                #
#  Instructions  #
#                #
##################
#
#
# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
#
#
# Examples:
#
# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"

##############
# PSEUDOCODE #
##############
#
# take in a string
# split the string by space
# iterate through the split string array
  # if the length of the word is 5 or greater:
    # reverse it
  # else
    # leave it as is
  # end

# join the string by space and return it.


#############
# SOLUTIONS #
#############

#***********#
# Attempt 1 #
#***********#

def spinWords(string)
  split_str_arr = string.split(" ");
  split_str_arr.map { |word| word.length >= 5 ? word.reverse : word }.join(' ')
end
