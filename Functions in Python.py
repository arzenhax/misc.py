#Functions are a programmers way of defining deferred, reusable behavior.

# What makes functions different from variables?

## Variables are like boxes you put stuff in.

## Functions are like recepies, like how to bake a cake. But you still need the ingredients even if you have the recipe.
## That means once you have this recepie, you can make the cake over and over again. 
## You also only need to make the cake when it's your birthday, and Functions are like that. 
## Functions don't run until you "call" them in the code.

# Function syntax looks like this:

def some_function(some_input1, some_input2):
  # … do something with the inputs …
  return output

#For example, a function that returns the sum of the first and last elements of a given list might look like this:

def first_plus_last(lst):
  return lst[0] + lst[-1]
#And this would produce output like:

#first_plus_last([1, 2, 3, 4])
#5
#first_plus_last([8, 2, 5, -8])
#0
#first_plus_last([-10, 2, 3, -4])
#-14

#################

# Here is a "to the tenth power" function:

def tenth_power(num):
  ans = num**10
  return ans

print("1 to the 10th power is" ,tenth_power(1))
# 1 to the 10th power is 1
print("0 to the 10th power is" ,tenth_power(0))
# 0 to the 10th power is 0
print("2 to the 10th power is" ,tenth_power(2))
# 2 to the 10th power is 1024

################

# A square_root function:
def square_root(num):
    ans = num**(1/2)
    return ans
# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

##############

# Win_percentage function:
def win_percentage(wins,loses):
  ans = (wins / 10) * 100
  return ans

print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100
print(win_percentage(7, 3))
# should print 70

###############

#Average function:
def average(num1,num2):
  ans = (num1 + num2) / 2
  return ans


print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

##############

#Tip function :
def tip(total,percentage):
  ans = total * (percentage/100)
  return ans
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

###########

#Here is an incorrect function:

def introduction(first_name,last_name):
  return last_name,", ", first_name, " ", last_name
 
print(introduction("James", "Bond"))

# It is supposed to say "Bond, James Bond." but it's all messed up
#This is the correct function:

def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

print(introduction("James", "Bond"))

#The problem is that the incorrect function was using commas instead of plus signs

##########

#This dog years calculator is wrong:
def dog_years(name,age):
  dyears = age*7
  return name + ", you are " + dyears +  "years old in dog years"

#It doesn't work because "dyears" has to be converted into a string (str) from an integer (int) for it to work and show as text.

def dog_years(name,age):
  dyears = age*7
  return name + ", you are " + str(dyears) +  " years old in dog years"

print(dog_years("Lola", 16))

################

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
  
# These 3 lines of code convert Fahrenheit to Celsius. 
## This is a function not a variable because it requires an input
## The first line is to tell the computer what its supposed to calculate.
## The second line is to teach the computer how do solve that calculation.
## The third line is to tell the computer to show the answer when we ask them the first line.

#The parentheses allow you to take in variables from other sources.

def reddit(word):
    print(word)

reddit("Hello World")

#The above requires a variable. If it does not get a variable 
#(in this case it's "word" after "def reddit") then it will error out.

