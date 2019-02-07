#################
# r1d2 practice #
#################

# strings are not mutable
# you can create comments in Python using the hash '#', followed by the comment


###########
# METHODS #
###########

x = 'Hello World'

x.upper()
#=> HELLO WORLD

x.lower()
#=> hello world

x.split()
#=> ['Hello', 'World']
# splits at each white space, by default

x = 'Hi this is a string'

x.split()
#=> ['Hi', 'this', 'is', 'a', 'string']

x.split('i')
#=> ['H', ' th', 's ', 's a str', 'ng']


##################################
# String formatting for printing #
##################################

# STRING INTERPOLATION #

# There are multiple way to format strings for injecting variables in them

#Two methods include:
# .format()
# f-strings


####################
# .format() method #
####################

print('This is a string {}'.format('INSERTED'))
#=> This is a string INSERTED


print('The {} {} {}'.format('fox', 'brown', 'quick'))
#=> The fox brown quick

# We can rearrange this via indexes by doing the following:
print('The {2} {1} {0}',format('fox', 'brown', 'quick'))
#=> The quick brown fox

# We can also do this:
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
#=> The fox fox fox

# Or, we can do this:
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
#=> The quick brown fox

####################
# float formatting #
####################

# Python provides a relatively easy
# way to format the output of a floating point number

# Example:
 result = 100/777

 result
 #=> 0.1287001287001287

 print("The result was {}".format(result))
 #=> The result was 0.1287001287001287

 # The way we can format is by typing {value:width.precision f}
 # for example, the following yields a number that has a precision of 3.
 print("The result was (r:1.3f)".format(r = result))
 #=> The result was 0.129


 ###################
 # f-string method #
 ###################

 #the f-string method works very similar to
 #string interpolation in Ruby and JavaScript

 #How it works

 name = 'Jose'
 print(f'Hello, his name is {name}')
 #=> Hello, his name is Jose

 name = "Sam"
 age = 3
 print(f'{name} is {age} years old.')

 '{p}'.format(p = 'Python rules!')

 #########
 # LISTS #
 #########

# A list can contain values of the same datatype
 my_list = [1,2,3]

 # or mixed data types
 my_list = ['STRING', 100, 23.2]

 # lists work similar to string in that we can use methods like len()
 len(my_list)
 #=> 3

 mylist = ['one', 'two', 'three']
 mylist[0]
 #=> 'one'

 mylist[1:]
 #=>['twp', 'three']

 # In python, we can concatonate lists

mylist = ['one', 'two', 'three']
anotherlist = ['four', 'five']

mylist + anotherlist
#=> ['one', 'two', 'three', 'four', 'five']

new_list = mylist + anotherlist
new_list[0] = 'ONE ALL CAPS'
#=> ['ONE ALL CAPS', 'two', 'three', 'four', 'five']

# added an item to the end of a list
new_list.append('six')
new_list
#=> ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']

new_list.append('seven')
new_list
#=> ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six', 'seven']

# removes an item from the end of the list
new_list.pop()
new_list
#=> ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']

popped_item = new_list.pop()
popped_item
#=> 'six'

new_list
#=> ['ONE ALL CAPS', 'two', 'three', 'four', 'five']

new_list.pop(0)
#=> 'ONE ALL CAPS'

new_list
#=> ['two', 'three', 'four', 'five']

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,8,3]

new_list.sort()
new_list
#=> ['a', 'b', 'c', 'e', 'x']

#CANNOT do the following, however
my_sorted_list = new_list_sort()
#=> Does not assign the sorted list

type(my_sorted_list)
NoneType


# to get the desired result, we need to do the following:
new_list.sort()
my_sorted_list = new_list
my_sorted_list
#=> ['a', 'b', 'c', 'e', 'x']

num_list.sort()
num_list
#=> [1, 3, 4, 8]

num_list.reverse()
num_list
#=> [8, 4, 3, 2, 1]

# So, lists work similar to strings. The difference, however, is that lists are mutable while strings are immutable. That is, we can change the value at any postion of the list without getting an error.
