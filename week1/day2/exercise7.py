#Exercise 7: Favorite fruits


fav_fruit = input("What is your favorite fruits? ")
fav_fruit_list = fav_fruit.split(",") 
testfruit = input('check your favorite fruit:')
if testfruit in fav_fruit_list:
    print("You really like ")
else:
    print('Thats new to you')