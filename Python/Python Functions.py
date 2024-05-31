# Activity 1

def show_list_content(list):
    print("Show the list content:", list)

def find_max_value(list):
    return max(list)

sample_list = [10, 2, 3, 4, 7]

show_list_content(sample_list)

max_value = find_max_value(sample_list)
print("Maximum value in the list:", max_value)

# Activity 2

def factorial(n):
    if n < 0:
        print("Factorial number does not exist for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

num = int(input("Input a number: "))
print("The factorial number of", num, "is", factorial(num))

# Activity 3

def is_prime(num):
    if num <= 1 :
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Input a prime number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
    