class Product:  # Класс продукта, содержит информацию о его категории, цене и наличии на складе
    def __init__(self, category, price, available):
        self.category = category
        self.price = price
        self.available = available

class Order:  # Класс для оформления заказа, содержит информацию о корзине, скидке и налоге
    def __init__(self, cart, discount=0, tax=0):
        self.cart = cart
        self.discount = discount
        self.tax = tax

    def final_price(self):  # Рассчитывает итоговую цену с учетом скидки и налога, округляет до 3 знаков после запятой
        prices = [i.price for i in self.cart.current_cart]
        return round(sum(prices) * (1 - self.discount / 100) * (1 + self.tax / 100), 3)

class Customer:  # Класс покупателя, содержит его текущую корзину
    def __init__(self):
        self.order_history = []
        self.current_cart = ShoppingCart()

    def cart(self):  # Печатает текущее содержимое корзины
        print(self.current_cart.cart())

    def add_product(self, product):  # Добавляет продукт в корзину, если он есть на складе
        if product.available:
            self.current_cart.add_product(product)
        else:
            print("Товара нет на складе.")

    def remove_product(self, product):  # Убирает продукт из корзины, если он там был
        if product in self.current_cart.current_cart:
            self.current_cart.remove_product(product)

    def make_order(self, discount, tax):  # Оформление заказа: добавляет его в историю и печатает итоговую цену
        result = Order(self.current_cart, discount, tax).final_price()
        self.order_history.append((self.current_cart.cart(), result))
        self.current_cart = ShoppingCart()  # Опустошение корзины
        print(f"Итого: {result}")

    def history(self):  # Печатает историю заказов
        print(self.order_history)

class ShoppingCart:  # Вспомогательный класс, отдельно от Customer не используется, так как привязывается к нему
    def __init__(self):
        self.current_cart = []

    def cart(self):  # Возвращает список категорий продуктов в корзине
        return [i.category for i in self.current_cart]

    def add_product(self, product):  # Добавляет продукт в корзину
        self.current_cart.append(product)

    def remove_product(self, product):  # Убирает продукт из корзины
        self.current_cart.remove(product)

John = Customer()
apple = Product('Яблоко', 10, True)  # Создание продуктов
banana = Product("Банан", 17, False)
John.cart()  # Пустая корзина

John.add_product(apple)  # Добавляем продукты в корзину
John.add_product(banana)  # Бананов нет на складе, поэтому выводится соответствующее сообщение
John.cart()  # Заполненная корзина

John.make_order(13, 20)
John.history()
John.cart()  # Вновь пустая корзина