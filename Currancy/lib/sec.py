import json

path = 'db\passkeys.json'


def authorise(login,password):
    with open(path) as passkeys:
        currency_data = json.load(passkeys)
        current_login = currency_data[0]
        current_password = currency_data[1]

        if login == current_login:
            if password  == current_password:
                return True
        else:
            return False
