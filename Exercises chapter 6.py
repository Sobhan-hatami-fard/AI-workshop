#Exercise 6.2
#(Sum the digits in an integer) Write a function that computes the sum of the digits in an integer. Use the following function header:
#def sumDigits(n):
#For example, sumDigits (234) returns 9 (2+3+4). (Hint: Use the % operator to extract digits, and the //
#operator to remove the extracted digit. For instance, to extract 4 from 234, use 234 % 10 (= 4). To remove 4 from 234, use 234 //
#10 (-23). Use a loop to repeatedly extract and remove the digits until all the digits are extracted.)
#Write a test program that prompts the user to enter an integer and displays the sum of all its digits.

def sumDigits(n):
 sum = 0
 while n > 0:
    digit = n % 10
 sum += digit
 n = n // 10
 return sum
n = int(input("Enter an integer: "))
print("The sum of its digits is", sumDigits(n))

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 6.6
#(Display patterns) Write a function to display a pattern as follows:
#Enter
#1
#2 1
#321
#n n-1 321
#The function header is
#def displayPattern(n):
#Write a test program that prompts the user to enter a number n and invokes displayPattern(n) to display the pattern

def displayPattern(n):
 for i in range(1, n + 1):
  for j in range(n, i - 1, -1):
   print(j, end=" ")
   print()
n = int(input("Enter a number: "))
displayPattern(n)

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 6.16
#(Number of days in a year) Write a function that returns the number of days in a year using the following header:
#def numberOfDaysInAYear (year):
#Write a test program that displays the number of days in the years from 2010 to
#2020

def numberOfDaysInAYear(year):
 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  return 366
 else:
  return 365
for year in range(2010, 2021):
 print(year, "has", numberOfDaysInAYear(year), "days")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 6.17
#(The MyTriangle module) Create a module named MyTriangle that contains
#the following two functions:
#greater than the third side. def isValid(sidel, side2, side3):
#def area(sidel, side2, side3):
#Write a test program that reads three sides for a triangle and computes the area if the input is valid.
#Otherwise, it displays that the input is invalid. The formula for computing the area of a triangle is given in Exercise 2.14. Here are some sample runs:
#Enter three sides in double: 1, 3, 1 Input is invalid
#Enter three sides in double: 1, 1, 1 The area of the triangle is 0.4330127018922193

import math
def isValid(side1, side2, side3):
 return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1
def area(side1, side2, side3):
 s = (side1 + side2 + side3) / 2
 A = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
 return A
side1, side2, side3 = map(float, input("Enter three sides in double: ").split(","))
if isValid(side1, side2, side3):
 print("The area of the triangle is", area(side1, side2, side3))
else:
 print("Input is invalid")

#----------------------------------------------------------------------------------------------------------------------

#Exercise 6.18
#(Display matrix of Os and 1s) Write a function that displays an n-by-n matrix using the following header:
#def printMatrix(n):
#Each element is 0 or 1, which is generated randomly. Write a test program that prompts the user to enter n and displays an n-by-n matrix. Here is a sample run:
#Enter n: 3 F
#010 000
#111

import numpy as np
def printMatrix(n):
 matrix = np.random.randint(0, 2, size=(n, n))
for i in range(n):
 for j in range(n):
  print(matrix[i][j], end=" ")
print()
n = int(input("Enter a number: "))
printMatrix(n)

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 6.27
#(Twin primes) Twin primes are a pair of prime numbers that differ by 2. For example, 3 and 5, 5 and 7, and 11 and 13 are twin primes.
#Write a program to find all twin primes less than 1,000. Display the output as follows:
#(3, 5) (5, 7)..

import math
def isPrime(n):
  if n <= 1:
   return False
   for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
     return False
  return True
def findTwinPrimes(limit):
 twin_primes = []
 for n in range(3, limit - 2, 2):
  if isPrime(n) and isPrime(n + 2):
   twin_primes.append((n, n + 2))
   return twin_primes
limit = 1000
twin_primes = findTwinPrimes(limit)
print(twin_primes)

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 6.28
#(Game: craps) Craps is a popular dice game played in casinos. Write a program to play a variation of the game, as follows
#Roll two dice. Each die has six faces representing values 1. 2, ..., and 6, respectively. Check the sum of the two dice.
#If the sum is 2, 3, or 12 (called craps), you lose; if the sum is 7 or 11 (called natural), you win; if the sum is another value (ie., 4, 5, 6, 8, 9, or 10),
#a point is established. Continue to roll the dice until either a 7 or the same point value is rolled. If 7 is rolled, you lose. Otherwise, you win.
#Your program acts as a single player. Here are some sample runs.
#You rolled S+6-11 You win
#You rolled 12-3 You lost
#You rolled 4+48 point is 8 You rolled 6+2-8 You win
#You rolled 3+2-5 points is 5. You rolled 2+5=7. You lose

import random
def rollDice():
 die1 = random.randint(1, 6)
 die2 = random.randint(1, 6)
 return die1 + die2
def playCraps():
 point = rollDice()
 print("You rolled", point)
if point in (2, 3, 12):
 print("You lose")
elif point in (7, 11):
 print("You win")
else:
 print("Point is", point)
 while True:
  newPoint = rollDice()
  print("You rolled", newPoint)
  if newPoint == point:
   print("You win")
   break
  elif newPoint == 7:
   print("You lose")
   break
playCraps()

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 6.48
#(Format an integer) Write a function with the following header to format the integer with the specified width.
#def format(number, width): The function returns a string for the number with prefix Os.
#The size of the string is the width. For example, format (34, 4) returns "0034" and format (34, 5) returns "00034".
#If the number is longer than the width, the function returns the string representation for the number.
#For example, format(34, 1) returns "34". Write a test program that prompts the user to enter a number and its width and displays a string returned from invoking format (number, width).
#Here is a sample run: Enter an integer: 453 Enter the width: 6 Enter The formatted number is 000453 Enter

def format(number, width):
 s = str(number)
 return s.zfill(width)
number = int(input("Enter an integer: "))
width = int(input("Enter the width: "))
formatted_number = format(number, width)
print("The formatted number is", formatted_number)

#-----------------------------------------------------------------------------------------------------------------------

