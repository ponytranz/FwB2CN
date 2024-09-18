label brothel:
    hide screen worldmap
    show screen vnui
    if brothelroute1 == 0:
        jump brothel1
    play music clubtheme fadein 1
    scene bg brothel1
    with d
    menu brothelmenu:
        "Work (Ask [rub] for an Interview)" if brothelroute2 == 0:
            menu:
                "(Go to [rub] now?)":
                    show black
                    show bg brothel5
                    with d
                    jump brothel2
                "(Back)":
                    jump brothelmenu
        "Work" if brothelroute2 == 1:
            jump brothelwork
        "Choose a Hostess":
            menu hostessmenu:
                "Grey Mare" if clairenamed == 0:
                    show cla happy with d
                    $ clairenamed = 1
                    menu:
                        "I think I recognize her. What was her name?"
                        "Default: Claire":
                            $ claire = "Claire"
                        "Custom":
                            $ claire = renpy.input("What was her name?")
                            if claire == "":
                                $ claire= "Claire"
                            $ claire = claire.strip()
                    jump bclaire
                "[cla]" if clairenamed == 1:
                    label bclaire:
                        show cla happy with d
                    if bclairemet == 0:
                        $ bclairemet = 1
                        "A grey mare of elegant stature stood behind a polished counter, tuning a large cello. I'd often see her waiting here for her next customer."
                        "Her long mane cascaded down her back like silk, accentuating her figure. One look at her was all you needed to know to realize why she's the most expensive and sought after hostess at this club."
                        "However, within the club, the fact [cla] only performs music in her private booth is a well known."
                        "Yet I can't help but wonder... has anyone else in the club actually confirmed that? With wealthy clients like hers, anything could be happening in those booths. They're sound proof after all."
                        "She begins to play, while most of the sound is snuffed out by the club music, I manage to catch the hints of a melody."
                        mc "That's some beautiful music you're playing." 
                        show cla wink with d
                        if event3 == 1:
                            cla "Why thank you, it's always a pleasure to play for an apprecative audience. Especially the hero that rescued my purse~"
                        else:
                            cla "Why thank you, it's always a pleasure to play for an apprecative audience."
                        mc "You say that like your usual audience doesn't appreciate it."
                        show cla happy2 with d
                        cla "Mmh... My clients? Not as much these days..."
                        "(Isn't that what they're paying for?)"
                        show cla happy with d
                        if event3 == 1:
                            cla "Are you working today?"
                        else:
                            cla "You're the new host here, right?" 
                        mc "Tonight, I'm just a customer. Mind if I join you?"
                        show cla horny with d
                        cla "A host playing the role of a customer? How novel. Please, have a seat."
                        "I slide onto the seat beside her, the close proximity allowing me to catch the faint scent of her perfume." 
                        mc "You have quite the reputation around here."
                        show cla wink with d
                        cla "Oh? And what reputation might that be?"
                        mc "Your performances... they can be quite expensive. You're the only lady here that doesn't have a price sheet."
                        mc "And let's just say I operate on a 'if it doesn't have a price tag, it's too expensive' policy."
                        mc "What's the catch? It's just a music performance, right? Even in this brothel of intellectual and physical pleasures, it does seem a little... out of place."
                        show cla horny with d
                        cla "Well, music is a form of intimacy, don't you think? It's all about connecting with the audience on a deeper level."
                        cla "The expense is part of the experience. I'm offering something grand and personal. The fact that only a few may experience it is part of that experience." 
                        mc "That, I get... But I have a feeling that you may be connecting with your clients on an even deeper level than that..."
                        "[cla] turns away, but her eyes twinkle with amusement."
                        show cla happy with d
                        cla "Well... That would depend on how deep they're willing to go in their coffers; how much they're willing to offer for such an experience." 
                        mc "I knew it... You're offering... something that's hard to even describe."
                        mc "The privacy itself is part of the appeal. You have to pretend it's only music."
                        show cla wink with d
                        cla "You're very bold, aren't you? But tell me. What exactly do you think my performance is?" 
                        "In my other world, I knew two mares that looked like this, identical twins. And while I know [cla] was the music teacher in the last world, there's always a chance that she's more like the masseuse that exchanged money for sex in this world."
                        "And if that's the case, if she enjoyed being a prostitute in that wholesome world, then it shouldn't be a surprise at all to see her turn to such a career in this harsher world."
                        mc "You pretend you're only there to play music, but what you're really doing is pretending you're not there for sex."
                        mc "The idea is to make you feel earned and personal. Perhaps by pretending you were seduced, or got so drunk that you couldn't resist." 
                        mc "Which is why the price and reputation that you {i}only{/i} play music is so important. It makes you elusive and mysterious."
                        show cla horny blush with d
                        cla "My, my, aren't you quite the detective? But you'll never get an answer from me. The only way to confirm your suspicion is to join me."
                        mc "And I imagine such a thing would be... prohibitively expensive."
                        show cla happy with d
                        cla "For an experience as exclusive as the one you're describing... Shouldn't it be? But, for a charming new colleague like yourself, I might consider... an introductory offer."
                        mc "An introductory offer, huh? How generous of you."
                        show cla wink with d
                        if event3 == 1:
                            cla "Consider it a thank you for returning my ba."
                        cla "I'll be waiting."
                    if clairenamefix == 0:
                        $ clairenamefix = 1
                        "(Hey, in the last update [cla]'s renaming didn't work. Would you like to rename her again?)"
                        menu:
                            "Default: Claire":
                                $ claire = "Claire"
                            "Custom":
                                $ claire = renpy.input("What was her name?")
                                if claire == "":
                                    $ claire= "Claire"
                                $ claire = claire.strip()
                    menu clairemenu:
                        "Pay for [cla]'s services $400" if event3 != 1 and cla1 == 0:
                            if money >= 400:
                                $ money -= 400
                                call cla1 from _call_cla1
                                jump brothel
                            else:
                                "Not enough monies!"
                                jump clairemenu
                        "Pay for [cla]'s services $100" if event3 == 1 or cla1 == 1:
                            if money >= 100:
                                $ money -= 100
                                call cla1 from _call_cla1_1
                                jump brothel
                            else:
                                "Not enough monies!"
                                jump clairemenu
                        "Back":
                            hide cla with d
                            jump brothelmenu
                "Dog Girl" if rosanamed == 0:
                    show ros happy
                    with d
                    if rosanamed == 0:
                        $ rosanamed = 1
                        menu:
                            "I think I recognize her. What was her name?"
                            "Default: Rosa":
                                $ rosa = "Rosa"
                            "Custom":
                                $ rosa = renpy.input("What was her name?")
                                if rosa == "":
                                    $ rosa= "Rosa"
                                $ rosa = rosa.strip()
                    jump brosa
                "[ros]" if rosanamed == 1:
                    if rosbusy == 2:
                        "You saw [ros] and a stallion head into the private booths section together..."
                        "As you step near, loud moans can be heard."
                        play sound2 cum
                        show secretrosa 1 with c
                        play sound2 cum 
                        with c
                        ros "I'm cumming! I'm cumming!"
                        "Looks like she couldn't handle the heat; now she's getting her pussy pounded by that giant horsecock."
                        show secretrosa 2 with d
                        ros "Ooohhh, you filled me up with so much! It feels so warm in my belly..." 
                        "Guess I'll have to come back tomorrow if I want to see her."
                        hide secretrosa with d
                        jump hostessmenu
                    label brosa:
                        show ros happy with d
                    if brosamet == 0:
                        $ brosamet = 1
                        "My eyes land on [ros] - who I assume is a shih tzu dog girl with fluffy ears and an infectious smile that lights up her entire face."
                        "I make my way over. She notices me and her tail already begins to wag."
                        mc "Good evening, [ros]. Mind if I join you?"
                        show ros laughing with d
                        if event2 == 1:
                            ros "Ooohh, I can't believe my savior is really working here! The wheel you fixed has been working a treat!"
                            ros "Please, take a seat! If you have any questions about hosting, you only need to ask."
                        else:
                            ros "Of course not! It's always nice to meet new friends. You just signed up as a host, right?"
                        "I slide into the seat next to her, feeling an immediate warmth from her fur so close to my skin."
                        mc "While I have just started working as a host, tonight, I thought I'd experience the club as a customer."
                        show ros happy with d
                        ros "In that case... Welcome! I'm [ros]! It's wonderful to meet you! How are you finding things so far?"
                        "Her cadence is almost filled with overwhelming warmth and kindness. If it wasn't so sincere, it'd almost be too much."
                        mc "This club is an interesting experience to say the least. Everyone offers a unique experience, right? I heard you're intended to be a sort of 'affectionate' host."
                        "She blushes slightly, ears twitching."
                        show ros laughing with d
                        ros "I think that's just in my blood as a dog girl. I can't help but want to make everyone feel welcomed and cared for. I feel such joy in spreading happiness! Uuuu, it almost makes my heart want to burst!"
                        mc "I can't help but imagine most people are into it for... other reasons."
                        show ros neutral with d
                        ros "You mean the lewd parts? {i}Sigh{/i} I know... I get propositions all the time, and they act confused when I refuse them."
                        ros "They say things along the lines of 'but you were having such a good time until now!'. As if my enjoyment and happiness somehow manifested into sexual desire."
                        ros "I just don't feel comfortable with selling myself like that. I'd rather focus on being affectionate and making people feel good in other ways."
                        mc "I respect that. Everyone has their boundaries."
                        if event2 == 1:
                            show ros horny with d
                            ros "But... That doesn't really apply to you, does it? We've already... you know."
                            mc "I won't soon forget it either."
                            show ros neutral with d
                        else:
                            show ros neutral with d
                            ros "But... I have to admit, it's hard some days."
                        ros "I go into heat like most other girls here, and this year is ruff!"
                        ros "Host-to-host: the other day, I almost caved in with a stallion. If we weren't in the public area, I... Uuuu, so embarrassing... It's like I'm not myself."
                        show ros horny with d
                        rosa "I've been, uh... looking for someone to help deal with that."
                        show ros neutral with d
                        ros "Now I know what that sounds like, I've already asked another one of the boys here and they said no, so... If you want to refuse, that's okay."
                        "In this city, there's no shortage of horny girls to go around. They outnumber the men in a ratio of about 3:1. Ironically, despite working as a hostess, it's hard for her to find her own relief outside of work."
                        "That said, there are still plenty of horny strangers willing to take advantage of a dog girl in heat this time of year. A trusted friend would be a much better outlet for her needs."
                        menu:
                            "I'll help ([rosa] will become loyal to you)":
                                mc "You can count on me!"
                                show ros laughing with d
                                ros "Aahhh... Thank you, thank you, thank you! I feel calmer already."
                            "Sorry, my hands are full ([rosa] will slip and start regularly fucking clients)":
                                show ros neutral with d
                                ros "Nuuu... But it's so bad today!"
                                "A stallion steps up to the table and makes eye contact with [rosa]."
                                $ misc = "Customer"
                                misc "Hey, [rosa]! Sorry about being pushy last time, can I make it up to you with a drink?"
                                show ros horny with d
                                ros "Uuuu, gotta go, [mc]!"
                                $ rosbusy = 2
                                hide ros with d
                                "Uh oh, I recognize that glint in her eyes. Maybe I should check up on her."
                                jump brothelmenu
                    menu rosamenu:
                        "Missionary Quickie (Free)":
                            call rosmissionary from _call_rosmissionary
                            jump brothel
                        "Hire Professionally ($50)" if ros2 == 0:
                            if money >= 50:
                                $ money -= 50
                                call ros2 from _call_ros2
                                jump brothel
                            else:
                                "Not enough monies!"
                                jump rosamenu
                        "Hire Professionally ($12)" if ros2 == 1:
                            if money >= 12:
                                $ money -= 12
                                call ros2 from _call_ros2_1
                                jump brothel
                            else:
                                "Not enough monies!"
                                jump rosamenu
                        "Back":
                            hide ros with d
                            jump brothelmenu
                "[hil]":
                    scene bg brothel2 
                    show hil happy
                    with d
                    if bhildamet == 0:
                        $ bhildamet = 1
                        "As I walked towards [hil], I couldn’t help but feel a strange connection. Like her, I wasn’t originally from this world. We both have our own reasons for being here, both thrust into a life we hadn’t anticipated." 
                        mc "[hil], right? Mind if I join you?"
                        "She looked up, her piercing emerald eyes striking straight to the heart."
                        hil "Take a seat, new guy. [rub] told me a bit about you."
                        "I slid onto the bar stool next to her, signaling the bartender for a drink."
                        mc "Yeah, I started recently. [rub] mentioned we might have some things in common."
                        show hil wink with d
                        hil "Oh? And what might those be?"
                        mc "Your crash landing sounds like quite a story. Surely such a thing is an insane revelation for a planet-bound civilization?"
                        "She chuckled softly, taking a sip of her drink."
                        show hil bashful with d
                        hil "You could say that. But not many people believe me when I tell them I’m from another planet. They just think it’s part of the ‘mysterious adventurer’ act."
                        mc "I believe you. I know what it’s like to end up somewhere you didn’t plan on being. I guess you could say, I know what it’s like to be trapped away from home."
                        show hil happy with d
                        hil "Trapped? So, what’s your story then?"
                        "I give her the footnotes of my experience. Having already explained this a few times already, I’ve gotten pretty efficient at it."
                        mc "It’s a strange feeling, isn’t it? Being so far from home, not knowing if you’ll ever see it again."
                        show hil awkward with d
                        hil "It is. But we adapt. We find ways to survive."
                        show hil bashful with d
                        "Her smile turned bittersweet, and she looked down at her drink."
                        show hil neutral with d
                        hil "That’s exactly what I did. When I first started here, it was just for the money. I needed to survive. But over time, I… well, I found a new kind of life here."
                        mc "Do you ever wish you could go back?"
                        show hil awkward with d
                        hil "{i}She sighs, her ears drooping slightly{/i} Sometimes. But then I think about the life I’ve built here. The friends I’ve made. It’s not perfect, but it’s mine."
                        mc "I get it. I really do. It’s hard to know what you want when your past and present are so tangled up. It can be hard to even know who you are sometimes, and it’s scary how easy it can be to forget your past life."
                        show hil happy with d
                        hil "It’s nice to have someone who understands, but… you said ‘trapped’ earlier. I wouldn’t use that word."
                        hil "I’ve given up trying to repair my ship. It won’t happen in this lifetime. I’ve had to accept that this is just another stage of my life. We all go through stages as we age, through school, then higher education, then work."
                        hil "That people we once knew get left behind, but we persist; we forge ahead, meeting new people and building new connections."
                        hil "I realized that if I spent my entire life focusing longing for my previous life, it wouldn’t be living at all. If anything, that’s being trapped."
                        mc "Shiiiit… You’ve got me dead to rights there… I also can’t stop thinking about ‘home’."
                        "[hil] reaches out and touches my shoulder."
                        show hil wink with d
                        hil "Hey… Look around you! This building is practically a temple dedicated to worshipping the moment. Here, people forget their troubles. No egos, no expectations; this is just an environment that reminds you what it means to be alive."
                        hil "We all get so caught up in our struggles, work, and drama that we forget that we’re just animals in an incomprehensibly large universe."
                        show hil awkward with d
                        hil "If I didn’t find a place like this, where I could comfortably switch off my brain, well… honestly, I think I’d have gone crazy."
                        mc "These are some interesting ideas in theory. Easier said to put them into practice."
                        show hil laughing blush with d
                        hil "Hehe, well… I could show you my ideas in practice if you want, with a friendly discount."
                        mc "Oh? I think I’d like that a lot."
                        show hil happy with d
                        hil "Me too! I’m usually with female customers, but my tongue doesn’t discriminate~"
                        hil "My prices for penetration are more expensive, but my pussy is out of this world! {i}Wink{/i}"
                        "Despite the good points [hil] brought up, I can’t help but wonder if she took them too far and lost sight of herself in the pursuit of happiness."
                        "If I were her, I don’t think I’d ever stop thinking of my original planet. I don’t think I’d ever stop trying to fix my spaceship."
                        "And that’s not to say I wouldn’t try and make any friends and start a new life here, but… I don’t know. It’s a lot to unpack."
                        "In a way, I can understand what [rub] said about [hil]. ‘Corruption’, in a sense, [hil] been changed by her environment to such a degree that she’s become a different person since she crashes landed here."
                        "And perhaps it’s a person she never wanted to be, but the person she had to become just to cope with the trauma of being stuck here." 
                    menu hildamenu:
                        "Sex In Development":
                            jump hildamenu
                        "Back":
                            hide hil 
                            show bg brothel1
                            with d
                            jump brothelmenu
                "[bas]":
                    show bas neutral with d
                    if bbastetmet == 0:
                        "As I approached, I couldn’t shake the feeling I was stepping into a lion’s den. Her gaze met mine, cool and assessing, as if weighing my worth in a single glance."
                        mc "[bas], right? Mind if I join you?"
                        "She didn’t respond immediately, her eyes flicking back to a chessboard that was in front of her. After a moment, she gestured to the seat opposite her with a languid wave of her hand."
                        show bas awkward with d
                        bas "If you think you can keep up."
                        "I took a seat, feeling the weight of her scrutiny. The pieces on the board seemed to taunt me."
                        mc "[rub] told me you’re unbeaten at chess. But whether I win or lose, I'm honored to play against a princess." 
                        show bas bashful with d
                        "A faint smile curved her lips, a flicker of amusement in her eyes."
                        bas "[rub] speaks too freely. But yes, I’ve yet to find a worthy opponent. Let’s see if you’re any different."
                        if magicroute3 == 1:
                            "Even though my brief game with [pen] revealed that I might not know the rules for this universe’s version of chess, I decided to try anyway."
                        show bas neutral with d
                        "I studied the board, trying to anticipate her moves. She played with calculated grace, each piece moving with multi-layered purpose. As the game progressed, I found myself drawn into her world, the outside noise fading into a distant hum."
                        "There was something about her aloofness. There was more than just a chess game at stake, there was also a challenge to break through the icy façade she wore so effortlessly. Each move on the board felt like a step closer to understanding her."
                        "And then, just as I was about to move my knight…"
                        show bas wink with d
                        bas "No, not there."
                        mc "Is this a bad move?"
                        show bas happy with d
                        bas "If you finish that move, I’ll checkmate you in the next seven."
                        "Somewhere bewildered, I leaned back and observed the board… A forced checkmate in seven moves? Can she really see such a thing?"
                        mc "But… how? That’s… amazing. Better than amazing, actually."
                        show bas bashful with d
                        "Her eyes narrowed slightly, a glint of interest shining through."
                        show bas neutral with d
                        bas "Flattery won’t help you. Now, focus on your next move. If you think you’ve found a good move, stop, and find a better one."
                        "I nodded, determined to prove myself. The world around us shrinking as I was fully absorbed in our game, but also, her…"
                        show bas happy with d
                        "I started to notice the subtle shifts in her demeanor. The way her eyes twitched when she concentrated, the almost imperceptible softening of her expression."
                        "It sounded simple, it sounded silly, but... she was having fun!"
                        mc "You were a princess? That must have been quite a life."
                        show bas awkward with d
                        "A shadow passed over her features, her gaze growing distant. A touchy subject, perhaps?"
                        show bas neutral with d
                        bas "It was. But that life is gone. Here, I am simply [bas]."
                        mc "There’s nothing simple about the way you’re playing me on this board right now."
                        show bas happy with d
                        "Her smile returned, more genuine this time."
                        bas "Yes, I suppose. But even a ‘princess’ can appreciate a challenge."
                        "The game continued, each move a dance of strategy and wits. I could feel the tension building, but I couldn’t help but notice one of her moves wasn’t as aggressive as it could have been."
                        "Sure, there could have been plenty of things I couldn’t anticipate, but in that moment, I realized she was going easy on me. No, I don’t think that’s right; what she’s doing is testing me, pushing me to see how far I could go."
                        "With each move, I could feel myself rising to the challenge."
                        show bas satisfied with d
                        bas "You’re not bad. For a beginner."
                        mc "Hah! I’ll take that as a compliment."
                        "A few moves later, the game ended with a decisive checkmate. It’s like her victory was only ever a few moves away throughout the entire game."
                        show bas happy with d
                        "She leaned back, her expression softer, more approachable, and a hint of warmth in her eyes."
                        bas "You played well. Most people don’t care for the game. They’re just humoring me, thinking if they play, I’ll like them more."
                        show bas wink with d
                        bas "You can tell a lot by the moves someone makes. You were genuinely trying to beat me."
                        mc "Of course! Why wouldn't I try to win?"
                        show bas laughing with d
                        bas "Obviously, you are a man worth my time. Enough games. Let's talk."
                        "As the night wore on, we talked more, the chessboard forgotten. She found herself opening up to me, sharing stories of our past. Our journeys here to Arcadia. She listened, her aloofness giving way to genuine curiosity."
                        "Indeed, she was another kindred spirit. Someone who had been displaced and had to find a new path."
                        show bas happy with d
                        mc "We’re not so different after all, princess."
                        show bas bashful with d
                        bas "Maybe not. Welcome to the club."
                        "She opened one of the drawers that were on this table. They were filled with board games, but she reached for a subtle leaflet and handed it to me."
                        "It simply had a selection of acronyms and numbers next to them, such as ’BJ – 100’, ‘VP – 200’, along with others."
                        show bas happy blush with d
                        bas "I’m sure you can figure out what these are."
                        mc "Me? Are you sure?"
                        show bas wink with d
                        bas "Yes. But no employee discount~"
                        "I had passed the unspoken test, earning a place in her world. All because I took a genuine, earnest interest in her as a person, and saw her as more than just a lady of the night."
                    menu bastetmenu:
                        "Sex In Development":
                            jump bastetmenu
                        "Back":
                            hide bas with d
                            jump brothelmenu
                "Back":
                    jump brothelmenu
        "Visit [rub]":
            scene bg brothel5
            if rubbusy == 1:
                "Looks like [rub] isn't here right now. I think she's on a short vacation, and should be returning tomorrow."
                jump brothel
            show rub happy
            with d
            if brothelroute1 == 1 and brothelroute2 == 0:
                rub "It's lovely to see you. Are you here for that interview?"
            else:
                rub "It's lovely to see you, darling."
            menu rubmenu:
                "Interview" if brothelroute2 == 0:
                    jump brothel2
                "Sex":
                    show rub wink with d
                    rub "Oh my, you're going to take me right here?"
                    menu rubsexmenu:
                        "Energy: [energy]"
                        "No Energy Left" if energy <= 0:
                            "I feel exhausted!"
                            jump rubmenu
                        "Thighjob" if energy > 0:
                            call rubthighjob from _call_rubthighjob
                            scene bg brothel5
                            show rub happy
                            with d
                            $ textbox = 1
                        "Couch Missionary" if energy > 0:
                            call rubmissionary from _call_rubmissionary
                        "From Behind" if energy > 0 and brothelroute2 == 1:
                            call rubfrombehind from _call_rubfrombehind
                            scene bg brothel5
                            show rub happy
                            $ textbox = 1
                            call camerareset2 from _call_camerareset2_22
                            with d
                            play music clubtheme fadein 1
                        "Legs-Up" if energy > 0 and brothelroute2 == 1:
                            call rublegsup from _call_rublegsup
                            scene bg brothel5
                            show rub happy
                            $ textbox = 1
                            call camerareset2 from _call_camerareset2_23
                            with d
                            play music clubtheme fadein 1
                        "Back":
                            show rub happy with d
                            rub "As you wish."
                    jump rubmenu
                "Back":
                    scene bg brothel1 with d
                    jump brothelmenu
                "Leave":
                    jump worldmap
        "Visit [mel]" if brothelroute2 == 0 and brothelroute3 == 0 or brothelroute3 == 1:
            scene bg brothel2
            if melbusy == 1:
                "Looks like [mel] isn't here right now. I think she's on a short vacation, and should be returning tomorrow."
                jump brothel
            show mel happy
            with d
            if brothelroute1 == 1 and brothelroute2 == 0:
                mel "So you came crawling back. Are you here to take my sister's interview? I think you should, ehehe."
            else:
                mel "So you came crawling back."
            menu melmenu:
                "Sex":
                    show mel smug
                    mel "What makes you think I'd do something like that with you?"
                    menu melsexmenu:
                        "Energy: [energy]"
                        "No Energy Left" if energy <= 0:
                            "I feel exhausted!"
                            mel "Pft, I could have kept going."
                        "Booth Footjob" if energy > 0:
                            call melfootjob from _call_melfootjob
                        "Booth Blowjob" if energy > 0:
                            call melblowjob from _call_melblowjob
                        "Handjob/Leaning Forward Cowgirl" if energy > 0 and brothelroute2 == 1:
                            call melhandjob from _call_melhandjob
                        "Leaning Back Cowgirl" if energy > 0 and brothelroute3 == 1:
                            call melcowgirl from _call_melcowgirl
                        "Reverse Cowgirl" if energy > 0 and brothelroute3 == 1:
                            call melreversecowgirl from _call_melreversecowgirl
                        "From Behind" if energy > 0 and brothelroute3 == 1:
                            call melfrombehind from _call_melfrombehind
                        "Legs Up" if energy > 0 and brothelroute3 == 1:
                            call mellegsup from _call_mellegsup
                        "Back":
                            show mel happy with d
                            mel "Tch, I was joking."
                            jump melmenu
                    play music clubtheme
                    scene bg brothel2
                    show mel happy
                    with d
                    jump melmenu
                "Back":
                    scene bg brothel1 with d
                    jump brothelmenu
                "Leave":
                    jump worldmap
        "Check on [mel]" if brothelroute2 == 1 and brothelroute3 == 0 and melbusy == 0:
            jump brothel3
        "Replay Events":
            menu:
                "While replaying, you can return at any time using the phone."
                "Brothel Visit 1":
                    $ gen3 = 10
                    $ replay = 1
                    show screen vnui
                    call brothel1 from _call_brothel1
                    $ replay = 0 
                    jump brothel
                "Brothel Visit 2":
                    $ replay = 1
                    show screen vnui
                    call brothel2 from _call_brothel2
                    $ replay = 0 
                    jump brothel
                "Brothel Visit 3":
                    $ replay = 1
                    show screen vnui
                    call brothel3 from _call_brothel3
                    $ replay = 0 
                    jump brothel
                "Back":
                    jump brothelmenu
        "Leave":
            jump worldmap
    jump brothelmenu
