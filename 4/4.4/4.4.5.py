def is_correct_json(string):
    import json
    try:
        data = json.loads(string)
        return True
    except:
        return False
    
data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
print(is_correct_json(data))  

print(is_correct_json('number = 17'))
