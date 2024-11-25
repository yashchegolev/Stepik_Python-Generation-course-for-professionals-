def is_good_password(string):
    if len(string) >= 9 and string != string.lower() and string != string.upper() and len(list(filter(lambda x: x in '0123456789', string))) > 0:
        return True
    else:
        return False
    
print(is_good_password('41157082'))
print()
print(is_good_password('мойпарольсамыйлучший'))
print()
print(is_good_password('МойПарольСамыйЛучший111'))
print()
print(is_good_password('!@#$%^&*()_+')) # False
print()
print(is_good_password('abc!@#%$#%#$%^&dABC8')) #True
print()
print(is_good_password('sjkdfsjkdfhjksdfhjkSDFSDAFSADFSADfsdajf')) # False
