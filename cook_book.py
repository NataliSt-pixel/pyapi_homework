def read_cook_book(filename):
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as file:
        while True:

            dish_name = file.readline().strip()
            if not dish_name:
                break 
            
           
            ingredient_count = int(file.readline().strip())
            
           
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip()
                name, quantity, measure = [part.strip() for part in ingredient_line.split('|')]
                ingredients.append({
                    'ingredient_name': name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            
            cook_book[dish_name] = ingredients
            
           
            file.readline()
    
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    
    shop_list = {}
    
    for dish in dishes:
        if dish not in cook_book:
            continue  
        
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count
            
           
            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {'measure': measure, 'quantity': quantity}
    
    return shop_list


def main():
    cook_book = read_cook_book('recipes.txt')
    
    # Задача №1
    print("Cook Book:")
    for dish, ingredients in cook_book.items():
        print(f"\n{dish}:")
        for ing in ingredients:
            print(f"  - {ing['ingredient_name']}: {ing['quantity']} {ing['measure']}")
    
    # Задача №2
    shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
    
    print("\n Shopping List:")
    for item, details in shop_list.items():
        print(f"  - {item}: {details['quantity']} {details['measure']}")


if __name__ == '__main__':
    main()