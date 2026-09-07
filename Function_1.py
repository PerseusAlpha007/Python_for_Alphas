def create_a_dictionary(product,price):
    print(product,price)
    jason = dict()
    if len(product) != len(price):
        print("No. of Products and Prices not match")
    else:
        for i in range(len(product)):
            jason[product[i]] = price[i]
    return jason




d = create_a_dictionary(["monitor","keyboard","cabinet"] , [6000 , 700 , 4000])
print(d)