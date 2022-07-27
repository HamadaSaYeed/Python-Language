# Python Program to Check Leap Year -- > > برنامج بايثون للتحقق من السنة الكبيسة

# 4 على بالقسمه << كبيسه السنه ان من للتاكد

year = int (input ('Enter a year : '))

if ( year % 4 == 0 ):
    
        if ( year % 400 == 0 ):
            
             print (f'{year} a leap year')
        
        elif (year % 100 == 0):
        
            print(" is  a leap year.")
        
        else:
            
            print (f'{year} a not leap year')
            
else:
    
    print (f'{year} a not leap year')            
    
    
    