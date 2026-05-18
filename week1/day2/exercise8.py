#Exercise 8: Pizza Toppings

toppings = []
baseprice = 10
toppingprice = 2.5

while True:
    topping = input('Choose a topping')
    if topping == 'quit':
        break

    print(f'adding {toppings} to your pizza.')
    toppings.append(topping)

    totalprice = baseprice + len(toppings) * toppingprice
    print('Toppings, toppings')
    print('total price', totalprice)
    