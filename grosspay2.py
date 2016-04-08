def getInput(inputDescription):
    getInputVariable = input('Enter ' + inputDescription + ': ')
    return (getInputVariable)
def floatCast(inputDescription):
    floatCastVariable = getInput(inputDescription)
    try:
        floatCastVariable=float(floatCastVariable)
        if floatCastVariable < 0:
            print ("cannot work negative hours please enter a valid number")
            return (floatCast(inputDescription))
        else:
            return (floatCastVariable)
    except ValueError:
        print ('please enter numerical value')
        return (floatCast(inputDescription))
def calculateGrossPay():
    hours=floatCast('Hours Worked')
    wage=floatCast('Wage')
    if hours <= 40:
       gross= hours*wage
    else:
       gross='%.2f'%((hours * wage) + ((hours-40) * (wage*0.5)))
    gross= str(gross)
    return gross
print ("Gross Wage: " + calculateGrossPay())