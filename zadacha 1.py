a = float(input('по шкале от 0 до 10, напишите, насколько Вы устали: '))
if a < 0.7:
    print('Кажется, Вы совсем не устали')
elif 0.7 <= a <= 4.8:
    print('Вы немного устали')
elif 4.9 <= a <= 8.5:
    print('Вы знатно устали')
elif 8.6 <= a <= 10:
    print('Вы очень сильно устали')
elif 10.1 <= a <=30:
    print('Вам  нужно ничего не делать в течение 3 дней')
elif a > 30:
    print('Возьмите двухнедельный отпуск')
