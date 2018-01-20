def meter(road, feat, price):
    return print(((road/100)*feat)*price)


road_u = float(input("Enter the lenth of way"))
feat_u = float(input("Enter your car`s fuel"))
price_u = float(input("Enter the price of fuel"))
meter(road_u, feat_u, price_u)
