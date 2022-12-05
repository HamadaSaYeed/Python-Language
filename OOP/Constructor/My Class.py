class myclass:
    value = 'my value'

# my value
c = myclass()
print(c.value) 

# hamada sayed
c.value = 'hamada sayed'
print(c.value)

# my value
del c.value 
print(c.value)