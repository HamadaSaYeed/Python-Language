'''                                   Square Number --> العدد مربع

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

                                      > use For Loop <

'''



print ('Number \t Square')

print ('---------------')


start = int (input('Enter the starting number : '))

end   = int (input('How high should I go : '))

for Number in range (start,end+1):
    
    Squer = pow(Number,2)    # Squer = Number * Number        # Squer = Number ** 2     <<  -- -- (2) اس معناهم
    
    print (Number,'\t',(Squer))
    




