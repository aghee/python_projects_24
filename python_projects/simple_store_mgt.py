import csv

class Item:
    pay_rate=0.8 #amount to pay after 20percent disc
    list_all=[]
    def __init__(self,name:str,price:float,quantity=250):
        #Run validations to the received arguments
        # assert isinstance(price,(int,float)),f'{price} should be a number'
        # assert isinstance(quantity,(int,float)),f'{quantity} should be a number'
        assert price >=0, f'Price {price} is not greater than zero!'
        assert quantity>=0,f'Quantity {quantity} is not greater than zero!'
        assert isinstance(name,str),f'Enter a string  for {name} please'
        
        #Assign to self object
        self.name=name
        self.quantity=quantity
        self.price=price

        #Actions to execute
        Item.list_all.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity
    def apply_disc(self):
        self.price=self.price*self.pay_rate
    def __repr__(self):
        return f'Item(\'{self.name}\',{self.price},{self.quantity})'
    #instantiate the object itself, object no longer in this file
    @classmethod
    def instantiate_csv(cls):
        with open('items.csv','r') as file_one:
            reader=csv.DictReader(file_one)
            itemlist=list(reader)
        for item in itemlist:
            # Create/instantiate objects
            Item(
                # get() retrieve values associated with specific keys without the risk of raising KeyError exceptions
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity'))

            )

#how to validate data type of arguments passed when instantiating an object
#eg name:str at  __init__ does not do anything--use assert???
#store in .csv file--allows data to be stored in a table format
# item1=Item('Hp85',100,5)
# item2=Item('Laptop',1000,45)
# item3=Item('Cable',200,15)
# item4=Item('Mice',850,35)
# item5=Item('Keyboard',13,1500)

# print(Item.list_all)
Item.instantiate_csv()
print(Item.list_all)

#how would this be for this case???
# if __name__=='__main__':
#     pass

# item1.pay_rate=0.9
# item1.apply_disc()
# print(item1.price)

# item2.pay_rate=0.5
# item2.apply_disc()
# print(item2.price)
# print(Item.__dict__)#all attributes for class level
# print(item1.__dict__)#all attributes for instance level