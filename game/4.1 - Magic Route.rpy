﻿label treehouse:
    hide screen worldmap
    show screen vnui
    play music lilytheme fadein 1
    scene bg library
    with d
    menu treehousemenu:
        "Visit [lil]":
            layeredimage lilybedroom:
                always:
                    "bg lilybedroom"
                if magicroute2 ==1:
                    "bg lilybedroomtidy"
            scene lilybedroom
            show night:
                alpha 0.75
                blend "multiply"
            show lil happy
            with d
            if magicroute1 == 0:
                lil "Good evening. I have your city pass somewhere around here."
            elif magicroute2 == 0:
                show lil blush coat with d
                lil "Mmhh... You're back..."
            else:
                lil "Good evening. It's nice to see you."
            menu lilmenu:
                "Where's [lil] 2.0?" if magicroute1 == 1 and magicroute2 == 0:
                    jump magic2
                "Get City Pass" if magicroute1 == 0:
                    jump magic1
                "Sex":
                    show lil horny with d
                    lil "Oh? What did you have in mind?"
                    menu lilsexmenu:
                        "Energy: [energy]"
                        "No Energy Left" if energy <= 0:
                            "I feel exhausted!"
                            jump lilmenu
                        "Buttjob" if energy > 0:
                            call lilbuttjob from _call_lilbuttjob
                            scene lilybedroom
                            show night:
                                alpha 0.75
                                blend "multiply"
                            show lil happy
                            call aftersex from _call_aftersex_1
                            with d
                            play ambience1 night
                            play music lilytheme
                        "Double Handjob" if energy > 0 and magicroute1 == 1:
                            call lildoublehandjob from _call_lildoublehandjob
                            scene lilybedroom
                            show night:
                                alpha 0.75
                                blend "multiply"
                            show lil happy
                            call aftersex from _call_aftersex_2
                            with d
                            play ambience1 night
                            play music lilytheme
                        "Selfcest Threesome" if energy > 0 and magicroute2 == 1:
                            call lilselfcestthreesome from _call_lilselfcestthreesome
                            scene lilybedroom
                            show night:
                                alpha 0.75
                                blend "multiply"
                            show lil happy
                            call aftersex from _call_aftersex_3
                            play ambience1 night
                            play music lilytheme
                            with d
                        "On-Side Sex Leg-Up" if energy > 0 and magicroute3 == 1:
                            call lilonside1 from _call_lilonside1
                            scene lilybedroom
                            show night:
                                alpha 0.75
                                blend "multiply"
                            show lil happy
                            call aftersex from _call_aftersex_4
                            play ambience1 night
                            play music lilytheme
                            with d
                        "On-Side Sex Leg-Down" if energy > 0 and magicroute3 == 1:
                            call lilonside2 from _call_lilonside2
                            scene lilybedroom
                            show night:
                                alpha 0.75
                                blend "multiply"
                            show lil happy
                            call aftersex from _call_aftersex_5
                            play ambience1 night
                            play music lilytheme
                            with d
                        "Back":
                            show lil happy with d
                            lil "Hum, okay."
                    jump lilmenu
                "Back":
                    scene bg library with d
                "Leave":
                    jump worldmap
        "Visit [pen]":
            play music penelopetheme fadein 1
            scene bg peneloperoom
            show night:
                alpha 0.5
                blend "multiply"
            show pen happy
            with d
            if magicroute2 == 1 and magicroute3 == 0:
                pen "Ah, there you are, [mc]! Are you taking me up on my offer?"
            else:
                pen "Hiya, [penmc]! Thanks for popping by!"
            menu penmenu:
                "Break out the Wine!" if magicroute2 == 1 and magicroute3 == 0:
                    jump magic3
                "Sex":
                    show pen horny with d
                    pen "Ohoho, this is what I've been waiting for!"
                    menu pensexmenu:
                        "Energy: [energy]"
                        "No Energy Left" if energy <= 0:
                            "I feel exhausted!"
                            jump penmenu
                        "Cowgirl" if energy > 0:
                            call pencowgirl from _call_pencowgirl
                            call aftersex from _call_aftersex_6
                        "Pet-Play Boobjob" if energy > 0 and magicroute1 == 1:
                            call penboobjob from _call_penboobjob
                            call aftersex from _call_aftersex_7
                        "Tied-Up From Behind" if energy > 0 and magicroute1 == 1:
                            call penfrombehind from _call_penfrombehind
                            call aftersex from _call_aftersex_8
                        "[mox] and [pen] Marathon" if energy > 0 and magicroute3 == 1:
                            call penmoxmarathon from _call_penmoxmarathon
                            call aftersex from _call_aftersex_9
                            scene bg peneloperoom
                            show night:
                                alpha 0.5
                                blend "multiply"
                            show pen happy
                            with d
                        "Back":
                            show pen happy with d
                            pen "Meh!"
                    jump penmenu
                "Toggle Collar":
                    if petplay == 1:
                        $ petplay = 0
                    else:
                        $ petplay = 1
                    jump penmenu
                "Change how [pen] addresses you" if magicroute3 == 1:
                    menu:
                        "You can call me…"
                        "Master":
                            $ penmc = "Master"
                        "[mc]":
                            $ penmc = "{}".format(mc)
                        "Custom":
                            $ penmc = renpy.input("What do you want [pen] to call you?")
                            if penmc == "":
                                $ penmc= "{}".format(mc)
                            $ penmc = penmc.strip()
                    jump penmenu
                "Back":
                    play music lilytheme fadein 1
                    scene bg library with d
                "Leave":
                    jump worldmap
        "Replay Events":
            menu:
                "While replaying, you can return at any time using the phone."
                "Treehouse Visit 1" if magicroute1 == 1:
                    $ replay = 1
                    show screen vnui
                    scene bg lilybedroom 
                    show night:
                        alpha 0.75
                        blend "multiply"
                    call magic1 from _call_magic1
                    $ replay = 0 
                    jump treehouse
                "Treehouse Visit 2"  if magicroute2 == 1:
                    $ replay = 1
                    show screen vnui
                    scene bg lilybedroom 
                    show night:
                        alpha 0.75
                        blend "multiply"
                    call magic2 from _call_magic2
                    $ replay = 0 
                    jump treehouse
                "Treehouse Visit 3"  if magicroute3 == 1:
                    $ replay = 1
                    show screen vnui
                    play ambience1 night
                    scene bg city2 with d
                    call magic3 from _call_magic3
                    $ replay = 0 
                    jump treehouse
                "Back":
                    pass
        "Leave":
            jump worldmap
    jump treehousemenu

