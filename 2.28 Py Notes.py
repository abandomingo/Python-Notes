#dictionary - like a map on C++ 

student = {'first' : 'aban',
            'last' : ' domingo',
            'id' : '87249424',
            'major' : 'Comp Sci'}
print(type(student))

fname = student["first"].title()
print(fname) #title() is a built in f(x) that caps Names but not filler like is, of, the
print(student)

student['major'] = " Nursing"
student['first'] = fname

print(student)

poll_response = { "Angela" : "n/a", "Austin" : "n/a", "Aban" : " n/a", "Gothem" : "n/a", }

poll_response['Angela'] = "Zoom"
poll_response['Aban'] = "Zoom"
poll_response["Austin"] = "Live"
poll_response["Gothem"] = "Live"

for k in poll_response.keys():
    print(poll_response[k]) #print a fornat string blank "chose" blank // f allows you to place the variables in a string without taking it outside the " "

for k,v in poll_response.items():
    print(f"{k} chose {v}") #print a fornat string blank "chose" blank // f allows you to place the variables in a string without taking it outside the " "

items = poll_response.items()
print(items)

response = poll_response.get('Nate', 'Invalid Key')
print(response)

for v in poll_response.values():
    pass 

del student['major']
print(student)

print(poll_response.keys())

keys = poll_response.keys()
print()