#Task 3

''' 1)
 ამ ამოცანის რამდენიმე გზით გაკეთებაა შესაძლებელი, მაგალითად
   else-ში while-ს მაგივრად პირდაპირ sum = sum(range(n + 1)) რომ დაგვწერა,
   ან else-ში while-ს მაგივრად მათემატიკური ფორმულა გამოგვეყენებინა sum = (n * (n + 1)) // 2


n = int(input("Enter a Number: "))
sum = 0
i = n

if n < 0:
    print("Enter Positive Number!")

else:
     while n > 0:
        sum += n
        n -=1

print(f"{i}'s Arithmetic Sum = {sum}")
'''


''' 2)
n = int(input("Enter an Integer: "))

if n <= 0:
    print("Enter Positive Integer!")

else:
    while n > 0:
        print(n, end=" ")
        n -= 1
'''



''' 3)
n = 10

while True:
    guess = int(input("Enter an Integer: "))
    
    if n == guess:
        print("You Win!")
        break

    else:
        print("Try Again")
'''
    

''' 4)
total_sum = 0

while True:
    num = input("Enter a Number: ")

    if num == "sum":
        break

    else:
        n = int(num)
        if n > 0:
            total_sum += n

print(f"Sum = {total_sum}")
'''