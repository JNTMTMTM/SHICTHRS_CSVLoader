# *-* coding: utf-8 *-*
# src\__init__.py
# SHICTHRS CSV LOADER
# AUTHOR : SHICTHRS-JNTMTMTM
# Copyright : © 2025-2026 SHICTHRS, Std. All rights reserved.
# lICENSE : GPL-3.0

import os
from colorama import init
init()
from .utils.SHRCSVLoader_read_csv_file import read_csv_file

print('\033[1mWelcome to use SHRCSVLoader - CSV file io System\033[0m\n|  \033[1;34mGithub : https://github.com/JNTMTMTM/SHICTHRS_CSVLoader\033[0m')
print('|  \033[1mAlgorithms = rule ; Questioning = approval\033[0m')
print('|  \033[1mCopyright : © 2025-2026 SHICTHRS, Std. All rights reserved.\033[0m\n')

class SHRCSVLoaderException(BaseException):
    def __init__(self , message: str) -> None:
        self.message = message
    
    def __str__(self):
        return self.message

def SHRCSVLoader_read_csv_file(path : str , read_encoding : str = 'GB2312') -> dict:
    try:
        if os.path.exists(path):
            if os.path.isfile(path) and (path.endswith('.csv') or path.endswith('.CSV')):
                return read_csv_file(path , read_encoding)
            else:
                raise SHRCSVLoaderException(f"SHRJsonLoader [ERROR.1017] only csv file is supported not .{path.split('.')[-1]}.")
        else:
            raise SHRCSVLoaderException(f"SHRJsonLoader [ERROR.1018] unable to find csv file. File Path : {path} NOT FOUND")
    except Exception as e:
        raise SHRCSVLoaderException(f"SHRJsonLoader [ERROR.1019] unable to read csv file. File Path : {path} | {e}")