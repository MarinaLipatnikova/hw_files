from pprint import pprint

cook_book = {}

with open('recipes.txt', encoding="utf-8") as f:
    lines = f.readlines()
    i = 0
    while i < (len(lines)):
        dish = lines[i].strip()
        i += 1
        num_ingredients = int(lines[i].strip())
        i += 1
        ingredients = []
        for num in range(num_ingredients):
            ingredient = lines[i].strip().split(' | ')
            ingredient_name = ingredient[0]
            quantity = int(ingredient[1])
            measure = ingredient[2]
            ingredient_dict = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
            ingredients.append(ingredient_dict)
            i += 1
        cook_book[dish] = ingredients
        i += 1


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        ingredients = cook_book[dish]
        for ingredient in ingredients:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            if ingredient_name in shop_list:
                shop_list[ingredient_name] += quantity
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}

    pprint(shop_list)

pprint(cook_book)
print()
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
