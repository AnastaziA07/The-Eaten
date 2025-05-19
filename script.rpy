screen wait_screen(duration=2.0):
    timer duration action Return()
    key "mouseup_1" action NullAction()  # ปิดการคลิกซ้าย
define playername = Character("[playername]")
define Father = Character("Father")
define priest = Character("Priest")

default current_time = "morning"   # ค่าตั้งต้นคือเช้า
default interaction_count = 0      # จำนวนการคุยที่เกิดขึ้นในวันนั้น

# ฟังก์ชันอัปเดตเวลา
init python:
    def update_time():
        global interaction_count
        global current_time

        interaction_count += 1
        if interaction_count >= 3:
            if current_time == "morning":
                current_time = "night"
            else:
                current_time = "morning"
            interaction_count = 0


screen scene_interact():

    # ปุ่มไปชิงช้า
    imagebutton:
        idle "exchage_prob.png"        # รูปตอนยังไม่ชี้เมาส์
        hover "exchage_prob_click.png"      # รูปตอนชี้เมาส์
        xpos 500
        ypos 200
        action Jump("swing")

    # ปุ่มเมื่อกดไปที่เด็ก
    imagebutton:
        idle "exchage_prob.png"        # รูปตอนยังไม่ชี้เมาส์
        hover "exchage_prob_click.png"      # รูปตอนชี้เมาส์
        xpos 100
        ypos 200
        action Jump("children")


label start:

    scene bg login
    show screen quest_notification
    with fade
    $ playername = renpy.input("Identify yourself",length=32)
    $ playername = playername.strip()

    if not playername :
        $ playername = "Kenji"
    playername "I'm [playername]."

    jump history

    return

label history:
    window hide  # ซ่อนหน้าต่างข้อความก่อนเริ่ม
    play music "nocturnal-fantasy-enchanted-loop-284212.mp3" fadein 0.5
    scene ritual with dissolve
    call screen wait_screen(2.0)
    "A long time ago, the belief in reincarnation emerged"
    window hide
    scene seprate with dissolve
    call screen wait_screen(2.0)
    window show
    "Giving rise to a grand cult that called itself the 'Messengers of the Afterlife.' They claimed to communicate with the god of Saṅsarās, the deity who governs the cycle of life. Thus began the ritual of delivering messages to the deceased—a practice that initially consisted of simple burials, cremations, and brief blessings."
    window hide
    scene sepatetodarkside with dissolve
    call screen wait_screen(2.0)
    window show
    "Over time, however, these customs evolved into elaborate ceremonies accepted as normal, with no one questioning where these people came from. As long as they believed in the same ideals, no doubt was cast upon them."
    window hide
    scene trio with dissolve
    call screen wait_screen(2.0)
    window show
    "Then came the modern era—the Age of Truth—a time when the new generation no longer accepted blind faith, but sought evidence behind every belief. These truth-seekers became known as scientists."
    window hide
    scene Who with dissolve
    call screen wait_screen(2.0)
    window show
    "In the beginning, society resisted them, for their truths contradicted the long-standing faith. But the scientists did not give up. They continued to seek out the truth and share it with the world, leading us to the present day—an age where belief and science coexist in harmony."
    window hide
    scene promise with dissolve
    call screen wait_screen(2.0)
    window show
    "That harmony, however..."
    window hide
    scene brokenpromise with dissolve
    call screen wait_screen(2.0)
    window show
    " would soon be shattered... For the deity once revered was not the exalted being people worshipped, but rather a dangerous entity to be feared."
    window hide
    stop music fadeout 0.5

    jump bedroomscene

    return

label bedroom:
    scene bedroom
    return

label bedroomscene:
    play music "morning.mp3" fadein 0.5
    scene wakeupclose with dissolve
    call screen wait_screen(2.0)
    scene wakeupopen with dissolve
    call screen wait_screen(2.0)
    scene wakeupnotice with dissolve
    call screen wait_screen(2.0)
    scene phonering with dissolve
    call screen wait_screen(2.0)
    scene phonehand with dissolve
    call screen wait_screen(2.0)
    scene phonegrab with dissolve
    call screen wait_screen(2.0)
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

