import math


def calculate_czuprow(data):
    r = len(data[0])
    k = len(data)
    total_sum = sum_all(data)

    chi_squared = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            n_d = sum_row(data, i) * sum_column(data, j) / total_sum
            chi_squared = chi_squared + ((data[i][j] - n_d)**2 / n_d)
            print("f_{},{} = {}".format(i, j, data[i][j]))
            print("fd_{},{} = {}".format(i, j, n_d))
            print("(f_{},{} - fd_{},{})**2 = {}".format(i, j, i, j, (data[i][j] - n_d)**2))
            print("(f_{},{} - fd_{},{})**2 / fd = {}".format(i, j, i, j, (data[i][j] - n_d)**2 / n_d))
            print("-------------------")

    print("chi_squared = {}".format(chi_squared))
    return math.sqrt(chi_squared / (total_sum * math.sqrt((r-1)*(k-1))))


def calculate_cramer(data):
    r = len(data[0])
    k = len(data)
    total_sum = sum_all(data)

    chi_squared = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            n_d = sum_row(data, i) * sum_column(data, j) / total_sum
            chi_squared = chi_squared + ((data[i][j] - n_d) ** 2 / n_d)
    return math.sqrt(chi_squared / (total_sum * min(r-1, k-1)))



def sum_column(d, k):
    s = 0
    for i in range(len(d)):
        for j in range(len(d[i])):
            if j == k:
                s = s + d[i][j]
    return s


def sum_row(d, r):
    s = 0
    for v in d[r]:
        s = s + v
    return s


def sum_all(d):
    s = 0
    for r in range(len(d)):
        s = s + sum_row(d, r)
    return s


with open("data_rp.txt") as textFile:
    data_rp = [[int(num) for num in line.split()] for line in textFile]
    print("RP")
    print("Czuprow: {}".format(calculate_czuprow(data_rp)))
    print("Cramer: {}".format(calculate_cramer(data_rp)))

with open("data_rww.txt") as textFile:
    data_rww = [[int(num) for num in line.split()] for line in textFile]
    print("RWW")
    print("Czuprow: {}".format(calculate_czuprow(data_rww)))
    print("Cramer: {}".format(calculate_cramer(data_rww)))