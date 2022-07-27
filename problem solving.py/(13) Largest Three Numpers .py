# Python Program to Find the Largest Among Three Numbers

num1 = int (input ("Enter a num1 : "))

num2 = int (input ("Enter a num2 : "))

num3 = int (input ("Enter a num3 : "))


if num1 >= num2 and num1 >= num3:
    Largest = num1
    
elif num2 >= num1 and num2 >= num3:
    Largest = num2
    
else:
    Largest = num3
    
    
print (f'The largest number is {Largest}')    
    