label brothel1:
    show screen vnui
    play music citytheme
    play ambience2 city
    scene bg city1
    "A brothel, huh? I didn’t know what to expect, but it’s certainly no boutique."
    "If it was any reprieve, it was the same building situatated in the same location."
    "However, the walk there couldn't be more different. Instead of taking a stroll through a vibrant grassy field, I'm instead wandering through thriving, narrow alleys lined with neon signs and crowded with more people than during the day."
    "This seems to be an entertainment district of sorts, the type where elegant, expensive bars are besides sleazy 'massage' parlours, each business likely boosting the other's."
    "Deep inside this district was [rub]'s home. The opulent building, even in this reality, somehow manages to tower over the others around it. A tribute to the sheer magnitude of success [rub] is experiencing with this business venture."
    "And since it was already night, this place was open, with the faint hum of music growing louder as I approached."
    "There’s a queue of a handful of mares at the door, each one approaching the bouncer and taking an ID out of their bags – oh fuck!"
    "When it’s my turn, the bouncer refuses to let me in, although she seems a little conflicted."
    show silhouette2 with d:
        xalign 0.25
    $ misc = "Bouncer"
    misc "I don't even know what species you are, man. How am I supposed to tell if you're over 18?"
    mc "But, uhm… I'm not a customer—I’m just here to see [rub] and [mel]."
    misc "If you had a meeting with the madam, you wouldn’t be coming in through the front door." 
    "However, it seems our fuss caught the attention of a special someone."
    $ gen1 = 11
    if default == 0 and gen3 != 10:
        call screen characterchoice
        $ melb = gen2
    play music melodytheme
    show mel happy with d:
        xalign 0.75
    "It’s alright, Julie. This one’s with me."
    mc "Ah—it’s you!"
    if default == 0 and gen3 != 10:
        menu:
            "What was her name?"
            "Default: Melody":
                $ melody = "Melody"
            "Custom":
                $ melody = renpy.input("What was her name?")
                if melody == "":
                    $ melody= "Melody"
                $ melody = melody.strip()
    show mel laughing with d
    mel "Heh, get in here, weirdo."
    scene bg city1 with d
    "The bouncer steps aside politely and gestures for me to enter, where I follow [mel]’s swishing tail deeper inside through a corridor of alternating light and darkness."
    show bg brothel1 with d
    "Once inside, the interior is absolutely not what I expected. It’s a large, hollow building with a ton of mares sipping wine and making conversation. I’m pretty sure I spot some people playing chess over there."
    "It seems like this is an establishment where you sit down, and host or hostess joins and drinks with you."
    "The music is light and classy, allowing for conversation, which is exactly the kind of vibe I prefer." 
    "There’re a handful of stallions and even other species of males in sight—notably a minotaur and a dragon. For once, this isn’t an area where my unusual appearance and the fact I’m a man command a lot of attention and glances." 
    show mel smug with d:
        xalign 0.5
    mel "Gross! Stop ogling the ladies! I thought you weren’t a customer."
    mc "I really wasn’t expecting… this…"
    show mel happy with d
    mel "Quite the shitshow, eh? Oh, and before you get any perverted ideas, I don’t work here."
    "She's music to my ears — [mel] hasn’t changed a bit."
    show mel neutral with d
    mel "You wanted to see me? I’d remember someone who looked so… hairless."
    "Under the light, [mel] looks me up and down."
    show mel smug with d
    mc "Yeah – well, uh…"
    "Now that I'm here, I'm at a loss for words. I can't just tell her I'm from another universe—it’d be exhausting to explain and prove every time."
    "But beyond being friends in the other universe, I don't have anything to offer or say to [mel] here. I have to accept that we’re strangers and treat our relationship accordingly to avoid coming across as—"
    show mel death with d
    mel "Creepy! The way you're staring at me is creepy! Being nude is socially acceptable and you're still making me want to cover up. Although, damn, you should cover up first, worm lookin' ass."
    mc "Ah—Wha?"
    show mel laughing with d
    mel "Hehe, did you really just throb down there? Don’t tell me you’re one of those perverts who gets off when they're bullied?"
    mel "Joke's on you. I'm not remotely attracted to whatever you are. Your worm wouldn't even be worth my feet, let alone my mouth. Hehehe."
    mc "Hey, why the hell would I get excited by your flat chest?"
    mc "Get outta here. If you’re going to roast me, at least don’t project your delusions in with it."
    show mel angry with d
    mel "What?! Who cares about fat, flabby tits! I have a great ass!" 
    mc "Oh yeah? Prove it!" 
    show mel smug with d
    mel "Ah- you cheeky little…"
    show mel neutral:
        linear 0.3 xalign 0.75
    show rub happy:
        xalign 0.25
    with d
    rub "Having a little verbal spar, I see?"
    "As [rub] intervenes, I notice a lot of people around the club watching us. Seems like we're causing a commotion."
    mel "Keep a close eye on this one, sis. He only wants to ogle our butts."
    hide mel with d
    "[mel] walks off – and… Oh!"
    image mel0a:
        "mel0a [melb]"
    scene mel0a
    $ textbox = 2
    with d
    "Oh! She gives me a sneaky glimpse of her ass as she passes [rub], which I, of course, admire."
    "She’ll probably use this against me later, but I don't care; I'm just glad she's her usual fun self."
    "Though... something seemed off about her face, like dark makeup around her eyes that's slightly obscured by tufts of fur."
    $ textbox = 1
    play music rubytheme
    scene bg brothel1
    show rub neutral 
    with d
    rub "First time here, isn't it? Apologies for that, darling."
    mc "Yeah, don’t worry, I’m used to people like that."
    show rub happy with d
    rub "[mel] only works here when she feels like it, offering arguments and insults, as she puts it."
    mc "She… works here? In the brothel?"
    show rub laughing with d
    rub "Ah, this isn't a brothel solely for physical pursuits but for intellectual ones too. It's a brothel of intellectual curiosities and mental stimulation."
    rub "Each host here offers a distinct experience—some of the flesh, yes, but others of the mind. For instance, an adventurer with a photographic memory who exchanges stories, or an extremely affectionate dog girl."
    show rub happy with d
    rub "[mel]… she doesn’t actually work here. She just enjoys the free drinks, I guess."
    hide screen vnui
    $ gen1 = 0
    $ gen2 = 0
    $ gen3 = 0
    menu rub1m:
        "What about your boutique business?" if gen1 == 0:
            $ gen1 = 1
            show rub neutral with d
            rub "Reminding me of that… You’re making me nostalgic."
            rub "That was my first dream, but trying to run a clothing shop in a society like this just didn’t make financial sense. Large expenses led to the closure of the business."
            jump rub1m
        "Were you a webcam model once?" if gen2 == 0:
            $ gen2 = 1
            show rub laughing with d
            rub "Heard of that, did you? I seldom did that once upon a time; the resulting funds were enough for me to start what you see today."
            rub "While I don’t participate in the sex industry anymore, but I don’t regret my time as a model."
            jump rub1m
        "Why did you start this brothel?" if gen3 == 0:
            $ gen3 = 1
            show rub happy with d
            rub "I like to consider this world as one of experiences. I desire to experience as much of this world as I can before I pass on."
            rub "This desire was sparked after the failure of my boutique. Spending so many years working on it, only for it to fail, was both a profound and sobering moment for me."
            rub "I realized there was more to life, and hence I began a social club."
            rub "Using my business acumen, it evolved under my leadership over a decade into what it is today." 
            jump rub1m
        "(Continue)":
            show screen vnui
    show rub wink with d
    rub "Enough about us, you seem like an intriguing fellow, and you seem to know quite a lot about me."
    mc "Where do I even begin…"
    "I give [rub] a brief rundown of how I’m trying to recreate the Virtues of Concord to protect this world, and they were a powerful group from my own universe. She doesn’t need all the details now; she can learn as we go."
    "Thankfully, she doesn't balk at the idea that I'm from another universe. She accepts it with a polite sip of wine."
    show rub happy with d
    rub "Now that’s quite the story."
    mc "Let’s just say, I have quite an experience to offer you. How would you like to meet the Queen?"
    show rub wink with d
    rub "Fuhuhu, one doesn’t simply walk into an establishment and hand such a thing out at random. Tell me, why do I deserve such an honor specifically?"
    "A surprisingly challenging question. Why do the virtues need to be the exact same six girls in every reality? They don’t, which is as much as [rub] is indirectly implying."
    show rub happy with d
    rub "I’d really love to discuss this further, darling, but I am swamped with work right now. However, I ask that you instead talk to the other ladies at the brothel and learn from them."
    rub "Once you feel like you’re ready, come back and tell me what you’ve learned."
    hide rub with d
    "[rub] takes off before I have time to think through a reply. Just what exactly is she expecting me to learn?"
    scene bg brothel2 with d
    "I take the opportunity to familiarize myself with the building. In addition to the sitting area, there's a bar over here, and there also seems to be a private area veiled behind curtains. Pretty obvious what happens behind there."
    show mel angry with d
    mel "Can you hear those broads moaning? It’s half the reason we have music here. Can’t believe that kind of thing is happening in my home." 
    mc "Hey again, [mel], where did you sneak off to?"
    show mel happy with d
    mel "The bar. The booze makes this all a little more bearable."
    "She holds out two drinks — pink glittery cocktails that fade into swirls of deeper purple at the bottom of the tall glass."
    show mel smug with d
    mel "Forget my sister’s dumb idea, you’re too good for this lot. Come talk with me instead." 
    "If I want to convince [rub] to help me, getting on [mel]'s good side will help significantly."
    stop music fadeout 10
    stop ambience1 fadeout 3
    scene bg brothel3 with d
    "[mel] leads me to a selection of private cubicles. Intimate sanctuaries that can be closed off by a curtain."
    "Inside, we sit on either side of the room, but still pretty close to each other. The seats were plush and soft, with ambient lighting inviting relaxation." 
    "We quietly sip on our drinks before she speaks up first."
    play music melodytheme
    show mel neutral with d
    mel "Surprising to see a man in here."
    mel "You could be gross and perverted like any other geezer, but you don’t seem to carry yourself like the others… There’s no ego or expectation surrounding you."
    mc "Yeah, I’m gross and perverted, but aren’t we all?"
    show mel smug with d
    mel "Nuh-uh, I’m pure. Such a dirty thought could never enter my pristine mind palace. Unlike you, greedily eyeing up my ass."
    mc "Pfft, as if you weren’t tilting so I could get a better view."
    show mel laughing with d
    mel "We’re all nude here; it’s impolite to stare like that~"
    mc "Speaking of your body, though…"
    "I finally figured out what those markings on her body are: metallic seams."
    show mel neutral with d
    mel "Stop making comments on my body, you lech. I’m not going to sleep with you."
    mc "I’m just curious why you seem to have metal augmentations?"
    show mel angry with d
    mel "Eugh, do you have any idea how bored I am with that conversation? Why can’t someone just accept my body and not ask their inane questions."
    mc "You don’t have to tell me, then. I’m just happy you’re alright."
    show mel neutral with d
    "I return to sipping my cocktail, only to look back up and realize that [mel] was staring at me in pleasant disbelief."
    mel "I, uh… It was an incident. A lot of me is cybernetic now. The details are a story I don’t tell to anyone."
    mel "It really put [rub] in a difficult financial situation… It’s the real reason she started this ‘strip club’ instead of following her dream of a boutique." 
    show mel angry with d
    mel "{i}Sigh{/i} She’s so stupid… Doesn’t she understand how awful that makes me feel?"
    mel "And even though she did it for me, I can’t help but resent her for degrading herself like this. If it wasn't for me, she could be a fashion designer right now!"
    mc "You shouldn't blame-"
    show mel neutral with d
    mel "Don't tell me I shouldn't blame myself! Empty sympathies from a stranger don't mean shit."
    mc "Hm, in that case, I’m curious, how much of you is robotic?"
    mel "It’s more than it looks, and it already looks like a lot... Approximately 50%% of my body is currently mechanical."
    mc "Is it possible for you to get a variety of parts, then?"
    mel "A ‘variety’? What do you mean?"
    mc "Like, different colors, or alternative features." 
    show mel smug with d
    mel "Pfft, do you hate my tiny tits that much? You are correct, though, I could –"
    show mel angry with d
    mel "Wait a second… You just implied you know what I looked like before the incident... that and my name... Who the hell are you?"
    show mel neutral with d
    mel "No, no, I don’t even want to know."
    mc "Really? I'd tell you."
    show mel angry with d
    mel "Even though I could get a larger rack, or a new set of enhanced legs, it’s something I’m very ideologically against."
    hide screen vnui
    menu:
        "I disagree, I’d love to augment my body.":
            show mel laughing with d
            mel "Pfft, sure, if I had such a small pecker, I’d want to augment it too."
            mc "You haven’t seen anything yet. It {i}does{/i} get bigger."
            show mel smug with d
            mel "Ahaha, sure, buddy."
            mel "I’ll stick to what I have. I don’t want to forget myself."
        "I agree; it’s important not to lose yourself.":  
            show mel happy with d
            mel "Exactly! This exact package is me, and I don’t want to forget that."
    show screen vnui
    show mel neutral with d
    mel "If I keep swapping out pieces, A new eye color, a new hair color, a new voice… When would I stop becoming myself?"
    mc "You’re like… a ship of Theseus."
    mel "Eh? Who or what is that?"
    mc "So you're interested in that but not me?"
    show mel smug with d
    mel "Yeah, you're boring! Now continue~"
    mc "It’s a well-known parable about a boat that had one of its pieces replaced by a new one. After one piece, it wasn’t a different boat, and I think we can both agree on that. However, eventually, every piece of this boat was replaced." 
    mc "Now that every piece has been changed, could it really be said that it’s the same boat? Where do we draw the line?"
    show mel neutral with d
    mel "Huh, interesting idea, but this is my body we’re talking about, I apply a line to my own experience far more easily than some boy toy."
    mel "For me, I can live with replacing the first piece… but it’s the second piece or second replacement that would make me feel uncomfortable."
    mel "My current cybernetics carry some meaning for me, although I can’t quite explain why."
    mel "At a certain point of continuing to replace or swapping out parts, I just wouldn’t feel like myself anymore. Perhaps you could liken it to dysmorphia."
    mc "While I can certainly empathize with you, you must appreciate that 99%% of the cells within our bodies also regenerate and replace themselves. So, if we apply my ship analogy to our own bodies, you could also ask, ‘What point is a human being not their original self’?"
    show mel happy with d
    mel "Huuhhh… I wonder, how much does that affect us? Are we truly different people, but the change is so subtle that we don’t realize it?" 
    mel "Every couple of years, some people could be said to be completely different, wouldn’t you agree? Can you really relate, or even remember the you of five years ago? Ten years ago? I can’t, not really."
    mel "How much of ourselves do we lose as our memories fade and we forget who we once were?"
    mel "Maybe we are different people every couple of years, but we’re such a subtle, constant gradient of change that it’s impossible to separate our identities at small timescales."
    mc "This is kind of something I have experience with. If cells were the end-all, we could just clone you, right? Could your brand-new set of cells, even identical, really be said to be the same person as your previous self?"
    mc "For seconds, at most. But give it only a few days, and we’d be experiencing different lived realities and developing in a variety of unique ways, like identical twins splitting at that exact point."
    mc "What I’m saying is, I don’t think you can anchor your identity to the parts that make you. We’ll always be more than their sum."
    show mel neutral with d
    mel "That’s where I have an advantage. My cybernetic parts remain the same. I can be sure of that, and… even find a little comfort in it."
    mc "But won’t even those parts need replacing eventually? They’ll wear and tear."
    mel "Eh… I’ve been stubborn about that. I admit that I hadn’t considered my biological parts changing as you say…"
    mel "Maybe, just maybe, I could be convinced to be more open about changing my parts if it ever comes down to that."
    mel "More than the sum, eh? I like the sound of that, wormy boy."
    mel "But thanks to you, I have a new dilemma now. About what being ‘me’ and ‘myself’ really means. If I’m not going to anchor myself with my parts, then what exactly do I tie my identity to?"
    mc "I guess that falls to what you argue as the ‘self’ being. Is it your body, your mind, or something more or less abstract?"
    mc "Change is inevitable, and nothing is permanent. Just as a ship will need new parts, people can’t escape the forces of time and experience."
    mc "Rather than resist the change, you’ll have to embrace that your identity is not a fixed entity but a constant evolution."
    show mel angry with d
    mel "Eh, but… how?"
    mc "It seems like you’re burdened by your past and the possibility that you’ll have to change in the future."
    mc "As someone that has personally and intimately dealt with losing my identity and grappling over what it means to be ‘me’, I have to say that what it really comes down to is just turning inwards and occupying the moment." 
    mc "No matter who I was in the past, and no matter who I will be in the future, right now, in this very moment, I know I’m me."
    show mel neutral with d
    mel "I’m starting to understand. That ship is only considered another ship relative to its original self, but if we isolate it in the present moment, how could its identity of being Theseus’ ship ever be denied?"
    show mel happy with d
    mel "No matter what… {i}I’m me{/i}…"
    mc "Exactly."
    "That’s how I must deal with it too. Who knows what the other me is doing right now?"
    "[mel] takes a long sip and finishes off her cocktail."
    show mel smug with d
    mel "I know you just told me to focus on ‘now’ instead of the future, but… if you’re going to be this cool, I wouldn’t mind having you around more often in the future."
    mc "Oh?"
    show mel happy blush with d
    mel "Don’t let that get to your head too much; I just meant you should come back to the club sometime…"
    "I can feel [mel]’s feet stretch towards me across the room, finding solace on my thighs. She’s so fluffy and soft that I don’t bother moving out of the way."
    "Although not quite satisfied with that, the toes gradually move closer to my crotch."
    show mel neutral with d
    mel "Mmm… Let’s play a game. If you can keep your grotesque pecker down for, hmm... three minutes, I’ll…"
    "I feel her big toe start tapping against my shaft, and while I was currently unerect, it wouldn’t stay that way for very long." 
    show mel angry with d
    mel "A-Are you… getting hard already?!"
    "Her second foot moves in to examine and squirm around my growing cock."
    show mel neutral with d
    mel "Unbelievable! You fucking pervert! You can forget the—"
    "A couple, a working stallion and female patron, walk past our cubicle, causing [mel] to hurriedly throw the curtains across the entrance in a blushy panic."
    show mel angry with d
    mel "Grrr… I can’t believe y-you—"
    "Turning around from the curtains, she watches full view of my erection, which she had only felt with her big toes before." 
    show mel neutral with d
    mel "You’re actually fucking big?!"
    "Ensuring that the curtains have absolutely no gaps in them, she sits on the same side of the booth as me this time."
    "Tossing her feet up, she returns them to my crotch. This time, however, I have a gorgeous view of her entire petite body."
    play music melodysextheme
    layeredimage mel1a:
        always:
            "mel1a [melb]"
        group eyes:
            attribute e1:
                "mel1ae1 [melb]"
            attribute e2:
                "mel1ae2"
            attribute e3:
                "mel1ae3 [melb]"
        group pantyhose:
            attribute p1:
                "mel1apantyhose 1"
            attribute p2:
                "mel1apantyhose 2"
        group pregnant:
            attribute pregnant:
                "mel1apregnant [melb]"
        group futa:
            attribute futa:
                "mel1afuta  [melb]"
        group cum:
            attribute cum:
                "mel1acum"
    scene mel1a e1 
    $ textbox = 2
    play moans1 moansmisc2
    call camerabreath from _call_camerabreath_15
    with d
    mel "I was going to let you grind it on my butt, which you seem to love so much, but since you’re a disgusting freak, I’ll do this instead!" 
    hide screen vnui
    $ mel1 = 0
    menu:
        "{i}Allow her to continue{/i}":
            "I haven’t said anything in a while; to be honest, I’m just enjoying the show. She’s carrying herself on her own hype and momentum perfectly, and I wouldn’t want to say anything to knock her off her game." 
        "Hang on, you’re not going to use your feet, are you?":
            mel "So what if I am? You don’t deserve any better!"
            mc "I’m not so sure… Are they even clean?"
            mel "Asking that, do you have a death wish?! Of course they’re clean!"
            mel "Hmph, if you’re a good boy, I might even use my mouth."
            menu:
                "{i}Accept her advancements{/i}":
                    mel "I knew you’d come around. This’ll be better than you think."
                "{i}Decline her advancements{/i}":
                    mel "You gotta be…"
                    mel "Hm, no, it’s fine… I respect it even…"
                    mel "Next time, you better be willing to take what you dole out!"
                    show screen vnui
                    jump postmel1
    show screen vnui
    "In addition to wrapping her toes around my shaft and tip, she wastes no time beginning to rub her gorgeous, dripping wet pussy. Her vulva was stunning, and I could feel my cock throbbing and dripping precum at the sight alone." 
    show mel1a e2 with d
    mel "Staring at my pussy, are you? Tsk, keep dreaming."
    play ambience1 handjob fadein 2
    "With a little more confidence in her toes, she starts to thrust them up and down my shaft."
    play moans2 moansmisc4 volume 0.5
    "In the booth beside us, passionate moans begin to ramp up. Likely from the couple that just walked past us. [mel] casts an annoyed glance, but grins as soon as she realizes she can use this as material to tease me with."
    show mel1a e1 with d
    mel "This place is extremely popular this time of year for slutty mares in heat that can’t resist their baser instincts and impulses."
    mel "But don’t think for a second that I’ll be fucking you in here. You’re barely good enough for my feet."
    "My cock twitched as her delicate feet massaged my member. I’m surprised she’s able to achieve such precision with them."
    "My eyes closed tightly as I leaned back and savored every sensation. Watching my enjoyment, [mel] sped up too, her fingers moving rapidly against her clit as her toes gripped around my shaft and started to jack me off."
    show mel1a e2 with d
    mel "Tsk, pahaha, there’s no way this feels good, right?"
    "My member twitched a few times against her tender touch, leaking precum onto her delicate toes—a testament to the fact that, yes, it does feel pretty good, actually."
    mc "Nngghh, [mel], you’re killing me with this. It feels good, but… never quite enough."
    show mel1a e1 with d
    mel "Mmm… Good~"
    show mel1a e2 with d
    "I opened my eyes slightly to watch her work, taking in the sight of her tail swishing back and forth playfully behind her. Gods above, she’s something entirely else."
    "Her voice had taken on a huskier, lustful tone since we’d begun, although now it was getting mixed up in moans of her own enjoyment."
    "The sounds of moans and grunts from the adjacent booth echoed through the thin walls, adding an extra layer of filthy excitement to this illicit encounter. Actually, it wasn’t just moans anymore, but the sound of flesh slapping against flesh—a stallion’s grunts muffled by a mare’s moans."
    mel "I bet you’re imagining us in that situation, aren’t you? Pfft, could you even imagine that? Riding that gross, fat, thick… thing? Ooohhh… No way, never~"
    "Her vulgar words weren’t only exciting me but were spurring her on too. Her fingers and toes were speeding up, relentlessly stroking us both towards climax."
    "I groaned louder, my hips instinctively bucking forward against her expert ministrations."
    mc "Fuuuck, [mel]… I’m actually getting close!"
    "Sensing this, she ceased her mockery to focus on finishing me off, and despite my healthy sex life, I was no match for [mel]’s feet."
    play sound2 cum
    show mel1a cum with c
    play sound2 cum
    with c
    "I groaned louder, my hips bucking forward as my cock throbbed violently and erupted all over her feet, thighs, and even her pussy."
    play sound2 cum
    with c
    play sound2 cum
    with c
    "My body was wracked by wave after wave of mind-numbing pleasure, and albeit subtly, even [mel] seemed to reach an orgasm."
    scene bg brothel3 
    show mel angry 
    show melodycum 
    $ textbox = 1 
    call stopbgs from _call_stopbgs_10
    call camerareset2 from _call_camerareset2_12
    with d
    "Finally, as the tremors subsided, I opened my eyes to discover [mel] pouting in front of me, a mixture of annoyance and mischief dancing behind those captivating eyes." 
    mel "Ugh, you covered us both in cum, and there aren’t any tissues in this cubical to clean us down..."
    mel "There’s no way I’m leaving here looking like this. Imagine what people would think if they saw me with a loser like you~?"
    mc "Yeah, like, ‘Wow, that cold bitch actually got some? I never thought I’d see the day’."
    show mel death with d
    mel "Bwahaha, you better watch what you say, or else I’ll bite~"
    layeredimage mel1b:
        always:
            "mel1bbase [melb]"
        group eyes:
            attribute e1:
                "mel1be1 [melb]"
            attribute e2:
                "mel1be2 [melb]"
        group underwear:
            attribute underwear:
                "mel1bunderwear"
        group leggings:
            attribute fishnets:
                "mel1bfishnets"
            attribute lingerie:
                "mel1blingerie"
        group cum:
            attribute cum:
                "mel1bcum"
    show mel1b e1
    $ textbox = 2
    call camerabreath from _call_camerabreath_16
    play moans1 moansmisc2
    play ambience1 blowjob
    with d
    "Like a shark, [mel] circles my cock and beckons for blood. Her wishes are granted as my erection swiftly returns."
    "Even though this was likely her first ever blowjob, there was nothing sweet and innocent about this truly sinful mare."
    "Her eyes locked onto mine as she took my throbbing cock by one hand and directed it towards her lips."
    "Slowly, teasingly, [mel] lowered her mouth onto my cock until the tip disappeared."
    mel "Mmphhh… {i}Slurp, lick{/i} Okay, this thing is stupidly big. I doubt I could even fit it in my mouth, let alone my precious holes."
    mc "I think you’d be surprised. Those holes can sure take a beating."
    show mel1b e2
    mel "Pfft, like you’d know."
    "Heh, I know."
    "As the passion and intensity of the rutting in the cubical next to ours increased, so did [mel]’s movements; the way she moved and touched me showed that she’d done her research before this."
    "Not only was her hand perfectly sliding back and forth against my shaft at the perfect angle to create some friction against my glans, but her tongue was focusing on all my most sensitive points."
    "Her tongue swirled around my glans, occasionally returning to flicker at the tip and collect all the pre-cum that’d ooze out at regular intervals."
    "At a certain point, I couldn’t help but buck my hips. She matched my enthusiasm as she allowed my cock to slide deeper into her mouth."
    mc "Ohh, fuck… You’re so good at that!"
    show mel1b e1
    mel "{i}Cough, gag{/i} Don’t say I’m good at sucking dick, nerd! {i}Slurp, lick{/i}"
    "Protest as she may, her voice vibrated into my dick and only served to pleasure me more. She knew exactly what she was doing to me, how close she was pushing me to my limit. And yet, she showed no signs of slowing down."
    "Her eyes met mine again, filled with unspoken desire, mixed with that classic tsundere defiance."
    "Naturally, there was something else lurking beneath that reluctant façade—an insatiable hunger brought upon by heat. There was no hiding the increase in her passion and desires." 
    "Eventually, the pleasure built up inside me to a boiling point. I could feel my climax fast approaching, my balls tightening, ready to release their thick seed into [mel]’s eager mouth."
    mc "I’m… I’m close, [mel]!"
    "Without pulling away for a second, [mel] responded by intensifying her sucking and stroking even further. Her tongue flickered over the sensitive spot on the underside of my cockhead, driving me straight over the edge."
    mc "Oh fuck!"
    play sound2 cum
    show mel1b e2 cum
    with c
    play sound2 cum
    with c
    "I roared as my body tensed up, unleashing hot, thick cum into her waiting mouth."
    play sound2 cum
    with c
    play sound2 cum
    with c
    "Orgasmic bliss washed over me as [mel] continued to diligently service my cock, ensuring every second of my orgasm was filled with intense pleasure."
    "She managed to do that, all while accepting every drop of cum into her mouth. Well... most of it, anyway."
    "Once I had finally finished, she gently pulled back, her lips glistening with cum that dripped down onto my thighs. She let out an annoyed but somehow still seductive moan as she moved down to lick it up."
    mel "Disgusting… Gross…"
    "Using her fingers, she wiped up a few more stray bits of cum that had landed on her earlier and licked it all off."
    stop music fadeout 10
    scene bg brothel3
    show mel happy  
    call camerareset2 from _call_camerareset2_13
    call stopbgs from _call_stopbgs_11
    $ textbox = 1
    with d
    mel "That should be enough. We can leave now."
    mc "That was good—"
    show mel smug with d
    mel "Good? What was good? We didn’t do anything in here, got it?"
    mc "As you say, [mel]."
    $ mel1 = 1
    label postmel1:
        scene black with d
        "My erection had finally shrunk to a socially acceptable level, allowing us to leave the cubical."
    play music clubtheme
    scene bg brothel2 
    show mel happy with d
    mel "You should come back here sometime. Decent company around here is a rarity."
    mc "Sure, I’d love to."
    show mel wink with d
    mel "Hehe, I bet you would, pervert~"
    mc "Wha- but you’re the one that invited me!" 
    show mel bashful with d
    mel "Bye for now! Whatever your name is~"
    play sound2 move
    hide mel with d
    "After dropping the bombshell that I forgot to ever give her my name, [mel] skips away. Oops."
    "In the time I’ve spent here, in this new urban Arcadia, I’ve met a lot of the same people with different parts to them."
    "[mel] is perhaps the most literal example of this with her robotic parts. Despite that, the core of her identity is very much still [mel] through and through, and there’s a good chance that everyone else in the universe is like that too." 
    "The differences may be overwhelming on the surface, but deep down, the heart is the same."
    play sound2 move
    show bg brothel1 with d
    "Now, where’s [rub]? I’ve scanned the floor, but I don’t see her anywhere. Will I have to sneak upstairs?"
    play sound2 move
    $ renpy.music.set_volume(0.5)
    show bg brothel4 with d
    "Even though the building is much larger, I end up upstairs in a hallway I recognize. If I’m right, that means [mel]’s bedroom should be here, and [rub]’s bedroom is the next door on the left."
    play sound2 move
    show bg brothel5 with d
    stop music fadeout 4
    "Both rooms are empty, but I hear some sounds coming out of [rub]’s office opposite her bedroom. With a polite knock, I enter."
    show ruby1a e1
    camera:
        linear 0.5 zpos -16 ypos -2 xpos 0
        block:
            linear 2.5 ypos 5
            linear 0.4 ypos 5
            linear 1.5 ypos -1
            linear 0.2 ypos -1
            repeat
    $ textbox = 2
    with dissolve
    $ renpy.music.set_volume(1)
    play music rubytheme
    rub "Good evening, darling. You’re here a little sooner than I expected. Especially considering it was my sister that whisked you away."
    "She looks gorgeous. The casual bathrobe coupled with the brazen nudity. Another win for the open nudity society." 
    rub "Needless to say, there’s a lot of wisdom that can be learned from her too. So, what exactly did you learn?"
    $ gen1 = 0
    $ gen2 = 0
    $ gen3 = 0
    $ textbox = 1
    hide screen vnui
    menu b1rm1:
        "I’m not sure." if gen1 == 0:
            $ gen1 = 1
            rub "You’re being too modest. I can tell that you’re a wise man."
            jump b1rm1
        "What am I supposed to be learning?" if gen2 == 0:
            $ gen2 = 1
            rub "Anything and everything, dear. Speak your mind; I won’t judge."
            jump b1rm1
        "She doesn’t like the brothel" if gen3 == 0:
            $ gen3 = 1
            rub "Ah, that she doesn’t. It was originally a necessity for our financial situation, but it has since evolved into a passion of mine."
            rub "That said, surely there's something more?"
            jump b1rm1
        "She’s half cyborg, but that doesn’t mean she isn’t the same person.":
            rub "Indeed, no amount of change will change the core of my sister; change her heart."
            mc "Not even an alternative universe. [mel] is [mel]."  
        "Our identities are ever evolving":
            rub "Perfect. That’s exactly what I wanted you to learn."
        "With a new universe, there’s potential for new experiences":
            rub "It sounds like you know exactly why I assigned you such a task. Or are you merely pandering to my own mindset?"
    show screen vnui
    rub "I noticed that you were quickly trying to appeal to my own philosophies and experiences. It’s a sign of sharp wit and empathy. I wouldn’t be surprised if you were the kind of gentleman that could crack open any lady’s mind or spread her legs."
    mc "And you’re even wiser than that if you managed to get such an accurate read on me in such a short amount of time."
    rub "I’ve had the opportunity to meet thousands, dearie, so you could chalk it up to experience. However, you were quite easy to read; it’s in your face."
    rub "You are burdened and stressed, are you not? You appealed to my desires not out of casual charisma but out of a necessary desire to convince me."
    mc "Yeah… It’s pretty important to me."
    rub "If you’re going to use the concept of experiential living, then you’re on my battlefield, darling. And it doesn’t seem like you’re applying that philosophy to your own life."
    rub "You’re in a new universe, so I can understand why you’d feel the sudden urge to ‘fix’ everything, ‘recreate’ everything as it once was."
    rub "But that’s not how life has to be, nor is it ever as simple as that."
    rub "You’re so caught up trying to recreate and match the past that perhaps you’ve overlooked the potential for growth, new avenues, and new experiences."
    mc "I admit, I have been rushing around while potentially overlooking the world around me. However, there’s no shortage of new experiences here, even with familiar faces." 
    mc "I’ve been keeping an open and cautious mind. All my past friends and family are now strangers, and they may be fundamentally different people."
    mc "But that also gives me the opportunity to meet them and fall in love all over again. Isn’t that alone an experience worth recreating?"
    rub "Ah… It seems I’ve made a mistake. I was viewing your situation from a naïve perspective."
    show ruby1a e3 with d
    rub "It’s not easy to place myself in your shoes, so I hadn’t considered such a beautiful possibility." 
    mc "That shouldn’t be too surprising; this is a new experience for you, after all."
    "My reply had a hint of [mel]-esque sass in it, causing [rub] to laugh."
    show ruby1a e2 with d
    rub "You are a fascinating man, [mc]."
    mc "And even in another universe, you’re still one of those most gorgeous mares I’ve ever met, [rub]."
    mc "Would you be willing to help me? I promise you that it’ll be one of the most incredible experiences you’ll ever get to have." 
    show ruby1a e1 with d
    rub "Hehe, I didn’t need {i}that{/i} much convincing. Talk about a gentleman that goes above and beyond." 
    show ruby1a e2 with d
    rub "And now you have me wondering if you match that vigor in the bedroom, darling…" 
    mc "Wouldn't you like to know?"
    show ruby1a e3 with d
    rub "Yes, I would. Tell me, what kind of relationship did you have with my prior self?" 
    mc "Oh, I wasn't expecting such a forward question. Well, it's likely as intimate as you're imagining."
    show ruby1a e2 with d
    rub "I knew it. Somehow, I could read it on your face."
    show ruby1a e1 with d
    rub "You handle yourself around me with such a strong sense of familiarity. You probably haven't even once considered my prolific status as 'Madam Ruby'."
    mc "Not particularly. To me, you're just '[rub]'. Is that wrong of me?"
    rub "Absolutely not, darling. You see, I've gained such notority that people all turn to stare at me when I walk by; those that do dare to talk to me stutter their lines no matter how prepared."
    mc "Hm, so that's the real reason people were staring at us on the club floor."
    rub "Quite. The harder I work, the more difficult it is for me to make a simple friend."
    mc "Really? I thought the brothel started as a social club."
    rub "People assume that I must have plenty of friends in my position, but from my experience there are either vultures trying to exploit me for their own gain, or people that put me too high on a pedestal for friendship to work."
    rub "I wish it wasn't the case, but some people just can't see past this 'power dynamic'."
    mc "Rich, affluent, beautiful... Life must be so hard~"
    show ruby1a e3 with d
    rub "Heh, your sarcasm is noted, but I've come to discover that all the gold in the world means nothing if you have no one to share it with. But you can't buy true friends, I learned that the hard way." 
    rub "I really appreciate that you treat me like ordinary person, an old friend. Very refreshing, very rare, and ideal lover material. Wouldn't you say?"
    mc "Heh, don't tell me that you're just curious to see what it'd be like to sleep with someone that's technically already slept with you."
    stop music fadeout 3
    show black with d
    layeredimage ruby1b:
        always:
            "ruby1bbase [rubb]"
        group eyes:
            attribute e1:
                "ruby1be1 [rubb]"
            attribute e2:
                "ruby1be2 [rubb]"
            attribute e3:
                "ruby1be3 [rubb]"
        group plug:
            attribute plug:
                "ruby1bplug"
        group cum:
            attribute cum:
                "ruby1bcum"
        group sex:
            attribute v1:
                "ruby1bv 1"
            attribute v2:
                "ruby1bv 2"
            attribute a1:
                "ruby1ba 1"
            attribute a2:
                "ruby1ba 2"
    play music sextheme
    play moans1 moansmisc2
    scene black with d
    $ textbox = 2
    with d
    "[rub] moves to a couch against a wall, leans back and stretches, causing the band of her bathrobe to unfurl and the clothing to fall backwards, leaving her bare." 
    show ruby1b e1 with d
    "She spreads her legs, her pussy so wet that it creates an audible schlick as it’s spread open by the movements."
    rub "No, darling. I want to sleep with you because I'm sexually attracted to you~" 
    mc "Woah… I- uh…"
    rub "I’m so horny that I admit it’s distracting me. You wouldn’t mind if I catered to myself as you continued to speak?"
    hide screen vnui
    menu:
        "{i}Pursue More{/i}":
            pass
        "{i}Back Out{/i}":
            mc "Sounds like you already get the idea. I wouldn’t want to impose." 
            rub "Oh, but you aren’t. Won’t you regale me with your tales?"
            menu:
                "Fine, I can’t resist you.":
                    pass
                "Another time for sure.":
                    show screen vnui
                    jump postrub1
    show screen vnui
    $ rub1 = 1
    "It looks like she was preparing to masturbate to whatever I was about to say next, and a mutual masturbation session would be fun… But I think she’s actually looking for me to take a little more initiative than that." 
    mc "Anything I could say would fall short of what I could show you instead. Why don’t I let my actions speak for themselves?"
    rub "My, my… I don’t sleep with people I’ve only just met, but you wouldn’t have said that if you didn’t know it wouldn’t have worked, right?"
    mc "And that's not to mention that we've known each other for ages."
    "She leans her hips forward and spreads her gooey pussy wide for me, inviting me to fuck her senseless." 
    rub "Very well, it’s not every day I get to sleep with someone who’s technically already fucked me. I was planning to seduce you later, but it seems you decided to seduce me first."
    "The sight of the refined unicorn lady in such a state of wanton need was enough to make my cock fully erect in a matter of seconds. I closed the door behind us before striding over to the table, my eyes feasting on every inch of [rub]’s exposed body."
    "Her delicate body was flushed with desire, sweat beading on her forehead and between her large breasts that bounced enticingly as she panted. The toll of her heat was clear; she needed this." 
    rub "I expect you to know all my sweet spots, okay~?"
    mc "More than."
    "She arched her hips up towards him, her wet pussy lips glistening in anticipation of my cock thrusting into her tight hole."
    if mel1 == 1:
        "It almost feels wrong to fuck her straight after her sister gave me a blowjob. My cock might even still be a little slick from it, which just makes it feel so wrong in all the right ways." 
    play sound2 cum
    show ruby1b e2 v1
    play moans1 moansmisc3
    with c
    "Wasting no more time, I grabbed hold of her hips with one hand, and guided my cock with the other. Pressing my tip against her wet entrance, I thrust hard, burying myself to the hilt inside her tight pussy in one smooth nation."
    "A ragged moan tore from her throat at the incredible feeling of being filled after an arduous season of heat."
    rub "Oooohhhh… Goodness me, I {b}needed{/b} that."
    play ambience1 sex
    "She continued to let out high-pitched whines of pure pleasure as I started thrusting—my cock grinding against all the right spots inside of her, sending shockwaves of pleasure coursing throughout her body."
    "Clenching tightly around my shaft, she teased and squeezed every inch of my cock with deliberate contractions and relaxations, an exquisite technique that I nearly forgot she had."
    "These motions transformed what would be primal rutting into a dance of lust where we moved to each other’s rhythm and our sex became more than the sum of its parts."
    mc "Mmhh, damn! I have no idea how you do that with your pussy, but never stop! {i}Thrust, thrust, thrust{/i}"
    rub "Hehe, I won’t stop if you don’t, darling… Mmhh, kiss me~"
    "Our lips locked together as her longer equine tongue quickly dominated my mouth. I love kissing these mares with their long muzzles, it feels so natural and sensual."
    "As the passion of our kiss intensified, so did our thrusting. The sound of our bodies slapping together got so loud that it echoed loudly throughout the room. Sweat dripped down from the body of us onto the office table beneath us, staining the pristine wood with our lust."
    "[rub]’s nails dug into the fabric of the tablecloth, leaving deep furrows as she arched her back off the table, begging for more."
    rub "Fuck me harder~"
    "She moaned breathlessly between gasps of air."
    rub "Rut me like the filthy mare I am!"
    "Don’t mind if I do! I picked up the pace, slamming into her tight pussy again and again without mercy or restraint."
    "I could feel myself getting closer and closer, and as she reached her climax, I was soon to follow."
    play sound2 cum
    show ruby1b e2 v2 cum
    with c
    play sound2 cum
    show internalcreampie
    with c
    "With one final, powerful thrust, I reached my release. My cock pulsed thick ropes of hot cum deep inside of [rub]’s womb."
    play sound2 cum
    with c
    play sound2 cum
    with c
    rub "Uooohhhhh, yeeesssss! Pump me full!"
    "My seed mixed with her own juices as I continued pounding into her, milking every last drop of pleasure I could from our shared orgasm."
    "Finally spent, I pulled out of her slick pussy, leaving behind a messy trail of our combined fluids dripping down onto the table below her." 
    show ruby1b e3 -v2
    hide internalcreampie
    with d
    "Panting heavily, we caught each other’s eyes—two people who had just experienced the height of carnal pleasure together."
    "There was no pretense of refinement or ladylike behavior from her—just an animal driven wild by lust during the heat of mating season. And damn did she enjoy every filthy second of it."
    label postrub1:
        scene bg brothel5
        show rub happy 
        call stopbgs from _call_stopbgs_12
        call camerareset2 from _call_camerareset2_14
        $ textbox = 1
        with d
    rub "Mmmm… I accept your invitation to meet with the Queen."
    rub "After all, how could I call myself a seeker of experience if I refused to join a man who claims to be from another universe?"
    mc "Excellent! I will send you the contact details of her student, [lil]. She’ll act as our middleman until everyone is ready to come together."
    show rub wink with d
    rub "I’ll be there. But in the meantime, I’ll be here, and I do hope you’ll come back for me."
    if rub1 == 1:
        mc "Still want more of me?"
        show rub horny with d
        rub "We haven’t even tried my favorite positions yet, darling. It’s not a case of wanting more of you; I haven’t even started with you yet."
    show rub happy with d
    rub "I also briefly considered asking if you’d like to work here. I must imagine that you’re struggling to find work, and you’d be the perfect candidate as one of our hosts."
    "I always enjoyed a general popularity in this female-dominated city, but there are plenty of men already working in this brothel. Stallions, a minotaur and more. I may slowly be getting fit and muscular, but I do wonder how I could compete against those guys."  
    hide screen vnui
    menu:
        "I appreciate the offer.":
            rub "Excellent!"
        "I’ll think about it.":
            pass
        "I don’t think so.":
            show rub wink with d
            rub "You needn’t sleep with the patrons, but merely share in drink and conversation."
            rub "And between you and me, you’d be very popular. The tips can be quite lucrative." 
    show screen vnui
    show rub laughing with d
    rub "If you’re interested, the next time you’re here, let’s do a mock conversation on the floor to act as an interview of sorts."
    mc "I’ll definitely be back."
    show rub happy with d
    rub "Hehe, I can’t wait."
    stop music fadeout 2
    scene bg brothel4 with dissolve
    play music melodytheme
    show mel angry with dissolve
    "I step outside the office and politely close the door behind me. As I go to start walking down the corridor, I’m somehow blindsighted by a grumpy [mel] crossing her arms."
    mel "{i}Hushed{/i} Seriously?! You pig!"
    mc "It was a business meeting, nothing more."
    show mel death with d
    mel "You did your business, alright!"
    mel "I thought you were interested in me! But you’re already fucking my sister! Have you no shame?"
    if rub1 == 1:
        mc "Depends who I’m talking to. You? Not much."
        show mel neutral with d
        mel "I- huh…"
    else:
        mc "You’re mistaken. We didn’t actually have sex."
        show mel neutral with d
        mel "Hmph, but you said you would later."
        mc "Just how long have you been eavesdropping?!"
    show mel wink with d
    mel "What’s this about another universe, hm? I figured you knew me too well too."
    mc "I wasn’t exactly hiding that from you. It’s just…"
    show mel bashful with d
    mel "Forget it. You know what, spending time with you was just fun enough for me to not even care."
    show mel smug with d
    mel "I’m just disappointed that you clearly didn’t enjoy it as much as I did."
    stop music fadeout 10
    hide mel with d
    "[mel] storms off in a theatric huff, closing her bedroom door behind her."
    "Briefly, I consider knocking on her door, but it might be best to give her some space for now."
    "To be honest, I can’t even tell if she’s being serious or if that was entirely a theatrical outburst. Especially considering this is an inverse of the first time I met her in the other universe, where instead of getting mad at me for sleeping with [rub], she was encouraging me to do it."
    $ melnerd = 0
    hide screen vnui
    menu:
        "Knock on her Door":
            "Alright, maybe one knock."
            "I quickly knock on [mel]’s door and say…"
            menu:
                "You’re a nerd!":
                    $ melnerd = 1
                    "Then I run away as fast as I can."
                    "Got’em."
                "Sorry!":
                    "Then I casually walk away."
        "Leave":
            pass
    show screen vnui
    scene black with d
    "…"
    $ brothelroute1 = 1
    scene bg apartment with d
    "By the time I get back to the apartment, [mox] is already back and beginning to prepare some food."
    show mox laughing with d
    mox "Hey tiger, how'd your little conquest go today?"
    mc "I went to the boutique—well, the brothel. I was well-prepared for this one. [rub] and particularly her sister [mel] are characters that can take some getting used to."
    show mox happy with d
    mox "Why’s that?"
    mc "I’m not even sure how I’d describe [mel] without you seeing her in action. Especially considering that I know she’s capable of switching her ‘bully’ mode off when around normal people."
    mc "I guess if I were to best describe it, her love language is a theatrical parley of bullying. There’s a bell curve where the more she likes you, the more she’ll want to bully and pick on you, but if you pass a certain point, she becomes extremely loving." 
    show mox sad with d
    mox "I couldn’t imagine bullying the people I love!"
    if replay == 0:
        play sound2 notification
        $ melmsg1 = 1
        $ unread += 1
        $ unreadmel += 1
    mc "The first time I met her, I just found it frustrating and confusing. Now I know how to bite back just the way she likes it, and once you get into that gooey center, she really opens up; she's a great conversationalist."
    show mox neutral with d
    mox "What about [rub]? Is she also a bully?"
    mc "She couldn’t be any more different. [rub] is a {i}lady{/i}, retaining even her delicacy and refinement in the hay – at least for the first few minutes anyway. Passionate sex is the ultimate equalizer."
    show mox horny blush with d
    mox "Phew, I’m working up a sweat just hearing that. I do have a fondness for those types of ladies; actually, come to think of it, I have a fondness for all types of ladies."
    mc "Me too, [mox], me too." 
    scene black with d
    "After eating dinner together, we went to bed."
    if replay == 1:
        return
    $ brothelcompletion += 1
    $ completion += 1
    $ feedupdate += 1
    jump newday
