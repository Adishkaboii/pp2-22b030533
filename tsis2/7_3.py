You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)
  
  Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)
  
  ------------------------
  
  Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

-----------------------------------

Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

Print the name of child 2:

print(myfamily["child2"]["name"])

---------------------------------------------------
Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

clear() -	Removes all the elements from the dictionary
copy() -	Returns a copy of the dictionary
fromkeys() -	Returns a dictionary with the specified keys and value
get() -	Returns the value of the specified key
items() -	Returns a list containing a tuple for each key value pair
keys() -	Returns a list containing the dictionary's keys
pop() -	Removes the element with the specified key
popitem() -	Removes the last inserted key-value pair
setdefault() -	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update() -	Updates the dictionary with the specified key-value pairs
values() -	Returns a list of all the values in the dictionary
