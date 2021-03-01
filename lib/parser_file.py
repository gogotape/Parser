import re

"""
import numpy
import pandas
E:/code/Parser_project/input_data/test_schedule.inc
'W1' 10 10 1 3 OPEN 1* 1 2 1 3* 1.0 /
'W3' 'LGR1' 10 10  2   2 	OPEN 	1* 	1	2 	1 	3* 			1.0918 /
"""

input_f = input('Введите абсолютный путь к .inc файлу: ')

try:
    f = open(input_f, 'r', encoding="utf-8")
except:
    print('There is no such file in this directory')

a = open('file.txt', 'w', encoding="utf-8")


def transform_schedule(keywords, parameters, input_file, output_file):
    pass


def read_schedule():
    pass


def inspect_schedule():
    pass


def clean_schedule():
    for i in f.readlines():
        if re.findall(r'\w+|/', i):
            i = re.sub(r'--.*', '', i)
            if not re.findall(r'\w+|/', i):
                pass
            else:
                a.write(i)


def parse_schedule():
    pass


def extract_keyword_blocks():
    pass


def extract_lines_from_keyword_block():
    pass


def parse_keyword_block():
    pass


def parse_keyword_DATE_line():
    string = input('Введите строку для обработки (DATE): ')
    out = string.split(' ')
    print(*out[:-1])


def parse_keyword_COMPDAT_line():
    string = input('Введите строку для обработки (COMPDAT): ')
    out = string.split(' ')
    print(out[:-1])


def parse_keyword_COMPDATL_line():
    string = input('Введите строку для обработки (COMPDATL): ')
    out = string.split(' ')
    print(out[:-1])


def format_eclipse_string():
    s = input('Введите строку для форматирования значений DEFAULT: ')
    old_string = s
    def f(match):
        return str(int(match.group(3))+1)

    L = re.sub('([0-9])+', f, old_string)
    print(L)


def result_to_csv():
    pass




a = open('file.txt', encoding="utf-8")

'''
parse_keyword_DATE_line()
parse_keyword_COMPDAT_line()
parse_keyword_COMPDATL_line()
'''


format_eclipse_string()

a.close()
print('finish')
