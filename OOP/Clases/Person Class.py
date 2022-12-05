class person:
    
    # attribute  /  variable
    greed = 90
    gpa = 3.2
    
    # behavior  /  method
    def show(self):
        print('name : hamada')
        print('age : ' + str(18))
        
p = person()
p.show()
print(f'greed : {p.greed}')
print(f'gpa : {p.gpa}')