class Store:
    def __init__(self, name, address):
        """Инициализирует магазин с названием, адресом и пустым ассортиментом."""
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент или обновляет его цену."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента, если он есть."""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Возвращает цену товара или None, если товар отсутствует."""
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара, если он есть в ассортименте."""
        if item_name in self.items:
            self.items[item_name] = new_price


# Создание магазинов
store1 = Store("Fresh Market", "123 Main St")
store2 = Store("Green Grocery", "456 Elm St")
store3 = Store("SuperMart", "789 Oak St")

# Добавление товаров в магазины
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)
store2.add_item("oranges", 0.6)
store2.add_item("milk", 1.2)
store3.add_item("bread", 1.5)
store3.add_item("eggs", 2.0)

# Тестирование методов на первом магазине
print("Цена яблок:", store1.get_price("apples"))
store1.update_price("apples", 0.55)
print("Обновленная цена яблок:", store1.get_price("apples"))
store1.remove_item("bananas")
print("Цена бананов после удаления:", store1.get_price("bananas"))
print("Цена молока:", store2.get_price("milk"))
store2.update_price("milk", 1.5)
print("Цена молока:", store2.get_price("milk"))