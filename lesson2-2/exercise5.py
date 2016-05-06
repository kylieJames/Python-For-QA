# Level 2
# fifth exercise

sample_array = ([1, 2, 2, 1, 13, 5, 4, 2, 'a', 'b', False])
empty_array = ([])


def sum13(myarray):
    summa = 0
    if not myarray:
        print("An array is empty")
        return 0
    else:
        for item in myarray:
            if item == 13:
                break
            else:
                if isinstance(item, (int, long, float, complex)):
                    summa += item
        print(summa)

sum13(sample_array)
sum13(empty_array)