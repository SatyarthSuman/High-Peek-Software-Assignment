nameOfGoodies = input('Enter the goodies :').split()
priceOfGoddies = input('Enter the price of goodies :').split()
res = {} 
lenOfGoodies = len(nameOfGoodies)
for key in nameOfGoodies: 
    for value in priceOfGoddies: 
        res[key] = value 
        priceOfGoddies.remove(value) 
        break


#print(res)
res1 = dict(sorted(res.items(), key=lambda item: item[1]))
#print(res1)


numberOfEmployee = int(input("Enter the number of emplyee :"))
#print('...............................................................')
if (lenOfGoodies >= numberOfEmployee):
    arr = res.values()
    #print(arr)
    list_arr = list(arr)
    #print('List of arr', list_arr)
    #print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(int(list_arr[numberOfEmployee -1]) - int(list_arr[0]))
else:
    print('Number of goodies should be greater or equal to Number of Employee')
