#Task 2

''' 1)
num_list = [44, 23, 11, 8, 20, 56, 33, 55]

num = eval(input("Enter a Number: "))
if num in num_list:
    print(f"{num} Is In The List")
else:
    print(f"{num} Is Not In The List")
 '''


''' 2)
num = int(input("Enter a Number: "))
if num % 2 == 0:
    print("The Number Is Even")
else:
    print("The Number Is Odd")
'''



'''3) is ამოწმებს არის თუ არა ეს ორი ცვლადი ერთი და იგივე მეხსიერებაში. 
     ამ დავალებაში ცვლადები input()-ით რომ შემოგვეტანა და შედარება Is-ით გვექნა,
     ერთი და იგივე ცვლადების შემთხვევაშიც დაწერდა "Different object", 
     რადგან ეს ორი ცვლადი ერთი და იგივე მეხსიერებაზე არ მიუთითებდა.
    
st1 = "TSU"
st2 = "TSU"

if st1 is st2: 
    print("Same object")
else:
    print("Different object")
'''



''' 4)
num_list = [44, 23, 11, 8, 20, 56, 33, 55]
num = eval(input("Enter a Number: "))

# თუ შეტანილი რიცხვი მეტია სიაში არსებულ მე-3 ელემენტზე და ნაკლებია ბოლო ელემენტზე გამოიტანეთ ტექსტი "More than list elements";
if num_list[2] < num < num_list[-1]:
    print("More Than List Elements")

# * თუ შეტანილი რიცხვი უდრის სიის მე-6 ელემენტს გამოიტანეთ ტექსტი "Equal";
elif num == num_list[5]:
    print("Equal")

# * სხვა ნებისმიერ შემთხვევაში გამოიტანეთ ტექსტი "None of the conditions were met".
else:
    print("None Of The Conditions Were Met.")
'''


