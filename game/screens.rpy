screen vnui():
    zorder 100
    if replay == 0:
        imagebutton:
            idle "vnui.png"
            hover "vnuih.png"
            xpos 1800
            action (Play("sound2", "audio/phonestart.ogg"), Hide("vnui"), SetField(persistent,"quick_menu", False), Call("phone"))
    else:
        imagebutton:
            idle "vnuireplay.png"
            hover "vnuireplayh.png"
            xpos 1730 ypos 10
            action (Play("sound2", "audio/phonestart.ogg"), SetVariable("replay", 0), Jump("replay"))

    if unread >= 1:
        image "notification":
            xpos 1800
        if unread < 10:
            text "[unread]":
                xpos 1883
        else:
            text "[unread]":
                xpos 1875
label replay:
    return
label phone: 
    call screen phone_screen
    return
screen phone_screen():
    zorder 94
    if worldmap == 1:
        if weather == 1:
            image "map night"
        if weather == 2:
            image "map night"
        if weather == 3:
            image "map night"
        if weather == 4:
            image "map night"
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
            hotspot (834, 988, 240, 84) action (Play("sound2", "audio/click1.ogg"), Show("vnui"), SetField(persistent,"quick_menu", True), Return())
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

label msgs:
    $ phoneenabled = 0
    #if worldmap == 0:
    #    show screen phone_screen
    menu msgmenu:
        "Unread: [unread]\nRead: [read]"
        "[hon] ([unreadhon])" if farmroute1 == 1:
            menu msgmenuhon:
                "Messages from [hon]"
                "Back":
                    jump msgmenu
        "[blo] ([unreadblo])" if farmroute1 == 1:
            menu msgmenublo:
                "Messages from [blo]"
                "i did it!" if blomsg1 == 1:
                    $ blomsg1 = 2
                    $ unread -= 1
                    $ unreadblo -= 1
                    $ read += 1
                    label blomsg1:
                        blo "hi i sent your letter to anna. and i have something for you too. (Open Attachment)"
                        layeredimage blomsg1:
                            always:
                                "blossommsg1 [blob]"
                            group text:
                                attribute text:
                                    "blossommsg1 text"
                        show blomsg1 text onlayer screens zorder 95
                        $ textbox = 2
                        with d
                        ""
                        show blomsg1 -text onlayer screens zorder 95 with d
                        "{i}Sheesh! The last person I was expecting to get such a raunchy picture from was [blo]!{/i}"
                        "{i}I guess she's someone that's more confident over text than in person. This has me excited to see what she has in store the next time we see each other.{/i}"
                        "{i}Let me just save this picture for later...{/i}"
                        hide blomsg1 onlayer screens
                        $ textbox = 1
                        with d
                    jump msgmenublo  
                "{i}i did it! (Read){/i}" if blomsg1 == 2:
                    jump blomsg1  
                "Back":
                    jump msgmenu
        "[mel] ([unreadmel])" if brothelroute1 == 1:
            menu msgmenumel:
                "Messages from [mel]"
                "Back":
                    jump msgmenu
                "Thanks" if melmsg1 == 1:
                    $ melmsg1 = 2
                    $ unread -= 1
                    $ unreadmel -= 1
                    $ read += 1
                    label melmsg1:
                        mel "It was nice talking to someone that feels sane for once. Let's see if I can't win you back from my sister, hm?"
                        if melnerd == 1:
                            mel "Also, you're the nerd."
                    jump msgmenumel
                "{i}Thanks (Read){/i}" if melmsg1 == 2:
                    jump melmsg1  
        "[rub] ([unreadrub])" if brothelroute1 == 1:
            menu msgmenurub:
                "Messages from [rub]"
                "Back":
                    jump msgmenu
        "[lil] ([unreadlil])" if magicroute1 == 1:
            menu msgmenulil:
                "Messages from [lil]"
                "xxx" if lilmsg1 == 1:
                    $ lilmsg1 = 2
                    $ unread -= 1
                    $ unreadlil -= 1
                    $ read += 1
                    label lilmsg1:
                        lil2 "[lil] 1.0 can't keep me around forever, since it's a big strain on her magic. But before I'm gone, I wanted to share one last picture to commemorate our life together~"
                        layeredimage lilmsg1:
                            always:
                                "lilytext1 [lilb]"
                        show lilmsg1:
                            xalign 0.5 ypos 0
                            linear 1 ypos 0
                            linear 4 ypos -1000
                        with dissolve
                        $ textbox = 2
                        "Woah! What a sexy pic!"
                        "Wasn't the language she was using a little dramatic, though?"
                        menu lilmsg1m:
                            "Zoom Out":
                                show lilmsg1:
                                    xalign 0.5 ypos -500 zpos -1000
                                ""
                                jump lilmsg1m
                            "Scroll Up":
                                show lilmsg1:
                                    xalign 0.5 ypos 0 zpos 0
                                ""
                                jump lilmsg1m
                            "Scroll Down":
                                show lilmsg1:
                                    xalign 0.5 ypos -1000 zpos 0 
                                ""
                                jump lilmsg1m
                            "(Finish Appreciating)":
                                hide lilmsg1 with d
                                $ textbox = 1
                                jump msgmenulil
                    jump msgmenulil
                "{i}xxx (Read){/i}" if lilmsg1 == 2:
                    jump lilmsg1  
                "Back":
                    jump msgmenu
        "[pen] ([unreadpen])":
            menu msgmenupen:
                "Messages from [pen]"
                "Threesome?" if penmsg1 == 1:
                    $ penmsg1 = 2
                    $ unread -= 1
                    $ unreadpen -= 1
                    $ read += 1
                    label penmsg1:
                        pen "Good evening! I was wondering if you wanted to give that threesome with [mox] and I another try? I'm free tonight, let me know if you're interested."
                        menu:
                            "Currently Busy" if worldmap == 0:
                                "I'm too busy right now. I should wait until I have some free time. (You can only accept [pen]'s proposition from the world map.)"
                            "Accept" if worldmap == 1:
                                $ moxpen2 = 1
                                "I send [pen] a reply saying yes, and within the hour, [mox] and I are in the treehouse with her."
                                show bg peneloperoom
                                show pen laughing:
                                    xalign 0.25
                                show mox happy:
                                    xalign 0.75
                                with d
                                pen "I'm so glad you could join us! Allow me to show you to my room."
                                $ replay = 1
                                call moxpen2 from _call_moxpen2_1
                                scene black with d
                                "Some cleaning up later, and we're back home."
                                jump worldmap
                            "Decline" if worldmap == 1:
                                jump msgmenupen
                "{i}Threesome? (Read){/i}" if penmsg1 == 2:
                    jump penmsg1
                "Back":
                    jump msgmenu
        "[mox] ([unreadmox])":
            menu msgmenumox:
                "Messages from [mox]"
                "Back":
                    jump msgmenu
                "hope u slept well" if moxmsg2 == 1:
                    $ moxmsg2 = 2
                    $ unread -= 1
                    $ unreadmox -= 1
                    $ read += 1
                    label moxmsg2:
                        mox "Sorry to leave you alone in bed! I trust you not to trash the apartment while im gone ;) \nIll be back later tonight good luck on your big quest! xx"
                    jump msgmenumox
                "{i}hope u slept well (Read){/i}" if moxmsg2 == 2:
                    jump moxmsg2  
                "Hiya!" if moxmsg1 == 1:
                    $ moxmsg1 = 2
                    $ unread -= 1
                    $ unreadmox -= 1
                    $ read += 1
                    label moxmsg1:
                        mox "I popped ur msg cherry! :) \nMaybe u can pop mine later too? xd"
                    jump msgmenumox
                "{i}Hiya! (Read){/i}" if moxmsg1 == 2:
                    jump moxmsg1  
        "Back":
            $ phoneenabled = 1
            if worldmap == 1:
                call screen worldmap
            call screen phone_screen    
            return

