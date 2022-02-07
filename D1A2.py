# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""

#bullet point one
fifty = 50

print(fifty + fifty)

print(100-10)

#bullet point two
thirty = 30
six = 6
print(thirty*six) #I did * since +* isn't recognized
print(six^six)
print(six**six)
print(six+six+six+six+six+six)

#bullet point three
print ("Hello World")

print("Hello World : 10")

#mathmatical calculation exercise.

#p = money borrowed
#r = intrest rate  use r/12
#m = monthly payment
#l = length of time
#i = intrest

#get all variables for the equation

p = float(input("Please enter how much money you are borrowing: "))
r = float(input("Please enter in your intrest rate in percent form (7 for 7%): "))
l = int(input("Please enter in how many months you have to pay this off: "))


#Amortized Loan Payment Formula as given by: https://www.thebalance.com/loan-payment-calculations-315564 

monthlyPayment = p*( (pow(r,l) * (r-1)) / (pow(r,l))-1 )

#output the monthly payment to the user.
print("The minimum amount you would have to pay is: " + str(monthlyPayment))