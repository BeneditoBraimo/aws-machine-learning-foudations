class SalesPerson:
    """The SalesPerson class represents a person that works in a store"""

    def __init__(self, first_name, last_name, employee_id, salary):
        """Method that initializes a SalesPerson object
        Args:
            first_name (str)
            last_name (str)
            employee_id (int)
            salary (float)
        Atributes:
            first_name (str): first name of the employee
            last_name (str): last name of the employee
            employee_id (int): indentification number of the employee
            salary (float): yearly salary of the employee
            pants_sold (list): a list of pants sold by the employee
            total_sales (float): sum of all sales made by the employee
        """
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants_object):
        """The sell_pants method appends a pants object to the pants_sold attribute
        Args:
            pants_object (obj): a pants object that was sold
        
        Returns: none
        """
        self.pants_sold.append(pants_object)

    def display_sales(self):
        """The display_sales method prints out all the pants that have been sold
        Args: None
        Returns: none
        """
        for pants in self.pants_sold:
            print('color: {}, waist_size: {}, length: {}, price: {}'.format(pants.color, pants.waist_size, pants.length, pants.price))

    def calculate_sales(self):
        """The calculate_sales methods sums the total price of all pants sold
        Args: None
        Returns:
            float: sum of all pants sold
        """
        total = 0
        for pants in self.pants_sold:
            total += pants.price
        self.total_sales = total
        return total
    
    def calculate_commission(self, persentage):
        """The calculate_commission method outputs the commission based on sales
        Args:
            percentage (float): the commission percentage as a decimal
        Returns:
            float: the comission due
        """
        sales_total = self.calculate_sales()
        return sales_total * persentage