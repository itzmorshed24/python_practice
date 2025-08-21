person = {
    'name' : 'Morshed',
    'age' : 25,
    'city' : "Dinajpur"
}
print(person["name"])
print(person.get("age"))
person["Country"]="Bangladesh" #add new item
person["age"]= 26       # Chance Value
print(person)
person.pop("city")      #remove key
print(person)

person.popitem()
del person["age"]
print(person)
person.clear()
print(person)

