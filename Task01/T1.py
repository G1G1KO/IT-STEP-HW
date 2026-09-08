#Task1

''' 1)

X = eval(input("Enter X: "))
Y = eval(input("Enter Y: "))

print("X + Y =", X + Y)
print("X - Y =", X - Y)
print("X * Y =", X * Y)
print("X / Y =", X / Y)
print("X // Y =", X // Y)
print("X % Y =", X % Y)
print("X^Y = ", X ** Y)
'''


''' 2)
diag1 = eval(input("Enter 1st Diagonal: "))
diag2 = eval(input("Enter 2nd Diagonal: "))

if diag1 > 0 and diag > 0:
    rhombusArea = (diag1 * diag2) / 2
    print("Rhombus Area = ", rhombusArea)
else:
    print("Lengths Must Be Positive, Try Again!")
'''

'''3)
meters = eval(input("Enter Meters: "))
cm = meters * 100
dm = meters * 10
mm = meters * 1000
mile = meters * 0.000621371192
print(f"{meters} M = {cm} CM")
print(f"{meters} M = {dm} DM")
print(f"{meters} M = {mm} MM")
print(f"{meters} M = {mile} Mile")
'''


''' 4)
top = eval(input("Enter Triangle Height: "))
bottom = eval(input("Enter Triangle Bottom: "))

if top > 0 and bottom > 0:
    trArea = (top * bottom) / 2
    print("Triangle Area = ", trArea)

else:
    print("Lengths Must Be Positive, Try Again!")
'''



''' 5)
num = eval(input("Enter 2 Digit Number: "))
if num < 10 or num > 99:
    print("This Number is not 2 Digit, Try Again!")
else:
    digitSum = (num % 10) + (num // 10)
    print("Sum = ", digitSum)    
'''