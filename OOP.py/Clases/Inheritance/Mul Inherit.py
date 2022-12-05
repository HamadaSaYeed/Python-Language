class A:
    def dothis(self):
        print('i am in A')

class B(A):
    pass

class C:
    def dothis(self):
        print('i am in C')

class D(B , C):
    pass


d  = D()
d.dothis() # i am in A