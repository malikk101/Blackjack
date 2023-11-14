'''
Created on Oct 23, 2023

@author: malikkhan
'''
import random

card_deck = {
    'Ace of Hearts': 11, '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4,
    '5 of Hearts': 5, '6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8,
    '9 of Hearts': 9, '10 of Hearts': 10, 'Jack of Hearts': 10,
    'Queen of Hearts': 10, 'King of Hearts': 10,
    'Ace of Spades': 11, '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4,
    '5 of Spades': 5, '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8,
    '9 of Spades': 9, '10 of Spades': 10, 'Jack of Spades': 10,
    'Queen of Spades': 10, 'King of Spades': 10,
    'Ace of Clubs': 11, '2 of Clubs': 2, '3 of Clubs': 3, '4 of Clubs': 4,
    '5 of Clubs': 5, '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8,
    '9 of Clubs': 9, '10 of Clubs': 10, 'Jack of Clubs': 10,
    'Queen of Clubs': 10, 'King of Clubs': 10,
    'Ace of Diamonds': 11, '2 of Diamonds': 2, '3 of Diamonds': 3,
    '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
    '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
    '10 of Diamonds': 10, 'Jack of Diamonds': 10,
    'Queen of Diamonds': 10, 'King of Diamonds': 10
}

def deal_card():
    card, value = random.choice(list(card_deck.items()))
    del card_deck[card]
    return card, value

def play_game():
    player1_score = 0
    player2_score = 0
    while card_deck:
        # Deal cards to both players
        player1_card1, player1_value1 = deal_card()
        player2_card1, player2_value1 = deal_card()
        player1_card2, player1_value2 = deal_card()
        player2_card2, player2_value2 = deal_card()

        # Calculate initial scores
        player1_score = player1_value1 + player1_value2
        player2_score = player2_value1 + player2_value2

        # Check for initial blackjack
        if player1_score == 21:
            print("Player 1 wins with a score of 21")
            break
        elif player2_score == 21:
            print("Player 2 wins with a score of 21")
            break

        # Player 1's turn
        while player1_score < 21:
            print("Player 1 Score is", player1_score)
            print("Player 2 Score is", player2_score)
            hit_or_stay = input("Player 1, do you want to hit or stay? (h/s)")
            if hit_or_stay.lower() == 'h':
                player1_new_card, player1_new_value = deal_card()
                player1_score += player1_new_value
                if player1_score > 21:
                    if 'Ace' in player1_card1 or 'Ace' in player1_card2 or 'Ace' in player1_new_card:
                        player1_score -= 10
                    else:
                        print("Player 1 busted with a score of", player1_score)
                        print("Player 2 wins!")
                        return
            else:
                break

        # Player 2's turn
        while player2_score < 21 and player1_score <= 21:
            print("Player 1 Score is", player1_score)
            print("Player 2 Score is", player2_score)
            hit_or_stay = input("Player 2, do you want to hit or stay? (h/s)")
            if hit_or_stay.lower() == 'h':
                player2_new_card, player2_new_value = deal_card()
                player2_score += player2_new_value
                if player2_score > 21:
                    if 'Ace' in player2_card1 or 'Ace' in player2_card2 or 'Ace' in player2_new_card:
                        player2_score -= 10
                    else:
                        print("Player 2 busted with a score of", player2_score)
                        print("Player 1 wins!")
                        return
            else:
                break

        # Determine the winner
        if player1_score > 21 and player2_score > 21:
            print("Both players busted!")
        elif player1_score > 21:
            print("Player 2 wins with a score of", player2_score)
        elif player2_score > 21:
            print("Player 1 wins with a score of", player1_score)
        elif player1_score == player2_score:
            print("Tied!")
        elif player1_score > player2_score:
            print("Player 1 wins with a score of", player1_score)
        else:
            print("Player 2 wins with a score of", player2_score)

    print("The cards ran out. Game over.")

play_game()
