# this function will use two parameters
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    
    # tell the user the size of the pizza
    # size is an 'int' type, so turn into string for concatenation
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    
    # then list the toppings for that pizza
    for topping in toppings:
        print("- " + topping)