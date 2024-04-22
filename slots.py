import random
import time
import sys
class SlotMachine:
    symbols = ["cherry", "lemon", "bell", "watermelon", "fried chicken", "bling"]
    def spinfr(self):
        return random.choice(self.symbols)
    def spin(self):
        return [self.spinfr() for _ in range(3)]
    def display(self, reels):
        print("\n-----------------------------------------------------")
        for row in reels:
            print("| " + "| ".join(row) + " |")
        print("-----------------------------------------------------")
    def win(self, reels):
        simcount = {symbol: 0 for symbol in self.symbols}
        for row in reels:
            for symbol in row:
                for symbol in simcount:
                    simcount[symbol] +=1
        if simcount["cherry"] == 3:
            return 15
        if simcount["lemon"] == 3:
            return 20
        if simcount["bell"] == 3:
            return 25
        if simcount["watermelon"] == 3:
            return 40
        if simcount["fried chicken"] == 3:
            return 63
        if simcount["bling"] == 3:
            return 100
        else:
            return 0
def playslots(credits):
    machine = SlotMachine()
    while True:
        input("press Enter to spin:")
        reels = [machine.spin() for _ in range(3)]
        for i in range(5):
            machine.display(reels)
            time.sleep(1)
            reels = [machine.spin() for _ in range(3)]
        machine.display(reels)
        winnings = machine.win(reels)
        if winnings > 0:
            print("HUZZAH WINNER", winnings)
            credits += winnings
        else:
            print("looser give me more money")
            credits -= 10
        return credits
if __name__ == "__main__":
    playslots()

