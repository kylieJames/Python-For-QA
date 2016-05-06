# Level 2
# sixth exercise


def key_value(n):
    value = []
    sum = []
    for item in range(1, n):
        if item % 2 == 0:
            value.append(item)
            sum.append(item ** 2)
    print(dict(zip(value, sum)))


key_value(100)