######################

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

    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

init: ### just setting variables in advance so there are no undefined variable problems
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)]) 
        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve 
        # ^This is the timer bar.

label questiontime1 :

    label menu1 :
        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'getpunch'
        show screen countdown
        "The priest think that you are a threat"
    menu:

        "Throw a punch" :
                jump menu2
        "Dodge" :
                jump menu3

            
    hide screen countdown
    jump getpunch

    label menu2 :
        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'getpunch'
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
        $ timer_jump = 'getpunch'
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
        $ timer_jump = 'lostsomeenrgy'
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
        $ timer_jump = 'dead'
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
#############################
# เก็บไว้ใน init python หรือเริ่มต้นเกม
init python:
    inventory = []
    toy_collected = False  # ของเล่นเก็บไปแล้วยัง
    quest_1_done = False
    current_quest = "Find the lost toys"

screen show_inventory():
    frame:
        xalign 0.95
        yalign 0.05
        padding 10
        background "#3338"
        has vbox
        text "🎒 Inventory" size 22 color "#fff"
        for item in inventory:
            text "[item]" size 18 color "#fff"



label playground:

    scene bg playground
    show screen toy_scene
    show screen quest_notification

    if not toy_collected:
        "You see something on the floor.."
    else:
        $ current_quest = "Give the lost toys"
        "you have gather all the toys"


    label children:
    scene bg children
    show po normal at left
    show kids happy at right

    playername "Hey kids, do you happen to know the person in this picture?"

    kid "Oh! You mean this scientist guy? Yeah, I kind of know who he is."

    kid "But first, you have to help us find three items — a windmill, a robot, and a wooden sword."

    playername "Alright, kids. But you'd better not break your promise."

    kid "We promise!!"

    jump collect_item


    return

label swing:
    scene bg swing
    with dissolve
    label playground_event:

    playername"Ugh... I'm so stressed out."

    show kids happy at right
    with dissolve

    kid "Hey!! Big bro!"

    playername "Huh?! What is it?"

    kid "Why are you so stressed, big bro? We've been watching you frown for a while now."

    playername "Well... I've got something on my mind."

    "(Po tells the kids about what's been bothering him.)"

    kid "Hmm... Then let us take you to a scientist we know. I think he might be able to help you."

    kid "But you have to help us find three items first — a windmill, a robot, and a wooden sword."

    playername "Alright, kids. But you better keep your promise."

    kid "You got it!!"
    
    $ quest_active = True
    $ quest_items = []

    jump collect_item


    return

label collect_item: 

    scene bg playground  # ใส่พื้นหลังสนามเด็กเล่น

    show screen show_inventory

    show screen toy_scene

screen toy_scene():
    if not toy_collected:
        imagebutton:
            idle "images/exchange_prob.png"
            hover "images/exchange_prob_click.png"
            xpos 600
            ypos 300
            focus_mask True
            action [
                SetVariable("toy_collected", True),
                Function(inventory.append, "Toy"),
                Hide("toy_scene"),
                Notify("You have pick up the toy")
            ]

    textbutton "back":
        xpos 50
        ypos 500
        action Return()


label toy_pickup:
    call screen toy_scene
    return


label talk_to_kid:
    scene bg playground_kid
    show kid normal
    show screen show_inventory
    show screen quest_notification

    if "Toy" in inventory:
        "You found all the lost toy!?"
        $ inventory.remove("Toy")
        $ quest_1_done = True
        "You give the toys back to the child"
        $ current_quest = "Quest complete"
        jump next_quest
    else:
        "Thank you very much.."

        jump child_happy


return
screen quest_notification():
    frame:
        xalign 0.95
        yalign 0.01
        background "#0008"
        padding (10, 5)
        has vbox
        text "Quest " size 18 color "#fff"
        text "[current_quest]" size 16 color "#fff"



