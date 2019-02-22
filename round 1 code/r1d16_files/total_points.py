# THE CHALLENGE

# Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the array.
#
# For example: ["3:1", "2:2", "0:1", ...]
#
# Write a function that takes such list and counts the points of our team in the championship. Rules for counting points for each match:
#
# if x>y - 3 points
# if x<y - 0 point
# if x=y - 1 point
# Notes:
#
# there are 10 matches in the championship
# 0 <= x <= 4
# 0 <= y <= 4


# Solution 1
def total_points(scorelist):
    total = 0;

    for score in scorelist:
        scores = score.split(':')
        x = scores[0]
        y = scores[1]

        if x>y:
            total += 3
        elif x=y:
            total += 1
    return total
