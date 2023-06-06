#Exercise 3.1
#(Geometry: area of a pentagon) Write a program that prompts the user to enter the length from the center of a pentagon to a vertex and computes the area of the pentagon, as shown in the following figure .
#The formula for calculating the area of a pentagon is Area = 3V3 2 s2, where s is the length of a side.
#The side can be calculated using the formula s = 2r sin 5 where r is the length from the center of a pentagon to a vertex.
#Here is a sample run: Enter the length from the center to a vertex: 5.5 The area of the pentagon is 108.61

import math
r = float(input("Enter the length from the center to a vertex: "))
s = 2 * r * math.sin(math.pi / 5)
area = (3 * math.sqrt(3) / 2) * s**2
print("The area of the pentagon is", round(area, 2))

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 3.9
#(Financial application: payroll) Write a program that reads the following information and prints a payroll statement:
#Employee's name (e.g., Smith) Number of hours worked in a week (e.g., 10) Hourly pay rate (e.g., 9.75) Federal tax withholding rate (e.g., 20%) State tax withholding rate (e.g., 9%) A sample run is shown below: Enter employee's name:
#Smith Enter Enter number of hours worked in a week: 10 Enter Enter Enter Enter hourly pay rate: 9.75 Enter Enter federal tax withholding rate: 0.20 Enter state tax withholding rate: 0.09 Employee Name: Smith

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked in a week: "))
pay_rate = float(input("Enter hourly pay rate: "))
federal_rate = float(input("Enter federal tax withholding rate: "))
state_rate = float(input("Enter state tax withholding rate: "))
gross_pay = hours * pay_rate
federal_withholding = gross_pay * federal_rate
state_withholding = gross_pay * state_rate
total_deduction = federal_withholding + state_withholding
net_pay = gross_pay - total_deduction
print("Employee Name:", name)
print("Hours Worked:", hours)
print("Pay Rate: $" + str(pay_rate))
print("Gross Pay: $" + str(gross_pay))
print("Deductions:")
print("\tFederal Withholding (" + str(federal_rate * 100) + "%): $" + str(federal_withholding))
print("\tState Withholding (" + str(state_rate * 100) + "%): $" + str(state_withholding))
print("\tTotal Deduction: $" + str(total_deduction))
print("Net Pay: $" + str(net_pay))

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 4.1
#(Algebra: solve quadratic equations) The two roots of a quadratic equation, for example, ax + bx +0, can be obtained using the following formula:
#-b+ Vb-4ac and r 24 b-4ar is called the discriminant of the quadratic equation. If it is positive, the equation has two real roots.
#If it is zero, the equation has one root. If it is negative. the equation has no real roots Write a program that prompts the user to enter values for a, b, and c and displays the result based on the discriminant.
#If the discriminant is positive, display two roots. If the discriminant is 0, display one root. Leherwise, display The equation has no real roots.
#Here are some sample runs Programming Exercises 121 b2-4ac Enter a, b, c: 1.0, 3, 1 The roots are -0.381966 and -2.61803 Enter a, b, c: 1, 2.0, 15 The root is -1 Enter a, b, c: 1, 2, 3 P The equation has no real roots

import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = b**2 - 4 * a * c
if d > 0:
 r1 = (-b + math.sqrt(d)) / (2 * a)
 r2 = (-b - math.sqrt(d)) / (2 * a)
 print("The roots are", r1, "and", r2)
elif d == 0:
 r = -b / (2 * a)
 print("The root is", r)
else:
 print("The equation has no real roots")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 4.4
#(Game: learn addition) Write a program that generates two integers under 100 and prompts the user to enter the sum of these two integers.
#The program then reports true if the answer is correct, false otherwise.

import random
num1 = random.randint(0, 99)
num2 = random.randint(0, 99)
answer = int(input("What is " + str(num1) + " + " + str(num2) + "? "))
if answer == num1 + num2:
 print("True")
else:
 print("False")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 4.5
#(Game: learn addition) Write a program that generates two integers under 100 and prompts the user to enter the sum of these two integers.
#The program then reports true if the answer is correct, false otherwise. The program is similar to Listing 4.1.
#(Find future dates) Write a program that prompts the user to enter an integer for today's day of the week (Sunday is 0, Monday is 1.' \
#' and Saturday is 6). Also prompt the user to enter the number of days after today for a future day and display the future day of the week. Here is a sample run:
#Enter today's day: 1 Enter Enter the number of days elapsed since today: 3 Today is Monday and the future day is Thursday
#Enter

today = int(input("Enter today's day: "))
elapsed = int(input("Enter the number of days elapsed since today: "))
future = (today + elapsed) % 7
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print("Today is", weekdays[today], "and the future day is", weekdays[future])

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 4.9
#(Financial: compare costs) Suppose you shop for rice and find it in two different-sized packages.
#You would like to write a program to compare the costs of the packages.
#The program prompts the user to enter the weight and price of each package and then displays the one with the better price. Here is a sample run:
#Enter weight and price for package 1: 50, 24.59 Enter weight and price for package 2: 25, 11.99 Package 1 has the better price.
#Enter
#Enter

weight1 = float(input("Enter weight for package 1: "))
price1 = float(input("Enter price for package 1: "))
weight2 = float(input("Enter weight for package 2: "))
price2 = float(input("Enter price for package 2: "))
cost1 = price1 / weight1
cost2 = price2 / weight2
if cost1 < cost2:
 print("Package 1 has the better price.")
elif cost1 > cost2:
 print("Package 2 has the better price.")
