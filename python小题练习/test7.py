def a(a1):
    a2 = list()
    a3 = list()
    dict1 = {0: 0, 1: 1}
    for i in a1:
        if i > 66:
            a2.append(i)
        elif i < 66:
            a3.append(i)
    dict1[0] = a2
    dict1[1] = a3
    print(dict1)


def main():
    a1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
    a(a1)


if __name__ == '__main__':
    main()
