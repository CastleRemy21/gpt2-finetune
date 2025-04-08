import random

def get_payout_multiplier(num_mines, picks):
    """Retrieves the payout multiplier based on the provided chart."""
    payout_chart = {
        1:  [1.01, 1.08, 1.12, 1.18, 1.24, 1.30, 1.37, 1.46, 1.55, 1.65, 1.77, 1.90, 2.06, 2.25, 2.47, 2.75, 3.09, 3.54, 4.12, 4.95, 6.19, 8.25, 12.38, 24.75],
        2:  [1.08, 1.17, 1.29, 1.41, 1.56, 1.74, 1.94, 2.18, 2.47, 2.83, 3.26, 3.81, 4.50, 5.40, 6.86, 8.25, 10.31, 14.14, 19.80, 29.70, 49.50, 99.00, 297.00, 0],
        3:  [1.12, 1.29, 1.48, 1.71, 2.00, 2.35, 2.79, 3.35, 4.07, 5.00, 6.26, 7.96, 10.35, 13.80, 18.97, 27.11, 40.61, 65.06, 113.85, 227.70, 569.25, 0, 0, 0],
        4:  [1.18, 1.41, 1.67, 2.00, 2.38, 2.83, 3.39, 4.05, 4.88, 5.90, 7.14, 8.67, 10.50, 12.83, 15.75, 19.39, 24.00, 30.00, 37.50, 47.25, 60.75, 81.00, 112.50, 0],
        5:  [1.24, 1.56, 1.90, 2.33, 2.88, 3.54, 4.37, 5.40, 6.68, 8.25, 10.20, 12.60, 15.54, 19.13, 23.55, 29.04, 35.79, 44.10, 54.39, 67.05, 82.65, 101.85, 125.37, 0],
        6:  [1.30, 1.74, 2.16, 2.70, 3.39, 4.26, 5.34, 6.69, 8.37, 10.47, 13.08, 16.32, 20.34, 25.32, 31.50, 39.15, 48.60, 60.30, 74.70, 92.52, 114.48, 141.48, 174.60, 0],
        7:  [1.37, 1.94, 2.46, 3.12, 3.96, 5.04, 6.42, 8.16, 10.38, 13.20, 16.77, 21.30, 27.00, 34.20, 43.29, 54.72, 69.12, 87.24, 109.98, 138.60, 174.60, 219.96, 276.84, 0],
        8:  [1.46, 2.18, 2.82, 3.63, 4.68, 6.03, 7.77, 10.02, 12.90, 16.59, 21.30, 27.30, 34.95, 44.70, 57.09, 72.81, 92.76, 117.96, 149.82, 189.90, 240.54, 304.20, 384.30, 0],
        9:  [1.55, 2.47, 3.24, 4.23, 5.52, 7.20, 9.39, 12.24, 15.96, 20.79, 27.06, 35.19, 45.72, 59.34, 76.95, 99.72, 129.06, 166.86, 215.46, 277.92, 358.02, 460.80, 592.92, 0],
        10: [1.65, 2.83, 3.75, 4.95, 6.54, 8.64, 11.40, 15.03, 19.80, 26.07, 34.29, 45.06, 59.13, 77.55, 101.61, 132.99, 173.88, 227.04, 296.16, 385.92, 502.56, 653.76, 849.96, 0],
        11: [1.77, 3.26, 4.38, 5.88, 7.89, 10.59, 14.19, 18.99, 25.41, 33.96, 45.33, 60.42, 80.46, 107.01, 142.20, 188.88, 250.74, 332.64, 440.82, 583.92, 772.92, 1022.40, 1351.80, 0],
        12: [1.90, 3.81, 5.19, 7.05, 9.57, 12.99, 17.61, 23.85, 32.28, 43.65, 58.98, 79.62, 107.37, 144.72, 194.94, 262.44, 353.04, 474.78, 638.04, 856.80, 1149.60, 1540.80, 2064.60, 0],
        13: [2.06, 4.50, 6.24, 8.58, 11.79, 16.20, 22.23, 30.48, 41.76, 57.15, 78.12, 106.68, 145.53, 198.45, 270.36, 367.92, 500.76, 681.12, 926.16, 1258.80, 1710.60, 2322.60, 3153.60, 0],
        14: [2.25, 5.40, 7.56, 10.53, 14.67, 20.43, 28.44, 39.57, 55.02, 76.44, 106.11, 147.24, 204.12, 282.96, 391.86, 542.16, 749.52, 1035.36, 1429.20, 1972.80, 2721.60, 3753.60, 5175.60, 0],
        15: [2.47, 6.86, 9.72, 13.77, 19.53, 27.66, 39.15, 55.35, 78.21, 110.43, 155.88, 219.78, 309.60, 435.96, 613.44, 862.92, 1213.20, 1704.60, 2394.00, 3360.00, 4716.00, 6615.00, 9282.00, 0],
        16: [2.75, 8.25, 12.15, 17.55, 25.38, 36.63, 52.83, 76.14, 109.62, 157.77, 226.89, 326.16, 468.72, 673.20, 966.60, 1387.44, 1990.80, 2854.80, 4090.80, 5860.80, 8391.60, 12009.60, 17190.00, 0],
        17: [3.09, 10.31, 15.39, 22.95, 34.29, 51.15, 76.23, 113.49, 168.84, 251.10, 373.14, 554.16, 822.24, 1219.68, 1808.64, 2679.36, 3969.36, 5878.56, 8700.48, 12876.00, 19056.00, 28188.00, 41712.00, 0],
        18: [3.54, 12.81, 19.44, 29.70, 45.36, 69.12, 105.30, 160.38, 244.08, 371.52, 565.02, 858.60, 1304.28, 1980.00, 3006.00, 4560.00, 6912.00, 10476.00, 15876.00, 24048.00, 36432.00, 55200.00, 83616.00, 0],
        19: [4.12, 15.93, 24.84, 38.88, 60.75, 94.77, 147.96, 230.76, 360.00, 561.60, 876.24, 1366.20, 2129.40, 3318.00, 5169.60, 8052.00, 12540.00, 19536.00, 30420.00, 47376.00, 73764.00, 114816.00, 178704.00, 0],
        20: [4.95, 19.80, 31.68, 50.76, 81.00, 129.24, 206.28, 329.40, 525.60, 838.80, 1338.48, 2136.00, 3408.00, 5436.00, 8676.00, 13848.00, 22104.00, 35280.00, 56304.00, 89856.00, 143424.00, 228960.00, 365616.00, 0],
        21: [6.19, 24.75, 40.59, 66.60, 108.90, 178.20, 291.60, 477.00, 780.30, 1276.20, 2087.28, 3414.00, 5580.00, 9120.00, 14904.00, 24360.00, 39816.00, 65088.00, 106380.00, 173880.00, 284256.00, 464640.00, 759240.00, 0],
        22: [8.25, 33.00, 54.45, 90.75, 150.15, 248.40, 411.00, 679.50, 1123.50, 1857.60, 3070.80, 5076.00, 8391.00, 13872.00, 22932.00, 37920.00, 62700.00, 103680.00, 171450.00, 283500.00, 468900.00, 775800.00, 1283250.00, 0],
        23: [12.38, 49.50, 82.50, 138.60, 231.00, 385.20, 642.00, 1071.00, 1785.00, 2976.00, 4962.00, 8268.00, 13776.00, 22968.00, 38280.00, 63792.00, 106320.00, 177120.00, 295200.00, 492000.00, 820200.00, 1366800.00, 2278800.00, 0],
        24: [24.75, 99.00, 165.00, 277.50, 465.00, 780.00, 1305.00, 2182.50, 3645.00, 6090.00, 10170.00, 16980.00, 28350.00, 47340.00, 79080.00, 132120.00, 220800.00, 368640.00, 615600.00, 1028400.00, 1717200.00, 2869200.00, 4795200.00, 0],
    }
    return payout_chart.get(num_mines, [1] * 24)[picks - 1] if picks <= 24 else 1.0

