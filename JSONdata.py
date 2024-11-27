import json


people_string='''
{
    "people"
    : [
        {
            "name": "John",
            "age": 30,
            "city": "New York",
            "email": "john@example.com"
            },
            {
            "name": "Alice",
            "age": 25,
            "city": "London",
            "email": "alice@example.com"
            }
            ]
}
'''

data=json.loads(people_string)
# print(data)

# print(type(data))

for person in data['people']:  #lists all the persons in the list
    print(person)

# for person in data['people']:  # used to access the name of all the persons
#     print(person['name'])
    
# for person in data['people']:  #used to delete the phone number of the person
#     del person['phone']

new_string=json.dumps(data,indent=2) # convert back to its string representation as json 

print(new_string)