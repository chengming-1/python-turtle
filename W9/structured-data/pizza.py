import random
def print_pizza_order(pizza):
    print("I would like a", pizza['size'], "pizza on a", pizza['crust'], "crust")
    print("With", pizza['toppings'], "on it")

monday = {'size': "small", 'crust': "traditional", 'toppings': "extra cheese"}
friday = {'size': "large", 'crust': "deep dish", 'toppings': "pepperoni"}
tuesday={'size': "medium", 'crust': "deep dish", 'toppings': "extra cheese"}
print_pizza_order(random.choice([monday,friday,tuesday]))

