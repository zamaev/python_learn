'''
Напишите интерпретатор языка управления роботом. Интерпретатор -- функция с именем `execute()`, принимающая на вход один параметр с именем `code`, который тоже строка и содержит код управляющей программы робота. Программа представляет из себя строку, содержащую набор команд движения робота. Например: `"FRL"` .

- F - движение вперед на одну клетку
- R - поворот робота на 90 градусов по часовой стрелке без движения
- L - поворот робота на 90 градусов против часовой стрелки без движения

Результатом выполнения функции `execute()` должна стать  двумерная карта движения робота.Пути движения робота могут пересекаться.**Примеры**.

1. Входные данные

```
"FFFFFLFFFFFLFFFFFLFFFFFL"
```

Выходные данные

```
******
*    *
*    *
*    *
*    *
******
```

2. Входные данные

```
"LFFFFFRFFFRFFFRFFFFFFF"
```

Выходные данные

```
    ****
    *  *
    *  *
********
    *
    *
```

**Ограничения:** Нельзя использовать классы. Решение не должно быть в одной функции.
'''


def get_road(code):
	direction_options = (1+0j, 0-1j, -1+0j, 0+1j)
	current_direction = 0
	road = [0+0j]

	for command in code:
		if command == 'F':
			next_pos = road[-1] + direction_options[current_direction]
			road.append(next_pos) 
		elif command == 'L':
			current_direction = (current_direction - 1) % len(direction_options)
		elif command == 'R':
			current_direction = (current_direction + 1) % len(direction_options)
		else:
			print(f'Command "{command}" is unknown')

	return road


def print_road(road):
	min_x, min_y, max_x, max_y = 0, 0, 0, 0
	
	for pos in road:
		min_x = min(min_x, int(pos.real))
		min_y = min(min_y, int(pos.imag))
		max_x = max(max_x, int(pos.real))
		max_y = max(max_y, int(pos.imag))

	for y in range(max_y, min_y-1, -1):
		line = ''
		for x in range(min_x, max_x+1):
			line += '*' if complex(x, y) in road else ' '
		print(line)


def execute(code):
	road = get_road(code)
	print_road(road)


def main():
	codes = ['FFFFFLFFFFFLFFFFFLFFFFFL', 'LFFFFFRFFFRFFFRFFFFFFF']
	
	for code in codes:
		execute(code)


if __name__ == '__main__':
	main()
