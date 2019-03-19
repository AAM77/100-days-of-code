# Name: Take a Ten Minute Walk
# Difficulty: 6 kyu
#
# --- sources ---
# Website: CodeWars
# URL: https://www.codewars.com/kata/take-a-ten-minute-walk/train/ruby
#
#

##################
#                #
#  Instructions  #
#                #
##################
#
#
# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block in a direction and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.
#
# Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

##############
# PSEUDOCODE #
##############
#
# since each direction of 'n','s','e', and 'w' represents 1 block
  # and each block take 1 minute to traverse
  # an array of 10 cardinal directions will equal to 10 minutes

  # So, first:
    # the walk array needs to have a length of 10


  # Then, we need to make sure that we end up back in the starting position
  # This means that, all of the cardinal directions need to have an equal number of opposite cardinal directions
  # So, second:
  # check that:
    # number of north directions === number of south directions
    # number of east directions === number of west directions


#############
# SOLUTIONS #
#############

#***********#
# Attempt 1 #
#***********#

def isValidWalk(walk)
  if walk.length === 10
    if walk.count('n') === walk.count('s') && walk.count('e') === walk.count('w')
      return true
    end
  end

  false
end
