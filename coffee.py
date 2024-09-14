class Coffee:
    def __init__(self, name):
        # Initializes the Coffee with a name and an empty list of orders
        self.name = name  
        self._orders = [] 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Setter for the name attribute with validation
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Name must be a string with at least 3 characters.")

    def orders(self):
        # Returns the list of orders associated with this coffee
        return self._orders

    def customers(self):
        # Returns a list of unique customers who have ordered this coffee
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        # Calculates and returns the average price of the orders for this coffee
        if not self._orders:  
            return 0
        total_price = sum(order.price for order in self._orders)  
        return total_price / len(self._orders)  