# Name: Sum of Positive
# Difficulty: 8 kyu
# --- sources ---
# Website: CodeWars
# URL: https://www.codewars.com/kata/sum-of-positive/train/ruby
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
# You get an array of numbers, return the sum of all of the positives ones.
#
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
#
# Note: if there is nothing to sum, the sum is default to 0.
#
#
#
#
#
#
##############
# PSEUDOCODE #
##############
#
#
#
#
#
#
#
#


####################
# PYTHON SOLUTIONS #
####################

#***********#
# Attempt 1 #
#***********#
def positive_sum(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total