label todo:
    $ phoneenabled = 0
    if worldmap == 0:
        show screen phone_screen
    call completionpercentcalc from _call_completionpercentcalc_1
    menu todomenu:
        "Game Completion: [completionpercent:.02f]%%\nSuggestion: [todosuggestion]"
        "Treehouse ([magiccompletion]/1)":
            menu:
                "First Visit ([magicroute1]/1)":
                    pass
                "Second Visit (In Development)":
                    pass
                "Back":
                    pass
            jump todomenu
        "Brothel ([brothelcompletion]/2)":
            menu:
                "First Visit ([brothelroute1]/1)":
                    pass
                "Second Visit ([brothelroute2]/1)":
                    pass
                "Back":
                    pass
            jump todomenu
        "Farm ([farmcompletion]/1)":
            menu:
                "First Visit ([farmroute1]/1)":
                    pass
                "Second Visit (In Dev)":
                    pass
                "Back":
                    pass
            jump todomenu
        #"Bakery (In Dev)":
        #    play sound2 error
        #    jump todomenu
        #"Forest (In Dev)":
        #    play sound2 error
        #    jump todomenu
        #"Bar (In Dev)":
        #    play sound2 error
        #    jump todomenu
        #"Castle (In Dev)":
        #    play sound2 error
        #    jump todomenu
        #"Extra (In Dev)":
        #    play sound2 error
        #    jump todomenu
        "Back":
            pass
            $ phoneenabled = 1
            if worldmap == 1:
                call screen worldmap
            call screen phone_screen    
            return
