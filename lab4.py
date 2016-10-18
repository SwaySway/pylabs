import math
"""
Josue Ruiz
CS 299


First Problem of Lab 4
"""
# Part A
lst = ["Hello", 7, 7, 9, 'a', 'cat', False]
print("Created list:\n", lst)

# Part B
lst.append(math.pi)
lst.append(7)
print("Added PI and another 7\n", lst)

# Part C
lst[3] = 'dog'
print("Added the word dog in position 3\n", lst)

# Part D
indx = lst.index('cat')
print("Index number for \'cat\' is ", indx)

# Part E
occurrence = lst.count(7)
print("In the list the number 7 shows up ", occurrence, " times.")

# Part F
lst.remove(7)
print("Removed the first 7 from the list\n", lst)

# Part G
lst.pop(lst.index('dog'))
print("List with dog removed by finding the index and then removing with pop\n", lst)

