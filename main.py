import time
import sys
import random


def win():
    print('Congratulations! You win')


def lost():
    print('Sorry! You lost')


def draw():
    print("It's a draw")


def game():
    options = ['rock', 'paper', 'scissors']


print('"R" for "rock", "P" for "paper", "S" for "scissors"')
attempts = 3
while True:
    if attempts == 0:
        print("You're yet to provide the right options, Try again")
        time.sleep(3)
        sys.exit(0)

    player = str(input('Player: ')).upper()
    if player.upper() not in options:
        print(f'Invalid Option! You have (attempts) attempts left')
        attempts -= 1
    else:
        computer = random.choice(options)
        print(f'Computer:{computer}')

        if player == computer:
            draw()
        elif player == 'R' and computer == 'S':
            win()
        elif player == 'R' and computer == 'P':
            lost()
        elif player == 'P' and computer == 'R':
            win()
        elif player == 'p' and computer == 'S':
            lost()
        elif player == 'S' and computer == 'P':
            win()
        elif player == 'S' and computer == 'R':
            lost()
        else:
            pass
        play_again = str(input('Retry? (y/n):'))
        if play_again.lower() == 'y':
            game()
        elif play_again.lower() == 'n':
            print('Game over. Goodbye')
            time.sleep(2.5)
            sys.exit(0)
        else:
            print('Invalid Options. Goodbye')
            time.sleep(2.5)
            sys.exit(0)