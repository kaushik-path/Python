import numpy as np
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_digits(num):
    return sum(int(digit) for digit in str(num))

def find_factors(num):
    factors = [i for i in range(1, 11) if num % i == 0]
    return factors

user_list = []

for i in range(1, 17):
    element = input(f"Enter element {i}: ")
    user_list.append(int(element))

array_4x4 = np.array(user_list).reshape(4, 4)

primary_diagonal_sum = sum(array_4x4[i][i] for i in range(4))

secondary_diagonal_sum = sum(array_4x4[i][3-i] for i in range(4))

diagonal_sum = primary_diagonal_sum + secondary_diagonal_sum

print("Sum of the diagonals:", diagonal_sum)

if is_prime(diagonal_sum):
    print(f"{diagonal_sum} is a prime number.")
    digit_sum = sum_digits(diagonal_sum)
    print(f"Sum of the digits of the prime number {diagonal_sum} is: {digit_sum}")
else:
    print(f"{diagonal_sum} is not a prime number.")
    factors = find_factors(diagonal_sum)
    print(f"Factors of {diagonal_sum} from 1 to 10 are: {factors}")