def display_grid(grid, revealed):
    """Displays the 5x5 grid with revealed tiles."""
    print("\n  0 1 2 3 4")
    for row in range(5):
        print(row, end=" ")
        for col in range(5):
            idx = row * 5 + col
            if idx in revealed:
                print("S", end=" ")  # Safe tile
            else:
                print("?", end=" ")  # Unrevealed tile
        print()

def play_round(balance, total_profit):
    """Plays a single round of the Mines game and returns the updated balance and total profit."""
    grid_size = 25  # 5x5 grid
    print("\n--- New Round ---")
    print(f"Current balance: {balance:.2f}")
    
    # Get user inputs for bet amount
    while True:
        try:
            bet_amount = float(input("Enter your bet amount: "))
            if bet_amount <= 0:
                print("Bet amount must be positive!")
                continue
            if bet_amount > balance:
                print(f"Bet amount cannot exceed your balance of {balance:.2f}!")
                continue
            break
        except ValueError:
            print("Please enter a valid number for the bet amount.")
    
    # Deduct the bet amount from the balance
    balance -= bet_amount
    
    # Get number of mines
    while True:
        try:
            num_mines = int(input("Enter the number of mines (1-24): "))
            if num_mines < 1 or num_mines > 24:
                print("Number of mines must be between 1 and 24!")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the number of mines.")
    
    # Initialize the game
    mine_positions = set(random.sample(range(grid_size), num_mines))
    revealed_tiles = set()
    safe_picks = 0
    game_over = False
    
    print("\nPick a tile by entering row (0-4) and column (0-4).")
    print("Type 'cashout' to cash out and end the game.")
    
    while not game_over:
        # Display the current grid
        display_grid([0] * grid_size, revealed_tiles)
        
        # Show current payout
        payout_multiplier = get_payout_multiplier(num_mines, safe_picks)
        potential_payout = bet_amount * payout_multiplier
        print(f"\nSafe picks: {safe_picks}, Payout multiplier: {payout_multiplier:.2f}x")
        print(f"Potential payout if you cash out now: {potential_payout:.2f}")
        
        # Get user input for the next pick
        user_input = input("Enter row and column (e.g., '2 3') or 'cashout': ").strip().lower()
        
        if user_input == "cashout":
            balance += potential_payout
            profit = potential_payout - bet_amount
            total_profit += profit
            print(f"\nYou cashed out! Payout: {potential_payout:.2f}, Profit: {profit:.2f}")
            break
        
        try:
            row, col = map(int, user_input.split())
            if row < 0 or row > 4 or col < 0 or col > 4:
                print("Row and column must be between 0 and 4!")
                continue
            pick = row * 5 + col
        except ValueError:
            print("Invalid input! Please enter row and column (e.g., '2 3') or 'cashout'.")
            continue
        
        # Check if the tile was already picked
        if pick in revealed_tiles:
            print("You've already picked this tile! Try another one.")
            continue
        
        # Reveal the tile
        revealed_tiles.add(pick)
        
        if pick in mine_positions:
            print(f"\nYou hit a mine at ({row}, {col})! Game over.")
            print(f"You lost your bet of {bet_amount:.2f}.")
            total_profit -= bet_amount
            game_over = True
        else:
            safe_picks += 1
            print(f"\nSafe pick at ({row}, {col})! {safe_picks} safe picks so far.")
            if safe_picks == grid_size - num_mines:
                payout_multiplier = get_payout_multiplier(num_mines, safe_picks)
                payout = bet_amount * payout_multiplier
                profit = payout - bet_amount
                balance += payout
                total_profit += profit
                print(f"\nYou revealed all safe tiles! Payout: {payout:.2f}, Profit: {profit:.2f}")
                game_over = True
    
    return balance, total_profit

def mines_game():
    """Main game loop that allows playing multiple rounds with a starting balance of 100."""
    print("Welcome to the Mines Game!")
    print("You start with a balance of 100.00.")
    balance = 100.0
    total_profit = 0.0
    play_again = True
    
    while play_again:
        if balance <= 0:
            print("\nYou're out of balance! Game over.")
            break
        
        balance, total_profit = play_round(balance, total_profit)
        print(f"\nCurrent balance: {balance:.2f}")
        print(f"Total profit/loss after this round: {total_profit:.2f}")
        
        # Ask if the user wants to play again
        while True:
            response = input("Would you like to play again? (yes/no): ").strip().lower()
            if response in ['yes', 'y']:
                break
            elif response in ['no', 'n']:
                play_again = False
                break
            else:
                print("Please enter 'yes' or 'no'.")
    
    print(f"\nThanks for playing! Final balance: {balance:.2f}")
    print(f"Final profit/loss: {total_profit:.2f}")

# Run the game
if __name__ == "__main__":
    mines_game()