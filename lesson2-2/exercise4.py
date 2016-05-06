# Level 2
# fourth exercise

matrix = [[False, False, False],
          [False, False, True],
          [False, True, False],
          [False, True, True],
          [True, False, False],
          [True, False, True],
          [True, True, True]]


def result(variable):
    return (variable[0] or not variable[1]) and (variable[2] or not variable[0])

for variable in matrix:
    print result(variable)