label magic1:
    show black with d
    show screen vnui
    "'Everything that irritates us about others can lead us to an understanding of ourselves.' - Carl Jung"
    hide black 
    show lil awkward blush
    with d
    "[lil] appears a bit flustered, her cheeks tinged with a faint blush as she retrieves my city pass from a cluttered desk."
    lil "Here's your city pass..."
    mc "Great, thanks! This is actually the second time you've gotten me a pass."
    show lil happy -blush with d
    lil "I thought so. How's your search going?"
    menu m1m1:
        "I’ve contacted [rub]." if brothelroute1 == 1:
            mc "I've successfully reached out to [rub]. Has she messaged you yet?"
            show lil neutral with d
            lil "Yes, she has. I was pretty shocked to learn that one of the supposed virtues is running a brothel, but apparently, it's a brothel of intellectual curiosities. I'm curious, but I don't think I'd want to be seen anywhere near there." 
        "I’ve contacted [hon]" if farmroute1 == 1:
            mc "I’ve contacted [hon] and given her your number."
            show lil happy with d
            lil "Oh, the farmer! At first, I was unsure about having a farmer on our team, but then I considered that if she owns the farm, she probably has some business acumen."
            mc "You’re a bit judgmental, aren’t you?"
            show lil bashful with d
            lil "I just find it strange that godlike power would be given to a humble farmer. Maybe that's the point." 
        "I’ve contacted [but]" if forestroute1 == 1:
            if forestroute2 == 0:
                mc "I met with [but], but she's not ready to join us yet. Just give me a bit more time to help her out."
            else:
                mc "I met [but], helped her out, and she’s now able to join us."
            show lil neutral with d
            lil "I don’t know anything about her. I’ll trust your judgment on this one."
        "I’ve befriended [rik]" if barroute1 == 1:
            mc "She definitely seems interested in our plan."
            show lil happy with d
            lil "I'm impressed you managed to befriend a celebrity like that. Did your prior knowledge help?"
            mc "Only in finding her. [rik] in this universe is a completely different person circumstantially." 
        "I think I’ve found [cre]?" if bakeryroute1 == 1:
            mc "There's some weird stuff happening at that bakery, but I can confirm [cre] will be joining us."
            show lil raised with d
            lil "Weird? What’s going on?"
            mc "There’s a… uh… It's something even less believable than me being from another universe. You'll have to see it for yourself."
            show lil happy with d
            lil "Oh…? Now I'm really intrigued! I'll contact her as soon as I can."
        "I haven’t found anyone yet (Continue)" if brothelroute1 == 0 and farmroute1 == 0 and forestroute1 == 0 and barroute1 == 0 and bakeryroute1 == 0:
            jump m1m1p
        "That’s everyone I’ve contacted (Continue)" if brothelroute1 == 1 or farmroute1 == 1 or forestroute1 == 1 or barroute1 == 1 or bakeryroute1 == 1:
            jump m1m1p
        "Everyone is ready! (Continue)" if brothelroute1 == 1 and farmroute1 == 1 and forestroute2 == 1 and barroute1 == 1 and bakeryroute1 == 1:
            lil "Perfect. I’ll arrange a time for all of us to meet the Queen as soon as I can."
            jump m1m1p
    jump m1m1
    label m1m1p:
        show lil bashful blush with d
        lil "{i}Sigh{/i} I also have your DNA results on my laptop."
    "[lil] blushes and opens her laptop, quickly navigating to a database that shows my DNA compared to tens of thousands of other citizens."
    show lil happy with d
    lil "Zero matches, not even a close match that could be an alternative species version of you."
    mc "As expected, but it was important to check. This is quite different from how you did it last time. Before, you relied solely on magic."
    show lil raised -blush with d
    lil "Based on our conversations and some discussions I've had with [pen], it seems your world is quite rudimentary compared to ours."
    mc "Well, a little. I wouldn't exactly call it medieval; we still had phones and computers. But the technology was downplayed to keep things cozy and rustic, evoking an idyllic village life blending seamlessly with the countryside."
    show lil angry with d
    stop music fadeout 5
    stop ambience1 fadeout 30
    lil "Ugh, that sounds terrible! The synergy between magic and technology has allowed both to reach new heights, and I’ll argue with any purist who says otherwise."
    "I wasn't expecting her to react like that."
    mc "You seem really passionate about this. But now that I think of it, I don't know much about you in this world."
    show lil smug with d
    lil "You're actually interested in me? I'm happy to answer any questions you have."
    mc "{i}Any{/i} questions?"
    show lil bashful with d
    lil "U-Uhm, yeah… I think so?"
    play music casual1
    menu m1m2:
        "What do you study?":
            show lil wink with d
            lil "Where do I even begin? I'm on the cutting edge of DNA and evolution, particularly focusing on sexually compatible creatures."
            lil "It's one thing to know that the offspring of two interspecies partners will share the mother's species, but it's entirely different to understand why that happens and what traits, if any, are inherited from the father."
            lil "Is a stallion born from a dragon and a mare really just a regular stallion? You can't tell me there's nothing special about that, and it's shocking how little research has been done on this topic. I may even be able to discover the origin of unicorns, pegasi, and earth ponies."
            mc "Is that why you've been so open and interested in me?"
            show lil laughing with d
            lil "Absolutely! You're another species for me to study, and you actually talk to me! {i}Sigh{/i} Do you know how hard it is to get people to sign up for even basic questionnaires?" 
        "What does it mean to be the Queen’s student?":
            show lil smug with d
            lil "It means I was recognized for my intelligence and potential early on. By consistently meeting those expectations, I now have access to resources and influence to pursue my dreams."
            lil "Naturally, it also means receiving special lessons and guidance from the Queen herself. I’m capable of managing many of her personal and political duties if needed."
            show lil laughing with d
            lil "However, she hasn’t requested my assistance in a few years, so I’ve been focusing on my own interests. As long as I’m being productive, she’s content to meet with me once a season."
            menu:
                "And what is she like?":
                    show lil happy with d
                    lil "When she’s not working, she’s the most graceful and loving goddess you could imagine."
                    show lil neutral with d
                    lil "When she’s working, she’s a ruthless leader who will do whatever it takes to achieve her goals."
                    lil "Strangely, knowing how kind and loving she can be makes her other side even more frightening."
                "I had another question":
                    pass
        "Do you have any fetishes?":
            show lil shocked blush with d
            lil "W-What?! What kind of ridiculous question is that? Why would I care about such things?"
            mc "You did say any question was fair game! Surely, you must have some specific preferences in sexual contexts."
            show lil awkward with d
            lil "I’m a pure lady. Just because I had that one ‘slip up’ last time we met, doesn’t mean I’d… {i}Clears throat{/i}"
            lil "My current work involves studying biology, fertilization, and pregnancy, it does cross my mind occasionally… In that sense… I’m a bit curious for work reasons, but it’s a waste of time!"
            mc "Interesting~"
            show lil neutral -blush with d
            lil "Hmph!"
        "How often do you masturbate?":
            show lil shocked blush with d
            lil "Ugh! I bet you already know, considering how close you were to my other self. You even knew where my dildo was. I’m embarrassed to even own one; no one was supposed to know."
            mc "It’s normal and healthy. We all do it. If you give me your answer, I’ll give you mine."
            show lil awkward with d
            lil "Hmm… Fine, just so I can hear your answer… I masturbate twice a day, once in the morning and once in the evening… and sometimes during the day too."
            show lil smug with d
            lil "Now you have to answer!"
            mc "Honestly, I don’t remember the last time I masturbated outside of doing it right here with you. I get so much action that I don’t need to do it anymore."
            show lil angry with d
            lil "Ew, that’s gross!"
            mc "Eh?! You’d prefer it if I masturbated more?"
            show lil bashful -blush with d
            lil "That’s not what I meant!"
        "What’s your relationship with [pen]?":
            show lil happy with d
            lil "We were lab partners in college, and she kind of ‘adopted’ me as a close friend."
            mc "'Adopted' is certainly a word choice."
            show lil bashful with d
            lil "Well, I don't really make friends, they make me. At first, I wasn’t fond of [pen], especially with that silly hair, but she eventually won me over. We’ve been very close ever since."
            lil "We became roommates in our final year, and when I decided to move here, it made sense to invite her along. I admit, I don’t leave my part of the tree much, so we don’t chat as often as we used to." 
        "What’s your relationship with [mox]?":
            show lil raised with d
            lil "A clown who mocks real magic! I'm here, researching critical aspects of magic to advance society, and she's impressive for making a rabbit disappear in a hat?"
            lil "What kind of nonsense is that? I could do that! I've always said this city has too many pegasi and earth ponies because no unicorn would be impressed by such a farce."
            mc "Isn't it her performance and theatrics that make the magic show captivating?"
            show lil awkward with d
            lil "Tsk, I don't care much for charisma. I'm interested in the mechanics!"
            mc "You seem like the type to focus so much on trying to figure out the trick that you miss the show."
            show lil shocked with d
            lil "But that’s the fun part!"
        "(Continue)":
            jump m1m2p
    jump m1m2
    label m1m2p:
        show lil bashful blush with d
        lil "Well... Enough about me, I wanted to talk about something you did."
        lil "I heard you, [pen] and [mox] going at it like rabbits the last time you were here."
    lil "You’re not seriously planning to do that with every girl you meet, are you?"
    menu:
        "That’s the best part!":
            show lil awkward with d
            lil "B-But, that’s so…"
        "Perhaps…":
            show lil shocked with d
            lil "You’re not even sure?!"
        "I’ll pick and choose.":
            show lil raised with d
            lil "What’s that supposed to mean?"
        "You’re misunderstanding, we didn’t do anything." if moxpen2 == 0:
            show lil neutral with d
            lil "You didn’t? Maybe I was just hearing things…"
            mc "Maybe you were hearing what you wanted to hear?"
    show lil bashful with d
    lil "Ugh, it’s just… The one time a man comes into my life and displays even a modicum of interest, he also has everyone else vying for him?"
    mc "Isn’t that how your society has to work? There are three times as many women as men."
    show lil angry with d
    lil "I know that! For goodness’ sake, I’ve studied the biology behind it. But that doesn’t mean I can’t be frustrated or jealous when other girls take you away…"
    lil "I’d be an excellent girlfriend! For one: I’m pretty cute. Two: I'm extremely smart! Thirdly, I can do some amazing things that you couldn’t even imagine!"
    "She’s much more closed-minded than her counterpart. Instead of valuing the foundations of friendship and sharing, she’s quite egotistical and selfish. But…"
    mc "We can still make it work. Tell me about those amazing things."
    show lil bashful blush with d
    lil "Well, uh… I can perform tricks that [mox] could never dream of!"
    stop music fadeout 10
    show lil laughing with d
    lil "In fact, I just had a great idea! I won’t dignify myself to performing sexual actions for your affection; I’m too good for that. But what if I summoned a familiar to assist us?"
    mc "Go on…"
    show lil smug with d
    lil "It won’t be your ordinary familiar either! It’ll be a perfect copy of me, lasting as long as I want. That’s how powerful my magic is."
    mc "And what’s your end goal for this experiment?"
    "The usage of the word experiment causes her ears to twitch eagerly."
    show lil happy with d
    lil "I’ll let you indulge your little sexual fantasies and even document your behavior as an unknown species. All without lifting a finger. I’m a damn genius."
    play sound2 magic1
    with c
    "Before I can reply, her horn is already glowing with magic. She skillfully channels her arcane abilities, weaving intricate threads of magic into the air." 
    scene bg lilybedroom
    show night:
        alpha 0.75
        blend "multiply"
    show lil2 happy at flip:
        xalign 0.2 
    with d
    "With a flicker of concentration, she conjures a perfect replica of herself. Every detail, from the mane to the feet, is meticulously mirrored, standing beside her as if born from her very essence. The only difference is the ethereal glow and eyes, radiating pure magic."
    "The clone stepped forward with an exuberant smile, her eyes twinkling with a familiar yet unsettling glint."
    play music comical fadein 2
    show lil2 laughing with d
    $ lil2 = "{} 2.0".format(lil)
    lil2 "Hey there! Wow, this is so cool! I’ve always wanted to see myself from the outside. Guess you could call me ‘[lil] 2.0’! Ready to rock and roll!"
    mc "I’ve literally been cloned before, and this still feels uncanny."
    show lil neutral with d:
        xalign 0.8
    "The original [lil] blinked, taken aback by the clone’s enthusiastic demeanor."
    lil "That’s… definitely not something I would say, is it? I mean… [lil] 2.0? That’s not exactly…"
    show lil2 smug with d
    lil2 "Oh, lighten up, me! We’re here to have fun, right? That’s the entire reason you summoned me." 
    show lil shocked blush with d
    lil "We? No, no, no. I’m just here to watch you two go at it like animals."
    show lil2 wink with d
    lil2 "Humph! You need to loosen up. Life’s not all about books and spells, you know!"
    show lil neutral with d
    "[lil] exchanged a bewildered glance with me, and I could only shrug in response."
    show lil raised -blush with d
    lil "I believe this situation requires extra special examination… [mc], can you do the honors?"
    mc "Me? What am I supposed to be doing?"
    show lil2 satisfied blush with d
    lil2 "Oh come on, cutie. Isn’t it obvious? She wants you to do me~"
    layeredimage lil2a:
        always:
            "lily2abase [lilb]"
        group lily1:
            attribute lily1:
                "lily2alily [lilb]"
        group goth:
            attribute goth:
                "lily2agoth"
        group eyes1:
            attribute l2e1:
                "lily2ae 1"
            attribute l2e2:
                "lily2ae 2"
            attribute l2e3:
                "lily2ae 3"
        group eyes2:
            attribute l1e1:
                "lily2alilye1 [lilb]"
            attribute l1e2:
                "lily2alilye2 [lilb]"
        group hj:
            attribute hj1:
                "lily2ahj"
            attribute hj2:
                "lily2ahj2"
        group cum:
            attribute cum:
                "lily2acum"
        group cum2:
            attribute hj1cum:
                "lily2ahjcum"
            attribute hj2cum:
                "lily2ahj2cum"
        group milk:
            attribute milk:
                "lily2amilk"
    play music sextheme 
    play moans1 moansmisc2 fadein 5
    stop ambience1 fadeout 10
    scene lil2a l2e1 
    call camerabreath from _call_camerabreath_29
    $ textbox = 2
    with d
    "[lil2] kneels before my crotch, and with large, adorable eyes looks up at me patiently as if waiting for my cock."
    menu:
        "I’m ready to rock and roll!":
            label rockandroll:
                $ lily2 = 1
                show lil2a l2e1 with d
                lil2 "Fantastic! Say, why don’t I help you with that? I regret not lending you a proper hand last time."
            show lil2a hj1 with d
            "[lil2] reached out and wrapped her hand around my cock. The tingling sensation from her touch made me hard within seconds."
            lil "H-Hey, don’t pretend you were me from back then! You’re way too… enthusiastic about this!"
            show lil2a l2e3 with d
            lil2 "Sounds like someone needs to be a little more honest with themselves. What do you think, [mc]?"
            play ambience1 handjob
            with hpunch
            "She began to stroke my throbbing member vigorously with one hand, her hips swaying rhythmically with each powerful motion, and her cute chest rising with each breath."
            mc "If this is how you really feel [lil], then damn! This is hot."
            lil "I… N-Not a chance!"
            show lil2a l2e2 with d
            lil2 "Mmm… You feel good in my hand."
            with hpunch
            "She purred before resuming her relentless strokes."
            "The real [lil] watched from the sidelines, her heart racing and cheeks flushing a deep crimson. She couldn’t even focus on writing anything down right now, not when she found herself both aroused and embarrassed by her other self’s brazen actions."
            "Her own marehood tingled with unfulfilled desire as she watched her clone receive and give it so eagerly and openly. The scent and sight made it difficult for her to ignore the building heat in her loins."
            mc "Ooohhh, you’re getting good at this! You’ve already figured out the best spot to rub."
            lil "L-Like fuck she has! There’s no way!"
            show lil2a l2e3 with d
            lil2 "It’s simple, my dear! The glans are too sensitive to touch directly, so I use the friction of the foreskin to glide against it, particularly around the crown."
            lil "Uwaaahhhhhhh, what are you even talking about?!"
            "I groaned in pleasure under the skilled ministrations of the clone. My cock throbbing as precum drips from the tip."
            lil2 "You want to cum, don’t you? Cover my face in your hot seed? Mmmhhh…"
            "She purred seductively before swiftly increasing the pace of her strokes."
            lil "Alright – Enough!"
            show lil2a lily1 l1e1 with d
            "[lil] could no longer idly stand by, trembling slightly; she crouched next to her and made her effort known."
            "She tentatively reached out towards my cock, her fingers barely touching the thick shaft. Her touch was soft, lacking her counterpart’s assertiveness. Eventually, she leaned back and rubbed her breasts together as seductively as she knew how."
            show lil2a l2e2 with d
            lil2 "I knew you had it in you. After all, you’re me~"
            "Encouraged by her hesitant participation, the clone glanced back with a triumphant smirk before returning her attention to me. She leaned closer still, her hot breath grazing against my tip."
            show lil2a l2e3 with d
            lil2 "That’s it… Let me help you cum for both of us."
            "I moaned in ecstasy as I felt myself on the brink of orgasm. My shaft stiffened under the assault of her eager hands, and prepared to unload."
            play sound2 cum
            show lil2a l1e2 l2e2 cum hj1cum with c
            play sound2 cum
            with c
            "With a roar of pleasure, my tip erupted fiercely. My hot seed spurted forth like a geyser, splattering both the mares’ faces and breasts."
            play sound2 cum
            show lil2a l2e1 with c
            play sound2 cum
            with c
            lil2 "Ooohhh yes… It feels just as good as last time, doesn’t it?"
            lil "Mmhhh… It does feel… pretty good…"
            stop ambience1
            play sound2 equip
            scene black with d
            "Before [lil] could fully process her feelings, she felt her clone’s soft lips pressing against hers in a passionate kiss."
            layeredimage lil2b:
                always:
                    "lily2b [lilb]"
                group lingerie:
                    attribute lingerie:
                        "lily2blingerie"
                group cum:
                    attribute cum1:
                        "lily2bcreampie"
                    attribute cum2:
                        "lily2bcum"
                group eyes:
                    attribute e1:
                        "lily2be1 [lilb]"
                    attribute e2:
                        "lily2be2"
                group milk:
                    attribute milk:
                        "lily2bmilk"
                group sex:
                    attribute sex:
                        "lily2bsex"
                group sex2:
                    attribute sex2:
                        "lily2bcreampie"
            # zoomed in on lily2b, no pussies visible yet
            show bg black:
                xpos 500
            show lil2b e1 
            camera:
                xpos 400 zpos -500 ypos 100
            play moans2 moansmisc3
            with d
            "The kiss deepened quickly, tongues dancing erotically as their bodies fell onto the bed together. The room seemed to spin around me as I caught my breath, my cock still throbbing from its intense release."
            lil "Aaahhh… What’s the meaning of this?"
            lil2 "Don’t play me for a fool, me… I know exactly what you want and exactly how you like it…"
            lil2 "Now, why don’t you spread your legs and put on a good show for [mc]? I bet he’d like that a lot."
            lil "B-But… My pussy…" 
            lil2 "Remember how much you loved showing your pussy off last time? It turned us on so much~"
            camera:
                linear 5 zpos -12 ypos -2 xpos 0
                block:
                    linear 2.4 ypos 5
                    linear 0.8 ypos 5
                    linear 1.5 ypos -2
                    linear 0.8 ypos -2
                    repeat
            "Her legs gently opened, revealing her glorious pussy to me. That, combined with her clone’s ass, which was purposely raised to show off, the sight was almost too much for my overstimulated brain to process."
            "[lil2] began kissing and licking [lil] clean; in a shocking amount of time, the girls went from being drenched in my seed to merely damp. Eventually, [lil2] ended up at her lovely breasts, sucking and teasing her nipples."
            lil2 "Mmhh… Like what you see, [mc]? Please feel free to touch yourself while you watch."
            "I approached closer; I couldn’t help but reach out and gently squeeze [lil]’s plump ass cheeks, feeling them jiggle slightly underneath my touch. She moaned slightly but didn’t reprimand me – if anything, her body language encouraged me further." 
            mc "You two look stunning together."
            "I kneeled right behind them, getting a perfect view of their pussies as I began to rub my cock."
            "[lil] moaned, surprised by how much she was enjoying this moment. She wrapped her slender legs around my waist, encouraging me closer while rocking her hips." 
            "The clone eyed me intently as she took the other of [lil]'s firm nipples into her lips. Her warm, long pony tongue flashed across the sensitive bud, eliciting a gasp from deep within [lil]."
            "Meanwhile, [lil]'s gaze shifted downward to watch as my big cock jerked enticingly between her legs. The thought of me spraying my cum over her was exhilarating, and she wanted more."
            show handjob at flip with d:
                xalign 0.05 yalign 0.9
            "She reached over, more confidentially wrapping her slender fingers around my shaft. It throbbed responsively under her touch."
            "Encouraged by the way her clone moaned into her breast, she began to stroke me slowly at first, but picked up speed as the passionate encounter intensified. "
            "[lil2] lifted herself up from between [lil]’s chest long enough to look down at us both with lust-filled eyes."
            lil2 "I want you to cum all over us." 
            show lil2b e2 with d
            "She panted breathlessly before leaning down again, capturing [lil]’s lips in a passionate kiss, while using her free hand to stimulate her own sensitive clit rhythmically."
            "[lil] kept stroking my member just inches from her pussy, her hips grinding as though she were pleading for it."
            show lil2b e1 with d
            lil2 "Hold on, don’t cum quite yet. I have an even better idea~"
            layeredimage lil2c:
                always:
                    "lily2cb [lilb]"
                group goth:
                    attribute goth:
                        "lily2cb goth" 
                group gotheyes:
                    attribute g1:
                        "lily2cgoth 1" 
                    attribute g2:
                        "lily2cgoth 2" 
                    attribute g3:
                        "lily2cgoth 3" 
                group legwear:
                    attribute l1:
                        "lily2clingerie"
                    attribute f1:
                        "lily2cfishnets 1"
                    attribute f2:
                        "lily2cfishnets 2"
                group eyes:
                    attribute e1:
                        "lily2ce1 [lilb]"
                    attribute e2a:
                        "lily2ce2 [lilb]"
                    attribute e2b:
                        "lily2ce2b"
                    attribute e2c:
                        "lily2ce2c"
                    attribute e3:
                        "lily2ce3 [lilb]"
                group cum1:
                    attribute cum1:
                        "lily2ccum"
                group cum1:
                    attribute cum2:
                        "lily2ccum2"
                group sex:
                    attribute v1a:
                        "lily2cv1a"
                    attribute v2a:
                        "lily2cv2a"
                    attribute v1b:
                        "lily2cv1b"
                    attribute v2b:
                        "lily2cv2b"
                group plug:
                    attribute plug:
                        "lily2cplug" 
            show lil2c e2b with dissolve
            "[lil] laid on her back, eyes closed tightly, heart racing like a runaway train as her body trembled with anticipation."
            lil2 "I want you to slide it inside, stud~ Take my virginity!"
            lil "(It’s finally going to happen, isn’t it? This is it!)"
            mc "You don’t have to ask twice! But, oh, what about her?"
            "Fear and excitement coursed through her veins as she felt her clone shift on top of her."
            lil "It’s okay! You don’t need my permission."
            lil2 "Hehe, I haven’t been this horny my entire life."
            "I moved in behind [lil2], and angled my cock at her identical virgin pussy, her folds already parting as my tip pressed in slightly." 
            lil2 "That’s right! Nnghhh, slide that cock right inside me!"
            lil "Wait… Inside… {b}you{/b}?"
            play sound2 cum
            show lil2c v1a e2a with d
            play ambience1 sex 
            play moans1 moansmisc4 
            camera:
                linear 0.2 zpos -17 ypos -2 xpos 0
                block:
                    linear 0.1
                    linear 0.3 ypos 8
                    linear 0.1
                    linear 0.2 ypos -8
                    repeat
            "Without another word, I plunged myself deep inside the clone’s tight entrance, groaning deeply as I tore through her folds and took her virginity." 
            "The sound of her resulting, impassioned moan, echoed through the room, reverberating through both of us, and it was sublime."
            "The clone’s body arched upwards, her back curving beautifully as she let out a high-pitched whine of pleasure mixed with pain."
            "[lil]’s eyes flew open at the sight before her – the sight of me pounding my cock into her clone’s tight pussy – she felt herself growing wetter by the second." 
            "She bit down harder on her lip, trying desperately not to whimper in need as she felt every powerful thrust indirectly pressed against her by her clone."
            "It was torture – exquisite torture – and she couldn’t tear her eyes away from the display unfolding before her." 
            mc "Ooohhh, your pussy is so tight, [lil]!"
            lil2 "Mmphhhh, this is the best feeling ever!"
            "The clone moaned my name over and over again, fingers digging into the sheets beside [lil] as she met each brutal thrust with equal ferocity – her body moving in perfect sync with mine."
            "It was beautiful chaos – an erotic dance purely fueled by lust and desire - and [lil] felt herself slipping further into the depths of depravity with each passing moment."
            "She couldn’t take it anymore – she couldn’t just lie there and watch them – and without even thinking about it, she reached down between her legs, finding her own wet folds deeply slick with need." 
            "Her fingers brushed against her clit, teasingly circling around the sensitive nub before finally plunging inside her tight entrance."
            "She gasped at the sensation – it wasn’t nearly enough – but it helped quell some of the burning desire threatening to consume her entirely."
            "As if sensing her need, the clone glanced over at her – eyes half-lidded with pleasure – and gave her a sultry smile, before returning her attention back to me."
            lil2 "Ooohhh, [lil]… I want you to watch… I want you to see how good he makes me feel."
            "And feel good, she did – her body arching off the bed as wave after wave of pleasure coursed through her – her walls clenching tightly around me as she approached orgasm." 
            "The sight of them – her clone experiencing such raw ecstasy while she lay there, helplessly aroused but still untouched—was almost too much for [lil] to bear."
            "Finally, with a shattering cry that echoed through the room like thunder rolling across plains, the clone’s body tightened one last time as it had a full-body orgasm."
            play sound2 cum
            show lil2c v2a with c
            "My cock followed shortly after, erupting deep inside her for one last time, cum shooting deep into her pussy and womb."
            play sound2 cum
            show fertilization at flip:
                alpha 0.8
                xalign 0.01 yalign 0.9
            with c
            lil2 "Uooohhh, that’s right! Fill up my womb with your hot cum!"
            lil2 "Nnghhh! Aaahhhh, so much! Get me pregnant, mmmhhhh!"
            play sound2 cum
            show lil2c e3 cum2 -v2a 
            call camerareset from _call_camerareset_14 
            call stopbgs from _call_stopbgs_34
            stop music fadeout 10
            hide fertilization
            with c
            "Load after load filled her up, until finally, I pulled out and covered the two of them, hot cum dripping down fluffy thighs."
            "Once we’d finally finished, she relaxed back onto the mattress, spent and satisfied."
            "Her eyes flickered closed for a moment before reopening again and locking onto [lil]’s own hazy gaze." 
            play music lilytheme fadein 25
            lil2 "This is what you wanted; don’t deny yourself."
            mc "Your turn, [lil]?"
            show lil2c e1 with d
            lil "I… I…"
            "[lil] stared back at her clone, confusion warring with desire in her eyes – unsure of what she should do next."
            "Part of her wanted me to turn my attention towards her, to take her virginity as I had taken the clones. But another part of her – the rational part – told her she should push these desires away – that this wasn’t right."
            "However, as her eyes turned to mine and we shared an intense stare down, she realized something profound: she didn’t care about right or wrong anymore. All she cared about was experiencing the same intense pleasure her cloned had just found – even if she had cuckolded herself in the process."
            "But…"
            lil "N-Not right now… {i}Pant, pant{/i} I can tell your pecker is clearly exhausted."
            "I look down, and she’s right, my cock will be out of commission for a while after those back-to-back orgasms."
            scene bg lilybedroom
            show night:
                alpha 0.6
                blend "multiply"
            show lil bashful blush:
                xalign 0.8
            show lil2 laughing blush cum at flip:
                xalign 0.2
            $ textbox = 1
            with d
            lil "What was all that about ‘get me pregnant, get me pregnant’! [lil2]?"
            lil2 "I was just being honest with myself."
            "The clone cradles her belly and giggles."
            show lil2 satisfied with d
            lil2 "Getting filled up like that, knowing I might get pregnant from this hot stud’s virile seed… Mmpphhh…"
            show lil awkward with d
            lil "W-What are you talking about? I don’t want that…"
            mc "Surely you relate to that, [lil]? I mean she’s you."
            show lil shocked -blush with d
            lil "U-Uhm, n-no! Not at all!" 
        "No way, you two need to figure this out between yourselves.":
            show lil2a l2e2
            lil2 "What’s there to figure out? I think the situation speaks for itself, don’t you?"
            lil "I’m really curious about [lil2]’s behavior right now. Please, [mc]?"
            menu:
                "Alright, fine.":
                    jump rockandroll
                "This is too weird, even for me.": 
                    lil2 "Awh! But I wanted your dick!"
                    scene bg lilybedroom
                    show night:
                        alpha 0.6
                        blend "multiply"
                    show lil2 sad at flip:
                        xalign 0.2
                    show lil awkward:
                        xalign 0.8
                    call camerareset2 from _call_camerareset2_18
                    with d
    lil "There’s clearly something wrong with this clone, correct?"
    mc "A lot more open and outgoing, I wouldn’t necessarily say it’s ‘wrong’, but she’s not identical to you."
    show lil2 happy -blush with d
    lil2 "You both make a good point. It seems I didn’t inherit all the intended traits perfectly. This requires further investigation, wouldn’t you agree, me?"
    show lil neutral with d
    lil "Absolutely. My current hypothesis is that your mind was influenced by my reasoning or mental state during your creation."
    show lil2 laughing with d
    lil2 "That's a great idea... If you created me for horny purposes, in a self-fulfilling way, I cater towards my purpose?"
    show lil happy with d
    lil "My thoughts exactly! Goodness, I never imagined how amazing it would be to have a discussion like this with myself. We definitely need to conduct more tests!"
    mc "Uh, you two are geeking me out a bit. Do you mind if I go visit [pen]?"
    show lil wink with d
    lil "Of course! Thank you so much for coming today, [mc]. I’m looking forward to catching up with you again."
    show lil2 smug blush with d
    lil2 "And me too, hopefully!"
    stop music
    scene bg black with d
    "'And the day came when the risk to remain tight in a bud was more painful than the risk it took to blossom.' - Anaïs Nin"
    play music penelopetheme
    show bg peneloperoom
    show night:
        alpha 0.5
        blend "multiply"
    with d
    "… On the other side of the treehouse, in [pen]’s room."
    show pen happy with d
    pen "I’m impressed by how quickly you’ve settled here and started making big moves."
    pen "It would probably take me a week to wrap my head around all of this, especially in such a grim urban setting."
    mc "This isn’t the first time something like this has happened, and you girls have been incredibly accommodating. I couldn’t be here or do this without your help."
    show pen laughing blush with d
    pen "Heh, I’m not great with compliments; you’ll make me blush."
    show pen happy -blush with d
    pen "I’ve been pondering your situation a bit more, and there’s one point that’s really sticking with me."
    mc "What’s on your mind, [pen]?"
    show pen awkward with d
    pen "It’s just… I find it incredibly unlikely for you to end up in this particular universe. I mean… what are the odds? Who gets thrown into another universe that just happens to have the exact same people? There could be an infinite number of other scenarios, right? Why this one?"
    mc "I can see your point. Out of countless theoretical universes, why this one with so many similarities to my original."
    show pen neutral with d
    pen "Even little things, like the atmosphere and biological conditions of the planet being perfectly habitable for you. You lucked out big time."
    mc "Maybe it wasn’t luck. Perhaps there were other versions of me that ended up in uninhabitable universes, and I happened to be the fortunate one."
    show pen bashful with d
    pen "No, that idea doesn’t sit well with me. I prefer not to chalk things up to coincidence in science. I want to break this down into the simplest and most logical possibility."
    show pen happy with d
    pen "Let’s begin with how you enter each universe. It’s always a [mox] casting a spell that pulls you from another reality, right?"
    mc "Yes, based on what I’ve learned, it requires a universe with a [mox] capable of interuniversal magic where I don’t already exist."
    show pen wink with d
    pen "That already significantly reduces the number of potential universes."
    mc "Only if we assume there aren’t infinite universes."
    show pen awkward with d
    pen "As I've said. If that were true, there’d surely be a universe bent on destroying all others."
    mc "What if there were only a dozen similar universes, or something?"
    show pen raised with d
    pen "There’s absolutely no way I’d accept that twelve universes could somehow remain so similar after trillions of years of development."
    mc "Hold on… What you just said reminded me of something important. The mare who first showed me the mirrors in the castle taught me something called ‘boundary’ theory."
    mc "It’s a theory that could challenge yours and consistently explain my existence."
    show pen happy with d
    pen "Is that so? Sounds like we should track down this lady of yours."
    mc "That’s tricky. The only connection I had with her was as the Queen’s former student. Other than that, it might be worth checking out for club in the city called ‘The Bed of Chaos.’"
    show pen wink with d
    pen "Another lead? I’m starting to enjoy investigating all these unique characters of yours. Maybe I’ll try meeting this one myself. But first, could you tell me about this ‘boundary’ theory?"
    mc "I was taught that there’s a boundary coefficient that determines the similarity between two universes. The closer this coefficient is to one, meaning nearly identical, the easier it is for these two universes to interact."
    mc "Therefore, this universe can only interact with others that are similar. That’s why the same people keep appearing in every universe I visit. I’ve encountered multiple copies of many different people, and without this idea of boundaries, the chances of that happening are nearly nonexistent."
    show pen raised with d
    pen "Ah, I see. Does this coefficient fluctuate?"
    mc "Certainly. Universes are constantly evolving and adapting. Two universes might intersect briefly in time before diverging completely, each with its own unique past and future."
    show pen happy with d
    pen "Like ships passing in the night... I really like this theory. But you’re not going to tell me there are still infinite universes within each boundary, are you? My ‘universe destruction’ theory still stands true."
    mc "How could a universe capable of destroying another ever fit within our boundary, hm? We’re safe."
    show pen bashful with d
    pen "You’ve got me there... It’s not my field of research, but I’m sure there must be a book about this somewhere on the ground floor."
    stop music fadeout 2
    scene bg black with dissolve
    scene bg library 
    camera: 
        ypos -150 zpos -350
    with d
    play music casual2
    "We head down to the ground floor together and start searching. Unfortunately, unlike the other tree library, this one isn’t organized by genre or alphabetically."
    mc "I’ve been wondering why this tree isn’t a public library. It seems odd to keep such a large and expensive structure solely as a home."
    show pen wink with d
    pen "A public library, huh? That does sound nice, but who would have the time to maintain something like that?"
    mc "You worked there part-time for a few hours a day, that’s all."
    show pen neutral with d
    pen "And I suppose the library was free, so who exactly paid me for that?"
    mc "The castle supported the library, of course. It viewed the sharing of knowledge as essential to society, and [lil] was actually positioned as a political representative of the suburbs."
    show pen happy with d
    pen "Now that’d be nice. Unfortunately, the focus of this city, the Queen, and even 'our' [lil] seems more inward and self-focused…"
    show pen awkward with d
    pen "But it’s not purely greed. Everyone is struggling, so those who have the means to accumulate resources will do so until they feel secure enough to share."
    show pen neutral with d
    pen "It’s not pleasant, but it’s a reality of society. Those who are struggling themselves can’t always help those in greater need until they’re on stable ground. It often leads to competition for limited resources."
    show pen bashful with d
    pen "I’m a student myself, and with the way the world is going, I’m grateful that education is still valued by the Queen, instead of solely focusing on the city’s defense and military."
    menu mr1p1:
        "What is your role in this world? Just studying enchantments?":
            show pen raised with d
            pen "That’s quite a heavy question, but I see why you’re asking. Yes, I specialize in enchantments, which involve imbuing magical properties into objects."
            pen "It’s considered one of the most practically valuable fields of magic, as these enchanted relics are highly sought after by countries worldwide."
            pen "Unfortunately, it’s never as straightforward as casting a spell on an object. For reasons I couldn’t possibly explain in an hour, sometimes specific metals are required, or the spell needed is so fundamentally different that it defies initial understanding."
            pen "But what I can tell you is that the Arcadian Army is heavily focused on developing equipment that can naturally counter those… well, those {i}creatures{/i}."
        "How did you become friends with [mox]?":
            show pen happy with d
            pen "You might already know a different version of this story. [mox] had an ambitious performance that nearly ended in disaster if [lil] hadn’t intervened."
            pen "[lil] helped, sure, but she’s not exactly the emotionally supportive type. I empathized with [mox], so I reached out and befriended her."
            pen "Initially I was just trying to teach [mox] a little bit more about magic, but our chemistry ended up great due to a variety of shared experiences and interests."
            mc "And now look at you two, having threesomes with familiars."
            show pen bashful with d
            pen "Pfft, I mean… What use is a bestie if you’re not going to eat each other out during mating season?"
        "Why are you so horny?":
            show pen wink blush with d
            pen "Was the other me a bit more reserved? Hehe, well, I’ve always had an incredibly high libido outside of mating season."
            pen "As you can imagine, when it comes to mating season, I’m practically drunk with lust. It’s the only reason I have enough confidence to go down on my friends."
            pen "When I’m that aroused, I can’t just lie in bed and daydream; I end up needing to act on it."
            if moxpen2 == 1:
                pen "Luckily, you’ve been a reliable supply of what I need, so I’ve managed to keep it under control this season."
            else:
                pen "And you haven’t even had sex with me yet! I’m finding it hard to even focus on finding this book. Do you have any idea how nice you smell right now?"
            mc "I don’t envy your animal instincts."
            show pen happy -blush with d
            pen "Maybe you would if you knew just how fucking amazing it felt to finally feel that relief after a month of being pent-up."
        "What was your past like? (Continue)":
            jump mr1p2
    jump mr1p1
    label mr1p2:
        mc "Everyone else I’ve met in this universe seems to be the same species, except you. The distinction between a morphling and a unicorn is subtle but significant. Maybe understanding your past could shed light on this."
    show pen awkward with d
    pen "I barely know what a morphling is… I do know their Queen was wiped out a few hundred years ago though. That’s long before my time."
    mc "I think that the morphling Queen had the ability to transform creatures of other species into morphlings. So, in this reality, your ancestors must have escaped that fate."
    show pen angry with d
    pen "Transformation into a morphling? That’s a bit unsettling to think about, but I suppose it’s possible."
    show pen neutral with d
    pen "As for my background, I’ve lived in Arcadia all my life. Raised by loving parents who managed to make ends meet. I went to college, and… now I’m… Is this…?"
    "[pen] discovers something in an old box next to a bookshelf. She pulls out a red dog collar and gives me a bemused look."
    show pen wink blush with d
    pen "Just how naughty was I when I was a morphling?"
    mc "{i}Naughty{/i}? Well, you did trick me and attempt to enslave all of Arcadia."
    show pen surprised with d
    pen "Whoa! That’s way worse than I expected! I was just trying to start dirty talking."
    mc "Does this have any relation to the dog collar?"
    show pen wink with dissolve
    show black with dissolve
    call camerareset2 from _call_camerareset2_19
    hide black with dissolve
    "She flashes me a wink and guides me to a sneaky corner on the ground floor where a couch sat."
    show pen horny with d
    pen "It could… if that’s what you want~"
    "The collar was simple yet striking—a plain red leather circle with a silver clasp. What drew my attention most was the engraving on the front: 'Property Of...' left intentionally blank. Finishing my inspection, she tilted her head, raising an eyebrow curiously."
    show pen raised with d
    pen "Well? Do you want me to be your naughty bitch?"
    "Her words sent a thrill through me. Was this dignified mare really offering herself up as a pet? She certainly has the libido to back it up. Handing me the collar, the decision is left up to me."
    layeredimage pen1a:
        always:
            "pen1ab [penb]"
        group bigger:
            attribute bigger:
                "pen1abigger [penb]"
        group cum:
            attribute cum:
                "pen1acum"
        group eyes:
            attribute e1:
                "pen1ae1 [penb]"
            attribute e2:
                "pen1ae2 [penb]"
        group petplay:
            attribute collar:
                "pen1apetplay"
    stop music fadeout 1
    menu:
        "Place the collar around her neck.":
            $ petplay = 1
            show pen horny collar with d
            "[pen] turned around and lifted her hair, exposing the back of her neck. Carefully, I wrapped the collar around her throat, fastening it snugly but not too tight. She turned back to face me, her eyes dark with anticipation."
            mc "How does it feel?"
            show pen happy with d
            pen "I feel… different. Excited. It's perfect…"
            play sound2 equip
            scene black with d
            "I couldn't resist any longer. Leaning in and kissed her deeply, my hands gripping the leash as I pulled her closer. She responded eagerly, her tongue tangling with mine in a passionate dance."
            show pen1a e1 collar 
            $ textbox = 2
            call camerabreath from _call_camerabreath_30
            play music sextheme
            play moans1 moansmisc2
            with d
            "When we finally broke apart, we were both breathless. [pen] took a step back, her eyes never leaving mine as she slowly sank to her knees and in front of my growing erection."
        "Not my thing.":
            $ petplay = 0
            pen "That’s okay. We all have our own tastes. But I have something else that I’m sure you’d love~"
            show pen1a e1 
            $ textbox = 2
            call camerabreath from _call_camerabreath_31
            play music sextheme
            play moans1 moansmisc2
            with d
            "[pen] took a step back, her eyes never leaving mine as she slowly sank to her knees and in front of my growing erection."
            pen "All you have to do is ask, and I’ll do anything you want me to~"
    menu:
        "Serve your master with your breasts, bitch.":
            $ pen1 = 1
        "Service my cock with your breasts.":
            $ pen1 = 1 
        "You’re getting distracted; we were supposed to be looking for a book.":
            pen "Aahh, but how am I supposed to concentrate with you in the room. Please, indulge me a small amount, and I’ll devote my undivided attention to you."
            pen "I’ll even let you put it inside~"
            menu:
                "{i}Let her continue{/i}":
                    pass
                "{i}Move away{/i}":
                    mc "Sorry, [pen]. I’m feeling a little worn out right now."
                    pen "Uuuhhh… I was going to let you fuck me too… It’s fiiinnee. I’ll summon a familiar later."
                    jump pen1skip
    "Without breaking eye contact, she pressed her breasts together and wrapped them around my length."
    if petplay == 1:
        "The sensation was incredible. Her soft, warm flesh enveloped me, and I let out a low groan of pleasure. I tightened my grip on the leash, feeling a surge of control that was both exhilarating and stimulating."
    else:
        "The sensation was incredible. Her soft, warm flesh enveloped me, and I let out a low groan of pleasure."
    play ambience1 handjob
    camera:
        linear 0.2 zpos -17 ypos -2 xpos 0
        block:
            linear 0.1
            linear 0.3 ypos 8
            linear 0.1
            linear 0.2 ypos -8
            repeat
    "[pen] began to move, sliding her breasts up and down my shaft in slow, deliberate strokes. Her eyes stayed locked on mine, a mixture of submission and desire in their depths. I could feel every inch of her against me: her soft fur, the subtle curve of her body, the way she moved with such grace and confidence."
    if petplay == 1:
        mc "Good girl. Keep going, just like that."
    else:
        mc "Mmhhh, your breasts are perfect! Keep going!"
    "She moaned softly in response, the sound vibrating through her chest and adding to the sensation. I couldn't take my eyes off her, mesmerized by the sight of her pleasuring me with such dedication."
    if petplay == 1:
        "I tugged lightly on the collar, and she looked up at me, her expression one of pure submission."
        mc "You’re my naughty bitch from now on. Don’t forget that."
        pen "Yes, master."
    else:
        "She looked up at me, her face practically radiating lust."
    mc "I still can’t believe how horny you get."
    pen "Hehehe, a cute man that’s smart too? Maybe you’re just sexier than you realize."
    "[pen] increased her pace, her breasts moving faster and faster along my length. I could feel myself getting closer, the pressure building with each stroke."
    if petplay == 1:
        "I tightened my grip on the collar again, the leather digging into her neck just enough to remind us both of the power dynamic."
    mc "Nngghh, if you keep going like that, I’m going to cum soon!"
    "I warned her, my breath coming in ragged gasps, and [pen] didn't slow down, her movements becoming even more determined."
    if petplay == 1:
        pen "Do it! Come for your little bitch, Master!"
    else:
        pen "Yes! Cum for me, [mc]!"
    play sound2 cum
    show pen1a e2 cum with c
    play sound2 cum
    with c
    "That was all it took. With a final, shuddering thrust, I exploded, my release spilling over her breasts in hot, thick streams."
    play sound2 cum
    with c
    play sound2 cum
    with c
    "She moaned in delight, continuing to move until I was completely spent."
    stop ambience1 fadeout 3
    call camerareset from _call_camerareset_8
    "But as I caught my breath, I noticed a gleam in [pen]’s eyes that told me she wasn’t done quite yet. She licked her lips, her face flushed with excitement."
    if petplay == 1:
        mc "Mmmhh… Good girl. That was exceptional, and I think you deserve a reward."
    else:
        mc "{i}Pant, pant{/i} You’re amazing, but I think it’s time you got to have a little fun too."
    pen "Would you be interested in taking it to the next level?"
    mc "What did you have in mind?"
    play sound2 equip
    scene black 
    show bg library
    show pen horny cum
    if petplay == 1:
        show pen collar
    call camerareset2 from _call_camerareset2_20
    $ textbox = 1
    with d
    pen "I’ve never done this before, but… I really want you to tie me up and have your way with me."
    layeredimage pen1b:
        always:
            "pen1bb [penb]"
        group arms:
            attribute rope:
                "pen1brope [penb]"
            attribute norope:
                "pen1bnorope [penb]"
        group lingerie:
            attribute lingerie:
                "pen1blingerie"
        group eyes:
            attribute e1:
                "pen1be1 [penb]"
            attribute e2:
                "pen1be2"
            attribute e3:
                "pen1be3 [penb]"
        group cum:    
            attribute cum:
                "pen1bcum"
        group plug:    
            attribute plug:
                "pen1bplug"
        group sex:    
            attribute v1:
                "pen1bvaginal"
            attribute a1:
                "pen1banal"
        group sex2:    
            attribute v2:
                "pen1bvaginalcum"
            attribute a2:
                "pen1banalcum"
    menu:
        "Tie her up! Tier her up! Tie her up!":
            $ tiedup = 1
            $ gent1 = "ropes"
            "The idea sent a jolt of excitement through me. I had dabbled in bondage before, but hearing [pen] express such a desire was something entirely different. I nodded, feeling a thrill of anticipation."
            mc "I’d love to."
            hide pen with d
            "She smiled, biting her lip as she stood and walked over to the box the collar was in, retrieving a length of rope and handing it to me. I took the rope and led her back over to the couch."
            mc "Get on your belly."
            "I instructed, my voice firm but gentle. [pen] complied eagerly, positioning herself with her belly against the couch, her ass raised invitingly, and her arms behind her back."
            show pen1b e1 rope 
            $ textbox = 2
            call camerabreath from _call_camerabreath_32
            with d
            "I started by wrapping the rope around her wrists, securing them together tightly but not too tight. I then wound the rope around her torso, creating a harness that pressed firmly against her arms and chest."
            "She let out a soft moan as the ropes tightened around her, her body shivering with anticipation."
            pen "Ooohhhh… I can’t believe how wet I’m getting right now! I knew I’d enjoy this, but… mmphhh… I didn’t realize how much."
            "I finished tying her up, making sure the knots were secure. She was at my complete mercy, and the sight of her bound and helpless sent a surge of desire through me."
        "Not my kind of thing.":
            $ tiedup = 0
            $ gent1 = "bed"
            pen "Awh, worth a shot~ At the very least, I know you’ll definitely like."
            show pen1b e1 norope 
            $ textbox = 2
            call camerabreath from _call_camerabreath_33
            with d
            "Turning around on the couch, she laid down and lifted her butt up, her tail flickering out the way and revealing her dripping wet pussy."
    "With her butt exposed, I couldn't resist running my hands over her fluffy, soft fur. She squirmed beneath my touch, her moans growing louder as I caressed her. I took my time, savoring the sensation of her body trembling under my hands."
    if petplay == 1:
        mc "You're so beautiful like this, pet." 
        "She looked back at me, her eyes filled with lust and her voice a breathy whisper."
        pen "Please, master… Have your way with me~"
    else:
        mc "You look so beautiful from behind."
        pen "Heh, don’t just stare… Have your way with me~"
    "I didn't need any more encouragement. I positioned myself behind her, my erection hard and ready. I teased her entrance with my tip, eliciting a gasp from her."
    mc "Is this what you want?"
    pen "Nngghh… Yes! I want it so bad!"
    play sound2 cum
    show pen1b v1 e2 with d
    "I thrust into her in one smooth motion, filling her completely. She cried out in pleasure, her body arching against the [gent1]. The feeling of her tight, wet heat around me was almost too much to bear."
    play ambience1 sex
    play moans1 moansmisc4
    camera:
        linear 0.2 zpos -16 ypos -2 xpos 0
        block:
            linear 0.05
            linear 0.5 ypos 4 xpos -12
            linear 0.05
            linear 0.4 ypos -4 xpos 8
            repeat
    "I began to move, my thrusts steady and deep. Each movement elicited a moan from [pen], her body straining against the [gent1] as she met my rhythm. "
    if petplay == 1:
        "And I grabbed hold of the collar around her neck, using it to pull her back against me with each thrust, choking her and slightly reducing her airflow."
    "The sight of her bound and writhing in pleasure was exhilarating. I could feel her tightening around me; her moans growing more frantic as she neared her climax. I increased my pace, driven by the sound of her pleasure and the feeling of her body responding to mine."
    if petplay == 1:
        mc "Good girl, you’re doing so well… Mmmhh… I love seeing this side of you. Such a beautifully intelligent woman, reduced to a quivering mess."
    else:
        mc "Mmmhh… I love seeing this side of you. Such a beautifully intelligent woman, reduced to a quivering mess."
    "Her response was a wordless cry of pleasure, her body shaking with the intensity of her orgasm."
    play sound2 cum
    show pen1b v2 with c
    play sound2 cum
    show internalcreampie with c:
        ypos 600
    "The sight and sound of her climaxing pushed me over the edge, and with a final, powerful thrust, I reached my own release, filling her with my seed."
    play sound2 cum
    with c
    play sound2 cum
    show pen1b -v2 -v1 cum e3
    hide internalcreampie
    call camerareset from _call_camerareset_9
    call stopbgs from _call_stopbgs_24
    with c
    "We stayed like that for a moment, both of us catching our breath."
    pen "That was incredible…"
    if tiedup == 1:
        play sound2 equip
        show pen1b norope e1 with d
        "I gently untied the ropes, freeing her from her bindings. She turned to face me, a satisfied smile on her lips."
    show pen1b e1 with d
    "I pulled her into my arms, kissing her tenderly. [pen] snuggled closer, her eyes closing as she rested against me."
    stop music fadeout 10
    scene black with d
    camera:
        ypos -150 zpos -400
    show bg library
    show pen laughing
    if petplay == 1:
        show pen collar
    with d
    pen "I can't wait to see what we’ll do next~"
    mc "Hahaha, I can’t believe you."
    show pen happy with d
    pen "What? Did I say something funny?"
    mc "It’s just… You’re so horny that even though we just had sex, you’re already imagining and anticipating the next time."
    show pen horny with d
    pen "Oops, hehe!"
    mc "But you’re right. I can’t wait to see what kind of mischief we’ll get up to next."
    label pen1skip:
        scene bg library
        show pen happy 
        if petplay == 1:
            show pen collar
        call camerareset2 from _call_camerareset2_21
        call stopbgs from _call_stopbgs_25
        $ textbox = 1
        with d
        pen "{i}Phew{/i} ... Well, I think finding a book on this ‘boundary’ theory is a lost cause."
        show pen laughing with d 
        pen "Instead, I’ll try to locate this lady you mentioned. Surely, finding a former student of the Queen won’t be too challenging while living with the current student."
    mc "I still can’t thank you enough for everything you do for me, [pen]."
    show pen wink with d
    if petplay == 1:
        pen "I already told you, Master, I’ll do anything you want me to~"
    else:
        pen "To be fair, I’m benefiting from this too. Your situation has me so curious that I want to meet this girl myself and probe her mind." 
    scene black with d
    "With that settled, [pen] and I part ways, and I head back to [mox]’s apartment before it gets too late."
    play music moxietheme
    play ambience1 night
    scene bg apartment with d
    "I was lounging on the couch when [mox] returned from a performance, looking as confident as ever, her usual smirk playing on her lips."
    show mox smug with d
    mox "Well, well… Judging by your messy hair, you must have had quite a day. Care to share the details?"
    mc "You wouldn’t believe it if I told you. Buuuut... since you asked, let’s start with [lil]."
    show mox laughing with d
    mox "This ought to be good!"
    mc "[lil] literally cloned herself so she could watch me fuck it. She was supposed to watch and record data… or something. Her experiments have always been a little crazy."
    show mox surprised with d
    mox "Fuck a clone!? What did the clone say? I can’t imagine even a cloned version of that dork would agree to that."
    if lily2 == 1:
        mc "Well, this clone was something else—far more outgoing. She really encouraged [lil] to be more open and adventurous. It was like watching [lil] discover a whole new side of herself."
        show mox surprised with d
        mox "Ooohhh…? Like a reflection of her true, deepest, darkest desires? Hoho, this is pretty juicy…"
        mc "The clone was persuasive, and pushed [lil] to try things she never would have considered on her own.... I ended up fucking the clone on top of [lil]."
        show mox laughing with d
        mox "Pfft… So… She cucked herself?"
        mc "Yup, technically she did."
    else:
        mc "I didn't agree to have sex with the clone. That whole situation felt a bit too weird."
        show mox happy with d
        mox "Hmm, yeah I agree."
    show mox wink with d
    mox "And I assume you visited the lovely [pen] while you were there."
    mc "She was like a force of nature. We were trying to do some research but she couldn't focus at all."
    show mox bashful blush with d
    mox "Aye, that's how heat is sometimes. Next time, I’ll have to join you. She doesn’t know I’ve lost my virginity yet, after all."
    mc "Although it’s pretty obvious~"
    show mox horny with d
    mox "Pfft… What would you do if you had us both to yourself again? You could do anything you wanted~"
    mc "Hmm… I think I’d make her spread your pussy out and rub it while I fucked you. Then after I finish inside, I’d make you sixty-nine, so she’s licking your pussy while it’s dripping with cum. She’d be on top, so I can fuck her, and you’d have a direct view of my cock sliding inside from below."
    show mox surprised with d
    "I turn back to a flustered [mox] with a wide blush."
    mox "Uhm, oh my goodness…"
    show mox horny with d
    mox "Do you… uh, want to go have sex right now?"
    mc "You didn’t have to ask."
    show moxie1a e3 v1 with dissolve
    "..."
    #lily friendship feed post after visit 2: new day, new me. more productive than ever
    scene black with d
    if replay == 1:
        return
    $ magicroute1 = 1
    $ magiccompletion += 1
    $ completion += 1
    $ lilmsg1 = 1
    $ unread += 1
    $ unreadlil += 1
    jump newday
