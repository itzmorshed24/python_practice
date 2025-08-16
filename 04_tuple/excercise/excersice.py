#Tuple Syntax
fruits = ('Apple', 'Orange', 'litchi', 'Mango', 'lemon')
print(fruits)

#first & last item print
print(fruits[0])
print(fruits[-1])

#Apple count
furits_count = fruits.count('Apple')
print(furits_count)

#index two item
print(fruits[2])

#unpack variable
person = ('Morshed', 25, "Dinajpur")
name, age, city = person
print(age)

numberss = (1, 2, 3, 4, 5, 6)
a, b, *rest = numberss
print(rest)

nested_tuple = ("Apple", ('orange', 'litchi', 'jackfruits'), 'lemon')
print(nested_tuple[1][2])
print(nested_tuple[1])

#error Message
nested_tuple.append('litchi')