# A "control flow" is kinda like a timeline with multiple splits. If we ask a question "Is today a weekday?",
## The whole day will split and be different depending on if that question is true or false.

# To build control flow into our program, we want to be able to check if something is true or not. 
## A "boolean expression" is a statement that can either be True or False.
## For example, an answer for "Is today a weekday?" in a booleen expression would be: 
"Today is a weekday."
## It can only be true or false
## Subjective statements like 
"Friday is the best day" 
## are not booleen expressions
## This is also a booleen expression: "Sunday starts with the letter 'C'."
## It is still true or false, so it's still a booleen expression

# "Relational Operations" are used to create booleen expressions
## They are also called "Comparators" because they compare two items and "return" either true or false
## The two boolean operators we’ll cover first are:

# Equals: ==
# Not equals: !=

# We can create boolean expressions by comparing two values using these operators:

print(1 == 1)
True
2 != 4
True
3 == 5
False
'7' == 7
False
# This is false because the first 7 is a string in quotes, the other is an integer

###

# when you type True or False in the  editor (with uppercase T and F), 
# they appear in a different color than variables or strings. 
# This is because True and False are their own special type: bool.

# Any variable that is assigned one of these values is called a "boolean variable"
## Boolean variables can be created in several ways. The easiest way is to simply assign True or False to a variable:

set_to_true = True
set_to_false = False

#You can also make a variable equal to a boolean expression.

bool_one = 5 != 7 
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9

#################################################################

# "If" Statements
## Recall the weekday example from the beginning. The decision-making process of “Is it raining? If so, 
## bring an umbrella” is a "Conditional Statement". Here it is phrased in a different way:
"If it is raining then bring an umbrella."
## "it is raining" is the boolean expression, and this conditional statement is checking to see if it is True.
## This is the form of a conditional statement:

## If [it is raining] then [bring an umbrella]
## In Python, it looks very similar:


## if is_raining:
  #bring_umbrella()


## You’ll notice that instead of “then” we have a colon, :. 
## That tells the computer that what’s coming next is what should be executed if the condition is met. 

## Let’s take a look at another conditional statement:


##if 2 == 4 - 2: 
  ##print("apple")


## Will this code print "apple" to the terminal? Yes, because the condition of the if statement, 2 == 4 - 2 is True.
## If it was False, then nothing would happen.

# Here is a function with an if statement inside


#def dave_check(user_name):
  #if user_name = "Dave":
    #return "Get off my computer Dave!"


# This was made because Dave keeps tryna get in my PC. So if Dave enters with his username "Dave", that message will pop up
# But there is actually a Syntax Error here because it only has one equals sign instead of the two, so lets change that

def dave_check(user_name):
  if user_name == "Dave":
    return "Get off my computer Dave!"

# But if we do this:

# dave_check(Dave)

# it still doesnt work because it has no quotes in the name, and were not even printing it, so lets change it

print(dave_check("Dave"))

# But if we use a different name, all that shows up is "None"
# Now Dave is using Angelas user name to log in, so we will put another if statement under the dave_check function

def dave_check(user_name):
  if user_name == "Dave":
    return "Get off my computer Dave!"
  if user_name == "angela_catlady_87":
    return "I know it is you Dave! Go away!"

print(dave_check("angela_catlady_87"))

####################################################################

# Here are more booleen operators:
##Greater than: >
##Less than: <
##Greater than or equal to: >=
##Less than or equal to: <=

#This function checks if our users are over 13 when showing them a PG-13 movie:

def age_check(age):
  if age >= 13:
    return "You can watch this movie."
  if age <= 13:
  	return "You cannot watch this movie."

print(age_check(11))
print(age_check(31))

#Another example, you need 120 credits to graduate:

def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"
  if credits < 120:
  	return "You ain't gon graduate kuh!"

print(graduation_reqs(110))

#############################################

