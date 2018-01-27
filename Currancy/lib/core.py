from lib import conf


def menu():
    print("Current courses are:\n"
          "USD:", conf.usd_buy, "/", conf.usd_sell,
          "    Press 1 to sell USD | Press 2 to buy USD\n"
          "EUR:", conf.eur_buy, "/", conf.eur_sell,
          "       Press 3 to sell EUR | Press 4 to buy EUR\n"
          "RUB:", conf.rub_buy, "/", conf.rub_sell,
          "   Enter 5 to sell RUB | Enter 6 to buy RUB\n"
          "Reserve:", round(conf.usd_reserve, 2), "USD |", round(conf.eur_reserve, 2),
          "EUR |", round(conf.uan_reserve, 2), "UAH |", round(conf.rub_reserve, 2), "RUB\n")


# USD operations
def sell_usd(ammount):
    total_sell = float(ammount)*float(conf.usd_buy)
    if total_sell <= conf.uan_reserve:
        conf.uan_reserve -= total_sell
        conf.usd_reserve += ammount
        print("Total ammount:", round(total_sell, 2))
        conf.update_info()
    else:
        print("Reserve UAN = ", conf.uan_reserve)


def buy_usd(ammount):
    total_sell = float(ammount)/float(conf.usd_sell)
    if total_sell <= conf.usd_reserve:
        conf.usd_reserve -= total_sell
        conf.uan_reserve += ammount
        print("Total ammount:", round(total_sell, 2))
        conf.update_info()
    else:
        print("Reserve USD = ", conf.usd_reserve)


# EUR operations
def sell_eur(ammount):
    total_sell = float(ammount)*float(conf.eur_buy)
    if total_sell <= conf.uan_reserve:
        conf.uan_reserve -= total_sell
        conf.eur_reserve += ammount
        print("Total ammount:", round(total_sell, 2))
        conf.update_info()
    else:
        print("Reserve UAN = ", conf.uan_reserve)


def buy_eur(ammount):
    total_sell = float(ammount)/float(conf.eur_sell)
    if total_sell <= conf.eur_reserve:
        conf.eur_reserve -= total_sell
        conf.uan_reserve += ammount
        print("Total ammount:", round(total_sell, 2))
        conf.update_info()
    else:
        print("Reserve USD = ", conf.eur_reserve)


# RUB operations
def sell_rub(ammount):
    total_sell = float(ammount)*float(conf.rub_buy)
    if total_sell <= conf.uan_reserve:
        conf.uan_reserve -= total_sell
        conf.rub_reserve += ammount
        print("Total ammount:", round(total_sell, 2))
        conf.update_info()
    else:
        print("Reserve UAN = ", conf.uan_reserve)


def buy_rub(ammount):
    total_sell = float(ammount)/float(conf.rub_sell)
    if total_sell <= conf.rub_reserve:
        conf.rub_reserve -= total_sell
        conf.uan_reserve += ammount
        print("Total ammount:", round(total_sell, 2))
        conf.update_info()
    else:
        print("Reserve USD = ", conf.rub_reserve)


def admin_login():
    login_adm = input("Enter your login: ")
    passwd_adm = input("Enter password: ")
    if login_adm == conf.login:
        if passwd_adm == conf.passwd:
            admin_func()

    else:
        print("fool)")


def admin_func():
    print("true")
    while True:
        print("What do you want to do?\n1.Edit currancy\n2.Edit reserve\n0.Exit")
        choice = int(input())
        if choice == 1:
            cur_edit()
        elif choice == 2:
            res_edit()
        else:
            break


def cur_edit():
    while True:
        choice = int(input("What cource you want to edit?\n1.USD\n2.EUR\n3.RUB\n"))
        if choice == 1:
            new_usd_sell = float(input("Enter new USD sell "))
            conf.usd_sell = new_usd_sell
            new_usd_buy = float(input("Enter new USD buy "))
            conf.usd_buy = new_usd_buy
        elif choice == 2:
            new_eur_sell = float(input("Enter new EUR sell "))
            conf.eur_sell = new_eur_sell
            new_eur_buy = float(input("Enter new EUR buy "))
            conf.eur_buy = new_eur_buy
        elif choice == 3:
            new_rub_sell = float(input("Enter new RUB sell "))
            conf.rub_sell = new_rub_sell
            new_rub_buy = float(input("Enter new RUB buy "))
            conf.rub_buy = new_rub_buy
        else:
            break


def res_edit():
    print("in process")
    choice = int(input("What reserve you want to edit?\n1.USD\n2.EUR\n3.RUB\n"))
    if choice == 1:
        new_usd_res = float(input("Enter new USD reserve "))
        conf.usd_reserve = new_usd_res
    elif choice == 2:
        new_eur_res = float(input("Enter new EUR reserve "))
        conf.eur_reserve = new_eur_res
    elif choice == 3:
        new_rub_res = float(input("Enter new RUB reserve "))
        conf.rub_reserve = new_rub_res










