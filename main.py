import random

running = True

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_total = 0
dealer_total = 0

dealer_hand = []
user_hand = []

user_hand.append(random.choice(cards))
dealer_hand.append(random.choice(cards))

print(f"your first card is {user_hand}")
print(f"dealer first card is {dealer_hand}")


def user_card_deal():
    user_hand.append(random.choice(cards))
    print(f"you have {user_hand}")
    user_total = sum(user_hand)
    if 11 in user_hand and user_total > 21:
        for number in range(len(user_hand)):
            if user_hand[number] == 11:
                user_hand[number] = 1
        print(f"you have {user_hand}")
        user_total = sum(user_hand)
    print(f"your total is {user_total}")
    print("____________________________________________")
    if user_total == 21:
        print("BlackJack !!")
    elif user_total > 21:
        print("You loose")


def dealer_card_deal():
    dealer_hand.append(random.choice(cards))
    dealer_total = sum(dealer_hand)
    if 11 in dealer_hand and dealer_total > 21:
        for number in range(len(dealer_hand)):
            if dealer_hand[number] == 11:
                dealer_hand[number] = 1
        dealer_total = sum(dealer_hand)
    while dealer_total < 17:
        dealer_hand.append(random.choice(cards))
        dealer_total = sum(dealer_hand)
    print(f"dealer total is {dealer_total}")
    if dealer_total == 21:
        print("Dealer got blackjack")
    elif dealer_total > 21:
        print("Dealer Bust !")


def user_pass():
    user_total = sum(user_hand)
    print(f"your total is {user_total}")


def dealer_pass():
    dealer_total = sum(dealer_hand)
    print(f"dealer total is {dealer_total}")


user_card_deal()
while running:
    q = input("Draw more cards or pass ? ( D/P) \n").lower()
    if q == "d":
        user_card_deal()
    else:
        user_pass()
        dealer_card_deal()
        running = False