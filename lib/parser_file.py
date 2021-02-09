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


