import time

def intro():
    print("Welcome to the Adventure Game!")
    print("You wake up in a mysterious room with no memory of how you got there.")
    print("You notice there are three doors: RED, BLUE, and GREEN.")
    time.sleep(1)
    print("Which door do you choose?")
    door_choice = input("> ").lower()

    if door_choice == "red":
        red_door()
    elif door_choice == "blue":
        blue_door()
    elif door_choice == "green":
        green_door()
    else:
        print("Invalid choice. Please try again.")
        intro()

def red_door():
    print("You enter the red door and find yourself in a dark room.")
    print("You see a dim light in the distance and hear footsteps.")
    time.sleep(1)
    print("What do you do? RUN or HIDE?")
    action_choice = input("> ").lower()

    if action_choice == "run":
        print("You start running towards the light, but trip and fall down a trapdoor.")
        time.sleep(1)
        print("You find yourself in a basement filled with spiders.")
        time.sleep(1)
        print("GAME OVER")
    elif action_choice == "hide":
        print("You hide behind a pile of boxes and wait for the footsteps to pass.")
        time.sleep(1)
        print("You find a key and use it to unlock the door at the end of the room.")
        time.sleep(1)
        print("Congratulations! You have escaped.")
    else:
        print("Invalid choice. Please try again.")
        red_door()

def blue_door():
    print("You enter the blue door and find yourself in a room with a giant snake.")
    print("You notice a sword on the ground and a flute on a pedestal.")
    time.sleep(1)
    print("What do you do? PICK UP SWORD or PLAY FLUTE?")
    action_choice = input("> ").lower()

    if action_choice == "pick up sword" or action_choice == "play flute":
        print("You defeat the snake and find a key.")
        time.sleep(1)
        print("You use the key to unlock the door at the end of the room.")
        time.sleep(1)
        print("Congratulations! You have escaped.")
    else:
        print("Invalid choice. Please try again.")
        blue_door()

def green_door():
    print("You enter the green door and find yourself in a room with three chests.")
    print("You notice a sign that reads: 'Only one chest contains the key to escape.'")
    time.sleep(1)
    print("Which chest do you choose? LEFT, MIDDLE, or RIGHT?")
    chest_choice = input("> ").lower()

    if chest_choice == "left":
        print("You open the left chest and find a snake.")
        time.sleep(1)
        print("The snake bites you and you die.")
        time.sleep(1)
        print("GAME OVER")
    elif chest_choice == "middle" or chest_choice == "right":
        print("You open the chest and find a key.")
        time.sleep(1)
        print("You use the key to unlock the door at the end of the room.")
        time.sleep(1)
        print("Congratulations! You have escaped.")
    else:
        print("Invalid choice. Please try again.")
        green_door()

intro()