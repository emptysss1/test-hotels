input_list = list(map(int, input().split()))


def common_div(args):
    my_dict = {}
    for el in args:
        for i in range(2, el+1):
            if el % i == 0:
                if i in my_dict:
                    my_dict[i] += 1
                else:
                    my_dict[i] = 1
    result_list = [k for k in my_dict if my_dict[k] == len(args)]

    return result_list


print(common_div(input_list))

