import pymysql


def get_info():
    connect = pymysql.connect(host="localhost", user="dark.loc", password="dark.loc", db="dark.ex.loc")
    cursor = connect.cursor()
    query = ("SELECT * FROM main")
    cursor.execute(query)
    data = cursor.fetchone()
    print(data)
    return data


data = get_info()
usd_buy = data[0]
usd_sell = data[1]
eur_buy = data[2]
eur_sell = data[3]
rub_buy = data[4]
rub_sell = data[5]

usd_reserve = data[7]
uan_reserve = data[9]
eur_reserve = data[6]
rub_reserve = data[8]


def insert_to_db(usd_reserve, uan_reserve, eur_reserve, rub_reserve):
    usd__reserve = float(usd_reserve)
    uan__reserve = float(uan_reserve)
    #eur__reserve = float(eur_reserve)
    #rub__reserve = float(rub_reserve)

    connect = pymysql.connect(host="localhost", user="dark.loc", password="dark.loc", db="dark.ex.loc")
    cursor = connect.cursor()
    cursor.execute("UPDATE `main` SET `usd_reserve`=usd__reserve ,`uan_reserve`=uan__reserve")
    data_1 = cursor.fetchone()
    print(data_1)
    print("Insert")

