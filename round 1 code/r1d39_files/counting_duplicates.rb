# Name: Counting Duplicates
# Difficulty: 6 kyu
#
# --- sources ---
# Website: CodeWars
# URL: https://www.codewars.com/kata/counting-duplicates/train/ruby
#
#

##################
#                #
#  Instructions  #
#                #
##################
#
#
# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
# 
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice


##############
# PSEUDOCODE #
##############
#
# declare a duplicate_counter variable and assign it a value of 0
# take in the text
# if the text is not empty:
  # change the split_text to all lower case
  # split the downcased text and assign it to a variable
  # iterate through a uniqu-ed list of the split_text
  # for each element in the split_text:
    # use the .count() method to return the number of times the letter appears in the split_text
    # if the count is greater than 1, increment the duplicate_counter by 1
# return the value of the duplicate_counter


#############
# SOLUTIONS #
#############

#***********#
# Attempt 1 #
#***********#

def duplicate_count(text)
  duplicate_letters = 0

  unless text.empty?
    split_text = text.downcase.split('')
    split_text.uniq.each { |l| duplicate_letters += 1 if split_text.count(l) > 1 }
  end

  duplicate_letters
end
