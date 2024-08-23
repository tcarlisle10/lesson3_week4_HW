# Question 1 

class BudgetCategory:
    
    def __init__(self, total, food, entertainment, utilities, savings):
        self.__total = total
        self.food = food
        self.entertainment = entertainment
        self.utilities = utilities
        self.__savings = savings

    def total(self,):
        total = float(input("How much are you spending this month? "))
        return total

    def get_total(self):
        return self.__total

    def set_total(self, total):
        self.__total = total

    def all_utilities(self, total):
        utilities = float(input("How much are you spending this month on entertainment? "))
        total - utilities
        amount = total - utilities
        return amount

    def fun_stuff(self, total):
        fun = float(input("How much are you spending this month on entertainment? "))
        total - fun
        amount = total - fun
        return amount

    def savings(self):
        savings = float(input("How much are you wanting to save this month? "))
        return savings

    def get_savings(self):
        return self.__savings

    def foods(self, total):
        food = float(input("How much are you wanting to save this month? "))
        total - food
        amount = total - food
        return amount
    

    def set_savings(self, savings):
        self.__savings = savings



    def add_expense(self, amount):
        add = input("What expense are you adding? ")
        amount = add
        return amount

#-----------------------------------------------#

# Question 2

class Product():

    def __init__(self, product_id, name, price, author):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.author = author

    def display_info(self):
        print(f"Product info: {self.product_id}, {self.name}, {self.price}, {self.author}")




class book(Product):

    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price, author)
        self.author = author
        

    def user_info(self):
        print(f"book: #{self.product_id} {self.author}")

    
    

my_book = book("123", "Python Essentials", 29.99, "J. Doe")
my_book.display_info()