label magic2:
    show lil awkward coat with d
    lil "Unfortunately, I can’t keep around the clones forever. Not only do they constantly drain my magic, but I also need to sleep. Concentrating under the sheets is nearly impossible."
    mc "Under the sheets? You managed just fine while we were... Well, it was incredible that you were able to create a clone in the first place."
    show lil laughing with d
    lil "Yup, not to toot my own horn—pun intended—but I am a prodigy. Only about one in ten thousand unicorns ever get skilled enough to pull a trick like that off!"
    lil "Your average familiar can’t even communicate, let alone show any semblance of personality."
    mc "She did feel very real, but…"
    show lil wink with d
    lil "And furthermore, I’m capable of summoning [lil] 2.0 again whenever you’d like."
    mc "Don’t you think giving a temporary clone such a rich sense of sentience is somewhat cruel?"
    show lil neutral with d
    lil "Pardonnez-moi?"
    mc "Let’s use you as an example. Since [lil] 2.0 essentially was you, imagine I tell you that as soon as I go to sleep, you will permanently cease to exist. How would you feel about that?"
    show lil awkward with d
    lil "That’s such a simplistic reduction of what really happened! I temporarily created an offshoot of myself that eventually disappeared, but the whole still remains."
    mc "Yeah, but that overlooks the fact that [lil] 2.0 was a sentient existence that is now gone forever."
    show lil happy with d
    lil "She continues to live through me, [lil] 2.0 and I spoke a lot, and ultimately, we concluded that she was another side of myself."
    mc "To acknowledge that, you’d have to deny that [lil] 2.0 engaged in various experiences that were external to you, experiences that are now lost forever."
    show lil neutral with d
    lil "Hm, how so? We were together the entire time."
    mc "Even the mundane things, like contemplating their mortality or going to the bathroom. If you were to conjure a technical [lil] 3.0, she wouldn't have the exact memories and experiences of [lil] 2.0, no matter how much she pretended to."
    mc "It’s like the immediate conception of a twin. If [lil] 2.0 had the opportunity to live the rest of a natural life, she would absolutely become a different person. Those opportunities were tragically taken away due to the short nature of her existence."
    show lil shocked with d
    lil "No, no, you’re overthinking this! I appreciate that this magic could be abused, but [lil] 2.0 was with me the entire time. There was nothing she experienced that I didn’t."
    mc "Ah, but that’s where you’re wrong. [lil] 2.0 lost her virginity, but you—and a possible [lil] 3.0—would still be virgins."
    show lil neutral with d
    lil "Ah…?! But… I—"
    show lil laughing with d
    lil "Infinite virginity glitch discovered?"
    show lil awkward with d
    lil "{i}Eh-hem{/i} Jokes aside. Maybe you’re right. But what would you have me do? Intentionally lobotomize my clones so they can’t self-actualize?"
    mc "That’s not really my point. As long as you’re aware and okay with these unusual circumstances." 
    mc "For me, it just hits close to home. [lil] 2.0 was a fun character, and she might be gone forever."
    show lil smug with d
    lil "Ohoho, no, no way did you just say that."
    camera:
        linear 0.5 ypos -150 zpos -400
    "[lil] leaned over me with a burst of surprising confidence."
    show lil shocked with d
    lil "Who do you think she was a clone of, punk? The real [lil] was right here all along, and I’m not about to be shown up by another version of myself that {i}I{/i} created!"
    show lil neutral with d
    lil "I’ve had enough of this charade, and more than enough of watching everyone else have some fun."
    show lil horny blush with d
    lil "In the wise words of [lil] 2.0, it’s finally time for me to be honest to myself."
    play sound2 equip
    show lil -coat with d
    "With a decisive flick of her wrist, [lil] let her lab coat fall to the floor, effectively stripping away the last barrier between us. Though I’d seen all the good parts anyway, it was still a sexy, bold statement."
    call camerareset1 from _call_camerareset1_10
    show lil bashful with d
    "Yet, despite her newfound confidence, she couldn’t help but sway shyly from side to side."
    lil "Uhm, perhaps that was a pretty forward move... The other me was completely honest, but that doesn’t mean I’m not shy about it."
    mc "You don’t think it’s disgusting?"
    show lil neutral with d
    lil "I’ve explored those feelings… and it all comes down to insecurity. It’s a lot easier to say you hate something than admit you don’t think you’re good enough for it."
    "Her voice was soft, barely a whisper, her expression flushed with embarrassment and something deeper—confidence tinged with uncertainty. Was she truly ready to take the next step?"
    mc "[lil], you’ve {i}always{/i} been good enough."
    show lil happy with d
    lil "Do you really mean that? I mean - of course!"
    mc "From what I know, you're the girl who can do anything, the future ruler of Arcadia. All you need to do is make that step."
    stop music fadeout 10
    stop ambience1 fadeout 10
    play sound2 equip
    camera:
        linear 0.5 ypos -150 zpos -400
    hide lil with d
    "I reached out and offered my hand. She took a step forward and then practically dived into me. Her warm fur brushed against my bare skin, and I felt a slight tremor as she clung to me."
    mc "We'll take it slow, and I'll be here with you every step of the way."
    "She took a deep breath, her chest rising and falling with the effort."
    show lil horny blush with d
    lil "The bed… I want to try it with you."
    layeredimage lily3a:
        always:
            "lily3ab [lilb]"
        group eyes:
            attribute e1:
                "lily3ae1 [lilb]"
            attribute e2:
                "lily3ae2"
            attribute e3:
                "lily3ae3 [lilb]"
        group legwear:
            attribute lingerie:
                "lily3alingerie"
            attribute p1:
                "lily3apantyhose 1"
            attribute p2:
                "lily3apantyhose 2"
        group cum:
            attribute cum:
                "lily3acum"
        group sex1:
            attribute v1:
                "lily3av 1"
            attribute a1:
                "lily3aa 1"
        group sex2:
            attribute v2:
                "lily3av 2"
            attribute a2:
                "lily3aa 2"
        group pregnant:
            attribute pregnant:
                "lily3apregnant [lilb]"
        group futa1:
            attribute f1:
                "lily3afuta 1"
        group futa2:
            attribute f2:
                "lily3afuta 2"
    show lily3a e1 
    call camerabreath from _call_camerabreath_47
    play music sextheme
    play moans1 moansmisc2
    $ textbox = 2
    with d
    $ lily3 = 1
    "I guided her towards the bed, and she laid down, her neat violet hair cascading over her shoulder. Nervousness still warred with desire in her eyes."
    "I leaned in and kissed her gently, my lips brushing against hers in a tender caress. She responded hesitantly at first, her lips soft and tentative, but as the kiss deepened, I felt her relax, the tension slowly melting away."
    mc "You’re doing great. Just follow your instincts."
    "My hands began to explore the curves of her body, her body completely opening up to me as I got down to her thighs. I could feel a shift in her, the way her body pressed closer to mine, her need becoming more pronounced."
    lil "Mmhh… Please, I want to feel you inside me~"
    "If she’s anything like her [lil] 2.0, this shyness won’t last. Her flank was raised and wiggling slightly, presenting an irresistible invitation."
    play sound2 cum
    "Taking my throbbing cock in my hand, I pressed it against her pussy. Gently pushing inside, allowing her slickness to coat my cock, allowing a deeper venture with each push."
    play sound2 cum
    show lily3a e2 v1 with d
    play moans1 moansmisc3
    "Once my tip was finally soaked with her juices, I pushed forward once more and finally pierced through her virginity." 
    "A deep moan escaped as she felt herself getting filled up for the first time, her body tensing up and before finally relaxing into the sensation. Any discomfort was replaced by an overwhelming flood of pleasure, leaving her body trembling in awe."
    play ambience1 sex
    camera:
        linear 0.3 zpos -12 xpos -2
        block:
            linear 0.6 xpos 5
            linear 0.2 xpos 5
            linear 0.4 xpos -2
            linear 0.1 xpos -2
            repeat
    "Sensing her relaxing around me, I began to move, my hips slowly thrusting back and forth. I slid in and out of her tight entrance, each movement eliciting a chorus of soft, breathy moans that grew louder as our rhythm intensified."
    lil "Mmphhh, I-I get it now… This is why everyone loves sex… Uoohhhh, I don’t think I’ve ever been so satisfied in my entire life, so much dopamine and serotonin!"
    mc "Hahaha, trust you to geek out while you’re losing your virginity."
    "I continued to kiss her, my hands exploring every inch of her body, taking my time to savor the feel of her beneath me. She responded eagerly, her hips arching up to meet mine, her moans growing louder, more urgent. I could feel her surrendering to her instincts, her fears and insecurities melting away in the heat of our passion."
    "Lost in the throes of our passionate union, time and reality seemed to dissolve around us. We moved together with a primal, instinctual grace, our bodies gradually becoming synchronized as she thrust her hips too. The once reserved and studious [lil] moaned and writhed beneath me, completely surrendered to the pleasure."
    "Our bodies became one, and I could see the transformation in her—the way she was embracing her desires, letting go of her doubts and fears."
    lil "Uooohhh, goddess yes! Thrust it right there! Ooohhh, just like thaaaat~!"
    "I felt my control slipping, overwhelmed by the tightness of [lil]’s pussy and the heady scent of our sex. I knew I couldn’t hold myself back much longer."
    mc "Aahhh, I can’t hold back much longer! I’m about to cum!"
    lil "Ngghh, don’t hold back! Ejaculate inside me with that hot, fertile sperm!"
    play sound2 cum 
    show lily3a cum v2 
    show internalcreampie 
    with c
    play sound2 cum
    with c
    "With a series of powerful thrusts, I reached climax, my seed spilling deep inside of her."
    play sound2 cum
    with c
    play sound2 cum
    show lily3a e3 
    hide internalcreampie
    with c
    "My body grew tense, my mind fuzzy and blank as intense amounts of orgasmic pleasure washed over me." 
    stop ambience1 fadeout 1
    play moans1 moansmisc2
    call camerabreath from _call_camerabreath_48
    show lily3a -v2 -v1 with d
    "Panting and slick with sweat, I pulled out and basked in the afterglow, but that wouldn’t last long…"
    layeredimage lily3b:
        always:
            "lily3bb [lilb]"
        group goth:
            attribute goth:
                "lily3bbgoth"
        group eyes:
            attribute e1:
                "lily3be1 [lilb]"
            attribute e2:
                "lily3be2"
            attribute e3:
                "lily3be3 [lilb]"
        group legwear:
            attribute lingerie:
                "lily3blingerie"
            attribute p1:
                "lily3bpantyhose 1"
            attribute p2:
                "lily3bpantyhose 2"
        group cum:
            attribute cum:
                "lily3bcum"
        group plug:
            attribute plug:
                "lily3bplug"
        group sex1:
            attribute v1:
                "lily3bv 1"
            attribute a1:
                "lily3ba 1"
        group sex2:
            attribute v2:
                "lily3bv 2"
            attribute a2:
                "lily3ba 2"
    play sound2 cum
    show lily3b e1 cum with d
    "[lil] curled up, her voluptuous rear presented prominently towards me like a delectable treat just waiting to be devoured. Her once pristine mane is now a tangled mess of violet curls cascading across the bed."
    lil "I’m not done yet! It’s your job to make my first time special, so get hard again for me, [mc]~"
    mc "Oh baby, you didn’t even have to ask."
    play sound2 cum
    show lily3b e2 v1 with d
    "Her luscious flanks quivered as I repositioned myself. With a powerful thrust, I buried my throbbing member deep inside her once again. This time it pushed inside with ease, a stark difference to when I had to fight for each inch."
    play moans1 moansmisc4
    play ambience1 sex
    camera:
        linear 0.3 zpos -14 xpos -2
        block:
            linear 0.4 xpos 6
            linear 0.1 xpos 6
            linear 0.3 xpos -3
            linear 0.1 xpos -3
            repeat
    "[lil] moaned louder than before, her body trembling as I pounded into her, resuming my frantic pace from earlier. After having already orgasmed once, I didn’t have to worry about going too fast for a while, so I went wild with my passion."
    mc "Mmmhh, this is what you wanted, isn’t it? To be fucked like one of those slutty mares you always despised."
    lil "Oooohh, yes! I’ve needed it so badly, for so long!!"
    "Her voice had transformed from that of a timid scholar to a needy slut. I leaned in, nibbling her ear possessively as my hips slammed into hers without mercy. She arched her back, pushing against my thrusts, begging for more. The thrusts were going so deep now, grinding against her most sensitive spots."
    "The passionate lovemaking continued unabated, our rhythm growing more frenzied with each passing second. Sweat dripped from our bodies as we moved together like two well-oiled machines. Any remnants of life and its burdens drowning away under the primal nature of the moment."
    mc "You’re mine now~"
    lil "Aaahhh, y-yes! I’ll belong to you, to fuck whenever you want!"
    "[lil] moaned and whimpered as she started to cum. The dirty talking had finally pushed over the edge. It was a full-body orgasm that rocked her to the core—a perfect climax for her first time."
    "Her tight pussy clenched around my cock, attempting to milk me for every last drop of my potent seed."
    lil "Uooohhhh! It’s shoooo goooood! Mmmhhhh! P-Please, cum inside me again! Get me pregnant!!!"
    play sound2 cum
    show lily3b v2 
    show internalcreampie
    with c
    play sound2 cum
    with c
    "How could I refuse such a polite request? With a series of powerful, final thrusts, I let loose inside her, filling her womb once again with my hot seed."
    play sound2 cum
    with c
    play sound2 cum
    show lily3b e3 
    hide internalcreampie 
    with c
    "My cock throbbed as it continued to empty itself, our point of contact bubbling with our shared fluids as we continued thrusting until the pleasure was long gone."
    stop ambience1 fadeout 1
    play moans1 moansmisc2
    call camerabreath from _call_camerabreath_49
    show lily3b -v2 -v1 with d
    "Finally, my lack of energy caught up with me, and I collapsed onto the bed beside her. Both of us lay there, panting heavily, drenched in sweat and satisfaction."
    play sound2 equip
    stop moans1
    play ambience1 night
    stop music fadeout 3
    scene bg lilybedroom
    show night:
        blend "multiply"
        alpha 0.8
    call camerareset1 from _call_camerareset1_11
    $ textbox = 1
    with d
    "But as I hit the pillow, she rises from hers."
    play sound2 move
    show lil happy cum with d:
        xalign 0.25 
        linear 0.6 xalign 0.75
    "While catching my breath, I turn my head to watch. The first thing she does is clean up the cum, then she starts shifting things around, her movements deliberate and purposeful."
    show lil happy -cum with d:
        linear 0.8 xalign 0.25 
    "Tidying up? The notion seemed out of place in the moment, but I kept silent, my curiosity piqued."
    show bg lilybedroomtidy
    show lil happy:
        linear 0.8 xalign 0.5 
    with dissolve
    "Minutes tick by, and the floor, previously a chaotic mess, is now completely clear." 
    mc "Uh, I see you’re tidying up. But… why?" 
    play music casual1 fadein 2
    show lil bashful blush with d
    lil "I’ve… it’s embarrassing…"
    "Her hands move with an almost desperate efficiency, throwing away remnants of a life she seems determined to shed."
    show lil neutral -blush with d
    lil "I’ve been living as a pathetic shell of myself for so long, that I forgot what it was even like to have a normal life…"
    show lil awkward blush with d
    lil "And if we’re… you’re…"
    lil "I couldn't be honest with anyone, including myself. My attitude has been ridiculous, unworthy of being a princess, and unworthy of you as well."
    show lil raised -blush with d
    lil "While lying in bed last night, I wondered if you would have ever given me the time of day if you hadn’t known about my alternate world self. It doesn’t matter whether you would have or not; what matters is that I concluded that you {i}shouldn’t{/i}."
    lil "I came to the conclusion that I didn’t deserve it… this… you…"
    mc "[lil]…"
    show lil shocked with d
    lil "That’s the crux of it. Ever since you showed up, purely by coincidence, and delivered the insane news that I was the fucking {i}ruler{/i} of Arcadia in another universe…"
    "She shook her head at the sheer absurdity of it."
    show lil angry with d
    lil "I just… I can’t fathom such a timeline. It’s like... unknowable, indescribable to me."
    lil "Me? I’m just some loser with a wall of stacked energy drink cans because I’m too lazy to take a few minutes to throw them out."
    show lil neutral with d
    lil "If I can’t even get myself in order, if I can’t even look after myself, how can I possibly lead the Virtues of Concord? Let alone be the Queen this country needs?"
    show lil shocked with d
    lil "I’m putting my foot down! From now on, I’m getting my shit together."
    "Her voice wavered, but there was a fierce determination there too, a spark of the leader I knew she could be."
    show lil wink with d
    lil "And I know it’s not an easy or fast road. There will always be moments of weakness, but you’ve given me the strength I need to stop being [lil] 1.0 and start being [lil] 2.0."
    show lil bashful with d
    lil "But I hope to be even higher versions than that in the future. One day, I hope I’ll be worthy of becoming Princess [lil]."
    "In that moment, I saw not just the fragile girl struggling against her own demons, but a future queen beginning to emerge from the shadows."
    mc "I’m so proud of you!"
    mc "But, heh, was losing your virginity really that big of a moment for you?"
    show lil neutral with d
    lil "{i}Pout{/i} M-Maybe? As my vision and mind slowly returned in my post-coital haze, the first thing I thought of was… ‘Holy shit, it’s messy in here!’"
    mc "It reminds me of something [pen] said. Good enough sex can help you redefine your perception of life and how you view it, but what she was really referring to was the person."
    mc "The right people can help you prioritize what’s important, instead of falling back into a bubble and leaning on unhealthy habits."
    show lil wink with d
    lil "Exactly! Thank you for reaching out your hand, [mc]. I won’t let you down."
    hide lil
    show night:
        linear 0.3 alpha 0.5
    with d
    "I lay back down, continuing to watch her. Even though the room had been untidy every time I arrived, it didn’t take [lil] long to clean it completely. It’s only been about ten minutes. It really goes to show that this was more a barrier in her mind."
    show lil bashful with d 
    camera:
        linear 0.5 ypos -150 zpos -400
    "[lil] finally sat back down beside me, letting out a satisfied sigh. Then, with newfound confidence, she leaned in and initiated a kiss. If this is only the beginning of the new [lil], then I can’t wait to see what she’ll do next."
    show lil happy with d
    lil "In regard to my clones, I was thinking I could adapt the spell so the memories and experiences of the clone are returned to me. This would allow them to truly live on; now that would be a groundbreaking spell."
    mc "And couldn’t you use that to read several books at once and retain all the information? Sounds overpowered!"
    show lil smug with d
    lil "Hum… that… sounds… amazing! I need to discuss this with the Queen immediately!"
    show lil happy with d
    lil "Oh, but first, I really need a shower after tidying up."
    mc "In that case, I’ll head back home before It gets too late."
    show lil laughing with d
    lil "Thanks again for coming today. You’re always welcome here, love~"
    scene black with d
    "Back in [mox]'s apartment..."
    play music moxietheme fadein 3
    scene bg apartment
    show mox happy 
    call camerareset1 from _call_camerareset1_12
    with d
    mox "So, she's really coming out of her shell?"
    mc "Tidied her room and everything. It's a great sign since she's the central figure for the Virtues."
    show mox awkward with d
    mox "Ahh, I'm glad, but..."
    mc "But?"
    show mox wink with d
    mox "I'm afraid I'll believe it when I see it. [lil] and I are a bit rocky."
    mox "But if she's willing to bridge that gap, I'll be on the other end with open arms. Well, maybe not open arms, but a firm handshake."
    mc "Guess it's up to me to build those bridges."
    show mox laughing with d
    mox "Hey, you're pretty good at it!"
    if replay == 1:
        return
    $ magicroute2 = 1
    $ magiccompletion += 1
    $ completion += 1
    $ penmsg2 = 1
    $ unread += 1
    $ unreadpen += 1
    jump newday
