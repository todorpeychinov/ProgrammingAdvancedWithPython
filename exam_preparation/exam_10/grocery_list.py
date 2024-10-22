def shop_from_grocery_list(budget, grocery_list, *args):
    bought_products = []

    for product, price in args:
        if product in grocery_list:
            if product not in bought_products:
                if budget >= price:
                    bought_products.append(product)
                    budget -= price
                else:
                    break

    if all([product in bought_products for product in grocery_list]):
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        missing_products = [product for product in grocery_list if product not in bought_products]
        return f'You did not buy all the products. Missing products: {", ".join(missing_products)}.'


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
