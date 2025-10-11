#Assignment5

import json

person = {
    "name": "John",
    "age": 28,
    "skills": ["Python", "Django", "Machine Learning"]
}

with open('person.json','w') as f:
    json.dump(person , f)

print("file created successfully")

with open('person.json','r') as fr:
    frr = json.load(fr)
print(frr)




