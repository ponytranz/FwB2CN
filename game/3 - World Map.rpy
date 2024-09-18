label worldmap:
    stop music fadeout 2
    scene black
    if weather == 1:
        show map day
    if weather == 2:
        show map rain
    if weather == 3:
        show map night
    if weather == 4:
        show map nightrain
    show mapbuttons
    if completion >= 5 and v2complete == 0:
        $ v2complete = 1
        "You've completed all the main story content so far in 0.2! Thanks for playing! {a=https://www.patreon.com/TwistedScarlett}Support me on Patreon for updates and your say in the game's development!{/a}"
        "Would you please take a moment to review this game?"
        menu:
            "What website did you download the game from?"
            "Patreon":
                "Please post your thoughts in the #my-games-spoiler-discussion channel of the Patreon Discord server! Thank you!"
            "F95zone":
                show reviewf95 with d
                "You can leave a review by clicking the stars in the top right of the thread."
                "I also read all posts on this thread, if you have any bug reports or simply something to say, feel free to drop by!"
                hide reviewf95 with d
            "No Thanks":
                pass
    hide screen vnui
    with d
    ### Common Events
    $ phoneenabled = 1
    $ textbox = 1
    $ mapphone = 0
    call genreset from _call_genreset
    call stopbgs from _call_stopbgs_9
    call camerareset2 from _call_camerareset2_11
    call todosuggestion from _call_todosuggestion
    call completionpercentcalc from _call_completionpercentcalc
    $ worldmap = 1
    if weather == 1:
        play ambience1 ambienceday volume 0.85
    elif weather == 2 or weather == 4:
        play ambience1 ambiencerain volume 0.5
    elif weather == 3:
        play ambience1 ambiencenight volume 0.85
    call screen worldmap
screen worldmap():
    zorder 100
    if gallery == 0:
        imagemap:
            ground "map icons"
            hover "map iconsh"
            hotspot (1701, 8, 109, 100)  action (SetVariable("todolist", 1))
            hotspot (1811, 8, 96, 99)  action (SetVariable("inventory", 1))
        imagemap:
            ground "mapbuttons"
            hover "mapbuttonsh"
            hotspot (1480, 637, 253, 145) clicked (SetVariable("worldmap", 0), Jump("apartment"))
            hotspot (47, 682, 154, 159) clicked (SetVariable("worldmap", 0), Jump("treehouse"))
            hotspot (360, 265, 147, 136) clicked (SetVariable("worldmap", 0), Jump("farm"))
            hotspot (1761, 399, 154, 144) clicked (SetVariable("worldmap", 0), Jump("brothel"))
            hotspot (35, 238, 202, 131) clicked (SetVariable("worldmap", 0), Jump("forest"))
            hotspot (701, 419, 208, 169) clicked (SetVariable("worldmap", 0), Jump("bakery"))
            hotspot (1125, 215, 177, 147) clicked (SetVariable("worldmap", 0), Jump("bar"))
            hotspot (1412, 97, 191, 158) clicked (SetVariable("worldmap", 0), Jump("castle"))
        text "$ [money]":
            pos (270, 7)
        text "Day [day]":
            pos (75, 7)
        #world map phone
        image "vnui2.png":
            xpos 1800
        imagebutton:
            idle "vnui.png"
            hover "vnuih.png"
            xpos 1800
            action (Play("sound2", "audio/phonestart.ogg"), SetVariable("mapphone", 1))
        if unread >= 1:
            image "notification":
                xpos 1800
            if unread < 10:
                text "[unread]":
                    xpos 1883
            else:
                text "[unread]":
                    xpos 1875
        if mapphone == 1:
            image "phonebg"
            if phonebg == 1:
                image "phonebg1"
            if phonebg == 2:
                image "phonebg2"
            if phonebg == 3:
                image "phonebg3"
            if phonebg == 4:
                image "phonebg4"
            imagemap:
                ground "phonemenu.png"
                hover "phonemenuh.png"
                if phoneenabled == 1:
                    hotspot (613, 146, 191, 181) action (Play("sound2", "audio/click1.ogg"), Jump("msgs"))
                    hotspot (857, 150, 187, 176) action (Play("sound2", "audio/click1.ogg"), Jump("todo"))
                    hotspot (1095, 151, 185, 202) action (Play("sound2", "audio/click1.ogg"), Jump("gallery"))
                    hotspot (620, 385, 189, 238) action (Play("sound2", "audio/click1.ogg"), Jump("socials"))
                    hotspot (861, 392, 186, 229) action (Play("sound2", "audio/click1.ogg"), Jump("shop1"))
                    hotspot (1089, 395, 188, 229) action (Play("sound2", "audio/click1.ogg"), Jump("shop2"))
                    hotspot (624, 627, 180, 204) action (Play("sound2", "audio/click1.ogg"), Jump("music"))
                    hotspot (859, 625, 186, 209) action (Play("sound2", "audio/click1.ogg"), Jump("cheats"))
                    hotspot (1092, 625, 193, 216) action (Play("sound2", "audio/click1.ogg"), Jump("settings"))
                    ## Close
                    hotspot (834, 988, 240, 84) action (Play("sound2", "audio/click1.ogg"), SetVariable("mapphone", 0))
            #notifications
            if unread > 0:
                image "notification":
                    pos (700, 145)
            if feedupdate > 0:
                image "notification":
                    pos (700, 380)
            text "[completionpercent:.02f]%":
                pos (940, 185)
            if phoneenabled == 0:
                image "black":
                    alpha 0.75

