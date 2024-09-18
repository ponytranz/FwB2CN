#Moxie
label moxiesexscenes:
    label moxfacesitting:
        layeredimage moxpen2a:
            always:
                "moxpen2ab [moxb]"
            group punk:
                attribute p1:
                    "moxpen2apunk 1"
                attribute p2:
                    "moxpen2apunk 1"
            group makeup:
                attribute m1:
                    "moxpen2amakeup 1"
                attribute m2:
                    "moxpen2amakeup 2"
            group eyes:
                attribute 1:
                    "moxpen2ae 1"
                attribute m1:
                    "moxpen2ae 1"
                attribute 2:
                    "moxpen2ae 2"
                attribute m2:
                    "moxpen2ae 2"
            group fishnets:
                attribute f1:
                    "moxpen2afishnet 1"
                attribute f2:
                    "moxpen2afishnet 2"
            group plug:
                attribute plug:
                    "moxpen2aplug"
                attribute plug2:
                    "moxpen2aplug" alpha 0.5
            group squirt:
                attribute squirt:
                    "moxpen2asquirt"
            group cum:
                attribute cum:
                    "moxpen2acum"
            group night:
                attribute night:
                    "night" alpha 0.30 blend "multiply"
        show bg moxiebedroom2 with d
        play music sextheme fadein 3
        play moans1 moansmisc2 fadein 3
        $ textbox = 4
        play ambience1 blowjob
        show moxpen2a 1 night
        call camerabreath from _call_camerabreath
        with d
        "Her body glistened, accentuating every curve and muscle as she lowered herself onto my face."
        mox "What kind of mood are you in today?"
        $ gen1 = 0
        $ gen2 = 0
        $ gen3 = 0
        $ gen4 = 0
        menu moxfacesittingmenu:
            "Select option to toggle on/off."
            "Make-Up (Needs Punk Costume)" if punk == 0:
                play sound2 error
                jump moxfacesittingmenu
            "Make-Up" if punk == 1:
                if gen1 == 0:
                    $ gen1 = 1
                    show moxpen2a m1 with d
                    mox "What do you think?"
                else:
                    $ gen1 = 0
                    show moxpen2a -m1 1 with d
                    mox "Not to your taste?"
                jump moxfacesittingmenu
            "Punk (Needs Purchasing)" if punk == 0:
                play sound2 error
                jump moxfacesittingmenu
            "Punk" if punk == 1:
                if gen2 == 0:
                    $ gen2= 1
                    show moxpen2a p1 with d
                    mox "Hit those lights!"
                else:
                    $ gen2 = 0
                    show moxpen2a -p1 with d
                    mox "Hit those lights! To... uh, turn them on this time."
                jump moxfacesittingmenu
            "Pantyhose (Needs Purchasing)" if pantyhose == 0:
                play sound2 error
                jump moxfacesittingmenu
            "Pantyhose" if pantyhose == 1:
                if gen3 == 0:
                    $ gen3 = 1
                    show moxpen2a f1
                    if gen4 == 1:
                        show moxpen2a plug2 with d
                    mox "Hehe, how does that feel?"
                else:
                    $ gen3 = 0
                    show moxpen2a -f1
                    if gen4 == 1:
                        show moxpen2a plug with d
                    mox "Fishnets and fur are an odd combo, I'll give you that."
                jump moxfacesittingmenu
            "Buttplug (Needs Purchasing)" if buttplug == 0:
                play sound2 error
                jump moxfacesittingmenu
            "Buttplug" if buttplug == 1:
                if gen4 == 0:
                    $ gen4 = 1
                    show moxpen2a plug
                    if gen3 == 1:
                        show moxpen2a plug2
                    with d
                    mox "Nngghh, I'm tight down there!"
                else:
                    $ gen4 = 0
                    show moxpen2a -plug -plug2 with d
                    mox "{i}Pop!{/i} Uooohhhh..."
                jump moxfacesittingmenu
            "(Continue)":
                pass
            "(Stop Scene)":
                return
        "As [mox]'s lithe form straddled me, hips swaying and her long tail flickering back and forth, I was transfixed."
        "The scent of her arousal was intoxicating—a heady mix of flowers and musk that only served to fuel my own raging lust."
        "My member throbbed in anticipation as I gazed upon her tight, little puzzle, hovering mere inches away from my awaiting lips."
        mox "Are you ready for me?"
        "She purred huskily, her voice dripping with desire."
        mc "Mmhh, yes! You're such a goddess~ Give it to me."
        "A satisfied smirk curved [mox]'s lips at my eagerness. Slowly but deliberately, she lowered herself onto my face, her wet folds immediately met by my eager tongue."
        "Her body quivered with pleasure as my tongue darted in search of her clit - a quest met with success when I found it and focused all my attention on it. [mox] was overwhelming with an onslaught of pleasure, many moans slipping past her parted lips."
        mox "Ahhh, unnfff! You certainly don't hold back~"
        "Slowly but surely, [mox] began rocking back and forth, savoring the resulting friciton between our lips. Her pace gradually increased, encouraged by my skilled tongue."
        if gen3 == 1:
            show moxpen2a f2
            if gen3 == 1:
                show moxpen2a plug
            with d
            "Before long, my fingers dug into her plump ass cheeks - tearing through her flimsy fishnets in the process - to keep her steady and anchored in place."
            show moxpen2a 2
            if gen1 == 1:
                show moxpen2a m2
            with d
            mox "Ooohhh, I love it when you get rough! Aahhhh, don’t stop!"
        else:
            "Before long, my fingers dug into her plump ass cheeks to keep her steady and anchored in place."
            mox "Ooohhh! Aahhhh, don’t stop!"
            show moxpen2a 2
            if gen1 == 1:
                show moxpen2a m2
            with d
        "My tongue continued to constantly brush against her sensitive clit, jolts of pure pleasure coursed through [mox]'s body. Her chest heaved enticingly above me, bouncing slightly with each movement of her hips." 
        "She had her eyes on something new. Reaching forward, she wrapped her hand around my throbbing cock and began to stroke my shaft as fast as she thrust her hips."
        "In the midst of this, we lost ourselves in our primal lust. [mox]’s grip tightening around my cock while her pussy was using my nose like a credit card."
        "The sensations were overwhelming, pushing us towards our limit."
        mox "Nngghh, I-I’m so close! Aaahhhh, are you close?"
        mc "Mmpphhh! {i}Lick, slurp.{/i} Yeah!"
        show moxpen2a squirt with d
        mox "I’m…. I’m going to… I’m, aahh, cumming!"
        "She screamed out in ecstasy, her body tensing up around my face, before I also exploded in an equally powerful orgasm."
        play sound2 cum
        show moxpen2a cum
        with c
        play sound2 cum
        with c
        "Waves upon waves of cum erupted from my cock and splattered the two of us as she rode out her climax on my face."
        play sound2 cum
        with c
        play sound2 cum
        with c
        "Just as I kept my tongue focused on her clit, she continued to give me a messy, cum-splattered handjob until we both finally came down from our highs."
        play sound2 cum
        with c
        play sound2 cum
        with c
        mox "Uooohhhh, so good…"
        mc "{i}Pant, pant{/i} I think this one is going to require a serious cleanup!"
        mox "You rest right there, stud. I’ll go get a towel."
        $ energy -= 1
        return
    label moxmissionary:
        layeredimage moxie1a:
            always:
                "moxie1abase [moxb]"
            group eyes:
                attribute e1:
                    "moxie1ae 1"
                attribute e2:
                    "moxie1ae 2"
                attribute e3:
                    "moxie1ae 3"
                attribute e4:
                    "moxie1ae 4"
                attribute e5:
                    "moxie1ae 5"
            group bunny:
                attribute bunny:
                    "moxie1abunny 2a"
                attribute bunny1:
                    "moxie1abunny 2a"
                attribute bunny2:
                    "moxie1abunny 2b"
            group cum:
                attribute cum:
                    "moxie1acum"
            group plug:
                attribute plug:
                    "moxie1aplug"
                attribute bunny:
                    "moxie1abunnyplug"
            group sex:
                attribute v1:
                    "moxie1avaginal 1"
                attribute v2:
                    "moxie1avaginal 2"
                attribute a1:
                    "moxie1aanal 1"
                attribute a2:
                    "moxie1aanal 2"
                attribute dp1:
                    "moxie1avaginal 1"
                attribute dp1:
                    "moxie1aanal 1"
                attribute dp2:
                    "moxie1aanal 2"
                attribute dp2:
                    "moxie1avaginal 2"
        show moxie1a e1
        $ textbox = 2
        call camerabreath from _call_camerabreath_1
        with d
        play music sextheme fadein 3
        play moans1 moansmisc2 fadein 3
        mox "I'm all yours, cutie. Just tell me how you want me."
        $ gen1 = 0
        $ gen2 = 0
        $ gen3 = 0
        menu moxmissionarymenu:
            "Select option to toggle on/off."
            "Bunny Girl (Needs Purchasing)" if bunnygirl == 0:
                play sound2 error
                jump moxmissionarymenu
            "Bunny Girl" if bunnygirl == 1:
                if gen1 == 0:
                    $ gen1 = 1
                    $ gen2 = 0
                    show moxie1a bunny -plug with d
                    mox "I hear rabbit girls have an unparalleled sexual appetite. But I reckon I could keep up with them!"
                else:
                    $ gen1 = 0
                    show moxie1a -bunny with d
                    mox "No bunnies today?"
                jump moxmissionarymenu
            "Plug (Needs Purchasing)" if buttplug == 0:
                play sound2 error
                jump moxmissionarymenu
            "Plug" if buttplug == 1:
                if gen2 == 0:
                    $ gen1 = 0
                    $ gen2 = 1
                    show moxie1a plug -bunny
                    mox "Nngghh, I'm tight down there!"
                else:
                    $ gen2 = 0
                    show moxie1a -plug
                    mox "{i}Pop!{/i} Uooohhhh..."
                jump moxmissionarymenu
            "(Continue)":
                pass
            "(Stop Scene)":
                return
        menu moxmissionarymenu2:
            "Vaginal":
                $ gen3 = 1
                $ gent = "pussy"
                mox "The classic~ I'm all yours."
            "Anal (Needs Lubrication)" if lubrication == 0:
                play sound2 error
                jump moxmissionarymenu2
            "Anal" if lubrication == 1:
                $ gen3 = 2
                $ gent = "ass"
                mox "Oh my, you want to do it there? Lube me up and I'm yours~"
                if gen1 == 1 or gen2 == 1:
                    if gen1 == 1:
                        show moxie1a -bunny bunny1
                    if gen2 == 1:
                        show moxie1a -plug
                    "First, I pop out her buttplug, getting a resounding groan from [mox] as it pops out."
                "I drip some lubrication onto the tip of my fingers and slowly massage it into her pucker. She coos and wiggles in response to the cool touch."
            "Double Penetration (Needs Lewd Spellbook)" if lewdspellbook == 0:
                play sound2 error
                jump moxmissionarymenu2
            "Double Penetration" if lewdspellbook == 1:
                $ gen3 = 3
                $ gent = "pussy"
                mox "Double trouble? Let me just check the spell..."
                "[mox] casts the spell and conjures a temporary familiar that looks just like me."
                mox "You won't share pleasure, but I'm certain to get the best of both worlds! Come at me, boys~"
                if gen1 == 1 or gen2 == 1:
                    if gen1 == 1:
                        show moxie1a -bunny bunny1
                    if gen2 == 1:
                        show moxie1a -plug
                    "First, I pop out her buttplug, getting a resounding groan from [mox] as it pops out."
        $ textbox = 2
        play moans1 moansmisc2
        stop ambience1 fadeout 30
        with d
        "As the intensity of our shared moment escalated, an electrifying current seemed to arc between us, heightening every sensation tenfold. Desire and lust sizzled so vividly that one might have sworn we were literally sparking with raw passion."
        "My erect cock was full of life, pushing against her thighs so insistently that I could clearly feel the velvety softness of her inner thigh brushing against my throbbing shaft."
        if gen3 != 3:
            mox "Aahh~  I can't wait to feel that beast inside me."
        else:
            mox "Nnghhh, I wonder if I can handle both of you at once?"
        show moxie1a e2 with d
        mox "I'm absolutely drenched down there... as ready as I could possibly be."
        mox "You know, you were right—we are going to check off every box on our naughty list, aren't we?"
        mox "So, my stud... Are you ready to give me everything I want? Are you prepared to take me here, now, like two animals driven wild by desire?"
        "Her hips shifted restlessly against his, seeking friction, pleading for release."
        mc "I'm going to pound you so hard, babe~"
        "[mox] eagerly spread her legs apart, anchoring them securely into position with a tight grip. She arched her hips upward, presenting herself as an irresistible temptation to be devoured by my eyes."
        if gen3 != 3:
            "My cock was no longer pressed between her thighs, but now hovering over her [gent1], the tip occasionally brushing against them."
            "With each passing heartbeat, my tip delved in just a little deeper."
        else:
            "Me and my familiar's cocks were now but now hovering over her pussy and ass, the tips occasionally brushing against them."
            "With each passing heartbeat, our tips pushed in just a little deeper."
        if gen1 == 1:
            play sound2 rip
            show moxie1a bunny2 with d
            "I tore a hole in her tights without a care in the world. This only turned her on more."
        "Never before had I experienced anything remotely comparable to the overwhelming craving that consumed me at that moment. It wasn't merely lust that coursed through my veins; no, there was an underlying depth to this hunger that left me quivering with anticipation"
        if gen3 != 3:
            mox "I want you inside me."
        else:
            mox "I want you both inside me."
        mox "Please… make love to me." 
        if gen3 == 3:
            "My familiar and I wordlessly agreed on which hole to bully [mox] with. I'll go on top and take her pussy, while he goes below and pounds into her ass."
        play music sextheme
        play sound2 cum
        if gen3 == 1:
            show moxie1a e3 v1
        elif gen3 == 2:
            show moxie1a e3 a1
        else:
            show moxie1a e3 dp1
        play moans1 moansmisc4
        with d
        "I guided my cock towards [mox], aligning our bodies perfectly. With measured precision, I slowly pushed my member into her tight opening, relishing in the way she arched her back and shivered with unadulterated pleasure as she accommodated each inch of my shaft."
        "A gut-wrenching moan tore through [mox]'s throat as she was filled up. Her insides clenched tightly around my cock, squeezing me mercilessly yet oh-so-exquisitely. The sensation threatened to overwhelm my own senses as we became one entity bound by our primal desires."
        camera:
            zpos -20
            linear 0.5 ypos 8
            linear 0.1
            linear 0.2 ypos -8
            linear 0.2
            repeat
        with vpunch
        play ambience2 sex
        if gen3 == 1:
            "Her pussy was already dripping wet, her flank trembling underneath me as I began to thrust into her."
        elif gen3 == 2:
            "Her flank trembled underneath me as I began to thrust into her. Her pussy was so wet, that her juices dripped down to her pucker and lubricated our point of contract."
        mc "Nngghh, damn, you’re tight!"
        mox "Ooohhh, that’s because your cock is so big! Mmh… and it feels so good!"
        with vpunch
        "Her [gent] squeezed and spasmed as precum oozed deep inside. I grabbed hold of her hips tightly, using them as leverage to drive myself deeper into her body." 
        if gen3 == 3:
            "We both thrust into her holes in an alternating rhythm, not giving [mox] a second of reprieve from the intense pleasure. And even though our cocks were never pushed all the way in at the same time, her pussy still felt tighter than ever as it coiled and throbbed around my shaft."
        mox "Yes! Ohhh, yes! This is everything I wanted it to be and more!"
        "[mox] moaned out loudly, not caring if the neighbours might hear. She continued to beg for more, urging me on with each breathy moan that escaped her lips. She was completely lost to her primal desires, her normal demeanour replaced by wanton lust." 
        mc "I can’t believe how good you feel right now! So wet and hot!"
        with vpunch
        if gen3 != 3:
            "I increased the pace of my thrusts, each one harder than the last. The sounds of our bodies colliding filled the apartment, - the slapping of flesh against flesh, the wet squelching sound of my cock sliding against her tight [gent], accompanied by her moans and gasps of pleasure."
        else:
            "We both increased the pace of our thrusts, each one harder than the last. The sounds of all three of our bodies colliding filled the apartment, - the slapping of flesh against flesh, the wet squelching sound of my cock sliding against her wet, mare pussy, accompanied by her moans and gasps of pleasure."
        "I leaned forward, burying my face into her mane as I continued to ravage her tight hole. I nibbled on ear earlobe, biting down gently as I felt myself getting closer to climax."
        show moxie1a e4 with d
        if gen3 != 3:
            mox "Oh gods! I can feel you getting even larger! Uoohhhh, you’re going to make me cum!"
        else:
            mox "Aaahhh, this is crazy! You're both throbbing inside me! Uoohhhh, I'm going to cum any second!"
        if gen3 != 3:
            "[mox] whimpered out between moans, her body growing tense in anticipation of her climax. She arched her ass upwards, pushing herself harder against my cock, begging for more of that incredible sensation."
        else:
            "[mox] whimpered out between moans, her body growing tense in anticipation of her climax. She arched her spasming body towards us, begging for more of that incredible sensation."
        if gen3 != 3:
            "I could feel myself teetering on the edge as well. The tightness of her [gent] around me was almost too much to bear."
        else:
            "I could feel myself teetering on the edge as well, and my familiar seemed to be just as close. The tightness of her pussy and ass were just too much to bear."
        mox "Aahhh, I-I’m almost…!"
        "I reached down between us, finding her sensitive clit with one of my hands. I began to rub it rhythmically as I continued to thrust into her tight hole. This was the final straw for both of us—we both exploded together."
        play sound2 cum
        if gen3 == 1:
            show moxie1a e3 v2
        elif gen3 == 2:
            show moxie1a e3 a2
        else:
            show moxie1a e3 dp2
        with c
        play sound2 cum
        if gen3 == 1:
            show internalcreampie 
        with c
        mox "I’m cumming!" 
        play sound2 cum
        with c
        play sound2 cum
        with c
        if gen3 != 3:
            "I let out a roar of pleasure as I came inside of her, filling her [gent] with my hot cum. My cock throbbed inside of her tight hole, pulsing with each spurt of seed that spilled into her depths."
        else:
            "I let out a roar of pleasure as both myself and my familiar came inside of her, filling her womb and ass with hot cum. My cock throbbed inside of her tight pussy, pulsing with each spurt of seed that spilled into her depths."
        play sound2 cum
        with c
        play sound2 cum
        with c
        "Meanwhile, [mox] screamed out in ecstasy as wave after wave of orgasmic bliss washed over her body. She clenched tightly around me, milking every last drop of cum from me before finally loosening its vice-like grip on my cock."
        hide moxie1avaginal
        show moxie1a e5 -v2 -a2 -dp2 cum
        call camerabreath from _call_camerabreath_2
        play moans1 moansmisc2
        stop ambience2 fadeout 2
        hide internalcreampie
        with d
        "My cock was slick with their combined juices, throbbing gently from our intense lovemaking. I looked down at her well-fucked [gent] oozing with cum, her legs trembling slightly."
        if gen3 != 1:
            "We snuggled in the afterglow of our orgasm while we caught our breath."
        elif gen3 == 3:
            "She was in luck as she got doubled snuggles from me and my familiar was we enjoyed the afterglow of our orgasms."
        scene bg moxiebedroom2 
        show mox laughing with d
        "Afterwards she bounced up with more energy than ever."
        mox "Heck yeah! I feel much better now!"
        if gen3 == 3:
            "A few minutes later, our quiet familiar friend disappears."
        $ energy -= 1
        return
    label moxfrombehind:
        layeredimage moxie1b:
            always:
                "moxie1bbase [moxb]"
            group eyes:
                attribute e1:
                    "moxie1be 1"
                attribute e2:
                    "moxie1be 2"
                attribute e3:
                    "moxie1be 3"
            group spanked:
                attribute spanked:
                    "moxie1bspanked"
            group cum:
                attribute cum0:
                    "moxie1bcum" alpha 0.5
                attribute cum:
                    "moxie1bcum"
            group plug:
                attribute plug:
                    "moxie1bbuttplug"
            group clothing:
                attribute lingerie:
                    "moxie1blingerie"
                attribute pantyhose1:
                    "moxie1bpantyhose 1"
                attribute pantyhose2:
                    "moxie1bpantyhose 2"
            group sex:
                attribute v1:
                    "moxie1bvaginal 1"
                attribute v2:
                    "moxie1bvaginal 2"
                attribute a1:
                    "moxie1banal 1"
                attribute a2:
                    "moxie1banal 2"
        scene moxie1b e1 
        $ textbox = 2
        with d
        mox "I know what position you'd like."
        "I bite my lip and masturbate to a full erection as I get back into position behind [mox]’s fat ass."
        mc "You read my mind."
        mox "How would you like me?"
        $ gen1 = 0
        $ gen2 = 0
        $ gen3 = 0 
        menu moxfrombehindmenu:
            "Pantyhose (Needs Purchasing)" if pantyhose == 0:
                play sound2 error
                jump moxfrombehindmenu
            "Pantyhose" if pantyhose == 1:
                if gen3 == 0:
                    $ gen3 = 1
                    show moxie1b pantyhose1 with d
                else:
                    $ gen3 = 0
                    show moxie1b -pantyhose1 with d
                jump moxfrombehindmenu
            "Lingerie (Needs Purchasing)" if lingerie== 0:
                play sound2 error
                jump moxfrombehindmenu
            "Lingerie" if lingerie == 1:
                if gen2 == 0:
                    $ gen2 = 1
                    show moxie1b lingerie with d
                else:
                    $ gen2 = 0
                    show moxie1b -lingerie with d
                jump moxfrombehindmenu
            "Buttplug (Needs Purchasing)" if buttplug == 0:
                play sound2 error
                jump moxfrombehindmenu
            "Buttplug" if buttplug == 1:
                if gen1 == 0:
                    $ gen1 = 1
                    show moxie1b plug with d
                    mox "Nngghh, I'm tight down there!"
                else:
                    $ gen1 = 0
                    show moxie1b -plug with d
                    mox "{i}Pop!{/i} Uooohhhh..."
                jump moxfrombehindmenu
            "(Continue)":
                pass
        menu mfbm2:
            "In the future, you will have to purchase and gift these options first."
            "Vaginal":
                $ gen4 = 1
                $ gent = "pussy"
                mox "The classic~ I'm all yours."
            "Anal (Needs Lubrication)" if lubrication == 0:
                jump mfbm2
            "Anal" if lubrication == 1:
                $ gen4 = 2
                $ gent = "ass"
                mox "Oh my, you want to do it there? Lube me up and I'm yours~"
                if gen1 == 1:
                    if gen1 == 1:
                        show moxie1b -plug
                    "Firstly, with a satisfying pop, I remove the plug from [mox]'s clenched ass, eliciting a deep moan."
                    if gen3 == 1:
                        "For the pedantic in the audience, yes, I did have to remove her pantyhose and put it back on!"
                "I dripped a generous amount of slippery lubricant onto my fingers before slowly and sensually applying it to [mox]'s pucker."
        mc "Let’s fuck that heat completely out of you, for a few days at least~"
        if gen3 == 1:
            "I poke my cock against her entrance, pushing against her pantyhose and stretching it as my tip pushes inside slightly."
            mox "Hehe, I don't think that'll work."
            mc "To think, you went to all that effort to put on your pantyhose only for me to do this."
            play sound2 rip
            show moxie1b pantyhose2 with d
            mox "Unnfff... You sexy beast~ Ravish me!"
        play sound2 cum
        if gen4 == 1:
            show moxie1b e2 v1
        elif gen4 == 2:
            show moxie1b e2 a1
        camera:
            zpos -20
            linear 0.5 xpos -8
            linear 0.1
            linear 0.2 xpos 8
            linear 0.2
            repeat
        with vpunch
        play ambience2 sex
        play moans1 moansmisc4
        with c
        "I take a few seconds to spread and admire her [gent], before guiding the tip of my cock straight inside."
        mox "Oh god, the first thrust always feels so fucking good."
        "She moans deeply as I begin slowly thrusting, savouring the tightness of her [gent] as I deliver hard, deep thrusts." 
        mc "You’re all mine."
        mox "That's right, babe. I'm yours!"
        "Her body shivers slightly, her ass pushing back against me with more vigour and enthusiasm, her hips grinding back and forth."
        "Pleased with her response, my cock tightens and throbs. I pick up the pace, and my thrusts become harder and faster. Each time I slammed into her tight [gent], her insides squeezed me tighter and tighter."
        mox "Ah, ah! Haaahhh… Your cock feels so good inside me! Nngghh, you're going to get me addicted to this feeling!"
        mc "Heh, as if you're not already completely bewitched by my cock~"
        "I stop moving my hips for a few seconds, and that alone is enough for [mox] to greedily start moving her own to resume the sex."
        mox "Gahhh, don't stop! I need it!"
        mc "Ahaha, if you say so!"
        play sound2 spank
        show moxie1b spanked with d
        "With a resounding spank, I resume bullying her [gent] in full force with my fastest and strongest thrusts yet. Her eyes roll back and her body spasms as the pleasure overwhelms her."
        "Her long, silky hair continued to swish and flicker against her back, giving me the perfect opportunity to grab it and pull it. [mox] responded passionately, her [gent] tightening and back arching as she loved absolutely everything I did to her."
        "Gripping her hair firmly, I pulled her head back enough to expose her delicate neck to my hungry lips. I started to kiss and nibble at a sensitive spot, drawing out low moans of pleasure from her." 
        mc "Cum for me, cutie."
        "I growled against her neck, thrusting myself balls-deep inside her once more."
        play moans1 moansmisc1
        mox "Ooohhh, fuck! I-I’m… cumming! S-So hard!"
        "[mox]’s entire body tensed up violently as she came hard around my cock. Her insides clenched so tightly around me that I thought I might cum too. But I held on, savouring this moment for just a little longer." 
        play sound2 cum
        if gen4 == 1:
            show moxie1b cum v2
        elif gen4 == 2:
            show moxie1b cum a2
        with c
        play sound2 cum
        if gen4 == 1:
            show internalcreampie
        with c
        "Finally, after what felt like an eternity but was only a few more thrusts, I reached my second climax."
        play sound2 cum
        with c
        play sound2 cum
        with c
        "I released another thick load deep inside of her, painting her insides white with my seed. Throughout both our orgasms, I don’t stop for a second, making sure to squeeze every drop of orgasmic pleasure from the two of us."
        play sound2 cum
        with c
        play sound2 cum
        with c
        "And in my animalistic haze, I continue thrusting until we both grow tired and sensitive."
        call camerareset1 from _call_camerareset1
        play sound2 cum
        show moxie1b e3 -v2
        hide internalcreampie
        play moans1 moansmisc2
        stop ambience2 fadeout 2
        with d
        "Breathing heavily, I pulled out slowly, watching as our combined fluids trickled down [mox]’s well-fucked [gent] and drip onto the couch below us."
        "I collapsed beside her; our sweaty bodies pressed against each other's warmth. We lay there together, basking in the afterglow of our intense sexual encounter."
        show black with d
        show bg apartment 
        camera:
            zpos -350 ypos -150
        show mox satisfied
        stop moans1 fadeout 5
        stop music fadeout 3
        play ambience1 ambiencerain volume 0.5 fadein 10
        $ textbox = 1
        with d
        mox "Amazing..."
        call camerareset2 from _call_camerareset2
        with dissolve
        $ energy -= 1
        return

