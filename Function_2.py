def discount_price(price,qty):
    amount = price*qty
    if amount >= 10000:
        discount = 0.1
    elif amount >= 5000:
        discount = 0.05
    elif amount >= 1000:
        dicount = 0.02
    else:
        discount = 0
    return amount - amount * discount

Consetion = discount_price(1000,10)
print(Consetion)
