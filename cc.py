def is_all_digits(cc_num):
    
    for char in cc_num:
        if char not in '0123456789':
            return False
    return True

def is_16_digits(cc_num):
    return len(cc_num) == 16

def clean_number(cc_num):
    for char in cc_num:
        cleaned_cc = '' 
        if char != '-':
            cleaned_cc = cleaned_cc + char

def is_valid_cc(cc_num):
    cleaned_cc = '' 
    for char in cc_num:
        if char != '-':
            cleaned_cc = cleaned_cc + char
    return is_all_digits(cleaned_cc) and is_16_digits(cleaned_cc)

        
  