#Treehouse:
label treehousesexscenes:
    label lilbuttjob:
        layeredimage lily1a:
            always:
                "lily1abg"
            group night:
                attribute night:
                    "night" alpha 0.75 blend "multiply"
            always:
                "lily1alily [lilb]"
            group eyes:
                attribute 1:
                    "lily1aea [lilb]"
                attribute 2:
                    "lily1aeb"
            group cum:
                attribute cum:
                    "lily1acum"
            group action:
                attribute hands:
                    "lily1ahands"
                attribute buttjob1:
                    "lily1abuttjob 1"
                attribute buttjob2:
                    "lily1abuttjob 2"
            always:
                "lily1asfx"
        lil "What's that? You just want me to bend over, like this?"
        play music sextheme
        show lily1a 1 night
        $ textbox = 4
        call camerabreath from _call_camerabreath_10
        play moans1 moansmisc2 volume 0.4
        with d
        "My gaze followed her retreating form with mild curiosity as she wandered over to an adjacent desk, swaying seductively as she went (as seductive as [lil] can muster anyway)."
        "As she assumed the position, her tail swayed provocatively from side to side, affording me an irresistible glimpse of her enticing derriere. "
        "Noticing [lil]'s obvious attempt at subtlety—or perhaps, an endearing lack thereof—a playful smirk tugged at the corners of my lips. The way the soft light cascading through the window fell upon her dripping wet pussy, accentuating every inviting fold and crevice, painting them with an ethereal glow, left me positively spellbound."
        "Unable to tear my gaze away from this view, my eyes devoured every sway of [lil]'s voluptuous behind as she leaned further forward, her tight ass cheeks clenching invitingly. In that moment, her ass seemed to exude an almost palpable allure, practically daring me to succumb to the overwhelming urge to touch, caress, and claim every inch as my own."
        play sound1 move
        "Taking tentative steps forward, I observed her reaction closely. She pretended to be engrossed in her notebook once again, feigning indifference to my presence."
        show lily1a hands with d 
        "However, my fingers couldn't resist the allure of her supple rear end any longer. Gently squeezing her soft flanks, I felt her body involuntarily squirm under my touch—a delightful reaction that fueled my courage."
        lil "(Ooohhh, it's happening again..! Nngghh, what's wrong with me? Why do I even like this? Aahh... I'm getting so wet...)"
        show lily1a 2 with d
        "Her butt shivered and wiggled. It seemed as though she was silently encouraging me to go further. At this point, my cock was rock hard."
        lil "(Aaahhh... Forget it... I just can't resist...)"
        show lily1a buttjob1 -hands with d
        "She pushed her butt out at the perfect angle for me to slide  my cock between her fluffy cheeks and making slight contact with both her dripping wet labia and tight pucker."
        "The contact sent shockwaves of pleasure through her slender body, causing her to jolt upwards involuntarily. However, instead of pulling away in disgust or shame, she turned back towards me, revealing a mix of surprise and curiosity on her innocent face."
        show lily1a 1 with d
        lil "Seriously, what sick pleasure do you derive from this?"
        "Her voice trembled slightly with a mixture of disdain and arousal."
        mc "I imagine it's similar to the enjoyment you get, [lil]."
        "I tightened my grip on her slender hips, using them as leverage to start thrusting, pushing myself deeper into her tight ass cheeks."
        "The sensation seemed to ignite something primal within her; she let out a moan that was part pleasure, part embarrassment, her body shuddering under mine as she surrendered completely to the forbidden desire."
        camera:
            linear 0.1
            linear 0.5 xpos -5 ypos -5
            linear 0.1
            linear 0.4 xpos 5 ypos 5
            repeat
        play moans1 moansmisc3
        play ambience2 handjob
        "As those ecstatic moments stretched into an erotic haze, I felt her body begin to respond in kind—albeit tentatively at first. She started moving her hips back and forth, rocking against my rigid member."
        "The sensation of my cock gliding effortlessly between her tight anal entrance and slick pussy lips sent waves of carnal pleasure coursing through my veins."
        show lily1a 2 with d
        lil "Oohhhh... This is... depraved... but... so hot... I... I can't..."
        mc "It’s amazing." 
        "We both found our rhythm, our bodies moving in perfect syncopation now—her hips undulating against mine, her wet pussy juices lubricating my shaft generously, creating a slick friction between our genitals."
        if lilyspank == 1:
            "With her ass at my complete mercy, I remember that she quite enjoyed getting spanked."
        else:
            "With her ass at my mercy, I'm tempted to spank her. I know I didn't last time, but I could..."
        menu:
            "{i}Spank her{/i}":
                play sound1 spank
                show lily1aspanked:
                    alpha 0.3
                with d
                "I deliver a firm slap onto [lil]'s plump ass cheek, eliciting an adorable yelp of mixed pleasure and surprise from her lips. Her eyes widen with shock as she clenches her pussy tightly."
                show lily1a 1 with d
                lil "{i}Pant, pant{/i} Owie! How is that supposed to help you cum?!"
                mc "Oh it helps."
                menu:
                    "{i}Spank her again{/i}":
                        $ lily1spank = 1
                        play sound1 spank
                        show lily1aspanked:
                            alpha 0.6
                        show lily1a 2 with d
                        lily "Ooohhhh... You're so bad~"
                        play sound1 spank
                        show lily1aspanked:
                            alpha 0.9
                        with d
                        mc "You love this, don't you? Naughty slut~"
                        lily "Uuuoohhh... I'm getting so wet! Nnghh..."
                    "{i}Show mercy{/i}":
                        jump lily1amercy2
            "{i}Show mercy{/i}":
                label lily1amercy2:
                    "I brush my fingers through her fluffy butt, causing a shiver up her spine."
                lil "Mmmhh... Your hands feel so firm."
        "Feeling bold and excited by [lil]'s reactions, I gradually adjusted my thrusts so that my cock glided closer and closer to her tight entrance. Each time it brushed against her sensitive folds or pucker, it would catch and push just the tip slightly inside. This new angle created an intense friction that heightened both our sensations."
        "The sensation clearly aroused [lil], as evidenced by her moans becoming more passionate and desperate. Her body tensed up with each teasing potential invasion." 
        lil "F-Fuck! D-Don't you dare slip inside!" 
        "Each time followed by an ecstatic whinny that echoed her escalating pleasure. Her own pace didn't waver; if anything, it intensified. Her powerful thrusts matched mine perfectly."
        "The sound of her moans fueled me further; I could feel myself on the brink of climax myself. The pleasure built up inside me like an unstoppable force, threatening to consume me completely."
        mc "I'm getting close!"
        lil "Uoohhh, me too!"
        "Her eyes met mine momentarily before she closed them tightly again, lost in the throes of passion. Her body shivered with desire as she began grinding against me harder than ever before. Her ass ground against mine with such force that it felt like she was trying to grind every last drop of my cum from me. It was too much for me to handle."
        play sound2 cum
        show lily1a buttjob2
        with c
        play sound2 cum
        show lily1a cum
        with c
        mc "Oohhh, I’m cumming!"
        play sound2 cum
        with c
        play sound2 cum
        with c
        "Gasping and shuddering, my voice hoarse with pleasure, I cried out as an intense orgasm washed over me, shooting thick streams of hot cum from the tip of my cock."
        play sound2 cum
        with c
        play sound2 cum
        with c
        "It splattered against [lil]'s ass cheeks, painting her ass white with my seed."
        lil "Nngghhh, so much! {i}Pant, pant{/i}"
        call camerareset1 from _call_camerareset1_1 
        call stopbgs from _call_stopbgs_7
        show lily1a 1 cum -buttjob2
        with d
        "As the waves of bliss subsided gradually, and I reveled in the afterglow of this experience."
        lil "{i}Pant, pant{/i} Amazing! I, I mean... I actually came that time... Just what I needed."
        stop music fadeout 3
        $ energy -=1 
        return
    label lildoublehandjob:
        lil "I suppose I better summon that troublemaker."
        show black with d
        "A solid thirty seconds later..."
        $ lil2count += 1
        $ lil2 = "{} {}.0".format(lil, lil2count)
        play music sextheme 
        play moans1 moansmisc2 fadein 5
        stop ambience1 fadeout 10
        scene lil2a l2e1 
        call camerabreath from _call_camerabreath_25
        $ textbox = 2
        with d
        "[lil2] kneels before me my crotch, and with large, adorable eyes looks up at me patiently as if waiting for my cock."
        $ lily2 = 1
        show lil2a l2e1 with d
        lil2 "So big! Say, why don't we find out if it really is more pleasurable for someone else to touch it, hm?"
        mc "I hope a single load is enough for your statistical analysis."
        lil2 "Ohh, it might be~"
        show lil2a lily1 l1e1 with d
        lil "Hey! Don't you dare start without me."
        "[lil] quickly jumps in and makes herself known, one hand moving to her breast, another down to her inner thighs. A third hand, the clone's, reaches for my cock."
        lil "Is there anything else you want before we start?"
        $ gen1 = 0
        $ gen2 = 0
        menu lildoublehandjobm:
            "Horsecock (Needs Lewd Spellbook)" if lewdspellbook == 0:
                jump lildoublehandjobm
            "Horsecock" if lewdspellbook == 1:
                if gen1 == 0:
                    $ gen1 = 1
                    show lil2a hj2 with c
                    lil "Now this is a spell I just have to try!"
                    lil2 "Uoohh... I want this beast inside me so badly~ I can feel my pussy itch just thinking about it."
                    lil2 "Just thinking about myself reduced back to an animal in heat, pumped full of virile cu-"
                    lil "T-That's quite enough of that!"
                else:
                    $ gen1 = 0
                    show lil2a -hj2 with d
                jump lildoublehandjobm
            "Goth Outfit (Needs Purchasing)" if goth == 0:
                jump lildoublehandjobm
            "Goth Outfit" if goth == 1:
                if gen2 == 0:
                    $ gen2 = 1
                    show lil2a goth with d
                    lil2 "So, what do you think~"
                    mc "Woah..."
                else:
                    $ gen2 = 0
                    show lil2a -goth with d
                jump lildoublehandjobm
            "Milky (In Development)":
                jump lildoublehandjobm
            "(Continue)":
                pass
            "(Stop Scene)":
                return
        if gen1 == 0:
            show lil2a hj1 with d
        "[lil2] wrapped her hand around my cock. The tingling sensation from her touch made me hard within seconds."
        lil "Unnhhff... Do I really make you that hard?"
        mc "That's right, cutie~"
        lil2 "Hehe, and you wouldn't believe how wet you get us~"
        play ambience1 handjob
        with hpunch
        show lil2a l2e3 with d
        "She began to stroke my throbbing member vigorously with one hand, her hips swaying rhythmically with each powerful motion, and her cute chest rising with each breath."
        lil "N-Not that wet! C-Come on now... I'm not that easy."
        mc "Remember [lil], be true to yourself."
        lil "I… I'm pretty wet, obviously..."
        show lil2a l2e2 with d
        lil2 "Mmm… I'm getting soaked. The scent of your cock drives me pretty wild~"
        with hpunch
        "She purred before resuming her relentless strokes."
        "The real [lil] watched from the sidelines, her heart racing and cheeks flushing a deep crimson."
        "Her own marehood tingled with unfulfilled desire as she watched her clone receive and give it so eagerly and openly. The scent and sight made it difficult for her to ignore the building heat in her loins."
        mc "Ooohhh, looks like you remember what you practiced from last time!"
        lil "S-Seriously? My clones are improving?"
        show lil2a l2e3 with d
        lil2 "Of course, dear. Once I return to you, so do a portion of my experiences~"
        lil "Uwaaahhhhhhh, what are you even talking about?! I don't want to be like you! You're far more open and... yeah..."
        lil2 "Come on, [lil], be the real us~ Show [mc] just how wet you are right now."
        show lil2a l1e2 with d
        lil "F-Fine... Just this once..."
        "[lil]'s fingers thrust deep into her pussy, the wet sounds distinct and loud enough to overpower even her clone's handjob."
        lil2 "Hehe, so wet~ Finger yourself as fast I stroke this cock."
        lil "Aahhh... F-Fine... Mmpphh!"
        "Well, this was hot. I groaned in pleasure under the skilled ministrations of the clone. My cock throbbing as precum drips from the tip."
        lil2 "You want to cum, don’t you? Cover my face in your hot seed? Mmmhhh…"
        "She purred seductively before swiftly increasing the pace of her strokes."
        lil "Uoohhh, ooohhh...!"
        lil2 "Hehe, are you getting close too, me~?"
        show lil2a l2e2 with d
        lil2 "I knew you had it in you. After all, you’re me~"
        "Encouraged by the fervant fingering, the clone glanced back with a triumphant smirk before returning her attention to me. She leaned closer still, her hot breath grazing against my tip."
        show lil2a l2e3 with d
        lil2 "That’s it… Let me help you cum for both of us."
        "I moaned in ecstasy as I felt myself on the brink of orgasm. My shaft stiffened under the assault of her eager hands, and prepared to unload."
        play sound2 cum
        if gen1 == 0:
            show lil2a l1e2 l2e2 cum hj1cum with c
        else:
            show lil2a l1e2 l2e2 cum hj2cum with c
        play sound2 cum
        with c
        "With a roar of pleasure, my tip erupted fiercely. My hot seed spurted forth like a geyser, splattering both the mares’ faces and breaths."
        play sound2 cum
        show lil2a l2e1 with c
        play sound2 cum
        with c
        "Simultaneously, [lil]'s lower body spasms; clear orgasmic contractions as her insides tightened around her fingers."
        lil2 "Ooohhh yes… Good girl~"
        lil "Mmhhh… Come on, don't call yourself that... It's weird."
        lil2 "Hehe, don't make me lick that cum off you~"
        lil "Uuhhhhh! I'm gonna unsummon you!"
        $ energy -= 1 
        return
    label pencowgirl:
        layeredimage moxpen2b:
            always:
                "moxpen2bbase [penb]"
            group lingerie:
                attribute lingerie:
                    "moxpen2blingerie"
            group eyes:
                attribute e1:
                    "moxpen2bea [penb]"
                attribute e2:
                    "moxpen2beb [penb]"
                attribute e3:
                    "moxpen2bec [penb]"
            group sex:
                attribute sex1:
                    "moxpen2b 1"
                attribute sex2:
                    "moxpen2b 2"
                attribute sex3:
                    "moxpen2b 3"
                attribute sex4:
                    "moxpen2b 4"
            group action:
                attribute action:
                    "moxpen2baction [penb]"  
            group night:
                attribute night:
                    "night" alpha 0.4 blend "multiply"
        play music sextheme fadein 3
        scene bg bedroom2
        show night:
            alpha 0.5
            blend "multiply"
        with dissolve
        show moxpen2b e1 night 
        $ textbox = 2
        with d
        pen "How'd you like me tonight, cutie?"
        menu pencowgirlm:
            "Lingerie (Needs Purchasing)" if lingerie == 0:
                jump pencowgirlm
            "Lingerie" if lingerie == 1:
                if gen1 == 0:
                    $ gen1 = 1
                    play sound2 equip
                    show moxpen2b lingerie
                    pen "Cute, right?"
                else:
                    $ gen1 =0
                    show moxpen2b -lingerie
                jump pencowgirlm
            "Futa (In Development)":
                jump pencowgirlm
            "Pregnant (In Development)":
                jump pencowgirlm
            "(Continue)":
                pass
            "(Stop Scene)":
                play music penelopetheme fadein 1
                scene bg peneloperoom
                show night:
                    alpha 0.5
                    blend "multiply"
                show pen happy
                with d
                pen "You're such a tease~"
                return
        pen "You ready?"
        mc "You know it. Show me what those hips can do."
        "As I lay there on the soft bed, I watched with bated breath as she descended gracefully towards me. Her eyes locked with mine, filled with desire and need."
        play sound2 cum
        show moxpen2b e2 sex2 with dissolve
        play moans2 moansmisc3
        with hpunch
        "She lowered herself slowly, savoring every sensation, her every move driving me wild with anticipation. Then finally, her tight pussy lips engulfed me completely."
        "She moaned deeply, a primal sound of pure ecstasy escaping from deep within her chest. Her inner walls clenched tightly around me like a velvet vice, milking moans of blissful pleasure from deep within me."
        "I couldn't help but marvel at how perfectly we fit together. Her body, designed by nature herself, seemed to mold perfectly around me; an exquisite symphony of smoothness and tightness that sent waves of unadulterated bliss coursing through my veins."
        camera:
            zpos -18
            block:
                linear 0.3 ypos -8 
                linear 0.1
                linear 0.2 ypos 8
                linear 0.1 
                repeat
        show moxpen2b action with dissolve
        with d
        play ambience2 sex
        "Wasting no time, her hips began to rock with a manic, desperate energy to claim as much pleasure as possible. This wasn't mere heat, there was a fire within her that refused to be quenched."
        pen "Aahhh, ngghhh... Your cock is so thick! You're filling me completely! Mmgghhh..."
        "I tried to return some thrusts, but at times her speed was almost overpowering."
        mc "That's it, babe, ride that cock~!"
        "She clung to my thighs, fingers digging in slightly as she used them as leverage for her relentless riding. Her hips swayed hypnotically, grinding against mine in perfect rhythm with each deep thrust."
        "Soon, she was so wet that each time out bodies met, it produced a wet slapping sound that echoed throughout the wooden bedroom. This combined with our ever-louder moans intermingling, created quite the erotic symphony which [lil] could almost certainly hear from her nearby bedroom."
        "I can only imagine that [lil] is the type to masturbate to these sounds with her ear to the wall."
        "[pen] moaned even louder, her pace quickening. She leaned forward this time, her breasts brushing against my chest as her whole body shook with each powerful thrust. The friction between our bodies intensified even further, sending shockwaves of pleasure coursing through us both."
        pen "Oh! I'm close... I'm gonna cum... Aahhhh..."
        mc "Already?! Does it really feel that good?"
        play moans1 moansmisc4
        pen "Oohhh, god yes! Your cock is amazing! Ooohhh, I'm cumming!"
        "With her orgasm, came waves of tightness as her pussy contracted around me shaft. As her inner walls clenched, I knew I probably wouldn't last much longer either, especially as she rode me harder and faster than ever before."
        "I wrapped my arms around her slender waist, pulling her body against mine as hard as I could."
        mc "I'm about to cum!"
        pen "Yes! Fill me up, [mc]!"
        "With one final thrust that sent waves of ecstasy coursing through us both... I reached an explosive orgasm."
        play sound2 cum 
        show moxpen2b sex3 with c
        play sound2 cum 
        show internalcreampie with c
        "My own orgasm washed over me like a tidal wave, filling her womb with hot seed."
        play sound2 cum
        with c
        play sound2 cum
        with c
        "Our bodies shook with shared pleasure as we rode out our climaxes."
        play sound2 cum
        show moxpen2b sex4 e3 -action
        hide internalcreampie
        call camerareset from _call_camerareset_2
        call stopbgs from _call_stopbgs_13 
        with c
        "And just at the edge of my orgasm, [pen] purposely allowed me cock to pop out, showering her entire body in a layer of hot cum."
        pen "Aaahhhh... Look at me... I'm such a slutty mare, covered in your cum~"
        pen "I couldn't even resist your cock when we first met, and now I'm addicted to it! Hehe."
        scene bg peneloperoom
        show night:
            alpha 0.5
            blend "multiply"
        show pen happy
        $ textbox = 1
        with d
        $ energy -=1 
        pen "Phew... Alright, I've calmed down a bit now."
        return
    label penboobjob:
        if petplay == 1:
            pen "Want me to be your naughty bitch again?"
        else:
            pen "Want to try using that collar this time?"
        "She led me over to the sofa, her seductive, expectant glare sent a thrill through me."
        show pen1a e1 
        if petplay == 1:
            show pen1a collar
        $ textbox = 2
        call camerabreath from _call_camerabreath_26
        play music sextheme
        play moans1 moansmisc2
        with d
        "[pen] took a step back, her eyes fixed on mine as she slowly lowered herself to her knees in front of my growing erection."
        "She knelt between my legs, her eyes filled with lust and submission."
        pen "All you have to do is ask, and I'll do anything you want~"
        if petplay == 1:
            $ gen1 = 1
            $ gent1 = "Master"
        else:
            $ gen1 = 0
            $ gent1 = "{}".format(mc)
        menu penboobjobmenu:
            "Pet-Play":
                if gen1 == 1:
                    $ gen1 = 0
                    show pen1a -collar with d
                    $ gent1 = "{}".format(mc)
                    pen "That's okay, [gent1], we don't need to do it like that every time."
                else:
                    $ gen1 = 1
                    show pen1a collar with d
                    $ gent1 = "Master"
                    pen "Mmfhh... [gent1] I'm already getting wet just thinking about being your naughty bitch."
                jump penboobjobmenu
            "Breast Expansion (In Development)":
                jump penboobjobmenu
            "Continue":
                pass
            "(Stop Scene)":
                scene bg peneloperoom
                show night:
                    alpha 0.5
                    blend "multiply"
                show pen happy
                if petplay == 1:
                    show pen collar
                with d
                return
        if gen1 == 1:
            $ petplay = 1
            mc "Now, use your breasts, you slutty bitch."
            pen "Uoohhh, yes, Master~"
            "[pen] began by pressing her soft, ample breasts around my shaft, her collar jingling slightly with her movements."
        else:
            pen "Make yourself comfortable, hehe..."
            "[pen] began by pressing her soft, ample breasts around my shaft." 
        play ambience1 handjob
        camera:
            linear 0.2 zpos -17 ypos -2 xpos 0
            block:
                linear 0.1
                linear 0.3 ypos 8
                linear 0.1
                linear 0.2 ypos -8
                repeat
        "The sensation was incredible, the warmth and softness of her fur sending waves of pleasure through me. She squeezed her breasts together, creating a tight, velvety tunnel, and started to move up and down, her eyes never leaving mine."
        "Occasionally, she would flick her tongue out, licking the tip of my cock, sending electric shivers down my spine. Her dedication and skill were evident in every movement, her breasts gliding smoothly along my length. She was much better than the first time."
        if petplay == 1:
            "I tightened my grip on the leash, pulling her closer, the leather collar digging slightly into her neck."
            mc "You're such a good bitch, [pen]."
        else:
            mc "Mmphhh, that feels so good! You've really improved!"
        "I praised, watching as her eyes sparkled with pleasure at my words. She increased her pace, her breasts moving faster, her tongue flicking out more frequently to tease me. The combination of her breasts and long pony tongue was driving me wild, the pressure building steadily."
        if petplay == 1:
            pen "Yes, Master. I'm your naughty bitch~!" 
            "She responded breathlessly, her voice filled with arousal. The collar and leash accentuated her submissive role, each tug and pull reinforcing the power dynamic between us."
            "As I felt myself getting closer, I pulled harder on the leash, this spurred her on to move faster, her tongue starting to get seriously sloppy."
        else:
            pen "Mmmhhh... I can't allow myself to get stale while there are so many other mares pining for your attention now, can I~"
            mc "Hah, you're actually been practicing?"
            pen "Mmh, I've seen a few videos~ Now about at this technique?"
        mc "Oohh, okay, that's amazing! Aahh... I'm going to cum soon!"
        "Even though I tried to hold back, [pen] didn't slow down; if anything, she became even more determined, her breasts moving with increased fervor."
        if petplay == 1:
            pen "Do it, Master! Cum for your little bitch!" 
        else:
            pen "Aahh, cum for me, [mc]!"
        "Her tone both submissive and eager. The combination of her words and her relentless movements pushed me over the edge."
        play sound2 cum
        show pen1a e2 cum with c
        play sound2 cum
        with c
        "With a final, powerful thrust between her breasts, I released, my cum spilling onto her fur and her tongue as she eagerly licked up every drop she could reach."
        play sound2 cum
        with c
        play sound2 cum
        with c
        "She moaned in delight, continuing to move until I was completely spent."
        stop ambience1 fadeout 3
        call camerareset from _call_camerareset_5
        "Once finished, [pen] looked up at me, her face brimming with satisfaction."
        if petplay == 1:
            mc "Good girl~"
            pen "Thank you, master."
        else:
            mc "That was exceptional..."
            pen "Hehe, it's a lot of fun for me too. But if you ever wanted to return the favor, my pussy is eagerly awaiting your next move~"
        "I gently petting her head. She leaned into my touch, a contented smile spreading across her face, her devotion and submissiveness clear in every fiber of her being."
        play music penelopetheme fadein 1
        scene bg peneloperoom
        show night:
            alpha 0.5
            blend "multiply"
        show pen happy
        $ energy -= 1
        return
    label penfrombehind:
        "She walked over to the couch with a seductive sway in her lips."
        if petplay == 1:
            mc "Get on your belly, pet"
        else:
            mc "Get on your belly."
        pen "Yes sir!"
        "Obediently, she crawled on the crouch, lying down with her face pressed against a cushion, and her backside raised invitingly."
        show pen1b e1 norope with d
        pen "What's your appetite tonight? Serve me however you want~"
        $ gen1 = 0
        $ gen2 = 0
        $ gen3 = 0
        if tiedup == 1:
            $ gent1 = "rope"
        else:
            $ gent1 = "bed"
        menu penfrombehindm:
            "Rope":
                if gen1 == 1:
                    $ gen1 = 0
                    $ gent1 = "bed"
                    show pen1b e1 norope with d
                else:
                    $ gen1 = 1
                    $ gent1 = "rope"
                    show pen1b e1 rope with d
                    pen "Oohhh, my pussy is soaking~"
                jump penfrombehindm
            "Lingerie (Needs Purchasing)" if lingerie == 0:
                jump penfrombehindm
            "Lingerie" if lingerie == 1:
                if gen2 == 1:
                    $ gen2 = 0
                    show pen1b -lingerie  with d
                else:
                    $ gen2 = 1
                    show pen1b lingerie with d
                jump penfrombehindm
            "Buttplug (Needs Purchasing)" if buttplug == 0:
                jump penfrombehindm
            "Buttplug" if buttplug == 1:
                if gen3 == 1:
                    $ gen3 = 0
                    show pen1b -plug  with d
                else:
                    $ gen3 = 1
                    show pen1b plug with d
                jump penfrombehindm
            "(Continue)":
                pass
            "(Stop Scene)":
                scene bg peneloperoom
                show night:
                    alpha 0.5
                    blend "multiply"
                show pen happy
                if petplay == 1:
                    show pen collar
                with d
                return
        if tiedup == 1:
            "I had produced some soft, but sturdy rope from [pen]'s bag. And tied her wrists together behind her back. The rope looped around her arms and chest, securing her tightly. She wiggled slightly, testing her bonds, a satisfied sigh escaping her lips as she realized how firmly she was restrained."
            "From behind, I could literally watch her pussy drip with need. To say that she was 'getting off' on this would be the understatement on the century." 
            "She was completely at my mercy, her body presented perfectly for my pleasure. I took a moment to admire my work, her goosebumps texturing her fur and her breathing heavy with anticipation."
            mc "You're such a good girl, [pen]... Now... Just what am I going to do to you?" 
        else:
            "In this position, she was completely at my mercy, her body presented perfectly for my pleasure."
            mc "Now... Just what am I going to do to you?" 
        "I ran my hand along her back, feeling her shiver under my touch. Her response was a soft, submissive whimper, her body eager for what was to come."
        "I positioned myself behind her, running my hands over her thighs, spreading her cheeks for a gorgeous view. Her body quivered with each touch, the anticipation building between us. I could feel the heat radiating from her, the readiness in her posture."
        "With one swift motion, I pressed against her entrance."
        if petplay == 1:
            mc "Are you ready, my pet?"
            pen "Yes, Master! Please, take me~"
        else:
            mc "Are you ready?"
            pen "Mhm! Please~"
        menu penfrombehindm2:
            "Vaginal":
                $ gent2 = "pussy"
                show pen1b v1 e2 with d
            "Anal (Requires Lubricant)" if lubrication == 0:
                jump penfrombehindm2
            "Anal" if lubrication == 1:
                $ gent2 = "ass"
                if gen3 == 1:
                    $ gen2 = 0
                    show pen1b -plug with d
                    "First I pop out the buttplug, eliciting a cute moan from [pen]."
                "I take out my bottle of bottomless lube and apply it directly to her tight pucker, I gently spread it around as she squirms."
                pen "Uoohhh, r-really?!"
                show pen1b a1 e2 with d
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
        "I entered her [gent2] slowly, savoring the sensation of her tightness enveloping me. Her body rocked against the [gent1] slightly with each thrust, her breath hitching as I filled her completely. I gripped her hips firmly, pulling her back onto me, setting a steady rhythm that had us both moaning in pleasure."
        if gen1 == 1:
            "Her bindings ensured she couldn't move much, leaving her entirely at my mercy as I took her from behind. The rope bit into her fur, a constant reminder of her submission and the power I held over her."
        pen "Uooohhohoh... That first feeling of being filled up by you is breathtaking every time~"
        if gent2 == "ass":
            mc "Nghh, and it's even tighter in your ass! Damn!"
            pen "{i}Pant, pant{/i} No kidding...~ But don't you dare go soft on me now, you know I love it hard!"
        "Each thrust pushed her deeper into the couch, her cries of pleasure muffled by the cushions."
        if petplay == 1:
            mc "You're such a perfect little bitch."
        "I growled, increasing my pace, feeling the pressure building within me. Her moans grew louder, matching my intensity, her body responding eagerly to every movement."
        if petplay == 1:
            pen "Thank you, master!"
        else:
            pen "Aaahhh, h-harder! I love it!"
        "She gasped between moans, her voice dripping with submissive bliss. The sound of her pleasure only spurred me on, driving me closer to the edge."
        "As I neared my climax, I tightened my grip on her hips, pulling her back onto me with each thrust. The sensation was overwhelming, her body grinding against the [gent1]."
        mc "I'm about to...!"
        if petplay == 1:
            pen "Yes! Cum for me, Master~!"
        else:
            pen "Yes! Cum for me~! Uoohhh, I'm cumming too!"
        "The sight and sound of her climaxing pushed me over the edge, and I reached my own release, filling her with my seed."
        play sound2 cum
        if gent2 == "pussy":
            show pen1b v2 cum with c
        else:
            show pen1b a2 cum with c
        play sound2 cum
        with c
        "[pen]'s body shuddered with pleasure as she felt her [gent2] get filled up with hot cum, her cries muffled against the couch."
        play sound2 cum
        with c
        play sound2 cum
        show pen1b -v2 -v1 -a1 -a2 cum e3
        hide internalcreampie
        call camerareset from _call_camerareset_6
        call stopbgs from _call_stopbgs_21
        with c
        "We stayed like that for a moment, both of us catching our breath."
        scene bg peneloperoom
        show night:
            alpha 0.5
            blend "multiply"
        show pen happy
        if petplay == 1:
            show pen collar
        with d
        pen "I feel like I could run a marathon! {i}Yawn{/i} Tomorrow..."
        return 
