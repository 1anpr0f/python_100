def binary_decimal(num):
    if num == 0:
        return 0
    binary = ''
    while num > 0:
        rem = num % 2
        binary += str(rem)
        num = num // 2
        return binary[::-1]
n = int(input())
result = binary_decimal(n)
print(result)