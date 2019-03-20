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

if __name__ == '__main__':
    investmentPlanTable = readCSV("source.csv")

    option,max = minMaxUsefull(investmentPlanTable)
    print('MiniMax usefull result: ')
    print('Chosen option: ' + str(int(option)))