#Brothel:
label brothelsexscenes:
    label rubmissionary:
        stop music fadeout 3
        show black with d
        play music sextheme
        play moans1 moansmisc2
        scene black with d
        $ textbox = 2
        with d
        "[rub] moves to a couch against a wall, leans back and stretches, causing the band of her bathrobe to unfurl and the clothing to fall backwards, leaving her bare." 
        show ruby1b e1 with d
        "She spreads her legs, her pussy so wet that it creates an audible schlick as it’s spread open by the movements."
        rub "It's rare for me to find a man irreistable. To think I'm back here again already."
        mc "Those are my lines you're stealing."
        rub "How would you like to take me today?"
        $ gen1 = 0
        $ gen2 = 0
        menu rubmissionarymenu:
            "Vaginal":
                $ gen1 = 1
                $ gent1 = "pussy"
            "Anal (Needs Lubrication)" if lubrication == 0:
                jump rubmissionarymenu
            "Anal" if lubrication == 1: 
                $ gen1 = 2
                $ gent1 = "ass"
                rub "Ohh? Goodness, that's naughty even for me~"
                if gen2 == 1:
                    $ gen2 = 0
                    show ruby1b -plug with d
                    "First I pop out the buttplug, eliciting a cute moan from [rub]."
                "I take some lube out of a nearby drawer that's filled with other sexual implements. Applying it directly to her pink pucker, I gently spread it around as she squirms."
                rub "Nnghh... I can't wait."
            "Buttplug (Needs Purchasing)" if buttplug == 0:
                jump rubmissionarymenu
            "Buttplug" if buttplug == 1:
                play sound2 equip
                if gen2 == 0:
                    $ gen2 = 1
                    show ruby1b plug with d
                    rub "Ooohh, you're so naughty, darling."
                else:
                    $ gen2 = 0
                    show ruby1b -plug with d
                    "{i}Pop!{/i}"
                    rub "Uuohhh, you tease~"
                jump rubmissionarymenu
        rub "May I be unladylike for a second? I want you to ravish me with that fat cock of yours~"
        "She leans her hips forward and spreads her gooey [gent1] wide for me, inviting me to fuck her senseless." 
        mc "How could I refuse an offer like that?"
        "The sight of the refined unicorn lady in such a state of wanton need was enough to make my cock fully erect in a matter of seconds. I closed the door behind us before striding over to the table, my eyes feasting on every inch of [rub]’s exposed body."
        "Her delicate body was flushed with desire, sweat beading on her forehead and between her large breasts that bounced enticingly as she panted. The toll of her heat was clear; she needed this." 
        rub "I expect you to know all my sweet spots, okay~?"
        mc "You know it."
        "She arched her hips up towards him, her [gent1] glistening in anticipation of my cock thrusting inside."
        if mel1 == 1:
            "It almost feels wrong to fuck her straight after her sister gave me a blowjob. My cock might even still be a little slick from it, which just makes it feel so wrong in all the right ways." 
        play sound2 cum
        if gen1 == 1:
            show ruby1b e2 v1
        else:
            show ruby1b e2 a1
        play moans1 moansmisc3
        with c
        "Wasting no more time, I grabbed hold of her hips with one hand, and guided my cock with the other. Pressing my tip against her wet entrance, I thrust hard, burying myself to the hilt inside her tight [gent1] in one smooth nation."
        "A ragged moan tore from her throat at the incredible feeling of being filled after an arduous season of heat."
        rub "Oooohhhh… Goodness me, I {b}needed{/b} that."
        play ambience1 sex
        "She continued to let out high-pitched whines of pure pleasure as I started thrusting—my cock grinding against all the right spots inside of her, sending shockwaves of pleasure coursing throughout her body."
        "Clenching tightly around my shaft, she teased and squeezed every inch of my cock with deliberate contractions and relaxations, an exquisite technique that I nearly forgot she had."
        "These motions transformed what would be primal rutting into a dance of lust where we moved to each other’s rhythm and our sex became more than the sum of its parts."
        mc "Mmhh, damn! I have no idea how you do that with your [gent1], but never stop! {i}Thrust, thrust, thrust{/i}"
        rub "Hehe, I won’t stop if you don’t, darling… Mmhh, kiss me~"
        "Our lips locked together as her longer equine tongue quickly dominated my mouth. I love kissing these mares with their long muzzles, it feels so natural and sensual."
        "As the passion of our kiss intensified, so did our thrusting. The sound of our bodies slapping together got so loud that it echoed loudly throughout the room. Sweat dripped down from the body of us onto the office table beneath us, staining the pristine wood with our lust."
        "[rub]’s nails dug into the fabric of the tablecloth, leaving deep furrows as she arched her back off the table, begging for more."
        rub "Fuck me harder~"
        "She moaned breathlessly between gasps of air."
        rub "Rut me like the filthy mare I am!"
        "Don’t mind if I do! I picked up the pace, slamming into her tight [gent1] again and again without mercy or restraint."
        "I could feel myself getting closer and closer, and as she reached her climax, I was soon to follow."
        play sound2 cum
        if gen1 == 1:
            show ruby1b e2 v2 cum
        else:
            show ruby1b e2 a2 cum
        with c
        play sound2 cum
        if gen1 == 1:
            show internalcreampie
        with c
        "With one final, powerful thrust, I reached my release. My cock pulsed thick ropes of hot cum deep inside of [rub]’s [gent1]."
        play sound2 cum
        with c
        play sound2 cum
        with c
        rub "Uooohhhhh, yeeesssss! Pump me full!"
        "My seed mixed with her own juices as I continued pounding into her, milking every last drop of pleasure I could from our shared orgasm."
        "Finally spent, I pulled out of her slick [gent1], leaving behind a messy trail of our combined fluids dripping down onto the table below her." 
        show ruby1b e3 -v2 -a2
        hide internalcreampie
        with d
        "Panting heavily, we caught each other’s eyes—two people who had just experienced the height of carnal pleasure together."
        "There was no pretense of refinement or ladylike behavior from her—just an animal driven wild by lust during the heat of mating season. And damn did she enjoy every filthy second of it."
        play music clubtheme fadein 5
        scene bg brothel5
        show rub happy 
        call stopbgs from _call_stopbgs
        call camerareset2 from _call_camerareset2_1
        $ textbox = 1
        with d
        rub "Simply fantastic performance, darling."
        mc "You were keeping score?!"
        $ energy -= 1
        return
    label rubfrombehind:
        rub "My, my... You want to take me in one of our booths like a mere whore~?"
        mc "Your words, not mine!"
        rub "Oh, just hurry up and ravish me, you beast~!"
        "Someone's horny!"
        play music sextheme
        play moans1 moansmisc2
        show rub2a e1a
        $ textbox = 2
        call camerabreath from _call_camerabreath_27
        with d
        "Not patient enough to even reach the booths, she positions herself on a nearby sofa, her belly against the cushions and her arms forward. She looks over her shoulder at me, her eyes filled with excitement."
        rub "I forgot to bring my own things this time, dear. If you have any preferences, I'm happy to accomodate."
        $ gen1 = 0
        $ gen2 = 0
        menu rubfrombehindm:
            "Lingerie (Needs Purchasing)" if buttplug == 0:
                jump rubfrombehindm
            "Lingerie" if lingerie == 1:
                play sound2 equip
                if gen1 == 0:
                    $ gen1 = 1
                    show rub2a lingerie with d
                    rub "Aahhh, isn't it a beautiful contrast on my snow white fur?"
                else:
                    $ gen1 = 0
                    show rub2a -lingerie with d
                jump rubfrombehindm
            "Buttplug (Needs Purchasing)" if buttplug == 0:
                jump rubfrombehindm
            "Buttplug" if buttplug == 1:
                play sound2 equip
                if gen2 == 0:
                    $ gen2 = 1
                    show rub2a plug with d
                    rub "Ooohh, you're so naughty, darling."
                else:
                    $ gen2 = 0
                    show rub2a -plug with d
                    "{i}Pop!{/i}"
                    rub "Uuohhh, you tease~"
                jump rubfrombehindm
            "(Continue)":
                pass
            "(Stop Scene)":
                return
        $ rub2 = 1
        mc "Damn, you're soaked."
        rub "Now, don't be gentle with me~ My heat has been really bad this season… Mmhh... I’d appreciate it if you went hard."
        menu rubfrombehindm2:
            "Vaginal":
                $ gent1 = "pussy"
                rub "Aahh, my favourite~ I'm all yours."
            "Anal (Needs Lubrication)" if lubrication == 0:
                play sound2 error
                jump rubfrombehindm2
            "Anal" if lubrication == 1:
                $ gent1 = "ass"
                rub "If you have the lube, it's all yours~"
                if gen2 == 1:
                    show rub2a -plug
                    "First, I pop out the buttplug, elicting a lady-like moan from [rub] as it pops out."
                "I drip some lubrication onto the tip of my fingers and slowly massage it into her pucker. She coos and wiggles in response to the cool touch."
        "I swallowed hard, my heart racing with the intensity of the moment. In three swift strides, I closed the distance between us, my pulse quickening at the sight of her raised, inviting ass."
        "Running my hands over her exposed skin, I felt the smoothness beneath my touch. [rub]'s soft moan filled the air, sending a thrill of anticipation through both of us."
        "Positioning myself behind her, I could feel my arousal pressing against her, eliciting a gasp as I pressed against her warmth. [rub]'s voice, husky with desire, filled the room."
        rub "Ooohh, I still can’t believe how thick you are down there… I want to really feel it stretching me out."
        play sound2 cum
        if gent1 == "pussy":
            show rub2a v1 with d
        else:
            show rub2a a1 with d
        "Entering her, a low, throaty moan escaped her lips, mingling with the night air, a melody of pleasure and surrender."
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
        "Her pleas fueled my arousal, each thrust driving deeper, gripping her hips for leverage. [rub]'s moans crescendoed, her body moving in sync with mine. I marveled at the contrast between her refined demeanor and her uninhibited desires."
        rub "Yes, darling! Aaahh, ahhh! Just like that!"
        "[rub] cried out, her voice trembling with ecstasy. Her melodic moans spurred me on, our bodies moving as one."
        "My hips thrust with increasing intensity, hers pushing back in perfect harmony. Her back arched beautifully, pushing herself against me, urging me to go deeper."
        rub "Uoohhh, I-I’m really about to cum already!"
        "Her outburst of gasps and moans sent waves of sensation through me, her tightness squeezing around me. It was pure bliss, every inch of me caressed from every angle."
        "But the euphoria wasn't mine alone; it surged through [rub], a culmination of desire unleashed by our connection. Her heat had become a catalyst, igniting a passion she couldn't resist." 
        mc "Ngghh, I’m getting close too!"
        rub "Aaahhh, cum inside! Fill my [gent1] up~"
        mc "Ooohhh, cumming!"
        play sound2 cum
        if gent1 == "pussy":
            show rub2a v2 e2a cum with c
        else:
            show rub2a a2 e2a cum with c
        play sound2 cum
        with c
        "Her words push me over the brink. With a final, powerful thrust, I reach my climax, orgasmic sensations flooding through me."
        play sound2 cum
        with c
        play sound2 cum
        with c
        rub "Nnghh, that feels so fucking good, darling!"
        $ energy -= 1
        return
    label rublegsup:
        rub "Oh, darling... I adore that position."
        show rub2b e1
        play moans1 moansmisc2
        $ textbox = 2
        with d
        "[rub] shifts around onto her back and assumes the next position she wants to be pounded in. She wasn't kidding, she's a lady that how to get what she wants, and I'd be lying if I said my cock wasn't rearing to go again." 
        rub "Take me how you'd like me, dear."
        $ gen1 = 0
        $ gen2 = 0
        menu rublegsupm:
            "Lingerie (Needs Purchasing)" if buttplug == 0:
                jump rublegsupm
            "Lingerie" if lingerie == 1:
                play sound2 equip
                if gen1 == 0:
                    $ gen1 = 1
                    show rub2b lingerie with d
                    rub "Aahhh, isn't it a beautiful contrast on my snow white fur?"
                else:
                    $ gen1 = 0
                    show rub2b -lingerie with d
                jump rublegsupm
            "Buttplug (Needs Purchasing)" if buttplug == 0:
                jump rublegsupm
            "Buttplug" if buttplug == 1:
                play sound2 equip
                if gen2 == 0:
                    $ gen2 = 1
                    show rub2b plug with d
                    rub "Ooohh, you're so naughty, darling."
                else:
                    $ gen2 = 0
                    show rub2b -plug with d
                    "{i}Pop!{/i}"
                    rub "Uuohhh, you tease~"
                jump rublegsupm
            "(Continue)":
                pass
            "(Stop Scene)":
                return
        menu rublegsupm2:
            "Vaginal":
                $ gent1 = "pussy"
                play sound2 cum
                show rub2b v1 e2 with d
            "Anal (Needs Lubrication)" if lubrication == 0:
                jump rublegsupm2
            "Anal" if lubrication == 1:
                $ gent1 = "ass"
                $ gen2 = 0
                show rub2b -plug with d
                "First, I pop out her buttplug, getting a resounding groan from [rub] as it pops out. In her position, she can't quite see what I'm planning, but as the cooling feel of lubricant is suddenly applied to her plug-loosened pucker, she gets a pretty good idea."
                play sound2 cum
                show rub2b a1 e2 with d
        "I pressed my pulsing cockhead against her snug entrance, teasingly circling before thrusting deep inside, stretching her in ways she'd never felt. Her tightness gripped me fiercely, every vein on my cock throbbing with urgency."
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
        "With a sharp intake of breath, she emitted a blend of pain and pleasure, her hair tugged gently by my grip as I pounded into her with unyielding force, relishing the sensation of her tightening [gent1]."
        if gen2 == 1:
            "The plug in her ass also made her feel tighter, as if this lady needed anymore advantages over me in the battlefield of love."
        rub "Uooohhhh, holy fuck… You’re such a beast~"
        "My hips drove into hers relentlessly, each thrust plunging deeper into her core. The tightness around my cock heightened my arousal, bringing me dangerously close to the edge."
        "Gripping her plush flank firmly, I squeezed as I maintained my fervent pace, her tight [gent1] yielding to my insistent thrusts."
        "With each powerful thrust, I felt her body yielding to mine, her moans becoming more urgent as I explored every inch of her trembling form. She was reaching the apex of her pleasure so fast, aided by the deep penetration of this position."
        "Her fur was damp with sweat, muscles taut with anticipation, and I relished the sight of her surrendering to my desires. The rhythm of our bodies became a symphony of need, a primal dance of lust and submission echoing under moonlight spilling through glass."
        rub "Oh god! I-I can’t take anymore! I’m cumming hard!" 
        "She cried out, her body tensing as her inner muscles clenched around my shaft. Her moans and gasps spurred me on, her plea to fill her driving me to the brink."
        rub "Aaahhhh… Cum inside me, baby!"
        "The intensity of her climax combined with her tight grip sent me over the edge."
        play sound2 cum
        if gent1 == "pussy":
            show rub2b v2 cum with c
        else:
            show rub2b a2 cum with c
        play sound2 cum
        with c
        "With a primal groan, I unloaded into her [gent1], our bodies quivering in sync with the aftershocks of our passionate encounter."
        play sound2 cum
        with c
        play sound2 cum
        with c
        "I held myself inside of her, savoring the feeling as my orgasm gradually started to subside."
        show rub2b -v1 -v2 -a1 -a2 e3 
        call stopbgs from _call_stopbgs_22
        call camerabreath from _call_camerabreath_28
        with d
        "When I finally pulled out of her [gent1], I couldn’t help but admire my work as a thick trail of cum spilled out of her."
        play sound2 spank
        if gen1 == 1:
            "I leaned back so I could get a better look at my handiwork. Pulling back one of the bands of her garterbelt, I let it snap back with a satisfying slap."
        else:
            "I leaned back so I could get a better look at my handiwork, gracing her with one final slap on her plump ass cheek."
        "[rub] gives me one last wink, a satisfied smile playing on her lips."
        rub "Thank you, darling… That was exactly the type of break I needed…"
        $ energy -= 1
        return

    label melfootjob:
        show mel smug with d
        mel "I knew you were into that shit! C'mon, let's sneak into a booth."
        play music melodysextheme
        scene mel1a e1 
        $ textbox = 2
        play moans1 moansmisc2
        call camerabreath from _call_camerabreath_3
        with d
        mel "You're such a freak getting turned on by my feet!"
        mc "Don't discredit yourself like that, the view of your body is amazing too." 
        mel "Heh, isn't it just? Maybe these tiny tits aren't so bad after all."
        mel "Want me to wear something? Might make it feel better."
        $ gen1 = 0
        menu melfootjobmenu:
            "Pantyhose (Needs Purchasing)" if pantyhose == 0:
                jump melfootjobmenu
            "Pantyhose" if gen1 == 0 and pantyhose == 1:
                $ gen1 = 1
                show mel1a p1 with d
                jump melfootjobmenu
            "Ripped Pantyhose" if gen1 == 1 and pantyhose == 1:
                $ gen1 = 2
                show mel1a p2 with d
                jump melfootjobmenu
            "Remove Pantyhose" if gen1 == 2 and pantyhose == 1:
                $ gen1 = 0
                show mel1a -p2 with d
                jump melfootjobmenu
            "(Continue)":
                pass
        "In addition to wrapping her toes around my shaft and tip, she wastes no time beginning to rub her gorgeous, dripping wet pussy. Her vulva was stunning, and I could feel my cock throbbing and dripping precum at the sight alone." 
        show mel1a e2 with d
        mel "Staring at my pussy, are you? Tsk, I don't think so."
        play ambience1 handjob fadein 2
        "With a little more confidence in her toes, she starts to thrust them up and down my shaft."
        play moans2 moansmisc4 volume 0.5
        "In the booth beside us, passionate moans begin to ramp up. Likely from the couple that just walked past us. [mel] casts an annoyed glance, but grins as soon as she realizes she can use this as material to tease me with."
        show mel1a e1 with d
        mel "Right on que. There's no shortage of slutty mares here that can’t resist their baser instincts and impulses. But don’t think for a second that I’ll be fucking you in here. You’re barely good enough for my feet."
        "My cock twitched as her delicate feet massaged my member. I’m surprised she’s able to achieve such precision with them."
        "My eyes closed tightly as I leaned back and savored every sensation. Watching my enjoyment, [mel] sped up too, her fingers moving rapidly against her clit as her toes gripped around my shaft and started to jack me off."
        show mel1a e2 with d
        mel "Tsk, pahaha, there’s no way this feels good, right?"
        "My member twitched a few times against her tender touch, leaking precum onto her delicate toes—a testament to the fact that, yes, it does feel pretty good, actually."
        mc "Nngghh, [mel], you’re killing me with this. It feels good, but… never quite enough."
        show mel1a e1 with d
        mel "Mmm… Good, I like it that way~"
        show mel1a e2 with d
        "I opened my eyes slightly to watch her work, taking in the sight of her tail swishing back and forth playfully behind her. Gods above, she’s something entirely else."
        "Her voice had taken on a huskier, lustful tone since we’d begun, although now it was getting mixed up in moans of her own enjoyment."
        "The sounds of moans and grunts from the adjacent booth echoed through the thin walls, adding an extra layer of filthy excitement to this illicit encounter. Actually, it wasn’t just moans anymore, but the sound of flesh slapping against flesh—a stallion’s grunts muffled by a mare’s moans."
        mel "I bet you’re imagining us in that situation, aren’t you? Pfft, could you even imagine that? Riding that gross, fat, thick… thing? Ooohhh… No way~"
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
        call stopbgs from _call_stopbgs_1
        call camerareset2 from _call_camerareset2_2
        with d
        "Finally, as the tremors subsided, I opened my eyes to discover [mel] pouting in front of me, a mixture of annoyance and mischief dancing behind those captivating eyes." 
        mel "Ugh, you covered us both in cum again! At least there are tissues in here this time."
        $ energy -= 1
        return
    label melblowjob:
        show mel bashful with d
        mel "Tsk, tsk..."
        mel "Fine."
        show mel1b e1
        $ textbox = 2
        call camerabreath from _call_camerabreath_4
        play moans1 moansmisc2
        play ambience1 blowjob
        with d
        mel "Mmphhh... How are you so freakin' big?"
        mel "I mean sure, I know stallions have big cocks too, but it's the girth that matters the most."
        mel "Anyway, want me to wear anything cute?"
        $ gen1 = 0
        $ gen2 = 0
        $ gen3 = 0
        menu melblowjobmenu:
            "Underwear (Needs Purchasing)" if lingerie == 0:
                jump melblowjobmenu
            "Pantyhose (Needs Purchasing)" if pantyhose == 0:
                jump melblowjobmenu
            "Stockings (Needs Purchasing)" if lingerie == 0:
                jump melblowjobmenu
            "Underwear" if lingerie == 1:
                if gen1 == 0:
                    $ gen1 = 1
                    show mel1b underwear with d
                else:
                    $ gen1 = 0
                    show mel1b -underwear with d
                jump melblowjobmenu
            "Pantyhose" if pantyhose == 1:
                if gen2 == 0:
                    $ gen2 = 1
                    $ gen3 = 0
                    show mel1b fishnets -lingerie with d
                else:
                    $ gen2 = 0
                    show mel1b -fishnets with d
                jump melblowjobmenu
            "Stockings" if lingerie == 1:
                if gen3 == 0:
                    $ gen3 = 1
                    $ gen2 = 0
                    show mel1b lingerie -fishnets with d
                else:
                    $ gen3 = 0
                    show mel1b -lingerie with d
                jump melblowjobmenu
            "(Continue)":
                pass
        "Like a shark, [mel] circles my cock and beckons for blood. Her eyes locked onto mine as she took my throbbing cock by one hand and directed it towards her lips."
        "Slowly, teasingly, [mel] lowered her mouth onto my cock until the tip disappeared."
        "While this was only one of her first ever blowjobs, there was nothing sweet and innocent about this truly sinful mare."
        mel "Mmprehhh… {i}Slurp, lick{/i} Okay, this thing is stupidly big. I doubt I could even fit it in my mouth, let alone my precious holes."
        mc "I think you’d be surprised. Those holes can sure take a beating."
        show mel1b e2
        mel "Pfft, the less I know about your alternative universe fan fiction the better."
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
        call camerareset2 from _call_camerareset2_3
        call stopbgs from _call_stopbgs_2
        $ textbox = 1
        with d
        mel "Bleh, I need a drink to wash this down."
        mc "That was good—"
        show mel smug with d
        mel "Good? What was good? We didn’t do anything in here, got it?"
        mc "Of course, [mel]."
        $ mel1 = 1
        "My erection had finally shrunk to a socially acceptable level, allowing us to leave the booth."
        $ energy -= 1
        return

