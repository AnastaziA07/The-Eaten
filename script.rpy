
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

label funeral :
    play music "funeral.mp3" fadein 0.5
    scene bg funeral
    with dissolve

    scene bg met the priest
    with dissolve

    "Your action?"
    
    menu:
        "Ask the priest what is he doing":
            jump askpriest

        "insult the priest":
            jump insult

        "keep watching" :
            jump keepwatch

        "take a picture" :
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

menu:
    "Your action?"

    "ask again" :
        jump askpriestsecondtime
    "go home" :
        jump bedroom
    
return 
    

label askpriestsecondtime :
    
    playername "I don't remember there's an extra rite.. ,what are you doing?"
    priest "*gloomy face* I'm just doing an extra rite for mrs.angela.."

    menu:
        "Your action?"

        "Go back home" :
            jump dead

        "Ask again" :
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
"You died"
#add cut scene eaten

label fight :

    init :
        $ timer_range = 0
        $ timer_jump = 0
        $ time = 0

        screen countdown :
            timer 0.01 repeat True action If(time > 0,true=SetVariable('time', time -0.01),false=[Hide('countdown'), Jump(timer_jump)])
            bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

label questiontime1 :

    label menu1 :
        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'menu1_slow'
        show screen countdown
    menu :
        "The priest think that you are a threat"
        "Throw a punch" :
                jump menu2
        "Dodge" :
                jump menu3

            
    hide screen countdown
    jump getpunch

    label menu2 :
        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'menu2_slow'
        show screen countdown

        "The priest gets dizzy what will you do next?"

        menu:
            "Throw another puch":
                jump getpunch

            "Dodge":
                jump menu3

            "Ask him again":
                jump getpunch

        hide screen countdown
        jump dead

    label getpunch :
        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'getpunch_slow'
        show screen countdown

        "You get dizzy what will you do next?"

        menu:
            "Run away":
                jump dead

            "Throw a punch":
                jump priestfakepassout

            "Ask him agian":
                jump getpunch
            "Dodge":
                jump lostsomeenrgy

    hide screen countdown
    jump dead

    label lostsomeenrgy :
        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'lostsomeenrgy_slow'
        show screen countdown

        "You have lost some enenergy what will you do next?"

        menu:
            "Run away":
                jump dead
            "Throw a punch":
                jump priestfakepassout
            "Ask him agian":
                jump getpunch
            "Dodge":
                jump getpunch

    hide screen countdown
    jump dead
    
    label menu3 :
        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'menu3_slow'
        show screen countdown

        "Your action?"

        menu:
            "Run away":
                jump dead
            "Throw a punch":
                jump priestfakepassout
            "Ask him agian":
                jump getpunch
            "Dodge":
                jump getpunch

        hide screen countdown
        jump dead

    label priestfakepassout :
        "The priest has pass out ,what will you do next? "
    menu:
        "Call the police":
            jump dead
        "Go back home":
            jump bedroom
        "Call out for help":
            jump dead

    return
