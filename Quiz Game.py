print('welcome to my Quiz game on india :)')

start = input('Type yes/y start and quit/q to Quit the game.\n ').lower()
if start not in ['yes','y']:
    print('Thank you for playing')
    quit()
print('let\'s begain!!!')
score = 0

print('Question no 1')
Ans = input('what is the national bird of India?\n').lower()
if Ans == "peacock":
    print('correct\n')
    score += 1
else:
    print('incorrect\n')
print('Question no 2')
Ans = input('What is the national animal of India?\n').lower()
if Ans == "tiger":
    print('correct\n')
    score += 1
else:
    print('incorrect\n')

print('Question no 3')
Ans = input('Who was the first Prime Minister of India?\n').lower()
if Ans in ["jawaharlal nehru", 'nehru']:
    print('correct\n')
    score += 1
else:
    print('incorrect\n')

print('Question no 4')
Ans = input('In which year did India gain independence from British rule?\n')
if Ans == "1947":
    print('correct\n')
    score += 1
else:
    print('incorrect\n')

print('Question no 5')
Ans = input('Which is the largest state in India by area?\n').lower()
if Ans == "rajasthan":
    print('correct\n')
    score += 1
else:
    print('incorrect\n')

print('Question no 6')
Ans = input('What is the capital of Maharashtra?\n').lower()
if Ans == "mumbai":
    print('correct\n')
    score += 1
else: 
    print('incorrect\n')

print('Question no 7')
Ans = input('What is the currency of India?\n').lower()
if Ans in ["rupee", 'rupees']:
    print('correct\n')
    score += 1
else:
    print('incorrect\n')

print('Question no 8')
Ans = input('Which state is the largest producer of tea in India?\n').lower()
if Ans == "assam":
    print('correct\n')
    score += 1
else:
    print('incorrect\n')

print('Question no 9')
Ans = input('The Taj Mahal is located in which city of India?\n').lower()
if Ans == "agra":
    print('correct\n')
    score += 1
else:
    print('incorrect\n')

print('Question no 10')
Ans = input('What is the capital of India?\n').lower()
if Ans == "new delhi":
    print('correct\n')
    score += 1
else:
    print('incorrect\n')

print(f'You got {score} correct out of 10 quesiton')
print(f'final score = {score} ')
print("Thank you for playing my Quiz game, have a wonderful day!!!")
