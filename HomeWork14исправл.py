import random
myDict = {}
while True:
    key = input('enter a dishname\n')
    myDict[key] = random.randint(1, 10000)
    if input('would you like to add another item? y/n\n') != 'y':
        break
sum = 0
print('---Cafe"Python"---')

menu_delimiter = '..........................................................'
for key in myDict:
    valueStr = str(myDict[key])
    sum = myDict[key] + sum
    print(key + menu_delimiter[len(key):-len(valueStr)] + valueStr + ' grn')

print('...\n' + 'Total:' + str(sum) + ' grn')
