def get_shop_list_by_dishes(dishes, person_count):
    cook_book = {
        'Омлет': [
            {'ingredient_name': 'Яйцо', 'measure': 'шт', 'quantity': 2},
            {'ingredient_name': 'Молоко', 'measure': 'мл', 'quantity': 100},
            {'ingredient_name': 'Помидор', 'measure': 'шт', 'quantity': 2},
        ],
        'Утка по-пекински': [
            {'ingredient_name': 'Утка', 'measure': 'шт', 'quantity': 1},
            {'ingredient_name': 'Вода', 'measure': 'л', 'quantity': 2},
            {'ingredient_name': 'Мед', 'measure': 'ст.л', 'quantity': 3},
            {'ingredient_name': 'Соевый соус', 'measure': 'мл', 'quantity': 60},
        ],
        'Запеченный картофель': [
            {'ingredient_name': 'Картофель', 'measure': 'кг', 'quantity': 1},
            {'ingredient_name': 'Чеснок', 'measure': 'зубч', 'quantity': 3},
            {'ingredient_name': 'Сыр гауда', 'measure': 'г', 'quantity': 100},
        ],
        'Фахитос': [
            {'ingredient_name': 'Говядина', 'measure': 'г', 'quantity': 500},
            {'ingredient_name': 'Перец сладкий', 'measure': 'шт', 'quantity': 1},
            {'ingredient_name': 'Лаваш', 'measure': 'шт', 'quantity': 2},
            {'ingredient_name': 'Винный уксус', 'measure': 'ст.л', 'quantity': 1},
            {'ingredient_name': 'Помидор', 'measure': 'шт', 'quantity': 2},
        ],
    }

    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}

    return shop_list