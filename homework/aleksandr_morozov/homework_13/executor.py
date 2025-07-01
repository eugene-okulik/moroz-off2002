import os
import datetime


homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
# print(eugene_file_path)


def read_file():
    with open(eugene_file_path) as data_file:
        # print(data_file.read())
        for line in data_file.readlines():
            yield line


for data_line in read_file():
    line_index = int(data_line[0])
    date_date = datetime.datetime.strptime(data_line[3:29], '%Y-%m-%d %H:%M:%S.%f')
    # print(line_index)
    # print(date_date)

    if line_index == 1:
        print(date_date + datetime.timedelta(days=7))

    elif line_index == 2:
        print(date_date.strftime('%A'))

    elif line_index == 3:
        before_date = datetime.datetime.now() - date_date
        print(before_date.days)
