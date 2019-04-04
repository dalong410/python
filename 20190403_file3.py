#파일에 데이터 읽고 쓰기 file2.py

from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys
import glob
import os


print('-----------여러파일 읽기---------------')

inputPath = sys.argv[1]

for input_file in glob.glob(os.path.join(inputPath, '*.txt')) :
    with open(input_file, 'r', newline='' ) as filereader :
        for row in filereader :
            print("{}".format(row.strip()))

#여러개 txt 파일 실행 방법 (디렉토리 명시)
#20190403_file3.py "d:\python" 
