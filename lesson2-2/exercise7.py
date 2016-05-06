# Level 3
# seventh exercise


# 1

def simple_way_is_palindrome(inputstr):
    rev = ''.join(reversed(inputstr))
    if rev == inputstr:
        print "1. Palindrome: True"
    else:
        print "1. Palindrome: False"


# 2, the same as first

def simple_way2_is_palindrome(input):
    if input == input[::-1]:
        print "2. Palindrome: True"
    else:
        print "2. Palindrome: False"


# 3

def is_palindrome(inpstr):
    count = len(inpstr)
    palindrome = False
    item = 0
    while item < count / 2 + 1:
        if inpstr[item] == inpstr[count - item - 1]:
            palindrome = True
            break
        item += 1
    print "3. Palindrome: {}".format(palindrome)
    return palindrome

simple_way_is_palindrome("anna")
simple_way2_is_palindrome("racecar")
is_palindrome("civic")
