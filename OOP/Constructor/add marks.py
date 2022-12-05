class student:

    # constructor
    def __init__(self , name) :
        self.name = name
        self.list = []
        print(f'welcome {name} in school ')

    # method
    def add_mark(self, val):
        self.list.append(val)

# object
s1 = student('Hamada')
s1.add_mark(50)
s1.add_mark(20)
s1.add_mark('hamada')
s1.add_mark(59)
s1.add_mark(9)
print(s1.list)