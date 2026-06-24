#Task 7


''' 1)
userInput = input("Enter Array Elements (separated by space): ")

arr = [i for i in userInput.split()]

newArr = set(arr)
print(newArr)
'''


''' 2)
userInput = input("Enter Array Elements (separated by space): ")

elements = userInput.split()

frozenElements = frozenset(elements)

print(frozenElements)
'''



''' 3)
set1 = {1, 2, 3, 4, 5} 
set2 = {3, 4, 6, 7, 8, 9}

tupleMerge = tuple(set1 | set2)
print(tupleMerge)
'''


''' 4)
userInput = input("Enter Array Elements (separated by space): ")

arr = tuple([int(i) for i in userInput.split()])
uniqueList = list(set(arr))
print(uniqueList)
'''

''' 5)
arr = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

for name, age in arr:
    print(f"Name: {name}, Age: {age}")
'''



''' 6)
arr1 = ["Irakli", "Giorgi", "Nona", "Oto"]
arr2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]

commonUser = set(arr1) & set(arr2)
print(list(commonUser))
'''