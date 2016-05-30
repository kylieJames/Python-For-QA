# -*- coding: utf-8 -*-
# Level 1
# third exercise

from lxml import etree

habr = etree.parse('habraharb_all.xml')

root = habr.getroot()

for item in root.iter('item'):
    title = item.find('title').text.strip()
    author = item.find('author').text.strip()

    category = item.findall('category')

    data = []
    for item in category:
        data.append(item.text)

    print "Author \"{}\" with article \"{}\" with categories - {}".format(author, title.encode('utf-8'), ', '.join(data).encode('utf-8'))


