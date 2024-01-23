#!/usr/bin/env python3

''' Description: Regex-ing - Write a function called filter_datum that returns
                 the log message obfuscated:
    Arguments:
                fields: a list of strings representing all fields to obfuscate
                redaction: a string representing by what the field will be
                           obfuscated
                message: a string representing the log line
                separator: a string representing by which character is
                           separating all fields in the log line (message)
   The function should use a regex to replace occurrences of certain field
   values.
   filter_datum should be less than 5 lines long and use re.sub to perform
   the substitution with a single regex.
'''
''' 0. Regex-ing '''

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
        return re.sub(fr'(?:(?<=\{separator})|^)({"|".join(fields)})=\S+?(?=\{separator}|$)', f'{redaction}', message)
