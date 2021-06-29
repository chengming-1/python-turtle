import pprint

def pizza(a):
    print("I would like a", a['size']," pizza on a", a['crust'],"crust")
    print("With", len(a['toppings']), "toppings on it:")
    for item in a['toppings']:
        print("-",item)
    print('The delivery address:')
    print(a['delivery']['street'])
    print(a['delivery']['apartment'])
    print(a['delivery']['type'])

deluxe_pizza = {
   'crust': "thin",
   'size': "extra large",
   'toppings': ["pepperoni",
                "black olives",
                "green peppers",
                "sausage",
                "mushrooms"
               ]
    }

address = {
    'street': "1278 Spartan Dr",
	'apartment': "4B",
	'type': "apartment"
    }

cheese_pizza = {
	'crust': "traditional",
	'size': "large",
	'toppings': ['cheese'],
	'delivery': address
}
pizza(cheese_pizza)
pprint.pprint(cheese_pizza)