def Agree(c):
    
    if(c == 'y' or c == 'Y'):
        
        print('Agreed')
        
    elif (c == 'n' or c == 'N'):
        
        print('Not Agreed')
        
    else :
        
        print('Enter char')
        
c = input('Do you Agree ? ')

Agree(c)