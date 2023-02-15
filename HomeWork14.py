import random
myDict = {}
while True:
    key = input('enter a dishname\n')
    myDict[key] = random.randint(1, 10000)
    if input('would you like to add another item? yes/no\n') != 'y':
        break
sum = 0
print('---Cafe"Pyhton"---')

menu_delimiter = '..........................................................'
for key in myDict:
    valueStr = str(myDict[key])
    sum = myDict[key] + sum
    print(key + menu_delimiter[len(key):-len(valueStr)] + valueStr + ' grn')

print('...\n' + str(sum) + ' grn')