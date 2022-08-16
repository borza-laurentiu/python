coffee_menu = [
                "Choose a coffee:\n(1)latte \n(2)americano \n(3)espresso\n\n", 
                "Choose the size:\n(1)Large \n(2)Regular \n(3)Small\n\n"
]

coffee_types = {1: "latte", 2: "americano", 3: "espresso"}
size = {1: "large", 2: "regular", 3: "small"}

customer_choice = int(input(coffee_menu[0]))
customer_size = int(input(coffee_menu[1]))

print("You chose " + coffee_types[customer_choice] + " size " + size[customer_size])


    

