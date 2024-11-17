first = input()
#вводим первое число
second = input()
#вводим второе число
third = input()
#вводим третье число
if first == second == third:
#если три числа одинаковые
    print(3)
#выводим 3
elif first == second or second == third or third == first:
#если хотябы два числа из трех одинаковые
    print(2)
#выводим 2
elif first != second and second != third and third != first:
#если числа неодинаковые
    print(0)
# выводим 0