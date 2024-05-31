# Activity 1
n = 50
num1 = 0
num2 =1

next_number = num2
count = 1

while count <= n :
    print(next_number, end=" ")
    count += 1

    num1, num2 = num2, next_number
    next_number = num1 + num2
    print()

# Activity 2

num = int(input("Input a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
