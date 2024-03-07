import random   
print('wellcome to my rock paper and sicssors game')

answer = input('To play game enter Yes/y and Quit/q to quit: ').lower()
if answer not in ['yes', 'y']:
    quit()

print('lets begain!!!')
player_score = 0
computer_score =0

while True:
    computer = random.choice(['rock', 'paper', 'scissors'])
    print('Type rock/paper/scissors to play or q to quit')
    user_choice = input('Type your choice: ').lower()
    if user_choice =='q':
        print('Thank you for playing my game!')
        break
    else:
        if user_choice not in ['rock', 'paper', 'scissors']:
            print('Please enter a valid choice')
            continue

    if user_choice == 'rock' and computer == 'scissors':
        print('you win')
        print(f'computer choice is {computer}')
        player_score += 1
        continue

    elif user_choice == 'paper' and computer == 'rock':
        print('you win')
        player_score += 1
        print(f'computer choice is {computer}')
        continue

    elif user_choice == 'scissors' and computer == 'paper':
        print('you win')
        print(f'computer choice is {computer}')
        player_score += 1
        continue

    elif user_choice == computer:
        print('its a tie')
        print(f'computer choice is {computer}')
        continue

    else:
        print('you lose')
        computer_score += 1
        print(f'computer choice is {computer}')
        continue
    


print(f'your score is {player_score}')
print(f'computer score is {computer_score}')
