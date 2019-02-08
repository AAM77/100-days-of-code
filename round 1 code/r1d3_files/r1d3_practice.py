# Dictionaries are unordered mappings
# for storing objects
# Dictorionaries are, essentially, hashes
# They have key:value pairs

my_dict = ('key1':'value1', 'key2':'value2')
my_dict
#=> ('key1':'value1', 'key2':'value2')

my_dict['key1']
'value1'

prices_lookup = {
    'apples':2.99,
    'oranges':1.99,
    'milk':5.00
    }

prices_lookup['apples']

d = {
    'k1':123,
    'k2'[0,1,2],
    'k3': {
            'insideKey':100
          }
    }

d['k2']
#=> [0, 1, 2]

d['k2'][2]
#=> 2

d['k3']['insideKey']
#=> 100

e = {'key1':['a','b','c']}
e
#=> {'key1':['a','b','c']}

mylist = d['key1']
mylist
#=> ['a', 'b', 'c']

letter = mylist[2]
letter
#=> 'c'

letter.upper()
#=> 'C'

d['key1'][2].upper()
#=> 'C'


f = {
    'k1':100,
    'k2':200,
}

f['k3'] = 300

f
#=> {'k1':100, 'k2':200, 'k3':300}

f['k1'] = 'NEW VALUE'
f
#=> {'k1':'NEW VALUE', 'k2':200, 'k3':300}

d = {'k1':100, 'k2':200, 'k3':300}

d.keys()
#=> dict_keys(['k1', 'k2', k3'])

d.values()
#=> dict_values([100, 200, 300])

d.items()
#=> dict_items([('k1', 100), ('k2', 200), ('k3', 300)])



##########
# TUPLES #
##########

# Tuples are very similar to lists
# Unlike lists, however, Tuples are immutable
# That is, once something is assigned inside of
# a tuple, it cannot be reassigned
# Also, tuples use parenthesis

t = (1,2,3)
mylist = [1,2,3]

type(t)
#=> tuple

type(mylist)
#=> list

len(t)
#=> 3

t = ('one', 2)
t[0]
#=> 'one'

t[-1]
#=> 2

t = ('a', 'a', 'b')
t.count('a')
#=> 2
# returns the number of times it appears

t.index('a')
#=> 0
# returns the first index it occures at


t.index('b')
#=> 2

t = ('a', 'a', 'b')
mylist = [1,2,3]

# lets try to reassign
mylist[0] = 'NEW'
mylist
#=> ['NEW', 2, 3]

t[0] = 'NEW'
#=> TypeError

# So, why are tuples useful?
# Tuples are good for data integrity
# They are great for when we want to pass
# around objects, but do not want them
# to get reassigned accidentally


########
# SETS #
########

# Sets are a way to return unique values of a list or string
set('Mississippi')
#=> {M, i, s, p}

set([1,1,2,3])
#=> {1,2,3}

# we use .add() to add to a set
# if a set already contains the value
# it doesn't add the value and returns
# a list of unique values inside it

########################
# FILE INPUTS & OUTPUS #
########################

# Note practiced this part purely in jupyter notebook
