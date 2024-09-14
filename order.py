class Order:
    def __init__(self, customer, coffee, price):
        # Initializes the Order with a customer, coffee, and price
        self.customer = customer  # Sets the customer for this order
        self.coffee = coffee  # Sets the coffee for this order
        self.price = price  # Sets the price for this order

        # Adds this order to the customer's and coffee's list of orders
        customer.orders().append(self)  
        coffee.orders().append(self)  

    @property
    def customer(self):
        # Getter for the customer attribute
        return self._customer

    @customer.setter
    def customer(self, value):
        # Setter for the customer attribute with validation
        # Ensures that the customer is an instance of the Customer class
        from .customer import Customer  
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise ValueError("Customer must be an instance of Customer.")

    @property
    def coffee(self):
        # Getter for the coffee attribute
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        # Setter for the coffee attribute with validation
        # Ensures that the coffee is an instance of the Coffee class
        from .coffee import Coffee  
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise ValueError("Coffee must be an instance of Coffee.")

    @property
    def price(self):
        # Getter for the price attribute
        return self._price

    @price.setter
    def price(self, value):
        # Setter for the price attribute with validation
        # Ensures that the price is a float between 1.0 and 10.0
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")