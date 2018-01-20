# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define old_man = Character("Mysterious Old Man")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene dark_school

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show kek:
        xalign 0.5
        yalign 0.4

    # These display lines of dialogue.

    old_man "Uhhhhnn I sure do love me some fresh young kids."

    old_man "What's your name young man?"
    
    python:
        player_name = renpy.input("Your name: ")
        player_name = player_name.strip() or "Soot Taymem"
    
    old_man "Mmmm I see, I won't forget you [player_name]"
    
    define player = Character("[player_name]")
    
    player "..."
    
    # This ends the game.

    return
