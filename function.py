'''
Функции во вложенных конструкциях - это работа внутри или вне функции дополнительными методами
'''

def average_grade():
    grade = int(input('Оценка (0 - завершить): '))
    total = 0 
    average = 0
    while grade != 0:
        average += grade
        total += 1
        grade = int(input('Оценка (0 - завершить): '))
    average /= total
    # if average >= 4:
    #     return 50
    # else:
    #     return 25

# print('Скидка в магазин манги (%):', average_grade())


# def mesto_bal():
#     bal = int(input("Введите кол-во баллов (0 - завершить): "))
#     total = 0
#     while bal != 0:
#         total += bal
#         bal = int(input("Введите кол-во баллов (0 - завершить): "))
#     if total >= 80:
#         print("Первое место! Вы получаете - НИЧЕГО!")
#     elif total >= 60:
#         print("Второе место! Вы получаете 20.000$ и поездку в Дубай")
#     elif total >= 40:
#         print("Третье место! Вы получаете грантовую основу на учебу в Стэндфорде, а также личную встречу с Илоном Маском в компании SpaceX")
    
# mesto_bal()

def mesto_bal():
    average = average_grade()
    if average >= 5:
        print("Первое место! Вы получаете - НИЧЕГО!")
    elif average >= 4:
        print("Второе место! Вы получаете 20.000$ и поездку в Дубай")
    elif average >= 3:
        print("Третье место! Вы получаете грантовую основу на учебу в Стэндфорде, а также личную встречу с Илоном Маском в компании SpaceX")

mesto_bal()