label brothel2:
    stop music fadeout 1
    stop ambience1 fadeout 1
    show black with d
    "'The only way to make sense out of change is to plunge into it, move with it, and join the dance.' - Alan Watts"
    hide black
    show rub laughing lingerie2 dress1
    with d
    play music rubytheme
    rub "Wonderful! As you know, we pride ourselves on offering more than just physical pleasures here. This is a brothel of intellectual curiosities."
    show rub horny with d
    $ textbox = 2
    "Today, [rub] was in a gorgeous red dress. I could barely take my eyes off her, and she happily took notice as she subtly showed herself off."
    $ textbox = 1
    rub "Like what you see?"
    mc "I {i}really{/i} do."
    show rub wink with d
    rub "Fuhuhu... Our hosts are expected to stimulate our guests in unique ways, encouraging them to stay longer and truly enjoy their time."
    rub "Come with me~"
    scene black with dissolve
    show bg brothel1 
    camera:
        ypos -150 zpos -400
    with d
    "She led me back downstairs to a cozy seating area where a small table was set with a bottle of wine and two glasses. Sitting here in the bustling club felt both daunting and immersive, adding to the atmosphere of the interview."
    show rub happy dress1 lingerie2 with d
    rub "For your interview, I’ll pretend to be a customer. Your task is to make me feel welcome, engage me in interesting conversation, and ensure I’m enjoying myself. It should be quite trivial for a gentleman such as yourself."
    "[rub] poured the wine and handed me a glass before taking a seat beside me. She sipped her wine, her eyes never leaving mine."
    show rub wink with d
    rub "So, tell me a bit about yourself. What brings you here?"
    "I took a moment to gather my thoughts. If this were a normal conversation, it’d be much easier, but the context added some unexpected tension. However, I quickly realized what she wanted and how easily I could provide it."
    mc "I’m from another universe similar to this one but with a variety of small changes. I could tell you all sorts about my previous world."
    show rub laughing with d
    rub "Marvellous. You understand exactly what we’re going for here. Our goal is for every host to offer an entirely unique experience. If you’re interested, I can introduce you to some of them around the floor."
    camera:
        linear 1 zpos 0 ypos 0
    menu bv2m1:
        "The grey mare":
            # if chl not named, name her here
            hide rub 
            show cla happy
            with d
            if clairenamed == 0:
                $ clairenamed = 1
                menu:
                    "I think I recognize her. What was her name?"
                    "Default: Claire":
                        $ claire = "Claire"
                    "Custom":
                        $ claire = renpy.input("What was her name?")
                        if claire == "":
                            $ claire= "Claire"
                        $ claire = claire.strip()
            rub "Over there is [cla], a musical genius. She's one of our most expensive and sought-after hostesses. She has a private, soundproof booth where she performs live music."
            rub "She's so high-class that her customer base is almost entirely unique. Even I don't know the details."
            hide cla
            show rub happy lingerie2 dress1
            with d
        "The dog girl":
            #if rosa not named, name her here
            hide rub 
            show ros happy
            with d
            if rosanamed == 0:
                $ rosanamed = 1
                menu:
                    "I think I recognize her. What was her name?"
                    "Default: Rosa":
                        $ rosa = "Rosa"
                    "Custom":
                        $ rosa = renpy.input("What was her name?")
                        if rosa == "":
                            $ rosa= "Rosa"
                        $ rosa = rosa.strip()
            rub "And over there, already entertaining a guest, is [ros], our dog girl. She's infectiously happy, loving, and loyal. I don’t think she’s capable of a bad thought."
            rub "She's incredibly popular, and with the number of requests I've seen, I often wonder if she’d be interested in the sexual side of the job."
            rub "It is mating season; I can see the temptation in her eyes... One nudge might do it, but I don’t want to be a bad influence."
            hide ros
            show rub happy lingerie2 dress1
            with d
        "The wolf girl":
            hide rub 
            show hilda char:
                zpos 350 xalign 0.5 yalign 0.6
            with d
            "(This character's art is in development)"
            if hildanamed == 0:
                $ hildanamed = 1
                menu:
                    "I think I recognize her. What was her name?"
                    "Default: Hilda":
                        $ hilda = "Hilda"
                    "Custom":
                        $ hilda = renpy.input("What was her name?")
                        if hilda == "":
                            $ hilda= "Hilda"
                        $ hilda = hilda.strip()
            rub "The wolf girl over there is [hil]. At first glance, she seems like an unremarkable adventurer, but she has a unique history like yours."
            rub "Allegedly, she wasn’t originally from this planet. Her space-capable vehicle crashed here, and we lack the technology to repair it."
            mc "Space travel? I feel like that should be more shocking to me, but compared to interuniversal travel and magic, it seems quite tame."
            rub "At first, she only worked here out of necessity for the money, but she grew to enjoy it, now regularly performing sexual favors for coin. I feel bad that I may have influenced that corruption and I wonder if she’d even want to leave if given the choice."
            hide hilda
            show rub happy lingerie2 dress1
            with d
        "The cat girl":
            hide rub 
            show bastet
            with d
            "(This character's art is in development)"
            if bastetnamed == 0:
                $ bastetnamed = 1
                menu:
                    "I think I recognize her. What was her name?"
                    "Default: Bastet":
                        $ bastet = "Bastet"
                    "Custom":
                        $ bastet = renpy.input("What was her name?")
                        if bastet == "":
                            $ bastet= "Bastet"
                        $ bastet = bastet.strip()
            rub "That’s [bas], the genuine ex-princess of the fallen feline kingdom."
            rub "Unlike the others, she offers a cold and disinterested approach. You may wonder what the appeal is, but [bas] has a way of making her affection and interest feel earned and precious. Such effort would only be appropriate for a princess, after all."
            rub "One of her services are her elusive private dances, so rare that they've earned a mythical status among the regulars, and whatever happens in those private booths is a secret that never gets out."
            rub "She also specializes in strategy games and challenges. Unbeaten at chess, for instance."
            hide bastet
            show rub happy lingerie2 dress1
            with d
        "The men of the brothel":
            rub "The men of the brothel are primarily here for the popular physical services they provide, especially during this busy season."
            rub "We have a stallion, and you've already seen the minotaur and dragon. With their diverse backgrounds and cultures, we ensure each one offers a distinctive host experience."
            mc "Looks like I fit into that niche of being a unique species too."
            rub "That’s why I just {i}had{/i} to interview you, darling. But understand that you’re more than just a commodity, you’re a genuine spectacle."
        "(Continue)":
            jump bv2m1p
            stop music fadeout 3
    jump bv2m1
    label bv2m1p:
        show rub laughing with d
        camera:
            linear 1 ypos -150 zpos -400
        rub "Now, darling. Imagine I've had a long day and I'm looking for some relaxation. How would you make me feel at ease?"
    play music casual1
    mc "I suppose not everyone is looking for an intense conversation, right? I'd offer to refill your glass and ask about your day. Attentive listening is the key to being a great host."
    show rub bashful with d
    rub "Lovely answer. Now, let's delve into a hypothetical scenario. Suppose I'm a guest who's feeling a bit out of place. How would you handle that?"
    mc "I think acknowledging that feeling openly and making it clear there’s nothing to be ashamed of is important. That should lead into a conversation that breaks the ice and leaves us feeling more connected." 
    show rub wink with d
    "[rub]’s eyes glinted with approval."
    rub "Excellent, darling. You're doing very well."
    "She leaned back, seeming to slip out of the interviewer mindset for a moment as she absorbed the atmosphere of the club. Perhaps the many sips of wine she’s had during the conversation were starting to take effect."
    show rub awkward with d
    rub "[mc], you can give me insights like no other man in the world. So please tell me... This brothel... What do you think of it? How does it compare to my beloved boutique?"
    mc "It is truly remarkable. The ambiance, the decor—it's all very impressive. But..."
    mc "It’s extremely different from your boutique. It’s missing the shabby chic atmosphere and your personality."
    show rub horny with d
    rub "My, my… To know me that well…"
    show rub bashful with d
    rub "But you must understand, the boutique was for me to work in; the club wasn't made for me. I've created generalized spaces where people can engage in meaningful conversations and physical pleasures."
    mc "’{i}The club wasn’t made for you?{/i} If not you, then for who?"
    "I recall what [mel] told me before. This club was a sacrifice [rub] had to make to pay for her surgeries. Is this truly what [rub] wanted, or is it simply a role she fell into?"
    show rub neutral with d
    rub "As you may remember me saying, this was once a mere social club for the needy, occupying the bottom floor of the building, with my boutique taking up half the ground floor."
    show rub bashful with d
    rub "I offered warm meals and games, even if it did stretch my purse thin." 
    show rub awkward with d
    rub "Eventually, it evolved into a club, and then a brothel… through upgrades, persistence, and yes… necessity."
    mc "Do you ever wonder if something was lost along the way?"
    show rub neutral with d
    rub "As anything grows and changes, it can forget itself. Sometimes, you lose even the most important things. Sometimes, you don’t have a choice."
    rub "Sometimes I still yearn for my boutique. I can only justify these sweeping changes as 'new experiences' for so long. There's nothing new about this anymore."
    show rub awkward with d
    rub "I've put so much of my energy and resources into making sure this place runs smoothly and that my sister has everything she needs. When you give up that much of yourself, there's a lot you forget."
    mc "That's a heavy burden to carry, but even someone as strong as you has their limits. Maybe it's time you shared that burden."
    mc "You can... I don't know, elope to a beach with me sometime. This place will hold without your direct involvement."
    show rub bashful with d
    rub "You're right... I spent so long struggling to make ends meet that I've forgotten how to even take a break... For too long, I was scared that if I ever stopped, it'd all come crashing down."
    mc "You've built something amazing here, but it's okay to take a step back now. You don't have to carry the weight of the world on your shoulders alone. You deserve to be happy too, [rub]. Don't forget that."
    show rub laughing with d
    rub "Thank you, [mc]. Your words mean more than you know. You would do well here."
    "We sat in silence for a moment, the connection between us deepening. I realized that this interview had turned into something much more—a genuine hosting session."
    show rub horny blush with d
    rub "I think I've had enough to drink. Now, let's see how you handle a more challenging situation. Suppose I'm a bit tipsy and start flirting with you. What would you do then?"
    mc "Heh, I already demonstrated how I’d handle that, didn’t I?"
    show rub wink with d
    rub "Fuhuh, that you did… But do humour me."
    mc "In that case… I’d reciprocate with charm and humor, keeping things light and friendly."
    show rub bashful with d
    rub "Mhm… And what if I asked if we could go to a private booth together~?"
    "Her longing eyes wander over to the section of the building with the booths."
    mc "I’d let you know my advanced payment rates."
    show rub laughing with d
    rub "Hahaha, cheeky, darling! Customers are well-informed of those prior to any engagement, to not ruin the mood."
    mc "In that case, I’ll let you pick the booth. I’m sure there are plenty of important things you could show me in there." 
    play music rubytheme
    scene bg brothel2 
    call camerareset2 from _call_camerareset2_24
    with d
    "I followed [rub] as she led me through the elegant halls of her establishment, her giggles displaying a sense of youthful excitement."
    show rub laughing dress1 lingerie2 blush with d
    rub "Goodness me, I'm getting so flustered. People saw me walk in here! What would they think of me?"
    mc "I think they’d be wondering who the lucky guy is!"
    show rub wink with d
    rub "{i}Giggle{/i} You’re so bad~"
    "Despite being the madam of this refined brothel, she seems to feel young again, her eyes sparkling." 
    scene bg brothel3 with d
    "She opens the door and gestures for me to enter first. The booth is luxurious, with a plush velvet sofa, dim lighting, and a small table adorned with an assortment of items. There's a cabinet on one side, partially open, revealing various supplies."
    show rub bashful dress2 lingerie2 blush with d
    "[rub] steps in after me, closing the door softly behind her. Her dress seems to slip off slightly as she moves to the table and picks up a small bottle, turning it in her hands with a seductive smile."
    show rub horny with d
    rub "In here, we have everything one might need for a delightful experience. Lubrication, to ensure everything goes smoothly, especially important for your large cock~"
    show rub bashful with d
    rub "And over here we have a variety of protection options… But I’d like you to take me raw today."
    show rub horny
    camera:
        linear 2 ypos -200 zpos -600
    with d
    "She places the bottle back on the table and steps closer to me, her breath warm against my ear."
    rub "And then, there are the more... intimate amenities: toys, restraints, anything you can imagine."
    "[rub]’s proximity and the sensual way she describes everything send a shiver down my spine. She pulls back slightly, her eyes locking onto mine with a mischievous glint."
    rub "Would you be interested in a little roleplay? Something a bit naughty like 'non-con?"
    stop music fadeout 3
    menu b1rm2:
        "I’m definitely interested":
            $ noncon = 1
            "Her proposition caught me off guard, but the excitement in her eyes is contagious. I find myself nodding, my pulse quickening."
            show rub wink with d
            rub "Perfect~ My safe word is Opal. Now make it seem like I'm completely at your mercy."
        "No thanks":
            $ noncon = 0
            rub "Of course, darling. A host having boundaries and being comfortable asserting them is a very important part of the job, and actually one of the reasons I asked."
        "What’s non-con?":
            show rub wink with d
            rub "It stands for non-consensual. It’s erotic roleplaying where one participant, me, plays the part of a character who does not consent to the actions being performed upon them by another participant, you~"
            mc "So this isn’t a trick, or something I should decline if a customer ever asks?"
            show rub horny with d
            rub "No, no, darling. I’m being serious."
            rub "It isn’t condoning genuine non-consensual activities. Quite the opposite; it allows individuals like myself who might harbor such desires or fantasies to explore them."
            mc "Huh, I had no idea you were into something like that."
            rub "Darling, we haven't even cracked the surface~"
            jump b1rm2
    play sound2 equip
    show rub -dress2
    call camerareset from _call_camerareset_10
    with d 
    "Her dress drops, along with my jaw."
    play music sextheme
    play moans1 moansmisc2
    layeredimage rub2a:
        always:
            "rub2ab [rubb]"
        group lingerie:
            attribute lingerie:
                "rub2alingerie"
            attribute lingerie2:
                "rub2alingerie2"
        group eyes:
            attribute e1a:
                "rub2ae1 [rubb]"
            attribute e1b:
                "rub2ae2 [rubb]"
            attribute e2a:
                "rub2ae3"
            attribute e2b:
                "rub2ae4"
            attribute e3:
                "rub2ae5 [rubb]"
        group cum:
            attribute cum:
                "rub2acum"
        group sex:
            attribute v1:
                "rub2av1"
            attribute v2:
                "rub2av2"
            attribute a1:
                "rub2aa1"
            attribute a2:
                "rub2aa2"
        group buttplug:
            attribute plug:
                "rub2aplug"
    #image
    show rub2a e1a lingerie2 plug 
    $ textbox = 2
    call camerabreath from _call_camerabreath_34
    with d
    "And the hits don't stop coming, as she positions herself on the sofa, her belly against the cushions and her arms forward. She looks over her shoulder at me, her eyes filled with excitement."
    "Woah, she's soaked, and she had that plug in the entire time during the interview? Holy shit, my cock couldn't be harder if I tried right now."
    rub "Now, don't be gentle with me. Make it real."
    menu:
        "{i}Continue{/i}":
            $ rub2 = 1
            if noncon == 1:
                show rub2a e1b with d
                "After saying that, her expression changes to one of vulnerability, and her tone shifts slightly."
                rub "P-Please, [mc]! I know I’ve been unable to pay your protection fees, but I promise I’ll get you the money."
            else:
                rub "My heat has been really bad this season… Mmhh... I’d appreciate it if we went for a few rounds."
            "I swallow hard, the intensity of the moment sinking in. I close the distance between us in three strides, my cock throbbing eagerly at the sight of her raised ass."
            if noncon == 1:
                "Since I was quiet, there was an obvious anticipation from [rub] about what my first move was going to be. Without a word, I grabbed her by the tail – hard enough to yank her butt up, but not hard enough to hurt her."
                "She let out a delightful gasp of surprise that quickly turned into a moan of desire."
                mc "You knew the consequences of falling behind on payment. I’ll find ways to make you pay."
            "I run my hands over her exposed butt, feeling the softness of her fur. [rub] lets out a soft moan, her body shivering in anticipation."
            "I position myself behind her. I can feel my erection pressing against her, and she lets out a gasp as I push against her entrance."
            if noncon == 1:
                rub "Please, no, don't do this... I-I’m still… It’s my first time…"
                mc "Good. Every time you fail to pay me back, I’ll take something from you that you’ll never get back." 
            else:
                rub "Ooohh, I still can’t believe how thick you are down there… No need for lube, I want to really feel it stretching me out."
            play sound2 cum
            show rub2a v1 with d
            "I enter her slowly, savoring the feeling of her warmth enveloping me. She whimpers, her body trembling."
            if noncon == 1:
                show rub2a e2b with d
                rub "No, no! Ooohhh…"
            else:
                show rub2a e2a with d
                rub "Ngghhh, it feels so good! Oohhh, fuck me hard!"
            mc "Nngghh, god damn, [rub]! You’re so tight!"
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
            "The sound of her pleading sends a jolt of arousal through me. I thrust into her harder, gripping her hips for leverage. [rub]’s moans grow louder, her body rocking against mine with each movement."
            if noncon == 1:
                rub "S-Stop! I-I can’t believe you’d do this to me!"
                mc "I own you, bitch. Now tighten that pussy for me.."
                "I couldn't believe this refined lady was getting off on pretending to be raped. And she was {i}really{/i} getting off on it, her pussy was gushing."
            "Her response is a mixture of gasps and moans, her body arching in pleasure. I continue to thrust into her, the intensity building with each stroke."
            if noncon == 1:
                "And the rawness of our roleplay adds to the thrill, driving me closer to the edge."
                rub "Please, stop! I can't take it... It’s too big!"
            else:
                rub "Uoohhh, I-I’m really about to cum already!"
            "Not only was [rub] naturally incredibly tight, but she loved teasingly squeezing even tighter around my shaft, and if that wasn't enough, the plug was somehow making her even tighter than usual. My cock was in pure heaven with every inch massaged from every angle." 
            "But if you thought I felt good, I don't know if it'd compare to the pure euphoria rushing through every part of [rub]'s being. It seems the mock interview setup led to her becoming extremely aroused. I bet she didn't even plan for this, she just couldn't help herself around me." 
            mc "Ngghh, I’m getting close too!"
            if noncon == 1:
                rub "N-No! Please don’t cum inside; it’s mating season! I'll get pregnant for sure!"
                mc "Oooohhh, I'm going to knock you up, bitch!"
            else:
                rub "Aaahhh, cum inside! Fill my fertile pussy up~"
                mc "Ooohhh, cumming!"
            play sound2 cum
            show rub2a v2 e2a cum with c
            play sound2 cum
            with c
            "Her words push me over the brink. With a final, powerful thrust, I reach my climax, orgasmic sensations flooding through me."
            play sound2 cum
            with c
            play sound2 cum
            with c
            rub "Nnghh, that feels so fucking good, darling!"
            show rub2a -v2 e3 
            call camerabreath from _call_camerabreath_35
            call stopbgs from _call_stopbgs_26
            with d
            if noncon == 1:
                mc "Hehe, so good that you couldn't help but break character?"
                rub "Mmmhh… That good~"
            layeredimage rub2b:
                always:
                    "rub2bb [rubb]"
                group lingerie:
                    attribute lingerie:
                        "rub2blingerie"
                    attribute lingerie2:
                        "rub2blingerie2"
                group eyes:
                    attribute e1:
                        "rub2be1 [rubb]"
                    attribute e2:
                        "rub2be2"
                    attribute e3:
                        "rub2be3 [rubb]"
                group cum:
                    attribute cum:
                        "rub2bcum"
                group sex:
                    attribute v1:
                        "rub2bvaginal"
                    attribute a1:
                        "rub2banal"
                group cum2:
                    attribute v2:
                        "rub2bvaginalcum"
                    attribute a2:
                        "rub2banalcum"
                group buttplug:
                    attribute plug:
                        "rub2bplug"
            scene black: 
                ypos 200
            show rub2b e1 lingerie plug cum
            play moans1 moansmisc2
            with d
            "[rub] shifts around onto her back and assumes the next position she wants to be pounded in. She wasn't kidding, she's a lady that knows how to get what she wants, and I'd be lying if I said my cock wasn't rearing to go again." 
            if noncon == 1:
                rub "Oh nyo~ Please don’t rape me~"
                mc "Hahaha! You’ve had plenty of time to pay, [rub]. Now you’re mine~"
            else:
                rub "Don’t you dare stop, dear~"
            menu:
                "Vaginal":
                    $ gent1 = "pussy"
                    play sound2 cum
                    show rub2b v1 e2 with d
                "Anal":
                    $ gent1 = "ass"
                    show rub2b -plug with d
                    "First, I pop out her buttplug, getting a resounding groan from [rub] as it pops out. In her position, she can't quite see what I'm planning, but as the cooling feel of lubricant is suddenly applied to her plug-loosened pucker, she gets a pretty good idea."
                    play sound2 cum
                    show rub2b a1 e2 with d
            "I pushed my throbbing cockhead against her tight little hole, teasing her entrance before I slammed my cock into her, stretching her out more than any stallion had before me. She was so tight around me that I could feel every vein throbbing on my cock, each one begging for release."
            play ambience1 sex
            play moans1 moansmisc1
            camera:
                linear 0.2 zpos -16 ypos -2 xpos 0
                block:
                    linear 0.05
                    linear 0.5 ypos 10
                    linear 0.05
                    linear 0.4 ypos -8
                    repeat
            "She let out a high-pitched yelp of pain mixed with pleasure as I gripped onto her hair hard enough to pull slightly, and I began to pound into her hard and fast, relishing the feeling of her tight [gent1]."
            if noncon == 1:
                rub "{i}Sniffle{/i} I-I’m so sorry! I’ll never do it again~"
                mc "You're my property now. Better get used to it, because I'm going to mold your [gent1] around the shape of my cock."
            else:
                rub "Uooohhhh, holy fuck… You’re such a beast~"
            "My hips slammed into hers again and again, driving my cock deep inside of her. I could feel myself getting close already – the tightness of her [gent1] around my cock was driving me wild."
            "I grabbed hold of her fluffy flank with one hand and squeezed hard as I continued my relentless assault on her tight [gent1]."
            if noncon == 1:
                rub "Ooooh noooo! I-I can’t believe I’m about to cum while I’m getting raped!"
            else:
                rub "Oh god! I-I can’t take anymore! I’m cumming hard!" 
            "She moaned out between gasps of air as her entire body tensed up, her insides contracting tightly around my shaft. I couldn’t last much longer if she kept responding like this."
            rub "Aaahhhh… Cum inside me, baby!"
            play sound2 cum
            if gent1 == "pussy":
                show rub2b v2 with c
            else:
                show rub2b a2 with c
            play sound2 cum
            with c
            "With one final powerful thrust, I came inside of her tight [gent1] – filling her once again with hot, sticky cum."
            play sound2 cum
            with c
            play sound2 cum
            with c
            if noncon == 1:
                "My cock spasmed uncontrollably as wave after wave of hot cum shot deep inside of her once ‘virgin’ hole."
            "I held myself inside of her, savoring the feeling as my orgasm gradually started to subside."
            show rub2b -v1 -v2 -a1 -a2 e3 
            call stopbgs from _call_stopbgs_27
            call camerabreath from _call_camerabreath_36
            with d
            "When I finally pulled out of her [gent1], I couldn’t help but admire my work as a thick trail of cum spilled out of her."
            play sound2 spank
            "I growled seductively before grabbing hold of her hips and pushing her onto her front so I could get a better look at my handiwork. With one final slap on her plump ass cheek."
            "[rub] turns her head back to look at me, a satisfied smile playing on her lips."
            rub "Thank you, darling… That was exactly the type of break I needed… {i}Phew{/i}"
            "I lean over to kiss her, my heart still racing. "
            show rub happy lingerie2 cum 
        "{i}Back Out{/i}":
            $ rub2 = 0
            mc "Sorry, I didn’t realize we were going all the way. I thought you were just giving me an explanation of how the room worked."
            rub "Ah, my apologies, darling. I must have misread the situation."
            show rub happy lingerie2 
    stop music fadeout 3
    scene bg brothel3
    $ textbox = 1
    call camerareset2 from _call_camerareset2_25
    with d
    "[rub] hops up from the sofa and starts to stretch."
    rub "What can I really say except… You have the job~"
    scene bg brothel1 with d
    "At night, you can choose to work at the brothel."
    show mox laughing with d
    "Various characters from Arcadia will appear as customers based on your ranking. The higher your rank, the more affluent the customer, and the more they may be willing to pay." 
    "When you have a customer, you have three important tasks."
    "1. Choose a conversational topic you think they would enjoy. Each girl has her own unique interests."
    menu:
        "Cooking (35 Points)":
            pass
        "Travel (10 Points)":
            pass
        "Hobbies (10 Points)":
            pass
    "2. Answer a question about them correctly. It's important to pay attention to your customers!"
    show mox wink with d
    menu:
        "What is [mox]'s eye color?"
        "Purple (Duh)":
            pass
    "3. Choose a sex position and accessory you think they'd like most. Each character has various fetishes and preferences."
    show mox horny with d
    menu:
        "Missionary (35 Points)":
            pass
        "Pet Play (5 Points)":
            pass
        "Non-Con (0 Points)":
            pass
    "After that, you'll receive a ranking and pay based on your performance."
    "Upgrades are also available, and they can do a variety of things, such as boost your score or reduce the number of incorrect answers that can appear."
    play music clubtheme volume 0.5 fadein 3
    scene bg brothel4
    show rub laughing 
    with d
    rub "I think that’s everything! I know it’s a lot to take in at once, but once you’re out there, you’ll figure things out in no time, darling."
    mc "Thank you so much, [rub]. I hope you have a great rest of your evening."
    hide rub with d
    "[rub] returns to her office, but I know I can’t leave without seeing a certain special someone first..."
    scene black with d
    "'As we move toward this singularity, we will transform our lives...  and ultimately redefine what it means to be human' - Ray Kurzweil"
    mel "Hey, freak shit! Let me be your first customer!" 
    play music melodytheme
    scene bg brothel4 
    show mel smug goth
    with d
    "Her outfit made a bold statement: a black tank top, hugging her form perfectly and exposing a hint of midriff. The short skirt, a vision of gothic charm, flared out slightly with chains." 
    "Lower still, her fishnet stockings—"
    show mel death with d
    mel "Oi! Stop ogling my body! I wore these clothes precisely to curb your rampant eye molestation!"
    mc "Awh, you put these on for me? That’s so sweet! By the way, you look great."
    show mel bashful with d
    mel "Guh – gross! But thanks, that's one compliment I can't refuse. I feel cute ass fuck in this."
    mc "Cute ass fuck?"
    show mel laughing with d
    mel "That was a brain typo! At least you can’t ogle my butt anymore! Bwahaha."
    mc "In this society, it feels like wearing clothing is somehow more inviting, and certainly attention-grabbing."
    show mel smug with d
    mel "Yeah, it does get me a lot of looks. Especially from stallions~ Does that make you jealous?"
    mc "I don’t need to be jealous; I know you have standards."
    show mel bashful with d
    mel "Ehehe..."
    show mel happy with d
    mel "I’m going to be honest. I fuckin’ {i}like{/i} you. Do you have any idea what it’s like to speak and actually be understood for once?"
    mc "It’s not like you make it easy for people."
    show mel wink with d
    mel "Pfft, like you just said, I don’t like to be easy~" 
    mel "Now, are you my host or what? Drinks are on me again tonight, and [aur] knows I need some booze down me tonight."
    stop music fadeout 2
    scene black with d
    "We go downstairs, order some cocktails, and sit at a table to ourselves…"
    scene bg brothel1 
    camera:
        ypos -150 zpos -400
    with d
    play music clubtheme
    mc "So, why did you order the 'most alcoholic drink on the menu'?"
    show mel smug goth with d
    mel "For one, this Meet Your Maykr drink is actually freakin’ delicious. And secondly... I found out that I need some replacement parts."
    show mel happy with d
    mel "If it wasn’t for you, I’m not sure how I’d take that news. But thanks to our last conversation, I feel more comfortable moving forward with the changes."
    mel "So, thank you. I really appreciate that."
    mc "If you don’t mind me asking, what parts need changing?"
    show mel neutral with d
    mel "My arm. It gets the most use and needs the most upkeep. There have been some improvements to the technology too. I’m used to what I have now, but I’m no longer against trying something new."
    mc "Improvements? Like, stronger, faster?"
    show mel bashful with d
    mel "Literally, yeah. I’m right-handed, and my natural right arm is still intact, but my left arm is now stronger, and I’m ambidextrous with it."
    mel "This technology does more than blur the lines between human and machine… They’re kind of improvements."
    mc "Actual improvements? Like getting bigger tits?"
    show mel wink with d
    mel "Pfft, you're joking, but some people actually would. These technologies won't just challenge our limits, but push right past them."
    mel "Unicorns with the might of earth ponies, earth ponies with mechanical wings... And, yeah, flatties like myself with monster milkers."
    mel "Although I know magic is capable doing much the same, I'm curious which of the two will win out in the end. Perhaps the true answer is a harmony of both."
    mc "Hmn... leveling the playing field is an interesting idea. I was thinking more of an increased quality of life for the average person, I, for one, would love to turn on live subtitles whenever I'm talking to someone."
    mc "Improvements like this could be the next step in evolution."
    show mel angry with d
    mel "Hm… The next step in evolution? Or an existential danger to our way of life?"
    mc "You're still uncertain about them? They’ve been beneficial for you."
    show mel neutral with d
    mel "It just occurred to me; I’m going to get an ‘improved’ arm. Faster, stronger, more precise… That would theoretically make me more competitive in a range of society’s roles."
    mel "What if it ever gets to the point where someone normal can’t keep up with me? I take their job; beat them at their sports…"
    mel "And then one day, they say, ‘fuck it,’ and get their own rocket arm and night vision eyes."
    mc "Hmm… I see your point. It could turn into a literal arms race where people are in a cycle of competing for improvements."
    show mel angry with d
    mel "{i}Expensive{/i} improvements, which further exacerbate the growing class divide. The last thing we need right now are new forms of discrimination and societal tension."
    mc "And who will control and distribute this technology? Corrupt individuals prioritizing profit over ethical considerations always rise to the top because they're willing to do the exploitative things no one else will."
    show mel bashful with d
    mel "Ugh… You were supposed to make me feel comfortable about getting a new arm, not disturbed by the entire concept of it!"
    mc "Cynicism aside, I do think these cybernetics are an overall good. Especially for people like yourself, restoring lost functions, enhancing your life, and reducing your dependence on others."
    show mel smug with d
    mel "Yeah, you’ve got me there. There’s nothing wrong with the tech, it’s people that are fucked."
    mc "Are you interested in helping the world?"
    show mel neutral with d
    mel "Huh? That’s a random question. Hm… ‘Fuck no’…"
    show mel bashful with d
    mel "Is what I’d say before our lil chats. Now? I’d be tempted, depending on what you had in mind."
    mc "I think you should help [rub] run the brothel."
    show mel angry with d
    mel "Wha?! Fuck no!"
    mel "Why would I want to associate myself with this sleazy place?"
    mc "The sleazy place you lounge around in almost every evening, chatting to folks and enjoying its booze?"
    show mel neutral with d
    mel "I guess those parts aren't so bad..."
    mc "You’re thinking too small. You wouldn’t just be ‘associating’ yourself with this place; you’d be {i}running{/i} it alongside your sister."
    show mel angry with d
    mel "Well! … I! … I’m not sure…"
    mc "You clearly like the idea. What's holding you back?"
    show mel sad with d
    mel "Because… I despise this place. It's a constant reminder of how much my sister sacrificed for me."
    mc "So, are you ready to give back to her?"
    show mel neutral with d
    mel "What do you mean?"
    mc "I spoke to her, and I can tell she's weary."
    mc "She needs someone who understands her, the business, and the toll it's taken on her."
    mc "Even more than that, she needs a week off, at least."
    show mel neutral with d
    mel "Hmm… You know what? You’re absolutely right..."
    show mel bashful with d
    mel "I’ve been sitting here feeling sorry for myself instead of getting shit done."
    show mel smug with d
    mel "I’ll do it. I’ll be the best assistant in the damn city for my sis!"
    show mel bashful with d
    mel "But, uh... I have no clue how to manage anything. I hope [rub] doesn't mind showing me the ropes."
    mc "I'm sure she'd be more than willing, especially if it means getting a break now and then."
    show mel happy with d
    mel "No doubt about that, man…"
    show mel wink blush with d
    mel "Say, are you just about ready to head into a booth?"
    "I raise an eyebrow, finish my drink quickly, and nod."
    mc "What did you have in mind?"
    show mel smug with d
    mel "Pft, wouldn’t you like to know, wormy boy~"
    stop music fadeout 3
    scene black 
    call camerareset2 from _call_camerareset2_26
    with d
    "I followed [mel] through the dimly lit corridors of the brothel. She turned her head back every so often, as if checking if I was still there and giving me a mischievous grin."
    "She pushed open the curtains to the same booth as before and gestured for me to enter."
    scene bg brothel3
    show mel happy goth blush 
    with d
    mel "Go on, I have a special treat for you today."
    "As I stepped inside, she closed the curtains behind us and sauntered over to me, her hips swaying with each step."
    mc "Planning something diabolical, no doubt."
    show mel smug with d
    mel "Oh, you’ll see…"
    "She purred, her fingers trailing down my chest, before suddenly prodding me forward and towards the couch."
    mel "Sit down."
    hide mel with dissolve
    layeredimage melody2a:
        always:
            "mel2ab [melb]"
        group eyes:
            attribute e1:
                "mel2ae1 [melb]"
            attribute e2:
                "mel2ae2 [melb]"
            attribute e3:
                "mel2ae3 [melb]"
        group pregnant:
            attribute pregnant:
                "mel2apregnant"
        group sex:
            attribute sex1:
                "mel2asex"
        group cum:
            attribute cum:
                "mel2acum"
        group cum2:
            attribute hj2:
                "mel2ahjcum"
            attribute sex2:
                "mel2asexcum"
        group clothes:
            attribute goth:
                "mel2aclothes [melb]"
        group hj:
            attribute hj:
                "mel2ahj"
    play music melodysextheme
    show melody2a e1 goth
    call camerabreath from _call_camerabreath_37
    play moans1 moansmisc2
    $ textbox = 2
    with dissolve
    "I obeyed, sitting in the plush couch in the center of the room. She climbed onto my lap, straddling me with her thighs spread wide, her skirt rode up, giving me a tantalizing glimpse between her legs that fell just inches short of the good stuff."
    "As if that wasn’t enough, she pulled her tank top back and flashed one of her breasts. Somehow, flashing it like this was even sexier than the nudity I’d become accustomed to." 
    "She leaned in close, her breath warm against my ear…"
    mel "Today, you’re going to…"
    "She whispered, her lips brushing against my earlobe."
    mel "…take my virginity~"
    menu:
        "{i}Continue{/i}":
            label b2m1:
                $ mel2 = 1
            show melody2a hj with d
            "Her left hand slipped between us. I could feel her fingers brush against my growing erection, sending jolts of pleasure through my body. She began jacking me off, her eyes gleaming with delight at the sight of my hardness."
            mel "Looks like someone's excited! Don't worry. I'll take good care of you."
            show melody2a e2 with d
            "She giggled, wrapping her fingers around me. She began to stroke me slowly, her grip firm and confident."
            "The strokes quickened, her hand moving with practiced precision. I could feel the heat building under her skirt."
            "She leaned back slightly, giving me a better view of her lithe body as she worked me with her hands. Her eyes never left mine, and her smile grew wider as she saw the effect she was having on me."
            show melody2a e1 with d
            mel "Hehe, your expressions are so gross! It makes you so easy to read…"
            "I could only nod, my breath coming in ragged gasps. [mel]’s touch was driving me crazy, and I was powerless to resist her."
            mel "Well, tonight's your lucky night."
            show melody2a e2 with d
            "She increased her pace, her hand moving faster and faster. The friction and the pressure of her closeness were too much to bear. I could feel the tension building inside me, ready to explode at any moment."
            mel "Go ahead, loser. Let go. I want to see you lose control."
            play sound2 cum
            show melody2a hj2 cum e3 with c
            play sound2 cum
            with c
            "Her words were the final push I needed. With a shuddering gasp, I felt the climax hit me like a tidal wave. [mel]’s hand never stopped moving, milking every last drop from me as I convulsed beneath her."
            play sound2 cum
            with c
            play sound2 cum
            with c
            "As the waves of pleasure subsided, she sat back, a satisfied smirk on her face. "
            "As I sat there, trying to regain my breath and composure, [mel] reached over to the table in the center of the room, grabbing the small bottle of lubrication and giving me a sly grin."
            mel "Get hard again. We’re not even close to done."
            scene black with d
            "She teased as she squeezed some of the lubricant on her hand and began to spread it over my length. I shivered from the chilly sensation and stared, entranced, as she climbed back into my lap."
            layeredimage melody2b:
                always:
                    "mel2bb [melb]"
                group eyes:
                    attribute e1:
                        "mel2be1 [melb]"
                    attribute e2:
                        "mel2be2"
                    attribute e3:
                        "mel2be3 [melb]"
                group cum:
                    attribute cum:
                        "mel2bcum"
                group action:
                    attribute v1:
                        "mel2bactionlines"
                    attribute a1:
                        "mel2bactionlines"
                group sex:
                    attribute v1:
                        "mel2bvaginal"
                    attribute a1:
                        "mel2banal"
                group cum2:
                    attribute v2:
                        "mel2bvaginalcum"
                    attribute a2:
                        "mel2banalcum"
                group clothes:
                    attribute c1:
                        "mel2bclothes 1"
                    attribute c2:
                        "mel2bclothes 2"
                    attribute c3:
                        "mel2bclothes 3"
                group milky:
                    attribute m1:
                        "mel2bminimilk"
                    attribute m2:
                        "mel2bbigboobs"
                group milky2:
                    attribute m2:
                        "mel2bmegamilk"
            show melody2b c1 e1 with d
            "Positioned directly over me, with her skirt hiding everything from view, all I could go on was the feeling of heat emanating from below her."
            mel "You ready? You’re about to take my first time~"
            "My heart raced as I felt the tip of my erection brushing against her. She looked down, briefly unsure and biting her lip in a way that almost made her look innocent."
            mel "And I’m glad it’s you. I want it to be you."
            play sound2 cum
            show melody2b a1 e2 
            play moans1 moansmisc3
            $ textbox = 4
            with d
            "Slowly, she began to lower herself onto me. The tightness was almost overwhelming, and I let out a groan as I felt myself being enveloped by her warmth. She moved cautiously, inch by inch, her breathing becoming more labored."
            mel "Ooohhh, this… actually feels so… good!"
            camera:
                linear 0.2 zpos -18 ypos -2 xpos 0
                block:
                    linear 0.05
                    linear 0.5 ypos 8
                    linear 0.05
                    linear 0.4 ypos -8
                    repeat
            "I was lost in the sensation, barely able to think straight as she started to ride me. The way she moved, the way she felt – it was hypnotic. Her skirt swayed with each movement, teasingly hiding our connection from view."
            mc "Oohhh, [mel]! You’re so tight!"
            "I groaned, my hands instinctively gripping her hips to steady her. She picked up the pace, her movements becoming more confident."
            mel "Nngghhh, you’re so deep~ I didn’t know it would feel like this!"
            "I was completely under her spell, each of her words and movements driving me closer to the edge. But just as I was about to lose myself completely, [mel]’s expression changed." 
            show melody2b e1 with d
            "Her eyes gleamed with mischief as she looked down at me, her enthusiastic riding not missing a beat."
            mel "Hey, worm~"
            "She whispered, a wicked smile spreading across her lips."
            mel "Wanna see something?"
            "Before I could respond, she reached down and flipped up her skirt..."
            show melody2b c2 with d
            "My eyes widened in shock and realization as I saw where we were truly connected. It wasn't her pussy at all – it was her ass that had been pleasuring me this whole time."
            show melody2b e2 with d
            mel "Bwahaha! You should see the look on your face! Did you really think I'd give you my first time like that?"
            "I was speechless, my mind racing to catch up with the situation. The tightness, the intensity – it all made sense now. And despite the shock, I couldn't deny the raw pleasure of it."
            mc "[mel], you…"
            show melody2b e1 with d
            mel "Don't act so shocked, dweeb~ Just enjoy it."
            show melody2b e2 with d
            "She teased, intensifying her movements. Her confidence and control were undeniable. She rode me with renewed vigor, her skirt now flipped up and giving me a clear view of everything. The sensation was overwhelming, and I couldn't hold back any longer."
            mel "Mmphhhhh... Fuck... Are you getting even harder now that you know the truth~?"
            "With a groan, I felt myself reaching the peak, the pleasure too intense to resist. [mel]’s moans echoed in my ears, her body moving with relentless rhythm."
            mc "Ngghh, I’m about to cum!"
            show melody2b e1 with d
            mel "That’s right! Cum for me, pathetic worm!"
            play sound2 cum
            show melody2b e2 cum a2 with c
            play sound2 cum
            with c
            "As I finally released, she continued to ride me, drawing out every last drop of pleasure. Her eyes sparkled with triumph as she watched me, fully aware of the power she held over me."
            play sound2 cum
            with c
            play sound2 cum
            with c
            mel "Mmhhh… All that cum, filling my virgin ass~"
            call camerareset1 from _call_camerareset1_8 
            show melody2b e3 with d
            mel "Hehe, see? I didn’t lie about everything; you really are taking one of my virginities. Aren’t you lucky?"
            layeredimage melody2c:
                always:
                    "mel2cb [melb]"
                group clothes:
                    attribute c1:
                        "mel2cgoth"
                group lingerie:
                    attribute lingerie:
                        "mel2clingerie"
                group pantyhose:
                    attribute pantyhose:
                        "mel2cpantyhose"
                group eyes:
                    attribute e1:
                        "mel2ce1 [melb]"
                    attribute e2:
                        "mel2ce2"
                group cum:
                    attribute cum:
                        "mel2ccum"
                group sex:
                    attribute v1:
                        "mel2cvaginal"
                    attribute a1:
                        "mel2canal"
                group sex2:
                    attribute v2:
                        "mel2cvaginalcum"
                    attribute a2:
                        "mel2canalcum"
                group plug:
                    attribute plug:
                        "mel2cplug"
            show melody2c e1 c1 with d
            "She turned around, her back now facing me, and bent over slightly, giving me a perfect view of her ass framed by the short, pleated skirt. This time, her fishnet tights were removed, her fluffy toes wriggling in the open."
            if rub1 == 1 or rub2 == 1:
                mel "Don’t think you’re off the hook just because you came… I still have to get you back for going balls-deep with my sister~"
            else:
                mel "Don’t think you’re off the hook just because you came… I still have a few tricks up my sleeve."
            show melody2c a1 e2 with d
            play moans1 moansmisc1
            camera:
                linear 0.2 zpos -18 ypos -2 xpos 0
                block:
                    linear 0.05
                    linear 0.5 ypos 8
                    linear 0.05
                    linear 0.4 ypos -8
                    repeat
            "She slowly began to lower herself back onto me, this time with her ass in full view. She adjusted herself, guiding me back into her with ease, her movements even more confident now. The sight was incredible; her back arched and her skirt barely concealed anything."
            mel "You fucking loved my ass and feet so much, that I thought I’d give you the full three course meal."
            "She started to move again, her hips swaying and her feet brushing against my thighs. The new angle was incredible, each movement sending sparks of pleasure through my body. I couldn't help but reach out, my hands resting on her hips to steady her."
            mc "Oohhh, [mel], you feel amazing!"
            show melody2c e1 with d
            mel "Bitch, I know it. Just enjoy the ride~"
            show melody2c e2 with d
            "She picked up the pace, her movements becoming more vigorous. The way her body moved, the way she looked back at me with those teasing eyes – it was all too much. I could feel the tension building again, the pleasure intensifying with each thrust."
            mel "I knew you’d love this… Don’t you? You’re such a filthy pervert."
            "I could only nod, lost in the sensation. She was in complete control, her every movement driving me closer to the edge. She shifted slightly, her back arching more, and I could feel her even deeper."
            mel "Nnghhh… Aahhhhh… I’m going to drain those balls dry!"
            "I clearly wasn’t the only one enjoying it. [mel]’s fingers clenched tighter into my thighs as her lithe frame barely managed to contain the pleasure coursing through it. She’d been going at this for a while now, it wouldn’t surprise me at all if she was close to cumming." 
            mc "I’m getting close again!"
            mel "Good…  Aahhh… Let it all out! Mhh - I want to feel it!"
            play sound2 cum
            show melody2c a2 cum with c
            play sound2 cum
            with c
            "The intensity of her words and movements pushed me over the edge. With a final a burst of speed, we both reached climax, the pleasure overwhelming. She continued to rock her hips, drawing out every drop of pleasure."
            play sound2 cum
            with c
            play sound2 cum
            show melody2c e1 with c
            mel "Oohhh, f-fuck! Y-You’re still cumming {i}this{/i} much?!"
            play sound2 cum
            with c
            play sound2 cum
            with c
            "As she was cumming, I couldn’t believe how tight her ass got - was she cumming too? - it easily spurred on my third orgasm to be just as powerful as my others." 
            call camerareset from _call_camerareset_11
            stop music fadeout 10
            call stopbgs from _call_stopbgs_28
            show melody2c -a1 -a2 with d
            "And after I finished unloading, it was obscene how much cum seeped from our point of contact. It’s lucky that [mel] has white fur, really." 
            "As I came down from the high, she slowed her movements, eventually stopping. She looked back at me, a satisfied smile on her face."
            "Although It was clear she was finally spent; panting and weary, her mind reeling from the experience."
            scene bg brothel3 
            $ textbox = 1
            with d
            "Standing up, [mel] adjusted her skirt in such a way that it hid all the cum, and gave me one last teasing glance before stepping out of the booth, leaving me to process everything that had just happened."
            "As I sat there, trying to catch my breath, I couldn't help but feel a mix of awe and anticipation. I had foolishly thought that [mel] no longer had anything left to trick or surprise me. But now I knew that this was only the beginning of her games."
            "Still… I can’t believe she just left. Wasn’t she covered in cum?"
            show mel smug goth with d
            mel "Here’s a towel, nerd."
            "Popping in with a dramatic entrance through the curtains, [mel] suddenly tosses a white towel into my face."
            show mel bashful blush with d
            mel "I think even I got a bit caught up in my heat for a while there."
            mc "Which parts? To me, that entire thing seemed crazy."
            show mel laughing with d
            mel "I wasn’t expecting to ride you twice, but it felt so good I couldn’t resist trying to make myself cum."
            mc "That was a pretty incredible performance for your first time~"
            show mel wink with d
            mel "Hmph, go shower, before I smother you with that towel."
            mc "There are showers?"
            show mel happy with d
            mel "Of course there are showers. Just down the hall are three cubicles."
            mc "Alright, I’ll hop to it. See you around, [mel]."
            show mel laughing with d
            mel "I hope so."
        "I don’t know…":
            $ mel2 = 0
            mel "W-what?! How can a guy say no to something like that? I even wore this just for you!"
            mel "If we don’t do anything, it’ll ruin what I have planned… It’ll be really good, I {i}promise{/i}!"
            menu:
                "Alright, you won me over.":
                    jump b2m1
                "I’m just not in the mood.":
                    scene bg brothel3 with d
                    mel "I… Uh… I guess that’s fine."
                    show mel goth neutral with d
                    "[mel] gets off me and seems a little dead inside. She seems to genuinely {i}really{/i} like me, and my sudden refusal hit hard."
                    mel "I’m gonna go get some air… See you."
                    hide mel with d
                    "She leaves in a hurry."
                    scene black with d
    scene bg black with d
    "After finishing my business in the brothel, I return to [mox]’s apartment, and I get to enjoy some of her late-night cooking."
    play music moxietheme 
    scene bg apartment
    show mox laughing with d
    mox "Pretty tasty, eh?"
    mc "I’ve finally found someone to rival the cooking of my [mox]. Another [mox]."
    show mox smug with d
    mox "Ahaha! I’m honored that my only competition is myself." 
    mox "I suck at most things, but I’ve been performing and cooking since I was a filly."
    mc "Suck at most things? Well, if you could enhance your body cybernetically in any way, what do you think you’d go for?"
    show mox happy with d
    mox "Oooo, I hear that’s a burgeoning industry at the moment. Can’t say I know what I’d want to improve practically, but I have a few ideas theoretically."
    mc "You do? That sounds very technical."
    show mox bashful with d
    mox "Oh, dude, you’re thinking way too highly of me. I’m literally thinking of a pair of gigantic robot breasts."
    mc "You want giant breasts? Yours are beautiful as they are."
    show mox wink with d
    mox "Ah, but now you’re thinking too lowly of me. I’m talking about temporary adjustments. For instance, one evening while we’re making love, I could wear my normal breasts, but another evening I could wear my mega milker 3,000s."
    mc "Oh, wow! Okay, I can definitely see the appeal now. (But why does it always come back to mega milkers?)"
    show mox horny with d
    mox "Think of that potential! It’s not just breasts; it’s every body part, and even body parts you don’t have! What if you had {i}two{/i} dicks? What if {i}I{/i} had a dick? The limit is our imagination!"
    scene black with d
    "[mox] rants about cybernetic sex mods for at least thirty minutes before we head to bed."
    if replay == 1:
        return
    $ brothelroute2 = 1
    $ brothelcompletion += 1
    $ completion += 1
    jump newday
