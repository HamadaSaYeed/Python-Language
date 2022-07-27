# -------------------------------------------------->> if Conditions <<--------------------------------------------------------------------#

x = int(input ('enter a value x : '))

y = int(input ('enter a value y : '))

if x == 5 and y == 5:
    print ('x = 5 >> y = 5')
    
elif x == 4:
    print('x = 4')
    
else:
    print('all a value')
    
    
# -------------------------------------------------->> {and,or,not} <<--------------------------------------------------------------------#    
    
username = 'Hamada' ; password = '12345'

if username == 'Hamada' and password == '12345': # tow Conditions == True 
    print('login success , welcom Hamada')
    
elif username == 'Hamada' or password == '123456': # one` Conditions == True 
    print('login success , welcom Hamada')    