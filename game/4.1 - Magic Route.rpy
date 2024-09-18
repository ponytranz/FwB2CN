label treehouse:
    hide screen worldmap
    play music lilytheme fadein 1
    scene bg library
    with d
    menu treehousemenu:
        "Visit [lil]":
            scene bg lilybedroom 
            show night:
                alpha 0.75
                blend "multiply"
            show lil happy
            with d
            if magicroute1 == 0:
                lil "Good evening. I have your city pass somewhere around here."
            if magicroute2 == 0:
                show lil blush with d
                lil "Mmhh... You're back..."
            else:
                lil "Good evening. It's nice to see you."
            menu lilmenu:
                "Where's [lil] 2.0? (In Development)" if magicroute1 == 1 and magicroute2 == 0:
                    jump lilmenu
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
                            scene bg lilybedroom 
                            show night:
                                alpha 0.75
                                blend "multiply"
                            show lil happy
                            $ textbox = 1
                            with d
                            play music lilytheme
                        "Double Handjob" if energy > 0:
                            call lildoublehandjob from _call_lildoublehandjob
                            scene bg lilybedroom 
                            show night:
                                alpha 0.75
                                blend "multiply"
                            show lil happy
                            $ textbox = 1
                            with d
                            play music lilytheme
                        "Selfcest Threesome (In Development - Planned for 0.3)" if energy > 0:
                            "The reason this scene is in development, is because [lil] is currently a virgin, and this scene will have additional sex variants once she's lost her virginity."
                            jump lilsexmenu
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
            if petplay == 1:
                show pen collar
            with d
            pen "Hiya! Thanks for popping by!"
            menu penmenu:
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
                        "Pet-Play Boobjob" if energy > 0:
                            call penboobjob from _call_penboobjob
                        "Tied-Up From Behind" if energy > 0:
                            call penfrombehind from _call_penfrombehind
                        "Back":
                            show pen happy with d
                            pen "Meh!"
                    jump penmenu
                "Back":
                    play music lilytheme fadein 1
                    scene bg library with d
                "Leave":
                    jump worldmap
        "Replay Events":
            menu:
                "While replaying, you can return at any time using the phone."
                "Treehouse Visit 1":
                    $ replay = 1
                    show screen vnui
                    scene bg lilybedroom 
                    show night:
                        alpha 0.75
                        blend "multiply"
                    call magic1 from _call_magic1 
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
                        "lily2cgoth" 
                group gotheyes:
                    attribute g1:
                        "lily2cgoth 1" 
                    attribute g2:
                        "lily2cgoth 1" 
                    attribute g3:
                        "lily2cgoth 3" 
                group legwear:
                    attribute l1:
                        "lily2clingerie 1"
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
                group cum:
                    attribute cum:
                        "lily2ccum"
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
            "Without another word, I plunged myself deep inside the clone’s tight entrance, groaning deeply as I tore through her folds and took her virginity. The sound of her resulting, impassioned moan, echoed through the room, reverberating through both of us, and it was sublime."
            "The clone’s body arched upwards, her back curving beautifully as she let out a high-pitched whine of pleasure mixed with pain."
            "[lil]’s eyes flew open at the sight before her – the sight of me pounding my cock into her clone’s tight pussy – she felt herself growing wetter by the second. She bit down harder on her lip, trying desperately not to whimper in need as she felt every powerful thrust indirectly pressed against her by her clone."
            "It was torture – exquisite torture – and she couldn’t tear her eyes away from the display unfolding before her." 
            mc "Ooohhh, your pussy is so tight, [lil]!"
            lil2 "Mmphhhh, this is the best feeling ever!"
            "The clone moaned my name over and over again, fingers digging into the sheets beside [lil] as she met each brutal thrust with equal ferocity – her body moving in perfect sync with mine. It was beautiful chaos – an erotic dance purely fueled by lust and desire - and [lil] felt herself slipping further into the depths of depravity with each passing moment."
            "She couldn’t take it anymore – she couldn’t just lie there and watch them – and without even thinking about it, she reached down between her legs, finding her own wet folds deeply slick with need. Her fingers brushed against her clit, teasingly circling around the sensitive nub before finally plunging inside her tight entrance."
            "She gasped at the sensation – it wasn’t nearly enough – but it helped quell some of the burning desire threatening to consume her entirely."
            "As if sensing her need, the clone glanced over at her – eyes half-lidded with pleasure – and gave her a sultry smile, before returning her attention back to me."
            lil2 "Ooohhh, [lil]… I want you to watch… I want you to see how good he makes me feel."
            "And feel good, she did – her body arching off the bed as wave after wave of pleasure coursed through her – her walls clenching tightly around me as she approached orgasm. The sight of them – her clone experiencing such raw ecstasy while she lay there, helplessly aroused but still untouched—was almost too much for [lil] to bear."
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
            show lil2c e3 cum -v2a 
            call camerareset from _call_camerareset_7
            call stopbgs from _call_stopbgs_23
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
                pen "Luckily, you’ve been a reliable source of what I’ve needed all these years, so I’ve managed to keep it under control this season."
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
    "Her words sent a thrill through me. Was this dignified mare offering really herself up as a pet? She certainly has the libido to back it up. Handing me the collar, the decision is left up to me."
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
            mc "I’d love to"
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
            "I finished tying her up, making sure the knots were secure. She was completely at my mercy, and the sight of her bound and helpless sent a surge of desire through me."
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
