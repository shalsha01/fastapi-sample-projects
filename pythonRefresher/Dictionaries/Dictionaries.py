"""# This module provides a refresher on Python dictionaries, including creation,
    """
    
user_decision = {
    "name": "shahd",
    "age": 24,
    "city": "baghdad"
}

print(user_decision)
print(type(user_decision))
print(len(user_decision))
print(user_decision["name"])
print(user_decision.get("age"))

user_decision["married a good man "] = "wii happend in the future"
print(user_decision)

user_decision.pop("city")
print(user_decision)

user_decision.update({"age": 25})
print(user_decision)

for x in user_decision:
    print(x) #only the keys will print not the values
    
for x,y in user_decision.items():
    print(x,y) # both keys and values will print

user_decision2= user_decision.copy()
user_decision2["name"] = "ali"
print(user_decision2)

user_decision.clear()