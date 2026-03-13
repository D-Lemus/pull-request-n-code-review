import random

CARDS_IN_HAND = 3
DECK_SIZE = 52

def build_card_deck() -> list:
    """
    Builds and shuffles a standard 52-card deck.

    Returns:
    --------
    list
        A shuffled list of 52 strings, each representing a card (e.g. 'Ace of Spades').
    """
    card_deck = [0] * 52

    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    for i in range(52):
        suit = suits[i // 13]
        rank_card = ranks[i % 13]
        card_deck[i] = f"{rank_card} of {suit}"

    random.shuffle(card_deck)
    return card_deck

def draw_cards(card_deck: list) -> list:
    """
    Draws 3 cards from the deck and returns them as the player's hand.

    Parameters:
    -----------
    card_deck : list
        A list of strings representing the full card deck.

    Returns:
    --------
    list
        A list of 3 strings representing the drawn cards.
    """
    my_deck = []
    while len(my_deck) < CARDS_IN_HAND:
        input("Press Enter to draw a card")
        random_card_choice = random.choice(card_deck)
        card_deck.remove(random_card_choice)
        print(f"You drew: {random_card_choice}")
        my_deck.append(random_card_choice)

    return my_deck

def guess_card(my_deck: list) -> None:
    """
    Guesses which card the player is thinking of and validates their answer.

    Parameters:
    -----------
    my_deck : list
        A list of strings representing the player's hand of cards.

    Returns:
    --------
    None
    """
    input("Press Enter when you have thought of a card")
    guessed_card = random.choice(my_deck)
    print(f"I guess you are thinking of: {guessed_card}")
    
    while True:
        answer = input("Was this your card? (yes/no): ").strip().lower()
        if answer == "yes":
            print("Easy...")
            break
        elif answer == "no":
            print("Hmm.. Youre lying!")
            break
        else:
            print("Please answer 'yes' or 'no'.") 


def the_magitian() -> None:
    """
    Main game function. Builds the deck, draws cards, displays the hand
    and attempts to guess the player's chosen card.

    Returns:
    --------
    None
    """
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


