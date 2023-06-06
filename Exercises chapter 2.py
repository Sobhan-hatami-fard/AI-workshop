#Exercise 2.1
#(Convert Celsius to Fahrenheit) Write a program that reads a Celsius degree from the console and converts it to Fahrenheit and displays the result.
#The formula for the conversion is as follows:
#fahrenheit (9/5) * celsius + 32
#Here is a sample run of the program
#Enter a degree in Celsius: 43 43 Celsius is 109.4 Fahrenheit

celsius = float(input("Enter a degree in Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print(f"{celsius} Celsius is {fahrenheit:.1f} Fahrenheit")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 2.5
#(Financial application: calculate tips)
#Write a program that reads the subtotal and the gratuity rate and computes the gratuity and total.For example,
#if the user enters 10 for the subtotal and 15 % for the gratuity rate, the program displays 1.5 as the gratuity and 11.5 as the total.Here is a sample run: Enter
#the subtotal and a gratuity rate: 15.69, 15 The gratuity is 2.35 and the total is 18.04 Enter

subtotal, rate = input("Enter the subtotal and a gratuity rate: ").split(",")
subtotal = float(subtotal)
rate = float(rate)
gratuity = subtotal * rate / 100
total = subtotal + gratuity
print(f"The gratuity is {gratuity:.2f} and the total is {total:.2f}")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 2.6
#( (Sum the digits in an integer) Write a program that reads an integer between 0 and 1000 and adds all the digits in the integer.
#For example, if an integer is 932, the sum of all its digits is 14. (Hint: Use the % operator to extract digits, and use the // operator to remove the extracted digit.
#For instance, 932 % 10 2 and 932 // = 10 93.) Here is a sample run: Enter a number between 0 and 1000: 999 The sum of the digits is 27 Enter

n = int(input("Enter a number between 0 and 1000: "))
sum = 0
while n > 0:
sum += n % 10
n //= 10
print("The sum of the digits is", sum)

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 2.7
#(Find the number of years and days) Write a program that prompts the user to enter the minutes(e.g., 1 billion), and displays the number of
#years and days for the minutes.For simplicity, assume a year has 365 days.Here is a sample run: Enter Enter the number of minutes: 1000000000 1000000000 minutes is approximately
#1902 years and 214 days

minutes = int(input("Enter the number of minutes: "))
years = minutes // (365 * 24 * 60)
days = (minutes % (365 * 24 * 60)) // (24 * 60)
print(f"{minutes} minutes is approximately {years} years and {days} days")

#-----------------------------------------------------------------------------------------------------------------------

#Exersise 2.8
#(Science: calculate energy) Write a program that calculates the energy needed to heat water from an initial temperature to a final temperature.
#Your program should prompt the user to enter the amount of water in kilograms and the initial and final temperatures of the water.
#The formula to calculate the energy is QM (final Temperature initial Temperature) * 4184 where M is the weight of water in kilograms, temperatures are in degrees Celsius, and energy Q is measured in joules.
#Here is a sample run: Enter the amount of water in kilograms: 55.5 Enter the initial temperature: 3.5 Enter the final temperature: 10.5 The energy needed is 1625484.0 Enter Enter Enter

C = 4184
M = float(input("Enter the amount of water in kilograms: "))
initial_temperature = float(input("Enter the initial temperature: "))
final_temperature = float(input("Enter the final temperature: "))
Q = M * (final_temperature - initial_temperature) * C
print("The energy needed is", Q)

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 2.10
#(Physics: find runway length) Given an airplane's acceleration a and take-offspeed v,you can compute the minimum runway length needed for an airplane totake off using the following formula:
#length=2/2
#Write a program that prompts the user to enter v in meters/second (m/s) and theacceleration a in meters/second squared (m/s2), and displays the minimum runwaylength.Here is a sample run:
#Enter speed and acceleration:60,3.5Enter
#The minimum runway length for this airplane is 514.286 meters

v = float(input("Enter speed in m/s: "))
a = float(input("Enter acceleration in m/s^2: "))
length = v**2 / (2 * a)
print(f"The minimum runway length for this airplane is {length:.3f} meters")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 2.11
#(Financial application: investment amount) Suppose you want to deposit a certain amount of money into a savings account with a fixed annual interest rate.
#What amount do you need to deposit in order to have $5,000 in the account after three years? The initial deposit amount can be obtained using the following formula:
#finalAccountValue
#initialDepositAmount = finalaccountvalue/(1 + monthlyInterest Rate numberOfMonths)
#Write a program that prompts the user to enter the final account value, annual interest rate in percent, and the number of years, and displays the initial deposit amount. Here is a sample run:
#Enter final account value: 1000
#Enter Enter annual interest rate in percent: 4.25 208 9630107431536 Enter
#Enter number of years: 5
#Enter

final_value = float(input("Enter final account value: "))
annual_rate = float(input("Enter annual interest rate in percent: "))
years = int(input("Enter number of years: "))
monthly_rate = annual_rate / 1200
months = years * 12
initial_value = final_value / ((1 + monthly_rate) ** months)
print(f"Initial deposit value is {initial_value:.2f}")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 2.15
#(Geometry: area of a hexagon) Write a program that prompts the user to enter the side of a hexagon and displays its area.
#The formula for calculating the area of a -s, where s is the length of a side.
#Here is a sample run: 3V3 hexagon is Area 2 Enter the side: 5.5 Enter The area of the hexagon is 78.5895

side = float(input("Enter the side: "))
area = (3 * 3 ** 0.5 * side ** 2) / 2
print(f"The area of the hexagon is {area:.4f}")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 2.18
#(Current time) Listing 2.7, ShowCurrentTime.py, gives a program that displays the current time in GMT.
#Revise the program so that it prompts the user to enter the time zone in hours away from (offset to) GMT and displays the time in the specified time zone.
#Here is a sample run: Enter the time zone offset to GMT: -5 The current time is 4:50:34 Enter

offset = int(input("Enter the time zone offset to GMT: "))
currentTime = int(time.time() * 1000)
totalSeconds = int(currentTime / 1000)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = totalHours % 24
currentHour = currentHour + offset
print(f"The current time is {currentHour}:{currentMinute}:{currentSecond}")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 2.24
#2.24 (Turtle: draw four hexagons) Write a program that draws four hexagons in the center of the screen, as shown in Figure 2.4b.

import turtle
t = turtle.Turtle()
def draw_hexagon(side):
    for i in range(6):
        t.forward(side)
t.right(60)
side = 50
t.speed(0)
t.pencolor("black")
t.fillcolor("red")
t.penup()
t.goto(-100, 0)
t.pendown()
t.begin_fill()
draw_hexagon(side)
t.end_fill()
t.penup()
t.goto(-50, -50 * 3 ** 0.5)
t.pendown()
t.begin_fill()
draw_hexagon(side)
t.end_fill()
t.penup()
t.goto(0, 0)
t.pendown()
t.begin_fill()
draw_hexagon(side)
t.end_fill()
t.penup()
t.goto(50, -50 * 3 ** 0.5)
t.pendown()
t.begin_fill()
draw_hexagon(side)
t.end_fill()
turtle.done()

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 2.26
#(Turtle: draw a circle) Write a program that prompts the user to enter the center and radius of a circle,
#and then displays the circle and its area

import turtle
import math
t = turtle.Turtle()
x = float(input("Enter the x-coordinate of the center: "))
y = float(input("Enter the y-coordinate of the center: "))
r = float(input("Enter the radius of the circle: "))
area = math.pi * r ** 2
t.penup()
t.goto(x, y)
t.pendown()
t.circle(r)
t.penup()
t.goto(x, y - r - 20)
t.write(f"The area of the circle is {area:.2f}", align="center", font=("Arial", 16, "normal"))
turtle.done()

#-----------------------------------------------------------------------------------------------------------------------
