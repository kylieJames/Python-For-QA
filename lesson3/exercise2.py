# Level 1
# second exercise

import re


def sentences_in_file(filename):
    with open(filename, 'r') as f:
        s = f.read()

        # variant 1
        # threeDotsOrOne = len(re.findall(r'\. |\.{3}', s))
        # end_with_dot = len([line for line in s.splitlines() if line.endswith('.')])
        # print("Total number of sentences: {}".format(threeDotsOrOne + end_with_dot))

        # variant 2
        endWithDot = len([item for item in s.split() if item.endswith('.')])
        print("Total number of sentences: {}".format(endWithDot))


sentences_in_file('alice_in_wonderland.txt')