# Often, the conditions you want to check in your conditional statement will require more than one boolean expression to cover. 
## In these cases, you can build larger boolean expressions using boolean operators. 
## These operators (also known as "Logical Operators") combine smaller boolean expressions into larger boolean expressions.
## "and", "or", and "not" are three boleen expressions

# and
## "Oranges are fruits and carrots are vegetables."
## This boolean expression is comprised of two smaller expressions, oranges are a fruit and carrots are a vegetable, 
## both of which are True and connected by the boolean operator "and", so the entire expression is True.

(1 + 1 == 2) and (2 + 2 == 4)

# The left parenthasees and right are both true, and because theyre connected with "and", they 
# count as one, and it counts as "True"

(1 + 1 == 2) and (2 < 1)

# Here, the first parenthases is true while the right is false. But since "and" is there,
# it counts them together, so it counts as "False"

(0 == 10) and (1 + 1 == 1) 

# Here, both parenthases are false so it counts as "False"

# Lets say you also need a 2.0 GPA to graduate. We'll change the function by putting and in the "if" line:

def graduation_reqs(gpa,credits):
  if (credits >= 120) and (gpa >= 2.0):
    return "You meet the requirements to graduate!"

# "or" combines two expressions into a larger expression that is True if either component is True.
## That means even if both statements are true it will still be "True".
## if both are false then it will still be "False"

# Here is an example, if your GPA is higher than 2, or have 120 credits or more, having either will result in "True"

def graduation_mailer(gpa,credits):
  if (gpa >= 2.0) or (credits >=120):
    return True

# "not"
## if we have a True statement and apply a "not" operator we get a False statement.
## In Python "not" is put at the beginning of the statement

not 1 + 1 == 2

# This will be "False" instead of "True" because theres a "not" operator before the statement.

not 7 < 0

# This will be "True"

