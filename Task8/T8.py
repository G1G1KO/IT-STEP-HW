#Task 8

''' 1)
def fib(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)
    
num = int(input("Enter an integer: "))
fibo = fib(num)
print(f"Fibonacci = {fibo}")
'''


''' 2)
def is_anagram(str1, str2):
    clean_str1 = str1.lower().replace(" ", "")
    clean_str2 = str2.lower().replace(" ", "")
    
    return sorted(clean_str1) == sorted(clean_str2)

word1 = "race"
word2 = "care"
print(f"Is '{word1}' and '{word2}' Anigmas? -> {is_anagram(word1, word2)}")
'''

''' 3)
def factorial(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Enter an Integer: "))
fact = factorial(num)
print(f"Factorial for {num} is {fact}")
'''



''' 4)
def countCharacter(text, char):
    return text.count(char)

# შემოწმება:
text = "We Love Paata"
char = "a"

result = countCharacter(text,char)
print(f"Symbol '{char}' is repeated {result} times")
'''