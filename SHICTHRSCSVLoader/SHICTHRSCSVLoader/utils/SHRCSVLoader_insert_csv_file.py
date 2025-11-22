
import os
import csv
from tempfile import NamedTemporaryFile

def insert_header_to_csv(file_path : str , header_row : list , insert_encoding):
    with NamedTemporaryFile(mode = 'w', delete = False, newline = '' , encoding = insert_encoding) as temp_file:
        temp_path = temp_file.name
        writer = csv.writer(temp_file)
        writer.writerow(header_row)
        with open(file_path , 'r' , newline = '', encoding = insert_encoding) as orig_file:
            reader = csv.reader(orig_file)
            for row in reader:
                writer.writerow(row)
        os.replace(temp_path , file_path)