label gallery:
    $ phoneenabled = 0
    $ gallery = 1
    show black:
        alpha 1
    $ textbox = 2
    menu gallerymenu:
        "This is a CG gallery, to replay entire scenes, you can visit characters at their homes."
        "Intro":
            menu galleryintromenu:
                "[mox] & [pen] Double Blowjob":
                    show moxpen1a 1 with d
                    ""
                    show moxpen1a 2 with d
                    ""
                    show moxpen1b 1 with d
                    ""
                    show moxpen1b 2 with d
                    ""
                    play sound2 cum
                    show moxpen1b cum with c
                    ""
                    play sound2 cum
                    hide moxpen1b
                    show moxpen1a 2 cum1
                    with c
                    ""
                    show moxpen1a 1 cum2 with c
                    ""
                    hide moxpen1a with d
                "[lil] Buttjob":
                    show lily1a 1 with d
                    ""
                    show lily1a hands with d
                    ""
                    show lily1a -hands with d
                    show lily1a buttjob1 with d
                    ""
                    show lily1a buttjob2 cum with c
                    ""
                    show lily1a -buttjob2 with d
                    ""
                    hide lily1a with d
                "[mox] & [pen] Threesome":
                    show moxpen2a 1 with d
                    ""
                    show moxpen2a 2 with d
                    ""
                    show moxpen2b e1 with d
                    ""
                    show moxpen2b e2 sex1 with d
                    ""
                    show moxpen2b sex2 with d
                    ""
                    show moxpen2b e3 sex3 with c
                    ""
                    show moxpen2b e3 sex4 with d
                    ""
                    show moxpen2c m1 p1 with d
                    ""
                    show moxpen2c m2 p2 cum with c
                    ""
                    hide moxpen2a
                    hide moxpen2b
                    hide moxpen2c
                    with d
                "[mox]'s First Time Marathon" if intro2 == 1:
                    show moxie1a e1 with d
                    ""
                    show moxie1a e2 v1 with d
                    ""
                    show moxie1a e3 v2 cum with c
                    ""
                    show moxie1a -v2  with d
                    ""
                    show moxie1b e1 with d
                    ""
                    show moxie1b e2 v1 with d
                    ""
                    show moxie1b e3 v2 cum with c
                    ""
                    show moxie1b e3 -v2 with d
                    ""
                    hide moxie1a
                    hide moxie1b 
                    with d
                "Back":
                    jump gallerymenu
            jump galleryintromenu
        "Treehouse" if magicroute1 == 1:
            menu gallerytreehousemenu:
                "[lil] Clone Handjob":
                    show lil2a l2e1 with d
                    ""
                    show lil2a hj1 l2e2 with d
                    ""
                    show lil2a lily1 l1e1 with d
                    ""
                    show lil2a l1e2 l2e2 cum hj1cum with c
                    ""
                    hide lil2a with d
                "[lil] Clone Threesome":
                    show lil2b e1 with d
                    ""
                    show lil2b e2 with d
                    show handjob at flip with d:
                        xalign 0.05 yalign 0.9
                    ""
                    show lil2c e2b 
                    hide lil2b
                    hide handjob 
                    with d
                    ""
                    show lil2c v1a e2a with d
                    ""
                    show lil2c v2a with c
                    ""
                    show lil2c e3 cum -v2a with d
                    ""
                    hide lil2c with d
                "[pen] Pet-Play Paizuri":
                    show pen1a e1 collar with d
                    ""
                    show pen1a cum e2 with d
                    ""
                    hide pen1a with d
                    ""
                "[pen] Tied From Behind":
                    show pen1b e1 rope with d
                    ""
                    show pen1b v1 e2 with d
                    ""
                    show pen1b v2 cum e2 with c
                    "" 
                    show pen1b -v2 -v1 e3 with d
                    ""
                    hide pen1b with d
                "Back":
                    jump gallerymenu
            jump gallerytreehousemenu
        "Brothel" if brothelroute1 == 1:
            menu gallerybrothelmenu:
                "[mel] Footjob":
                    show mel1a e1 with d
                    ""
                    show mel1a e2 with d
                    ""
                    show mel1a cum e3
                    with c
                    ""
                    hide mel1a
                "[mel] Blowjob":
                    show mel1b e1 with d
                    ""
                    show mel1b e2 with d
                    ""
                    show mel1b cum
                    with c
                    ""
                    hide mel1b
                "[mel] Handjob" if brothelroute2 == 1:
                    show melody2a e1 hj goth with d
                    ""
                    show melody2a e2 with d
                    ""
                    show melody2a hj2 cum e3 with c
                    ""
                    hide melody2a with d
                "[mel] Cowgirl and Reverse Cowgirl" if brothelroute2 == 1:
                    show melody2b c1 e1 with d
                    ""
                    show melody2b a1 e2 with d
                    ""
                    show melody2b c2 with d
                    ""
                    show melody2b e2 cum a2 with c
                    ""
                    show melody2b e3 with d
                    ""
                    hide melody2b
                    show melody2c e1 c1 
                    with d
                    ""
                    show melody2c a1 e2 with d
                    ""
                    show melody2c a2 cum with c
                    ""
                    show melody2c -a1 -a2 e1 with d
                    ""
                    hide melody2c
                "[rub] Bathrobe":
                    show ruby1a e1 with d
                    ""
                    show ruby1a e2 with d
                    "" 
                    show ruby1a e3 with d
                    ""
                    hide ruby1a with d
                "[rub] Couch Missionary":
                    show ruby1b e1 with d
                    ""
                    show ruby1b e2 v1 with d
                    ""
                    show ruby1b e3 v2 cum with c
                    ""
                    show ruby1b -v2 with d
                    ""
                    hide ruby1b with d
                "[rub] From Behind" if brothelroute2 == 1:
                    show rub2a e1a lingerie2 plug with d
                    ""
                    show rub2a e2a v1 with d
                    ""
                    show rub2a v2 e2a cum with c
                    ""
                    show rub2a -v2 e3 with d
                    ""
                    hide rub2a with d
                "[rub] Legs Up" if brothelroute2 == 1:
                    show rub2b e1 lingerie plug with d
                    ""
                    show rub2b v1 e2 with d
                    ""
                    show rub2b v2 cum with c
                    ""
                    show rub2b -v1 -v2 -a1 -a2 e3 -plug with d 
                    ""
                    show rub2b a1 e2 with d
                    ""
                    show rub2b a2 e2 with d
                    ""
                    show rub2b -v1 -v2 -a1 -a2 e3 with d 
                    ""
                    hide rub2b with d
                "Back":
                    jump gallerymenu
            jump gallerybrothelmenu
        "Farm" if farmroute1 == 1:
            menu galleryfarmmenu:
                "[blo] Butt from Below":
                    show blossom1a e1 with d
                    ""
                    show blossom1a e2 with d
                    ""
                    hide blossom1a with d
                "[blo] Butt from the Side":
                    show blossom1b with d
                    ""
                    show blossom1b hand with d
                    ""
                    show blossom1b -hand b1 with d
                    ""
                    show blossom1b b1 b2 cum with d
                    ""
                    show blossom1b -b1 -b2 cum with d
                    ""
                    hide blossom1b with d
                "[blo] Butt from a MSG":
                    show blomsg1 text with d
                    ""
                    show blomsg1 -text with d
                    ""
                    hide blomsg1 with d
                "[hon] Shower":
                    show honeycrisp1a with d
                    ""
                    hide honeycrisp1a with d
                "[hon] Thighjob":
                    show honeycrisp1b e1 with d
                    ""
                    show honeycrisp1b e2 tj1 with d
                    ""
                    show honeycrisp1b e3 tj2 with d
                    "" 
                    show honeycrisp1b e2 -tj2 cum with d
                    ""
                    hide honeycrisp1b with d
                "[hon] Butt Tease":
                    show honeycrisp1c with d
                    ""
                    hide honeycrisp1c with d
                "Back":
                    jump gallerymenu
            jump galleryfarmmenu
        "Bakery" if bakeryroute1 == 1:
            play sound2 error
            jump gallerymenu
        "Forest" if forestroute1 == 1:
            play sound2 error
            jump gallerymenu
        "Bar" if barroute1 == 1:
            play sound2 error
            jump gallerymenu
        "Castle" if castleroute1 == 1:
            play sound2 error
            jump gallerymenu
        "Extra" if dayevent >= 4:
            menu galleryextramenu:
                "[rosa] Missionary":
                    show rosa1a e1 with d
                    ""
                    show rosa1a e2 v1 with d
                    ""
                    show rosa1a e3 v2 cum with d
                    ""
                    show rosa1a e3 -v2 with d
                    ""
                    hide rosa1a with d
                "Back":
                    jump gallerymenu
            jump galleryextramenu
        "Back":
            $ gallery = 0
            $ textbox = 1
            $ phoneenabled = 1
            if worldmap == 1:
                call screen worldmap
            hide black with d
            call screen phone_screen    
            return
