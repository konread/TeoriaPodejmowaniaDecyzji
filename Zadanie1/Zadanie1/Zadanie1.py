import criterions as crit

if __name__ == '__main__':
    investmentPlanTable = crit.readCSV("source.csv")

    option,value = crit.minMaxUsefull(investmentPlanTable)
    print('MinMax usefull criterion: ')
    print('Chosen option: ' + str(int(option)))
    print('The amount of investment: ' + str(int(investmentPlanTable[int(option-1)][1])) + ' tys. zł')
    print('')

    option,value = crit.savage(investmentPlanTable)
    print('Savage criterion: ')
    print('Chosen option: ' + str(int(option)))
    print('The amount of investment: ' + str(int(investmentPlanTable[int(option-1)][1])) + ' tys. zł')
    print('')

    option,value = crit.hurwitz(investmentPlanTable, 0.25)
    print('Hurwitz criterion: ')
    print('Chosen option: ' + str(int(option)))
    print('The amount of investment: ' + str(int(investmentPlanTable[int(option-1)][1])) + ' tys. zł')
    print('')
    
    option,value = crit.bayes(investmentPlanTable, [0.25, 0.25, 0.25, 0.25])
    print('Bayes criterion: ')
    print('Chosen option: ' + str(int(option)))
    print('The amount of investment: ' + str(int(investmentPlanTable[int(option-1)][1])) + ' tys. zł')
    print('')

    option,value = crit.laplace(investmentPlanTable)
    print('Laplace criterion: ')
    print('Chosen option: ' + str(int(option)))
    print('The amount of investment: ' + str(int(investmentPlanTable[int(option-1)][1])) + ' tys. zł')
    print('')