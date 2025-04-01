import random
import math

def get_payout_multiplier(num_mines, picks):
    """Retrieves the payout multiplier based on the provided chart."""
    payout_chart = {
        1:  [1.01, 1.08, 1.17, 1.29, 1.41, 1.56, 1.74, 1.94, 2.18, 2.47, 2.81, 3.22, 3.71, 4.29, 4.98, 5.81, 6.79, 7.97, 9.37, 11.06, 13.09, 15.55, 18.52, 22.11],
        2:  [1.02, 1.12, 1.24, 1.41, 1.61, 1.85, 2.13, 2.47, 2.87, 3.35, 3.92, 4.59, 5.40, 6.36, 7.49, 8.83, 10.41, 12.28, 14.48, 17.08, 20.14, 23.75, 28.00, 33.00],
        3:  [1.03, 1.17, 1.32, 1.52, 1.77, 2.08, 2.47, 2.94, 3.51, 4.20, 5.04, 6.06, 7.31, 8.82, 10.66, 12.87, 15.54, 18.75, 22.61, 27.24, 32.83, 39.58, 47.76, 57.71],
        4:  [1.04, 1.21, 1.41, 1.67, 2.01, 2.42, 2.94, 3.57, 4.36, 5.32, 6.50, 7.94, 9.70, 11.85, 14.47, 17.64, 21.49, 26.16, 31.86, 38.81, 47.34, 57.82, 70.73, 86.66],
        5:  [1.05, 1.26, 1.48, 1.78, 2.16, 2.64, 3.24, 3.99, 4.91, 6.04, 7.41, 9.06, 11.05, 13.44, 16.30, 19.72, 23.79, 28.61, 34.34, 41.13, 49.20, 58.81, 70.30, 84.10],
        6:  [1.06, 1.30, 1.55, 1.89, 2.32, 2.86, 3.54, 4.40, 5.49, 6.85, 8.52, 10.57, 13.05, 16.05, 19.66, 23.98, 29.12, 35.25, 42.55, 51.24, 61.61, 73.96, 88.67, 106.17],
        7:  [1.07, 1.34, 1.61, 1.98, 2.46, 3.06, 3.82, 4.75, 5.90, 7.30, 8.99, 11.02, 13.45, 16.37, 19.86, 24.02, 28.97, 34.85, 41.84, 50.15, 60.01, 71.72, 85.61, 102.06],
        8:  [1.08, 1.38, 1.68, 2.09, 2.64, 3.32, 4.20, 5.34, 6.77, 8.55, 10.72, 13.37, 16.60, 20.52, 25.26, 31.00, 37.91, 46.23, 56.29, 68.48, 83.31, 101.35, 123.22, 149.61],
        9:  [1.09, 1.42, 1.75, 2.19, 2.81, 3.56, 4.50, 5.68, 7.16, 8.99, 11.24, 13.97, 17.27, 21.22, 25.94, 31.57, 38.26, 46.23, 55.76, 67.13, 80.67, 96.81, 116.04, 138.88],
        10: [1.10, 1.46, 1.82, 2.29, 2.98, 3.81, 4.82, 6.14, 7.88, 10.02, 12.63, 15.81, 19.70, 24.45, 30.26, 37.27, 45.71, 55.87, 68.02, 82.53, 99.83, 120.38, 144.75, 173.58],
        11: [1.11, 1.50, 1.89, 2.39, 3.15, 4.06, 5.14, 6.60, 8.60, 10.99, 13.91, 17.66, 22.38, 28.07, 35.04, 43.57, 53.63, 65.79, 80.51, 98.28, 119.75, 145.61, 176.39, 213.41],
        12: [1.12, 1.54, 1.96, 2.49, 3.32, 4.31, 5.46, 7.06, 9.32, 11.96, 15.19, 19.51, 25.06, 31.69, 39.82, 49.87, 62.02, 76.71, 94.00, 114.03, 137.09, 163.84, 195.07, 231.91],
    }
    return payout_chart.get(num_mines, [1] * 24)[picks - 1] if picks <= 24 else 1.0

def mines_game_simulation(bet_amount, num_mines, num_picks, num_simulations=10000):
    grid_size = 25  # 5x5 grid
    total_profit = 0
    
    for _ in range(num_simulations):
        mine_positions = set(random.sample(range(grid_size), num_mines))
        selected_tiles = set()
        profit = -bet_amount  # Initial loss of bet
        
        for picks in range(num_picks):  # Cash out after user-defined safe picks
            remaining_safe = grid_size - len(selected_tiles) - num_mines
            remaining_total = grid_size - len(selected_tiles)
            mine_probability = num_mines / remaining_total
            
            pick = random.randint(0, grid_size - 1)
            if pick in selected_tiles:
                continue  # Avoid picking the same tile twice
            
            if pick in mine_positions:
                print(f"Pick {picks + 1}: Hit a mine! Lost {bet_amount:.2f}")
                break  # Hit a mine, lose the bet
            
            selected_tiles.add(pick)
            payout_multiplier = get_payout_multiplier(num_mines, picks + 1)
            payout = bet_amount * payout_multiplier
            profit = payout  # Adjust profit based on payout
            print(f"Pick {picks + 1}: Won {payout:.2f}, Total Profit: {profit:.2f}, Mine Probability: {mine_probability:.2%}")
        
        total_profit += profit
    
    return total_profit

# User inputs
bet_amount = float(input("Enter your bet amount: "))
num_mines = int(input("Enter the number of mines (1-24): "))
num_picks = int(input("Enter the number of safe picks before cashing out: "))

# Run simulation
profit_or_loss = mines_game_simulation(bet_amount, num_mines, num_picks)
print(f"Total profit/loss after 10,000 simulations: {profit_or_loss:.2f}")