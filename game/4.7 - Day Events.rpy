label dayevent:
    play ambience1 ambienceday
    if dayevent == 0:
        $ dayevent += 1
        play music casual1 fadein 3
        scene bg city3 with d
        "As I leave the apartment, I notice a lone stallion sitting by the side of the road, hunched over, exuding an air of weariness."
        "Is he... homeless? In the other Arcadia, such a thing seemed unthinkable, a distant concept from that utopia."
        "Yet here he is, a stark reminder of the harsh realities that permeate this world."
        menu:
            "Monies: $[money]"
            "Hand the beggar 20 Monies":
                $ money -= 20
                $ event1 = 3
                "I decide to extend a generous hand to the homeless stallion. I reach into my bag and retrieve 20 monies, an offering that could provide several days of relief."
                "The stallion bows and thanks me profusely."
            "Give the beggar 2 Monies":
                $ money -= 2
                $ event1 = 2
                "My heart urges me to help, but practical considerations temper my altruism. I am also technically homeless and surviving by the kindness of others. At the very least, I want to pass some of that forward."
                "I withdraw a modest sum and offer him the two notes."
                "He thanks me, and even though it may seem like an insignificant amount, even small gestures of kindness can have a meaningful impact."
            "Ignore":
                $ event1 = 1
                "Compelled by a mixture of indifference and self-preservation, I avert my gaze and continue on my way."
                "Guilt gnaws at the edges of my conscience as I rationalize the decision. After all, I’m practically homeless with little money to my name too."
    elif dayevent == 1:
        $ dayevent += 1
        jump blankday
    elif dayevent == 2:
        $ dayevent += 1
        play music citytheme fadein 3
        scene bg city4 with d
        #Lend a Hand to a fellow traveller with a broken-down carriage.
        "The distant sound of wheels grinding to a halt catches my attention. Curiosity piqued, I quicken my pace and soon spot a familiar wheel rolling past me."
        scene bg wagon1 with d
        "It’s… [mox]’s caravan? Huh?" 
        show ros neutral with d
        "A blonde dog girl hops out of the car pulling the wagon and growls at the lost wheel. It's actually kind of funny." 
        "I grab the wheel and return it to her. Now that I'm closer, I think I recognize her."
        if rosanamed == 0:
            $ rosanamed = 1
            menu:
                "What was her name?"
                "Default: Rosa":
                    $ rosa = "Rosa"
                "Custom":
                    $ rosa = renpy.input("What was her name?")
                    if rosa == "":
                        $ rosa= "Rosa"
                    $ rosa = rosa.strip()
        show ros laughing with d
        ros "Thanks, stranger! Although... I’m not quite sure how I’m going to put this back on by myself..."
        "I step back and admire the wagon. It seems more rustic than I remember, like it's one coat of paint behind."
        mc "How'd you end up with such a fine wagon?"
        show ros happy with d
        ros "I think it used to belong to some big performer. I thought it’d make a perfect holiday home." 
        "I’d like to check the inside, even if just for nostalgia, but it feels rude to ask while she's trying to fix the wagon."
        menu:
            "Help [ros] fix the wagon":
                $ event2 = 1
                "With a determined nod, I step forward and offer my help."
                scene bg city3 with d
                "Together, under the hot sun and in the middle of a busy street, we set to work repairing the wagon wheel."
                "It’s no easy task. We can't just put the wheel back on; the bolt holding the wheel needs to be replaced."
                "This turned the endeavour into a several hour ordeal of wandering around the town together to find the right replacement parts."
                show ros neutral with d
                ros "My goodness, this place doesn’t have the right size either! I’m so sorry to drag you around like this!"
                mc "Don’t worry about it. Let’s try the next shop."
                "I can’t exactly tell her I'm helping because I knew her from another universe, so she must only see me as an exceedingly kind stranger."
                show ros happy with d
                "However, her positive outlook and affectionate doggy demeanour really contribute to the enjoyment of this experience." 
                scene bg wagon1 with d
                "Once we're back, the carriage begins to take shape again, inching closer to becoming roadworthy. [ros]’s relief is palpable."
                show ros laughing with d
                ros "Thank you so much! I absolutely couldn’t have done this without your help!"
                mc "No problem! I couldn’t leave you stranded like that. Say, do you mind if I come inside?"
                show ros horny with d
                ros "Oh? Be my guest!"
                stop music fadeout 3
                scene bg wagon2 with d
                "As I step inside, I expect a wave of nostalgia, but with most of the furniture rearranged, the wagon feels completely different. Only this one corner remains recognizable."
                play music sextheme
                play moans1 moansmisc2
                show rosa1a e1 
                call camerabreath from _call_camerabreath_24
                $ textbox = 2
                with dissolve
                "When I enter the bedroom, I… Oh my goodness!"
                layeredimage rosa1a:
                    always:
                        "rosa1b"
                    group cum:
                        attribute cum:
                            "rosa1cum"
                    group eyes:
                        attribute e1:
                            "rosa1e 1"
                        attribute e2:
                            "rosa1e 2"
                        attribute e3:
                            "rosa1e 3"
                    group sex:
                        attribute v1:
                            "rosa1 v1"
                        attribute v2:
                            "rosa1 v2"
                        attribute a1:
                            "rosa1 a1"
                        attribute a2:
                            "rosa1 a2"
                ros "You said you wanted to cum inside, didn’t you~?"
                "I didn’t even notice her slip in here. I was so focused on the labor of fixing the wagon, that I probably didn’t notice [ros] swooning from the sidelines as she watched me."
                ros "You’re such a hardworking hunk… I’m not even going to pretend I’m offering this as thanks, I just straight up want your cock!"
                menu:
                    "I can tell you’re in heat, you slutty pup.":
                        pass
                    "Afraid that’s not what I meant, pup.":
                        ros "Awwhhh… We’re not going to?"
                        menu:
                            "I never said that. Let’s do it~":
                                pass
                            "Nah, we’ve only known each other for a few hours!":
                                ros "R-Right… If you’re ever in [rub]’s brothel, you should see me! I don’t usually sleep with clients, but I can make an exception for you."
                                jump postros1
                ros "Oohhhh yes! I want you to pump me full of puppies! I need it so bad!" 
                "I stood there naked before [ros], that irresistible canine goddess. Her fur glistened under the setting sun, inviting me into her soft, warm embrace. Her ample breasts were heaving with anticipation as she wagged her tail at me, her eyes sparkling with desire."
                "The sight of her wet pussy, glistening with anticipation, stole my attention as I stepped closer, my raging erection throbbing with each step."
                ros "{i}Pant, pant{/i} Don’t hold back; I haven’t had a good pounding in years!"
                mc "Hehe, I can tell, but don’t worry, you’ll be remembering this one for years."
                "Gently, moved over her on the soft bed beneath us, her ample ass lifting off the sheets as I positioned myself between her thighs. I could see her quiver as I teased my tip against her engorged clit, sending waves of pleasure through her body."
                ros "Aaaahhhh… I’m ready for you!"
                play sound2 cum
                show rosa1a v1 e2 with d
                play moans1 moansmisc3
                "I groaned as I felt her tight pussy grip my shaft as I slid inside, impaling her with my cock in a single deep thrust. She was certainly wet and ready!"
                play ambience1 sex fadein 2
                "[ros] let out a loud whine of ecstasy as I began to thrust into her, her hands digging into my back as I claimed her body. The sound of my flesh and her fur slapping together filled the air as I pumped her hard and deep."
                mc "Woaahhh… Your pussy feels fucking incredible! It’s squeezing around me so tightly!"
                ros "Uoohhhh… Are you sure it’s not just your cock being massive? You’re filling me up completely! Nngghh!"
                "I reached out, my fingers brushing against her supple fur as I cupped her breasts, feeling her heartbeat race beneath her skin." 
                "I could hardly contain my lust as I leaned down, my lips meeting hers in a passionate kiss that left us both breathless. Her tongue danced with mine, tasting of sweet animal desire as her hands found their way up to my neck."
                ros "Mmphhh… {i}Kiss, slurp{/i} Aaahhh, love yoursh kisshes~ {i}Kiss, lick{/i}"
                "It was almost hard to believe we were in the middle of a public road as she enveloped me in her erotic embrace and moaned without a care in the world." 
                "Her hefty tits were bouncing with each powerful thrust, and her whines were growing louder with each passing moment."
                ros "Uuuuu! I’m getting really close! Aaahhh!"
                mc "Good girl, cum for me! I’m close too!"
                "As I called her a good girl, I could feel her wet pussy clenching around my cock, milking me with every spasm of her inner muscles as I plowed into her relentlessly." 
                "I leaned down, my lips finding her neck, biting gently as I whispered filthy words of desire into her ear. She whimpered her approval, her body arching off the ground as her orgasm ripped through her like wildfire."
                "Her pussy tightened around me as her juices flowed freely, coating my shaft with her essence as her body shook with ecstasy."
                mc "Ahh! I’m about to cum!"
                ros "Yessss! Give it to me! Fill me with your puppies!" 
                "I could feel my own orgasm building, my balls tightening as I slammed into her one last time, burying myself deep within her quivering core."
                play sound2 cum
                show rosa1a cum v2 e3 with c
                play sound2 cum
                show internalcreampie with c
                "With one final growl of satisfaction, I let go, my hot cum flooding her insides as I held her close through our shared moment of release."
                play sound2 cum
                with c
                play sound2 cum
                with c
                ros "There’s so much! Aaaahhhhh, it feels so warm!"
                "We continue rutting until the heightened pleasure of our orgasms finally fades." 
                call stopbgs from _call_stopbgs_20
                call camerareset from _call_camerareset_4
                stop music fadeout 20
                hide internalcreampie
                show rosa1a -v2 
                with d
                "We lay there entwined, breathless, and sated, our juices mixing together as we basked in the afterglow of our carnal union. I could have stayed there forever, but eventually, reality crept back in as I heard the sounds of passing pedestrians."
                "With one last kiss, I pulled out of her, watching as her freshly fucked pussy leaked cum, leaving me both wanting more but feeling satisfied with what we'd shared."
                ros "Oooohhhh yes! You weren’t kidding about giving me a fuck for the ages. I feel full of energy after that!"
                play sound2 equip
                scene bg wagon2 
                show ros laughing 
                $ textbox = 1
                with d
                "I smiled as I watched [rosa] bounce up, her tag wagging wildly."
                mc "Haha, I must admit, I was not expecting my day to go like this."
                mc "It’s tragic to part, but I believe we both have places to be."
                show ros happy with d
                ros "Say it ain’t so… But this is a moment in time I’ll certainly never forget."
                label postros1:
                    show ros laughing with d
                    ros "I hope we’ll see each other again sometime, [mc]!"
                scene black with d
                "I returned to the apartment to rest."
            "Wish her luck and leave":
                $ event2 = 2
                ros "Ah, thanks! Take care, stranger."
                stop music fadeout 2
                scene black with d
    elif dayevent == 3:
        $ dayevent += 1 
        jump blankday          
    elif dayevent == 4:
        $ dayevent += 1
        play music casual1 fadein 3
        scene bg city4 with d
        #Marketplace Distraction
        "As I navigate through a bustling marketplace, far larger and more exhausting than any I've visited before, I spot exactly what I'm looking for."
        "Donuts! [mox] loves these, so I'll buy some as a treat."
        "As I make my purchase, the distracted merchant accidentally hands me a 20 monie bill back instead of 5. I'm briefly excited by this realization, but..."
        menu:
            "Monies: $[money]"
            "Keep the extra change (+15 M)":
                $ money += 15
                $ event4 = 1
                "Temptation tugs at me. After all, no one would notice. With the marketplace this busy, the merchant's coffers must be overflowing."
                "With a subtle glance around, I discreetly pocket the extra change, rationalizing it as a stroke of good luck amid the chaos."
            "Return the extra change":
                "My sense of honesty compels me to do the right thing. Despite the allure of extra coins, I gently alert the merchant to the mistake and exchange the 20 bill for the correct amount."
                "As a bonus for the honesty, he thanks me, hands me a crumpled stack of three 1 monie bills then continues frantically working."
                $ money += 3
                $ event4 = 2
    elif dayevent == 5:
        #$ dayevent += 1
        #This is the highest event level for version 0.1 since Chloe's standing art is unfinished
        jump blankday
    elif dayevent == 6:
        $ dayevent += 1
        play music citytheme fadein 3
        scene bg city3 with d
        #Lost Wallet
        "Strolling down a bustling street, I notice something on the pavement, partially obscured by fallen leaves."
        "When I bend down to investigate, my heart skips a beat—I’ve found a lost wallet."
        "Inside, I find crisp bills neatly tucked away. My fingers brush the smooth surface of the currency, and I count fifty monies in total. What luck!"
        "But then, I find something unexpected—a slip of paper with a nearby return address, important cards, and a small photo of a mare with purple sunglasses."
        mc "Aaahhh… Damn…"
        "Returning the wallet means giving up its contents…"
        menu:
            "Return the Wallet":
                "In the end, I know what I must do. With a heavy sigh, I resolve to do the right thing, no matter how difficult."
                "Clutching the wallet tightly, I make my way to the nearby address and return it to its rightful owner."
                chl "Oh! Thank you! Thank you so much!"
                mc "Ah… You’re!"
                menu:
                    "What was her name?"
                    "Default: Chloe":
                        $ chl = "Chloe"
                    "Custom":
                        $ chl = renpy.input("What was her name?")
                        if chl == "":
                            $ chl= "Chloe"
                        $ chl = chl.strip()
                chl "Recognize meeve? A brothel regular, perhaps?"
                "She slips me a 20 M note and winks."
                chl "I’ll certainly recognize you, so if you ever see me there and want a special, I’ll give you a discount~" 
                "(Gained +20 M and a discount on at the brothel!)"
                $ money += 20
                $ event3 = 1   
            "Keep the Wallet (+50 M)":
                "With a swift motion, I slip the wallet into my satchel. The weight fills my bag, a tangible reminder of the wealth now in my possession."
                "I continue down the street, wondering what I’ll do with all that money."
                $ money += 50
                $ event3 = 2
    else:
        label blankday:
            "I spent the morning researching my leads and planning my next moves."
    if day >= 2 and moxpen2 == 0 and penmsg1 == 0:
        $ penmsg1 = 1
        $ unread += 1
        $ unreadpen += 1
    return
