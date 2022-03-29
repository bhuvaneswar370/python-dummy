## Interface for ordering Menu Items
''' We want to let customer order and add as many menu items as they want. A for loop wouldn't be good for this because 
we don't know how many times to loop... '''
## A while loop would be better since while loops continue looping while a condition is True.

'''


x =0

while x!=3:
    print(x)
    x = x+1
'''
orders= []
menu = ['idly','dosa','chapathi']
found =0
order = input("what would yo like to order?(Q to quit) ")
while (order.upper() != 'Q'):
    breakpoint()
    found = menu.get(order)
    if found:
        orders.append(order)
    else:
        print("Menu item doesn't exist")

print(order)