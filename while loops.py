# While Loops
# can be used when you dont know how many loops you need beforehand

total = 0
for x in range(1,5):
	total += x

print(total)

# we can also do this with "while loops"

total1 = 0
w = 1
while w < 5:
	total1 += w
	w += 1

print(total1)

# The line that says "while", it means "check if 'w' 
# less than 5". And when it is, the next two lines
# will initiate. It will keep doing that until that 
# "while" line is not True and it will stop.

###


total2 = 0
k = 2
while k < 4:
	total2 += k
	k += 1

print(total2)

# The way the lines of code under "while" works
# is that the "total2" (which is '0') will get added
# with 'k', and in this case it's '2', so it's 2.
# Then the next line adds 'k' with '1', which makes
# it 3. AND, it goes back and asks "Is 'k' still less
# than 4?", and it (3) still is, so it does the loop again.
# Now at the end of "k += 1", it will become '4', and
# since 4 is not bigger than 4, the loop will stop.
## So basically, all this code here does is add 2 and 3.

###

# Here is an example of "while" using lists
# you want to add these numbers in this list
# but only the positive ones

given_list = [5,4,4,3,1,-2,-3,-5]

total3 = 0
i=0
#this '0' means "the first number/element in the list"
while given_list[i] > 0:
# the ">" is what we use for only getting the numbers
# more than 0, so the positive numbers
# the "[i]" after "given_list" is what place we're on
# in the list (1st place = 0; 2nd = 1)
	total3 += given_list[i]
	i += 1
# "i += 1" is basically just saying "go to the next item
# on the list"
print(total3)

# If we only used "if" instead of "while", all it
# will do is print 5 because of "i=0" and '5'
# is in that 1st (0) spot

# But if there were no negative numbers,
# there will be an IndexError

#given_list2 = [5,4,4,3,1]

#total3 = 0
#i=0
#while given_list2[i] > 0:
	#total3 += given_list[i]
	#i += 1

# This error happens because once we get to '1' in the list,
# which is the 4th index (but 5th in the list),
# when we add "i+=1", it will try to check for the
# 5th index using the "while given list[i]" line,
# where there is nothing.

# We need to add "i < len(given_list2)" after "while", 
# so that it only goes up to whatever the
# length ("len") of the list is. 
# In this case, that "i < len(given_list2)" would
# be the same as "i < 5", because the length of
# this list is only 5 things
### Remember the first index is [0]

given_list2 = [5,4,4,3,1]

total4 = 0
i=0
while i < len(given_list2) and given_list2[i] > 0:
	total4 += given_list2[i]
	i += 1

print(total4)

# We can also use the "for" loops with the first 
# given list, but we need to use the "break" function
# so that it won't count the negative numbers

forgiven_list = [5,4,4,3,1,-2,-3,-5]
totalfor = 0
for element in forgiven_list:
	if element <= 0:
		break
	totalfor += element

print(totalfor)

# The "break" statement also works in "while" loops
# we'll use the same "given_list"

total5 = 0
e = 0
while True:
	# this "while True" means that whatever comes
	# next will always happen
	total5 += given_list[e]
	e += 1
	if given_list[e] <= 0:
		break
	# this means "if whatever number we're on ([e])
	# in the list is less than or equal to '0'",
	# we will "break" the operation

print(total5)

# Ok what if we wanna do only the negative numbers

given_list3 = [7,5,4,4,3,1,-2,-3,-5, -7]

total6 = 0
n = 0
while True:
	total6 += given_list3[n]
	n += 1
	if given_list3[n] >= 0:
		break

print(total6)
# This doesnt work because it will "break" right
# at the start, which will only make '7'

totalneg = 0
for n in given_list3:
	if n > 0:
		n +=1
	else:
		totalneg += n

print(totalneg)

# another way:

wtotalneg = 0
h = len(given_list3) - 1 
	# means "start from the end of the list"
while given_list3[h] < 0:
	# means if the 'h'th number is less than '0'
	wtotalneg += given_list3[h]
		#means add the h'th number to 'wtotalneg'
	h -= 1
		# means go backwards from the list because
		# we started from the end of the list
print(wtotalneg)

#bonus: put the numbers on the same line:

for i in range(3):
    print(i)

#Would look like this: 
#0
#1
#2

# While the following:
for i in range(3):
    print(str(i), end = " ")

# Would look like this: 
# 0 1 2