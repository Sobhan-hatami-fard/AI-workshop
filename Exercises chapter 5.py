#Exercise 5.10
#(Find the highest score) Write a program that prompts the user to enter the number of students and each student's score, and displays the highest score.' \
#' Assume that the input is stored in a file named score.txt, and the program obtains the input from the file.

file = open("score.txt", "r")
num_students = int(file.readline())
highest_score = 0
for i in range(num_students):
 score = int(file.readline())
if score > highest_score:
 highest_score = score
file.close()
print("The highest score is", highest_score)

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 5.11
#(Find the two highest scores) Write a program that prompts the user to enter the number of students and each student's score, and displays the highest and second-highest scores.
# Prompt the user to enter the number of students

num_students = int(input("Enter the number of students: "))
highest_score = 0
second_highest_score = 0
for i in range(num_students):
 score = int(input("Enter a score: "))
if score > highest_score:
 second_highest_score = highest_score
 highest_score = score
elif score > second_highest_score:
 second_highest_score = score
print("The highest score is", highest_score)
print("The second-highest score is", second_highest_score)

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 5.17
#(Display the ASCII character table) Write a program that displays the characters in the ASCII character table from 1 to Display ten characters per line.
#The characters are separated by exactly one space.

CHARS_PER_LINE = 10
count = 0
for code in range(1, 128):
 print(chr(code), end=" ")
count += 1
if count == CHARS_PER_LINE:
 print()
count = 0

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 5.18
#(Find the factors of an integer) Write a program that reads an integer and displays all its smallest factors,
#also known as prime factors. For example, if the input integer is 120, the output should be as follows:
#2, 2, 2, 3, 5

number = int(input("Enter an integer: "))
factor = 2
while number > 1:
 if number % factor == 0:
  print(factor, end=", ")
 number //= factor
else:
 factor += 1

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 5.19
#(Display a pyramid) Write a program that prompts the user to enter an integer from 1 to 15 and displays a pyramid, as shown in the following sample run

n = int(input("Enter an integer from 1 to 15: "))
for i in range(1, n + 1):
 for j in range(n - i):
print("   ", end="")
for j in range(i, 0, -1):
 print(format(j, "3d"), end="")
for j in range(2, i + 1):
 print(format(j, "3d"), end="")
print()

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 5.20
#(Display four patterns using loops) Use nested loops that display the following patterns in four separate programs: Pattern A Pattern B Pattern C Pattern D

class Main {
public static void main(String[] args) {
int rows = 5;
for (int i = 1; i <= rows; ++i) {
for (int j = 1; j <= i; ++j) {
System.out.print(j + " ");
}
System.out.println("");
}
}
}

#Output:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

#To create the patterns you asked for, you can modify the code above by changing the range of the loops, the order of the loops, and the symbols to print.
#Here are some possible solutions:

#Pattern A:

class Main {
public static void main(String[] args) {
int rows = 6;
for (int i = 1; i <= rows; ++i) {
for (int j = 1; j <= i; ++j) {
System.out.print(j + " ");
}
System.out.println("");
}
}
}

#Output:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
#1 2 3 4 5 6

#Pattern B:

class Main {
public static void main(String[] args) {
int rows = 6;
for (int i = rows; i >= 1; --i) {
for (int j = i; j >= 1; --j) {
System.out.print(j + " ");
}
System.out.println("");
}
}
}

#Output:
#6 5 4 3 2 1
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1

#Pattern C:

class Main {
public static void main(String[] args) {
int rows = 6;
for (int i = rows; i >= 1; --i) {
for (int j = rows - i; j >= 1; --j) {
System.out.print(" ");
}
for (int k = i; k >=1 ; --k) {
System.out.print(k);
}
System.out.println("");
}

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 5.27
#(Compute π) You can approximate # by using the following series:
#1 1 + 3 5 π=41 - + + (-1)+1) 2i -1 11 Write a program that displays the value for i = 10000, 20000,..., and 100000.

class Main {
public static void main(String[] args) {
double sum = 0;
int sign = 1;
int n = 10000;
for (int i = 1; i <= 2 * n - 1; i += 2) {
sum += sign * (1.0 / i);
sign *= -1;
}
double pi = 4 * sum;
System.out.println("The value of pi for n = " + n + " is " + pi);
}
}

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 5.29
#(Display leap years) Write a program that displays, ten per line, all the leap years in the twenty - first century (from year 2001 to 2100).The
#years are separated by exactly one space.

def is_leap_year(year):
 return (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0))
count = 0
for year in range(2001, 2101):
 if is_leap_year(year):
    print(year, end=" ")
count += 1
if count == 10:
    print()
count = 0

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 5.30
#(Display the first days of each month) Write a program that prompts the user to enter the year and first day of the year, and displays the first day of each month in the year on the console.
#For example, if the user entered year 2013, and 2 for Tuesday, January 1, 2013, your program should display the following output:
#January 1, 2013 is Tuesday
#December 1, 2013 is Sunday

def get_days_in_month(year, month):
 if month in [1, 3, 5, 7, 8, 10, 12]:
  return 31
 elif month in [4, 6, 9, 11]:
  return 30
 elif month == 2:
   if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return 29
 else:
   return 28
 else:
 return -1

months = ["January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December"]
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
year = int(input("Enter the year: "))
first_day = int(input("Enter the first day of the year (0 for Sunday, ..., 6 for Saturday): "))
for month in range(1, 13):
 print(months[month - 1], "1,", year, "is", weekdays[first_day])
first_day = (first_day + get_days_in_month(year, month)) % 7

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 5.31
#(Display calendars) Write a program that prompts the user to enter the year and first day of the year, and displays on
#the console the calendar table for the year.For example, if the user entered the year 2005, and 6 for Saturday, January 1

def get_days_in_month(year, month):
 if month in [1, 3, 5, 7, 8, 10, 12]:
  return 31
 elif month in [4, 6, 9, 11]:
  return 30
 elif month == 2:
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
   return 29
 else:
  return 28
 else:
 return -1

def print_month_calendar(year, month, start_day):
 months = ["", "January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December"]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print("          ", months[month], year)
print("-------------------------------------")
print(" Sun Mon Tue Wed Thu Fri Sat")
i = 0
while i < start_day:
 print("    ", end = "")
i += 1
i = 1
while i <= get_days_in_month(year, month):
 print(format(i, "4d"), end = "")
if (i + start_day) % 7 == 0:
 print()
i += 1
def print_year_calendar(year, start_day):
 for month in range(1,13):
  print_month_calendar(year, month, start_day)
print()
start_day = (start_day + get_days_in_month(year, month)) % 7
year = int(input("Enter the year: "))
start_day = int(input("Enter the first day of the year (0 for Sunday, ..., and 6 for Saturday): "))
print_year_calendar(year, start_day)

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 5.38
#(Simulation: clock countdown) You can use the time. sleep (seconds) function in the time module to let the program pause for the specified seconds.
#Write a program that prompts the user to enter the number of seconds, displays a message at every second, and terminates when the time expires.
#Here is a sample run: Enter the number of seconds: 3 Enter 2 seconds remaining 1 second remaining Stopped

import time
seconds = int(input("Enter the number of seconds: "))
for i in range(seconds, 0, -1):
 print(i, "second(s) remaining")
time.sleep(1)
print("Stopped")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 5.45
#(Decimal to hex) Write a program that prompts the user to enter a decimal integer and displays its corresponding hexadecimal value

decimal = int(input("Enter a decimal integer: "))
hexadecimal = hex(decimal)
print("The hexadecimal value is", hexadecimal)

#-----------------------------------------------------------------------------------------------------------------------
