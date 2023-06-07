#Exercise 7.2
#(The Stock class) Design a class named Stock to represent a company's stock that contains: A private string data field named symbol for the stock's symbol.
#' A private string data field named name for the stock's name. A private float data field named previousClosingPrice that stores the stock price for the previous day.' \
#' A private float data field named currentPrice that stores the stock price for the current time.' \
#' A constructor that creates a stock with the specified symbol, name, previous price, and current price.' \
#' A get method for returning the stock name. A get method for returning the stock symbol.' \
#' Get and set methods for getting/setting the stock's previous price. Get and set methods for getting/setting the stock's current price.' \
#' A method named getChangePercent () that returns the percentage changed from previous closing price to current price.' \
#' Draw the UML diagram for the class, and then implement the class.' \
#' Write a test program that creates a Stock object with the stock symbol INTC, the name Intel Corporation, the previous closing price of 20.5, and the new current price of 20.35, and display the price-change percentage.

class Stock:
 def __init__(self, symbol, name, previousClosingPrice, currentPrice):
  self.__symbol = symbol
  self.__name = name
  self.__previousClosingPrice = previousClosingPrice
  self.__currentPrice = currentPrice
def getName(self):
 return self.__name
def getSymbol(self):
 return self.__symbol
def getPreviousClosingPrice(self):
 return self.__previousClosingPrice
def setPreviousClosingPrice(self, previousClosingPrice):
 self.__previousClosingPrice = previousClosingPrice
def getCurrentPrice(self):
 return self.__currentPrice
def setCurrentPrice(self, currentPrice):
 self.__currentPrice = currentPrice
