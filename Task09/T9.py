# Task 1

''' 1)
int_list = [10,20,30,40]

def addInteger(num):
    int_list.append(num)

num = int(input("Enter an Integer to add in the global array: "))
addInteger(num)
print(int_list)
'''


''' 2)
def calculate_sum(arr):    
    total = 0
    for number in arr:
        total += number
    return total


my_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

result = calculate_sum(my_list)
print("Sum:", result)
'''



''' 3)
gl_str = "Global"

def my_function():
    gl_str = "Local"
    return gl_str  

print("Fuction returned:", my_function()) #Local

print("Global:", gl_str) #Global
'''



''' 4)
def numSum(num):
    if num == 0:
         return 0

    sum = num % 10 + numSum(num // 10)
    return sum
    
num = 120345
sum = numSum(num)
print(sum)
'''


''' 5)
def strRevers(word):

    if word == "":
        return ""
    
    return word[-1] + strRevers(word[:-1])

word = "hello"
newWord = strRevers(word)
print(newWord)
'''
