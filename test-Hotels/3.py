num1, num2 = map(int, input().split())


def get_simple_list(a: int, b: int) -> list:
    simple_list = []
    for i in range(a, b+1):
        count = 0
        for k in range(1, i+1):
            if i % k == 0:
                count += 1
        if count == 2:
            simple_list.append(i)
    return simple_list


print(get_simple_list(num1, num2))
