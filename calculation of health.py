print('Данная программа на основе средней статистики и может дать заключение по состоянию здоровья')
name = input('Напищите своё Имя: ')
later = int(input('Укажите свой возраст: '))
mass = int(input('Укажите свой вес: '))

if later <= 29 and mass >= 70 and mass <= 120 or later >= 29 and mass >= 70 and mass <= 120:
    print(f'{name} у вас хорошее состояние здоровья, так держать!')
else:
    later >= 29 and mass <= 70  or mass >= 120
    print(f'{name} у вас плохое состояние здоровья, обратитесь к врачу!')