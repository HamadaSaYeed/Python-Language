'''                                 Square Number --> العدد مربع

Number    Square
----------------
1         1
2         4
3         9
4         16
5         25
6         36
7         49
8         64
9         81
10         100

                                    > use While Loop <

'''




print ('Number \t Square')

print ('---------------')

number = int (input('Enter the starting number : '))

while (number):
    
    squer = number ** 2
    
    if number == 11:  # controll end
        
        break
    
    print (number,'\t',(squer))
    
    number += 1
    
    

