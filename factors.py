
#Asks the user to enter an integer
num_1 = int(input("Please enter a positive integer: "))

#Print the list of factors
print ("The factors of",num_1, "are: ")

#The range in ascending order
for factor in range(1, num_1 + 1):
   if num_1 % factor == 0:
       print(factor)