def getChangePercent(self):
 changePercent = (self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice * 100
 return changePercent
stock = Stock("INTC", "Intel Corporation", 20.5, 20.35)
print("Stock name:", stock.getName())
print("Stock symbol:", stock.getSymbol())
print("Previous closing price:", stock.getPreviousClosingPrice())
print("Current price:", stock.getCurrentPrice())
print("Price-change percentage:", format(stock.getChangePercent(), ".2f"), "%")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 7.3
#(The Account class) Design a class named Account that contains: A private int data field named id for the account.
#A private float data field named balance for the account. A private float data field named annual InterestRate that stores the current interest rate.
#A constructor that creates an account with the specified id (default 0), initial balance (default 100), and annual interest rate (default 0).
#The accessor and mutator methods for id, balance, and annual interest rate. A method named getMonthlyInterest Rate that returns the monthly interest rate.
#A method named getMonthlyInterest() that returns the monthly interest. A method named withdraw that withdraws a specified amount from the account.
#A method named deposit that deposits a specified amount to the account. Draw the UML diagram for the class, and then implement the class.
#(Hint: The method getMonthlyInterest() is to return the monthly interest amount, not the interest rate. Use this formula to calculate the monthly interest: balance * monthlyInterestRate.
#monthlyInterestRate is annual InterestRate / 12. Note that annual InterestRate is a percent (like 4.5%).
#You need to divide it by 100.) Write a test program that creates an Account object with an account id of 1122, a balance of $20,000, and an annual interest rate of 4.5%.
#Use the withdraw method to withdraw $2,500, use the deposit method to deposit $3,000, and print the id, balance, monthly interest rate, and monthly interest.

class Account:
 def __init__(self, id=0, balance=100, annualInterestRate=0):
  self.__id = id
  self.__balance = balance
  self.__annualInterestRate = annualInterestRate
def getId(self):
 return self.__id
def setId(self, id):
 self.__id = id
def getBalance(self):
 return self.__balance
def setBalance(self, balance):
 self.__balance = balance
def getAnnualInterestRate(self):
 return self.__annualInterestRate
def setAnnualInterestRate(self, annualInterestRate):
 self.__annualInterestRate = annualInterestRate
def getMonthlyInterestRate(self):
 monthlyInterestRate = self.__annualInterestRate / 12 / 100
 return monthlyInterestRate
def getMonthlyInterest(self):
 monthlyInterest = self.__balance * self.getMonthlyInterestRate()
 return monthlyInterest
def withdraw(self, amount):
 self.__balance -= amount
def deposit(self, amount):
 self.__balance += amount
account = Account(1122, 20000, 4.5)
account.withdraw(2500)
account.deposit(3000)
print("Account ID:", account.getId())
print("Account Balance:", account.getBalance())
print("Monthly Interest Rate:", format(account.getMonthlyInterestRate(), ".2f"))
print("Monthly Interest:", format(account.getMonthlyInterest(), ".2f"))

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 7.4
#(The Fan class) Design a class named Fan to represent a fan. The class contains:
#Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 respectively
#denote the fan speed.
#A private int data field named speed that specifies the speed of the fan. A private bool data field named on that specifies whether the fan is on (the default is False).
#A private float data field named radius that specifies the radius of the fan.
#A private string data field named color that specifies the color of the fan.
#The accessor and mutator methods for all four data fields.
#A constructor that creates a fan with the specified speed (default SLOW), radius
#(default 5), color (default blue), and on (default False).
#Draw the UML diagram for the class and then implement the class.
#Write a test program that creates two Fan objects. For the first object, assign the maximum speed, radius 10, color yellow, and turn it on. Assign medium speed, radius 5, color blue, and turn it off for the second object.
#Display each object's speed, radius, color, and properties.
#(Geometry: n-sided regular polygon) An n-sided regular polygon's sides all have the same length and all of its angles have the same degree (i.e., the polygon is both equilateral and equiangular). Design a class named Regular Polygon that

class Fan:
 SLOW = 1
 MEDIUM = 2
 FAST = 3
def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
  self.__speed = speed
  self.__radius = radius
  self.__color = color
  self.__on = on
def getSpeed(self):
 return self.__speed
def setSpeed(self, speed):
 self.__speed = speed
def getRadius(self):
 return self.__radius
def setRadius(self, radius):
 self.__radius = radius
def getColor(self):
 return self.__color
def setColor(self, color):
 self.__color = color
def getOn(self):
 return self.__on
def setOn(self, on):
 self.__on = on
fan1 = Fan(Fan.FAST, 10, "yellow", True)
fan2 = Fan(Fan.MEDIUM)
print("Fan 1:")
print("Speed:", fan1.getSpeed())
print("Radius:", fan1.getRadius())
print("Color:", fan1.getColor())
print("On:", fan1.getOn())
print("Fan 2:")
print("Speed:", fan2.getSpeed())
print("Radius:", fan2.getRadius())
print("Color:", fan2.getColor())
print("On:", fan2.getOn())

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 7.8
#(Stopwatch) Design a class named Stopwatch. The class contains:
#The private data fields startTime and endTime with get methods. A constructor that initializes startTime with the current time.
#A method named start() that resets the start time to the current time. A method named stop() that sets the end time to the current time.
#A method named getElapsedTime() that returns the elapsed time for the stop watch in milliseconds.
#Draw the UML diagram for the class, and then implement the class. Write a test program that measures the execution time of adding numbers from 1 to 1,000,000.

import time
class Stopwatch:
  def __init__(self):
   self.__startTime = 0
   self.__endTime = 0
def getStartTime(self):
 return self.__startTime
def getEndTime(self):
 return self.__endTime
def start(self):
  self.__startTime = int(time.time() * 1000)
def stop(self):
 self.__endTime = int(time.time() * 1000)
def getElapsedTime(self):
 return self.__endTime - self.__startTime

stopwatch = Stopwatch()
stopwatch.start()
sum = 0
for i in range(1, 1000001):
 sum += i
stopwatch.stop()
print("The sum of numbers from 1 to 1,000,000 is", sum)
print("The elapsed time is", stopwatch.getElapsedTime(), "milliseconds")

#-----------------------------------------------------------------------------------------------------------------------

#Exercise 7.10
#(The Time class) Design a class named Time. The class contains: The private data fields hour, minute, and second that represent a time.
#A constructor that constructs a Time object that initializes hour, minute, and second using the current time.
#The get methods for the data fields hour, minute, and second, respectively. A method named setTime (elapseTime) that sets a new time for the object using the elapsed time in seconds.
#For example, if the elapsed time is 555550 seconds, the hour is 10, the minute is 19, and the second is 12.
#Draw the UML diagram for the class, and then implement the class.
#Write a test program that creates a Time object and displays its hour, minute, and second.
#Your program then prompts the user to enter an elapsed time, sets its elapsed time in the Time object, and displays its hour, minute, and second.
#Here is a sample run: Current time is 12:41:6 Enter the elapsed time: 55550505 Enter the hour: minute: second for the elapsed time is 22:41:45 (Hint: The initializer will extract the hour, minute, and second from the elapsed time.
#The current elapsed time can be obtained using time.time(), as shown in Listing 2.7, ShowCurrentTime.py.

import time
class Time:
 def __init__(self):
  self.__hour = 0
  self.__minute = 0
  self.__second = 0
  self.setTime(int(time.time()))
def getHour(self):
 return self.__hour
def getMinute(self):
 return self.__minute
def getSecond(self):
 return self.__second
def setTime(self, elapseTime):
 self.__hour = (elapseTime // 3600) % 24
 self.__minute = (elapseTime // 60) % 60
 self.__second = elapseTime % 60
time = Time()
print("Current time is", time.getHour(), ":", time.getMinute(), ":", time.getSecond())
elapseTime = int(input("Enter an elapsed time: "))
time.setTime(elapseTime)
print("The hour:minute:second for the elapsed time is", time.getHour(), ":", time.getMinute(), ":", time.getSecond())

#-----------------------------------------------------------------------------------------------------------------------