else:
 print("The two packages have the same price.")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 4.11
#(Find the number of days in a month) Write a program that prompts the user to enter the month and year and displays the number of days in the month.
#For example, if the user entered month 2 and year 2000, the program should display that February 2000 has 29 days.
#If the user entered month 3 and year 2005, the gram should display that March 2005 has 31 days. pro-

month = int(input("Enter month: "))
year = int(input("Enter year: "))
months = ["January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December"]
days = [31, 28, 31, 30, 31, 30,
31, 31, 30, 31, 30, 31]
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
 days[1] = 29
print(months[month - 1], year, "has", days[month - 1], "days")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 4.17
#(Game: scissor, rock, paper) Write a program that plays the popular scissor-rock-paper game.
#(A scissor can cut a paper, a rock can knock a scissor, and a paper can wrap a rock.) The program randomly generates a number 0, 1, or 2 representing scissor, rock, and paper.
#The program prompts the user to enter a number 0, 1, or 2 and displays a message indicating whether the user or the computer wins, loses, or draws. Here are sample runs:
#scissor (0), rock (1), paper (2): 1 Enter The computer is scissor. You are rock. You won.
#scissor (0), rock (1), paper (2): 2 Enter The computer is paper. You are paper too. It is a draw.

import random
choices = ["scissor", "rock", "paper"]
computer = random.randint(0, 2)
user = int(input("scissor (0), rock (1), paper (2): "))
print("The computer is", choices[computer] + ".")
print("You are", choices[user] + ".")
if computer == user:
 print("It is a draw.")
elif (computer == 0 and user == 1) or (computer == 1 and user == 2) or (computer == 2 and user == 0):
 print("You won.")
else:
 print("You lost.")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 4.18
#(Financials: currency exchange) Write a program that prompts the user to enter the currency exchange rate between U.S.
#dollars and Chinese Renminbi (RMB).
#Prompt the user to enter 0 to convert from U.S. dollars to Chinese RMB and 1 for vice versa. Prompt the user to enter the amount in U.S. dollars or Chinese RMB to convert it to Chinese RMB or U.S. dollars, respectively.
#Here are some sample runs:
#Enter the exchange rate from dollars to RMB: 6.81 Enter 0 to convert dollars to RMB and 1 vice versa: 0 Enter the dollar amount: 100 $100.0 is 681.0 yuan Enter Enter Enter

rate = float(input("Enter the exchange rate from dollars to RMB: "))
option = int(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))
if option == 0:
 amount = float(input("Enter the dollar amount: "))
 print("$" + str(amount), "is", amount * rate, "yuan")
elif option == 1:
 amount = float(input("Enter the RMB amount: "))
 print(str(amount) + " yuan", "is", "$" + str(amount / rate))
else:
 print("Incorrect input")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 4.21
#Write a program that prompts the user to enter a year, month, and day of the month, and then it displays the name of the day of the week. Here are some sample runs:
#Enter year: (e.g., 2008): Enter month: 1-12: 1
#Enter
#Enter the day of the month: 1-31: 25 Day of the week is Friday
#2013
#Enter
#Enter
#Bing, 4:22 PM

year = int(input("Enter year: (e.g., 2008): "))
month = int(input("Enter month: 1-12: "))
day = int(input("Enter the day of the month: 1-31: "))
if month == 1 or month == 2:
 month += 12
year -= 1
century = year // 100
year_of_century = year % 100
h = (day + (26 * (month + 1) // 10) + year_of_century + (year_of_century // 4) + (century // 4) + (5 * century)) % 7
weekdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print("Day of the week is", weekdays[h])

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 4.26
#(Palindrome number) Write a program that prompts the user to enter a three-digit integer and determines whether it is a palindrome number.
#A number is a palindrome if it reads the same from right to left and from left to right.
#Here is a sample run of this program: Enter a three-digit integer: 121 121 is a palindrome Enter a three-digit integer: 123 123 is not a palindrome Enter Enter 127

number = int(input("Enter a three-digit integer: "))
first = number // 100
last = number % 10
if first == last:
 print(number, "is a palindrome")
else:
 print(number, "is not a palindrome")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 4.33
#(Decimal to hex) Write a program that prompts the user to enter an integer between 0 and 15 and displays its corresponding hex number. Here are some sample runs:
#Enter a decimal value (0 to 15): 11 ter The hex value is B
#Enter a decimal value (0 to 15): 5 The hex value is 5
#Enter a decimal value (0 to 15): 31 E Invalid input

decimal = int(input("Enter a decimal value (0 to 15): "))
if 0 <= decimal <= 9:
 print("The hex value is", decimal)
elif 10 <= decimal <= 15:
 letters = ["A", "B", "C", "D", "E", "F"]
 print("The hex value is", letters[decimal - 10])
else:
 print("Invalid input")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 4.34
#(Hex to decimal) Write a program that prompts the user to enter a hex character and displays its corresponding decimal integer. Here are some sample runs:
#Enter a hex character: A The decimal value is 10
#Enter a hex character: a The decimal value is 10
#Enter a hex character: 5 The decimal value is 5

hex = input("Enter a hex character: ")
if "0" <= hex <= "9":
 print("The decimal value is", hex)
elif "A" <= hex.upper() <= "F":
 numbers = [10, 11, 12, 13, 14, 15]
 print("The decimal value is", numbers[ord(hex.upper()) - ord("A")])
else:
 print("Invalid input")

#-----------------------------------------------------------------------------------------------------------------------