label socials:
    $ phoneenabled = 0
    if worldmap == 0:
        show screen phone_screen
    $ feedupdate = 0
    menu socialmenu:
        "Select a post to read more."
        "{color=#0077ff}{b}[rub]{/b}:{/color} Now Hiring! {color=#00ff62}(43 Likes){/color}"  if brothelroute1 == 1:
            rub "RUBY's is now looking to hire male talent! You can send me your resumes directly by messaging this account."
            "{i}Rather than messaging [rub], I should visit her instead.{/i}"
            jump socialmenu
        "{color=#0077ff}{b}[mox]{/b}:{/color} Thank you everyone! {color=#00ff62}(5,430 Likes){/color}":
            mox "Thank you to everyone that saw my biggest show ever at the Grand Theatre!"
            "{i}There are hundreds of comments. Wow, it looks like [mox] is doing extremely well for herself.{/i}"
            jump socialmenu
        "{color=#0077ff}{b}[pen]{/b}:{/color} Ice Cream {color=#00ff62}(1 Like){/color}":
            pen "Anyone else miss those cherry flavoured ice cream pots they used to sell at MacDairies?"
            mox "Oh yeah! Those were the bomb!"
            pen "Preach, sister."
            "{i}I could go for some ice cream right now.{/i}"
        "Back":
            $ phoneenabled = 1
            if worldmap == 1:
                call screen worldmap
            call screen phone_screen    
            return
    jump socialmenu
