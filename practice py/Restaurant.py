class Restaurant:
    """My first class"""

    def __init__(self, name, cuisine_type):
        """Initialization of attributes"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value

    def describe_restaurant(self):
        print(f"{self.name} is our restaurant. We serve {self.cuisine_type} food, and the number of customers served is {self.number_served}.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

    def set_number_served(self, number):
        """Set the total number of customers served"""
        self.number_served = number

    def increment_number_served(self, number):
        """Add to the total number of customers served"""
        self.number_served += number


class IceCreamStand(Restaurant):
    
    def __init__(self, name, cuisine_type , flavors):
        super().__init__(name, cuisine_type)
        self.flavors=flavors

    def desplay(self):
        print("the flavors that we have are :")
        for flavor in self.flavors:
            print(flavor)

# Instance and usage
restaurant = Restaurant("Foodie's Place", "Italian")

# Print default value
restaurant.describe_restaurant()

# Change the value directly
restaurant.number_served = 15
restaurant.describe_restaurant()

# Set the number using method
restaurant.set_number_served(30)
restaurant.describe_restaurant()

# Increment the number
restaurant.increment_number_served(10)
restaurant.describe_restaurant()

# IceCreamStand class
iceCream = IceCreamStand("vencii gelato","italian",["choclate","vanilla","stawberry"])
iceCream.desplay()
