#Exercise 1: Favorite number

fav_num = {1, 2, 3, 4, 5}
fav_num.add(6)
print(fav_num)
fav_num.add(7)
print(fav_num)

fav_num.remove(7)
print(fav_num)

f_fav_num = {8, 9, 10, 11, 12}
our_fav_num = fav_num.union(f_fav_num)
print(our_fav_num)