label shop1:
    $ phoneenabled = 0
    if worldmap == 0:
        show screen phone_screen
    if shoptut == 0:
        call shoptut from _call_shoptut
    menu shop1menu:
        "Money: [money]"
        "Unique Outfits":
            menu shop1menu2:
                "Money: [money]"
                "[mox] Punk for Facesitting - $100 - Owned: [punk]" if punk == 0 and moxiepunk == 0:
                    if money >= 100:
                        play sound2 shop2
                        $ money -= 100
                        $ punk = 1
                    else:
                        play sound2 error
                "[mox] Bunny Girl for Missionary - $100 - Owned: [bunnygirl]" if bunnygirl == 0 and moxiebunnygirl == 0:
                    if money >= 100:
                        play sound2 shop2
                        $ money -= 100
                        $ bunnygirl = 1
                    else:
                        play sound2 error
                "[lil] Goth for Handjob and Threesome - $200 - Owned: [goth]" if goth == 0:
                    if money >= 100:
                        play sound2 shop2
                        $ money -= 200
                        $ goth = 1
                    else:
                        play sound2 error
                "Back":
                    jump shop1menu
            jump shop1menu2
        "Self-Repairing Pantyhose and Fishnets - $125 - Owned: [pantyhose]" if pantyhose == 0:
            if money >= 125:
                play sound2 shop2
                $ money -= 20
                $ pantyhose = 1
            else:
                play sound2 error
        "Personalized Lingerie - $250 - Owned: [lingerie]" if lingerie == 0:
            if money >= 250:
                play sound2 shop2
                $ money -= 250
                $ lingerie = 1
            else:
                play sound2 error
        "Back":
            $ phoneenabled = 1
            if worldmap == 1:
                call screen worldmap
            call screen phone_screen    
            return
    jump shop1menu   
label shop2:
    $ phoneenabled = 0
    if worldmap == 0:
        show screen phone_screen
    if shoptut == 0:
        call shoptut from _call_shoptut_1
    menu shop2menu:
        "Money: [money]"
        "Performance Boosters - $100 - Increases Max Energy by 1" if maxenergy == 2:
            if money >= 100:
                play sound2 shop2
                $ money -= 100
                $ maxenergy += 1
                $ energy += 1
            else:
                play sound2 error
        "Secret Formula - $500 - Increases Max Energy by 1" if maxenergy == 3:
            if money >= 500:
                play sound2 shop2
                $ money -= 500
                $ maxenergy += 1
                $ energy += 1
            else:
                play sound2 error
        "Buttplugs for All - $125" if buttplug == 0:
            if money >= 125:
                play sound2 shop2
                $ money -= 125
                $ buttplug = 1
            else:
                play sound2 error
        "Bottomless Anal Lubrication - $300" if lubrication == 0:
            if money >= 300:
                play sound2 shop2
                $ money -= 300
                $ lubrication = 1 
            else:
                play sound2 error
        "Lewd Spellbook - $500" if lewdspellbook == 0:
            #the price of this should probably raise in a later update.
            if money >= 500:
                play sound2 shop2
                $ money -= 500
                $ lewdspellbook = 1
            else:
                play sound2 error
        "Insta-Futa Pills - $1500 - In Development. Futa planned, hard to implement for a lot of scenes tho":
            pass
        "'Milky' Potion - $1500 - In Development. Pregnancy/Breast Inflation/Lactation planned":
            pass
        "Back":
            $ phoneenabled = 1
            if worldmap == 1:
                call screen worldmap
            call screen phone_screen    
            return
    jump shop2menu
