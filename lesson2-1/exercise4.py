# Level 2
# fourth exercise

sentence = 'hi df fdgv dfv dfr cv  HI dfvdfxv  dfg gfd vsdjijc dfdfv Hi Alex'

count = sentence.lower().count('hi')
replace = sentence.replace('hi', 'bye')

print "Initial string: {}".format(sentence) + "\n"
print "Appearance of 'hi' in string: {}".format(count) + "\n"
print "Replaced 'hi' to 'bye' in string: {}".format(replace)