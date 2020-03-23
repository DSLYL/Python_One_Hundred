if __name__ == '__main__':
    b = list()
    for i in range(2, 101):
        if i % 2 != 0:
            i = -i
        b.append(i)
    print(sum(b))
