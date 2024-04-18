from blackjack import play_blackjack
def welcome():
    print("cole and jerald lowkey kinda stanks gurley #so not slay, jerald and cole sittin in a tree K. I. S. S. I. N. G.")
def main():
    welcome()
    credits=215
    while True:
        print("you have", credits, "dollars")
        choice = int(input("\n1. Blackjack\n2. Slots\n3. Horsey Racin'\n4. Quit\n whatchya wanna do"))
        if choice == 1:
            credits = play_blackjack(credits)
        #if choice == 2:
        elif choice == 4:
            print("cya")
            break
        else:
            print("we dont have that hear pardner")
if __name__ == "__main__":
    main()

