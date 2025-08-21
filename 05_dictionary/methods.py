#get(key)
person = {
    "name" : "Morshed Alam",
    "age" : 23,
    "city" : "Dinajpur"
}
print(person)
print(person.get("name"))

#keys (সব keys রিটার্ন করে)
print(person.keys())

#values(সব values রিটার্ন করে)
print(person.values())

#items(সব key-value pair রিটার্ন করে)
print(person.items())

#update
person.update({"age":28})
print(person)

#Added
person ["country"] = "Bangladesh"
print(person)

#pop(key)
person.pop("name")
print(person)

#popitem (শেষের key-value pair রিমুভ করে রিটার্ন দেয়)
person.popitem()
print(person)

person.clear()
print(person)

