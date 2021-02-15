from lib import parser_file


if __name__ == '__main__':
    keywords = ('DATES', 'COMPDAT', 'COMPDATL')
    input_file = ''
    output_csv = ''
    parameters = ()
    schedule_df = parser_file.transform_schedule()

