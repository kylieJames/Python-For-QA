# Level 1
# first exercise

# list comprehension


def divisible_numbers(n):
    div = [item for item in range(1, n) if item %2 == 0 and item %3 == 0]
    print(div)

divisible_numbers(10000)

# filter function


def divisible_numbers_filt(n):
    division = filter(lambda number: number %2 == 0 and number %3 == 0, range(1, n))
    print(division)

divisible_numbers_filt(10000)