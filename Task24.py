'Задача 24: Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.'

n = int(input())
bushes = [int(i) for i in input().split()]
bush_max = 0

for i in range(n):
    bush_sum = bushes[i - 1] + bushes[i] + bushes[i + 1 if i < n - 1 else 0]
    if bush_sum > bush_max:
            bush_max = bush_sum

print(bush_max)