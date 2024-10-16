# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 10/15/2024
#Ask the user to enter positive integers that prints a list of all positive integers that divide by that number evenly
#Including itself and 1 in ascending order

#Asks the user to enter an integer
num_1 = int(input("Please enter a positive integer: "))

#Print the list of factors
print ("The factors of",num_1, "are: ")

#The range in ascending order
for factor in range(1, num_1 + 1):
   if num_1 % factor == 0:
       print(factor)
