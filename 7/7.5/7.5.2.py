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
        raise LengthError(PasswordError)
        return False
    elif string == string.lower() or string == string.upper():
        raise LetterError(PasswordError)
        return False
    elif len(list(filter(lambda x: x in '0123456789', string))) == 0:
        raise DigitError(PasswordError)
        return False
    else:
        return True  
    
try:
    print(is_good_password('Short7'))
except Exception as err:
    print(type(err))
print()
print(is_good_password('еПQSНгиfУЙ70qE'))
print()
try:
    print(is_good_password('41157081231232'))
except Exception as err:
    print(type(err))
print()    
try:
    print(is_good_password('abc12345678ansdfjkasdkjfbsdk'))
except Exception as err:
    print(type(err))
