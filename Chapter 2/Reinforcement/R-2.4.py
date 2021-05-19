class Flower:
    """A class that represents a real-life flower."""
    def __init__(self, name = "Hibiscus", number_of_petals = 5, price = 150.00):
        """Initialize a flower object.
        name                   Name of the species of flower
        number_of_petals       number of petals on the flower
        price                  price of the flower
        """
        self._name = name
        self._petalcount = number_of_petals
        self._price = price

    def change_name(self, name):
        """Changes the name of the flower."""
        self._name = name

    def change_petalnumber(self, number):
        """Changes the number of petals."""
        self._petalcount = number

    def change_price(self, price):
        """Changes the price of the flower."""
        self._price = price

    def get_name(self):
        """Returns the name of the flower."""
        return self._name

    def get_petalnumber(self):
        """Returns the number of petals."""
        return self._petalcount

    def get_price(self):
        """Gets the price of the flower."""
        return self._price

    def __str__(self):
        """Returns all the flowers properties as a string."""
        return self._name + ", number of petals: " + str(self._petalcount)+", price: " + str(self._price)


if __name__ == '__main__':
    hibiscus = Flower("Hibscus", 5, 14.00)

    hibiscus.change_name("Dandelion")
    hibiscus.change_price(10.00)
    hibiscus.change_petalnumber(20) # Modify the flower's properties.
    
    print(hibiscus)  # Return the string representation of the flower.

    hibiscusname = hibiscus.get_name()
    print(hibiscusname)

    hibiscuspetalnum = hibiscus.get_petalnumber() # Access the flower's petal count.
    print(hibiscuspetalnum)
    
    hibiscusprice = hibiscus.get_price() # Access the flower's price.
    print(hibiscusprice)

   
   
    

    
