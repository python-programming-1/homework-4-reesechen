# Python - HW4_Rock Paper Scissors Game - Chia-Yu Chen

import random

human_score = 0
computer_score = 0
play_again = 'y'

while play_again == 'y':
    print('Make a move! (r/s/p): ')
    moves = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    human = moves[input()]
    compu_moves = ['rock', 'paper', 'scissors']
    computer = random.choice(compu_moves)
    
    # human wins:
    if (human == 'rock' and computer == 'scissors') \
        or (human == 'scissors' and computer == 'paper') \
        or (human == 'paper' and computer == 'rock'):
        human_score += 1
        print('You chose ' + human + ' and the computer chose ' + computer + '. You win!')
    
    # computer wins:
    elif (computer == 'rock' and human == 'scissors') \
        or (computer == 'scissors' and human == 'paper') \
        or (computer == 'paper' and human == 'rock'):
        computer_score += 1
        print('You chose ' + human + ' and the computer chose ' + computer + '. You lose!')
    
    # draw:
    else:
        print('You chose ' + human + ' and the computer chose ' + computer + '. It\'s a draw!')

    # check score
    score = input()
    if score == 'sc':
        print('human: ' + str(human_score) + ', computer: ' + str(computer_score))
    
    # play again or not
    print('Do you want to play again? (y/n)')
    play_again = input()
    if play_again == 'n':
        print('Thanks bye!')
