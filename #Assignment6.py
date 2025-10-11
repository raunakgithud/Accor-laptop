#Assignment6

library = {
    "name": "City Library",
    "books": [
        {"title": "Book A", "author": "Author X", "year": 2005},
        {"title": "Book B", "author": "Author Y", "year": 2010},
        {"title": "Book C", "author": "Author Z", "year": 2015}

    ]
}

import json

with open('library.json','w') as lib:
    json.dump(library , lib)

print("json writen successfully")

with open('library.json','r') as rd:
    r1 = json.load(rd)
     
print(r1['books'][1]['title'])
print(r1['books'][2]['title'])





