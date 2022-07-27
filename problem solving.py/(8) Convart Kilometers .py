# Python Program to Convart Kilometers Number

# tack kilometers input from the user

kilometers = float (input('Enter value in kilometers: '))

# conversion factor  التحويل عامل 

conv_fac = 0.621371


miles = kilometers * conv_fac

print(f'{kilometers} kilometers is equal to {miles} miles')