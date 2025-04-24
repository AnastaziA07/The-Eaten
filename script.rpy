
define playername = Character("[playername]")
define define f = Character("Father")
label start:
    scene bg login
    $ playername = renpy.input("Identify yourself",length=32)
    $ playername = playername.strip()

    if not playername :
        $ playername = "Kenji"
    playername "I'm [playername]."
    return
label Fcall:
    scene bg bedroom
return

