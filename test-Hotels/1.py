string = int(input())


def add_comp(a: int) -> str:
    if a in range(11, 20):
        return f'{a} компьютеров'
    elif a % 10 == 1:
        return f'{a} компьютер'
    elif a % 10 == 2 or a % 10 == 3 or a % 10 == 4:
        return f'{a} компьютера'
    else:
        return f'{a} компьютеров'


print(add_comp(string))
