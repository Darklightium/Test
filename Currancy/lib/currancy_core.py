from lib import config


def Menu():
    print(
        "Welcome to currancy exchange 24!\n"
        "USD:" , config.usd_buy , "/" ,config.usd_sell  , "Enter 1 to sell USD | Enter 2 to buy USD\n"
        "EUR:", config.eur_buy, "/", config.eur_sell, "Enter 3 to sell EUR | Enter 4 to buy EUR\n"
        "RUB:", config.rub_buy, "/", config.rub_sell, "Enter 5 to sell RUB | Enter 6 to buy RUB\n"
        "Reserve:", round(config.usd_reserve, 2), "USD |", round(config.eur_reserve, 2),
        "EUR |", round(config.uah_reserve, 2),  "UAH |", round(config.rub_reserve, 2),  "RUB\n"
        "Press 0 to exit."
    )


def sell_usd(amount):
    total_sell = float(amount) * float(config.usd_buy)
    if total_sell <= config.uah_reserve:
        config.uah_reserve -= total_sell
        config.usd_reserve += amount
        print("Total amount: ", round(total_sell, 2))
    else:
        print("Reserve UAH = ", round(config.uah_reserve, 2))


def buy_usd(amount):
    total_buy = float(amount) / float(config.usd_sell)
    if total_buy <= config.usd_reserve:
        config.usd_reserve -= total_buy
        config.uah_reserve += amount
        print("Total amount", round(total_buy,2))
    else:
        print("Reserve USD = ", round(config.usd_reserve, 2))
