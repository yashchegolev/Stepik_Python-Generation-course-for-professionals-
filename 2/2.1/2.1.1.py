card = input()

def hide_card(card_number):
    card_number = '*' * 12 + ''.join(filter(lambda num: num in '0123456789', card_number))[12:]
    return card_number 
    
print(hide_card(card))
