# customer.py

class Customer:
    def __init__(self, name):
        self.name = name  
        self._orders = []  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters long.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        from .order import Order  
        new_order = Order(self, coffee, price)  
        self._orders.append(new_order)  
        return new_order  

    @classmethod
    def most_aficionado(cls, coffee):
        customers_spending = {}
        for order in coffee.orders():
            if order.customer in customers_spending:
                customers_spending[order.customer] += order.price
            else:
                customers_spending[order.customer] = order.price

        if customers_spending:
            return max(customers_spending, key=customers_spending.get)
        return None
