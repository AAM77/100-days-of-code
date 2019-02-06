##################################
# Numbers: Simple Arithmetic     #
# Expressions that result in 100 #
##################################

print(23+77)
print((250/5) + (2*25))

########################
# Variable assignments #
# dynamically typed    #
########################

# The following two assignments are valid in python
my_dogs = 2

my_dogs = ["Sammy", "Frankie"]

# dynamic typing is a double edged sword
# it makes variable assignment easier
# BUT: it can also result in unexpected errors
# having to do with incorrect data typing

# this is why the 'type()' function is useful
# here are some examples of how it works:

a = 10
type(a)
#=> int

a = 28.2
type(a)
#=> float


###################
# Strings         #
# string indexing #
# & slicing       #
###################

# Indexing #
new_string = 'Hello World'
new_string[0]
#=> 'H'

new_string[7]
#=> 'o'

# reverse indexing #
new_string[-2]
#=> 'l'

new_string[-4]
#=> 'o'


# Slicing #
second_string = 'abcdefghijk'
second_string[2:]
#=>'cdefghijk'

second_stirng[:3]
#=> 'abc'

second_string[3:6]
#=>'def'

second_string[1:3]
#=> 'bc'

second_string[3:9]
#=> 'defghi'

## slicing step size ##

second_string[::]
#=> 'abcdefghijk'

second_string[::2]
#=> 'acegik'

second_string[::3]
#=> 'adgj'

second_string[2:7:2]
#=> 'ceg'

second_string[::-1]
#=> 'kjihgfedcba'


string_three = 'tinker'
string_three[1:4]

## Strings in Python are immutable ##
# example #
name = 'Pam'

# this is illegal #
name[0] = 'S'
#=> Results in an ERROR. Cannot change (mutate) string.
