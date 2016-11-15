
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
        return pattern(x-1) + x + pattern(x-1)


def q4():
    print('Beginning List', l)
    double_l = list(map((lambda x: x*2), l))
    print('Double Valued List', double_l)
    odd_list = list(filter((lambda x: x % 2 == 1), [x**2 for x in l]))
    print('List with only odds', odd_list)
    prime_list = list(filter((lambda x: is_prime(x)), l))
    print('List with only primes', prime_list)

print(reverse_string("hello world"))