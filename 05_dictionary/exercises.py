self = {
    "name" : "Morshed Alam",
    "age" : 22,
    "country" : "Bangladesh"
}

#All key print
print(self.keys())

#dictionary update
self.update({"age": 28})
print(self)

print(self.get("name"))

self ["city"] = "Dinajpur"
print(self)

del self["age"]
print(self)

