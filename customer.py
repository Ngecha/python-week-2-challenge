# customer.py

class Customer:
    def __init__(self, name):
        # Initializes the Customer with a name and an empty list of orders
        self.name = name  
        self._orders = []  

    @property
    def name(self):
        # Getter for the name attribute
        return self._name

    @name.setter
    def name(self, value):
        # Setter for the name attribute with validation and ensures that the name is a string with length between 1 and 15 characters
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters long.")

    def orders(self):
        # Returns the list of orders associated with this customer
        return self._orders

    def coffees(self):
        # Returns a list of unique Coffee objects that this customer has ordered
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        # Creates a new Order for the customer
        # This method imports the Order class and creates a new Order instance
        from .order import Order  
        new_order = Order(self, coffee, price)  
        self._orders.append(new_order)  
        return new_order  

    @classmethod
    def most_aficionado(cls, coffee):
        # Class method to find the customer who has spent the most on a particular coffee
        total = {}  
        for order in coffee.orders():
            if order.customer in total:
                total[order.customer] += order.price
            else:
                total[order.customer] = order.price
        if total:
            return max(total, key=total.get)
        return None
