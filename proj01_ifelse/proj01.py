# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

# print "Hello World!"
# fav_color = raw_input("What's your favorite color?")
# fav_number = int(raw_input("What's your fav number?"))
# print "Your fav color is " + fav_color + "."
# print "5 + your favorite number =" + str(5 + fav_number) + "."
Name = raw_input("What's your name?")
Grade = int(raw_input("What grade are you in?"))
print Name + ", you wil graduate from highschool in " + str(13 - Grade) + " years."
# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday


user_number = int(raw_input("Enter a number: "))

if user_number > 5:
    print "Your number is greater than 5!"
elif user_number == 5:
    print "Your number is 5!"
else:
    print "Your number is less than 5!"
Birthmonth = int(raw_input("What month were you born in?"))
Birthday = int(raw_input("What day were you born on?"))
if Birthmonth >= 6:
    Months = str(Birthmonth - 6)
    if Birthday >= 12:
        Day = str(Birthday - 12)
    if Birthday < 12:
        Day = str(31 - 12 + Birthday)
if Birthmonth < 6:
    Months = str(12 - 6 + Birthmonth)
    if Birthday >= 12:
        Day = str(Birthday - 12)
    if Birthday < 12:
        Day = str(31 - 12 + Birthday)
print Name + ", your birthday is in " + str(Months) + " months and " + str(Day) + " days."
# If you complete extensions, describe your extensions here!
Age = int(raw_input("How old are you?"))
if Age < 13:
    print Name + ", you can watch G and PG rated movies."
if Age >= 13 and Age <= 17:
    print Name + ", you can watch G, PG, and PG-13 rated movies."
if Age >= 18:
    print Name + ", you can watch any rating of movies"