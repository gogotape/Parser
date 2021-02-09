import re
import numpy
import pandas


input_f = input('Введите абсолютный путь к .inc файлу')


try:
    with open (input_f, 'r', encoding="utf-8") as f:
        print(f.read())
except:
    print('There is no such file in this directory')


def transform_schedule(keywords, parameters, input_file, output_file):
    pass


def read_schedule():
    pass


def inspect_schedule():
    pass


def clean_schedule():
    pass


def parse_schedule():
    pass


def extract_keyword_blocks():
    pass


def extract_lines_from_keyword_block():
    pass


def parse_keyword_block():
    pass


def parse_keyword_DATE_line():
    pass


def parse_keyword_COMPTDAT_line():
    pass


def parse_keyword_COMPTDATL_line():
    pass


def result_to_csv():
    pass