import random

def main():
    player1 = 0
    player1wins = 0
    player2 = 0
    player2wins = 0
    player3 = 0
    player3wins = 0
    rounds = 1
    
    while rounds !=11:
        print('Round ' + str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        player3 = dice_roll()
        print("Player 1 rolls: " + str(player1))
        print("Player 2 rolls: " + str(player2))
        print("Player 3 rolls: " + str(player3))
        
        if player1 == player2 == player3:
            print("Draw!")
        
        elif player1 > player2 and player3:
            player1wins = player1wins + 1
            print ("Player 1 Wins - Rounds Won: " + str(player1wins))
            
        elif player2 > player1 and player3:
            player2wins = player2wins + 1
            print("Player 2 Wins - Rounds Won: " + str(player2wins))
            
        else:
            player3wins = player3wins + 1
            print("Player 3 Wins - Rounds Won: " + str(player3wins))
        
        rounds = rounds + 1

    if player1wins == player2wins == player3wins:
        print("Draw!")
    elif player1wins > player2wins and player3wins:
        print("Player 1 Wins - Rounds Won: " + str(player1wins))
    elif player2 > player1 and player3:
        print("Player 2 Wins - Rounds Won: " + str(player2wins))
    else:
        print("Player 3 Wins - Rounds Won: " + str(player3wins))

def dice_roll():
    diceRoll = random.randint(2, 12)
    return diceRoll

main()