label apartment:
    hide screen worldmap
    scene bg apartment
    show mox happy
    with d
    menu moxmenu:
        mox "Hey stud!"
        "Gift" if moxgift != 7:
            menu moxgiftmenu:
                "Punk Costume - Owned: [punk]" if moxiepunk == 0:
                    if punk >= 1:
                        $ moxgift += 1
                        $ moxiepunk = 1
                        show mox laughing with d
                        "[mox]'s eyes widen as she unwraps the gift, revealing a set of bold spiked accessories. Her expression shifts from surprise to delight as she examines its features."
                        mox "Behold, the Great and Powerful [mox] has received an unexpected yet marvelous gift! Truly, this'll amplify my already dazzling presence."
                        mox "Thank you so much, baby. I know exactly how to use this one against you."
                        show mox happy with d
                    else:
                        play sound2 error
                "Bunny Girl Costume - Owned: [bunnygirl]" if moxiebunnygirl == 0:
                    if bunnygirl >= 1:
                        $ moxgift += 1
                        $ moxiebunnygirl = 1
                        show mox laughing with d
                        "[mox]'s eyes widened with delight as she unwrapped the gift, revealing a sleek bunny suit complete with fishnets and a playful plug tail."
                        "Whoa, you really outdid yourself this time!” she exclaimed, holding up the outfit."
                        "Her fingers traced the smooth fabric, and she couldn’t help but grin."
                        mox "This is absolutely adorable. I love it! I can't wait to try it out with you."
                        show mox happy with d
                    else:
                        play sound2 error
                "Pantyhose - Owned: [pantyhose]" if moxiepantyhose == 0:
                    if pantyhose >= 1:
                        $ moxgift += 1
                        $ moxiepantyhose = 1
                        show mox laughing with d
                        "[mox]'s eyes lit up as she unwrapped the pantyhose."
                        mox "Wow, these are perfect! You really know my style!"
                        show mox happy with d
                    else:
                        play sound2 error
                "Lingerie - Owned: [lingerie]" if moxielingerie == 0:
                    if lingerie >= 1:
                        $ moxgift += 1
                        $ moxielingerie = 1
                        play sound2 equip
                        show mox laughing lingerie with d
                        mox "Oh, this is absolutely gorgeous!"
                        "She slipped it on immediately, a sly smile playing on her lips."
                        mox "You've got excellent taste, darling. Thank you, this is a gift we'll both enjoy~"
                        show mox happy -lingerie with d
                    else:
                        play sound2 error
                "Buttplug - Owned: [buttplug]" if moxiebuttplug == 0:
                    if buttplug >= 1:
                        $ moxgift += 1
                        $ moxiebuttplug = 1
                        show mox horny with d
                        mox "Aren't you full of surprises!"
                        "She twirled the plug in her fingers, clearly intrigued."
                        mox "Never used one, but..."
                        "Leaning in closer, her voice drops to a playful whisper."
                        mox "I can't wait to try it out later~"
                        show mox happy with d
                    else:
                        play sound2 error
                "Anal Lubrication - Owned: [lubrication]" if moxielubrication == 0:
                    if lubrication >= 1:
                        $ moxgift += 1
                        $ moxielubrication = 1
                        show mox horny with d
                        mox "Well, well, look at you, thinking ahead!"
                        "She examined the bottle with a playful smirk, clearly pleased."
                        mox "You really do know how to spoil a girl."
                        mox "And I have a feeling that this is going to come in handy very soon~"
                        show mox happy with d
                    else:
                        play sound2 error
                "Lewd Spellbook - Owned: [lewdspellbook]" if moxielewdspellbook == 0:
                    if lewdspellbook >= 1:
                        $ moxgift += 1
                        $ moxielewdspellbook = 1
                        show mox horny with d
                        mox "Ohoh, this is wickedly delightful!"
                        "She bit her lip as she traced the ornate cover with her fingers."
                        mox "You really know the way to a girl's heart."
                        "Flipping through the pages, she chuckled at the illustrations and incantations."
                        mox "I can't wait to try some of these out! You'll definitely be getting a front-row seat to the magic show, stud~"
                        show mox happy with d
                    else:
                        play sound2 error
                "Back":
                    jump moxmenu
            jump moxgiftmenu
        "Replay Events":
            menu:
                "While replaying, you can return at any time using the phone."
                "Replay Intro": 
                    $ gen3 = 0
                    $ replay = 1
                    show screen vnui
                    call intro from _call_intro
                "Replay [mox] & [pen] Double Blowjob":
                    $ gen3 = 0
                    $ replay = 1
                    show screen vnui
                    call moxpen1 from _call_moxpen1
                "Replay [mox] & [pen] Threesome":
                    $ gen3 = 0
                    $ replay = 1
                    show screen vnui
                    call moxpen2 from _call_moxpen2
                "Back":
                    jump moxmenu
        "Sex":
            show mox wink
            mox "Yes please~"
            if energytutorial == 0:
                call energytutorial from _call_energytutorial
            menu:
                "Energy: [energy]"
                "No Energy Left" if energy <= 0:
                    "I feel exhausted!"
                    jump moxmenu
                "Facesitting" if energy > 0:
                    call moxfacesitting from _call_moxfacesitting
                "Legs-Up Missionary" if energy > 0:
                    call moxmissionary from _call_moxmissionary
                "Standing From Behind" if energy > 0:
                    call moxfrombehind from _call_moxfrombehind
                "Back":
                    show mox happy with d
                    mox "Aw."
                    jump moxmenu
        "Sleep":
            jump newday
        "Outside":
            jump worldmap
    call postreplaycleanup from _call_postreplaycleanup
    play ambience1 ambiencenight
    jump apartment
