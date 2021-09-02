class Pants:
    """The Pants class represents an article of clothing sold in a store"""
    def __init__(self, color, waist_size, length, price):
        """Method for initializing a Pants object
        
        Args:
            color (str)
            waist_size (int)
            length (int)
            price (float)
            
        Attributes:
            color (str): color of a pants object
            waist_size (int): waist size of a pants object
            length (int): length of a pant
            price (float): price of a pants object
        """

        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

    def change_price(self, new_price):
        """
        Method that changes the price of pant
        Args:
            new_price (float): the new price of the pant
        Returns:
            None
        """
        self.price = new_price
    
    def discount(self, discount):
        """Method that computes the discount
        Args:
            discount (float): a decimal value for the discount.
            For example 0.05 for a 5% discount
        
        Returns:
        float: the discounted price"""

        return self.price * (1 - discount)