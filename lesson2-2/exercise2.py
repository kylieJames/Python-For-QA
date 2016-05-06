# Level 1
# second exercise

comma_string = "Once, the, basic structure, of a function, is finalized, you, can, execute it by, calling it, " \
               "from another, function, or directly, from the Python, prompt."
no_comma_string = "Once the basic structure of a function is finalized you can execute it by calling it from another " \
                  "function or directly from the Python prompt."


def separator(str):
    if ',' in str:
        last_element = str.split(',').__getitem__(-1)
        print("Last element after comma: {}".format(last_element))
        return last_element
    else:
        print("String doesn't contain comma: {}".format(str))
        return str

separator(comma_string)
separator(no_comma_string)