label brothel3:
    stop music fadeout 1
    play ambience1 ambiencenight
    scene bg brothel5 with d
    "The office was still, save for the low drone of the air conditioning and the sporadic clatter of keys."
    "It was late, far later than I expected anyone to still be working here. Sure, the club is bustling at night, by the office?"
    mc "[mel]? What are you doing up here?"
    "Apparently she hadn’t heard me come in, so she jumped a little when she heard me."
    play music melodytheme fadein 1
    show mel bashful with d
    mel "Ack! My stalker is back! Security! Security!"
    mc "Hey, keep it down! Julie would actually kick my ass if you told her to."
    show mel laughing with d
    mel "Bwahaha, Julie’s the least of your problems when you’re dealing with me."
    mc "Ain’t that the truth. But it’s late. You been here all day?"
    show mel happy with d
    mel "Yeah, just wrangling schedules, keeping the staff in line. The usual grunt work while I learn the ropes. It’s not much, but it’s something."
    mel "Honestly, I’ve just been idling here now. Feels good to have a purpose, even if it’s something small and silly like this. Beats sitting at the bar watching people drift in and out."
    mc "Must’ve been boring as hell with nothing to do. Figured you might’ve gone to college or something by now."
    show mel neutral with d
    mel "College? Maybe in some other life. This suits me fine. I know the staff, they know me. Feels like I’m actually doing something that matters."
    "There was something about the way she said it, the genuine warmth in her voice, that made me realize just how much this meant to her."
    show mel smug with d
    if mel2 == 1:
        mel "What brings you here anyway? Not hoping for more of that sexy business, I hope? Don’t forget, you’re only good enough for my butt~"
    else:
        mel "What brings you here anyway? Not hoping for more sexy time, I hope? Don’t forget that you’re only good enough for my feet~"
    mc "And you’re only good for your butt! Not exactly the type for a boob job with that wooden board of yours, are you?"
    show mel laughing with d
    mel "Tsk. You’d think a hairless ape would have a better appreciation for butts. They’re the original sexy asset!"
    mc "Sometimes, during these conversations, I think animals gaining sentience was a mistake."
    show mel wink with d
    mel "Even if I was a horse on a ranch, I’d still get my kicks by nipping at your balls."
    mc "Don’t even think about it!"
    show mel death with d
    mel "So, what brings you to the office? Here to bang my sister?"
    mc "I’m actually here to see how those upgrades turned out."
    show mel bashful with d
    mel "You actually remembered? Well, that’s… sweet of you."
    "Her bravado seemed to waver, as if she were caught off guard by the sentiment."
    show mel happy with d
    mel "You know, it’s hard to keep up the bullying act when you’re so… damn… kind. Makes me wonder if this thing between us might turn serious."
    mc "It could be, if that’s what you want. But you don’t have to drop your edge. It’s what makes you… you. It’s what makes you interesting."
    show mel bashful with d
    mel "Interesting, huh? Maybe that’s why you might just be the one."
    show mel happy with d
    "She looked at me, really looked. Tenderness from [mel] was rare, making moments like this so precious."
    show mel laughing with d
    mel "You know, I keep my guard up around others. No one else can handle my prickly nature. But you’re different. You get me. You speak my language."
    mc "Most folks see only the thorns, but I see the rose too."
    show mel death with d
    mel "Ewwww! I’d rather be a cactus! At least then I’d be useful for keeping people at a distance! And when necessary, shoved up—"
    mc "{i}Eh-hem{/i} So, [rub] has you working with the staff despite your... 'weaknesses' as an employee?"
    show mel wink with d
    mel "Tsk, you’re not supposed to say those parts out loud! Though, I’d be lying if I said I didn’t think it myself."
    mel "I reckon it’s to give me practice with people in a working setting. It makes sense, given how much of my life I’ve spent skirting around people. My angst was always a reliable shield."
    mc "Why the need to push people away?"
    show mel neutral with d
    mel "I despise what this place has become... It’s supposed to be a boutique!"
    mel "My rudeness was initially just… childish attempts to lash out and discourage people from coming here."
    stop music fadeout 10
    mel "But the real reason I push people away, what it all boils down to, is the incident that caused my injuries."
    mel "I’ve only shared this with [rub] and my doctors, but I want to tell you too." 
    "I reached out, took [mel]’s hands in my own, and nodded."
    mc "I’m here for you. You can tell me anything."
    show mel bashful with d
    mel "Tch, you’re so cliché… {i}Phew{/i} Here goes…"
    play music sad fadein 3
    show mel angry with d
    mel "When I was young, there was a split between my parents. [rub] stayed here in Arcadia because she had already bought property, but I went to live in Maplewood with my mother."
    mel "The nightmares… they took more than just my body back there. They took mother, too."
    mc "Nightmares suddenly appeared? You didn’t have time to evacuate?"
    show mel neutral with d
    mel "There were plans to evacuate eventually. They figured the darkness would claim the city in a few years. But this... this was sudden. In the dead of night, the city was overrun with nightmares."
    mel "I was half nightmare by the time they pulled me back. The only cure they had was to cut away the infected parts."
    mc "That’s awful. I’m so sorry."
    show mel sad with d
    mel "I was one of the few who survived. I became a ‘useful’ subject for the scientists, and they gave me the best care they could. But once they were done, I was bedridden, and [rub] looked after me for a year."
    mel "It was a humiliating time, but at least it was just us. Little did I know, the ground floor of the building was changing. [rub] scraped together every bit of money she could to give me a semblance of normalcy."
    mel "She succeeded, and I got my body back, but the last thing I wanted in such a fragile state was my own home swarming with strangers. Strangers who came to gawk and judge."
    mel "And all that was meant for me? I thought it was a cruel joke... But now, it’s painfully clear how ungrateful I was."
    mc "It’s hard to fault you for feeling that way. Regaining your independence doesn’t erase the pain. Some never recover from something like that. You’ve been stronger than most."
    show mel smug with d
    mel "Heh… You only think I’m strong because you’ve only known the {i}me{/i} that came after I met {i}you{/i}."
    show mel bashful with d
    mel "You quelled my rage. You opened my eyes to the idea that with a little more openness, a dose of sex positivity, and treating others with respect… Well, things can change."
    "She gestures towards the computer."
    show mel happy with d
    mel "This is it. This is the change. I can make amends with my sister and with those who stood by me in the hard times."
    mel "I really couldn’t have done this without you. So..."
    mel "Thanks. No quips this time. Just a plain, honest thank you."
    mc "Man… You’re fucking incredible, you know that?"
    show mel neutral with d
    mel "Eh?"
    mc "You can give me all the credit you want, but this? This is {i}all{/i} you."
    show mel happy blush with d
    "[mel] stands speechless, a blush spreading across her face as she stares at me."
    mel "(Well. That’s it. I’m in love.)"
    mel "(Me… Who would have thought?)"
    mel "(But… isn’t this guy also sleeping with a bunch of other mares, including my sister?)"
    mel "(I need to show him I can keep pace with these other broads.)"
    mel "{i}Clears throat{/i} With all that said… I’m going to try to behave from now on. At least in the public eye~"
    mel "Look at me, I’m an office lady now! Which means I need a target for all that pent-up bullying I won’t be doing to anyone else."
    mc "Don’t you worry, [mel]. I can take it."
    camera:
        linear 2 zpos -350 ypos -150
    "She stepped closer, her head tilting up to hold my gaze. She was a foot shorter, but in that moment, she felt like she towered over me."
    show mel happy blush with d
    mel "Oh yeah? If you like it that much, maybe I’ll stop playing around and show you what I can really do."
    "I could feel the tension and heat between us rising. I realized that if I got hard now, it’d press right against her. She closed the gap, her hips swaying as she moved in, until our bodies touched."
    show mel smug with d
    mel "Ah, there it is… I can feel your little friend twitching. Can’t believe I can get you going this fast. You must want me bad."
    mc "And what about you? Show me how badly you want me."
    layeredimage mel3a:
        always:
            "mel3ab [melb]"
        group eyes:
            attribute e1:
                "mel3ae1 [melb]"
            attribute e2:
                "mel3ae2"
            attribute e3:
                "mel3ae3 [melb]"
        group cum:
            attribute cum:
                "mel3acum"
        group lingerie:
            attribute lingerie:
                "mel3alingerie"
            attribute lingerie2:
                "mel3alingerie2"
        group plug:
            attribute plug:
                "mel3aplug"
        group pregnant:
            attribute pregnant:
                "mel3apregnant"
        group sex1:
            attribute v1:
                "mel3av1"
            attribute a1:
                "mel3aa1"
        group sex2:
            attribute v2:
                "mel3av2"
            attribute a2:
                "mel3aa2"
    show mel3a e1 
    call camerabreath from _call_camerabreath_67
    play music melodysextheme
    play moans1 moansmisc2
    $ textbox = 4
    with dissolve
    "She shrugged, turning to lean against the desk. Each movement was slow, deliberate, as she bent over and revealed her pussy, dripping wet and ready."
    "There was a contradiction in her approach that I couldn’t ignore. She was in control, but the way she displayed herself carried a hint of submission."
    "Yet, [mel] had a way of flipping the script, making even the most vulnerable positions feel like power plays. Tonight was no different. She eased back into my crotch, her hips moving with a grace that was almost predatory. The heat of pussy gracing my shaft was exquisite."
    show mel3a e2 with d
    mel "Fuhuhu, you remember last time, don’t you?"
    if mel2 == 0:
        mel "I was only planning on giving you my anal virginity."
    "Her voice dropped to a sultry whisper, laced with that teasing edge I knew so well. She lowered herself just enough for my tip to brush against her pucker."
    show mel3a e1 with d
    if mel2 == 1:
        mel "Mmmhh, you seemed to enjoy my ass so much…"
        mc "How could I forget? I really thought I took your virginity then."
    else:
        mel "Mmmhh... I bet you would have loved my ass..."
    "Her butt raised again, this time my tip slid against the wet heat of her pussy, the slickness of her desire coating me. Every movement pressed me closer, teasing, threatening to pull me in."
    show mel3a e3 with d
    mel "Oh my~ This time, you won’t miss, will you?" 
    "Her eyes locked on mine, a challenge within them, daring me to take that final step. I reached out, fingers brushing against the soft fur of her butt, and she let out a breathless gasp."
    "She took my hand then, guiding it with a confidence that left no room for hesitation. Together, we aligned my cock with her pussy, the tip nestled against her entrance, each shift of her hips drawing me closer. I could feel it, the way I sank a little deeper each time she moved."
    "The warmth of her, the way she began to stretch around me, was like nothing else. I could sense her body yielding, growing more desperate, her need palpable. I knew I could slip inside her in an instant."
    show mel3a e1 with d
    mel "Don’t hold back. I want all of you. Make me feel it."
    mc "You have no idea how much I want you. Ready?"
    play sound2 cum
    show mel3a v1 e2 
    $ textbox = 5
    with d
    "She nodded, biting her lip as I began to press forward, sliding into her slowly. The sensation defied words, a perfect blend of pleasure and connection. Her eyes widened, a gasp escaping her lips as I pushed deeper, lost in the moment."
    camera:
        linear 0.1
        linear 0.4 xpos -6
        linear 0.1
        linear 0.3 xpos 6
        repeat
    with d
    play ambience1 sex
    play moans1 moansmisc3
    "Even though she was slick with arousal, she was tight, too tight for me to push all the way in. With only half of my cock inside her, I had to take it slow, using shallow thrusts while she eased around my girth."
    mel "Uooohhh, fuck! I didn’t expect you to be {i}this{/i} big!"
    mel "I never mentioned it ‘cause it didn’t fit my teasing routine, but you really do have a ridiculous, monster cock, you know that?"
    "Thrusting inside once again, I manage to take her to the hilt, my glans grinding against her deepest and most sensitive parts. The sudden rush of pleasure had her fingers desperately gripping to the desk for support."
    play sound2 spank
    mc "You seem to be handling it pretty well! Taming the beast, eh? {i}Spank{/i}"
    show mel3a e3 with d
    mel "Nnngghh… don’t get cocky! I’m the one in control!"
    show mel3a e2 with d
    "As she grew more comfortable, she began pushing her hips back into me, urging me to go deeper still. Her body responded to every movement with rebellious counters to my thrusts."
    "But in this back-and-forth, the rhythm we found was perfect, a dance of desire. I could feel her pussy squeezing around me in that intentional teasing way her sister would often do, her breaths coming in short, ragged gasps."
    mel "Aaaahhhh… [mc]… I wanted this so much; I want you."
    "Her voice was desperate, pleading, and I had no intention of stopping. I could feel my own release building, a wave of pleasure threatening to crash over me. But I held on, determined to give her everything she needed."
    mc "I’m already getting close!"
    show mel3a e3 with d
    mel "Mmhh… Hold on a little longer! I’m almost there too!"
    "Her eyes met mine, filled with a mix of love and lust. I nodded, her body trembling beneath me as I pounded her marshmallow butt at a pace she struggled to match."
    show mel3a e2 with d
    mel "Uoohhh, yes! That’s it! Aaaahhh, cumming!!"
    play sound2 cum
    show mel3a cum v2 with c
    play sound2 cum
    with c
    "As she cried out, I stopped holding back, and immediately the tremendous pleasure of my orgasm crashed over me in waves."
    play sound2 cum
    with c
    play sound2 cum
    with c
    "Her body shook under me, tensing wildly with such intensity that it was hard to even continue thrusting. Her orgasm was so raw that I almost felt jealous at the visible bliss coursing throughout her."
    play sound2 cum
    show mel3a -v1 -v2 e3 with d
    stop ambience1
    call camerabreath from _call_camerabreath_68
    play moans1 moansmisc2
    "I pulled out and took a moment to admire her flank while catching my breath. She was still trembling, her body quivering from the aftermath of her release, but the hunger in her eyes hadn’t dimmed. If anything, it had grown fiercer, a fire that refused to be extinguished."
    layeredimage mel3b:
        always:
            "mel3bb [melb]"
        group eyes:
            attribute e1:
                "mel3be1 [melb]"
            attribute e2:
                "mel3be2"
            attribute e3:
                "mel3be3 [melb]"
        group cum:
            attribute cum:
                "mel3bcum"
        group lingerie:
            attribute lingerie:
                "mel3blingerie"
        group plug:
            attribute plug:
                "mel3bplug"
        group sex1:
            attribute v1:
                "mel3bv1"
            attribute a1:
                "mel3ba1"
        group sex2:
            attribute v2:
                "mel3bv2"
            attribute a2:
                "mel3ba2"
        group futa1:
            attribute f1:
                "mel3bfuta [melb]"
        group futa2:
            attribute f2:
                "mel3bfutacum"
    show mel3b e1 cum with d
    "With a quick, fluid motion, she hoisted herself up the desk. Her hands braced against the wood, and she looked at me with a challenge in her eyes, legs lifted high."
    mel "I’m not done with you yet. I want more~"
    "The low growl of her words was a command, not a request. My hands slid along her thighs as I got back into position, my cock mere moments from being ready to go once again."
    play sound2 cum
    show mel3b v1 e2 with d
    "I lined myself up, her body inviting me to claim her again, and then I pushed in, savoring the feeling while she gasped as I filled her once more."
    camera:
        linear 0.1 zpos -12
        linear 0.4 ypos -6
        linear 0.1
        linear 0.3 ypos 6
        repeat
    play ambience1 sex
    play moans1 moansmisc4
    with d
    "Her head fell back, her back arching as I buried myself to the hilt with ease this time. The position made her pussy feel impossibly tight, every thrust drawing out a quivering breath from her lips."
    mel "Yes... oh, yes... just like that..."
    "Her voice was breathless, each word punctuated by the slap of our bodies meeting, the desk creaking beneath us. Her hands desperately held her legs up, fingers digging into the fur as she held on, her body rocking with every powerful thrust."
    "I leaned over, capturing her lips in a fierce kiss, swallowing her moans as I relentlessly bullied her pussy. Her legs shook, struggling to stay upright, and I knew she was close, so close."
    mc "Cum for me, [mel]!"
    "The words were a whisper against her lips, and they pushed her over the edge. She cried out, her voice breaking as she came, her insides clenching around my shaft with an intensity that pulled me along with her."
    play sound2 cum
    show mel3b v2
    show internalcreampie
    with c
    play sound2 cum
    with c
    "The world narrowed to this moment, to the feel of her, the sound of her, the way she shattered beneath me, and then I was falling too, lost in the heat of our climax."
    play sound2 cum
    with c
    play sound2 cum
    with c
    "My release came like a storm, fierce and overwhelming, crashing through me as I thrust deep, holding her close as the pleasure took over. Her name was a moan on my lips, mingling with her own cries of pleasure, our bodies locked together in a final, glorious moments of ecstasy."
    show mel3b -v1 -v2 e3
    hide internalcreampie
    stop music fadeout 3
    call stopbgs from _call_stopbgs_39
    call camerareset from _call_camerareset_18
    with d
    "When it was over, we collapsed together, spent, and breathless, her body still trembling beneath mine. I pulled out of her, feeling the last shudders of my climax."
    mel "That… was incredible."
    mc "You’re damn incredible yourself."
    scene bg brothel5 
    play ambience1 ambiencenight
    $ textbox = 1
    with d
    "The room was quiet now, the intensity of our passion fading into the background as we lay there together, bodies still entangled, a perfect stillness settling over us. There was nothing left to say; the connection between us spoke louder than words ever could."
    "Although, obviously, [mel] wasn’t one to keep quiet for long."
    show mel cum blush smug with d
    mel "{i}Pant, pant{/i} That was wild! You really do hump like a crazed virgin."
    mc "Please, you were the crazed virgin this time. You should’ve seen the way your hips were moving!"
    show mel laughing with d
    mel "Only because you couldn’t keep up! Tsk, tsk. Can’t believe I’m already outperforming you in bed."
    mc "You can outperform me anytime you want, if only I could be so lucky."
    show mel wink with d
    mel "Oh, but you are that lucky, wormy boy~"
    scene bg brothel5
    camera:
        linear 2 zpos -400 ypos -150
    "She lets out a satisfied sigh, leaping onto a chair and throwing her feet up on the desk."
    show mel laughing cum with d:
        xalign 0.25
    mel "For once in my life, everything’s looking up."
    play sound2 equip
    "[rub] steps into the office, a bag in each hand, and drops them in the corner with a relieved huff."
    play music rubytheme fadein 3
    show rub happy with d:
        xalign 0.75
    rub "Ah, [mc], darling! Great to see you. And [mel], thank you so much for your hard work today." 
    rub "It’s a real relief having someone reliable to cover for me. I’d never have been able to go shopping on a busy day like this."
    show mel happy with d
    mel "You betcha! I know it’s still early, but I’m ready to grind and make something of myself."
    mel "For so long, I’ve just been drifting in limbo, and—" 
    show rub neutral blush with d
    rub "[mel], dearie… I know we both have white fur, but I can still see the semen." 
    show mel angry blush with d
    mel "Gah?! [mc], you didn’t tell me I had any on me!"
    mc "I, uh… thought it was implied."
    show mel death with d
    mel "Uwah! Freaking… pervert, weirdo! I’m out of here!"
    scene bg brothel5
    play sound2 move2
    call camerareset from _call_camerareset_19
    with d
    "[mel] fled the room, then a few seconds later I heard the slam of a door down the hall."
    show rub laughing with d
    rub "My, my… Chasing after two sisters. Now there’s a novel experience, don’t you think?"
    mc "Ehehe, for me? Not really…"
    "Quite certain this is technically the fourth pair of sisters I’ve slept with."
    mc "And you don’t mind?"
    show rub bashful with d
    rub "I mind a little. But in the grand scheme, it makes sense. You’ve brought a fair bit of light into our lives. It’s only natural for us to become attached."
    rub "Within that framework, I chose to be with you, and my sister came to the same conclusion, independently."
    show rub happy with d
    rub "You don’t strike me as the manipulative sort. So it's less about finding fault with you and more about discussing the implications with [mel]."
    rub "For example, who gets the weekends? I’d like Thursdays and Fridays."
    mc "Haha, glad you have a sense of humour about it."
    show rub laughing with d
    rub "I suppose I’d have to, especially considering there are a few other ladies that have caught your interest."
    mc "Ehehe… A ‘few’ more is putting it mildly. It’s almost more strange if I meet a woman and don’t end up in bed with her."
    mc "Sometimes I wonder what all the girls see in me."
    show rub wink with d
    rub "Forgive me for prying, but I believe your success is rooted in your empathy. The gift of truly listening is rare these days; most are too consumed with their own lives."
    rub "In that listening, you gain an understanding that’s rare and precious. It’s the sort of insight that deep friends share, and of course, lovers too."
    mc "Is it really that straightforward?"
    show rub laughing with d
    rub "Darling, communication is the bedrock of every relationship. It’s where it all starts."
    show rub happy with d
    rub "We unicorns trace our lineage back to wild horses. Even now, they gather in groups called 'harems'—a dominant stallion, several mares, and their young."
    mc "But that evolution happened millions of years ago. Wouldn't there be some divergence?"
    show rub wink with d
    rub "Perhaps. The world has shifted considerably. We now graze in supermarkets rather than fields."
    rub "Still, much of our biology harkens back to those wild horses. They had robust genes that proved themselves through the ages and persist in various forms across species."
    show rub happy with d
    rub "Yet as society and culture have evolved, so have our needs. The wild stallion’s vigilance and strength are no longer the concerns of the modern world."
    rub "Ladies today have different needs, and in a way that’s almost humorous, you’re the contemporary ideal for many of them."
    mc "Is that why multiple ladies flock to a single guy?"
    show rub horny with d
    rub "Consider this: in the pony world, about 75%% of the population are mares, leaving an average of three mares for every stallion."
    mc "Yep. It sounds way easier for the guys."
    show rub bashful with d
    rub "Indeed, seeing one stallion with two or three partners isn’t out of the ordinary. It’s crucial, too, because if we only had ‘couples,’ that’d mean, at most, only half of our population would breed."
    mc "Ah, harems aren’t merely cultural artifacts; they’re a biological necessity."
    show rub wink with d
    rub "Correct. And that’s why mares, as a species, possess a certain weakness."
    mc "A weakness?"
    show rub laughing with d
    rub "When we ladies see a high-value partner, we fall for them hard."
    rub "You needn’t worry about letting us down or feeling overwhelmed by balancing so many partners. These are partnerships of mutual responsibility, so when you’re low, it’s our duty to lift you up."
    mc "Heh, you see what I mean, though, right? You girls really are remarkable."
    mc "Truth is, I’d be nothing without mares like you. You’re all so impressive—business owners, masters of your crafts, homeowners—and then there’s me… a homeless guy leaning on your support."
    show rub wink with d
    rub "Despite that, you’re the key."
    mc "Shouldn’t it be the other way around? Wouldn’t a successful alpha with wealth and power be a better fit for a harem?"
    show rub happy with d
    rub "You don’t have to be some growling, prowling ‘alpha’ to win our favor. All you need to do is be the one who brings us to our true potential and then binds us together."
    rub "Everywhere you go, you leave a path of light in this encroaching darkness. You can’t blame us for wanting to follow you, can you?"
    show rub happy with d
    rub "And... that is the long answer for why I'm okay with you dating my sister."
    mc "If it’s any comfort, she made me work hard for it."
    show rub bashful with d
    rub "Fuhuhu, I can imagine. I was quite the teasing minx myself back in the day."
    mc "{i}Really{/i}? I couldn’t imagine that!"
    show rub happy with d
    rub "She’ll soften with time, though it seems you’ve already tamed the wild mare, haven’t you? Never thought I’d see that day."
    scene bg brothel5 
    show rub bashful:
        xalign 0.25
    show mel laughing:
        xalign 0.75
    with d
    mel "Even if you are a big loser!"
    "[mel] stepped in with a towel, her fur damp and messy."
    show rub laughing with d
    "I couldn’t help but laugh as I glanced over at [mel], then back to [rub]. They’ve both come to mean so much to me."
    "It was strange, despite this being another universe, I felt like I belonged here, with them…"
    mc "Well, if being a loser means I get to stay with you two, I suppose it’s not such a bad deal after all."
    show rub happy with d
    rub "That’s the spirit. Besides, ‘alpha’ is just a label. Action is what counts. You accomplish more than you realize."
    show mel wink with d
    mel "{i}Giggle{/i} Yeah, but don’t let it go to your head. We’ve got enough egos in this brothel already."
    stop music fadeout 3
    "As more laughter and chatter continued to fill the room, they chased away the last of my doubts."
    scene bg city1 with d
    "We said our goodbyes and I left the brothel. Stepping outside, I breathed in the cool, crisp air and began to walk back to the apartment."
    scene bg apartment
    play music moxietheme fadein 2
    show mox laughing 
    with d
    mox "Well, hey there, stranger! Been a long night?"
    mc "You could say that. Every night in the brothel feels long, but I’m not even the least bit tired."
    show mox wink with d
    mox "Oh? Spill the gossip!"
    mc "For starters, [mel] confessed how she felt about me. It’s something I think we both knew was there, but tonight she finally said it out loud. One thing led to another."
    show mox laughing with d
    mox "First me, then [rub], then [mel] too! She wasn’t even on your original hit-it list. I don’t know how you keep up!"
    mc "Yup, I’m still trying to wrap my head around it all. I mean, how did I get so lucky? How did a guy like me end up surrounded by so many amazing people? … Twice."
    show mox bashful with d
    mox "Luck’s got nothing to do with it, [mc]. You’ve earned this by being who you are. That’s all we ever really want." 
    "She leaned in, planting a gentle kiss on my cheek."
    mc "Thanks again, [mox]. I couldn’t do this without you."
    show mox happy with d
    mox "You’re doing just fine, [mc]. And no matter what, we’re all in this together. That’s the beauty of it."
    "It wasn’t about what I had or lacked, what I’d done or hadn’t done. It was about the bonds I’d forged, the people who stood by me, and how I’d once again found my place in their lives."
    "As the night drew to a close, I realized I had a new purpose. No longer would I be the man adrift in another universe, haunted by his past."
    "Whether I could return to my old world or not, the priority now was to anchor myself to this reality."
    hide mox with d
    if replay == 1:
        return
    $ brothelroute3 = 1
    $ brothelcompletion += 1
    $ completion += 1
    jump newday
