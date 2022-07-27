# Python Program to Calculate the Area of Triangle -- >> المثلث مساحه

# if (a),(b)and(c)are three sides of a triangle.Then,
# s = (a+b+c)/2
# area = جذر (s(s-a)*(s-b)*(s-c)) --- >> المثلث مساحه قانون



# Python Program to Calculate the Area of triangle

a = 5
b = 6
c = 7



# calculate the semi-perimeter

s = (a + b + c) / 2


# calculate the area

area = (s*(s-a)*(s-b)*(s-c))**0.5

print(f'The area of the triangle = {area}')