#Farm
label farmsexscenes:
    label honthighjob:
        hon "Oh? That's what you want~?"
        layeredimage honeycrisp1b:
            always:
                "honeycrisp1bb [honb]"
            group eyes:
                attribute e1:
                    "honeycrisp1be 1"
                attribute e2:
                    "honeycrisp1be 2"
                attribute e3:
                    "honeycrisp1be 3"
            group cum:
                attribute cum:
                    "honeycrisp1bcum"
            group thighjob:
                attribute tj1:
                    "honeycrisp1bthighjob 1"
                attribute tj2:
                    "honeycrisp1bthighjob 2"
        show honeycrisp1b e1 with d
        hon "How's this, hun?"
        "I couldn't resist any longer. I reached out and caressed [hon]'s ass cheek, my fingers sinking softly into her fur, eliciting a soft moan from her lips."
        "In response, [hon] turned her head slightly, our faces now inches apart. Her eyes locked with mine, brimming with desire and anticipation. She parted her lips slowly, invitingly."
        "Without a second thought, our lips met in an intense kiss, our tongues dancing passionately."
        "Breathless but craving more, we broke apart briefly. I couldn’t look away from her flushed face. She looked utterly irresistible."
        hon "I can feel you growing down there… It's just as nice and big as I’d hoped~"
        "With her sitting on me, my growing erection had little space, pressing against her butt with increasing pressure. Each time she squirmed or adjusted herself, I could feel her wet folds brushing against my tip."
        mc "You’re driving me crazy!"
        hon "That’s the idea, sugar. Just sit back and enjoy what comes next~"
        show honeycrisp1b tj1 with d
        "Her whispers were husky with desire. With one swift motion, she adjusted her position, freeing my throbbing cock from its confines and nestling it between her thighs."
        "But not just between her thighs; she pressed it firmly against the full length of her pussy lips."
        play moans1 moansmisc3
        play ambience2 handjob2 fadein 3
        camera:
            linear 0.2 zpos -15
            linear 0.6 ypos -7
            linear 0.2
            linear 0.3 ypos 7
            repeat
        show honeycrisp1b e2 with vpunch
        "[hon] moved like an expert, rolling her hips up and down, massaging my twitching cock between her thighs and wet entrance."
        mc "Aahhh, you’re really skilled at this!"
        show honeycrisp1b e1 with d
        hon "Like I said, babe, it’s all in the hips~"
        show honeycrisp1b e2 with d
        "Pleasure surged through me as I joined in, rocking my hips in sync with hers. Soon, our movements harmonized into a seamless rhythm, our moans and gasps blending into a primal symphony of desire."
        "I could sense her pleasure intensifying as she adjusted her grinding to focus on her clit. Her ragged breaths transformed into needy moans." 
        show honeycrisp1b e1 with d
        hon "Ooohhh, that’s feels great against my clit! {i}Pant, pant{/i} Does this feel good for you?"
        mc "Nnhhg yeah, it feels incredible!"
        show honeycrisp1b e2 with d
        "Our bodies intertwined tightly, sweat glistening on our bodies as we moved faster and harder together. I couldn’t gauge if she was nearing climax, but my own orgasm was on the brink of release."
        show honeycrisp1b e1 with d
        hon "I can feel you stiffening up; are you close?"
        mc "Yeah! I’m getting really close!"
        show honeycrisp1b e2 with d
        "Upon hearing this, she picked up the pace, moving so swiftly I struggled to keep up. It was a stark reminder of the strength and agility of these creatures." 
        "I surrendered to her movements, helpless as she effortlessly milked me with just her thighs."
        hon "Mmhh, cum for me, stud!"
        mc "Fuck, yes! Cumming now!"
        play sound2 cum
        show honeycrisp1b e3 tj2 cum with c
        play sound2 cum
        with c
        "With a final thrust upward, my hot cum erupted from my tip, showering her body." 
        play sound2 cum
        with c
        play sound2 cum
        with c
        hon "Aahhh! So much! Mmmhh... good boy~"
        show honeycrisp1b -tj2 
        call camerabreath from _call_camerabreath_17
        call stopbgs from _call_stopbgs_14
        stop music fadeout 10
        play ambience1 night fadein 10
        with d
        "The orgasm seemed to last an eternity, leaving me breathless and spent." 
        "She remained seated on me, our hearts pounded in unison."
        "[hon] leaned in closer, giving me a side hug before reaching for a tissue to pat herself dry."
        mc "I always thought not having wings or a horn would be a bad deal, but you gals seem make up for it in raw strength."
        hon "Heh, that's right. They call us 'earth' ponies, because our strongest can crack the earth!"
        play sound2 equip
        scene bg farm2
        call camerareset1 from _call_camerareset1_4
        $ textbox = 1
        show hon wink with d
        hon "That was good! Let's see if we can't do something even more intense next time."
        $ energy -= 1
        return
    label blobuttjob:
        blo "Would it be alright if we snuck over to the barn to do that? [hon] might hear me moaning otherwise."
        layeredimage blossom1b:
            always:
                "blossom1bb [blob]"
            group spanked:
                attribute spanked:
                    "blossom1bspanked"
            group cum:
                attribute cum:
                    "blossom1bcum"
            group buttjob:
                attribute b1:
                    "blossom1bbuttjob1"
            group buttjob2:
                attribute b2:
                    "blossom1bbuttjob2"
            group hand:
                attribute hand:
                    "blossom1bhand"
        play music sextheme
        play moans1 moansmisc2
        stop ambience1 fadeout 3
        show blossom1b 
        call camerabreath from _call_camerabreath_18
        $ textbox = 2
        with d
        "I couldn't tear my eyes away from [blo], who had bent over a nearby crate with her perfect ass on display."
        mc "God, you’re so hot…"
        blo "Mmmhh… I am? T-Thank you... I think you're really hot too."
        "Her legs were  scrunched in such a position to give me an unobstructed view of her pink anus and soaked pussy. The sight alone was enough to make my cock twitch in anticipation."
        mc "Can I touch it?"
        blo "P-Please do…"
        show blossom1b hand with d
        "I spread apart [blo]'s left cheek, exposing her glistening slit further. A moan escaped her lips as my fingers brushed against her sensitive entrance, causing more of her juices to ooze out onto the barn floor."
        "I couldn't resist taking another moment to admire [blo]'s tight pucker too; both it and her pussy were practically begging for my cock's attention. Despite being a virgin, she exuded an irresistible allure that made me question my own self-control."
        mc "Mmhh... I'm so tempted to just slide it inside..."
        blo "{i}Gasp...{/i} [mc]..."
        "I saw her eyes widen when they flicked downwards towards my growing erection. A soft gasp escaped her lips before she quickly looked away again. She squirmed slightly in her place, her hips starting to instinctively grind."
        blo "I can't believe how thick it is..."
        show blossom1b -hand b1 with d
        "Withdrawing my hand, I replaced it with my throbbing member, pressing firmly against her ass cheeks. The temptation to claim her tight hole was almost unbearable. She is definitely wet enough for it..."
        blo "Mmmhhh... That feels so good..."
        "Instead, I began rubbing myself against her sensitive entrance, grinding my throbbing member against her dripping wet folds."
        "The heat from her petite body ignited a burning desire within me, and I began to furiously pleasure myself, my tip pressing and gliding against her entrance."
        mc "Nnggh, you’re so wet. It feels like if I press any harder, I’d slip right inside!"
        blo "Uoohhh… You're so naughty!"
        "The contact sent waves of pure ecstasy coursing through me. Each movement against her was a delight I savored deeply."
        "Her tail began a seductive dance, occasionally brushing against my chest or shaft, adding to the intensity of the moment. Her entire body was trembling with pleasure."
        menu:
            "{i}Spank Her!{/i}":
                play sound2 spank
                show blossom1b spanked with d
                "Unable to resist, I lifted my hand and brought it down on her firm ass, eliciting a yelp that was a blend of pain and pleasure."
                blo "Oooohhhhh, that was… good…"
                mc "Want me to do it again?"
                blo "Y-Yeah…"
                play sound2 spank
                "I spanked her again, this time on the other cheek. Her moan was filled with pleasure, and her hips squirmed with desperate need."
                mc "You like that, don't you?"
                blo "Yes... more, please..."
                play sound2 spank
                "I continued to alternate between her cheeks, each spank drawing louder moans and more intense reactions."
            "{i}Have Mercy{/i}":
                pass
        mc "You feel too damn good... I can't hold on much longer!"
        "She let out a soft moan of pleasure, her body arching back into me instinctively. With each thrust, I could feel my tip almost sliding in. That brief, tantalizing touch of her warmth was enough to send me over the edge."
        play sound2 cum
        show blossom1b b2 with c
        play sound2 cum
        with c
        "My voice strained with desire as overwhelming pleasure consumed me. I let out an earth-shattering groan as hot, thick cum spurted from the head of my cock."
        play sound2 cum
        show blossom1b cum with c
        play sound2 cum
        with c
        "Hot streams of cum painted her backside white, some of it dripping down over her anus and pussy."
        show blossom1b -b1 -b2 cum with d
        "My orgasm raged on for almost thirty seconds before finally subsiding. Panting heavily, I pulled away from her cum-soaked flank, feeling utterly spent."
        mc "{i}Pant, pant{/i} Incredible…"
        blo "Oooohhh... Let's hurry back."
        call camerareset2 from _call_camerareset2_15
        call stopbgs from _call_stopbgs_15
        play ambience1 night fadein 10
        $ textbox = 1
        $ energy -= 1
        return