# Here is the Graduation Function again using "not"

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and (credits < 120):
    return "You do not have enough credits to graduate."
  if (gpa < 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if (not gpa >= 2.0) and (not credits >= 120):
    return "You do not meet either requirement to graduate!"

# Ok theres a lot of "if"s now, its starting to get clunky. This is where "else" comes in.
## "else" tekks code what to do if the conditions are not met in the "if" statement.

#if weekday:
  #wake_up("6:30")
#else:
  #sleep_in()

# "If it's a weekday, wake up 6:30." Instead of putting another "If it isnt, sleep in",
# Just put "Or else, sleep in."

# Instead of putting another "if" statement for not meeting requirements, we can put this instead:

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet the GPA or the credit requirement for graduation."

# elif
## yes that means "else if"
## elif statement checks another condition after the previous if statements conditions aren’t met.
# we can use this to change the order we want the statements to be checked
# "if" is checked first, then "elif", then if none of the conditions are met, "else" is used

def thank_you(donation):
  if donation >= 1000:
    print("Thank you for your donation! You have achieved platinum donation status!")
  if donation >= 500: 
    print("Thank you for your donation! You have achieved gold donation status!")
  if donation >= 100:
    print("Thank you for your donation! You have achieved silver donation status!")
  else:
    print("Thank you for your donation! You have achieved bronze donation status!") 

# This Thank You Function thanks the donator differently based on how much they donated.

# The problem here is that if we donate 1000 or more, ALL of the "if" statements will be printed.
## That is why we use "elif" instead

def thank_you(donation):
  if donation >= 1000:
    print("Thank you for your donation! You have achieved platinum donation status!")
  elif donation >= 500: 
    print("Thank you for your donation! You have achieved gold donation status!")
  elif donation >= 100:
    print("Thank you for your donation! You have achieved silver donation status!")
  else:
    print("Thank you for your donation! You have achieved bronze donation status!") 

# If I donate 600, the code first checks if that is over 1000, and it's not, so it doesn't print the first "if" statem
## then it checks if it’s over $500.00, which it is, so it prints that message, then because all of the other statements are elif and else, 
## none of them get checked and no more messages get printed.

# Heres a Grade Converter Function that changes number grades to letters

def grade_converter(gpa):
  grade = "A", "B", "C", "D", "F"
  if gpa >= 4.0:
    return "A"
  elif gpa >= 3.0:
    return "B"
  elif gpa >= 2.0:
    return "C"
  elif gpa >= 1.0:
    return "D"
  elif gpa >= 0.0:
    return "F"
  return grade

print(grade_converter(0.2))

#"try" and "except"

# try:
    # some statement
# except ErrorName:
    # some statement

# The "try" statement will be excecuted, and if an exception will pop up (like NameError or ValueError)
# the "except" statement will be excecuted instead

# I want to write a function that takes two numbers, "a" and "b" as an input and then returns "a divided by b". 

# def divides(a,b):
	# result = a / b
	# print (result)

# divides(4,0)

# This fuction doesn't work because we can't divide by zero, it will make an error called "ZeroDivisionError"
## "try" and "except" will catch this error.

def divides(a,b):
  try:
    result = a / b
    print (result)
  except ZeroDivisionError:
    print ("Can't divide by zero!")

####

# Lets say the school is looking for applicants with a GPA more than 3, Personal Statement score more than 90, and EC count of more than 3:

def applicant_selector(gpa,ps_score,ec_count):
  if (gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
    return "This applicant should be accepted."

# But they also want people with high GPA and PS to get in, so if their EC count isn't good, they want an interview:

def applicant_selector(gpa,ps_score,ec_count):
  if (gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
    return "This applicant should be accepted."
  elif (gpa >= 3.0) and (ps_score >= 90) and not (ec_count >= 3):
    return "This applicant should be given an in-person interview."

# and then we put an "else" statement for the people who get rejected

def applicant_selector(gpa,ps_score,ec_count):
  if (gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
    return "This applicant should be accepted."
  elif (gpa >= 3.0) and (ps_score >= 90) and not (ec_count >= 3):
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."


###########################################################

# So to review:
## Boolean expressions are statements that can be either True or False
## A boolean variable is a variable that is set to either True or False.
## You can create boolean expressions using relational operators:
## Equals: ==
## Not equals: !=
## Greater than: >
## Greater than or equal to: >=
## Less than: <
## Less than or equal to: <=
## "if" statements can be used to create control flow in your code.
## "else" statements can be used to execute code when the conditions of an "if" statement are not met.
## "elif" statements can be used to build additional checks into your "if" statements
## "try" and "except" statements can be used to build error control into your code.


#nother example
## Over Budget Function

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if budget < (food_bill + electricity_bill + internet_bill + rent):
    return True
  else:
    return False
# Uncomment these function calls to test your over_budget function:
#print(over_budget(100, 20, 30, 10, 40))
# should print False
#print(over_budget(80, 20, 30, 10, 30))
# should print True


# "Is this number divisible by 10" Function

# Write your divisible_by_ten function here:
def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False
# Uncomment these function calls to test your divisible_by_ten function:
#print(divisible_by_ten(20))
# should print True
#print(divisible_by_ten(25))
# should print False

# Movie Review Function

def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif (rating > 5) and (rating < 9):
    return "This one was fun."
  else:
    return "Outstanding!"
# Uncomment these function calls to test your movie_review function:
#print(movie_review(9))
# should print "Outstanding!"
#print(movie_review(4))
# should print "Avoid at all costs!"
#print(movie_review(6))
# should print "This one was fun."

## What is the biggest number function

# Write your max_num function here:
def max_num(num1,num2,num3):
  if (num1 > num2) and (num1 > num3):
    return num1
  elif (num2 > num1) and (num2 > num3):
    return num2
  elif (num1 == num2) or (num1 == num3) or (num2 == num3):
    return "It's a tie!"
  else:
    return num3
# Uncomment these function calls to test your max_num function:
#print(max_num(-10, 0, 10))
# should print 10
#print(max_num(-10, 5, -30))
# should print 5
#print(max_num(-5, -10, -10))
# should print -5
#print(max_num(2, 3, 3))
# should print "It's a tie!"
