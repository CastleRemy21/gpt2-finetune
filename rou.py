import random
import time

class Roulette:
    def __init__(self):
        self.balance = 100  # Starting balance
        self.wheel = list(range(37))  # 0-36
        self.red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        self.columns = {
            1: [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
            2: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
            3: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
        }
        self.dozens = {
            1: list(range(1, 13)),    # 1-12
            2: list(range(13, 25)),   # 13-24
            3: list(range(25, 37))    # 25-36
        }

    def spin_wheel(self):
        print("Spinning the wheel...")
        time.sleep(2)  # Simulate spinning
        result = random.choice(self.wheel)
        color = "Green" if result == 0 else ("Red" if result in self.red_numbers else "Black")
        return result, color

    def place_bet(self):
        print(f"\nCurrent balance: ${self.balance}")
        print("Betting options:")
        print("1. Red/Black (Pays 1:1)")
        print("2. Odd/Even (Pays 1:1)")
        print("3. Specific number (Pays 35:1)")
        print("4. Dozen (1-12, 13-24, 25-36) (Pays 2:1)")
        print("5. Column (1st, 2nd, 3rd) (Pays 2:1)")
        
        bet_type = input("Choose bet type (1-5): ")
        amount = int(input("Enter bet amount: "))
        
        if amount > self.balance or amount <= 0:
            print("Invalid bet amount!")
            return False

        if bet_type == "1":
            choice = input("Red or Black? ").lower()
            return {"type": "color", "choice": choice, "amount": amount}
        elif bet_type == "2":
            choice = input("Odd or Even? ").lower()
            return {"type": "parity", "choice": choice, "amount": amount}
        elif bet_type == "3":
            choice = int(input("Choose number (0-36): "))
            if 0 <= choice <= 36:
                return {"type": "number", "choice": choice, "amount": amount}
            else:
                print("Invalid number!")
                return False
        elif bet_type == "4":
            choice = int(input("Choose dozen (1: 1-12, 2: 13-24, 3: 25-36): "))
            if 1 <= choice <= 3:
                return {"type": "dozen", "choice": choice, "amount": amount}
            else:
                print("Invalid dozen!")
                return False
        elif bet_type == "5":
            choice = int(input("Choose column (1, 2, or 3): "))
            if 1 <= choice <= 3:
                return {"type": "column", "choice": choice, "amount": amount}
            else:
                print("Invalid column!")
                return False
        else:
            print("Invalid bet type!")
            return False

    def resolve_bet(self, bet, result, color):
        if not bet:
            return

        amount = bet["amount"]
        self.balance -= amount
        
        if bet["type"] == "color":
            won = (bet["choice"] == "red" and color == "Red") or (bet["choice"] == "black" and color == "Black")
            if won:
                winnings = amount * 2
                self.balance += winnings
                print(f"You won ${winnings - amount}!")
            else:
                print("You lost!")
                
        elif bet["type"] == "parity":
            if result == 0:
                print("You lost! (Zero)")
            else:
                is_even = result % 2 == 0
                won = (bet["choice"] == "even" and is_even) or (bet["choice"] == "odd" and not is_even)
                if won:
                    winnings = amount * 2
                    self.balance += winnings
                    print(f"You won ${winnings - amount}!")
                else:
                    print("You lost!")
                    
        elif bet["type"] == "number":
            won = bet["choice"] == result
            if won:
                winnings = amount * 36
                self.balance += winnings
                print(f"You won ${winnings - amount}!")
            else:
                print("You lost!")
                
        elif bet["type"] == "dozen":
            won = result in self.dozens[bet["choice"]] and result != 0
            if won:
                winnings = amount * 3
                self.balance += winnings
                print(f"You won ${winnings - amount}!")
            else:
                print("You lost!")
                
        elif bet["type"] == "column":
            won = result in self.columns[bet["choice"]] and result != 0
            if won:
                winnings = amount * 3
                self.balance += winnings
                print(f"You won ${winnings - amount}!")
            else:
                print("You lost!")

    def play(self):
        while self.balance > 0:
            print("\n=== Roulette Game ===")
            bet = self.place_bet()
            if bet:
                result, color = self.spin_wheel()
                print(f"The ball landed on: {result} {color}")
                self.resolve_bet(bet, result, color)
                print(f"New balance: ${self.balance}")
            
            if input("\nPlay again? (y/n): ").lower() != 'y':
                break
        
        if self.balance <= 0:
            print("You're out of money! Game over!")
        else:
            print(f"Game ended. Final balance: ${self.balance}")

if __name__ == "__main__":
    game = Roulette()
    game.play()