label music:
    $ phoneenabled = 0
    $ bigmenu = 1
    $ renpy.music.set_volume(0)
    $ renpy.music.set_volume(0, 0, "ambience1")
    if worldmap == 0:
        show screen phone_screen
    menu musicmenu:
        "Now playing: [gent1]\n{size=*0.6}Pro Tip: Long menus can be scrolled or dragged."
        "Back":
            jump musicmenuback
        "[blo]'s Theme - Discovery by Purrple Cat":
            play music2 blossomtheme 
            $ gent1 = "Discovery by Purrple Cat"
        "Casual 1 - Quiet Ocean by Peritune":
            play music2 casual1 
            $ gent1 = "Quiet Ocean by Peritune"
        "Casual 2 - Firmament Calm by Peritune":
            play music2 casual2
            $ gent1 = "Firnament Calm by Peritune"
        "City - Sparkle by Peritune":
            play music2 citytheme
            $ gent1 = "Sparkle by Peritune"
        "Club - delirium dreams by Mindvacy":
            play music2 clubtheme
            $ gent1 = "delirium dreams by Mindvacy"
        "Comical - Larry by Purgatory Garden":
            play music2 comical
            $ gent1 = "Larry by Purgatory Garden"
        "[hon]'s Theme - Meteorites by Purrple Cat":
            play music2 honeycrisptheme 
            $ gent1 = "Meteorites by Purrple Cat"
        "Intro - microcosm by Mindvacy":
            play music2 intro 
            $ gent1 = "microcosm by Mindvacy"
        "Lily's Theme - Aether by Purrple Cat":
            play music2 lilytheme 
            $ gent1 = "Aether by Purrple Cat"
        "Melody's Theme - lorncloudshit by Sewerslvt":
            play music2 melodytheme 
            $ gent1 = "lorncloudshit by Sewerslvt"
        "Moxie's Theme - Abstract Foilage by Artificial Music":
            play music2 moxietheme 
            $ gent1 = "Abstract Foilage by Artificial Music"
        "Penelope's Theme - Going With The Flow by Purrple Cat":
            play music2 penelopetheme 
            $ gent1 = "Going With The Flow by Purrple Cat"
        "Rainy Day - Cold & Rainy by Purrple Cat":
            play music2 rainytheme 
            $ gent1 = "Cold & Rainy by Purrple Cat"
        "Ruby's Theme - Toe Wizard by Sewerslvt":
            play music2 rubytheme 
            $ gent1 = "Toe Wizard by Sewerslvt"
        "Sad - hopelessness by Sewerslvt":
            play music2 sad 
            $ gent1 = "hopelessness by Sewerslvt"
        "Sex - Glowing Tides by Purrple Cat":
            play music2 sextheme 
            $ gent1 = "Glowing Tides by Purrple Cat"
        "Back":
            label musicmenuback:
                stop music2
            $ renpy.music.set_volume(1)
            $ renpy.music.set_volume(1, 0, "ambience1")
            $ phoneenabled = 1
            $ bigmenu = 0
            if worldmap == 1:
                call screen worldmap
            call screen phone_screen    
            return
    jump musicmenu
