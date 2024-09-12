def f():
    pass 
"""
def f1(my_list = None):
    if my_list is None:
        my_list = []
    my_list.append("###")
    return my_list

my_list = f1(my_list=None)   # or we can just write print(f1()) , it will have same output
print(my_list)  
"""
"""
#python assigns the same address/ Id for same variable if it has been called many times in code(though it has been initialized at the begining)
def f2(my_list = []):
    print(id (my_list))
    my_list.append("###")
    return my_list

print(f2())
print(f2())
"""

"""
# *args can  take as many arguments as we can assign 
def avg(*args):
    total = 0
    for i in args:
        total += i
    return total/len(args)

print(avg(1,2,3,4,5))
"""
"""
#**kwargs takes the dictionary as argument , ** means key- value pair
def f(**kwargs):
    for key, val in kwargs.items():
        print(key, "->", val)
        
f(pizza = 1, tomato = 2, potato = 3)
"""
"""
def f(apple, oranges, *args, **kwargs):
    print(f"apple = {apple}")
    print(f"oranges = {oranges}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")
    
    
apple = 2.0
oranges = 3.0

f( apple, oranges, 23,"tomatoes", ora= 33,  x=55, y=100)
"""
"""

#using generator prevents the loading all the data at once 
#it only loads the data which has been requested(yield)
def my_generator():
    yield 1
    yield 2
    yield 3
    
gen = my_generator()
print(next(gen))
print(next(gen))
"""
"""
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
        
gen = csv_reader("1000_lines.txt")
#print(csv_reader("1000_lines.txt"))

print(next(gen))
print(next(gen))

"""
"""
file_name = "1000_lines.txt"
gen = (row for row in open (file_name, "r"))
print(gen)
print(next(gen))
print(next(gen))

"""
#hi this is for the git test in test branch
class pizza():
    
    #list of available itemss 
    available_sizes = ["small", "medium", "large"]
    
    #class variable 
    price_per_topping = 1.5
    
    #class variable 
    no_of_pizza_made = 0
    
    def __init__(self, size, toppings=None):
        if size
        self.size = size
        self.toppings = toppings if toppings else []
        self
        pizza.no_of_pizza_made += 1
        
    def add_topping(self, topping):
        """_
        This method adds toppings.
        """
        
        self.toppings.append(topping)
        
    def remove_toppings(self, topping):
        """
        removes toppings from the topping list
        """
        if topping in self.toppings:
            self.toppings.remove(topping)
            
        else:
            print(f"{topping} not found")
            
    def get_price(self):
        """Generates price of the pizza for different sizes
        """
        
        base_price={
            "small" :8,
            "medium" :12,
            "large" :15
        }
        
        topping_price =self.price_per_topping* len(self.toppings)
        return base_price[self.size] + topping_price
            
    def __str__(self):
        """provide name to the class object of pizza
        """
        toppings_str = "".join(self.toppings) if self.toppings else "no-toppings"
        return (f"{self.size} size pizza with {toppings_str}.price {self.get_price():.2f}"  ) 
       
 # pizz1 and pizz2 are the instances 
pizz1 = pizza(size = "Medium")
pizz1.add_topping("tomatoes")

pizz2 = pizza(size = "Large")
pizz2.add_topping("onion")


print(pizz1)
print(pizz2)



