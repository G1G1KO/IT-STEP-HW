# Task 10

''' 1)
def merge(arr1, arr2):
    if len(arr1) != len(arr2):
        return "Arrays must be the same size!"
    else:
        zipped = zip(arr1, arr2)
        result = [str(item) for item in zipped]
        return result

arr1 = input("1st Array: ").split()
arr2 = input("2nd Array: ").split()
output = merge(arr1, arr2)
print(output)
'''





''' 2)
from functools import reduce

def mult(nums):
    try:
        return reduce(lambda x, y: x * y, nums)
    except TypeError:
        return "Fuction Error: Must Use Numbers Only, Try Again!"


try:
    userInput = input("Enter numbers: ").split()
    nums = [float(item) for item in userInput]
    
    output = mult(nums)
    print(output)

except ValueError:
    print("Error: Must Enter numbers only, Try Again")
'''



''' 3)
userInput = input("Enter Numbers: ").split()
arr = [int(item) for item in userInput]

newArr = list(filter(lambda x: x%2 == 1, arr))

print("New Array", newArr)
'''



''' 4)
def similar(arr: list, word: str):
    newArr = []
    try:
       return list(filter(lambda item: item.endswith(word), arr))
    
    except TypeError:
        print("Error: Endswith Arguments must be char, Try Again!")
    except AttributeError:
        print("Error: List must be Strings only")
    
    return newArr

arr = ['hello', 'world', 'coding', 'nod','running']

newArr = similar(arr, "ing")
print(newArr)
'''