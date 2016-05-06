# Level 1
# first exercise

some_text = "Once the basic structure of a function is finalized, you can execute it by calling it from another " \
            "function or directly from the Python prompt."


def concatenation(str):
    first_chars = str[:10]
    last_chars = str[-10:]

    print("Concatenated string: {} {}".format(first_chars, last_chars))


concatenation(some_text)
