"""1. Write a python program to store all the programming languages known to you using
Set."""

# s = input('Enter the string separated by comma').split(",")
# sOne = {i for i in s}
# print(sOne)

"""
2. Write a python program to store your own information {name, age, gender, so on..}
"""
# s = input('Enter the string separated by comma').split(",")
# sOne = {eval(i) for i in s}
# print(sOne)

"""
3. Write a python script to get the data type of a Set.
"""
# s=set()
# s.update(range(10,20),'abc')
# print(type(s))

"""
4.Write a Python script to find if “Python” is present in the set thisset = {"Java",
"Python", "Django"} """

# set = {"Java","Python", "Django"}
# for i in set:
#   if i == "Python":
#     print('Its Present')


"""Write a python program to add items from another set to the current set. 
thisset = {"Java", "Python", "SQL"} secondset= {"C", "Cpp", "NoSQL"}"""

# thisset = {"Java", "Python", "SQL"}
# secondset= {"C", "Cpp", "NoSQL"}

# thisset.add(secondset)
# print(thisset)

"""6. Write a python program to add elements of list to a set
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]"""

# thisset = {"Python", "Django", "JavaScript"}
# mylist = ["Java", "C"]

# thisset.update(["Java","C"])
# print(thisset)

"""7. Write a python program to remove last item of the given set
thisset = {"Python", "Django", "JavaScript", “SQL”}
"""

# thisset = {"Python", "Django", "JavaScript", "SQL"}
# thisset.remove("SQL")
# print(thisset)
# thisset.pop()
# print(thisset)

"""
8. Write a python program to delete the set completely."""
# thisset = {"Python", "Django", "JavaScript", "SQL"}
# thisset.clear()
# print(thisset)

"""Write a python program to loop through the set and print values
thisset = {"Python", "Django", "JavaScript", "SQL"}"""

# thisset = {"Python", "Django", "JavaScript", "SQL"}
# for element in thisset:
#   print(element)

"""10. Write a python program to find the maximum and minimum value in a set."""
# setOne = {10,20,30,40,50,100,180,190,75,85}
# maxValue = 10
# for i in setOne:
#   if i > maxValue:
#     maxValue = i
# print("The maxvalue is:",maxValue)


