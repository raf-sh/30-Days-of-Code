# variables
mealCost = float(input())
tipPercent = float(input())
taxPercent = float(input())

#

totalCost = mealCost + (mealCost * tipPercent / 100.00) + (mealCost * taxPercent / 100.00)

print('The total meal cost is ' + str(int(round(totalCost))) + ' dollars.')
