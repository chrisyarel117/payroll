#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Christopher Y Sanchez
Course Name: ENTD200 B002 SUMMER2020
Instructors Name: Joseph Kivacic
Week 4
Date Completed: Aug 28, 2020
"""

def pay(hours, rate): ###functions when writing in the parenthesis is provoding an argument to the function.
    return hours * rate
def paywovertime(overtime, OTrate): ###functions
    return overtime * OTrate 
def totalpay(OverTimePay, GrossPay): ###functions
    return OverTimePay + GrossPay

###beginning lets the user know to only input a non decimal number
hourly_rate = int(input("Enter Hourly Rate Here: ")) ###Same Here
hours_worked = int(input("Enter Hours Worked Here: ")) ###Having the int at the
overtime_hoursworked = int(input("Enter Over Time Hours Here: ")) 
regular_shift = 40
OTrate = hourly_rate * 1.5
operation = 1 #sets the attempt to start from number 1.
yes = "y"
no = "n"
pay_noovertime = regular_shift * hourly_rate
GrossPay = pay(int(hours_worked), int(hourly_rate)) ###2 arguments
OverTimePay = paywovertime(int(overtime_hoursworked), int(OTrate)) ###2 argumenrs
GrossPaywOverTime = totalpay(int(OverTimePay), int(GrossPay))

while(operation == 1): #while loops continue as long as the value continues to be true. 
    if (hours_worked == regular_shift) :
        print("You worked your assigned shift.")
        print("Your Gross Pay is: ", GrossPay)
    elif (hours_worked <= regular_shift) :
        print("You did not work your assigned shift.")
        print("Your Gross Pay is: ", GrossPay)
    elif (hours_worked >= regular_shift) : #regular_shift = 40
        print("You worked Over Time.")
        print("Over Time hours worked: ", overtime_hoursworked)
        print("Your Over Time Pay is: ", OverTimePay)
        print("Your Gross Pay without Over Time is: ", pay_noovertime)
        print("Your total pay with Over Time is: ", GrossPaywOverTime)
        choice = input("Would you like to check your pay and time again? (y/n) : ")
    
    if (choice == "n") : #makes the choice value of No executable.
        print("Thank you for using our application. See you next time.")
        break
    


    
###print("You missed your shift by "" hours")    


