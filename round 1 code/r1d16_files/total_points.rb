
=begin
  Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the array.

  For example: ["3:1", "2:2", "0:1", ...]

  Write a function that takes such list and counts the points of our team in the championship. Rules for counting points for each match:

  if x>y - 3 points
  if x<y - 0 point
  if x=y - 1 point
  Notes:

  there are 10 matches in the championship
  0 <= x <= 4
  0 <= y <= 4
=end

###################
#  My Pseudocode  #
###################

=begin

#set total = 0
#for each item in the games array:
#split the # before colon and the # after the colon
  # store them into a new array
  #convert the first item in the array to an integer & assign it to x
  #convert the second item in the array to an integer & assign it to y
  # if x > y, total = total + 3
  # if x < y, total = total
  # if x == y, total = total + 1
# once we're done with the list, return the total

=end

def points(games)

  total = 0

  games.each do |game|
    score = game.split(':')
    x = score[0].to_i
    y = score[1].to_i

    if (x > y)
      total += 3
    elsif (x == y)
      total += 1
    end
  end

  return total
end
