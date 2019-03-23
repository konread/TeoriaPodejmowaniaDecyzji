import pandas as pd
import math

def readCSV(filename):
    data = pd.read_csv(filename, sep = ',', index_col='option')
    return data.reset_index().values

def minMaxUsefull(investmentPlanTable):
    currentValue = 0.0
    option = 0
    for row in investmentPlanTable:
        newValue = min(row[2:])
        if newValue > currentValue:
            currentValue = newValue
            option = row[0]

    return option,currentValue

def hurwitz(investmentPlanTable, gamma):
    currentValue = 0.0
    option = 0
    for row in investmentPlanTable:
        newMin = min(row[2:])
        newMax = max(row[2:])
        newValue = (gamma * newMin) + ((1-gamma) * newMax)
        if newValue > currentValue:
            currentValue = newValue
            option = row[0]

    return option,currentValue

def laplace(investmentPlanTable):
    probability = 1.0 / len(investmentPlanTable[0][2:])
    currentValue = 0.0
    option = 0
    for row in investmentPlanTable:
        newValue = 0.0
        for value in row[2:]:
            newValue += (probability*value)
        if newValue > currentValue:
            currentValue = newValue
            option = row[0]

    return option,currentValue

def savage(investmentPlanTable):
    currentValue = 0.0
    option = 0

    max_column = []
    i = 1

    while i <= len(investmentPlanTable[0][2:]):
        max_column.append(max(investmentPlanTable[:, i + 1]))

        i += 1

    max_row = []

    for row in investmentPlanTable:
        matrix_row = []
        i = 0

        for value in row[2:]:
            matrix_row.append(round(max_column[i] - value, 1))
            i += 1

        max_row.append(max(matrix_row))

        option = row[max_row.index(min(max_row))]

    return option,currentValue

def bayes(investmentPlanTable):
    currentValue = 0.0
    option = 0


    return option,currentValue