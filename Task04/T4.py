#Task 4

''' 1)
n = input("Enter a String: ")
print(n.encode('utf-8'))
'''


''' 2)
n = input("Enter a String: ")
n = n.strip().lower()

words = n.split()

foundPython = False

for i in range(len(words)):
    if words[i] == "python":
        words[i] = "Python"
        foundPython = True

n = " ".join(words)

if not foundPython:
    n += " Python"

print(n)
'''

''' 3) თუ სიტყვა კენტი ჩარებისგან შედგება არ დამრგვალდება, 
       ანუ თუ სიტყვის ნახევარი არის 2.5, მაშინ დაიბეჭდება 2 ჩარი

str = input("Enter a String: ")
strHalf = int(len(str) / 2)

newStr = str[:strHalf]
print(newStr)
'''



''' 4)
from string import ascii_letters, digits
 
str = input("Enter a String: ")

isValid = True
hasDigit = False
hasLetter = False

if str == "":
    isValid = False

for char in str:

    if char in ascii_letters:
        hasLetter = True
    
    elif char in digits:
        hasDigit = True
        
    else:
        isValid = False
        break

if isValid and hasLetter and hasDigit:
    print("Valid")
else: 
    print("Invalid")
'''


''' 5)
str = input("Enter a String: ")

str_byte = str.encode()
print(str_byte)

byte_str = str_byte.decode()
print(byte_str)
'''


