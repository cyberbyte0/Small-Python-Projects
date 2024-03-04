import random
print('Wellcome to my Number Guessing game :) ')
start = input('Type yes/y to start and quit/q to Quit the game.\n ').lower()
if start not in ['yes','y']:
    print('Thank you for playing')
    quit()

print('let\'s begain!!!')
low = input('Enter the lower limit: ')
if low.isdigit()== False:
    print('Please enter a valid number')
    quit()
high = input('Enter the higher limit: ')
if high.isdigit() == False:
    print('Please enter a valid number')
    if high <= low:
        print('The higher limit should be greater than the lower limit')
    quit()
number = random.randint(int(low), int(high)+1)
print(f'Guess the number between {low} and {high}')
number_of_guesses = 0
while True:
    number_of_guesses += 1
    guess = int(input('Enter your guess: '))
    if guess == number:
        print('Congratulations! You have guessed the number correctly.')
        break
    elif guess < number:
        print('Your guess is too low')
    else:
        print('Your guess is too high')

print(f'You have guessed the number in {number_of_guesses} attempts')
print('Thank you for playing my number guessing game :)')
