# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define old_man = Character("Mysterious Old Man")
define narrator = Character("Narrator, Dream of Shadows", who_color="#3e034f")

# Game Start
label start:
    # scene file_name: background file_name.png or file_name.jpg must be somewhere in images folder
    # show file_name: character sprite file_name.png or file_name.jpg must be somewhere in images folder
    # play music file_path: play looping music file file_path (path starts in game folder), add fadeout x to fadeout in x sec when next music plays
    # play sound file_path: play sound file file_path once (path starts in game folder)
    play music "sounds/music/night.mp3" fadeout 1
    scene solid_black

    narrator "Welcome, wanderer. It seems you have strayed from the path and somehow entered my domain."
    narrator "How peculiar. But while you are here, wanderer, answer me this: do you believe there is such thing as life after death?"
    
    show blue_flame1:
        xalign 0.5
        yalign 0.4
    with Dissolve(0.5)
    hide blue_flame1 with Dissolve(0.5)
    
    narrator "If you don’t, then I suppose that’s normal. It would be irrational to blame the supernatural for every apparent mystery you come across."
    narrator "But it would also be unfair to dismiss them altogether."
    
    image blue_flame_animated:
        "blue_flame1"
        pause 0.25
        "blue_flame2"
        pause 0.25
        repeat
    show blue_flame_animated:
        xalign 0.5
        yalign 0.4
    with Dissolve(0.5)
    
    narrator "Make no mistake: {b}Ghosts{/b} are real. And you can see them, can’t you?"
    narrator "I know, because you can see the flame. That, my dear, is a Ghost."
    narrator "You are one of the gifted few, and one of even fewer who have begun to tap into their gifts. A {b}Tamer{/b}."
    narrator "And you, wanderer, are especially gifted. But only one shall transcend the boundary and grasp ahold of their true potential…"
    narrator "…Me? Who am I, you ask?"
    
    hide blue_flame_animated with Dissolve(1)
    
    narrator "That is of no consequence. Perhaps a better question is..."
    narrator "Who are you?"
    
    python:
        player_firstname = renpy.input("Enter your first name: ")
        player_firstname = player_firstname.strip() or "Soot" # Default if player enters no name

        player_lastname = renpy.input("Enter your last name: ")
        player_lastname = player_lastname.strip() or "Taymem" # Default if player enters no name
    
    define player = Character("[player_firstname]")
    
    narrator "…I see. I shall keep it in mind."
    narrator "Now go forth. Seek power, whatever your context, and peer into the beyond."
    narrator "I will watch over you closely, {b}[player_firstname] [player_lastname]{/b}, and shall eagerly await the day we meet again…"
    
    player ". . ."
    
    # Game End
    return
