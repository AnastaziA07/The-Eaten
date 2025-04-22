
define e = Character("Eileen")
define playername = Character("[playername]")

label start:
    scene bg room
    show eileen happy
    e "You've created a new Ren'Py game."
    $ playername = renpy.input("Identify yourself",length=32)
    $ playername = playername.strip()

    if not playername :
        $ playername = "Kenji"
    playername "I'm [playername]."
    return
