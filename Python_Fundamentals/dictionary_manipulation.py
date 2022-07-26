import email


person = {
    "first": "Ada",
    "last": "Lovelace",
    "age": 42,
    "is_organ_donor": True
}
value_reward =person.pop('first')
# person["email"] = "thierynisengwe@gmail.com"
print(person)

if "email" not in person:
    person["email"] = "thierytony123@gmail.com"

print(person["email"])
