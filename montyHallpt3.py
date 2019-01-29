'''
Created on Nov 20, 2018

@author: Cooper Schlegel
'''
import random


#guessing
print("Welcome to the Monty Hall simulation.")

numrounds = int(input("Please enter the number of rounds you would like the simulation to run.  Please pick a number between 10 and 10,000: "))
initialSwitch= input("Would you like to always switch or always stay:")
switch = initialSwitch.lower()
right = 0

for num in [1, numrounds, 1]:
        #car assignment
        car = random.randint(1,3)
        #players random door assignment
        guess = random.randint(1,3)
        #car is behind door number 1
        if guess==1 and car==1:
            if switch == "stay":
                right += 1
        if guess==1 and car==2:
            if switch == "switch":
                right += 1
        if guess==1 and car==3:
            if switch == "switch":
                right += 1
        #car is behind door number 2
        if guess==2 and car==1:
            if switch == "switch":
                right += 1
        if guess==2 and car==2:
            if switch == "stay":
                right += 1
        if guess==2 and car==3:
            if switch == "switch":
                right += 1
        #car is behind door number 3
        if guess==3 and car==1:
            if switch == "switch":
                right += 1
        if guess==3 and car==2:
            if switch == "switch":
                right += 1
        if guess==3 and car==3:
            if switch == "stay":
                right += 1
    
    
percent = ((right/numrounds)*(100))
print("Number of rounds won: ", right)
print("Percentage of rounds won: ", percent)
