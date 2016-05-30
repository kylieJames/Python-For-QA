# coding=utf-8
# Level 1
# first exercise


import requests
import lxml.html as html

ENDPOINT = 'http://deshevshe.net.ua/iron-bosch/bosch_tds373118p'
ENDPOINT_PR_NOT_AVAILABLE = 'http://deshevshe.net.ua/iron-maestro/maestro_mr_316'


def product_price(url):
    item_name = '//h1[@itemprop="name"]/text()'
    price_value = '//span[@itemprop="price"]/text()'
    currency = '//span[@itemprop="priceCurrency"]/text()'
    availability = '//div[@class="wareAvail"]/text()'

    page = requests.get(url)
    root = html.fromstring(page.content)

    available = root.xpath(availability)

    if available[0].encode('utf-8') == 'Есть в наличии':

        title = root.xpath(item_name)
        price = root.xpath(price_value)
        currency = root.xpath(currency)

        print ("Product '{productname}' with price - {price}{currency}".format(productname=title[0].encode('utf-8'),
                                                                                price=price[0],
                                                                                currency=currency[0].encode('utf-8')))

    else:
        title = root.xpath(item_name)
        price = root.xpath(price_value)

        if len(price[0]) > 1:
            currency = root.xpath(currency)

            print ("Product '{productname}' isn't available, but with price - {price}{currency}".format(productname=title[0].encode('utf-8'),
                                                                                price=price[0],
                                                                                currency=currency[0].encode('utf-8')))
        else:
            print ("Product '{productname}' doesn't have price".format(productname=title[0].encode('utf-8')))


product_price(ENDPOINT)
product_price(ENDPOINT_PR_NOT_AVAILABLE)
