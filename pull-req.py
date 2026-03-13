import random

def build_card_deck():
    card_deck = [0] * 52

    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    for i in range(52):
        suit = suits[i // 13]
        rank_card = ranks[i % 13]
        card_deck[i] = f"{rank_card} of {suit}"

    random.shuffle(card_deck)
    return card_deck

def draw_cards(card_deck):
    my_deck = []
    while len(my_deck) < 3:
        input("Press Enter to draw a card")
        random_card_choice = random.choice(card_deck)
        print(f"You drew: {random_card_choice}")
        my_deck.append(random_card_choice)

    return my_deck

def guess_card(my_deck):
    input("Press Enter when you have thought of a card")
    guessed_card = random.choice(my_deck)
    print(f"I guess you are thinking of: {guessed_card}")


def the_magitian():
    print("WELCOME TO MAGORIUM'S WONDER EMPORIUM CARD GAME")
    print("Think of a card from your hand and I will guess it.")
    card_deck = build_card_deck()
    my_deck = draw_cards(card_deck)
    print("Your hand of cards:")
    for card in my_deck:
        print(card)
    guess_card(my_deck)


if __name__ == "__main__":
    the_magitian()


