# Level 3
# sixth exercise

import csv
import os
import re
import shutil

from datetime import datetime
from tempfile import NamedTemporaryFile

NGINX_LINE_REGEXP = re.compile(
    ('(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
     ' - - '
     '\[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] '
     '((\"(?P<method>GET|POST|CONNECT|HEAD) )'
     '(?P<url>.+)(http\/1\.(1|0)")) '
     '(?P<statuscode>\d{3}) '
     '(?P<bytessent>\d+) '
     '(["](?P<refferer>(\-)|(.+))["]) '
     '(["](?P<useragent>.+)["])'), re.IGNORECASE)

DATE_TIME_FORMAT = '%d/%b/%Y:%H:%M:%S'
DATE_FORMAT = '%d/%m/%y'
TIME_FORMAT = '%H:%M:%S'
FIELDS = ['ip', 'date', 'time', 'method', 'url', 'status_code']


def distinct_requests(file, delimiter):
    file.seek(0)
    reader = csv.DictReader(file)
    unique = []
    for row in reader:
        if row[delimiter] not in unique:
            unique.append(row[delimiter])
    print ("Distinct request status codes: {}".format(unique))


def requests_without_perm(file, search_field):
    file.seek(0)
    reader = csv.DictReader(file)
    for row in reader:
        if row[search_field] == '403':
            print (row)


def created_resources(file, search_field):
    file.seek(0)
    reader = csv.DictReader(file)
    for row in reader:
        if row[search_field] == '201':
            print (row)


def requests_count(file, search_field, start_time, end_time):
    file.seek(0)
    reader = csv.DictReader(file)
    m = 0
    for row in reader:
        if start_time <= row[search_field] <= end_time:
            m += 1
    print("Requests count in {starttime} - {endtime}: {result}".format(starttime=start_time,
                                                                       endtime=end_time, result=m))


def requests_rate(file, search_field):
    file.seek(0)
    reader = csv.DictReader(file)
    i = j = 0
    f = lambda i, j: (j / i) * 100
    for row in reader:
        if row[search_field] > 0:
            i += 1
            match = re.findall(r"2..", row[search_field])
            if match:
                j += 1
    print ("Successful requests rate: {}".format(f(float(i), j)))


def main():

    storage = NamedTemporaryFile()
    writer = csv.DictWriter(storage, FIELDS)

    with open('logs.txt') as f:
        for line in f.readlines():
            match = re.match(NGINX_LINE_REGEXP, line)
            if not match:
                continue
            log_datetime = match.group('dateandtime').split(' ')[0]
            log_datetime = datetime.strptime(log_datetime, DATE_TIME_FORMAT)
            parsed_item = {'ip': match.group('ipaddress'),
                           'date': log_datetime.strftime(DATE_FORMAT),
                           'time': log_datetime.strftime(TIME_FORMAT),
                           'method': match.group('method'),
                           'url': match.group('url'),
                           'status_code': match.group('statuscode')}
            writer.writerow(parsed_item)

    shutil.copy(storage.name, os.path.join(os.getcwd(), 'logs.csv'))
    storage.close()

    with open('logs.csv', 'r+') as csvfile:
        header = ['ip', 'date', 'time', 'method', 'url', 'status_code']

        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()

        distinct_requests(csvfile, 'status_code')
        requests_without_perm(csvfile, 'status_code')
        created_resources(csvfile, 'status_code')
        requests_count(csvfile, 'time', '15:11:00', '15:26:00')
        requests_rate(csvfile, 'status_code')


if __name__ == '__main__':
    main()


