#Task 5

''' 1)
arr = []

while True:

    print("a - append")
    print("r - remove")
    print("e - exit")   

    choice = input("Enter your choice: ")

    if choice == "a":
        addNum = int(input("Enter a number to add in array: "))
        print("\n")
        arr.append(addNum)

    elif choice == "r":
        rmNum = int(input("Enter a number to remove in array: "))
        if rmNum not in arr:
            print(f"({rmNum}) is not in array")
        else:
            print("\n")
            arr.remove(rmNum)

    elif choice == "e":
        print("Exiting...")
        print("Final array: ", arr)
        break

    else:
        print("Wrong choice, try again!")
'''



''' 2)
my_list_1 = [43, '22', 12, 66, 210, ["hi"]]

# a. დაბეჭდავს 210-ის ინდექსს;
print(my_list_1.index(210))
 
# b. დაამატებს ბოლო ელემენტში ტექსტს "hello";
my_list_1[-1].append("hello")

# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;
my_list_1.pop(2)
print(my_list_1)

# d. შექმენით ახალი სია my_list_2, რომელსაც ექნება my_list_1-ის მნიშვნელობა, გაასუფთავეთ my_list_2-ის მნიშნველობა და დაბეჭდეთ ორივე სია.
my_llist_2 = my_list_1.copy()
my_llist_2.clear()
print("List1: ", my_list_1)
print("List2: ", my_llist_2)
'''


''' 3)
import re

phone_number = input("Enter a phone number (example: (123) 456-789): ")

pattern = r"\(\d{3}\)\s\d{3}-\d{3}"

if re.fullmatch(pattern, phone_number):
    print(phone_number)
else:
    print("Invalid format")
'''