label cheats:
    $ phoneenabled = 0
    if worldmap == 0:
        show screen phone_screen
    menu cheatmenu:
        "+/- Money":
            $ gen1 = renpy.input("Enter an amount of monies to gain or lose. Current Monies: [money]", allow="-0123456789")
            $ money += int(gen1)
        "+/- Energy":
            $ gen1 = renpy.input("Enter an amount of energy to gain or lose. Current Energy: [energy]", allow="-0123456789")
            $ energy += int(gen1)
        "Change Names/Styles":
            menu:
                "You, [mc]":
                    $ mc = renpy.input("What is your name?")
                    if mc == "":
                        $ mc= "Anon"
                    $ mc = mc.strip()
                "[mox] Style [moxb]":
                    $ gen1 = 1
                    call screen characterchoice
                    $ moxb = gen2
                    menu:
                        "What was her name?"
                        "Default: Moxie":
                            $ moxie = "Moxie"
                        "Custom":
                            $ moxie = renpy.input("What was her name?")
                            if moxie == "":
                                $ moxie= "Moxie"
                            $ moxie = moxie.strip()
                "[pen] Style [penb]":
                    $ gen1 = 2
                    call screen characterchoice
                    $ penb = gen2
                    menu:
                        "What was her name?"
                        "Default: Penelope":
                            $ penelope = "Penelope"
                        "Alternate: Sundowner":
                            $ penelope = "Sundowner"
                        "Custom":
                            $ penelope = renpy.input("What was her name?")
                            if penelope == "":
                                $ penelope= "Penelope"
                            $ penelope = penelope.strip()
                "[hon] Style [honb]":
                    $ gen1 = 3
                    call screen characterchoice
                    $ honb = gen2
                    menu:
                        "What was her name?"
                        "Default: Honeycrisp":
                            $ honeycrisp = "Honeycrisp"
                        "Custom":
                            $ honeycrisp = renpy.input("What was her name?")
                            if honeycrisp == "":
                                $ honeycrisp= "Honeycrisp"
                            $ honeycrisp = honeycrisp.strip()
                "[rub] Style [rubb]":
                    $ gen1 = 4
                    call screen characterchoice
                    $ rubb = gen2
                    menu:
                        "What was her name?"
                        "Default: Ruby":
                            $ ruby = "Ruby"
                        "Custom":
                            $ ruby = renpy.input("What was her name?")
                            if ruby == "":
                                $ ruby= "Ruby"
                            $ ruby = ruby.strip()
                "[lil] Style [lilb]":
                    $ gen1 = 7
                    call screen characterchoice
                    $ lilb = gen2
                    menu:
                        "What was her name?"
                        "Default: Lily":
                            $ lily = "Lily"
                        "(Custom Name)":
                            $ lily = renpy.input("What was her name?")
                            if lily == "":
                                $ lily= "Lily"
                            $ lily = lily.strip()
                "[mel] Style [melb]":
                    $ gen1 = 11
                    call screen characterchoice
                    $ melb = gen2
                    menu:
                        "What was her name?"
                        "Default: Melody":
                            $ melody = "Melody"
                        "Custom":
                            $ melody = renpy.input("What was her name?")
                            if melody == "":
                                $ melody= "Melody"
                            $ melody = melody.strip()
                "[blo] Style [blob]":
                    $ gen1 = 12
                    call screen characterchoice
                    $ blob = gen2
                    menu:
                        "What was her name?"
                        "Default: Blossom":
                            $ blossom = "Blossom"
                        "Custom":
                            $ blossom = renpy.input("What was her name?")
                            if blossom == "":
                                $ blossom= "Blossom"
                            $ blossom = blossom.strip()
                "Back":
                    jump cheatmenu
        "Back":
            $ phoneenabled = 1
            if worldmap == 1:
                call screen worldmap
            call screen phone_screen    
    jump cheatmenu
label settings:
    $ phoneenabled = 0
    if worldmap == 0:
        show screen phone_screen
    menu settingsmenu:
        "Change Phone Background":
            menu phonebgmenu:
                "Default BG":
                    $ phonebg = 1
                "Under the Sea":
                    $ phonebg = 2
                "Ominous Moon":
                    $ phonebg = 3
                "Grand Journey":
                    $ phonebg = 4
                "Back":
                    jump settingsmenu
            jump phonebgmenu
        "Back":
            $ phoneenabled = 1
            if worldmap == 1:
                call screen worldmap
            call screen phone_screen  
    jump settingsmenu  
 

################################################################################
## Initialization
################################################################################

