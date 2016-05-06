# Level 1
# third exercise

original_numbers = [1, 2, 3, 4, 4, 6, 2]
print ("Original string: {}\n".format(original_numbers))


def counter(elements):
    formatted_numbers = []
    for item in elements:
        if elements.count(item) == 1:
            formatted_numbers.append(item)
    print ("Formatted string: {}".format(formatted_numbers))


counter(original_numbers)
