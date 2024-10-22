def cookbook(*args):
    cook_book = {}
    for recipe_name, cuisine, ingredients in args:
        if cuisine not in cook_book:
            cook_book[cuisine] = {}
        cook_book[cuisine][recipe_name] = ingredients

    sorted_cook_book = sorted(cook_book.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''

    for cuisine, recipes in sorted_cook_book:
        result += f"{cuisine} cuisine contains {len(recipes)} recipes:\n"
        for recipe_name, ingredients in sorted(recipes.items(), key=lambda x: [x[0]]):
            result += f' * {recipe_name} -> Ingredients: {", ".join(ingredient for ingredient in ingredients)}\n'

    return result.strip()


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
print()
print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))
print()
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
