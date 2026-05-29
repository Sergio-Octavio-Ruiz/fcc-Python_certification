def data_validation(price, discount):
    error_messages = []

    if not isinstance(price, (int, float)):
        error_messages.append('The price should be a number')
    elif price <= 0:
        error_messages.append('The price should be greater than 0')

    if not isinstance(discount, (int, float)):
        error_messages.append('The discount should be a number')
    elif not (0 <= discount <= 100):
        error_messages.append('The discount should be between 0 and 100')

    if error_messages:
        return error_messages

def apply_discount(price, discount):

    error_messages = data_validation(price, discount)
    if error_messages:
        return error_messages
    
    final_price = price * (1 - discount / 100)
    return final_price

price = 100
discount = 20
apply_discount(price, discount)