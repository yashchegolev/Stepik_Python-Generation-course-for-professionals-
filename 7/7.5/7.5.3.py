class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string):
    if len(string) < 9:
        raise LengthError('LengthError')
    elif string == string.lower() or string == string.upper():
        raise LetterError('LetterError')
    elif len(list(filter(lambda x: x in '0123456789', string))) == 0:
        raise DigitError('DigitError')
    else:
        return 'Success!'


import sys
passwords = [line.strip() for line in sys.stdin]

for passw in passwords:
    try:
        print(is_good_password(passw))
        break
    except Exception as err:
        print(err)
        
arr1
Arrrrrrrrrrr
arrrrrrrrrrrrrrr1
Arrrrrrr1

beegeek
Beegeek123
Beegeek2022
Beegeek2023
Beegeek2024
