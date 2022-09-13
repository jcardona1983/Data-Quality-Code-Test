import os
import re
import numpy as np

# installed libraries
import validators
import phonenumbers


def is_zero_file(filepath):
    """Checks if a file is empty, return True if the file is empty, False otherwise
       
       Input Arguments: filePath - path of a file
    """
    return not(os.path.isfile(filepath) and os.path.getsize(filepath) > 0)


def validate_url(url_path):
    """Validates url, return True if it's valid, False otherwise
       
       Input Arguments: url_path - url column
    """
    if validators.url(url_path):
        return True
    else:
        return False
    
       
def strip_character(dataCol, reg):
    r = re.compile(reg)
    return r.sub('', dataCol)


def search_character(dataCol, reg):
    r = re.compile(reg)
    return r.search(dataCol)


def empty_string(string_col):
     if string_col == '' or string_col == None:
        return True
     else:
        return False


def validate_phone(phone_num):
    """Validates a phone number, return True if it's valid, False otherwise
       
       Input Arguments: phone_num - phone column
    """
    if empty_string(phone_num):
        return True
    
    # Validates phones from India
    try:
        my_number = phonenumbers.parse(phone_num,'IN')
        return phonenumbers.is_valid_number(my_number)
    except Exception as e:
        return False
        

def unique_list(list1):
    x = np.array(list1)
    return np.unique(x)
  