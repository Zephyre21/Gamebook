print("Welcome to the game 'my story'! \nThanks to this program, you get to create your very own gamebook. \nYou will be able to imagine twists and denouements and thanks to the multiple choices, each action will have the consequences you have chosen! \nYou are now the master of the game!\nAre you ready to create your story?", "\n\nPress space to continue")
a = str(input(""))
b = " "
while a != b:
    print("Press space to continue")
    a = str(input(""))
while a == b:
    print("Allez, ça continue")
    break