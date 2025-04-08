import random
import time

def print_plinko_board(position):
    """Prints a simple visual representation of the ball's final position"""
    board = [
        "      /\\      ",
        "     /  \\     ",
        "    /    \\    ",
        "   /      \\   ",
        "  /________\\  ",
        "|  1  2  3  4  |"
    ]
    # Add ball marker
    if position == 1:
        board[-1] = "| *1  2  3  4  |"
    elif position == 2:
        board[-1] = "|  1 *2  3  4  |"
    elif position == 3:
        board[-1] = "|  1  2 *3  4  |"
    else:
        board[-1] = "|  1  2  3 *4  |"
    
    for line in board:
        print(line)

def play_plinko(balance):
    """Main Plinko game function"""
    while True:
        # Show current balance and get bet
        print(f"\nCurrent balance: ${balance:.2f}")
        try:
            bet = float(input("Enter your bet amount (or 0 to quit): $"))
            if bet == 0:
                return balance
            if bet > balance:
                print("You can't bet more than your current balance!")
                continue
            if bet < 0:
                print("Bet must be positive!")
                continue
        except ValueError:
            print("Please enter a valid number!")
            continue

        # Simulate ball dropping
        print("\nDropping the ball...")
        time.sleep(1)
        
        # Random landing position (1-4)
        position = random.randint(1, 4)
        print_plinko_board(position)
        
        # Determine winnings based on position
        if position == 1:
            multiplier = 0.5  # Lose half the bet
            winnings = bet * multiplier
            print(f"Position 1: You won back {multiplier}x your bet!")
        elif position == 2:
            multiplier = 1.0  # Get your bet back
            winnings = bet * multiplier
            print(f"Position 2: You won back {multiplier}x your bet!")
        elif position == 3:
            multiplier = 2.0  # Double your bet
            winnings = bet * multiplier
            print(f"Position 3: You won back {multiplier}x your bet!")
        else:  # position 4
            multiplier = 3.0  # Triple your bet
            winnings = bet * multiplier
            print(f"Position 4: You won back {multiplier}x your bet!")
        
        # Update balance
        balance = balance - bet + winnings
        print(f"Winnings: ${winnings:.2f}")
        print(f"New balance: ${balance:.2f}")

        # Check if player can continue
        if balance <= 0:
            print("You're out of money!")
            return balance

def main():
    # Starting balance
    balance = 100.0
    print("Welcome to Plinko!")
    print("Starting balance: $100.00")
    print("Land in positions 1-4 for different multipliers:")
    print("1: 0.5x, 2: 1x, 3: 2x, 4: 3x")

    while True:
        balance = play_plinko(balance)
        
        if balance <= 0:
            print("Game Over! You've lost all your money.")
            break
            
        # Ask to play again
        while True:
            play_again = input("\nWould you like to play again? (yes/no): ").lower()
            if play_again in ['yes', 'no']:
                break
            print("Please enter 'yes' or 'no'")
            
        if play_again == 'no':
            print(f"Thanks for playing! Final balance: ${balance:.2f}")
            break

if __name__ == "__main__":
    main()