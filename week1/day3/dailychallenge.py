#Daily challenge

#Challenge 1: Letter Index Dictionary

word = input("Enter a word: ")

result = {}

for i, letter in enumerate(word):
    if letter in result:
        result[letter].append(i)
    else:
        result[letter] = [i]

print(result)

#Challenge 2: Affordable Items

items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = "$300"

# clean wallet
money = int(wallet.replace("$", "").replace(",", ""))

basket = []

for item, price in items_purchase.items():
    clean_price = int(price.replace("$", "").replace(",", ""))

    if clean_price <= money:
        basket.append(item)
        money -= clean_price

if not basket:
    print("Nothing")
else:
    print(sorted(basket))