label magic3:
    play ambience1 night
    scene bg city2 with d
    "Tonight, I didn’t just visit [pen] alone; [mox] decided to come along too. Perhaps intrigued by the lewd comments I’d brought back from my last visit."
    "As we walked to the tree, our implied plans of eroticism were hushed by giggles, the air thick with unspoken thoughts."
    show bg peneloperoom
    show mox happy:
        xalign 0.25
    show pen laughing:
        xalign 0.75
    with d
    pen "Hey, my beauties! Feel free to pour yourself a glass of wine."
    if petplay == 1:
        show mox neutral with d
        "Noticing the collar around [pen]'s neck, [mox] leaned in, curiosity lighting up her face. "
        mox "What’s that collar you have on, [pen]?" 
        show pen laughing with d
        "[pen] puffed her chest out with pride, raising her chin so [mox] could get a better look."
        show mox surprised
        mox "W-Wha?! This has [mc]’s name on it!"
        mc "Really? Let me see that!"
        "Sure enough, there it was. The tag read, ‘Property of [mc].’"
        show pen wink blush with d
        pen "Hehe, I’ve taken to wearing it more often. It makes me wet~"
        show mox bashful blush with d
        mox "Oh my goodness! Lewd!"
        show pen happy with d
        pen "I did have a question for you, [mc]. Do you want me to call you master outside of the bedroom too?"
        menu:
            "You can call me…"
            "Master":
                $ penmc = "Master"
            "[mc]":
                $ penmc = "{}".format(mc)
            "Custom":
                $ penmc = renpy.input("What do you want [pen] to call you?")
                if penmc == "":
                    $ penmc= "{}".format(mc)
                $ penmc = penmc.strip()
        show pen laughing -blush with d
        pen "Fantastic choice, [penmc]."
        show mox laughing -bluhs with d
        mox "My goodness… I look away for a few days, and things really move fast, don’t they?"
    scene bg peneloperoom with d
    "The three of us settled onto [pen]’s couch, the soft cushions welcoming us like old friends. The wine poured freely, its rich aroma mingling with the evening air."
    "[pen] took out some boardgames for some drunken fun. I’m not familiar with most of them, but I find it particularly fascinating that both chess and checkers remain popular in this reality."
    show mox happy:
        xalign 0.75
    show pen laughing:
        xalign 0.25
    with d
    mc "Chess, it’s even {i}called{/i} chess here. That’s insane, isn’t it?"
    show pen laughing with d
    pen "In some ways, the three universes you’ve experienced are so similar it’s uncanny."
    mc "And yet, so different."
    show pen happy with d
    "[pen] and I set up a game of chess, and we start making a few rapid-fire moves. We’re both too drunk to really think about deep strategy right now."
    "[mox] watches, although she doesn’t seem to have a fantastic grasp on the rules…"
    "And apparently, neither do I as [pen] pulls out a bizarre move. A bishop, moving forward one square."
    mc "Is that really a valid move?"
    show pen neutral with d
    pen "Of course. Bishops are allowed to move forward once instead of performing a diagonal move. This allows them to swap between the white or black squares."
    mc "Wow, maybe I don’t know how to play this variant of the game after all."
    "Noticing [pen] has both bishops with good sightlines towards my king, I decide to castle, only to receive a bewildered glance from her."
    show pen surprised with d
    pen "W-What kind of move is that?!"
    mc "This is called castling; it’s when an unmoved king and rook can kind of meet in the middle and swap places. It’s a trick you can only do once."
    show pen awkward with d
    pen "I’ve never heard of a chess move that lets you move two pieces at once before! Let alone under such specific circumstances…"
    show mox smug with d
    mox "Uhm… I don’t really get chess either, so why don’t we just play some checkers? The superior strategy game, right~?"
    mc "[mox] has a point. We could sit here and go over every single rule from our variants of chess, but I bet good ol’ simple checkers is exactly the same."
    show pen wink with d
    pen "Sure, checkers is very simple. Isn’t it a solved game, or something?"
    show mox laughing with d
    mox "Awh, don’t be like that, [pen]! You know, I bet if we played checkers and chess on the same board, the simplicity of checkers would give it an easy win!"
    mc "Well… If you’re so fond of checkers, and [pen] is so fond of chess, why don’t you try it?"
    show pen laughing with d
    pen "Hah! Now we’re talking. I’m going to mop you up!"
    show mox surprised with d
    mox "Wait a minute! You have 16 pieces, and I only have 12! Could I at least use four more to make up for that?"
    show pen wink with d
    pen "Heck, you can even go first if you think that’ll help you."
    show mox smug with d
    mox "Hehe, you’ll regret underestimating me, [pen]! With my checkers, I have unmatched board presence. You won’t be able to take anything without threatening huge losses!"
    stop music fadeout 1
    show black with d
    "The girls set up their games and operate through a few basic moves. The weaknesses of [mox]’s side become instantly apparent."
    hide black 
    play music comical fadein 1
    show pen happy 
    with d
    pen "My chess pieces are far more mobile than your checkers. I can quite effortlessly ensure that you never get more than a trade."
    show mox sad with d
    mox "Nuuuu, check your horse outta there!"
    show pen laughing with d
    pen "And these trades will only benefit me…"
    pen "As I slam my queen into your back ranks and proceed to clean up! Muhahaha! You can’t even stop me because checkers pieces can’t capture pieces against the sides of the board."
    show mox awkward with d
    mox "Uuoohhh, nooo! My pieces! I didn’t think this through!"
    show pen wink with d
    pen "Let’s not forget that checkers pieces are entirely confined to black squares, giving me tremendous safety when infiltrating your side of the board."
    show black with d
    "A few minutes later… [pen] had defeated [mox] and her army of checkers. It wasn’t even close."
    hide black 
    show pen happy
    with d
    pen "Don’t feel bad. I’d estimate a chess player would win this 99%% of the time."
    show mox neutral with d
    mox "Damn, sis... You literally got me playing checkers while you’re playing chess…"
    show mox laughing with d
    mox "Can we just play some Guess Whooves? Everyone loves Guess Whooves."
    stop music fadeout 1
    "After about an hour of casual fun, [pen] brings up the first serious topic of the night."
    play music casual2
    show pen happy with d
    pen "So, [penmc], I followed that lead to find a club called the ‘Bed of Chaos’ and its owner. But it turned out to be a complete dead end."
    pen "I’m afraid this is the first time one of your leads didn’t pan out. The information wasn’t exactly elusive—the timeline of The Queen’s past students is meticulously documented."
    show mox neutral with d
    mox "The last student was someone called ‘Stellar,’ I think. That was over a decade ago."
    mc "Really? I wonder how… and why? I’m fairly familiar with the major shifts that have shaped this world, but how could that lead to an entire person vanishing?"
    mc "Especially someone so crucial to my understanding of multiverses…"
    "I spent so long trying to fight the feeling of loss brought on by this universe, but it settled over me once again like thick fog. Yet more pieces of the puzzle seemed to be eluding me, and an unsettling feeling gnawed at my insides."
    show pen neutral with d
    pen "Why don’t we apply your boundary theory to this? You mentioned that I’m not even the same species between the two universes, correct?"
    pen "If the differences between universes can be as vast as species or levels of technology within a civilization, it’s not hard to imagine individuals disappearing here and there."
    show pen bashful with d
    pen "I think that makes sense to me. After all, you don’t seem to exist here, do you?"
    mc "H-Huh… You’ve got me there."
    show pen happy with d
    pen "Sorry I couldn't be any more help. If you have any other leads, I'll be happy to check them out for you. But, to be fair, you seem to have your shit together, do you even need my help anymore?"
    mc "I think that's everything. Thank you so much for all your help, both of you. I couldn't have gotten this far without you two, same in the other universe too."
    mc "If there's anything I can do to repay you two..."
    show mox horny blush with d
    mox "Aaahhh - I know how! After all, we came here to have to fuuuuck!"
    show pen surprised blush with d
    pen "[mox], we haven’t even gotten halfway through the bottle yet. How are you so drunk?"
    show mox wink with d
    mox "I’m not drunk on wine; I’m drunk on fine—on that fine stud right here!"
    show pen laughing with d
    pen "Hmm, hehe, very well. What did you have in mind?"
    show mox horny with d
    "With a glint of mischief dancing in her eyes, [mox] leaned in, whispering something into [pen]’s ear. My only clue about what was coming next was the widening surprise in [pen]’s eyes, followed by a sultry glance in my direction."
    show pen horny with d
    pen "Goodness me… It sounds like you’re in for a treat, [penmc]. I’m getting gooey just thinking about it."
    show mox laughing with d
    mox "Hmm… I know how we should start. [mc], please close your eyes for us." 
    stop music fadeout 1
    scene black with d
    "I shut my eyes, the world slipping into darkness as soft, playful hands lift me and guide me through the building. The wooden floorboards of the treehouse creaked beneath us."
    mox "We’ve got a surprise for you, and you’re going to love it~"
    "As I stumbled slightly, I felt a reassuring touch on my arm and then warm breath tickling my neck. A soft giggle floated in the air. The tension was palpable, electric, crackling with anticipation. I eagerly awaited the bliss they had in store."
    pen "Alright, just lie down right here, [penmc]."
    "[pen] voice held a hint of mischief as she guided me with gentle nudges until I felt the edge of the bed against my legs. Hands helped me recline, and the softness of the mattress beneath me was a welcome relief from the hard edge of my anticipation."
    mox "Open your eyes~"
    layeredimage pen2a:
        always:
            "penelope2ab"
        group moxie:
            attribute always:
                "penelope2amoxb [moxb]"
        group penelope:
            attribute always:
                "penelope2apenb [penb]"
        group moxeyes:
            attribute me1:
                "penelope2amoxe"
        group peneyes:
            attribute pe1:
                "penelope2apene [penb]"
    show pen2a always me1 pe1 
    play music sextheme
    $ textbox = 2
    call camerabreath from _call_camerabreath_50 
    play moans2 moansmisc2
    with d
    "I complied. The scene that met me was surreal, almost dreamlike."
    "[mox] and [pen] were perched atop me, their lithe bodies positioned ass-to-ass directly over my face." 
    "I was greeted with the sight of their flawless fur, mere inches away from my face. A perfect image of allure."
    "A heady scent filled my nostrils, a mix of their excitement and something sweet, almost floral. My senses were on fire, my body reacting instinctively to the raw sexuality of the scene. [mox]’s violet eyes met mine, a wicked smile curling her lips. She whispered…"
    mox "Surprise~"
    "Before I could fully process the view above me, [mox] began to move."
    layeredimage pen2b:
        always:
            "penelope2bbase"
        group moxie:
            attribute always:
                "penelope2bmoxb [moxb]"
        group penelope:
            attribute always:
                "penelope2bpenb [penb]"
        group punk:
            attribute p0:
                "penelope2bpunk"
        group moxpeyes:
            attribute p1:
                "penelope2bpunk 1"
            attribute p2:
                "penelope2bpunk 2"
            attribute p3:
                "penelope2bpunk 3"
        group moxeyes:
            attribute me1:
                "penelope2bmoxe1"
            attribute me2:
                "penelope2bmoxe2"
            attribute me3:
                "penelope2bmoxe3"
        group peneyes:
            attribute pe1:
                "penelope2bpene1 [penb]"
            attribute pe2:
                "penelope2bpene2 [penb]"
            attribute pe3:
                "penelope2bpene3 [penb]"
        group cum:
            attribute cum:
                "penelope2bcum"
        group sex1:
            attribute v1:
                "penelope2bv 1"
            attribute a1:
                "penelope2ba 1"
        group plug:
            attribute plug:
                "penelope2bplug"
        group sex2:
            attribute v2:
                "penelope2bv 2"
            attribute a2:
                "penelope2ba 2"
    show pen2b always me1 pe1 with d
    "She bent over slowly, deliberately, each movement a calculated act of seduction; the curve of her back arched provocatively. [pen] wasted no time following her lead."
    "The presented herself with an audacious confidence that left me breathless. [pen] took control with grace, her arms cradling [mox]’s flank while her greedy hands were firm but gentle as they spread [mox]’s pussy, exposing her fully to my hungry gaze."
    "There was a fluidity to their movements, a silent communication that spoke of their trust and comfort together as [pen] ran her finger against [mox]’s exposed clit, causing a shiver of anticipation." 
    pen "Go ahead, she’s ready for you~"
    mox "Mmm… More than."
    menu:
        "{i}Continue{/i}":
            $ pen2 = 1
            "I positioned myself behind [mox], the heat of her body palpable even from inches away. My hands found her hips, gripping her soft flesh with a possessiveness that surprised even me. [mox]’s body responded instantly, her back arching further, her breath hitching in anticipation."
            play sound2 cum
            play moans1 moansmisc2
            show pen2b v1 me2 pe2 with d
            "With a powerful thrust, I buried myself deep inside her. The feeling of her insides was incredible: a rush of heat and wetness."
            "[mox] moaned as she was filled up, her voice full of need. When I began to move, her body quaked beneath me, struggling to stay upright due to the sudden pleasure tearing through her."
            play ambience1 sex
            pen "Mmmhhh… There we go! That’s it… Give her everything you have."
            mox "Aaahhh, ahhh! I-It’s so good! [mc] is a bad influence. He’s turned me into an addict for his cock~"
            "[pen] watched enthusiastically; her eyes dark with desire. She leaned in close, her breath hot against my ear as she whispered encouragements, her hands never ceasing their exploitation of [mox]’s trembling form."
            pen "Ooohhh, look at the way her lips grip around your cock. You’re spreading her out so much!"
            "[mox]’s moans turned into cries of ecstasy as I picked up the pace, our bodies moving together in a frantic rhythm that left no room for thought, only pure sensation. The aroma of our lovemaking filled the room, mingling with the heady aroma of sweat and arousal."
            "At this point, [pen]’s hands found their focus, teasing [mox]’s clit, driving her wild with pleasure. [mox]’s response was a wordless cry, her body pushing back against mine with a desperate need that matched my own."
            pen "Mmhh… cum for us, [mox]~ And [penmc], I want you to fill her tight pussy up for me."
            "[mox]’s climax was sudden and powerful, her body convulsing around me as she was swept away by relentless tides of bliss. Her pussy clenched around my cock incredibly tightly, an ecstasy that easily sent me over the edge."
            play sound2 cum
            show pen2b cum v2 with c
            play sound2 cum
            with c
            "I found my release, accompanied by a burst of intense pleasure that left my mind numb."
            play sound2 cum
            with c
            play sound2 cum
            show pen2b me3 pe3 with c
            mox "Uooohhhh, gods yes! I love the feeling of your cum shooting inside, mmphhh…"
            show pen2b -v1 -v2 with dissolve
            stop ambience1
            play moans1 moansmisc2
            scene black with dissolve
            "As the echoes of our climax faded, [mox] rolled over and feigned death on the bed. Her eyes were closed, a look of blissful exhaustion painting her features. At least she died doing what she loved."
            layeredimage pen2c:
                always:
                    "penelope2cbg"
                group moxie:
                    attribute always:
                        "penelope2cmoxb [moxb]"
                group penelope:
                    attribute always:
                        "penelope2cpenb [penb]"
                group lingerie:
                    attribute lingerie:
                        "penelope2clingerie"
                group eyes:
                    attribute e1:
                        "penelope2ce 1"
                    attribute e2:
                        "penelope2ce 2"
                group cum1:
                    attribute c1:
                        "penelope2ccum 1"
                group cum2:
                    attribute c2:
                        "penelope2ccum 2"
                group futa1:
                    attribute futa1:
                        "penelope2cfuta 1"
                group futa2:
                    attribute futa2:
                        "penelope2cfuta 2"
                group sex1:
                    attribute v1:
                        "penelope2csex 1"
                group sex2:
                    attribute v2:
                        "penelope2csex 2"
                group squirt:
                    attribute v2:
                        "penelope2csquirt"
            show pen2c always e1 c1 
            $ textbox = 1
            with d
            "However, [pen], ever the opportunist, had other ideas. Her movements were fluid, predatory as she gracefully positioned herself on top of [mox]."
            pen "I'm going to have to administer the kiss of life~"
            "With clear experience, she slid her head between [mox]’s thighs, her face hovering tantalizingly close to [mox]’s pussy, still oozing with cum."
            mox "Woah! I think those are the wrong lips, lady!"
            "Her breath was warm and soft against [mox]’s inner thighs, and I could see [mox]’s fur standing on end in anticipation."
            mox "Ahhh, someone’s eage- ooohh!"
            "[pen]’s tongue emerged from between her lips, teasingly tracing delicate patterns across [mox]’s folds, lapping away at the thick cum. The soft, wet warmth of [pen]’s tongue elicited a shudder from [mox], her back arching slightly off the bed."
            "The contrast between [pen]'s gentle loving compared to my raw intensity was beautiful, yet I could still see the pleasure building in [mox]’s eyes. It didn’t take her long to join in, her tongue beginning to lap at [pen]’s juicy, swollen clit."
            "While watching, I could no longer contain the urgent need that had been simmering beneath the surface. My cock was locked and loaded, ready to go again. My gaze aimed squarely onto [pen]’s exposed ass. I moved silently from behind."
            "[pen]’s curves were perfect as they arched over [mox]’s body. I took a moment to brush my fingers down her sides before I reached for my cock and angled it in position. I realized that [mox] was keenly watching my every movement, eagerly anticipating the insertion."
            play ambience1 sex
            play sound2 cum
            play moans1 moansmisc4
            show pen2c v1 with d
            "With a slow, deliberate push, I entered [pen]. The sensation of her insides enveloping was deeply satisfying, and I began thrusting immediately. My cock stretched out [pen]’s pussy mere inches from [mox]’s face, my balls even occasionally brushing against her hair (and yes, I did avoid the horn)."
            pen "Hooohhh, finally… I really needed that~ Fuck me hard, [penmc]."
            mox "Mmphh, mhh… What a gorgeous view~" 
            "The rhythm of my thrusts was steady, deliberate. [pen] moans were muffled, her attention divided between pleasuring [mox] and the relentless thrusts that I administered from behind. Despite that, her body would still push back, striving to move in time with my thrusts in order to extract as much pleasure as possible."
            "The room was alive with the sounds of our passion—the wet, rhythmic slap of flesh against flesh, the gasps and moans that mingled with the hum of our shared intensity. Louder, and louder yet, echoing against the wooden walls of the treehouse."
            "As we continued, the boundaries of our selves seemed to blur into one single entity of sensation and need. The lines between pleasure and pain, between control and surrender, became indistinguishable. Every thrust, every touch, and every moan were testaments to the powerful, almost hypnotic pull of our primal instincts."
            play sound2 cum 
            show pen2c c2 v2 e1 with c
            play sound2 cum 
            with c
            "The climax, when it came, was a shared eruption of intensity. [pen]’s body tensed around me, her moans mingling with [mox]’s cries as our release mingled in a torrent of raw, unfiltered ecstasy. The final waves of pleasure left us all breathless, our bodies collapsing together in a tangled, sweaty heap on the bed."
            play sound2 cum 
            with c
            play sound2 cum 
            with c 
            stop music fadeout 1
            call stopbgs from _call_stopbgs_35
            call camerareset1 from _call_camerareset1_13
            "For the first time in almost ten minutes, the room was quiet, save for the sound of… incoming stomping?!"
            play sound2 move1
            scene bg bedroom2
            show night:
                blend "multiply"
                alpha 0.66
            show lil angry blush:
                xalign 0.25
            with d
            "Suddenly, the door flung open, and a familiar figure stood proud in the doorway, her silhouette framed by the intense light of the hallway."
            "[lil], her expression curious and exasperated."
            lil "Do I really have to listen to you the entire time?! You guys are so loud!"
            "The three of us just sat on the bed like puppies being told off."
            show lil raised with d
            lil "I can’t believe how long you’ve been at it... without… without inviting me!"
            "[pen], [mox] and I exchanged quizzical glances before turning towards me with sudden realization. The idea of [lil] joining us had never crossed our minds, but now that she had voiced it, the room seemed to pulse with a renewed sense of life."
            "[pen] was the first to recover and rise, the mischievous smile she started this session once again curling around her lips as she beckoned [lil] closer."
            show pen horny blush cum with d:
                xalign 0.75
            pen "Well, [lil]… If you think you can really handle us, why don’t you join in? There’s always room for one more~"
            "[lil] gulped, then nodded. Her curiosity and desire won out over any lingering reservations. She approached the bed, her eyes scanning over our glistening cum, taking in the evidence of our recent exploits."
            pen "[mox], [lil], turn around and present yourselves to [penmc]."
            layeredimage pen2d:
                always:
                    "penelope2dbg"
                group lily:
                    attribute always:
                        "penelope2dlilb [lilb]"
                group mox:
                    attribute always:
                        "penelope2dmoxb [moxb]"
                group pen:
                    attribute always:
                        "penelope2dpenb [penb]"
                if petplay == 1:
                    "penelope2dcollar"
                group leyes:
                    attribute l1:
                        "penelope2dlile1 [lilb]"
                    attribute l2:
                        "penelope2dlile2"
                    attribute l3:
                        "penelope2dlile3 [lilb]"
                group meyes:
                    attribute m1:
                        "penelope2dmoxe1"
                    attribute m2:
                        "penelope2dmoxe2"
                    attribute m3:
                        "penelope2dmoxe3"
                group peyes: #hehe pies
                    attribute p1:
                        "penelope2dpene1 [penb]"
                    attribute p2:
                        "penelope2dpene2 [penb]"
                    attribute p3:
                        "penelope2dpene3 [penb]"
                group cum1:
                    attribute c1:
                        "penelope2dc1"
                group cum2:
                    attribute c2:
                        "penelope2dc2"
                group cum3:
                    attribute c3:
                        "penelope2dc3"
                group sex1:
                    attribute s1:
                        "penelope2dsex 1"
                    attribute s3:
                        "penelope2dsex 3"
                group sex2:
                    attribute s2:
                        "penelope2dsex 2"
                    attribute s4:
                        "penelope2dsex 4"
            play moans1 moansmisc2
            play moans2 moansmisc3
            play music sextheme2
            call camerabreath from _call_camerabreath_51
            show pen2d always l1 m1 p1 c1 
            $ textbox = 2
            with d
            "Commanding and confidence, [pen] had taken charge once more, and the other girls complied without hesitation. With their flanks now tantalizingly presented, it was enough to reignite even a dying star, and my cock found itself swelling up once again."
            play sound2 magic1
            with p
            "[pen]’s hands caressed each flank, her touch both soothing and stimulating for the girls. There was a faint fizzle of magic at her horn, and I found myself miraculously invigorated."
            pen "{i}Pant, pant{/i} That’s a little magic to pep you up. Let’s make this a finale to remember~"
            "I moved in behind [lil] first, my hands gliding over her smooth fur, feeling the heat radiating from her."
            mc "You couldn’t resist, could you?"
            lil "Resist you? Hehe, not a chance…"
            mox "My, my. And you think you know someone? Let’s see what you’ve got, purple butt."
            play sound2 cum
            show pen2d s1 l2 m2 p2 with d
            play ambience1 sex 
            play moans1 moansmisc4
            "I pressed my tip against her entrance and pushed inside, our connection sending sparks of pleasure through both of us. She was dripping wet already, so I wasted no time thrusting."
            pen "Goodness me, you’re absolutely soaked~ And judging by how easily [penmc]’s cock slid in, you’ve already been playing with yourself, haven’t you? Fuhuhu. Just how long were you listening in?"
            lil "Aaahh.. Haahhh… Y-Yeah… I was listening the entire time…"
            "[pen]’s hands never left [lil]’s body, spreading, rubbing, and teasing, amplifying the pleasure until it became almost unbearable. [lil]’s moans grew louder, and each thrust pushed us both closer to the edge." 
            pen "Mmmhh… Cum for us~"
            play sound2 cum
            show pen2d s2 c2 with c
            play sound2 cum
            with c
            "With one last thrust, I reached my third climax, pouring fresh hot cum straight into [lil]’s needy pussy. The rush of pleasure she gained from being filled was enough to push her over the edge too."
            stop ambience1 fadeout 3
            play moans1 moansmisc2
            show pen2d -s2 -s1 l1 m1 p1 with d
            "But the night was not over yet. As I withdrew from [lil], [pen] guided me back towards [mox], her eyes gleaming with anticipation."
            mox "I get two turns? Lucky me!"
            "I positioned myself behind her, my cock managing to squeeze out one last erection at the promise of more pleasure."
            pen "Are you ready?"
            mox "Pfft, I’m always ready."
            play sound2 cum
            show pen2d s3 l3 m3 p3 with d
            play ambience1 sex 
            play moans1 moansmisc4
            "Slipping inside, [mox]’s body welcomed me with a familiar warmth, her moans echoing as I thrust deep inside."
            pen "Ooohhh, there you go. Fuck all that heat away."
            "Despite the building fatigue, our movements were laced with passion, a dance of desire firmly focused on reaching climax." 
            pen "Can you believe these two slutty mares were virgins only [day] days ago? Now look at how finely their pussy lips grip around your thick cock, mmmhh..."
            "[pen]’s greedy hands wasted no time slipping beneath the action and rubbing [mox]’s clit, her voice a soothing murmur that spurred us on. Judging by [lil]’s moans too, it seems [pen] was still rubbing her clit too!"
            pen "Although... I never expected you to open up like this, [lil], it almost feels weird."
            lil "Aahhh, ngghh… Weird? As if you didn’t always ask me."
            pen "Of course, you’re cute as a button! I've love to wear your thighs like earmuffs. What I never expected is for you to actually say yes."
            lil "Mmmhh… This isn’t me saying yes; we all know why we’re here tonight."
            "As the final moments approached, the room was filled with the sounds of our collective passion—a symphony of moans, gasps, and the rhythmic slap of flesh against flesh. With one last, explosive thrust, I reached my climax."
            play sound2 cum
            show pen2d s4 c3 l2 with c
            play sound2 cum
            with c
            mox "Uooohhhh! I’m cumming agaaaaiinn!"
            play sound2 cum
            with c
            play sound2 cum
            with c
            lil "Nnghhh, me too!"
            show pen2d p2 with c
            pen "Fuhuhu, I can’t believe I made [lil] cum~"
            stop music fadeout 3
            call stopbgs from _call_stopbgs_36
            scene bg bedroom2
            show night:
                blend "multiply"
                alpha 0.66
            with d
            "In the end, we fell onto the bed, a tangled heap of sated bodies and lingering touches. The room was heavy with the scent of sex."
            play music comical
            show lil happy cum:
                ypos 1080 xalign 0
                linear 0.8 ypos 500
            call camerareset1 from _call_camerareset1_14
            with d
            lil "Aaahhhh… That was exactly what I needed… I’m so glad I caved into my deserves and came."
            "I nodded, too exhausted to speak, but my thoughts echoed her sentiment. It was heartening to see [lil] shed her inhibitions so dramatically, even if it was driven by raw, unfiltered desire."
            show mox happy cum:
                ypos 1080 xalign 0.5
                linear 0.8 ypos 500
            with d
            mox "I didn’t think you had it in ya, [lil]. You always seemed a bit uptight to me."
            show lil awkward with d
            lil "You were right… I was ‘uptight’ and had locked myself away for too long. But now I’m trying to be more open."
            show mox laughing with d
            mox "Well, I like this new upbeat attitude! You’re always welcome to join in the fun."
            show lil happy with d
            lil "Really? You’d forgive me that easily? I haven’t even apologized for disrespecting your craft."
            show mox neutral with d
            mox "Eh, why shouldn’t I forgive you? Everyone’s entitled to their own opinions. As long as you’re not rude about it, that’s fine with me."
            show lil neutral with d
            lil "Mmh… But I do genuinely admire magical theatre. I was just being stubbornly blind to its merits."
            show mox smug with d
            mox "I wonder if you really mean that?"
            show pen laughing:
                ypos 1080 xalign 0.99
                linear 0.8 ypos 500
            with d
            pen "Heh, she can see right through you, [lil]. Tell her what you’re really feeling."
            show lil bashful with d
            lil "Ahh… It’s {i}not entirely{/i} my current opinion. B-But I want to be able to like and respect it, to see the good in things. That’s the kind of person I want to become."
            show mox laughing with d
            mox "I respect that… and I get it too. I used to be a pretty toxic person myself, and it took a lot of time and growth to get better. I’d suggest you take it one step at a time, but… then again, you leaped into this headfirst."
            show mox wink with d
            mox "But I can’t imagine that orgies are going to be your usual strategy for growth, so good luck!"
            show lil horny with d
            lil "Hehe, {i}(they might be){/i}, thank you! It’s actually past my usual bedtime, so I’m going to bow out of this wild ride before you decide to go another round."
            show pen bashful with d
            pen "I wouldn’t worry about that. We were exhausted {i}before{/i} you stormed in."
            show lil laughing with d
            lil "Oopsie~ Goodnight, girls, and a special goodnight to you, handsome."
            play sound2 move
            hide lil with d
            "[lil] planted a quick peck on my cheek before she left, her steps light and bouncy as she disappeared."
        "{i}Decline{/i}":
            mc "Sorry, ladies. I’m afraid the wine’s taken its toll, and mini-me’s out of energy."
            show pen2b pe2 with d
            pen "Bah, humph. Who’s been tiring him out?"
            show pen2b me2 with d
            mox "Ahaha, that may be my fault…"
            stop music fadeout 3
            call stopbgs from _call_stopbgs_37
            scene black 
            call camerareset1 from _call_camerareset1_15
            with d
            "We drank and chatted the night away. Even without the added heat of passion, it was still a wonderful time that lasted long after the wine had run dry."
    stop music fadeout 3
    play ambience1 night
    scene bg peneloperoom 
    show mox happy:
        xalign 0.25
    show pen happy:
        xalign 0.75
    $ textbox = 1
    with d
    mox "Well, it’s getting quite late, and… I’m absolutely wiped out. Shall we call it a night?"
    show pen laughing with d
    pen "Yeah, I need to be up at the ass crack of dawn to start working on a report. Goodnight, you two."
    mc "Thanks for inviting us over. Sleep well!"
    scene black with d
    "With that, [mox] and I slipped back to the apartment. We crawled into bed, our bodies grateful for the embrace of the sheets."
    if replay == 1:
        return
    $ magicroute3 = 1
    $ magiccompletion += 1
    $ completion += 1
    jump newday
    jump newday
