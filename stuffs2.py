import random
import math

def get_payout_multiplier(num_mines, picks):
    """Retrieves the payout multiplier based on the provided chart."""
    payout_chart = {
        1:  [1.01, 1.08, 1.12, 1.18, 1.24, 1.30, 1.37, 1.46, 1.55, 1.65, 1.77, 1.90, 2.06, 2.25, 2.47, 2.75, 3.09, 3.54, 4.12, 4.95, 6.19, 8.25, 12.38, 24.75],
        2:  [1.08, 1.17, 1.29, 1.41, 1.56, 1.74, 1.94, 2.18, 2.47, 2.83, 3.26, 3.81, 4.50, 5.40, 6.86, 8.25, 10.61, 14.14, 19.80, 29.70, 49.50, 99.00, 297.00, 0],
        3:  [1.12, 1.29, 1.48, 1.71, 2.00, 2.35, 2.79, 3.35, 4.07, 5.00, 6.26, 7.96, 10.35, 13.80, 18.97, 27.11, 40.66, 65.06, 113.85, 227.70, 569.25, 0, 0, 0],
        4:  [1.18, 1.41, 1.71, 2.09, 2.58, 3.23, 4.09, 5.26, 6.88, 9.17, 12.51, 17.52, 25.30, 37.95, 59.64, 99.39, 178.91, 834.90, 2504.00, 0, 0, 0, 0, 0],
        5:  [1.24, 1.56, 2.00, 2.58, 3.39, 4.52, 6.14, 8.50, 12.04, 17.52, 26.77, 41.60, 66.41, 113.85, 208.72, 411.45, 939.26, 2504.00, 0, 0, 0, 0, 0, 0],
        6:  [1.30, 1.74, 2.35, 3.23, 4.52, 6.46, 9.44, 14.17, 21.89, 35.03, 58.38, 102.17, 189.75, 379.50, 834.90, 2087.25, 6261.00, 0, 0, 0, 0, 0, 0, 0],
        7:  [1.37, 1.94, 2.79, 4.09, 6.14, 9.44, 14.85, 24.47, 41.60, 73.95, 138.66, 277.33, 600.87, 1442.08, 3795.00, 11385.00, 0, 0, 0, 0, 0, 0, 0, 0],
        8:  [1.46, 2.18, 3.35, 5.26, 8.50, 14.17, 24.47, 44.05, 83.20, 166.40, 356.56, 831.98, 2163.15, 6489.45, 25957.80, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        9:  [1.55, 2.47, 4.07, 6.88, 12.04, 21.89, 41.60, 83.20, 176.80, 404.10, 1010.25, 2831.40, 9193.05, 36772.20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        10: [1.65, 2.83, 5.00, 9.17, 17.52, 35.03, 73.95, 166.40, 404.10, 1010.25, 2831.40, 9193.05, 36772.20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        11: [1.77, 3.26, 6.26, 12.51, 26.77, 58.38, 138.66, 356.56, 1010.25, 2831.40, 9193.05, 36772.20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        12: [1.90, 3.81, 7.96, 17.52, 41.60, 102.17, 277.33, 831.98, 2831.40, 9193.05, 36772.20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        13: [2.06, 4.50, 10.35, 25.30, 66.41, 189.75, 600.87, 2163.15, 9193.05, 36772.20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        14: [2.25, 5.40, 13.80, 37.95, 113.85, 379.50, 1442.08, 6489.45, 36772.20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        15: [2.47, 6.86, 18.97, 59.64, 208.72, 834.90, 3795.00, 25957.80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        16: [2.75, 8.25, 27.11, 99.39, 411.45, 2087.25, 11385.00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        17: [3.09, 10.61, 40.66, 178.91, 939.26, 6261.00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        18: [3.54, 14.14, 65.06, 834.90, 2504.00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        19: [4.12, 19.80, 113.85, 834.90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        20: [4.95, 29.70, 227.70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        21: [6.19, 49.50, 569.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        22: [8.25, 99.00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        23: [12.38, 297.00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        24: [24.75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    }
    return payout_chart.get(num_mines, [1] * 24)[picks - 1] if picks <= 24 else 1.0

def mines_game_simulation(bet_amount, num_mines, num_picks, num_simulations=100000):
    grid_size = 25  # 5x5 grid
    total_profit = 0
    
    for _ in range(num_simulations):
        mine_positions = set(random.sample(range(grid_size), num_mines))
        selected_tiles = set()
        profit = -bet_amount  # Initial loss of bet
        
        # Try to reach the desired number of safe picks
        for picks in range(num_picks):
            remaining_safe = grid_size - len(selected_tiles) - num_mines
            remaining_total = grid_size - len(selected_tiles)
            mine_probability = num_mines / remaining_total
            
            # Pick a random tile that hasn’t been selected yet
            available_tiles = [tile for tile in range(grid_size) if tile not in selected_tiles]
            if not available_tiles:  # No more tiles to pick
                break
            pick = random.choice(available_tiles)
            
            if pick in mine_positions:
                print(f"Pick {picks + 1}: Hit a mine! Lost {bet_amount:.2f}")
                profit = -bet_amount  # Lose the entire bet
                break  # End this simulation round
            
            selected_tiles.add(pick)
            payout_multiplier = get_payout_multiplier(num_mines, picks + 1)
            payout = bet_amount * payout_multiplier
            print(f"Pick {picks + 1}: Safe pick, Potential Payout: {payout:.2f}, Mine Probability: {mine_probability:.2%}")
        
        else:  # This runs only if the loop completes without hitting a mine
            profit = payout - bet_amount  # Final profit after all picks
        
        total_profit += profit
    
    return total_profit

# User inputs
bet_amount = float(input("Enter your bet amount: "))
num_mines = int(input("Enter the number of mines (1-24): "))
num_picks = int(input("Enter the number of safe picks before cashing out: "))

# Run simulation
profit_or_loss = mines_game_simulation(bet_amount, num_mines, num_picks)
print(f"Total profit/loss after 100,000 simulations: {profit_or_loss:.2f}")