# This Python code is a Temperature Converter. The hashtags will explain how the code works and what they mean.


def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
  
# These 3 lines of code convert Fahrenheit to Celsius. 
## The first line is to tell the computer what its supposed to calculate.
## The second line is to teach the computer how do solve that calculation.
## The third line is to tell the computer to show the answer when we ask them the first line.

### More detailed explanaitions:

# def f_to_c(f_temp) 
## A "function" (thing sthat start with "def") (in this case it's "f_to_c") gets "defined" (using "def") and takes in an "input" (f_temp), which
## is just anything (integers [whole numbers], floats [decimal numbers] or strings [words or text]) that a user or person will 
## put in, that will change or affect the next lines of code.

# c_temp = (f_temp - 32) * 5/9 
## "c_temp" is the "variable" (think of it like an empty box that we're gonna put stuff inside of), 
## and the right side of the equals sign is what is inside the "box". In this case, it's an equation that's gonna
## calculate the Fahrenheit to Celsius. Note that when we used "def" in the previous line, we put an indent using TAB. 
## Indention is very important in coding.

# return c_temp 
## "return" is what gives back or changes the variable (which is "c_temp") to something else, a different
## number. In this case, "return" is used to answer to the equation from line before, which in this case
## converts Fahrenheit "f_temp" to Celsius "c_temp". "return" is used when giving an answer.

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

# Same as the first defined function, just switched Fahrenheit and Celsius

print(c_to_f(23),"Degrees Fahrenheit")

# This is just to "print" out or show what 23 Degrees Celsius is in Fahrenhiet when we run the code.

print(f_to_c(80), "Degrees Celsius")

#It also works for Fahrenheit to Celsius


#####
#In this next part, there will be deliberate mistakes, and how to fix them


def f100_in_celsius():
  f_to_c(100)


# def f100_in_celsius(): 
## Here we are just defining that variable, the next line is the thing that defines it
## Here we define what 100 Degrees Fahrenheit in Celsius is. In the code it's just "f100_in_celsius"
## 

# f_to_c(100) 
## This is a variable that was defined a few lines before, and the 100 is the 
## input that it will take for the equation to compute.

print(f100_in_celsius())

# This code here will only print out "None" because the function "f100_in_celsius" doesn't have a "return".

print(f100_in_celsius)

# This code will only print out a location, which is not what you want to do.
# If you only want to show what 100 Degrees Fahrenheit is in Celsius, just use a variable instead of a function, 
# because it already uses the "f_to_c" function equation, and doesn't have a return.

# So instead of
#	def f100_in_celsius():
#  f_to_c(100)
# You use this:

f100_in_celsius = f_to_c(100)

# And all you have to do is:

print(f100_in_celsius)



