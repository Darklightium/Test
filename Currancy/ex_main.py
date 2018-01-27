from lib import core

while True:
    core.menu()
    choice = int(input("Enter your choice: "))
    if choice == 0:
        print("Be back!")
        break
    elif choice == 1:
        amount = float(input("Enter amount to sell USD: \t"))
        core.sell_usd(amount)
        input("Press any keys to continue!")
    elif choice == 2:
        amount = float(input("Enter amount to buy USD for UAH: \t"))
        core.buy_usd(amount)
        input("Press any keys to continue!")
    elif choice == 3:
        amount = float(input("Enter amount to sell EUR: \t"))
        core.sell_eur(amount)
        input("Press any keys to continue!")
    elif choice == 4:
        amount = float(input("Enter amount to buy EUR for UAN: \t"))
        core.buy_eur(amount)
        input("Press any keys to continue!")
    elif choice == 5:
        amount = float(input("Enter amount to sell RUB: \t"))
        core.sell_rub(amount)
        input("Press any keys to continue!")
    elif choice == 6:
        amount = float(input("Enter amount to buy RUB for UAN: \t"))
        core.buy_rub(amount)
        input("Press any keys to continue!")
    elif choice == 666:
        core.admin_login()
        input("Press any keys to continue!")

input("Enter any keys to continue!")