

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
#
# The output should be two capital letters with a dot seperating them.
#
# It should look like this:
#
# Sam Harris => S.H
#
# Patrick Feeney => P.F




# My Solution # 1
def abbrevName(name):
    split_name = []

    for word in name.split():
        split_name.append(word[0].capitalize())

    return '.'.join(split_name)

# My Solution # 2