label nightevent:
    if nightevent == 0:
        $ nightevent += 1
    elif nightevent == 1:
        $ nightevent += 1
        play sound1 earthquake volume 0.7
        with sshake
        "As [mox] and I got into bed, the entire thing suddenly began to shake. Another earthquake."
        show mox neutral with d
        mox "You’re not vibrating, are you?"
        mc "I don’t think so."
        show mox laughing with d
        mox "Damn, I kind of wish you could."
        mc "I’m seriously wondering why this universe has earthquakes."
        show mox neutral with d
        mox "I heard from someone that they’re technically not earthquakes, which are when tectonic plates in the earth move against each other or something."
        show mox awkward with d
        mox "Instead the entire planet is shaking."
        mc "What? The {i}entire{/i} planet?"
        show mox neutral with d
        mox "I mean, just a theory. But these ‘earthquakes’ are global."
        mc "Man… This universe is something else."
        scene black with d
    elif nightevent == 2:
        $ nightevent += 1
    elif nightevent == 3:
        $ nightevent += 1
        #Day 3:
        play music sad
        play ambience1 staticlong volume 0.2 fadein 5
        scene black with dissolve
        show space1:
            alpha 0.5
            linear 10 alpha 0
            linear 11 alpha 0.8
            repeat
        show space2:
            alpha 0
            linear 12 alpha 0.8
            linear 13 alpha 0
            repeat
        with dissolve
        show silhouette1
        with dissolve
        $ textbox = 2
        "[mc], are you there? I don’t have long."
        "A shimmering figure with a familiar voice appeared before me."
        "You’re doing so good so far – keep meeting with the virtues, so they can reach their potential."
        "And with that, hopefully, this –"
        stop ambience1
        play sound2 staticshort1
        show eyes
        scene bg moxiebedroom with d
        $ textbox = 1
        "Ack?! How could the dream end right there?"
        "That woman though… I only know one person that was able to comfortably enter people’s dreams to communicate with them, and since this is the third dream of its type in a row, I can’t put it down to coincidence."
        "Princess [sel] is trying to communicate with me – but… this is a world without Princess [sel]."
    elif nightevent == 4:
        $ nightevent += 1
    elif nightevent == 5:
        $ nightevent += 1
        "Just as we’re getting into bed, I remember my dream from the prior night."
        mc "[mox], I had a small question for you."
        show mox bashful with d
        mox "You can ask me anything you want, darling."
        mc "It’s just… I’ve kind of asked you this before, but it’s about a Princess [sel]."
        show mox neutral with d
        mox "Yeah, I’ve never heard of her before. It’s hard to imagine that I’m blood related to someone like that."
        mc "Hm… She’s supposed to be [aur]’s sister, the Princess of the Moon."
        show mox surprised with d
        mox "A Queen of the Sun and a sister Princess of the Moon would certainly make a lot of sense."
        mc "She’s been appearing in my dreams, asking me to gather the virtues. Although I haven’t quite figured out why, I can only imagine it’s related to solving the troubles around the world."
        show mox neutral with d
        mox "It sounds like we need to get that meeting with [aur] and fast!"
        mc "You’re right. I’ll ask her for help directly." 
    else:
        "I get into bed, and [mox] snuggles up beside me as we doze off together."
    return
init:
    $ dayevent = 0
    $ event1 = 0
    $ event2 = 0
    $ event3 = 0 
    $ event4 = 0

    $ nightevent = 0

