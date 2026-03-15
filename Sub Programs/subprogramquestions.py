# def double_value(num):
#     return num * 2

# result = double_value(5)
# print(result)

def calculate_discount(price, discount_percentage):
    return price / 100 * (100 - discount_percentage)

print(calculate_discount(1000, 50))