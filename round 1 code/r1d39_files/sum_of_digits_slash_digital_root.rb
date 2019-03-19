# Name: Sum of Digits / Digital Root
# Difficulty: 6 kyu
#
# --- sources ---
# Website: CodeWars
# URL: https://www.codewars.com/kata/sum-of-digits-slash-digital-root/train/ruby
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
# In this kata, you must create a digital root function.
#
# A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
#
# Here's how it works:
# 
# digital_root(16)
# => 1 + 6
# => 7
#
# digital_root(942)
# => 9 + 4 + 2
# => 15 ...
# => 1 + 5
# => 6
#
# digital_root(132189)
# => 1 + 3 + 2 + 1 + 8 + 9
# => 24 ...
# => 2 + 4
# => 6
#
# digital_root(493193)
# => 4 + 9 + 3 + 1 + 9 + 3
# => 29 ...
# => 2 + 9
# => 11 ...
# => 1 + 1
# => 2

##############
# PSEUDOCODE #
##############
#
# take in a number
 # declare a sum variable and assign it a value of 0
 # change the number to a string and check its length
 # if the length of the string is 1
   # convert it to a number and return it
 # else
   # iterate through the string
   # convert it to an integer and add it to the sum
 # end

 # Call digital_root(sum) again and pass the sum as its argument


#############
# SOLUTIONS #
#############

#***********#
# Attempt 1 #
#***********#

def digital_root(n)

  sum = 0
  stringed_n = n.to_s

  if stringed_n.length === 1
    n
  else
    stringed_n.split('').each { |num| sum += num.to_i }
    digital_root(sum)
  end
end
