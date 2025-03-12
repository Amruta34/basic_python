"""
Write a Python program that takes two numbers, start and end, and prints all prime numbers in that range.

Example:
  For start = 10, end = 30:
  11, 13, 17, 19, 23, 29
"""
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            return False
    return True
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
print("Prime numbers in the range:", end=" ")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
