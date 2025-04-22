
define e = Character("Eileen")
define playername = Character("[playername]")

label start:
    scene bg room
    e "You've created a new Ren'Py game."
    $ playername = renpy.input("กรอกนามของท่าน",length=32)
    $ playername = playername.strip()

    if not playername :
        $ playername = " เคนจิ"
    playername "ฉันมีนามว่า[playername]."
    return
