'Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.'
alp = "аеёиоуыэюя"
word_sug = input().split()
vowel_letters = [sum([True for j in word if j.lower() in alp]) for word in word_sug]

if all(vowel_letters) and len(set(vowel_letters)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")