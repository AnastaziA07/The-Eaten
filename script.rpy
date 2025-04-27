
define playername = Character("[playername]")
define Father = Character("Father")
label start:

    scene bg login
    with fade
    $ playername = renpy.input("Identify yourself",length=32)
    $ playername = playername.strip()

    if not playername :
        $ playername = "Kenji"
    playername "I'm [playername]."

    jump history

    return

label history:
    play music "funeral.mp3" fadein 0.5
    scene library
    with dissolve
    "Hiya"
    stop music fadeout 0.5

    jump bedroom

    return

label bedroom:
    play music "morning.mp3" fadein 0.5
    scene bedroom
    with dissolve

    play sound "phonecall.mp3" fadein 0.5 volume 0.1
    queue sound "phone-pick-up-46796.mp3" fadein 0.5 volume 0.5

    playername "Hello?"
    Father "Hi,[playername] sorry for calling this early son.."
    playername "It's fine, what's up?"
    Father "well,*sign* listen carefully son... our granmma had pass away.."
    playername "are you kidding?"
    Father "Sorry son.."
    Father"take your time... the funeral will be setting on Sunday 17.00 p.m. don't be late okay"
    Father "Drive safe son, you can call us anytime okay?"
    playername "yes.."
    play sound "phonehangingup.mp3" fadein 0.5
    stop music fadeout 0.5 


    return
