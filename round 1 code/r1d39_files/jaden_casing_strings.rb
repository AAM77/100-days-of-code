# Name: Jaden Casing String
# Difficulty: 7 kyu
#
# --- sources ---
# Website: CodeWars
# URL: https://www.codewars.com/kata/jaden-casing-strings/train/ruby
#
#
#
##################
#                #
#  Instructions  #
#                #
##################
#
#
# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word.
#
# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.
#
# Example:
#
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
# Note that the Java version expects a return value of null for an empty string or null.

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
