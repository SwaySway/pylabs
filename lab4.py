import math

"""
Josue Ruiz
CS 299
Lab 4
"""


def median(data_lst):
    data_lst = sorted(data_lst)
    len_size = len(data_lst)
    position = (len_size - 1) // 2

    if len_size % 2:
        return data_lst[position]
    else:
        return (data_lst[position] + data_lst[position + 1])/2.0


def index(d_list, pos):
    list_size = len(d_list)
    if pos not in d_list:
        return -1
    for i in range(list_size):
        if pos is d_list[i]:
            return i


def reverse(d_lst):
    return d_lst[::-1]


# First Part - Part A
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


# Second Part of assignment
# Part A
lst = reverse(lst)
print("Reversed List from Part 1\n", lst)

# Part B
rev_lst = index(lst, 'armor')
print("Trying to find word that doesn't exist such as \"armor\" \n", rev_lst)
rev_lst2 = index(lst, 'cat')
print("Trying to find word that exists such as \"cat\" \n", rev_lst2)


# Part C
aList = [24, 5, 8, 2, 9, 15, 10]
med_aList = median(aList)
print("Current List ", aList, "\nImplemented Median:\n", med_aList)
bList = [24, 5, 8, 2, 9, 15, 10, 54]
med_bList = median(bList)
print("Current List ", bList, "\nImplemented Median:\n", med_bList)
