#Josue Ruiz Lab 3 Part 2

def salesRecieptPrint(*cost, tax=0.08):
    sum=0
    for i in cost:
        sum = sum + i
    return sum + (sum * tax)


print("%2f" % salesRecieptPrint(80, 125, 45.5))
print("%2f" % salesRecieptPrint(95, tax=.105))
print("%2f" % salesRecieptPrint(12, 5.5, 6.5, 7.5, 9.0, tax=.07))
