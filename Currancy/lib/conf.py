import json


path = 'db\curses.json'
with open(path) as curses:
    currency_list = json.load(curses)
    usd_sell = currency_list[0]
    usd_sell = float(usd_sell['usd_sell'])
    usd_buy = currency_list[1]
    usd_buy = float(usd_buy['usd_buy'])
    eur_sell = currency_list[2]
    eur_sell = float(eur_sell['eur_sell'])
    eur_buy = currency_list[3]
    eur_buy = float(eur_buy['eur_buy'])
    rub_sell = currency_list[4]
    rub_sell = float(rub_sell['rub_sell'])
    rub_buy = currency_list[5]
    rub_buy = float(rub_buy['rub_buy'])
    usd_reserve = currency_list[6]
    usd_reserve = float(usd_reserve['usd_reserve'])
    eur_reserve = currency_list[7]
    eur_reserve = float(eur_reserve['eur_reserve'])
    rub_reserve = currency_list[8]
    rub_reserve = float(rub_reserve['rub_reserve'])
    uan_reserve = currency_list[9]
    uan_reserve = float(uan_reserve['uan_reserve'])


def update_info():
    currency_info = [
        {"usd_sell": usd_sell},
        {"usd_buy": usd_buy},
        {"eur_sell": eur_sell},
        {"eur_buy": eur_buy},
        {"rub_sell": rub_sell},
        {"rub_buy": rub_buy},
        {"usd_reserve": usd_reserve},
        {"eur_reserve": eur_reserve},
        {"rub_reserve": rub_reserve},
        {"uan_reserve": uan_reserve}
    ]
    with open(path, 'w') as curses_update:
        json.dump(currency_info, curses_update)


login = "root"
passwd = "root"

