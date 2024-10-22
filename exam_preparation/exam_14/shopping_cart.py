def shopping_cart(*args):


    def is_products_in_the_carts():
        for cart in meals.values():
            if cart:
                return True
        return False


    meals = {
    "Soup": [],
    "Pizza": [],
    "Dessert": []
    }

    limits = {
        "Soup":  3,
        "Pizza":  4,
        "Dessert": 2
    }

    for arg in args:
        if arg == 'Stop':
            break

        meal_type, product   = arg

        if product in meals[meal_type]:
            continue

        elif len(meals[meal_type]) < limits[meal_type]:
            meals[meal_type].append(product)

    sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''

    if not is_products_in_the_carts():
        return "No products in the cart!"

    for meal, products in sorted_meals:
        result += f"{meal}:\n"
        if products:
            for product in sorted(products):
                result += f" - {product}\n"

    return result.strip()


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print()
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print()
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
