

def charge(total_checks, counter):
    while total_checks > 0:
        if 1 <= total_checks <= 20:
            counter += total_checks * .10
            total_checks = 0
        elif 21 <= total_checks <= 50:
            counter += total_checks * .07
            total_checks -= 20
        elif total_checks >= 51:
            counter += total_checks * .05
            total_checks -= 51
    return counter


def bank_account(name, fee, *args):
    total_checks = 0
    counter = 0
    for arg in args:
        total_checks = arg + total_checks

    total = charge(total_checks, counter)
    bank_charge = fee + total
    print(name, " has a deposited a total of ", total_checks, " checks")
    print("They will be charged ", bank_charge)

# Question 1 of Exam Part 2
bank_account("Jack", 10, 15, 29, 18, 7)
bank_account("Joan", 10, 36)
bank_account("David", 20, 3, 5, 2, 6)
bank_account("Diana", 20, 0)


# def format_list(list1, list2):
#     if len(list1) != len(list2):
#         print("Error not same size")
#     else:
#         tup = list(zip(list1, list2))
#         print("merged together", tup)
#         print()
# #
# format_list([13, 3, 25 , 7 ,21, 2, 50, 2, 13, 40, 34, 14, 6, 16], [1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1])
# format_list([])
