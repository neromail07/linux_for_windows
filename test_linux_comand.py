## Данный код написан исключительно в ознакомительных целях и будет подлежать апгрейду.

print('Привет,это тест на знание основных команд linux консоли. У тебя будет всего 1 попытка,будь внимателен. Тест адоптирован под разные уровни сложности.Приступим.')

## a = 1 введение шансов на ошибку в разработке

name = input ('Как вас зовут ?')
level = int(input('Охарактеризуй уровнь своих знаний от 1 до 3 ,где 1,это "знаю плохо"" и 3 "знаю отлично"'))

ls = 'ls'
cd = 'cd'
mkdir = 'mkdir'
mv = 'mv'
cp = 'cp'
sudo = 'sudo'
install = 'install'
update = 'update'
shutdown = 'shutdown -P now'

if level == 1:
	vopros1 = input('Какая команда отвечает за отображение файлов и папок в репозитории в котором ты находишься: ')
	if vopros1 == ls:
		print("Поздравляю,", name,"вы правильно ответил на вопрос")
		vopros2 = input ('Какая команда отвечает за копирование файлов? : ')
		if vopros2 == cd:
			print(' Здорово и снова правильно,поздравляю!')
			vopros3 = input ('Какая команда отвечает за перемещение файла из одной папки в другую? : ')
			if vopros3 == mv:
				print('Отлично ,ты уже знаешь несколько важных команд,предлагаю перейти на ровень сложности 2.')
				## автоматизированный смена слодности теста без перезапуска программы в разработке.
			else:
				print('Эх жаль, попробуй ещё раз.')
		else:
			print ('Тест окончен.')
	else:
		print("Тест окончен.")
elif level == 2:
		vopros1 = input('Какой командой создаются репозитории? : ')
		if vopros1 == mkdir:
			print('Хорошее начало,', name,'продолжай в том же духе.')
			vopros2 = input('Какая команда отвеяает за переименовывание файла? : ')
			if vopros2 == mv:
				print('Отлично, 2-ой вопрос пройден успешно,приступим в последнему.')
				vopros3 = input('Какая команда производит установку пакета? : ')
				if vopros3 == install:
					print('Поздравляю ,ты прошел 2 уровень сложности теста,попробуй себя на 3-ем уровне!')
				else:
					print('Тест окончен.')
			else:
				print('Тест окончен.')
		else:
			print('Тест окончен.')
elif level == 3:
		vopros1 = input('Команда отвечающая за запуск действия от имени администратора? : ')
		if vopros1 == sudo:
			print('Супер, верно,переходим, к второму вопросу! ')
			vopros2 = input('Команда с помощью которой можно обновить основные пакеты ОС? : ')
			if vopros2 == update:
				print(' Отлично ,остался последний вопрос.')
				vopros3 = input('Какой командой можно выключить компьютер из консоли,при условии что выключить нужно прямо сечас? : ')
				if vopros3 == shutdown:
					print('Поздравляю ,ты прошел тест на максимальной уровне сложности,можешь собой гордиться', name,'жди обновлений !!!')
				else:
					print('Тест окончен.')
			else:
				print('Тест окончен.')
		else:
			print('Тест окончен.')