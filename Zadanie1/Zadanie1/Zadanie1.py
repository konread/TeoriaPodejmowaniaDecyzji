import criterions as crit

if __name__ == '__main__':
    investmentPlanTable = crit.readCSV("source.csv")

    option,max = crit.minMaxUsefull(investmentPlanTable)
    print('MiniMax usefull criterion: ')
    print('Chosen option: ' + str(int(option)))
    print('The amount of investment: ' + str(int(investmentPlanTable[int(option-1)][1])) + ' tys. zł')

    print('')

    option,max = crit.hurwitz(investmentPlanTable, 0.25)
    print('Hurwitz criterion: ')
    print('Chosen option: ' + str(int(option)))
    print('The amount of investment: ' + str(int(investmentPlanTable[int(option-1)][1])) + ' tys. zł')
    print('')
