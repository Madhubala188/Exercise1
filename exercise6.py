#Write a program that draws two random combinations of numbers for a combination lock:
import random
def generate_combination(length, min_value, max_value):
    # Generate a combination of random numbers within the specified range
    return [random.randint(min_value, max_value) for _ in range(length)]
# Generate a 3-digit code where each number is between 0 and 9
combination1 = generate_combination(4, 0, 7)
# Generate a 4-digit code where each number is between 1 and 6
combination2 = generate_combination(3, 2, 5)

print(f"3-digit combination: {combination1}")
print(f"4-digit combination: {combination2}")