#one.py

# There is no main() function in Python
# Instead, everything gets run implicitly
# from the very first line of a file

# In Python, there is a built in variable
# called __name__
# This variable (__name__) gets assigned
# a string, depending on how you are
# running the actual script

# For example,
# if you went to the command line and
# wrote out 'python one.py'
# it will set __name__ = "__main__"
# This lets us use an if-statement
# if __name__ == "__main__":
    # myfunc()

def func():
    print("FUNC() IN ONE.PY")

def function1():
    pass

def function2():
    pass

# print("TOP LEVEL IN ONE.PY")

# if __name__ == '__main__':
#     print('ONE.PY is being run directly!')
# else:
#     print('ONE.PY has been imported!')

# in Python files, the code is structured about
# and then, the " if __name__ == '__main__': "
# statement is used to execute the program
# in a logical way
#
if __name__ == '__main__':
    # RUN THE SCRIPT!
    function2()
    function1()
