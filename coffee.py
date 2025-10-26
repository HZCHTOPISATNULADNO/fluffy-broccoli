water = 300
milk = 200
coffe = 100

recipes = {
    'espresso': {'water': 50, 'milk': 0, 'coffee': 18},
    'latte': {'water': 20, 'milk': 150, 'coffee': 24},
    'cappuccino': {'water': 25, 'milk': 100, 'coffee': 24},
}

order = input('Добро пожаловать! Выберете кофе: ')

while True:
    if order in recipes:
        RECIPE = recipes[order]
        if (water >= RECIPE['water'] and milk >= RECIPE['milk'] and coffe >= RECIPE['coffee']):
            water -= RECIPE['coffee']
            milk -= RECIPE['milk']
            coffe -= RECIPE['coffee']
            print(f'Ваш {order} готов!)')
            order = input('Добро пожаловать! Выберете кофе: ')

        else:
            print('Извините, мы не можем приготовть этот заказ.(')
            order = input('Добро пожаловать! Выберете кофе: ')
    else:
        print(f'Такого напитка нет, введите заказ.')
        order = input('Добро пожаловать! Выберете кофе: ')