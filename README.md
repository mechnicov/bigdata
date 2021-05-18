## Задача 1

Нужно написать две программы: Первая генерирует бинарный файл (min 2Гб), состоящий из случайных 32-рязрядных беззнаковых целых чисел (big endian). Вторая считает сумму этих чисел (с применением длинной арифметики), находит минимальное и максимальное число.

Реализуйте две версии - 1. Простое последовательное чтение 2. Многопоточная + memory-mapped files. Сравните время работы.

### Solution

To generate binary file run

```console
$ python task1/generate.py
```

You can change filesize by changing `count` variable in this script.

To compare naive and multithread search run

```console
$ python task1/calculate.py
```

You can change threads quantity when call `multithread` method.

Example of use:

```console
$ python task1/calculate.py 
Naive search
Sum: 1152888151715470256
Max: 4294967282
Min: 2
169.36330672300028
Multithread search
Sum: 1152888151715470256
Max: 4294967282
Min: 2
49.91939028199977
```
