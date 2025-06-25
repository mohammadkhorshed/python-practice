# Rock-Paper-Scissor Simulation

import random
options = ['rock', 'paper', 'scissor']
num_of_pick = int(input("How many times do you want to play? "))
player_won = 0
computer_won = 0

for t in range(num_of_pick):
    player_pick = input("Your pick (Rock/Paper/Scissor): ").lower().strip()
    computer_pick = random.choice(options)
    if player_pick == computer_pick:
        pass
    elif player_pick == 'rock' and computer_pick == 'scissor':
        player_won += 1
    elif player_pick == 'paper' and computer_pick == 'rock':
        player_won += 1
    elif player_pick == 'scissor' and computer_pick == 'paper':
        player_won += 1
    else:
        computer_won += 1
    print(f"Score:\nPlayer: {player_won}\nComputer: {computer_won}")

if player_won > computer_won:
    print('Congratulations! You Win!')
else:
    print('Bad Luck! You Lose!')
    print('Better Luck Next Time!')
