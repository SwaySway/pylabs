
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def reverse_string(x):
    if x == "":
        return x
    else:
        return x[len(x)-1] + reverse_string(x[:len(x)-1])


def pattern(x):
    x = str(x)
    if x == "0":
        return x
    else:
        return pattern(int(x)-1) + x + pattern(int(x)-1)


def generic_sort(func, seq):
    for i in range(len(seq)):
        for j in range(len(seq)-1-i):
            if func(seq[j], seq[j+1]):
                seq[j], seq[j+1] = seq[j+1], seq[j]

    return seq


def less_sort(x, y):
    if x < y:
        return True
    else:
        return False


def greater_sort(x, y):
    if x > y:
        return True
    else:
        return False


def q1():
    print("Printing abc in reverse:", reverse_string("abc"))
    print("Printing hello, world! in reverse:", reverse_string("hello, world!"))


def q2():
    print(pattern(0)+'\n'+pattern(1)+'\n'+pattern(2)+'\n'+pattern(3)+'\n'+pattern(4))


def q3():
    seq = [5, 2, 12, 4, 9, 13, 22, 1, 6, 17]
    seq2 = ["Kate", "Sam", "Kate", "Jolly", "Alp", "Beta", "Alpine", "Samuel", "Bob", "Joy"]
    name_age = [("Kate", 3), ("Sam", 2), ("Kate", 5), ("Jolly", 1), ("Alp", 2), ("Beta", 3), ("Alp", 1), ("Alpine", 2),
               ("Sam", 4), ("Bob", 2), ("Sam", 3)]
    print(generic_sort(less_sort, seq))
    print(generic_sort(greater_sort, seq2))
    print(generic_sort(greater_sort, name_age))


def q4():
    l = [x for x in range(1, 21)]
    print('Beginning List', l)
    double_l = list(map((lambda x: x*2), l))
    print('Double Valued List', double_l)
    odd_list = list(filter((lambda x: x % 2 == 1), [x**2 for x in l]))
    print('List with only odds', odd_list)
    prime_list = list(filter((lambda x: is_prime(x)), l))
    print('List with only primes', prime_list)


def main():
    q1()
    q2()
    q3()
    q4()


if __name__ == "__main__":
    main()