#REPLAYS
label replaysexscenes:
    label postreplaycleanup:
        $ textbox = 1
        $ replay = 0
        stop music fadeout 1
        call stopbgs from _call_stopbgs_3
        call camerareset2 from _call_camerareset2_4
        return
    label moxpen1:
        scene bg apartment
        show mox horny:
            xalign 0.75
        show pen horny:
            xalign 0.25
        with d
        menu:
            "{i}Lean back and enjoy the show{/i}":
                mc "Some things never change. All right girls, show me what you’ve got." 
            "This is very sudden!":
                show pen laughing with d
                pen "Not sudden for us! We’ve been planning this for six days."
                show mox happy with d
                mox "[mc] does have a point. It's different from using a familiar. It feels more personal and intimate, and since this is one of my first times, it carries weight."
                mc "Exactly!"
                show pen wink with d
                pen "Hm… Well, it’s up to you, [mc]. Want us to blow your mind?"
                menu:
                    "Blow my mind, girls.":
                        show pen happy with d
                        pen "Don’t mind if I do~"
                    "I have too much on my mind right now.":
                        show pen neutral with d
                        pen "Hm… given the circumstances, that’s fair enough…"
                        show pen wink with d
                        pen "Let’s give this another shot later, lover boy."
                        show mox laughing with d
                        mox "Yeah! – Uh, I mean, r-right…"
                        "These two seem pent up!" 
                        return
        "I’d barely noticed it, but the two girls had slowly been edging closer to me throughout the entire conversation. Of course, they were both nude, but I was so occupied with my thoughts that I somehow missed their clear arousal and interest."
        "Right now, they were pincering me from either side."
        show mox horny with d
        mox "He looks so exotic, doesn’t he?"
        pen "This scar gives him a lot of character!"
        mox "Oh look! It's getting even bigger!"
        mc "You two were waiting for this the whole time, weren’t you!"
        pen "Ehehe, you got us. When we’re in heat and around a hunk, there's only one thing on our minds…"
        show mox:
            linear 0.3 ypos 200
        show pen:
            linear 0.3 ypos 200
        "The girls kneeled on each side of my growing erection, their breathing ragged with animalistic lust."
        show mox surprised with d
        mox "Getting bigger, bigger… Oh my goodness…! Sir, that is fucking massive!"
        show pen surprised with d
        pen "Oh god, it’s not just the length, it’s the girth… it looks so fucking good."
        play music sextheme volume 0.6 fadein 2
        play ambience1 rain volume 0.1 fadein 2
        show moxpen1a 1
        call camerareset2 from _call_camerareset2_5
        $ textbox = 2
        play ambience2 blowjob
        play moans1 moansmisc2
        with d
        call camerabreath from _call_camerabreath_5
        "The girls couldn’t hold back anymore; they finally moved in for their attack. I was fully erect and ready to go, my hard cock standing tall at eight inches of pure, veiny manhood, dripping with precum."
        camera:
            linear 2 xpos -100 zpos -200
        "With a wicked grin, [pen] moved in first, her eyes never leaving my cock as her long equine tongue immediately started lapping upwards from the base."
        "She was aggressive and dominant, her tongue darting around my throbbing member and lavishly coating it in a slick layer of saliva."
        pen "Mmmm… {i}Slurp{/i} This is way better than a familiar."
        camera:
            linear 2 xpos 190 ypos 105 zpos -250
        "[mox] was a little more hesitant, but quickly got over it to start focusing on my ball. Her warm breath sent shivers down my spine as she licked them softly with the tip of her tongue before engulfing them completely into her mouth."
        "Before long, she was happily suckling and swirling her tongue around below [pen]."
        show moxpen1a 2
        camera:
            linear 2 xpos 0 ypos 0 zpos -16
            block:
                linear 1.8 ypos 6
                linear 0.4 ypos 6
                linear 0.8 ypos -2
                linear 0.2 ypos -2
                repeat
        with d
        mc "Hooohhh, you two were eager, weren’t you?"
        pen "Ehehe, are you kidding? I was horny before I even left my house! {i}Lick, lick{/i}"
        mox "Mmpghhhh… {i}Suckle, slurp{/i} And I abstained from masturbating all day today! Nnghhh… It’s been so hard to concentrate."
        "[pen]’s tongue continued to flick upwards, gaining more ground with each lap. The combination of her tongue combined with [mox]’s luscious lips wrapped around my balls left my cock constantly throbbing."
        "Together they worked in harmony, with [mox] sucking my balls as if they were a precious treasure, while [pen] bobbed her head up and my own shaft." 
        "The contrast of their mouths was exquisite; where [pen] was firm and commanding, [mox] was delicate and gentle."
        mc "Nngghh, if you keep going like this, I won’t be able to hold back long at all!"
        mox "Fuhuhu, then don’t~ You know what we want."
        "Soon enough, [mox] parted from my balls with a new goal in mind. She trailed her tongue up the entire length of my shaft until…"
        show black:
            ypos 100
        show moxpen1b 1
        camera:
            ypos 250 zpos -500
            linear 8 ypos -150
            linear 8 ypos 0 zpos -16
            block:
                linear 1.8 ypos 6
                linear 0.4 ypos 6
                linear 0.8 ypos -2
                linear 0.2 ypos -2
                repeat
        with d
        "[mox] finally claimed my tip. Her warm lips wrapped around the most sensitive part, constantly squeezing and sucking, while her tongue swirled around the crown."
        pen "Found your confidence, [mox]?"
        mox "Mmghhh… {i}Slurp{/i} Yesh, I think so! Turns out being horny as hell is great at alleviating nerves."
        "[mox] moaned with delight as she started to bop up and down around my sensitive tip. Meanwhile, [pen] continued to diligently serve my shaft, almost becoming hypnotically absorbed into her work."
        "Their equine tongues were considerably larger than any humans, with a slightly rougher texture that combined a wider surface area with a constantly higher stimulation. I’d almost say it felt twice as good, and I was dealing with two girls at once!" 
        pen "God, the smell is intoxicating."
        "Subtly under the sounds of their tongues were the wet sounds of masturbating, as both girls began to pleasure themselves. [pen] sank two fingers deep into her pussy and curled it upwards to tease at her g-spot, while [mox] rubbed her needy clit back and forth."
        mox "I really want you to cum for me, [mc]… Coat the roof of my mouth with your seed~"
        mc "Nngghh, fuck… If you keep talking like that…"
        "I whispered as they increased their pace. Their eyes locked on mine as they milked my cock with their mouths. I could see the hunger in their eyes, as they wanted nothing more than for me to explode into their waiting maws."
        pen "Cum for us, [mc]… Cum~"
        play sound2 cum
        show moxpen1b 2 cum 
        with c
        play sound2 cum
        with c
        "Finally, I couldn't hold back any longer as my body convulsed with pleasure. My seed erupted from my cock, filling [mox]’s mouth as they greedily swallowed every drop."
        play sound2 cum
        with c
        play sound2 cum
        with c
        "Although my load was too much for her, thick ropes of cum dripped down my cock to be met by [pen]’s hungry tongue below."
        play sound2 cum
        scene moxpen1a 1 cum1
        with c
        play sound2 cum
        with c
        "Almost too much for her to handle, [mox] retreated back to the base of my cock as my last few sprays of cum dosed their snouts."
        show moxpen1a 1 cum2
        with c
        play sound2 cum
        with c
        "They continued their ministrations even as I came down from the high, their tongues licking my cock clean as they shared my essence between them with eager kisses."
        stop music fadeout 10
        call stopbgs from _call_stopbgs_4
        mox "Aahh… {i}Pant, pant{/i} I’ve never actually done that before, was I any good?"
        mc "You were perfect, [mox]."
        pen "Took the words right out of my mouth, [mc]."
        $ replay = 0
        return
    label moxpen2:
        scene black with d
        call camerareset2 from _call_camerareset2_6
        show bg bedroom2 with d
        "Sixty seconds later, I was laying in the center of the bed, my cock twitching eagerly as I gazed up upon two of the most captivating mares in Arcadia."
        show mox horny with d
        "[mox] stood tall over me, her luscious ass perched temptingly close to my hungry mouth."
        mox "Is this seat free?"
        mc "All yours, cutie."
        play music sextheme fadein 3
        play moans1 moansmisc2 fadein 3
        $ textbox = 4
        play ambience1 blowjob
        show moxpen2a 1
        call camerabreath from _call_camerabreath_6
        with d
        "Her body glistened, accentuating every curve and muscle as she lowered herself onto my face."
        "Straddling my face, her plump ass rested firmly on my nose and lips, blinding me, preventing me from speaking, and completely arousing me."
        mox "Oooo, now that got you going! Your cock looks absolutely delicious."
        "Her voice was like honey, fuelling my raging erection and causing precum to start oozing at the tip." 
        "I stuck my tongue out and wriggled around blindly for a while. Every touch felt good for her, but once I found her swollen clit the pleasure elevated to an entirely new level."
        "Her hips start rocking, her thighs trembling as she both sought my pleasure while struggling to handle it all coursing throughout her."
        show moxpen2a 2
        mox "Ohhh! Now you’ve got me going!"
        pen "Hehe, you two are having fun, aren’t you?"
        "I felt a kiss against the tip of my cock, [pen]’s warm breath tickling my shaft."
        scene moxpen2b e1 sex1 with dissolve
        pen "Time for the main course."
        "I could just barely peep from between [mox]’s thighs to witness [pen] shuffling into position on my other half."
        pen "You ready?"
        mc "Mmphh, mhh... {i}Lick, slurp{/i}"
        mox "I think that was a yes~"
        play sound2 cum
        scene moxpen2b e2 sex2 with dissolve
        play moans2 moansmisc3
        with hpunch
        "Slowly, she lowered herself onto my throbbing cock, moaning deeply as she sank down onto my member, inch by delicious inch."
        "Her tight, wet pussy clenched around me like a vice, milking moans of pleasure from deep within me."
        "She was so fucking tight, so damn good. It felt like she was made for just this moment."
        camera:
            zpos -18
            block:
                linear 0.3 ypos -8 
                linear 0.1
                linear 0.2 ypos 8
                linear 0.1 
                repeat
        show moxpen2b action with dissolve
        with d
        play ambience2 sex
        pen "Nnngghhh, so fucking good! Your cock is spreading me out perfectly! Aaahhh!"
        "Meanwhile, [mox] continued to mercilessly ride my face, grinding her pussy down against my mouth, reminding me to continue licking."
        "Her juices dripped down from her dripping wet cunt, painting hot, sticky trails across my cheeks."
        mox "Keep licking right there! Uooohhh, you’re so good with your tongue!"
        pen "Ehehe, seems our friend here already knows our weak spots." 
        "She wasn’t kidding; I knew exactly how to turn [mox] into a quivering mess with my tongue alone."
        "And I rocked my hips in perfect rhythm to grind my cock against the sensitive depths of [pen]’s pussy."
        scene moxpen2c m1 p1
        call camerabreath from _call_camerabreath_7
        with dissolve
        "With each thrust of the hips, each grunt of pleasure, and each moan of ecstasy that escaped these two marvellous mares, I felt myself spiralling deeper into instinctual, primal lust."
        "As wave after wave of pleasure hit the three of us, I could tell that we were all getting closer to cumming. Our movements became more needy, desperate, and chaotic, quelled only slightly by the passionate kiss shared between the mares."
        show moxpen2c m2 
        mox "Aahhh! I’m getting really close!"
        show moxpen2c p2
        with d
        pen "Mmm, me too! I can’t wait for you to fill me up, [mc]~"
        camera:
            zpos -18
            block:
                linear 0.3 ypos -4 
                linear 0.1
                linear 0.2 ypos 4
                linear 0.1 
                repeat
        "I held [mox] tightly in place, flickering my tongue against her clit to drive her over the edge – while [pen] continued to slam against me, grinding and pounding her hips into mine as hard and as fast as she could."
        "In a glorious crescendo, both girls were pushed over the edge simultaneously. [mox]’s thighs tightening and quivering around my head while [pen]’s pussy squeezed and spasmed around my shaft."
        "With one swift, forceful thrust, [pen] buried herself completely onto my throbbing member, her tight pussy squeezing out one final, earth-shattering moan from deep within her. It was this thrust that pushed me over the edge–" 
        mc "I’m cumming!"
        play sound2 cum
        show moxpen2c cum
        show internalcreampie
        with c
        "—I exploded, unloading crazy amounts of hot, thick cum deep inside her, filling her up to overflowing."
        play sound2 cum
        with c
        play sound2 cum
        with c
        "[pen] threw her head back, her orgasm brought to new heights as she’s filled up."
        play sound2 cum
        with c
        play sound2 cum
        with c
        "[mox] watches longingly as cum bubbles and seeps around [pen]’s pussy, our mixed juices splattering onto the bed sheets in a sticky mess."
        scene moxpen2b e3 sex4
        call camerabreath from _call_camerabreath_8
        call stopbgs from _call_stopbgs_5
        stop music fadeout 3
        with dissolve
        "[pen] continued to ride long after our orgasms faded, only stopping once we’d both grown sensitive, her body lightly spasming with the aftershocks of her orgasmic release." 
        "Breathing heavily, sweat dripping down from their flushed, sex-crazed faces, they look down at me, eyes filled with satisfaction and admiration."
        pen "That was… {i}Pant, pant{/i} an utterly transcendent experience…"
        mox "Ahaha, so dramatic… It was equivalently good, though."
        mox "That’s the kind of earth-shattering orgasm that makes you rethink your life."
        pen "Exactly! It makes you reevaluate what really matters to you."
        mc "… Are you two just going to have this conversation while still sitting on my face and dick?"
        mox "What can I say? They’re the best seats in the house. No offense, [pen]."
        pen "She’s right, no offense taken."
        pen "[mox], did you want to...?"
        mox "Ahh, uhm... N-No! It's fine!"
        pen "Your loss~"
        $ replay = 0
        return