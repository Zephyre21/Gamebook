print ("Great! Now that you have given a title to your Gamebook, you have to choose which gameplay aspect it will have.\nWe will make different propositions, for all of them answer by Yes or No according to wether you want them or not.\n")
selected_options = ["none"]
def show_options():
    print ("*"*200, "\n")
    print ("Selected options :", selected_options, "\n")
show_options()
b = "Yes"
c = "No"

#Health option selection
print("Do you want the player to have health points?")
a = str(input(""))
if a == b:
    health = 0
    selected_options = ["health"]
    print("You have selected the health option")
if a == c:
    print("You have not selected the health option")

show_options()

#Inventory option selection
print("Do you want the player to have an inventory option?")
a = str(input(""))
if == b:
    inventory = []
    selected_options += ["inventory"]
    print("You have selected the inventory option")
    break
if == c:
    print("You have not selected the inventory option")
    break

show_options()