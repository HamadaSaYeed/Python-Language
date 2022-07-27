# Python Program to Check Prime Number -- >> الاوليه الاعداد

# Program to check if a number is Prime or not

num = 407


# Prime Numbers are greater than 1

if num > 1 :
    
    # check for factors -- >>  العوامل من تحقق
    
    for i in range (2,num):
        
        if(num % 1) == 0:
            print(num,'is not a prime numper')
            
            print(i,'times',num//i,'is',num)
            
            break
            
         else:
             
             print(num,'is a prime numper')
            
            
else:
    
    print(num,'is not a prime numper')
    
    
            
            
            