# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def stepen_numbers(A, B):
    if (B == 1):
        return A
    if B != 1:
        return A * stepen_numbers(A, B - 1)


A = int(input())
B = int(input())
print(stepen_numbers(A, B))
