#Greeting user
print("Welcome to our [Gamebook maker]. Thanks to this software, you are going to be able to create you very own Gamebook\n")

#Title
print("Let's start by first giving you Gamebook a title\n")
title = str(input())

#Options presentation
print ("\n\nGreat! Now that you have given a title to your Gamebook, you have to choose which gameplay aspect it will have.\n\nWe will make different propositions, for all of them answer by Yes or No according to wether you want them or not.\n\n")
selected_options = []
def show_options():
    print ("*"*200, "\n")
    print ("Selected options :", selected_options, "\n")
show_options()
y = "Yes"
n = "No"

#Health option selection
print("Do you want the player to have health points?\n")
a = str(input(""))
if a == y:
    health = 0
    selected_options += ["health"]
    print("You have selected the health option")
if a == n:
    print("You have not selected the health option")

show_options()

#Inventory option selection
print("Do you want the player to have an inventory option?\n")
a = str(input(""))
if a == y:
    inventory = []
    selected_options += ["inventory"]
    print("You have selected the inventory option")
if a == n:
    print("You have not selected the inventory option")

show_options()

#Defining the health
if "health" in selected_options:
    print("How much health does the player start with?\n")
    health = int(input())

#Death message
if "health" in selected_options:
    print("Please enter the death message (when the player hits 0 hp)\n")
    death_msg = str(input())
    
#Writing the actual story
print("\n\nGreat, now that you have selected all your options, you are going to be able to start writing your story.\n")
print("This is how it is going to work: you must have prepared your story and separated it in multiple paragraphs, as well as prepared the choices the player can make, to which paragraph each choice redirects the player, and what influence it has on the health and inventory of the player\n")

print("How many paragraphs are there?")
nb_parag = int(input())
all_txt = list(range(nb_parag))
all_choice_txt = list(range(nb_parag))
all_rdrct = list(range(nb_parag))
all_choice_hp = list(range(nb_parag))
y ="yes"
n = "no"

for i in range(0, nb_parag):
    print("What is the number of the paragraph you are now doing?")
    pos_parag = int(input())
    print("Now enter the text of you paragraph")
    txt_parag = str(input())
    del(all_txt[pos_parag-1])
    all_txt.insert(pos_parag-1, txt_parag)
    #Now doing the choices
    print("How many choices does the player have now?")
    nb_choice = int(input())
    #Reseting the temporary lists
    choice_lst = list(range(nb_choice))
    rdrct = list(range(nb_choice))
    choice_hp = list(range(nb_choice))
    choice_inv = list(range(nb_choice))
    for i in range(0, nb_choice):
        print("Enter the text of the choice", i+1)
        txt_choice = str(input())
        #Putting the choice in a temporary list that will reset each paragraph
        del(choice_lst[i])
        choice_lst.insert(i, txt_choice)
        #Choices actions
        print("What paragraph does this choice redirect to?")
        temp_rdrct = int(input())
        del(rdrct[i])
        rdrct.insert(i, txt_choice)
        if "health" in selected_options:
            print("How much health does the player gain from this choice? If he doesn't lose health, type 0, if he loses health, type a negative number")
            temp_hp = int(input())
            del(all_choice_hp[i])
            all_choice_hp.insert(i, txt_choice)
        if "inventory" in selected_options:
            print("Does the player get an item from this choice")
            yn_item_add = 0
            while yn_item_add != y and yn_item_add != n:
                yn_item = str(input)
                if yn_item == y:
                    print("How many items doest the plauyer get?")
                    nb_item = int(input)
                    for i in range(0, nb_item):
                        print("What is the name of the item the player gets?")
                        name_item = str(input)
                        inv.append(name_item)
                if yn_item == n:
                    break
            print("Does this choice remove an item from the player's inventory?")
            yn_item_remove = 0
            while yn_item_remove != y and yn_item_remove != n:
                yn_item_remove = str(input)
                if yn_item_remove == y:
                    print("How many items are removed from the player's inventory?")
                    nb_of_item_removed = int(input)
                    for i in range(0, nb_of_item_removed):
                        print("What is the position of the item you want to remove?")
                        print(inventory)
                        item_to_remove = int(input)
                        del(inventory[item_to_remove])              
    #Putting the temporary list in the permament list
    del(all_choice_txt[pos_parag-1])
    all_choice_txt.insert(pos_parag-1, choice_lst)

print(all_txt)
print(all_choice_txt)
print(inventory)
print(all_rdrct)
print(all_choice_hp)