label forest:
    "In Dev"
    jump worldmap
label bakery:
    "In Dev"
    jump worldmap
label bar:
    "In Dev"
    jump worldmap
label castle:
    "Guards at the city gate stop me, refusing me entry without a pass."
    jump worldmap

label newday:
    stop music
    call stopbgs from _call_stopbgs_17
    label sleep:
        show bg moxiebedroom2 with d
        call nightevent from _call_nightevent
        scene black with d
        show bg moxiebedroom with dissolve
        pause 0.1
        show bg apartment2 with dissolve
        call dayevent from _call_dayevent
        play ambience1 ambiencenight
        show bg apartment with dissolve
        "As the sun began to set, the city woke up, and it was time for me to head out."
    show black with d
    #variables
    call versionfix from _call_versionfix
    $ weather = renpy.random.randint(3,4)
    $ day += 1
    $ save_name = "v0.2 - Day {} - {}%".format(day, completionpercent)
    $ energy = maxenergy
    jump worldmap

label todosuggestion:
    #Brothel 1 is the Default Suggestion
    if brothelroute1 == 1 and farmroute1 == 0:
        #Farm 1 Suggestion
        $ todosuggestion = "I'll make good time if I visit the farm today."
    elif farmroute1 == 1 and magicroute1 == 0:
        #Magic 1 Suggestion
        $ todosuggestion = "Now might be a good time to see if {} has my city pass.".format(lil)
    elif magicroute1 == 1 and brothelroute2 == 0:
        #Brothel 2 Suggestion (Should be placed after the other first visits in later versions)
        $ todosuggestion = "I'm getting a bit tight on money. Maybe I should do that interview with {}.".format(rub)
    elif v2complete == 1:
        #Complete
        $ todosuggestion = "That's everything in this version! Thanks for playing! {a=https://www.patreon.com/TwistedScarlett}Support me on Patreon for updates and your say in the game's development!{/a}"
    return

label completionpercentcalc:
    $ completionpercent = (completion/fullcompletion * 100)
    $ save_name = "v0.2 - Day {} - {}%".format(day, completionpercent)
    return

label energytutorial:
    $ energytutorial = 1
    "(Having wild sex can be quite tiring! While in free-roam, you only have so much energy to have sex. Going to sleep will restore your energy!)"
    return

label versionfix:
    $ lil1 = lily1
    return 

init:
    $ worldmap = 0
    $ weather = 3
    $ mapphone = 0
    $ todosuggestion = "I should try visiting the brothel, it's the nearest building to the apartment."
    $ completionpercent = 0
    $ completion = 1
    $ fullcompletion = 5
    $ replay = 0
