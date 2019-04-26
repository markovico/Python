fruit = "apple"

print(fruit)
print('orange')
print(fruit[0])
print (len(fruit))
print (fruit.upper())

# Concatenating Strings
print(fruit[0] + ' ' + fruit[1] + ' '+ fruit[2] + ' '+fruit[3] + ' '+fruit[4])

# Repeating string
print('-'*10)

print('+'*10)
print('='*10)


# Conversion to String with str()
v = 3
print('Python ' + str(3))


# Formating Strings instead of Concatenating
print('Python {0} {2} {1}' .format('3', 'Version', 'Windows'))

# eliminate str() call when using Format !
print('Python {}' .format(v))

# Location 0 - > 5 places reserved
# Location 1 - > 15 places reserved
# Location 2 - > 10 places reserved
print('{0:5} {1:15} {2:10}' .format('ID', 'Class', 'Item'))
print('{0:5} {1:15} {2:10}' .format('00001', 'Fruit', 'Banana'))

# ^ center < Left(default) > right  ALIGNMENT
print()
print('{0:>5} {1:^15} {2:<10}' .format('ID', 'Class', 'Item'))
print('{0:>5} {1:^15} {2:<10}' .format('00001', 'Fruit', 'Banana'))

# Fractions .2f Two Decimal Places
print()
print('{0:>5} {1:^15} {2:<10} {3:^10}' .format('ID', 'Class', 'Item', 'Price') )
print('{0:>5} {1:^15} {2:<10} {3:^10.2f}' .format('00001', 'Fruit', 'Banana', 1.099))

# User Inputs
# input()
# input('Prompt to Display')
myFruit = input('Enter Fruit : ')
quantity_s = input('Enter Quantity :')
quantity = int(quantity_s)
print('Entered  {0} {1} peaces.' .format(myFruit, quantity))


"""
    Multiple
    Line
    Comments
"""

"""
    Boolean types

    True
    False

    comparators
      ==
      !=
      > <
      >= <=
    Operators
     and
     or
     not
"""

a_boolean = True
b_boolean = False

print('Booleans : {1} {0}.' .format(a_boolean,b_boolean))

"""
    Conditions

    if condition_1 :
        Block 1
    elif condition_2 :
        Block 2
    else
        Block 3
"""


age = int(input('Age :'))
if age>18:
    print("Adult")
elif age>12:
    print("Junior")
else:
    print("Kindergarden")


#
#    Functions
#
#    def functionName(param1, param2, ...):
#       Code block



def myFunction():
    print("My Function got called!")

myFunction()

# Function Paramethers
def myF1(first = 'Joe', last = 'Blow'):
    print('Name : {} {}' .format(first, last))

myF1('Tobias', 'Muller')


# Return from function
def even_odd(num):
    if num%2 == 0:
        return True
    else:
        return False

if even_odd(age):
    print('Age {0} Even!' .format(age))
else:
    print('Age {0} Odd!' .format(age))


# f function on strings
print(f'The {myFruit.upper()} says {quantity} pices')


        
