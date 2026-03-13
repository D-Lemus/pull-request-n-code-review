import random

def TheMagitian():
    card_deck = [0] * 52

    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    for i in range(52):
        suit = suits[i // 13]
        rankCard = ranks[i % 13]
        card_deck[i] = f"{rankCard} of {suit}"

    random.shuffle(card_deck)

    myDeck = []
    while len(myDeck) < 3:
        input("Press Enter to draw a card")
        randomCardChoice = random.choice(card_deck)
        print(f"You drew: {randomCardChoice}")
        myDeck.append(randomCardChoice)

    print("Your hand of cards:")
    for card in myDeck:
        print(card)

    print("Think of a card from your hand and I will guess it.")
    input("Press Enter when you have thought of a card")
    guessedCardbyMagitian = random.choice(myDeck)
    print(f"I guess you are thinking of: {guessedCardbyMagitian}")

if __name__ == "__main__":
    TheMagitian()


