# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:

a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.
empty_list = []
for numbers in a_list:
    if numbers < 5:
        empty_list.append(numbers)
print empty_list
Number = int(raw_input("Enter a number."))
for numbers in a_list:
    if numbers < Number:
        print numbers




#Part II
# Take two lists, say for example these two:
b_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

#for numbers in c_list:
    #if numbers == numbers in b_list:
        #print numbers
import random
random1 = random.randint(1,10)
import random
random2 = random.randint(10,20)
import random
random3 = random.randint(20,30)
import random
random4 = random.randint(30,40)
import random
random5 = random.randint(40,50)
import random
random6 = random.randint(50,60)
import random
random7 = random.randint(60,70)
import random
random8 = random.randint(70,80)
import random
random9 = random.randint(80,90)
import random
random10 = random.randint(90,100)
random_list = [random1, random2, random3, random4, random5, random6, random7, random8, random9, random10]
import random
random11 = random.randint(1,10)
import random
random12 = random.randint(10,20)
import random
random13 = random.randint(20,30)
import random
random14 = random.randint(30,40)
import random
random15 = random.randint(40,50)
import random
random16 = random.randint(50,60)
import random
random17 = random.randint(60,70)
import random
random18 = random.randint(70,80)
import random
random19 = random.randint(80,90)
import random
random20 = random.randint(90,100)
random_list2 = [random11, random12, random13, random14, random15, random16, random17, random18, random19, random20]

for numbers in random_list2:
    if numbers == numbers in random_list:
        print numbers

#Part III
# Take a list, say for example this one:

d_list = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# and write a program that replaces all “a” with “*”.
counter = 0
for items in d_list:
    old_name = "a"
    new_name = "*"
    if items == old_name:
        d_list[counter] = new_name
    counter = counter + 1
print d_list





#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.
String = raw_input("Type a string to determine whether it's a palindrome or not.")
String = String.lower()
String_list = []
for letter in String:
    String_list.append(letter)
if String_list[0] == String_list[-1]:
    print "The string is a palindrome."
if String_list[0] != String_list[-1]:
    print "The string isn't a palindrome."








