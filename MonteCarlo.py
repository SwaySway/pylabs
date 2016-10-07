#Josue Ruiz Lab 3 Part 1
import random

def m_carlo(n):
    counter = 0
    for i in range(n):
        result = (random.uniform(-1, 1)) ** 2 + (random.uniform(-1, 1)) ** 2
        if result <= 1:
            counter += 1
        else:
            continue
    return 4 * counter / (1.0 * n)


print("Monte Carlo with the following inputs")
print("10000 runs: " + str(m_carlo(10 ** 4)))
print("100000 runs: " + str(m_carlo(10 ** 5)))
print("1000000 runs: " + str(m_carlo(10 ** 6)))

