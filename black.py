import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return None

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        aces = 0

        for card in self.cards:
            if card.value in ['J', 'Q', 'K']:
                value += 10
            elif card.value == 'A':
                aces += 1
            else:
                value += int(card.value)

        for _ in range(aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1

        return value

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

def play_blackjack(balance):
    print(f"\nCurrent balance: ${balance}")
    
    # Get bet amount
    while True:
        try:
            bet = int(input("Place your bet (minimum $5): $"))
            if bet < 5 or bet > balance:
                print(f"Bet must be between $5 and ${balance}")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
            continue

    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    # Initial deal
    for _ in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

    print(f"\nDealer's hand: {dealer_hand.cards[0]}, [Hidden]")
    print(f"Your hand: {player_hand} (Value: {player_hand.get_value()})")

    # Player's turn
    while player_hand.get_value() < 21:
        action = input("\nWould you like to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.add_card(deck.deal_card())
            print(f"Your hand: {player_hand} (Value: {player_hand.get_value()})")
        elif action == 'stand':
            break
        else:
            print("Invalid input! Please enter 'hit' or 'stand'.")

    player_value = player_hand.get_value()
    
    if player_value > 21:
        print("\nBust! You lose!")
        return balance - bet

    # Dealer's turn
    print(f"\nDealer's hand: {dealer_hand} (Value: {dealer_hand.get_value()})")
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())
        print(f"Dealer draws: {dealer_hand.cards[-1]}")
        print(f"Dealer's hand: {dealer_hand} (Value: {dealer_hand.get_value()})")

    dealer_value = dealer_hand.get_value()

    # Determine winner
    print(f"\nFinal Results:")
    print(f"Your hand: {player_hand} (Value: {player_value})")
    print(f"Dealer's hand: {dealer_hand} (Value: {dealer_value})")

    if dealer_value > 21:
        print("Dealer busts! You win!")
        return balance + bet
    elif player_value > dealer_value:
        print("You win!")
        return balance + bet
    elif dealer_value > player_value:
        print("Dealer wins!")
        return balance - bet
    else:
        print("It's a tie!")
        return balance

def main():
    print("Welcome to Blackjack!")
    balance = 100  # Starting balance
    
    while balance >= 5:
        balance = play_blackjack(balance)
        print(f"New balance: ${balance}")
        
        if balance >= 5:
            play_again = input("\nWould you like to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break
        else:
            print("You're out of money! Game over!")
            break
            
    print(f"Thanks for playing! Final balance: ${balance}")

if __name__ == "__main__":
    main()