set_name = {"item1", "item2", "item3"}

fruits = {"Apple", "Orange", "Lemon"}
print(fruits)

fruits.add("Litchi")
print(fruits)

fruits.update(["Mango", "Grape"])
print(fruits)

fruits.remove("Orange")
print(fruits)
fruits.discard("Orange")
print(fruits.clear())