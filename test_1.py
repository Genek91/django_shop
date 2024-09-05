"""
Напишите программу, которая выводит n первых элементов
последовательности 122333444455555…
(число повторяется столько раз, чему оно равно).
"""


def main(n):
    result = []
    i = 1
    while len(result) < n:
        result.extend([str(i)] * i)
        i += 1
    return ''.join(result[:n])


if __name__ == '__main__':
    n = int(input('Введите число: '))
    print(main(n))
