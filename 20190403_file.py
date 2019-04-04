#파일에 데이터 읽고 쓰기

from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys

#입력
input_file = sys.argv[1]
filereader = open(input_file, 'r')
for row in filereader :
    print(row.strip())
filereader.close()