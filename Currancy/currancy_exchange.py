from lib import currancy_core

while True:
    currancy_core.Menu()
    choice = int(input("Enter operation: \t"))
    if choice == 0:
        print("Bye!")
        break
    elif choice == 1:
        amount = float(input("Enter amount to sell USD: \t"))
        currancy_core.sell_usd(amount)
        input("Press any keys to continue!")
    elif choice == 2:
        amount = float(input("Enter amount to buy UAH: \t"))
        currancy_core.buy_usd(amount)
        input("Press any keys to continue!")


input("Enter any keys to continue!")