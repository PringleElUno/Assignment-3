# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 10/15/2024
# Description: Asks the user the amount of integers they would like to enter and finds the minimum and maximum integers.

print ("How many integers would you like to enter? ") #Enter integers greater than or equal to 1
num_1 = int(input())

print ("Please enter", num_1, "integers. ")
_min =  int(input())
_max =  int(input())

for num in range (1, 3):
    number = int(input())  #Reads the integers one at a time
    if number > _max:
        _max = number
    if number < _min:
        _min = number
print ("min:",_min)
print ("max:",_max)