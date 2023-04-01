x = dict()
y = {
    "Name":"Dave",
    "Age":32,
    "Roll No":1001,
    "score":{
        "Math":90,
        "science":87,
        "internals":[12,13,12,14,15]
            }
    }
print(y.get("score").get("internals")[0])


y.get("score").get("internals")[0] = 21

print(y.get("score").get("internals")[0])
print(type(y))

y.pop("Name")
print(y)
y.popitem()
print(y)