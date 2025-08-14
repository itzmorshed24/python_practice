#append(x)
number = [10, 20, 30, 40, 50, 60, 70, 80]
number.append(90)
print(number)

#insert(i,x)
fruits = ['apple', 'orange', 'litchi', 'lemon',]
fruits.insert(2,"jackfruits")
print(fruits)

#remove(x)
fruits = ['apple', 'orange', 'litchi', 'lemon',]
fruits.remove('lemon')
print(fruits)

#pop(i)
fruits = ['apple', 'orange', 'litchi', 'lemon',]
fruits.pop(1)
print(fruits)

#clear()
fruits = ['apple', 'orange', 'litchi', 'lemon',]
fruits.clear()
print(fruits)

#sort()
friend_age = [25, 22, 22, 34, 35, 26, 21, 18, 17, 54, 52, 26, 12, 18]
friend_age.sort()
print(friend_age)

#reverse
friend_age1 = [25, 22, 22, 34, 35, 26, 21, 18, 17, 54, 52, 26, 12, 18]
friend_age1.reverse()
print(friend_age1)

#count(x)
number1 = [2, 4, 6, 8, 1, 2, 3, 4, 5, 6, 8, 6, 4, 2, 3, 5, 6, 4, 8, 2, 1, 2, 3, 2, 3, 1]
number2 = number1.count(2)
print(number2)
number8 = number1.count(8)
print(number8)

#copy
flower = ['shapla', 'bely', 'bokul', 'kadam',]
new_flower = flower.copy()
print(new_flower)


