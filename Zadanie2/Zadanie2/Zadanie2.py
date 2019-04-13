import re as re
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from sklearn import preprocessing
from collections import deque

def search_dominated_column(data):
    dominated = []
    k1 = 0
    while k1 < len(data.columns):
        last_column = data[k1]
        k2 = k1 + 1
        while k2 < len(data.columns):
            if all(last_column <= data[k2]):
                dominated.append(k2)
            k2 += 1
        k1 += 1

    return list(dict.fromkeys(dominated))

def search_dominated_row(data):
    dominated = []
    k1 = 0
    while k1 < len(data.columns):
        last_column = data[k1]
        k2 = k1 + 1
        while k2 < len(data.columns):
            if all(last_column >= data[k2]):
                dominated.append(k2)
            k2 += 1
        k1 += 1

    return list(dict.fromkeys(dominated))

def generate_value(defaultValue, length):
    list = []
    [list.append(defaultValue) for i in range(length)]

    return list

def main():
    A = 4
    
    print("Dla A=" + str(A))
    print()

    data = pd.read_csv('data.csv', sep = ';', header = None)
    data = data.replace('A', A)
    data = data.astype(float)

    dominated_column = search_dominated_column(data)
    dominated_row = search_dominated_row(data.T)

    print("Kolumny zdominowane: " + str(dominated_column))
    print("Wiersze zdominowane: " + str(dominated_row))
    print()

    data = data.drop(data.index[dominated_row])
    data = data.drop(dominated_column, axis=1)

    min_row = data.min(axis = 1)
    max_column = data.max()
    
    max_min_row = max(min_row)
    min_max_column = min(max_column)
    
    id_max_min_row = min_row.idxmax()
    id_min_max_column = max_column.idxmin()

    print("Max min row: " + str(max_min_row))
    print("Min max column: " + str(min_max_column))
    print("Id max min row: " + str(id_max_min_row))
    print("Id min max column: " + str(id_min_max_column))
    print()

    if max_min_row == min_max_column:
        print("Rozwiązanie w zbiorze strategii czystych VA = VB = " + str(max_min_row))
        print()
    else:
        print("Rozwiązanie w zbiorze strategii mieszanych VA=" + str(max_min_row) + ", " + "VB=" + str(min_max_column))
        print()

        data1 = data.copy()
        data2 = data.copy()

        resultFinal = generate_value(0, len(data) + 1)
        resultFinal[len(data)] = 1

        condition1 = generate_value(0, len(data1.columns))
        condition1[0] = -1
        condition1[1] = -1

        resultPart1 = generate_value(0, len(data1) + 1)
        resultPart1[0] = 1
        resultPart1[1] = 1

        data1.loc[len(data1)] = condition1
        data1[len(data1)] = resultPart1

        ax = np.array(data1.T.values)
        bx = np.array(resultFinal)
        x = np.linalg.solve(ax, bx)

        print("Optymalna strategia gracza A wynosi: x=[" + str(round(x[0], 2)) + " " + str(round(x[1], 2)) + "]")

        condition2 = generate_value(0, len(data2) + 1)
        condition2[0] = -1
        condition2[1] = -1

        resultPart2 = generate_value(0, len(data2.columns))
        resultPart2[0] = 1
        resultPart2[1] = 1

        data2.loc[len(data2)] = resultPart2
        data2[len(data2)] = condition2

        ay = np.array(data2.values)
        by = np.array(resultFinal)
        y = np.linalg.solve(ay, by)
    
        print("Optymalna strategia gracza B wynosi: y=[" + str(round(y[0], 2)) + " " + str(round(y[1], 2)) + "]")

        print()

if __name__ == "__main__":
    main()
