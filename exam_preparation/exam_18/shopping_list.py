def shopping_list(budget, **kwargs):
    products_bought = {}
    if budget < 100:
        return "You do not have enough budget."

    for product_name, product in kwargs.items():
        product_price, product_quantity = product
        total_sum = product_price * product_quantity
        if total_sum <= budget:
            products_bought[product_name] = total_sum
            budget -= total_sum
            if len(products_bought) == 5:
                break

    result = ''

    for product_name, product_price in products_bought.items():
        result += f"You bought {product_name} for {product_price:.2f} leva.\n"

    return result.strip()


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