init offset = -1
label splashscreen:
    scene black
    pause 0.5
    show image "splash1" with dissolve
    pause 1.5
    show image "splash2" with dissolve
    pause 3.0
    return

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    color "#f00"
    outlines [ (2, "#000", 2, 2) ]
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    zorder 95
    style_prefix "say"
    window:
        id "window"
        if textbox == 2:
            background None
        if textbox == 3:
            yalign .1
            background None
        if textbox == 4:
            yalign .85
            background None
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what":
            size persistent.text_size
    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    zorder 105
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    modal True
    zorder 102
    style_prefix "choice"
    if bigmenu == 1:
        side "c":
            area (380, 25, 1850, 800)
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                side_yfill True
                vbox:
                    for i in items:
                        $ disabled = i.kwargs.get("disabled", False)
                        textbutton i.caption action i.action sensitive not disabled
    else:
        vbox:
            for i in items:
                $ disabled = i.kwargs.get("disabled", False)
                textbutton i.caption action i.action sensitive not disabled

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    activate_sound "click1.ogg"
style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    ## Ensure this appears on top of other screens.
    zorder 100
    if quick_menu and persistent.quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Settings") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos 91
        yalign 0.5

        spacing 50


        if main_menu:

            textbutton _("New Game") action Start()

        else:

            #textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Settings") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        #textbutton _("Credits") action ShowMenu("about")

        #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        #
        #    ## Help isn't necessary or relevant to mobile devices.
        #    textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu
image mainmenuwater1:
    "mainmenuwater1.png"
    alpha 1
    linear 0.1
    linear 1 alpha 0
    linear 0.1
    linear 1.1 alpha 1.0
    repeat
image mainmenuwater2:
    "mainmenuwater2.png"
    alpha 0
    linear 0.1
    linear 1.2 alpha 1
    linear 0.1
    linear 1.3 alpha 0
    repeat
label before_main_menu:
    play ambience1 ambiencenight
    play ambience2 river volume 0.5
    play ambience3 wind volume 0.5
screen main_menu():
    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background
    image "mainmenuwater1"
    image "mainmenuwater2"

    imagemap:
        ground "MainMenuUI.png"
        hover "MainMenuUIh.png"

        hotspot (1153, 975, 800, 150) action OpenURL("https://www.patreon.com/TwistedScarlett") hovered [ Play ("sound", "click1.ogg")]

        hotspot (129, 372, 329, 81) action Start() hovered [ Play ("sound", "click1.ogg")]

        hotspot (126, 455, 332, 77) action ShowMenu("load") hovered [ Play ("sound", "click1.ogg")]

        hotspot (105, 531, 365, 81) action ShowMenu("preferences") hovered [ Play ("sound", "click1.ogg")]

        hotspot (123, 610, 339, 91)action Quit(confirm=not main_menu) hovered [ Play ("sound", "click1.ogg")]

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    #use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action If(renpy.get_screen("save"), true=Show("savegameName", accept=FileSave(slot)), false=FileLoad(slot))


                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("%d %B - {#file_time}%H:%M"), empty=_("")):
                            style "slot_time_text"

                        if FileSaveName(slot):
                                $ fn = FileSaveName(slot)
                                if fn and ("-" in fn):
                                    $ y = fn.split("-")
                                text fn:
                                    style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5

## BadMustard's code Start (second section)
screen savegameName(accept=NullAction()):

    modal True
    add "black" alpha 0.8
    style_prefix "savegameName"

    frame:
        has vbox:
            xalign 0.5
            spacing 20

        label _("Save Name"):
            text_color gui.text_color
            xalign 0.5

        null height 10

        input size 40 color gui.hover_color default store.save_name changed Namer length 22 allow allowedChars:
            yalign 1.0
            xalign 0.5
            xysize (550, 40)

        textbutton _("{u}Save the Game{/u}"):
            xalign 0.5
            keysym ['K_RETURN', 'K_KP_ENTER']
            action [accept, (Hide("savegameName"))]

init python:
    import string
    def Namer(name):
        store.save_name = name

# Define characters that can be typed in. We allow:
# - Uppercase letters (In ascii_letters)
# - Lowercase letters (In ascii_letters)
# - Numbers 0 to 9 (In digits)
# - space, dash
define allowedChars = string.ascii_letters + string.digits + " -"
default persistent.saveName = True

style savegameName_frame:
    padding gui.confirm_frame_borders.padding
    xsize 650
    xalign 0.5
    yalign 0.5

style savegameName_frame:
    variant "touch"
    padding gui.confirm_frame_borders.padding
    xsize 650
    xalign 0.5
    yalign 0
    ypos 50
## BadMustard's code Stop (second section)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    zorder 95
    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    #textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
                vbox:
                    style_prefix "radio"
                    label _("Quick Menu")
                    textbutton _("Enabled") action SetField(persistent,"quick_menu", True)
                    textbutton _("Disabled") action SetField(persistent,"quick_menu", False)
                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
                            
            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("Text Size ([persistent.text_size]/45)")
                    bar value FieldValue(persistent, "text_size", offset=20, range=25, style="slider")
                    textbutton _("Set to default") action InvertSelected(SetVariable("persistent.text_size", gui.text_size))

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
