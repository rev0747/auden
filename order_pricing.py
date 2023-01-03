product_list ={}

# used to create the product with its properties
class Product:
    def __init__(self, product_code,price, special_quantity=None, special_price=None):
        self.product_code = product_code
        self.price = price 
        self.special_quantity = special_quantity 
        self.special_price = special_price

    def __str__(self):
        return " product_code: %s \n Price: %s \n Special_Quantity: %s \n Special_price: %s \n" % (self.product_code, self.price,self.special_quantity, self.special_price)
    
    
# used to create a order with the product name and quantity    
class Order:    
    def __init__(self, *products_name_quantity_list):
        self.order_product_list ={}        
        for p,q in products_name_quantity_list:
            self.order_product_list[p] =q 
            
    def __str__(self):
        return str(self.order_product_list)

    def total_price(self):
        total_price_val=0
        for product_name,quantity in self.order_product_list.items():
            total_price_val+=calculate_price(product_name, quantity)
        return str(total_price_val)
            
# calculate the total price of each products 
def calculate_price(product_name, quantity):
    product=product_list[product_name]
    if product.special_quantity is not None:
        q,r =divmod(quantity, product.special_quantity)
        price = q*product.special_price + r*product.price
    else:
        price = quantity*product.price    
    return(price)
    

#create the product objects
producta= Product('A', 50, 3, 130)
productb= Product('B', 30, 2,45)
productc= Product('C', 10)

#add the product objects to a dictionary. to find the products quickly using its product_code
product_list['A'] =producta
product_list['B'] =productb
product_list['C'] =productc

# Sample execution of the programme
order_total_price = Order(('A', 5), ('B', 5), ('C', 7)).total_price()
print(f"Total price to be paid for order ('A', 5),('B', 5),('C', 7):{order_total_price}")
order_total_price = Order(('A', 1)).total_price()
print(f"Total price to be paid for order ('A', 1):{order_total_price}")
order_total_price = Order(('A', 2)).total_price()
print(f"Total price to be paid for order ('A', 2):{order_total_price}")
order_total_price = Order(('A', 1),('B', 1)).total_price()
print(f"Total price to be paid for order ('A', 1),('B', 1):{order_total_price}")
order_total_price = Order(('A', 1), ('B', 1),('C', 1)).total_price()
print(f"Total price to be paid for order ('A', 1),('B', 1),('C', 1)):{order_total_price}")
order_total_price = Order(('A', 3), ('B', 1)).total_price()
print(f"Total price to be paid for order ('A', 3),('B', 1)):{order_total_price}")

