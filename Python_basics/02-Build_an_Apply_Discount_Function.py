def apply_discount(price, discount):
    if (type(price) == int or type(price) == float) and (type(discount) == int or type(discount) == float):
        if price <= 0 and (discount > 0 or discount <= 100):
            return 'The price should be greater than 0'
        elif price > 0 and (discount < 0 or discount > 100):
            return 'The discount should be between 0 and 100'
        elif price <= 0 and (discount < 0 or discount > 100):
            return 'The price should be greater than 0', 'The discount should be between 0 and 100'
        else:
            final_price = price - (price * discount / 100)
            print(final_price)
            return final_price
    if (type(price) == int or type(price) == float) and (type(discount) != int or type(discount) != float):
        return 'The discount should be a number'
    if (type(price) != int or type(price) != float) and (type(discount) == int or type(discount) == float):
        return 'The price should be a number'
    else:
        return 'The discount should be a number', 'The price should be a number'


price = 100
discount = 20
apply_discount(price, discount)