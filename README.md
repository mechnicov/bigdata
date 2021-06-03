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

## Задача 2

1. Нужно сгенерировать файл, содержащий 2000 48-битных случайных целых чисел, каждое число на отдельной строке. 

2. Посчитать, какое суммарное количество простых множителей присутствует при факторизации всех чисел.  Например, пусть всего два числа: 6 и 8. 
6 = 2 * 3, 8 = 2 * 2 * 2. Ответ 5.  

3. Реализовать подсчет 
    - простым последовательным алгоритмом
    - многопоточно, с использованием примитивов синхронизации
    - с помощью Akka (или аналога)
    - c помощью RxJava (или аналога)

4. Измерить время выполнения для каждого случая. Использовать уровень параллельности в соответствии с числом ядер вашего CPU. 

### Solution

To generate file with integers run

```console
$ make task2_generate
```

To calculate the number of prime factors count with all numbers factorization using

<details><summary><b>naive sequential method</b></summary>

```console
$ make task2_calculate method=naive
```
<details open><summary>Example</summary>

```console
$ make task2_calculate method=naive
cd task2 && ./gradlew calculate --args=naive

> Task :calculate
[Factorization Test] Start
Naive result: 8987
[Factorization Test] 146948ms

BUILD SUCCESSFUL in 2m 28s
2 actionable tasks: 2 executed
```

</details>
</details>

<details><summary><b>multithread method with synchronization primitives</b></summary>

```console
$ make task2_calculate method=multi
```
<details open><summary>Example</summary>

```console
$ make task2_calculate method=multi
cd task2 && ./gradlew calculate --args=multi

> Task :calculate
[Factorization Test] Start
Multithread result: 8987
[Factorization Test] 38965ms

BUILD SUCCESSFUL in 39s
2 actionable tasks: 2 executed
```

</details>
</details>

<details><summary><b>Akka method</b></summary>

```console
$ make task2_calculate method=akka
```
<details open><summary>Example</summary>

```console
$ make task2_calculate method=akka
cd task2 && ./gradlew calculate --args=akka

> Task :calculate
[Factorization Test] Start
Workers have started: akka://factorization/user/$a
Akka result: 8987
[Factorization Test] 36976ms

BUILD SUCCESSFUL in 39s
2 actionable tasks: 2 executed
```

</details>
</details>

<details><summary><b>RxJava method</b></summary>

```console
$ make task2_calculate method=rx
```
<details open><summary>Example</summary>

```console
$ make task2_calculate method=rx
cd task2 && ./gradlew calculate --args=rx

> Task :calculate
[Factorization Test] Start
Rx result: 8987
[Factorization Test] 44249ms

BUILD SUCCESSFUL in 44s
2 actionable tasks: 2 executed
```

</details>
</details>
