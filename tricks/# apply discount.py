# apply discount

def apply_discount(product, discount):
    price = int(product['price'] * (1.0  - discount))
    assert 0 <= price <= product['price'], ['exprsn two show the error message ']
    return price

shoes = {'name': 'fancy', 'price':14900}
print(apply_discount(shoes, 0.5))

# assert syntax
#""" assert exp1, [exp2]
#"""