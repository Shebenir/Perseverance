'Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.'
def power(num1, num2):
    if num2 == 0:
        return 1

    return num1 * power(num1, num2 - 1)


num = power(int(input('number: ')), int(input('degree: ')))
print(f'number is {num}')