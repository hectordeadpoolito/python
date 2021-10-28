def my_soul_price(gross_price, deadpool):
    if isinstance(deadpool, int):
        deadpool = deadpool * 0.01

    return int(gross_price) + deadpool

print(my_soul_price(3.20, 99))
print(my_soul_price(3.20, 0.89))
print(my_soul_price(3.20, 0.8889))
print(my_soul_price(3.10, 0.89))