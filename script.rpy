
define playername = Character("[playername]")
define Father = Character("Father")
label start:
    scene bg login
    $ playername = renpy.input("Identify yourself",length=32)
    $ playername = playername.strip()

    if not playername :
        $ playername = "Kenji"
    playername "I'm [playername]."
    return
label History:
    scene bg histoty
return

label bedroom :
    scene bg bedroom
        play music "morning-in-the-mountains-201840g" fadeout 1
     playername "Hello?"

return


