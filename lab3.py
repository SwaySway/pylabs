import random
#josue ruiz

def mc_runs():
    print("Monte Carlo with the following inputs")
    print("10000 runs: " + str(m_carlo(10 ** 4)))
    print("100000 runs: " + str(m_carlo(10 ** 5)))
    print("1000000 runs: " + str(m_carlo(10 ** 6)))


def m_carlo(n):
    counter = 0
    for i in range(n):
        result = (random.uniform(-1, 1)) ** 2 + (random.uniform(-1, 1)) ** 2
        if result <= 1:
            counter += 1
        else:
            continue
    return 4 * counter / (1.0 * n)


def sales():
    print("%2f" % salesRecieptPrint(80, 125, 45.5))
    print("%2f" % salesRecieptPrint(95, tax=.105))
    print("%2f" % salesRecieptPrint(12, 5.5, 6.5, 7.5, 9.0, tax=.07))


def salesRecieptPrint(*cost, tax=0.08):
    sum=0
    for i in cost:
        sum = sum + i
    return sum + (sum * tax)


def error():
    print("Goodbye!")


switch = {
    "1": mc_runs,
    "2": sales,
}


def main():
    print("CS 299 Lab 3")
    print("1) Monte Carlo")
    print("2) Sales")
    choice = input("Enter a choice: \n")
    switch.get(str(choice), error)()


if __name__ == "__main__":
    main()