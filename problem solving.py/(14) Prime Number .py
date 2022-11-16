a = int(input("Enter A Number : "))
flag = 0
for i in range(2,a):
    if a % i == 0:
        print('NO Prime')
        flag = 1
        break
    
if flag == 0:
    print('Yes Is Prime')