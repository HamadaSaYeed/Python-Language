answer = 23

question = 'what numper am i thinking of ? '

print('let\'s play the guessing game ! ') # دعونا  نلعب لعبة التخمين!

while True:
    guess = int(input(question))
    
    if guess < answer :
        print('little higher')
        
    elif guess > answer :
        print('little lower')
        
    else: # guess == answer :
        print('Exceleent!!!')