def valid_number():
    while True:
        try:
            temp = int(input())
            return temp
        except ValueError:
            print("Please enter a valid number")

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
a = 0
while a != y and a!= n:
    print("Please answer with Yes or No")
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
a = 0
while a != y and a != n:
    print("Please answer with Yes or No")
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
    health = valid_number()

#Death message
if "health" in selected_options:
    print("Please enter the death message (when the player hits 0 hp)\n")
    death_msg = str(input())
    
#Writing the actual story
print("\n\nGreat, now that you have selected all your options, you are going to be able to start writing your story.\n")
print("This is how it is going to work: you must have prepared your story and separated it in multiple paragraphs, as well as prepared the choices the player can make, to which paragraph each choice redirects the player, and what influence it has on the health and inventory of the player\n")

print("How many paragraphs are there?")
nb_parag = valid_number()
all_txt = list(range(nb_parag))
all_choice_txt = list(range(nb_parag))
all_rdrct = list(range(nb_parag))
all_choice_hp = list(range(nb_parag))
all_inv = list(range(nb_parag))
all_inv_rem = list(range(nb_parag))

for i in range(0, nb_parag):
    print("What is the number of the paragraph you are now doing?")
    pos_parag = valid_number()
    print("Now enter the text of you paragraph")
    txt_parag = str(input())
    del(all_txt[pos_parag-1])
    all_txt.insert(pos_parag-1, txt_parag)
    #Now doing the choices
    print("How many choices does the player have now?")
    nb_choice = valid_number()
    #Reseting the temporary lists
    choice_lst = list(range(nb_choice))
    rdrct = list(range(nb_choice))
    choice_hp = list(range(nb_choice))
    choice_inv = list(range(nb_choice))
    choice_inv_rem = list(range(nb_choice))    
    for i in range(0, nb_choice):
        print("Enter the text of the choice", i+1)
        txt_choice = str(inpuce))
        #Putting the choice in a temporary list that will reset each paragraph
        del(choice_lst[i])
        choice_lst.insert(i, txt_choice)
        #Choices actions
        print("What paragraph does this choice redirect to?")
        temp_rdrct = valid_number()
        del(rdrct[i])
        rdrct.insert(i, temp_rdrct)
        if "health" in selected_options:
            print("How much health does the player gain from this choice? If he doesn't lose health, type 0, if he loses health, type a negative number")
            temp_hp = valid_number()
            del(choice_hp[i])
            choice_hp.insert(i, temp_hp)
        if "inventory" in selected_options:
            print("Does the player get an item from this choice?")
            yn_item_add = 0
            while yn_item_add != y and yn_item_add != n:
                print("Please answer with Yes or No")
                yn_item_add = str(input())
                if yn_item_add == y:
                    print("What is the name of the item the player gets?")
                    name_item = str(input())
                    del(choice_inv[i])
                    choice_inv.insert(i, name_item)
                if yn_item_add == n:
                    name_item = "none"
                    del(choice_inv[i])
                    choice_inv.insert(i, name_item)
                    break
            print("Does this choice remove an item from the player's inventory?")
            yn_item_remove = 0
            while yn_item_remove != y and yn_item_remove != n:
                print("Please answer with Yes or No")
                yn_item_remove = str(input())
                if yn_item_remove == y:
                    print("What is the name of the item you want to remove?")
                    item_rem = str(input())
                    del(choice_inv_rem[i])
                    choice_inv_rem.insert(i, name_item)
                if yn_item_remove == n:
                    item_rem = "none"
                    del(choice_inv_rem[i])
                    choice_inv_rem.insert(i, name_item)
            del(all_inv[i])
            all_inv.insert(i, choice_inv)
            del(all_inv_rem[i])
            all_inv_rem.insert(i, choice_inv_rem)   
            del(all_choice_hp[i])
            all_choice_hp.insert(i, temp_hp)     
        del(all_rdrct[i])
        all_rdrct.insert(i, rdrct)        
    #Putting the temporary list in the permament list
    del(all_choice_txt[pos_parag-1])
    all_choice_txt.insert(pos_parag-1, choice_lst)

with open("Gamebook.txt", "a") as f:
    f.writelines(i for i in all_txt)

print(all_txt)
print(all_choice_txt)
print(inventory)
print(all_rdrct)
print(all_choice_hp
print(all_inv)
print(all_inv_rem)