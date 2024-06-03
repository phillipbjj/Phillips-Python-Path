class Category:
    
    def __init__(self, food, entertainment, clothing, gambling, crafts):
        self.food = food
        self.entertainment = entertainment
        self.clothing = clothing
        self.gambling = gambling
        self.crafts = crafts
        
    """food = Category("Food")

    categories = [Category.food ]
    for category in Category:  
        categories.append(category)
    print(categories)"""
    
    ledger = []


    def create_spend_chart(self, categories):
        pass

    def deposit(self, amount, description=''):
       # for category in Category:
        #    ledger.append({self.amount} )   #f'NationalPokedex: {self.pokedex}
        
        
        pass

    def withdraw(self, amount, description): #amount passed in should be stored as negative in the ledger. if overdrawn then return false
        pass

    def get_balance(self, balance):
        pass

    def transfer(self, amount, Category):
        pass
    
    def check_funds(self, amount): #returns false if the amount is greater than the balance of the budget category
        pass
    
    