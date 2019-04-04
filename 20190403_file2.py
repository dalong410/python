#파일에 데이터 읽고 쓰기 file2.py

from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys

#입력
input_file = sys.argv[1]
#filereader = open(input_file, 'r')
with open(input_file, 'r', newline='' ) as filereader :
    for row in filereader :
        print("{}".format(row.strip()))
