import os
rooms = {
    "main lobby" : {"north":"weapon room","south":"poition room","left":"boss room"},
    "weapon room" : {"south" : "main lobby","item" : "rockets"},
    "potion room" : {"north" : "main lobby","item" : "heal spell"},
    "boss room" : {"boss" : "the void","right":"main lobby"}
}
inventory=[]
your_place = "main lobby"
message=""
while True:
    print(f"you are in the {your_place}\nInventory : {inventory} \n{"*"*20}")
    print(message)
    if "item" in rooms[your_place].keys():
        the_item = rooms[your_place]["item"]
        if the_item not in inventory:
             if the_item[-1] == "s":
              print(f"you see {the_item}")
             elif the_item[0] in ['a','e','u','o','i']:
                print(f"you see{the_item}")
             else:
                 print(f"you see{the_item}")
    if "boss" in rooms[your_place].keys():
        if len(inventory)<2:
            print("you lost the game")
            break
        else:
            print(f"you beat{your_place} boss")
            break
the_move = input("enter your move:\n")



              