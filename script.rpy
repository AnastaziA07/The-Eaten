
define playername = Character("[playername]")
define Father = Character("Father")
define priest = Character("Priest")
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
    play music "nocturnal-fantasy-enchanted-loop-284212.mp3" fadein 0.5
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

    jump funeral

    return

label funeral:
    play music "funeral.mp3" fadein 0.5
    scene bg funeral
    with dissolve

    scene bg met the priest
    with dissolve
    
    menu :
        "Your action?"

    "ask the priest what is he doing"
    jump askpriest

    "insult the priest"
    jump insult

    "keep watching"
    jump keepwatch

    "take a picture"
    jump takeapic


    return

label takeapic :
    scene bg met the priest
    with dissolve

    jump dead

    return

label keepwatch :

    scene bg met the priest
    with dissolve
    jump bedroom

    return

label insult :

    playername "What on earth are you doing with my granma!!"
    jump fight

    return

label askpriest :
    scene bg zoom
    with dissolve

    playername "what are you doing?"
    priest "*surprised* I'm just doing an extra rite for mrs.angela"

menu :
    "Your action?"

    "ask again" :
        jump askpriestsecondtime
    "go home" :
        jump bedroom
    
return 
    

label askpriestsecondtime :
    
    playername "I don't remember there's an extra rite.. ,what are you doing?"
    priest "*gloomy face* I'm just doing an extra rite for mrs.angela.."

    menu :
        "Your action?"

        "go back home" :
            jump dead

        "ask again" :
            jump askpriestthirdtime

    return

label askpriestthirdtime :

    playername "seriously priest what are you doing.."
    priest "..."
    jump dead

    return

label chruch:
    scene bg chruch
    with dissolve
    return

label children:

    return

label lab:

    return

label hospitol :

    return

label dead :
    scene bg dead
    with dissolve
    return

label fight :

    return
