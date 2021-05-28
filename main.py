from lib import parser_file


if __name__ == "__main__":
    keywords = ("DATES", "COMPDAT", "COMPDATL", "END")
    parameters = ""
    input_file = 'input data/test_schedule.inc'
    output_file = 'output data/schedule.csv'


data = parser_file.read_schedule(input_file)
print(parser_file.parse_schedule(data, keywords))

i=1
