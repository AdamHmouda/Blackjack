# Blackjack Game

This program simulates a game of Blackjack between a user and a dealer. It is written in Python and uses the `random` module.

## How to Play

1. Run the program in a Python environment.
2. The program will deal two cards to the user and the dealer, and display the user's first card and the dealer's first card.
3. The user will be prompted to draw more cards or pass (type "D" to draw more cards or "P" to pass).
4. If the user draws more cards, the program will add a new card to the user's hand, display the updated hand and calculate the user's total. If the user's total exceeds 21, the program will end the game and display a message indicating the user has lost.
5. If the user passes, the program will add cards to the dealer's hand until the dealer's total is at least 17, then display the dealer's total.
6. The game ends and the winner is determined as follows:
    - If the user's total is 21, the user wins.
    - If the dealer's total is 21, the dealer wins.
    - If both the user and dealer's totals are under 21, the one with the higher total wins.
    - If both the user and dealer's totals are over 21, the one with the lower total wins.
7. The program will prompt the user to play again or quit.

## Code Explanation

The program starts by initializing the `running` variable to `True`, creating a list of cards with their values, and initializing the `user_total` and `dealer_total` variables to 0.

The program then creates empty lists for the user's hand and the dealer's hand, and adds a card to each.

The `user_card_deal()` function is defined to add a new card to the user's hand and calculate the new total. If the user's total exceeds 21 and the hand contains an ace (with a value of 11), the function changes the value of the ace to 1. The function then displays the updated hand and total, and checks for a Blackjack or bust.

The `dealer_card_deal()` function is defined to add cards to the dealer's hand until the total is at least 17. If the hand contains an ace and the total exceeds 21, the function changes the value of the ace to 1. The function then displays the dealer's total and checks for a Blackjack or bust.

The `user_pass()` and `dealer_pass()` functions are defined to display the current total for each player.

The program then starts a loop that prompts the user to draw more cards or pass. If the user chooses to draw more cards, the `user_card_deal()` function is called. If the user passes, the `user_pass()` and `dealer_card_deal()` functions are called to complete the dealer's hand. The loop ends and the game ends when the user passes.

## Limitations

This program is a basic implementation of Blackjack and has a few limitations:

- It only allows the user to draw one card at a time.
- It does not allow the user to split pairs or double down.
- It does not include any betting or money management features.