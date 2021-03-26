health = int(input("Choose the ammount of health for your hero: "))
inventory_slots = int(input("Choose the ammount of inventory slots for your hero: "))
inventory = []
number_of_items = int(input("How many items do you want to insert in the game?: "))
item_list = []
for i in range(0, number_of_items):
    print("Name of the item", i+1, " : ")
    item_name = str(input(""))
    item_list += [item_name]
print("Here are the items that you have selected:",item_list)

