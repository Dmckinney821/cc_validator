from cc import *

cc1 = '0000000000000000'
assert is_valid_cc(cc1), '000000000000000 is valid' 

cc2 = '1234'
assert not is_valid_cc(cc2), 'credit card numbers should be 16 characters long' 

cc3 = 'aaaaaaaaaaaaaaaaa'
assert not is_valid_cc(cc3), 'credit card numbers should only contain numbers' 

cc4 = '0000-0000-0000-0000'
assert is_valid_cc(cc4), 'credit card numbers can contain dashes'

cc5 = '0000 0000 0000 0000'
assert is_valid_cc(cc4), 'credit card numbers can contain spaces'