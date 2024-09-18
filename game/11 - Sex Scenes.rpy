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
            group pregnant:
                attribute pregnant:
                    "moxpen2apregnant"
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
        call genreset from _call_genreset_1
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
            "Pregnant (Needs Milky Potion)" if pregpotion == 0:
                jump moxfacesittingmenu
            "Pregnant" if pregpotion == 1:
                if gen5 == 0:
                    $ gen5 = 1
                    $ gent2 = "pregnant"
                    show moxpen2a pregnant with d
                    "[mox] drinks the potion and the effects are immediate. Her belly expands, and her nipples spurt with excess milk."
                    mox "Mmmhh, you better take good care of me now I'm knocked up, hehe~"
                else:
                    $ gen5 = 0
                    $ gent2 = ""
                    mox "Hm, let me see if I know the reversal spell."
                    show moxpen2a -pregnant
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
        "A satisfied smirk curved [mox]'s lips. Slowly but deliberately, she lowered herself onto my face, her wet folds immediately met by my eager tongue."
        "Her [gent2] body quivered with pleasure as my tongue darted in search of her clit - a quest met with success when I found it and focused all my attention on it. [mox] was overwhelming with an onslaught of pleasure, many moans slipping past her parted lips."
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
            group pregnant:
                attribute pregnant:
                    "moxie1apregnant [moxb]"
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
        call genreset from _call_genreset_2
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
            "Pregnant (Needs Milky Potion)" if pregpotion == 0:
                jump moxmissionarymenu
            "Pregnant" if pregpotion == 1:
                if gen4 == 0:
                    $ gen4 = 1
                    $ gent2 = "pregnant"
                    show moxie1a pregnant with d
                    "[mox] drinks the potion and the effects are immediate. Her belly expands, and her nipples spurt with excess milk."
                    mox "Woah, that was fast! Nngghh, and I feel warm inside too!"
                else:
                    $ gen4 = 0
                    $ gent2 = ""
                    mox "Hm, let me see if I know the reversal spell."
                    show moxie1a -pregnant
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
        mox "I'm absolutely drenched down there... As ready as I could possibly be."
        mox "You know, you were right — we are going to check off every box on our naughty list, aren't we?"
        mox "So, my stud... Are you ready to give me everything I want? Are you prepared to take me here, now, like two animals driven wild by desire?"
        "Her hips shifted restlessly against mine, seeking friction, pleading for release."
        mc "I'm going to pound you so hard, babe~"
        "[mox] eagerly spread her legs apart, anchoring them securely into position with a tight grip. She arched her hips upward, presenting herself as an irresistible temptation to be devoured by my eyes."
        if gen3 != 3:
            "My cock was no longer pressed between her thighs, but now hovering over her [gent1], the tip occasionally brushing against them."
            "With each passing heartbeat, my tip delved in just a little deeper."
        else:
            "Me and my familiar's cocks were now hovering over her pussy and ass, the tips occasionally brushing against them."
            "With each passing heartbeat, our tips pushed in just a little deeper."
        if gen1 == 1:
            play sound2 rip
            show moxie1a bunny2 with d
            "I tore a hole in her tights without a care in the world. This only turned her on more."
        "Never before had I experienced anything remotely comparable to the overwhelming craving that consumed me at that moment. It wasn't merely lust that coursed through my veins; no, there was an underlying depth to this hunger that left me quivering with anticipation."
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
        "Her [gent] squeezed and spasmed as precum oozed deep inside. I grabbed hold of her hips tightly, using them as leverage to drive myself deeper into her [gent2] body." 
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
            "[mox] whimpered out between moans, her [gent2] body growing tense in anticipation of her climax. She arched her ass upwards, pushing herself harder against my cock, begging for more of that incredible sensation."
        else:
            "[mox] whimpered out between moans, her [gent2] body growing tense in anticipation of her climax. She arched her spasming body towards us, begging for more of that incredible sensation."
        if gen3 != 3:
            "I could feel myself teetering on the edge as well. The tightness of her [gent] around me was almost too much to bear."
        else:
            "I could feel myself teetering on the edge as well, and my familiar seemed to be just as close. The tightness of her pussy and ass were just too much to bear."
        mox "Aahhh, I-I’m almost…!"
        "I reached down between us, finding her sensitive clit with one of my hands. I began to rub it rhythmically as I continued to thrust into her tight hole. This was the final straw for both of us — we both exploded together."
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
            "She was in luck as she got doubled snuggles from me and my familiar while we enjoyed the afterglow of our orgasms."
        scene bg moxiebedroom2 
        show mox laughing cum with d
        "Afterwards she bounced up with more energy than ever."
        mox "Heck yeah! I feel much better now!"
        if gen3 == 3:
            "A few minutes later, our quiet familiar friend disappears."
        elif gen4 == 1:
            show mox surprised blush milk with d
            "Her body had returned to normal, but there was still a bit of milk leakage."
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
                    $ gen2 = 0
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
                    $ gen3 = 0
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
        "I released another thick load deep inside of her, painting her insides white with my seed. Throughout both our orgasms, I don’t stop for a second, making sure to squeeze every drop of pleasure from the both of us."
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
    label lilysexscenes:
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
                always:
                    "lily1asfx"
                group action:
                    attribute hands:
                        "lily1ahands"
                    attribute buttjob1:
                        "lily1abuttjob 1"
                    attribute buttjob2:
                        "lily1abuttjob 2"
                    attribute sex1:
                        "lily1asex 1"
                    attribute sex2:
                        "lily1asex 2"
            lil "What's that? You just want me to bend over, like this?"
            play music sextheme
            show lily1a 1 night
            $ textbox = 4
            call camerabreath from _call_camerabreath_10
            play moans1 moansmisc2 volume 0.6
            with d
            "My gaze followed her retreating form with mild curiosity as she wandered over to an adjacent desk, swaying seductively as she went (as seductive as [lil] can muster anyway)."
            "As she assumed the position, her tail swayed provocatively from side to side, affording me an irresistible glimpse of her enticing derriere. "
            "Noticing [lil]'s obvious attempt at subtlety—or perhaps, an endearing lack thereof—a playful smirk tugged at the corners of my lips. The way the soft light cascading through the window fell upon her dripping wet pussy, accentuating every inviting fold and crevice, painting them with an ethereal glow, left me positively spellbound."
            "Unable to tear my gaze away from this view, my eyes devoured every sway of [lil]'s voluptuous behind as she leaned further forward, her tight ass cheeks clenching invitingly. In that moment, her ass seemed to exude an almost palpable allure, practically daring me to succumb to the overwhelming urge to touch, caress, and claim every inch as my own."
            play sound1 move
            "Taking tentative steps forward, I observed her reaction closely. She pretended to be engrossed in her notebook once again, feigning indifference to my presence."
            menu lilbuttjobm:
                "Buttjob":
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
                "Insert It ([lil] isn't ready yet)" if magicroute2 == 0:
                    show lily1a hands with d
                    jump lilbuttjobm
                "Insert It" if magicroute2 == 1:
                    "As I take out my cock, she turns to the desk and ignores it."
                    "Despite that, she gasped as I pressed the tip of my cock against her folds. As usual, she's so wet that only a small amount of pressure would suck me right in."
                    lil "Mmhh, just hurry up~ I have a lot of reading to do."
                    play sound2 cum
                    show lily1a sex1 2 with d
                    "Oh? What's this routine she's playing? Regardless, the heat of her desire is evident as I entered her slowly."
                    play moans1 moansmisc4
                    play ambience1 sex
                    "She let out a shaky breath, her hands gripping the edge of the desk for support. I moved deliberately, each thrust measured and deep, eliciting soft moans that she tried to stifle. Her attempts to remain composed and indifferent only made the moment more intense."
                    show lily1a 1 with d
                    lil "Oh... you... you don't have to be so... gentle."
                    "Her voice was strained, the pretense of boredom slipping away as her hips began to move in rhythm with mine. I could feel her muscles tightening around me, her body responding instinctively to the pleasure building between us. I increased my pace, each thrust drawing louder and more desperate sounds from her lips."
                    mc "You like that, don't you?"
                    show lily1a 2 with d
                    "She bit her lip, a low whine escaping as she nodded. Her facade was crumbling, the scholar giving way to the passionate woman beneath. I could feel her reaching the brink, her body trembling with anticipation."
                    lil "I can't help it... I want you to pump me fill of your cum so badly..."
                    "Her voice was a breathless whisper, the book forgotten as she gave in to the pleasure. I thrust harder, feeling her tighten around me as she neared her climax. Her moans grew louder, more urgent."
                    mc "[lil], I'm getting close!"
                    lil "Oh... fuck, me too! C-Cumming!"
                    play sound2 cum
                    show lily1a cum sex2 with c
                    play sound2 cum
                    with c
                    "She arched her back, pressing against me with a fervor that matched my own. The tension between us snapped, a wave of ecstasy crashing over us as she cried out, her body convulsing with pleasure."
                    "I kept cumming more and more, the intensity of my orgasm leaving me both breathless."
                    play sound2 cum
                    with c
                    play sound2 cum
                    with c
                    "She panted, her body still trembling as she leaned against the desk, her hair disheveled and her eyes glazed with satisfaction. I held her close, feeling the warmth of her skin against mine as we both caught our breath."
                    call stopbgs from _call_stopbgs_23
                    show lily1a -sex1 -sex2 1 with d
                    "She smiled, the playful glint returning to her eyes as she looked back at me, her hands still resting on the desk for support."
                    lil "Hehe... I don't even know what book this is."
                    "We both laughed as I cleaned the cum off her butt with a tissue."
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
                "Milky (Requires Milky Potion)" if pregpotion == 0:
                    jump lildoublehandjobm
                "Milky" if pregpotion == 1:
                    if gen3 == 0:
                        $ gen3 = 1
                        show lil2a milk with d
                        "The two girls take a small sip of the potion, not enough for the more drastic effects. The results are still quite explosive as milk leaks from their nipples."
                        lil2 "Wowsers! I'm extremely turned on right now!"
                        lil "Mmm... I guess I'll admit I am too."
                    else:
                        $ gen3 = 0
                        lil2 "Awh, do we have to undo it?"
                        lil "Here's the spell."
                        show lil2a -milk with d
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
            call stopbgs from _call_stopbgs_29
            $ energy -= 1 
            return
        label lilselfcestthreesome:
            $ lil2count += 1
            $ lil2 = "{} {}.0".format(lil, lil2count)
            show lil2b e1 
            play moans2 moansmisc3
            call camerabreath from _call_camerabreath_38
            $ textbox = 2
            with d
            "After the summoning, the two [lil]s got to work quickly, tongues dancing erotically as their bodies fell onto the bed together. Didn't take long for me to summon my extra too (my penis)."
            lil2 "My, oh my... Just how will you be able to pick between the two of us?"
            lil2 "Don't worry, darling, I'll let you have first dibs. But, one more thing... How would you like us served, [mc]~?"
            call genreset from _call_genreset_3
            menu lilselfcestthreesomem:
                "Lingerie (Needs Purchasing)" if lingerie == 0:
                    jump lilselfcestthreesomem
                "Lingerie" if lingerie == 1:
                    if gen1 == 0:
                        $ gen1 = 1
                        show lil2b lingerie with d
                        lil2 "Let's fuck with style~"
                    else:
                        $ gen1 = 0
                        show lil2b -lingerie with d
                    jump lilselfcestthreesomem
                "Lactating (Needs Milky Potion)" if pregpotion == 0:
                    jump lilselfcestthreesomem
                "Lactating" if pregpotion == 1:
                    if gen2 == 0:
                        $ gen2 = 1
                        lil "M-Me? Here goes nothing! {i}Gulp{/i}"
                        show lil2b milk with d
                        "Suddenly, milk sprays freely from [lil]'s nipples, filling up her clone's hungry mouth."
                        lil2 "Mmmhhh... Look [lil], you're pregnant~"
                        lil "Nnggh, don't say that!" 
                    else:
                        $ gen2 = 0
                        lil "It's okay, I know the counterspell."
                        show lil2b -milk with d
                    jump lilselfcestthreesomem
                "(Continue)":
                    pass
            "[lil]'s legs gently opened, revealing her glorious pussy to me. Combined with her clone’s ass, which was purposely raised to show off, the sight was almost too much for my overstimulated brain to process."
            "[lil2] ended up sucking her original selves' lovely breasts, sucking and teasing her nipples. I wonder if she has a thing for that?"
            lil2 "Mmhh… Like what you see, [mc]? But I'd much rather you join us than watch."
            "I approached closer; I couldn’t help but reach out and gently squeeze [lil]’s plump ass cheeks, feeling them jiggle slightly underneath my touch. She moaned slightly but didn’t reprimand me – if anything, her body language encouraged me further."
            mc "You two look stunning together."
            "[lil]'s gaze shifted downward to watch as my big cock jerked enticingly between her legs. The thought of me entering her was exhilarating, and I could tell she wanted it too."
            show handjob at flip with d:
                xalign 0.05 yalign 0.9
            "She reached over, more confidently wrapping her slender fingers around my shaft. It throbbed responsively under her touch."
            "Encouraged by the way her clone moaned into her breast, she began to guide me towards her entrance, her hips grinding as though she were pleading for it."
            lil "Please. I need you inside me."
            play sound2 cum
            hide handjob
            show lil2b sex e2
            with d
            "With one swift motion, I positioned myself at her entrance and pushed in. Her warm, wet folds enveloped me, drawing me deeper inside her. She let out a loud moan, her body shivering with pleasure."
            "[lil2] lifted herself up from [lil]’s chest long enough to look down at us both with lust-filled eyes."
            lil2 "Ooohh, watching myself get fucked is so hot... I want you to cum inside her."
            mc "Looks like your clone also picked up the propensity for getting cucked~"
            lil "Pft, get to thrusting, you~"
            play ambience1 sex
            play moans1 moansmisc4
            camera:
                linear 0.3 zpos -14 xpos -2
                block:
                    linear 0.4 xpos 6
                    linear 0.1 xpos 6
                    linear 0.3 xpos -3
                    linear 0.1 xpos -3
                    repeat
            "She panted breathlessly before leaning down again, capturing [lil]’s nipple in a passionate kiss, while using her free hand to stimulate her own sensitive clit rhythmically."
            "I began to thrust into [lil] with a steady rhythm, her moans mixing with the wet sounds of our bodies colliding. Her clone’s tongue flicked across her nipple, heightening her pleasure."
            "[lil]'s hips rocked against mine, meeting each thrust with equal fervor. Her pussy clenched around me, driving me closer to the edge."
            mc "You're so tight... feels amazing..."
            lil "Don’t stop, please... Both of you, it feels so good!"
            "I picked up the pace, our bodies moving in perfect harmony. The sensation of her tight, wet heat around me was almost too much to bear. I could feel the pressure building, the climax approaching."
            play sound2 cum
            show lil2b sex2 cum2
            show internalcreampie
            with c
            play sound2 cum
            with c
            "[lil] threw her head back, an orgasmic moan escaping her lips as she came, her pussy contracting around my cock. The sensation pushed me over the edge, and with one final thrust, I released inside her, filling her with my seed."
            play sound2 cum
            with c
            play sound2 cum
            show lil2b e1
            hide internalcreampie
            call camerabreath from _call_camerabreath_39
            with c
            "We came hard together, our bodies entwined, panting and sated. The clone watched us with a satisfied smile, her fingers still working her own clit as she leaned in for a kiss."
            show lil2b -sex -sex2 with d
            "I pulled out slowly, our mixed fluids dripping onto the bed. As we lay there in the aftermath, I couldn't help but think about how lucky I was to have experienced such an incredible moment with two beautiful women."
            mc "Definitely. This was unforgettable."
            lil2 "And it's only the beginning..."
            show lil2c e1 cum1 with dissolve
            lil2 "Well, now... Who will be the next lucky lady? Will it be {i}me{/i} or how about {i}me{/i}?"
            lil "But first, give me a little breather!"
            call genreset from _call_genreset_4
            menu lthreesomem2:
                "Goth (Needs Purchasing)" if goth == 0:
                    jump lthreesomem2
                "Goth" if goth == 1:
                    if gen1 == 0:
                        $ gen1 = 1
                        show lil2c goth g1 with d
                        lil2 "This is more like it!"
                    else:
                        $ gen1 = 0
                        show lil2c -goth -g1 with d
                    jump lthreesomem2
                "Lingerie (Needs Purchasing)" if lingerie == 0:
                    jump lthreesomem2
                "Lingerie" if lingerie == 1:
                    if gen2 == 0:
                        $ gen2 = 1
                        show lil2c l1 with d
                        lil "I brought extra for you, [lil2]!"
                    else:
                        $ gen2 = 0
                        show lil2c -l1 with d
                    jump lthreesomem2
                "Fishnets (Needs Pantyhose)" if pantyhose == 0:
                    jump lthreesomem2
                "Fishnets" if pantyhose == 1:
                    if gen3 == 0:
                        $ gen3 = 1
                        show lil2c f1 
                        if gen4 == 1:
                            show lil2c f2
                        with d
                        lil2 "Oooo, now this is sexy!"
                    else:
                        $ gen3 = 0
                        show lil2c -f1 -f1 with d
                    jump lthreesomem2
                "Plug (Needs Purchasing)" if buttplug == 0:
                    jump lthreesomem2
                "Plug" if buttplug == 1:
                    if gen4 == 0:
                        $ gen4 = 1
                        lil2 "We've only got one? {i}Yoink{/i} I'll take that!"
                        if gen3 == 1:
                            show lil2c f2 with d
                            "[lil2] rips her fishnets open!"
                        show lil2c plug with d
                        "[lil2] pops the buttplug in with some practiced ease. No idea where she got that practice though."
                    else:
                        $ gen4 = 0
                        lil2 "Hum? Fine... {i}Pop{/i}!"
                        show lil2c -plug with d
                    jump lthreesomem2
                "(Continue)":
                    pass
            lil2 "Excellent choices! Now you have one more excellent choice to make~"
            menu:
                "Fuck [lil]":
                    $ gent1 = "{}".format(lil)
                    $ gent2 = "{}".format(lil2)
                    play sound2 cum
                    show lil2c v1b e2b
                    if gen1 == 1:
                        show lil2c g2
                    $ gen5 = 1
                    with d
                "Fuck [lil2]":
                    $ gent1 = "{}".format(lil2)
                    $ gent2 = "{}".format(lil)
                    play sound2 cum
                    show lil2c v1a e2a
                    if gen1 == 1:
                        show lil2c g2
                    $ gen5 = 2
                    with d
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
            "Without another word, I plunged myself deep inside the [gent1]'s tight entrance, groaning deeply as I tore through her folds until I was balls deep. The sound of her resulting, impassioned moan, echoed through the room, reverberating through both of us, and it was sublime."
            "[gent1]'s body arched upwards, her back curving beautifully as she let out a high-pitched whine of pleasure mixed with pain."
            "I could feel her growing wetter by the second. She bit down harder on her lip, trying desperately not to whimper in need as she felt every powerful thrust pressed against her."
            mc "Ooohhh, your pussy is so tight, [gent1]!"
            gent1 "Mmphhhh, this is the best feeling ever!"
            gent2 "Pfft, don't have too much fun~"
            "She moaned my name over and over again, fingers digging into the sheets beside [gent2] as she met each brutal thrust with equal ferocity – her body moving in perfect sync with mine."
            "It was beautiful chaos – an erotic dance purely fueled by lust and desire - and [gent1] felt herself slipping further into the depths of depravity with each passing moment."
            "Deciding that she couldn’t just lie there and watch us – [gent2] reached down between her legs, finding her own wet folds deeply slick with need. Her fingers brushed against her clit, teasingly circling around the sensitive nub before finally plunging inside her tight entrance."
            "Now they were both moaning – but it wasn’t nearly enough to quell the burning desire coursing through [gent2]."
            gent2 "Aaahhh, you guys are such teases!"
            "As if sensing her need, the [gent1] glanced over at her – eyes half-lidded with pleasure – and gave her a sultry smile, before returning her attention back to me."
            gent1 "Ooohhh, [gent2]… Forget watching someone get fucked, having someone else watch me is hot too~!"
            gent2 "Mmhhh... If it's so good, cum for me~"
            "And cum, she did – her body arching off the bed as wave after wave of pleasure coursed through her – her walls clenching tightly around me as she approached orgasm."
            "Finally, with a shattering cry that echoed through the room like thunder rolling across plains, the [gent1] body tightened one last time as it had a full-body orgasm."
            play sound2 cum
            if gen5 == 1:
                show lil2c v2b with c
            else:
                show lil2c v2a cum2 with c
            "My cock followed shortly after, erupting deep inside her for one last time, cum shooting deep into her pussy and womb."
            play sound2 cum
            with c
            play sound2 cum
            with c
            gent1 "Uooohhh, that’s right! Fill up my womb with your hot cum!"
            gent1 "Nnghhh! Aaahhhh, so much! Get me pregnant, mmmhhhh!"
            play sound2 cum
            show lil2c e3 -v2a -v2b 
            if gen1 == 1:
                show lil2c g3
            call aftersex from _call_aftersex
            stop music fadeout 10
            with c
            "Load after load filled her up, until finally, I pulled out and covered the two of them, hot cum dripping down fluffy thighs."
            "Once we’d finally finished, they both relaxed back onto the bed, spent and satisfied."
            $ energy -= 1 
            return
        label lilonside1:
            show lily3a e1 
            call camerabreath from _call_camerabreath_40
            play music sextheme
            play moans1 moansmisc2
            $ textbox = 2
            with d
            $ lily3 = 1
            "I guided her towards the bed, her neat violet hair cascading over her shoulder as she lay down. The desire in her eyes flickering like fire."
            lil "Do you have any ideas to spice things up?"
            call genreset from _call_genreset_5
            menu lilonsidem:
                "Lingerie (Needs Purchasing)" if lingerie == 0:
                    jump lilonsidem
                "Lingerie" if lingerie == 1:
                    if gen1 == 0:
                        $ gen1 = 1
                        $ gen2 = 0
                        show lily3a lingerie with d
                    else:
                        $ gen1 = 0
                        show lily3a -lingerie with d
                    jump lilonsidem
                "Pantyhose (Needs Purchasing)" if pantyhose == 0:
                    jump lilonsidem
                "Pantyhose" if pantyhose == 1 and gen3 == 0:
                    if gen2 == 0:
                        $ gen2 = 1
                        $ gen1 = 0
                        if gen4 == 1:
                            $ gen2 = 2
                            show lily3a p2 with d
                        else:
                            show lily3a p1 with d
                    else:
                        $ gen2 = 0
                        show lily3a -p1 with d
                    jump lilonsidem
                "Pregnant (Needs Milky Potion)" if pregpotion == 0:
                    jump lilonsidem
                "Pregnant" if pregpotion == 1:
                    if gen3 == 0:
                        $ gen3 = 1
                        if gen2 == 1:
                            $ gen2 = 0
                            show lily3a -p1 with d
                            "[lil] removes her pantyhose in anticipation them becoming uncomfortable against her belly."
                        show lily3a pregnant with d
                        "After drinking the potion, [lil] lets out a groan as her belly steadily grows to a pretty wild size."
                        lil "Uuu, I think I had too much of the potion!"
                    else:
                        $ gen3 = 0
                        show lily3a -pregnant with d
                    jump lilonsidem
                "Futa (Needs Futa Pills)" if futapill == 0:
                    jump lilonsidem
                "Futa" if futapill == 1:
                    if gen4 == 0:
                        $ gen4 = 1
                        show lily3a f1
                        if gen2 == 1:
                            $ gen2 = 2
                            show lily3a p2 -p1
                        with d
                        "[lil] pops the pill and suddenly a cock manifests between her legs."
                        if gen2 == 1:
                            "It ripped straight through her pantyhose. And how stange, various other rips also appeared."
                        lil "Wow! It's so big!"
                    else:
                        $ gen4 = 0
                        show lily3a -f1 with d
                    jump lilonsidem
                "(Continue)":
                    pass
            "Leaning in, I kissed her gently, my lips brushing against hers in a tender caress. She responded hesitantly at first, her lips soft and tentative, but as the kiss deepened, I felt her relax, the tension slowly melting away."
            mc "I can't believe how wet you are already."
            lil "Mmhh... I'm always wet around you, [mc]..."
            mc "Then I think that makes it my responsibility~"
            "My hands began to explore the curves of her body, tracing the contours of her form, moving lower until I reached her thighs. She pressed closer to me, her need becoming more pronounced with each touch."
            lil "Mmhh… Please, I want to feel you inside me~"
            "If she’s anything like her [lil] 2.0, this shyness won’t last. Her flank was raised and wiggling slightly, presenting an irresistible invitation."
            menu lilonsidem2:
                "Vaginal":
                    $ gent1 = "pussy"
                "Anal (Requires Lube)" if lubrication == 0:
                    jump lilonsidem2
                "Anal" if lubrication == 1:
                    $ gent1 = "ass"
            if gen2 == 1:
                show lily3a p2 -p1 with d
                "Satisfied with my choice, I ripped a path in her pantyhose and got into position."
            play sound2 cum
            "Taking my throbbing cock in my hand, I pressed it against her [gent1], gently pushing inside. Her slickness coated me, allowing a deeper venture with each push."
            play sound2 cum
            if gent1 == "pussy":
                show lily3a e2 v1 
            else:
                show lily3a e2 a1 
            with d
            play moans1 moansmisc3
            "Once my tip was finally wet enough, I pushed forward once more and finally thrust until I was balls deep." 
            "A deep moan escaped her lips as she felt herself getting filled for once again, her body tensing up before finally relaxing into the sensation. Any discomfort was replaced by an overwhelming flood of pleasure, leaving her body trembling in awe."
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
            if gen4 == 1:
                "With each thrust, her cock tightened and throbbed, and I was tempted to do something..."
                menu:
                    "Stroke her Cock":
                        "I reached out and began to stroke her massive cock. The additional pleasure hit [lil] in the core, causing her hips to shake and twitch."
                    "Pass":
                        pass
            lil "Mmphhh, I finally understand the importance of sex. It's not just a waste of time, it's great exercise, a mood booster, and so much more~!"
            mc "Hahaha, geeking out again? I must not be fucking you hard enough if you can still talk."
            lil "Oohh, well... Why don't you shut me up, then?"
            "I leaned over and kissed her, my hands exploring every inch of her body, savoring the feel of her beneath me. She responded eagerly, her hips arching up to meet mine, her moans growing louder, more urgent."
            "I could feel her surrendering to her instincts, her [gent1] squeezing my cock tighter and tighter, begging to be filled."
            if gen3 == 1:
                "And the better she felt, the more milk would spray from her swollen breasts, her heavy belly heaving with each thrust."
            "Lost in the throes of our passionate union, time and reality seemed to dissolve around us."
            "We moved together with a primal, instinctual grace, our bodies gradually becoming synchronized. The once reserved and studious [lil] moaned and writhed beneath me, completely surrendered to the pleasure."
            lil "Uooohhh, goddess yes! Thrust it right there! Ooohhh, just like thaaaat~!"
            "I felt my control slipping, overwhelmed by the tightness of [lil]’s [gent1] and the heady scent of our sex. I knew I couldn’t hold myself back much longer."
            mc "Aahhh, it feels too good! I’m about to cum!"
            lil "Ngghh, don’t hold back! Ejaculate inside me with that hot, fertile sperm!"
            play sound2 cum 
            if gent1 == "pussy":
                show lily3a cum v2 
            else:
                show lily3a cum a2 
            with c
            play sound2 cum
            with c
            "With a series of powerful thrusts, I reached climax, my seed spilling deep inside of her."
            play sound2 cum
            with c
            play sound2 cum
            show lily3a e3 
            with c
            if gen4 == 1:
                show lily3a f2
                with c
                "Her own cock erupted, spraying her bed with hot loads of horse cum."
            else:
                "My body grew tense, my mind fuzzy and blank as waves of orgasmic pleasure washed over me." 
            stop ambience1 fadeout 1
            play moans1 moansmisc2
            call camerabreath from _call_camerabreath_41
            show lily3a -v2 -v1 -a2 -a1 with d
            "Panting and slick with sweat, I pulled out and basked in the afterglow."
            lil "Aahhh, you're the best, [mc]~ I never thought my road to princesshood would be paved with so much sex."
            $ energy -= 1
            return
        label lilonside2:
            play sound2 cum
            show lily3b e1 
            $ textbox = 2
            call camerabreath from _call_camerabreath_42
            play moans1 moansmisc2
            with d
            "[lil] curled up, her voluptuous rear prominently presented like a delectable treat just waiting to be devoured. Her pristine mane a tangled mess of violet curls cascading across the bed."
            lil "This is a good pose, right? I like watching you, and you get a good view of my butt and all the good stuff~"
            mc "When I met you, I never imagined you'd say something like that."
            lil "Ah, I'm so over thinking sex is 'gross'. Now come on, stud! {i}She pats her butt and spreads her labia{/i}"
            mc "I'm such a bad influence."
            call genreset from _call_genreset_6
            menu lilonside2m:
                "Goth (Needs Purchasing)" if goth == 0:
                    jump lilonside2m
                "Goth" if goth == 1:
                    if gen4 == 0:
                        $ gen4 = 1
                        show lily3b goth with d
                    else:
                        $ gen4 = 0
                        show lily3b -goth with d
                    jump lilonside2m
                "Lingerie (Needs Purchasing)" if lingerie == 0:
                    jump lilonside2m
                "Lingerie" if lingerie == 1:
                    if gen1 == 0:
                        $ gen1 = 1
                        $ gen2 = 0
                        show lily3b lingerie with d
                    else:
                        $ gen1 = 0
                        show lily3b -lingerie with d
                    jump lilonside2m
                "Pantyhose (Needs Purchasing)" if pantyhose == 0:
                    jump lilonside2m
                "Pantyhose" if pantyhose == 1:
                    if gen2 == 0:
                        $ gen2 = 1
                        $ gen1 = 0
                        show lily3b p1 
                        if gen3 == 1:
                            $ gen2 = 2
                            show lily3b p2
                        with d
                    else:
                        $ gen2 = 0
                        show lily3b -p1 with d
                    jump lilonside2m
                "Plug (Needs Purchasing)" if buttplug == 0:
                    jump lilonside2m
                "Plug" if buttplug == 1:
                    if gen3 == 0:
                        $ gen3 = 1
                        if gen2 >= 1:
                            show lily3b p2 -p1 with d
                            "The pantyhose was ripped before putting the plug in."
                        with d
                        show lily3b plug with d
                        "After a few moments of teasing and easing, the finally slips in!"
                    else:
                        $ gen3 = 0
                        show lily3b -plug with d
                    jump lilonside2m
                "(Continue)":
                    pass
            lil "And where is my big friend going today?"
            menu lilonside2m2:
                "Vaginal":
                    $ gent1 = "pussy"
                "Anal (Needs Lubrication)" if lubrication == 0:
                    jump lilonside2m2
                "Anal" if lubrication == 1:
                    $ gent1 = "ass"
                    show lily3b -plug with d
                    "I pop her plug out first and start to apply the cool lubrication to her twitching butt."
            if gen2 == 1:
                show lily3b p2 -p1 with d
                "Satisfied with my choice, I ripped her pantyhose open."
            play sound2 cum
            if gent1 == "pussy":
                show lily3b e2 v1 with d
            else:
                show lily3b e2 a1 with d
            "Her luscious flanks quivered as I repositioned myself. With a powerful thrust, I buried my throbbing member deep inside her once again. This time it pushed inside with ease, her [gent1] almost sucking me deeper with desperate need."
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
            "[lil] moaned louder than ever, her body trembling as I thrust into her, quickly adopting a wild, almost feral pace."
            lil "Nngghhh, this is what I always wanted! I said sex was gross, I said people were gross, but it was all bullshit! I always watched porn, I always fantasized about hot studs..."
            mc "Mmmhh, you always wanted to be taken like a slutty mare~?"
            lil "Uooohhh yes! This is the real me! A dumb mare gasping for sex! Pound my [gent1] with your thick cock!"
            "Her voice had transformed from that of a timid scholar to a sex-starved slut."
            "I leaned in, nibbling her ear possessively as my hips slammed into hers with relentless force. She arched her back, pushing against my thrusts, begging for more. Each movement drove deeper, grinding deep inside her [gent1]."
            "Our passionate union continued unabated, the rhythm growing more frenzied with each passing second."
            "Sweat dripped from our bodies as we moved together like two well-oiled machines, the burdens of life melting away in the heat of the moment."
            lil "Aaahhh, y-yes! Keep going like that and I-I'll..."
            mc "Nngghh, cum for me. Be a good girl and cum!"
            "[lil] moaned and whimpered as she began to climax. The dirty talk had finally pushed her over the edge. It was a full-body orgasm that rocked her to the core."
            "Her tight [gent1] clenched around my cock, trying to draw out every last drop of my seed."
            lil "Uooohhhh! It’s sooo goooood! Mmmhhhh! P-Please, cum deep inside me!"
            play sound2 cum
            if gent1 == "pussy":
                show lily3b v2 cum
                show internalcreampie
            else:
                show lily3b a2 cum
            with c
            play sound2 cum
            with c
            "With a series of powerful, final thrusts, I let loose inside her, filling her [gent1] with my hot seed."
            play sound2 cum
            with c
            play sound2 cum
            show lily3b e3 
            hide internalcreampie 
            with c
            "My cock throbbed as it continued to empty itself, our point of contact bubbling with our shared fluids as we continued thrusting until the pleasure was long gone."
            stop ambience1 fadeout 1
            play moans1 moansmisc2
            call camerabreath from _call_camerabreath_43
            show lily3b -v2 -v1 -a2 -a1 with d
            "Finally, my lack of energy caught up with me, and I pulled out of her [gent1] and collapsed onto the bed."
            "Both of us lay there, panting heavily, drenched in sweat and satisfaction."
            play sound2 equip
            stop moans1
            play ambience1 night
            stop music fadeout 3
            $ energy -=1 
            return
    label pensexscenes:
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
                group pregnant:
                    attribute pregnant:
                        "moxpen2bpregnant [penb]"
                group futa:
                    attribute futa:
                        "moxpen2bfuta [penb]"
                group futacum:
                    attribute futac:
                        "moxpen2bfutacum"
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
            call genreset from _call_genreset_7
            menu pencowgirlm:
                "Lingerie (Needs Purchasing)" if lingerie == 0:
                    jump pencowgirlm
                "Lingerie" if lingerie == 1:
                    if gen1 == 0:
                        $ gen1 = 1
                        play sound2 equip
                        show moxpen2b lingerie with d
                        pen "Cute, right?"
                    else:
                        $ gen1 =0
                        show moxpen2b -lingerie
                    jump pencowgirlm
                "Futa (Requires Instant-Futa Pills)" if futapill == 0:
                    jump pencowgirlm
                "Futa" if futapill == 1: 
                    if gen2 == 0:
                        $ gen2 = 1
                        play sound2 equip
                        show moxpen2b futa with d
                        "[pen] pops the pills and suddenly a massive cock emerges from her crotch."
                        pen "Huh... That's not a horsecock, but I'll take it!"
                    else:
                        $ gen2 = 0
                        pen "A little bit of magic will remove it."
                        show moxpen2b -futa with d
                    jump pencowgirlm
                "Pregnant (Requires Milky Potion)" if pregpotion == 0:
                    jump pencowgirlm
                "Pregnant" if pregpotion == 1:
                    if gen3 == 0:
                        $ gen3 = 1
                        play sound2 equip
                        show moxpen2b pregnant with d
                        "[pen] downs the potion and suddenly her body and breasts swell until she looks completely pregnant."
                        pen "Uoohhh, is this an aphrodisiac too? I'm feeling so horny right now..."
                    else:
                        $ gen3 = 0
                        pen "A little bit of magic will remove it."
                        show moxpen2b -pregnant with d
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
            if gen2 == 1:
                pen "You like my cock? Hehe. It feels so strange..."
                mc "Show me what those hips can do."
            elif gen3 == 1:
                pen "Mmhh, my breasts won't stop leaking..."
                mc "Show me what those hips can do."
            else:
                pen "You ready?"
                mc "You know it. Show me what those hips can do."
            "As I lay there on the soft bed, I watched with bated breath as she descended gracefully towards me. Her eyes locked with mine, filled with desire and need."
            play sound2 cum
            show moxpen2b e2 sex2 with dissolve
            play moans2 moansmisc3
            with hpunch
            if gen2 != 1:
                "She lowered herself slowly, savoring every sensation, her every move driving me wild with anticipation. Then finally, her tight pussy lips engulfed me completely."
            else:
                "Even though she had a massive cock now, she still had a pussy down there somewhere. She lowered herself slowly, savoring every sensation, her every move driving me wild with anticipation. Then finally, her tight pussy lips engulfed me completely."
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
            if gen2 != 1:
                "[pen] moaned even louder, her pace quickening. She leaned forward this time, her breasts brushing against my chest as her whole body shook with each powerful thrust. The friction between us intensified even further, sending shockwaves of pleasure coursing through us both."
            else:
                "[pen] moaned even louder, her pace quickening. She leaned forward this time, her large belly and milky breasts brushing against me as her whole body shook with each powerful thrust. The friction between us intensified even further, sending shockwaves of pleasure coursing through us both."
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
            if gen3 == 1:
                show moxpen2b futac
            show moxpen2b sex3 
            with c
            play sound2 cum 
            show internalcreampie with c
            if gen3 != 1:
                "My own orgasm washed over me like a tidal wave, filling her womb with hot seed."
            else:
                "And her cock erupts too, splattering my torso and chest with her hot cum."
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
            if gen2 == 1:
                "After about twenty minutes of action, her body finally reverts to normal."
                pen "So, is that what it's like to be a guy? Well, I guess not, I was still getting fucked in my pussy! Hehe."
            elif gen3 == 1:
                "After about twenty minutes of action, her body finally reverts to normal."
                pen "That was more of a workout than usual - ah, and look how much mess the milk made!"
            else:
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
                "Breast Expansion (Requires Milky Potion)" if pregpotion == 0:
                    jump penboobjobmenu
                "Breast Expansion" if pregpotion == 1:
                    if gen2 == 0:
                        $ gen2 = 1
                        show pen1a bigger with d
                        $ gent2 = "milky"
                        $ gent3 = "inflated"
                        $ gent4 = "fat"
                        "[pen] drinks the potion and suddenly her breasts visibly expand and enlarge."
                        "Once it seems like they've finally finished, milk suddenly spurts out of her teats."
                        pen "Uooohhh, w-why does that feel so good?"
                    else:
                        $ gen2 = 0
                        pen "A little bit of magic will fix that right up."
                        $ gent2 = ""
                        $ gent3 = ""
                        $ gent4 = ""
                        show pen1a -bigger with d
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
                mc "Now, use your [gent4] breasts, you slutty bitch."
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
            "The sensation was incredible, the warmth and softness of her fur sending waves of pleasure through me. She squeezed her [gent2] breasts together, creating a tight, velvety tunnel, and started to move up and down, her eyes never leaving mine."
            "Occasionally, she would flick her tongue out, licking the tip of my cock, sending electric shivers down my spine. Her dedication and skill were evident in every movement, her [gent3] breasts gliding smoothly along my length. She was much better than the first time."
            if petplay == 1:
                "I tightened my grip on the leash, pulling her closer, the leather collar digging slightly into her neck."
                mc "You're such a good bitch, [pen]."
            else:
                mc "Mmphhh, that feels so good! You've really improved!"
            "I praised, watching as her eyes sparkled with pleasure at my words. She increased her pace, her [gent2] breasts moving faster, her tongue flicking out more frequently to tease me. The combination of her [gent3] breasts and long pony tongue was driving me wild, the pressure building steadily."
            if petplay == 1:
                pen "Yes, Master. I'm your naughty bitch~!" 
                "She responded breathlessly, her voice filled with arousal. The collar and leash accentuated her submissive role, each tug and pull reinforcing the power dynamic between us."
                "As I felt myself getting closer, I pulled harder on the leash, this spurred her on to move faster, her tongue starting to get seriously sloppy."
            else:
                pen "Mmmhhh... I can't allow myself to get stale while there are so many other mares pining for your attention now, can I~"
                mc "Hah, you're actually been practicing?"
                pen "Mmh, I've seen a few videos~ Now about at this technique?"
            mc "Oohh, okay, that's amazing! Aahh... I'm going to cum soon!"
            "Even though I tried to hold back, [pen] didn't slow down; if anything, she became even more determined, her [gent4] breasts moving with increased fervor."
            if petplay == 1:
                pen "Do it, Master! Cum for your little bitch!" 
            else:
                pen "Aahh, cum for me, [mc]!"
            "Her tone both submissive and eager. The combination of her words and her relentless movements pushed me over the edge."
            play sound2 cum
            show pen1a e2 cum with c
            play sound2 cum
            with c
            "With a final, powerful thrust between her [gent2] breasts, I released, my cum spilling onto her fur and her tongue as she eagerly licked up every drop she could reach."
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
            if gen2 == 1:
                pen "Oh, my nipples are still leaking a little. That potion doesn't have any permanent effects, right?"
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
        label penmoxmarathon:
            show pen2a always me1 pe1 
            play music sextheme
            $ textbox = 2
            call camerabreath from _call_camerabreath_44 
            play moans2 moansmisc2
            with d
            "After being lead to the bedroom, I found myself in yet another heavenly position."
            "[mox] and [pen] perched atop me, their sleek, lithe bodies aligned ass-to-ass above my face. Their flawless fur was so close I could see every strand, the sight both captivating and seductive."
            "A heady scent filled my nostrils—a blend of their excitement and something sweet, almost floral." 
            "My senses were ablaze, my body responding instinctively to the raw eroticism of the scene. [mox]'s violet eyes locked onto mine, a wicked smile curling her lips as she whispered..."
            mox "Less of a surprise than last time, but you can't deny that you love the view~"
            "Before I could fully absorb the view above, [mox] began to move."
            show pen2b always me1 pe1 with d
            "She bent over slowly, deliberately, each motion a calculated act of seduction. Her back arched provocatively, drawing my gaze. [pen], ever the willing accomplice, mirrored her movements with a dancer's grace."
            "With audacious confidence, [pen] cradled [mox]'s flank, her greedy hands firm yet gentle as they spread [mox]'s pussy, exposing her fully to my hungry gaze."
            pen "Shall we slip a plug in and tighten that pussy up? Or maybe you have your eyes on a different prize, hmm?"
            call genreset from _call_genreset_8
            menu penmoxmarathonm1:
                "Punk (Needs Purchasing)" if punk == 0:
                    jump penmoxmarathonm1
                "Punk" if punk == 1:
                    if gen1 == 0:
                        $ gen1 = 1
                        mox "Hit those lights!"
                        show pen2b p0 p1 with d
                    else:
                        $ gen1 = 0
                        show pen2b -p0 -p1 with d
                    jump penmoxmarathonm1
                "Plug (Needs Purchasing)" if buttplug == 0:
                    jump penmoxmarathonm1
                "Plug" if buttplug == 1:
                    if gen2 == 0:
                        $ gen2 = 1
                        show pen2b plug with d
                        "With some careful easing, the plug pops inside of [mox]'s butt."
                    else:
                        $ gen2 = 0
                        show pen2b -plug with d
                    jump penmoxmarathonm1
                "Continue with Vaginal":
                    $ gent1 = "pussy"
                "Continue with Anal (Needs Lubrication)" if lubrication == 0:
                    jump penmoxmarathonm1
                "Continue with Anal" if lubrication == 1:
                    $ gent1 = "ass"
                    if gen2 == 1:
                        pen "Let's see if the plug loosened you up at all?"
                        show pen2b -plug with d
                        "[pen] pops the plug out and squeezes her ass wide for me."
                        "I step forward with the lubrication and we apply it together, while [mox] coos and wiggles at the touch."
            pen "Mmhh, what a juicy [gent1]! Can't wait to bury my face in there once you've filled her up, [mc]."
            "There was a fluidity to their actions, a silent communication that spoke volumes about their trust and comfort together. [pen]'s finger traced [mox]'s exposed clit, sending a shiver of anticipation through her."
            pen "Go ahead, she’s more than ready for your cock."
            mox "Mmmhh, always am~"
            $ pen2 = 1
            "I positioned myself behind [mox], the heat radiating from her body palpable even from inches away. My hands found her hips, gripping her soft fur with a possessiveness that surprised even me."
            "[mox]'s body responded instantly, her back arching further, her breath hitching in eager anticipation."
            play sound2 cum
            play moans1 moansmisc2
            if gent1 == "pussy":
                show pen2b v1 me2 pe2
            else:
                show pen2b a1 me2 pe2 
            if gen1 == 1:
                show pen2b p2
            with d
            "With a powerful thrust, I buried myself deep inside her [gent1]. The sensation of her inner heat and wetness was overwhelming, an electrifying rush that set every nerve on fire."
            play ambience1 sex
            "[mox] moaned, a sound filled with need, her voice a symphony of desire. As I began to move, her body quaked beneath me, struggling to remain upright under the onslaught of sudden, fierce pleasure."
            "A hushed, carnal ambience filled the room, the atmosphere thick with the raw energy of our sex."
            mox "Aaahhh, ahhh! [mc] is a bad influence~ I was such a pure mare, but now he pounds me every day~"
            pen "Hahaha, pure? You were just waiting for the right guy to pounce~"
            mox "Mmmhh, [mc] is the right guy and more!"
            "[pen] watched with ravenous eyes, her desire palpable. She leaned in close, her breath hot against my ear as she whispered encouragement, her hands never stopping their relentless teasing of [mox]'s trembling body."
            pen "Ooohhh, I love the way her [gent1] squeezes against your cock as you slide in... Mmm..."
            "[mox]’s moans crescendoed into cries of ecstasy as I picked up the pace, our bodies locked in a frenzied rhythm that obliterated all thought, leaving only the raw, pure sensation of our fucking."
            "The room was suffused with the intoxicating aroma of sweat and arousal, a testament to our fevered passion."
            "At this point, [pen]'s hands found their target, teasing [mox]’s clit with expert precision, driving her wild with pleasure. [mox]’s response was a wordless scream, her body pushing back against mine with a desperation that matched my own."
            pen "Mmhh… [penmc], I want you to fill up [mox]'s tight [gent1] up for me."
            "[mox]’s climax was sudden and explosive, her body convulsing around me as she was swept away by relentless waves of bliss."
            "Her pussy clenched around my cock with a fierce, exquisite pressure that sent me over the edge, lost in the euphoria of our shared ecstasy."
            play sound2 cum
            if gent1 == "pussy":
                show pen2b cum v2 with c
            else:
                show pen2b cum a2 with c
            play sound2 cum
            with c
            "I found my release, accompanied by a burst of intense pleasure that left my mind numb."
            play sound2 cum
            with c
            play sound2 cum
            show pen2b me3 pe3 
            if gen1 == 1:
                show pen2b p3
            with c
            mox "Uooohhhh, gods yes! I love the feeling of your cum shooting inside me, mmphhh…"
            show pen2b -v1 -v2 -a1 -a2 with dissolve
            stop ambience1
            play moans1 moansmisc2
            scene black with dissolve
            "As the echoes of our climax faded, [mox] rolled over and feigned death on the bed. Her eyes were closed, a look of blissful exhaustion painting her features. At least she died doing what she loved."
            show pen2c always e1 c1 
            $ textbox = 1
            with d
            "However, [pen], ever the opportunist, had other ideas. Her movements were fluid, predatory, as she gracefully positioned herself atop [mox]."
            pen "Wow, you came so much~ Hehe."
            mox "While [pen] is muff diving, want to add anything else to the passion before you get erect again?"
            call genreset from _call_genreset_9
            $ gent2 = "pussy"
            menu penmoxmarathonm2:
                "Lingerie (Needs Purchasing)" if lingerie == 0:
                    jump penmoxmarathonm2
                "Lingerie" if lingerie == 1:
                    if gen1 == 0:
                        $ gen1 = 1
                        show pen2c lingerie with d
                        "While the girls go at it, I slip the lingerie on them."
                    else:
                        $ gen1 = 0 
                        show pen2c -lingerie with d
                    jump penmoxmarathonm2
                "Futa (Needs Futa Pills)" if futapill == 0:
                    jump penmoxmarathonm2
                "Futa" if futapill == 1:
                    if gen2 == 0:
                        $ gen2 = 1
                        show pen2c futa1 with d
                        $ gent2 = "cock"   
                        "[mox] takes the pill and all of a sudden a horse cock gradually grows and fills up [pen]'s mouth!"
                        pen "Mmpphh, mfff! Wasn't expecting cock!"
                        mox "Uuuooohhh, it's so sensitive! Don't stop, [pen]!"
                    else:
                        $ gen2 = 0 
                        show pen2c -futa1 with d
                        $ gent2 = "pussy"
                    jump penmoxmarathonm2
                "(Continue)":
                    pass
            "[pen]'s breath was warm and soft against [mox]’s inner thighs, and I could see [mox]’s fur standing on end in anticipation."
            mox "Ahhh, someone’s eage- ooohh!"
            if gen2 == 0:
                "[pen]’s  tongue emerged, a flickering serpent that traced teasing patterns across [mox]’s folds. She lapped at the thick cum with a tenderness that made [mox] shudder, her back arching off the bed in a silent plea for more."
            else:
                "[pen]’s  tongue emerged, a flickering serpent that slid up [mox]'s newfound girth. She lovingly worshipped the cock in a way that made [mox] shudder, her back arching off the bed in a silent plea for more."
            "The contrast between [pen]’s soft, loving touch and the raw intensity of my previous bout was a sight to behold. Yet, despite the delicate nature of [pen]’s ministrations, the pleasure was unmistakable in [mox]’s eyes. It wasn’t long before [mox]’s own tongue began to explore, lapping eagerly at [pen]’s swollen, juicy clit."
            "As I watched the scene unfold, the urgent need that had been simmering within me could no longer be contained. My cock was fully erect once again and my eyes locked on [pen]’s fluffy butt."
            "Reaching for my cock, I angled myself against [pen]'s opening. [mox]’s keen gaze from below eagerly watching every move."
            play ambience1 sex
            play sound2 cum
            play moans1 moansmisc4
            show pen2c v1 with d
            "With a slow, deliberate motion, I eased into [pen]. The feeling of her warmth wrapping around me was accompanied by a shiver of satisfaction"
            "I began thrusting immediately, my cock stretching [pen]’s pussy tantalizingly close to [mox]’s face, my balls occasionally brushing against her face (and yes, once again I made sure to dodge the horn)."
            pen "Ahhh, finally… I needed this so bad~ Fuck me hard, [penmc]."
            mox "Mmphh, mhh… {i}Lick, suck{/i} What a stunning view~"
            "The rhythm of my thrusts was relentless, each thrust deliberate and firm. [pen]’s moans were a muffled symphony, her attention split between [mox]'s [gent2] and the ceaseless drive of my cock from behind."
            "Even so, her body seemed to fight back, instinctively moving in time with me, eager to savor every fragment of pleasure."
            "The room thrummed with our shared intensity. The wet, rhythmic slap of flesh against fur, mingled with our gasps and moans, filled the air, reverberating off the wooden walls of the treehouse like a living, breathing entity."
            "As we lost ourselves in the moment, it felt as though our individual selves were dissolving into a singular force of need and sensation. The boundaries between pleasure and pain, control and surrender, blurred until they were indistinguishable."
            "Every thrust, every touch, every moan became a testament to the primal, almost hypnotic pull of our deepest instincts."
            play sound2 cum 
            show pen2c c2 v2 e1 with c
            play sound2 cum 
            with c
            "The climax, when it came, was a shared eruption of intensity. [pen]’s body tensed around my cock, her moans mingling with [mox]’s cries as our release mingled in a torrent of raw, unfiltered ecstasy."
            play sound2 cum 
            with c
            play sound2 cum 
            with c 
            if gen2 == 1:
                show pen2c futa2 with d
                "And what's more, [pen] had successfully managed to force an orgasm out of [mox], causing thick loads of horse cum to launch against the back of her throat. She almost gagged under the force and quantity, but dutifully swallowed down every load."
            stop music fadeout 1
            call stopbgs from _call_stopbgs_30
            call camerareset1 from _call_camerareset1_9            
            "The final waves of pleasure left us all breathless, our bodies collapsing together in a tangled, sweaty heap on the bed."
            "For the first time in almost ten minutes, the room was quiet, save for the sound of… someone opening the door!"
            play sound2 move1
            scene bg bedroom2
            show night:
                blend "multiply"
                alpha 0.66
            show lil horny blush:
                xalign 0.25
            with d
            lil "Room for one more, girls?"
            show pen horny blush cum with d:
                xalign 0.75
            pen "[lil], there’s always room for one more~"
            pen "[mox], [lil], turn around and present yourselves to [penmc]."
            play moans1 moansmisc2
            play moans2 moansmisc3
            play music sextheme2
            call camerabreath from _call_camerabreath_45
            show pen2d always l1 m1 p1 c1 
            $ textbox = 2
            with d
            "Commanding and confident, [pen] was a true switch as she seized control once more. The other girls fell into line without hesitation. Their flanks, now tantalizingly presented, were enough to reignite even the coldest ember, and my cock responded, swelling with renewed vigor."
            play sound2 magic1
            with p
            "[pen]’s hands glided over each ass and down to the pussies, her touch a blend of soothing warmth and electric stimulation. There was a faint crackle of magic from her horn, and I felt an unexpected surge of vitality course through me."
            pen "{i}Pant, pant{/i} That’s a little magic to pep you up. Let's show these girls what you've got!"
            "I moved in behind [lil], my hands tracing the contours of her smooth fur, feeling the heat radiate from her body."
            lil "I couldn't resist again... I was masturbating to the sounds."
            mc "Oh really? Truth is, I'm the one that can't resist you, [lil]."
            play sound2 cum
            show pen2d s1 l2 m2 p2 with d
            play ambience1 sex 
            play moans1 moansmisc4
            "I pressed the tip of my cock against [lil]’s entrance and pushed inside. The sensation sparked a jolt of pleasure through both of us. She was already dripping wet, so I wasted no time thrusting."
            pen "I hope you don't mind, but I'm going to be strumming your clit like a guitar, cutie~"
            lil "Aaahh... Haahhh... You can touch me wherever~"
            "[pen]’s hands never left [lil]’s body, spreading, rubbing, and teasing, each touch amplifying the pleasure until it bordered on overwhelming. [lil]’s moans grew louder, each thrust drawing us both closer to the precipice."
            pen "Mmmhh… What a good girl! Now, cum for us~"
            play sound2 cum
            show pen2d s2 c2 with c
            play sound2 cum
            with c
            "The final thrust pushed me over the edge, my body shuddering as I released a torrent of hot cum deep inside [lil], sending her spiraling into her own rapturous climax. Our orgasms were intense, with an infectious satisfaction radiating out from her."
            stop ambience1 fadeout 3
            play moans1 moansmisc2
            show pen2d -s2 -s1 l1 m1 p1 with d
            "But the night had more in store. As I withdrew from [lil], [pen] gently guided me toward [mox], her eyes flickering with a predatory glint."
            mox "Two turns? [mox] hits the jackpot yet again, baby!"
            "I maneuvered myself behind her, my cock responding instinctively, stirring to life at the mere thought of what was to come."
            pen "Ready?"
            mox "Always."
            play sound2 cum
            show pen2d s3 l3 m3 p3 with d
            play ambience1 sex 
            play moans1 moansmisc4
            "I slipped inside [mox], her pussy enveloping my cock with incredible warmth. Her moans slipped out freely in rhythm to my movements."
            pen "There you go. Fuck all that heat away."
            "Even as fatigue began to set in, our actions were driven by a raw, unrelenting desire, all aimed at one goal: release."
            pen "Can you believe these two were virgins just [day] days ago? Look at how their pussies cling around you now, mmm..."
            "[pen]’s hands were busy, slipping beneath the action to caress [mox]’s clit, her voice a low, encouraging murmur that pushed us further. I could tell from [lil]’s moans that [pen] was still rubbing her clit too."
            pen "Are you getting close again, [lil]?"
            lil "Uooohhhh, y-yes, [pen]!"
            mox "Nnngghhh, I-I'm about to cum!"
            pen "Gosh, you're both adorable!"
            "As we neared the climax of our encounter, the room was a cacophony of our collective ecstasy. With an explosive thrust, I reached my climax, my body trembling as I surrendered to the incoming storm of pleasure."
            play sound2 cum
            show pen2d s4 c3 l2 with c
            play sound2 cum
            with c
            mox "Uooohhhh! I’m cumming!"
            play sound2 cum
            with c
            play sound2 cum
            with c
            lil "Nnghhh, me too!"
            show pen2d p2 with c
            pen "Fuhuhu, I can’t believe I made [lil] cum~"
            stop music fadeout 3
            call stopbgs from _call_stopbgs_31
            call camerareset from _call_camerareset_12
            scene bg bedroom2
            show night:
                blend "multiply"
                alpha 0.66
            with d
            "After a period of resting, the four of us went our separate ways, and once again, quiet returned to the treehouse."
            $ energy -=1 
            return
#Brothel:
label brothelsexscenes:
    label rubysexscene:
        label rubthighjob:
            stop music fadeout 3
            show black with d
            play music sextheme
            scene black with d
            $ textbox = 2
            with d
            layeredimage ruby1a:
                always:
                    "ruby1ab [rubb]"
                group eyes:
                    attribute e1:
                        "ruby1ae1 [rubb]"
                    attribute e2:
                        "ruby1ae2 [rubb]"
                    attribute e3:
                        "ruby1ae3 [rubb]"
                group lingerie:
                    attribute lingerie:
                        "ruby1alingerie"
                group underwear:
                    attribute underwear:
                        "ruby1aunderwear"
                group wet:
                    attribute wet:
                        "ruby1awet"
                group cum:
                    attribute cum:
                        "ruby1acum"
                group thighjob:
                    attribute t0:
                        "ruby1athighjob 0"
                    attribute t1:
                        "ruby1athighjob 1"
                    attribute t2:
                        "ruby1athighjob 2"
                group futa:
                    attribute futa:
                        "ruby1afuta [rubb]"
                group pregnant:
                    attribute pregnant:
                        "ruby1apregnant [rubb]"
                group futaclip:
                    attribute futaclip:
                        "ruby1afutaclip"
                group cum2:
                    attribute cum2:
                        "ruby1afutacum"
            "While we were absentmindedly chatting in the office, with [rub] drinking tea and lounging around in a bathrobe. I notice her thighs and get an idea." 
            show ruby1a e1 wet with d
            rub "Between my fluffy thighs? That sounds simply divine, darling."
            rub "Do you have any ideas how to spice it up further?"
            call genreset from _call_genreset_10
            menu rubythighjobmenu:
                "Lingerie (Requires Purchasing)" if lingerie == 0:
                    jump rubythighjobmenu
                "Lingerie" if lingerie == 1:
                    play sound2 equip
                    if gen1 == 0:
                        $ gen1 = 1
                        show ruby1a lingerie with d
                        rub "Aahhh, isn't it a beautiful contrast on my snow white fur?"
                    else:
                        $ gen1 = 0
                        show ruby1a -lingerie with d
                    jump rubythighjobmenu
                "Underwear (Requires Lingerie)" if lingerie == 0:
                    jump rubythighjobmenu
                "Underwear" if lingerie == 1:
                    play sound2 equip
                    if gen2 == 0:
                        $ gen2 = 1
                        show ruby1a underwear with d
                        rub "I bet this'll be a nice texture against your cock."
                    else:
                        $ gen2 = 0
                        show ruby1a -underwear with d
                    jump rubythighjobmenu
                "Futa (Requires Futa Pills)" if futapill == 0:
                    jump rubythighjobmenu
                "Futa" if futapill == 1:
                    if gen3 == 0:
                        $ gen3 = 1
                        if gen2 == 1:
                            rub "Hold it, dear. I should take off the underwear first."
                            show ruby1a -underwear with d
                            $ gen2 = 0
                        show ruby1a futa 
                        if gen4 == 1:
                            show ruby1a futaclip 
                        with d
                        "[rub] pops a pill, and watches as her new member grows."
                        rub "Oh my, this is rather unique, isn't it?"
                    else:
                        $ gen3 = 0
                        show ruby1a -futa -futaclip with d
                    jump rubythighjobmenu
                "Pregnant (Requires Milky Potion)" if pregpotion == 0:
                    jump rubythighjobmenu
                "Pregnant" if pregpotion == 1:
                    if gen4 == 0:
                        $ gen4 = 1
                        show ruby1a pregnant 
                        if gen3 == 1:
                            show ruby1a futaclip 
                        with d
                        "[rub] pops a pill, and patiently watches her belly grow and press against the robe of her gown."
                        rub "This'll make it a little harder to move, you know~"
                        "Just as it's finished growing, milk suddenly sprays from her teats."
                        rub "Oh my, I can add my own milk to the tea."
                    else:
                        $ gen4 = 0
                        show ruby1a -pregnant -futaclip with d
                    jump rubythighjobmenu
                "(Continue)":
                    pass
                "(Stop Scene)":
                    return
            if gen3 == 1 and gen4 == 1:
                rub "Uhm... Darling... Is this really how we're going to do it?"
                mc "Is something wrong?"
                rub "Nothing, nothing... I just didn't quite anticipate you to have such... specific... tastes."
            "She sits before me, her fingers teasing the knot of her bathrobe, loosening it just enough to hint at the treasures underneath."
            rub "I accept your challenge, but... let's see if we can make it even more interesting..."
            "She gestures for me to kneel down below her. I obey as she positions herself above me, her thighs now ontop of me. The angle is perfect."
            play moans1 moansmisc2
            show ruby1a t0 with d
            "The wamrth of her body as she settles into place was enough to get the blood flowing, my cock gradually swelling between her thighs."
            mc "You're about to make this unforgettable, aren't you?"
            rub "Oh, darling, you have no idea."
            show ruby1a e2 t1 with d
            play ambience1 handjob2
            "She picks up her tea again, her robe slipping further as she balances it in one hand. With the grace of a dancer, she begins to move, her thighs tightening around me, creating a delicious friction."
            "I watch in awe, every movement precise and controlled. The sight of her, half-clothed and utterly confident, is amazing."
            "She arches her back, the robe falling to reveal her bare breasts, her nipples hard with arousal."
            mc "[rub], you're incredible..."
            if gen3 != 1:
                rub "I do aim to please, darling. Now, hold on tight."
            else:
                rub "I'm going to use a little bit of magic to link our members and their pleasure together. Now, hold on tight~"
                play sound2 magic1
                with vpunch
                "A little bit of magic later, and I can immediately tell that with every movement, she's feeling a ton of pleasure."
            "Her voice is steady, despite the challenging position, her gaze is unwavering as she focuses on not spilling a drop of tea."
            "The movements become more fluid and intense, her thighs squeezing and releasing me, purposely driving me to the edge."
            "The rhythmic motion, combined with the sight of her poised and elegant, is alone almost too much for me to hold back."
            "My breathing quickens, my hands gripping anything around me as I feel the pressure building inside."
            mc "[rub], I'm close!"
            rub "Then let go, my dear. Let me take you there."
            "She gives me a knowing smile, her thighs continuing to work me with expert precision. Her tea remains perfectly steady, a testament to her extraordinary control."
            play sound2 cum
            show ruby1a e3 t2 
            if gen3 == 1:
                show ruby1a cum2
            with c
            play sound2 cum
            with c
            if gen3 != 1:
                "With some final, graceful movements, she brings me to my release. Cum spraying high and nothing in its path is spared."
            else:
                "With some final, graceful movements, she brings me to my release. Cum spraying from both our cocks as we enjoy a shared orgasm."
            play sound2 cum
            with c
            play sound2 cum
            show ruby1a e3 t0 cum 
            with c
            "I groan in ecstasty as pleasure overtakes my shuddering body. [rub] remains composed throughout, her eyes twinkling with satisfaction as she watches me succumb."
            stop moans1 fadeout 2
            stop ambience1 fadeout 2
            stop music fadeout 10
            if gen3 != 1:
                "After my orgasm settles down, I catch my breath and look up at her with awe."
            else:
                show ruby1a -futa -cum2 with dissolve
                "After my orgasm settles down, I catch my breath and look up at her with awe. It seems the orgasm was actually enough to make her cock disappear."
            mc "You... Didn't spill a single drop."
            "She takes a last sip of her tea, her eyes never leaving mine."
            if gen4 != 1:
                rub "Perfection is an art, darling. And I am nothing if not an artist."
            else:
                rub "Unfortunately, I did spill a lot of milk~"
            play sound2 equip
            scene bg brothel5 
            $ textbox = 1
            with d
            "She slowly rises from the table, her robe falling back into place as if it had never been disturbed."
            "She sets the empty cup on the desk and smiles down at me, her expression serenely content."
            rub "I do hope you enjoyed our little session. Now, would you like another cup of tea? Or perhaps something... stronger?"
            mc "I think I'm ready for anything, as long as it's with you."
            $ energy -= 1
            return
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
    label melodysexscenes:
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
            call genreset from _call_genreset_11
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
                "Futa (Requires Futa Pills)" if futapill == 0:
                    jump melfootjobmenu
                "Futa" if futapill == 1:
                    if gen2 == 0:
                        $ gen2 = 1
                        show mel1a futa with d
                        "[mel] took the pill, and a cock quickly emerged from her crotch and grew to full mast."
                        mel "Haha! It's even bigger than yours!"
                        mel "Although, you know why we mares don't like sleeping with stallions right? These fuckers are uncomfortable inside, and finish extremely fast... Well, not that I'd know personally."
                        mel "I admit, as gross as yours is, it's still better."
                    else:
                        $ gen2 = 0
                        mel "What's wrong? Can't handle a girl with a bigger cock than you?"
                        show mel1a -futa with d
                    jump melfootjobmenu
                "Pregnant (Requires Milky Potion)" if pregpotion == 0:
                    jump melfootjobmenu
                "Pregnant" if pregpotion == 1:
                    if gen3 == 0:
                        $ gen3 = 1
                        show mel1a pregnant with d
                        "[mel] drank the potion and watched in real time as her body swelled up. She was already shocked at the size before milk suddenly spurted from her nipples."
                        mel "You really are a sick fuck, [mc]~"
                    else:
                        $ gen3 = 0
                        mel "You bore~"
                        show mel1a -pregnant with d
                    jump melfootjobmenu
                "(Continue)":
                    pass
            if gen2 == 1 and gen3 == 1:
                mel "Really? Futa and pregnant? That doesn't even make sense!"
            if gen2 == 1:
                mel "Hmm... Let's see how it feels to stroke my cock."
            if gen2 != 1:
                "In addition to wrapping her toes around my shaft and tip, she wastes no time beginning to rub her gorgeous, dripping wet pussy. Her vulva was stunning, and I could feel my cock throbbing and dripping precum at the sight alone." 
            else:
                "In addition to wrapping her toes around my shaft and tip, she wastes no time beginning to rub her new, throbbing cock. The shaft was dwarfed mine, and I could see her hips shaking and instinctively thrusting already."
            show mel1a e2 with d
            if gen2 != 1:
                mel "Staring at my pussy, are you? Tsk, I don't think so."
            else:
                mel "Already loving my new equipment, aren't you? Tsk, if you're lucky, maybe I'll take {i}your{/i} virginity."
            play ambience1 handjob fadein 2
            "With a little more confidence in her toes, she starts to thrust them up and down my shaft."
            play moans2 moansmisc4 volume 0.5
            "In the booth beside us, passionate moans begin to ramp up. Likely from the couple that just walked past us. [mel] casts an annoyed glance, but grins as soon as she realizes she can use this as material to tease me with."
            show mel1a e1 with d
            mel "Right on que. There's no shortage of slutty mares here that can’t resist their baser instincts and impulses. But don’t think for a second that I’ll be fucking you in here. You’re barely good enough for my feet."
            "My cock twitched as her delicate feet massaged my member. I’m surprised she’s able to achieve such precision with them."
            if gen2 != 1:
                "My eyes closed tightly as I leaned back and savored every sensation. Watching my enjoyment, [mel] sped up too, her fingers moving rapidly against her clit as her toes gripped around my shaft and started to jack me off."
            else:
                "My eyes closed tightly as I leaned back and savored every sensation. Watching my enjoyment, [mel] sped up too, her fingers moving rapidly against her cock as her toes gripped around my shaft and started to jack me off."
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
            if gen2 != 1:
                "I groaned louder, my hips bucking forward as my cock throbbed violently and erupted all over her feet, thighs, and even her pussy."
            else: 
                "I groaned louder, my hips bucking forward as my cock throbbed violently and erupted all over her feet. Mere seconds after my own, shockingly, her cock erupted too, splattering us both in yet more cum. She'd done a good job of concealing her own pleasure."
            play sound2 cum
            with c
            play sound2 cum
            with c
            "My body was wracked by wave after wave of mind-numbing pleasure, and albeit subtly, even [mel] seemed to reach an orgasm."
            scene bg brothel3 
            show mel angry cum 
            $ textbox = 1 
            call stopbgs from _call_stopbgs_1
            call camerareset2 from _call_camerareset2_2
            with d
            if gen2 == 1:
                "As she gets up, her cock suddenly vanishes."
            "Finally, as the tremors subsided, I opened my eyes to discover [mel] pouting in front of me, a mixture of annoyance and mischief dancing behind those captivating eyes." 
            if gen2 != 1:
                mel "Ugh, you covered us both in cum again! At least there are tissues in here this time."
            else:
                mel "Tell anyone about this, and I'll make your cock disappear just like mine did!"
                mc "{i}Gulp{/i}!"
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
        label melhandjob:
            mel "Hmph. Come on, then. Let's get to a booth, perv~"
            stop music fadeout 10
            scene bg brothel3 with d
            "As I stepped inside, she closed the curtains behind us and sauntered over to me, her hips swaying with each step."
            mc "Planning something diabolical, no doubt."
            show mel smug with d
            mel "Oh, you’ll see…"
            "She purred, her fingers trailing down my chest, before suddenly prodding me forward and towards the couch."
            mel "Sit down."
            hide mel with dissolve
            play music melodysextheme
            show melody2a e1
            call camerabreath from _call_camerabreath_57
            play moans1 moansmisc2
            $ textbox = 2
            with dissolve
            "I settled into the plush embrace of the couch that anchored the room. She, a figure of undeniable allure, mounted my lap with a deliberate elegance, her thighs spreading wide "
            "She leaned in close, her breath warm against my ear, her lips brushing against my earlobe."
            mel "Want any 'extras'?"
            call genreset from _call_genreset_14
            menu mhandjobm:
                "Goth Clothes":
                    if gen1 == 0:
                        $ gen1 = 1
                        show melody2a goth with d
                        mel "Now we're talking!"
                    else:
                        $ gen1 = 0
                        show melody2a -goth with d
                        mel "We're no longer talking!"
                    jump mhandjobm
                "Pregnant (Requires Milky Potion)" if pregpotion == 0:
                    jump mhandjobm
                "Pregnant" if pregpotion == 1:
                    if gen2 == 0:
                        $ gen2 = 1
                        mel "You are such a pervy, freak weirdo! ... Fine, I'll drink it."
                        show melody2a pregnant with d
                        "[mel]'s body swells up and her nipples begin to squirt milk."
                        mel "You're cleaning that up."
                    else:
                        $ gen2 = 0
                        show melody2a -pregnant with d
                        mel "Aahhh, that's much better."
                    jump mhandjobm
                "Continue":
                    pass
            if brothelroute3 == 1:
                mel "Hm... I could give you another handjob, but I feel like we're past that. Want me to slip it inside?"
            menu mhandjobm2:
                "Vaginal (Unavailable while she's a virgin)" if brothelroute3 == 0:
                    jump mhandjobm2
                "Vaginal" if brothelroute3 == 1:
                    mel "Hehe... Well, well, look who’s eager. You ready for a taste of what I can really offer?"
                    mc "Eager? Maybe. But I’m more curious to see if you can keep up on top."
                    mel "Tsk, tsk. I know we haven't done this often, but this might be my favourite position. Just you wait~"
                    play sound2 cum
                    show melody2a sex1 e2 with d
                    "She began to lower herself onto me, the tight embrace of her body wrapping around me with a deliberate, almost methodical rhythm. Her smug eyes locked onto mine."
                    play ambience1 sex
                    play moans1 moansmisc3
                    "As she took me fully, she started moving immediately. Her hips undulated with a practiced rhythm, the friction inside her pussy was incredible. No matter how good it felt, her grin never wavered as she observed my reactions."
                    "[mel] would never admit this, but I could tell she's been practicing and theorycrafting this, and is excited to put it all in practice. Each shift and turn of her body a testament to her desire for mastery."
                    "Who knew this bully would be such a giver in the bedroom?"
                    show melody2a e1 with d
                    mel "Do you know how lucky you are? Not every guy gets this kind of show. How does it feel to be the center of my attention?"
                    mc "Feels pretty good, but I’m betting you’re just warming up. I’m waiting for the real performance."
                    show melody2a e2 with d
                    "She responds with a coy smile as my smug comment gets under her skin. Obviously, she wasn't warming up, but now she really wanted me to have it!"
                    "As she continued, her pace quickened, the movements becoming more fervent and confident. Her pussy squeezed against my throbbing cock without mercy, the pressure and friction inside her building was euphoric. Her hands gripped my shoulders for support, the connection between us deepened with every thrust."
                    show melody2a e1 with d
                    mel "Hehe, how's this? Can you keep this up, or are you already at your limit?"
                    mc "I’ve got plenty left. If you think you’re pushing me, you might need to try a bit harder!"
                    show melody2a e2 with d
                    "My teasing was exaggerated, she was doing an amazing job and I could still feel myself getting close. However, in an attempt to show me up, she grit her teeth and began to pound me recklessly. Taking full advantage of her equine power, she completely overpowered me."
                    "At this speed, we'd both reach explosive orgasms in no time at all. There was no holding back against the her right now. With each wet smack of our bodies, I could feel myself getting closer to releasing."
                    mel "Ahaha, that's riiight! Cum, c-cum... aahhh, cumming!"
                    play sound2 cum
                    show melody2a cum sex2 
                    show internalcreampie
                    with c
                    play sound2 cum
                    with c
                    "With a final, shuddering release, I was overtaken by the climax, a surge of pleasure that seemed to stretch time itself."
                    play sound2 cum
                    with c
                    play sound2 cum
                    with c
                    "She continued to ride me through the waves of my release, her movements steady and relentless, drawing out every last ounce of cum and pleasure until we were both completely and utterly satisfied."
                    show melody2a -sex1 -sex2 e3
                    hide internalcreampie
                    call aftersex from _call_aftersex_10
                    with d
                    "As the last remnants of pleasure ebbed away, she slowly withdrew, her expression one of quiet triumph and satisfaction."
                    mel "Well, it looks like I won~ Did you enjoy the ride? Or should I say, did I leave you completely spent?"
                    mc "Absolutely. I’ll be coming back for an encore."
                    mel "We'll see, wormy boy~"
                "Handjob":
                    mel "Guess I’m the one holding the reins tonight. Lucky me~"
                    show melody2a hj with d
                    "Her left hand slipped between us. I could feel her fingers brush against my growing erection, sending jolts of pleasure through my body. She began jacking me off, her eyes gleaming with delight at the sight of my hardness."
                    show melody2a e2 with d
                    "She giggled, wrapping her fingers around me. She began to stroke me slowly, her grip firm and confident. She's gotten extremely good at this since the first time, causing me to throw my head back in pleasure."
                    mel "Look at your face. Completely defeated by only my hand! I expected a bit more, you know!"
                    "The strokes quickened, her hand moving with practiced precision. I could feel the heat building between her legs"
                    mel "Feeling a bit overwhelmed, are we? I’m just getting started. You didn’t think I’d let you off that easy, did you?"
                    "She leaned back slightly, giving me a better view of her lithe body as she worked me with her hands. Her eyes never left mine, and her smile grew wider as she saw the effect she was having on me."
                    mel "I have to say, you’re really making this fun. I didn’t realize you could get so stiff and throbby~"
                    show melody2a e1 with d
                    "I could only nod, my breath coming in ragged gasps. [mel]’s touch was driving me crazy, and I was powerless to resist her."
                    show melody2a e2 with d
                    "She increased her pace, her hand moving faster and faster. The friction and the pressure of her closeness were too much to bear. I could feel the tension building inside me, ready to explode at any moment."
                    play sound2 cum
                    show melody2a hj2 cum e3 with c
                    play sound2 cum
                    with c
                    "Her words were the final push I needed. With a shuddering gasp, I felt the climax hit me like a tidal wave. [mel]’s hand never stopped moving, milking every last drop from me as I convulsed beneath her."
                    play sound2 cum
                    with c
                    play sound2 cum
                    with c
                    call aftersex from _call_aftersex_11
                    "As the waves of pleasure subsided, she sat back, a satisfied smirk on her face."
                    mel "Look at you now, all flustered and out of breath over a handy. What if I wanted more? You better not bore me in the future~"
                    mc "I'll rise to tha challenge!"
                    mel "Fuhuhu. We'll see~"
            $ energy -=1
            return
        label melcowgirl:
            mel "Hmph. Come on, then. Let's get to a booth, perv~"
            "As I stepped inside, she closed the curtains behind us and wasted no time reaching for the lube."
            scene black with d
            mc "You're not going to trick me again, are you?"
            mel "Hehe, only if you want me to~ I wasn't expecting to like anal so much in the first place."
            "She coaxed a slow smile from her lips as she took a generous glob of the lubricant. With deliberate care, she smeared it along the length of my erection."
            mel "The real reason I need this, is because my cute, pure hole is too tight for your monstrous cock."
            show melody2b e1 with d
            "Her next movement was to sit directly over me. I could feel the heat between her legs radiating against my erection as they got closer and closer."
            mel "Before we start, anything you want to add?"
            call genreset from _call_genreset_15
            $ gent2 = "hips"
            menu mcowgirlm:
                "Goth Clothes":
                    if gen1 == 0:
                        $ gen1 = 1
                        $ gent2 = "skirt"
                        show melody2b c1 with d
                        mel "Now we're talking!"
                    else:
                        $ gen1 = 0
                        $ gent2 = "hips"
                        show melody2b -c1 with d
                        mel "Doh..."
                    jump mcowgirlm
                "Stockings":
                    if gen4 == 0:
                        $ gen4 = 1
                        $ gen1 = 0
                        show melody2b c3 with d
                        mel "Cute!"
                    else:
                        $ gen4 = 0
                        show melody2b -c3 with d
                    jump mcowgirlm
                "Mini Milk (Requires Milk Potion)" if pregpotion == 0:
                    jump mcowgirlm
                "Mini Milk" if pregpotion == 1:
                    if gen2 == 0:
                        $ gen2 = 1
                        show melody2b m1 with d
                        "[mel] takes a tentative sip of the potion and milk suddenly spurts from her nipples."
                        mel "... That happens so fast, it's kind of scary."
                    else:
                        $ gen2 = 0
                        show melody2b -m1 with d
                        mel "Ahhh, that's better."
                    jump mcowgirlm
                "Mega Milk (Requires Milk Potion)" if pregpotion == 0:
                    jump mcowgirlm
                "Mega Milk" if pregpotion == 1:
                    if gen3 == 0:
                        $ gen3 = 1
                        show melody2b m2 with d
                        "[mel] takes a long swig of the potion and suddenly moans as her breasts heave. Before my very eyes, I watch them enlarge until they completely encompass her chest. And as soon as they do, milk erupts from the teats."
                        mel "Uoohhhh, I wasn't expecting that to feel so good... Nnggh, careful, they're really sensitive."
                    else:
                        $ gen3 = 0
                        show melody2b -m2 with d
                        mel "Phew... That's a load off my chest!"
                    jump mcowgirlm
                "Continue":
                    pass
            mel "And did you decide on one of my lovely, lovely holes~?"
            menu:
                "Vaginal":
                    $ gent1 = "pussy"
                    play sound2 cum
                    show melody2b v1 e2 
                "Anal":
                    $ gent1 = "ass"
                    play sound2 cum
                    show melody2b a1 e2 
            play moans1 moansmisc3
            $ textbox = 4
            with d
            "With the grace of a dancer, she began her descent, my cock gently sinking into her [gent1]. Each inch she lowered herself onto me was a tantalizing assault on my senses."
            "The tightness around my throbbing shaft was amazing, an intense pressure that elicited a groan from deep within. She moved cautiously, her progress marked by the steady rise and fall of her breath, which grew more labored with each inch of movement until my throbbing shaft was completely inside."
            mel "Feeling that? How does it feel now that you're finally snug inside?"
            mc "Snug doesn’t even begin to cover it. You’ve got me feeling like our bodies were made for each other."
            mel "Ew... I'm going to start moving now."
            play ambience1 sex
            camera:
                linear 0.1 zpos -12
                linear 0.4 ypos 6
                linear 0.1
                linear 0.3 ypos -6
                repeat
            "As she began to ride me, the sensation was so consuming that I found myself lost in the experience. The hypnotic rhythm of her movements, the gentle but firm pressure of her body, was mesmerizing. My hands found their way to her swaying [gen2], gripping firmly to steady her so I could start thrusting from below."
            mel "Look at us, moving in sync. Mmmhh, I can't lie, your cock feels pretty fuckin' amazing right now."
            show melody2b e1 with d
            "Her gaze gleamed with a glint of mischief, an enigmatic smile tugging at the corners of her mouth. The rhythmic cadence of her riding did not falter; instead, it took on an even more enthusiastic and confident pace."
            if gen1 == 1:
                show melody2b c2 with d
                "And the faster she got, the more disheveled her clothing became, now giving me a complete view of the penetration as the flaps of her pleated skirt creased upward."
            show melody2b e2 with d
            mel "You’re getting close, aren’t you? I can feel it. Are you ready to let go? Because I’m not slowing down until I get what I want."
            mc "Keep going like this, and you’ll have me filling you up in no time. I hope you’re ready."
            "Her movements grew more intense, her confidence unshaken. The renewed vigor with which she rode me left no doubt of her command over the situation. The sensations were so overwhelming that I was driven to the brink of surrender."
            "But I wasn't the only one drowning under the waves of pleasure, moans were now spilling freely from [mel]'s mouth as she had fully lost herself to the ecstasy. She couldn't care less about teasing me anymore, the only thing that mattered was reaching climax."
            mel "Aaahhhh, I-I won't cum before you do!"
            mc "Nngghh, I... can't hold back anymore! Take it all!"
            mel "Yes, that’s it. Give it all to me, every drop. Good boy!"
            play sound2 cum
            if gent1 == "pussy":
                show melody2b e2 cum v2 with c
            else:
                show melody2b e2 cum a2 with c
            play sound2 cum
            with c
            "As I finally released, she continued to ride me triumphantly, milking my cock for every drop of cum."
            play sound2 cum
            with c
            play sound2 cum
            with c
            "However, seconds later, she was consumed by her own orgasm, losing control of her body as her eyes rolled back."
            call aftersex from _call_aftersex_12
            show melody2b e3 -v1 -v2 -a1 -a2 with d
            "She continued riding me until I was completely spent, and a bit longer than even that. Once finished, she popped my cock out with a satisfied sigh."
            mel "Not bad, not bad..."
            mc "Why are you rating my performance? You were the one on top!"
            mel "Fuhuhu, that doesn't give you an excuse to be a pillow princess~"
            $ energy -=1 
            return
        label melreversecowgirl:
            mel "Hmph. Come on, then. Let's get to a booth, perv~"
            show melody2c e1 with d
            "As soon as we were in the private booth, thirty seconds, no more, and we were in position. Her back to me now, bent over just enough to give a glimpse of ass and pussy, her toes curling in the open air, soft and vulnerable, twitching in anticipation."
            mel "Bet you love this position, since you get a full serving of ass."
            mc "You know it!"
            mel "Want me to wear anything?"
            call genreset from _call_genreset_16
            menu mreversecowgirlm:
                "Goth Clothes":
                    if gen1 == 0:
                        $ gen1 = 1
                        show melody2c c1 with d
                        mel "Once again, we are now talking!"
                    else:
                        $ gen1 = 0
                        show melody2c -c1 with d
                        mel "Come on, why you gotta make me dress and undress all the time?"
                "Pantyhose (Needs Purchasing)" if pantyhose == 0:
                    jump mreversecowgirlm
                "Lingerie (Needs Purchasing)" if lingerie == 0:
                    jump mreversecowgirlm
                "Plug (Needs Purchasing)" if buttplug == 0:
                    jump mreversecowgirlm
                "Pantyhose" if pantyhose == 1:
                    if gen2 == 0:
                        $ gen2 = 1
                        show melody2c pantyhose with d
                        mel "I bet you were thinking that you'd have to rip these. But nah! Mine come pre-ripped. I'm just that kinda girl."
                    else:
                        $ gen2 = 0
                        show melody2c -pantyhose with d
                    jump mreversecowgirlm
                "Lingerie" if lingerie == 1:
                    if gen3 == 0:
                        $ gen3 = 1
                        show melody2c lingerie with d
                        mel "Ahh, cute! Reminds me of the boutique!"
                    else:
                        $ gen3 = 0
                        show melody2c -lingerie with d
                    jump mreversecowgirlm
                "Plug" if buttplug == 1:
                    if gen4 == 0:
                        $ gen4 = 1
                        show melody2c plug with d
                        "[mel] takes the plug and confidently eases it into her pucker herself."
                        mel "You better not turn around and ask me for anal now."
                        mc "Plugs aren't just for tightening your pussy, they can also prepare you for anal."
                        mel "Sure, if I wore it for longer than 30 seconds!"
                    else:
                        $ gen4 = 0
                        show melody2c -plug with d
                        mel "Damnit, what did I just say?"
                    jump mreversecowgirlm
                "Continue":
                    pass
            menu:
                "Vaginal":
                    $ gent1 = "pussy"
                    mel "Mmhh, your wish is my command. Be careful though, you only have two left~"
                    show melody2c v1 e2 with d
                "Anal":
                    $ gent1 = "ass"
                    mel "In that case, let's get a little lube on your pecker of yours!"
                    show melody2c a1 e2 with d
            "She pressed her [gent1] against my tip and let gravity do the work as she gradually adjusted to its girth, she didn't even use a hand to guide herself as she took me with ease, her movements exuding pure confidence. Once I was balls deep, she arched her back and ensured I got the perfect view."
            mel "Enjoy the view, perv~"
            camera:
                linear 0.2 zpos -18 ypos -2 xpos 0
                block:
                    linear 0.05
                    linear 0.5 ypos 8
                    linear 0.05
                    linear 0.4 ypos -8
                    repeat
            play moans1 moansmisc3
            play ambience1 sex
            "Her hips began to rock immediately, putting her entire body into each motion, with even her feet brushing against my thighs. This position didn't just provide an amazing view, but each thrust went to hard, ensuring every inch of my cock and her [gent1] was thoroughly massaged."
            "The point of our connection practically sparked with pleasure, igniting every nerve ending in my body. Before I even knew it, my hips were moving on their own accord, desperate for more pleasure. All while I reached out to tease and squeeze her butt with my hands, a touch she welcomed with a quiver and moan."
            mc "Nngghh, you feel even better today, [mel]!"
            show melody2c e1 with d
            mel "Bitch, I know it~ I'mma squeeze you like a succubus!"
            "Picking up the pace, her movements became more relentlessly. Her body moved in incredible ways, and the way her eyes gazed deeply into mine took my breath away."
            show melody2c e2 with d
            "I could already feel the tension building in my loins, the pleasures intensifying with each deep thrust inside her [gent1]."
            mel "You like watching me take you like this, don't you? I can feel how down bad you are with each throb~"
            "I was unable to muster a reply between my moans and pants. She was in complete control, her every movement pushing me closer to the edge. She shifted slightly, her back arching more, and I could feel her take me even deeper."
            mel "I know you’re close. But I’m not done with you yet!"
            "I clearly wasn’t the only one enjoying it. [mel]’s fingers clenched tighter into my thighs as her lithe frame barely managed to contain the pleasure coursing through it."
            mel "You feel so perfect inside me. I wonder how long I can keep you on the edge."
            "She’d been going at this for a while now, it wouldn’t surprise me at all if she was close to cumming. " 
            mc "I’m getting close again!"
            mel "Good…  Aahhh… Let it all out! Mhh - I want to feel it!"
            play sound2 cum
            if gent1 == "pussy":
                show melody2c v2 cum with c
            else:
                show melody2c a2 cum with c
            play sound2 cum
            with c
            "The intensity of her words and movements pushed me over the edge. With a final a burst of speed, we both reached climax, the pleasure overwhelming. She continued to rock her hips, milking my cock for everything it's worth."
            play sound2 cum
            with c
            play sound2 cum
            show melody2c e1 with c
            mel "Oohhh, f-fuck! Y-You’re still cumming {i}this{/i} much?!"
            play sound2 cum
            with c
            play sound2 cum
            with c
            "As she was cumming, I couldn’t believe how tight her [gent1] got - she was cumming too, and hard!" 
            call aftersex from _call_aftersex_13
            show melody2c -a1 -a2 with d
            "And after I finished unloading, it was obscene how much cum seeped from our point of contact. It’s lucky that [mel] has white fur, really." 
            "As I came down from the high, she slowed her movements, eventually stopping. She looked back at me, a satisfied smile on her face."
            "Although It was clear she was completely spent; panting and weary, her mind reeling from the experience."
            mel "Just... Aahhh, cuddle for five minutes... Too tired to tease you."
            $ energy -= 1
            return
        label melfrombehind:
            mel "The office is empty if you want to... Ah, why am I even asking! Come upstairs with me!"
            show mel3a e1 
            call camerabreath from _call_camerabreath_58
            play music melodysextheme
            play moans1 moansmisc2
            $ textbox = 4
            with dissolve
            "As soon as we were in the office, we transitioned from a passionate kiss to her leaning against the desk. Each movement was fast, needy, as she bent over and revealed her pussy, dripping wet and ready."
            mc "You were this wet already?"
            mel "Tsk, for some reason, I always get like this around you. Your pervy influence, no doubt."
            "Even if she was poised to be the submissive bottom in this position, [mel] always had a way of making herself known. This was no different, as she eased her butt back into my crotch, teasingly grinding her hips against my shaft in an attempt to get me harder faster."
            mel "I'm this wet, and you're not even hard yet? What an insult~!"
            mc "Hey, I'm halfway there!"
            show mel3a e1 with d
            mel "Fuhuhu, while I wait, why don't I try some of the things in your bag?"
            call genreset from _call_genreset_17
            menu mfrombehindm:
                "Lingerie (Needs Purchasing)" if lingerie == 0:
                    jump mfrombehindm
                "Plug (Needs Purchasing)" if buttplug == 0:
                    jump mfrombehindm
                "Pregnant (Needs Milky Potion)" if pregpotion == 0:
                    jump mfrombehindm
                "Lingerie" if lingerie == 1:
                    if gen3 == 1:
                        $ gen1 = 1
                        show mel3a lingerie2 with d
                        mel "Looks like the garter won't fit this massive belly!"
                    elif gen1 == 0:
                        $ gen1 = 1
                        show mel3a lingerie with d
                        mel "What are you doing with such cute lingerie? No, don't tell me, I'm not interested in your hobbies~"
                    else:
                        $ gen1 = 0
                        show mel3a -lingerie with d
                    jump mfrombehindm
                "Plug" if buttplug == 1:
                    if gen2 == 0:
                        $ gen2 = 1
                        show mel3a plug with d
                        "[mel] takes my plug and slips it in with practiced ease. It almost surprises me a little."
                    else:
                        $ gen2 = 0
                        show mel3a -plug with d
                    jump mfrombehindm
                "Pregnant" if pregpotion == 1:
                    if gen3 == 0:
                        $ gen3 = 1
                        show mel3a pregnant 
                        if gen1 == 1:
                            show mel3a lingerie2
                        with d
                        "[mel] curiously takes a sip from a potion in my bag. Unbeknownst to her, it was a pregnancy potion, causing her belly to swell up and breasts to squirt with milk."
                        if gen1 == 1:
                            "Also, the garter popped off! That was quite a surprise."
                        mel "Damn it! Next time I'm making you drink this!"
                        mc "Jokes on you, it has literally no effect on men."
                    else:
                        $ gen3 = 0
                        show mel3a -pregnant with d
                    jump mfrombehindm
                "Continue":
                    pass
            mel "Now... Will I let you put it in my butt?"
            if gen2 == 0:
                "Her voice dropped to a sultry whisper, laced with that teasing edge I knew so well. She lowered herself just enough for my tip to brush against her pucker."
            else:
                "Her voice dropped to a sultry whisper, laced with that teasing edge I knew so well. She lowered herself just enough for my tip to brush against her buttplug."
            show mel3a e1 with d
            mel "Or maybe... should I let it slide in my warm pussy?"
            "Her butt raised again, this time my tip slid against the wet heat of her pussy, the slickness of her desire coating me. Every movement pressed me closer, teasing, threatening to pull me in."
            show mel3a e3 with d
            mel "Oh my~ I just can't make up my mind! [mc], could you decide for me?"
            menu mfrombehindm2:
                "Vaginal":
                    $ gent1 = "pussy"
                "Anal (Needs Lubrication)" if lubrication == 0:
                    jump mfrombehindm2
                "Anal" if lubrication == 1:
                    $ gent1 = "ass"
                    show mel3a -plug with d
                    "With the choice made, I popped her plug out."
            mel "Hehehe, good choice."
            "Her eyes locked on mine, a challenge within them, daring me to take that final step. I reached out, fingers brushing against the soft fur of her butt, and she let out a breathless gasp."
            "She took my hand then, guiding it with a confidence that left no room for hesitation. Together, we aligned my cock with her [gent1], the tip nestled against her entrance, each shift of her hips drawing me closer. I could feel it, the way I sank a little deeper each time she moved."
            "The warmth of her, the way she began to stretch around me, was like nothing else. I could sense her body yielding, growing more desperate, her need palpable. I knew I could slip inside her in an instant."
            show mel3a e1 with d
            mel "You think you can handle me? I bet I could make you beg."
            mc "Just let me put it inside, you tease~"
            play sound2 cum
            if gent1 == "pussy":
                show mel3a v1 e2 
            else:
                show mel3a a1 e2
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
            "Even though she was slick with arousal, her [gent1] was incredible tight, too tight for me to push all the way in. With only half of my cock inside her, I had to take it slow, using shallow thrusts while she eased around my girth."
            mc "Mmm... Is this what you wanted? Because I can give you more."
            mel "Haha come on, then. Show me what you’ve really got."
            "I thrust into her once again, feeling her tighten around my shaft. I loved the way her [gent1] simultaneously yielded and resisted. Her fingers gripped at the desk with an effort to contain the intense pleasure."
            mc "Oh my, don't tell me you're already losing control to the pleasure."
            show mel3a e3 with d
            mel "Hmph~ We'll see who's still in control at the end of this."
            show mel3a e2 with d
            "But I could feel the shift in her. The way her hips started to push back against me, daring me to go deeper, to test the limits of her control. There was a wildness in her now, a rebellion that answered every thrust with a challenge of its own."
            "And in that storm of thrusts, we found a rhythm, a savage harmony. Her [gent1] clenched around me, tight and insistent, refusing to let me go. Her breath came in gasps, each one a small surrender to the pleasure that tore through her."
            mel "Harder... I can take more than this! You know I can."
            "Her voice was desperate, pleading. Her ass pushed back harder, challenging me to go even further. I met her demands, gripping tightly onto her fluffy butt as leverage while I pounded away."
            "Howerver, the faster I got, the more I could feel my own release building, a wave of pleasure threatening to crash over me. But I held on, determined to give her everything she needed."
            mc "Aahhh, I'm starting to get really close!"
            show mel3a e3 with d
            mel "Don’t stop — God, don’t you dare stop."
            "Her eyes locked with mine, wild and desperate, and for a moment, the world stopped. There was nothing but her, nothing but the heat and the need that burned between us. And then it all broke loose. She cried out, her body arching, every muscle tight as the pleasure ripped through her like a storm."
            show mel3a e2 with d
            mel "Uooohhh! Yes—yes, just like that... right there."
            play sound2 cum
            if gent1 == "pussy":
                show mel3a cum v2 with c
            else:
                show mel3a cum a2 with c
            play sound2 cum
            with c
            "That was all it took. I gave in, let the pleasure overtake me, felt it crash through me in waves, relentless and consuming. The tip of my cock erupted, spraying endless amounts of cum deep inside her [gent1]."
            play sound2 cum
            with c
            play sound2 cum
            with c
            "Her body shook against mine as I filled her, still caught in the grip of her orgasm, so fierce it left her breathless."
            play sound2 cum
            show mel3a -v1 -v2 -a1 -a2 e3 with d
            call aftersex from _call_aftersex_14
            "I pulled out and took a moment to admire her flank while catching my breath. She was still trembling, her body quivering from the aftermath of her orgasm."
            mel "{i}Pant, pant{/i} I think I got a little too loud there. I hope [rub] didn't hear." 
            $ energy -= 1 
            return
        label mellegsup:
            mel "The office is empty if you want to... Ah, why am I even asking! Come upstairs with me!"
            play music melodysextheme
            show mel3b e1 
            $ textbox = 5 
            with d
            "As soon as we were in the office, she hoisted herself up the desk. Her hands braced against the wood, and she looked at me with a challenge in her eyes, legs lifted high."
            mel "I really liked this pose. Made it nice and tight. Can we get a repeat?"
            mc "Your wish is my command."
            "I reached in, my hands slid along her thighs as I got into position, my cock mere seconds from being ready to go."
            mel "Let's see what you have in your bag of tricks first. It'd be boring if we just did it like this every time~"
            call genreset from _call_genreset_18
            menu mlegsupm:
                "Lingerie" if lingerie == 0:
                    jump mlegsupm
                "Plug" if buttplug == 0:
                    jump mlegsupm
                "Futa" if futapill == 0:
                    jump mlegsupm
                "Lingerie" if lingerie == 1:
                    if gen1 == 0:
                        $ gen1 = 1
                        show mel3b lingerie with d
                        mel "Aahhh, perfectly gothic!"
                    else:
                        $ gen1 = 0
                    jump mlegsupm
                "Plug" if buttplug == 1:
                    if gen2 == 0:
                        $ gen2 = 1
                        show mel3b plug with d
                        "[mel] takes the plug from me and gently pops it in herself. She's getting shockingly good at that."
                    else:
                        $ gen2 = 0
                    jump mlegsupm
                "Futa" if futapill == 1:
                    if gen3 == 0:
                        $ gen3 = 1
                        show mel3b f1 with d
                        "[mel] takes the futa pill, and before she knows it, she's out of the matrix and now enjoying true reality with her giant horse cock."
                        mel "You'll jack me off, won't you~?"
                    else:
                        $ gen3 = 0
                    jump mlegsupm
                "Continue":
                    pass
            mel "Mmhh... Where do you wanna stick it? Surprise me."
            if gen3 == 1:
                mel "And yes, surprisingly, my pussy is still up there somewhere. Maybe lift up my giant balls to find it~?"
            menu mlegsupm2:
                "Vaginal":
                    play sound2 cum
                    show mel3b v1 e2 with d
                "Anal (Needs Lubrication)" if lubrication == 0:
                    jump mlegsupm2
                "Anal" if lubrication == 1:
                    play sound2 cum
                    show mel3b -plug with d
                    "With the choice made, I popped her plug out."
                    show mel3b a1 e2 with d
            "I lined myself up, her body inviting me to claim her, and then I pushed in, savoring the feeling while she gasped as I filled her once more."
            camera:
                linear 0.1 zpos -12
                linear 0.4 ypos -6
                linear 0.1
                linear 0.3 ypos 6
                repeat
            play ambience1 sex
            play moans1 moansmisc4
            with d
            "I started moving, every inch claimed without resistance. Each thrust drawing a tremor from her lips, her breath hitching. The desk beneath her groaned, straining to keep steady."
            mel "Mmm, so deep... I can feel every inch of you! Ahh, and every twitch too."
            "Her voice was ragged, strained, barely managing the words between the raw sounds our sex. Her legs quivered with the effort to stay raised."
            "Eventually, her body was rocking so much that she struggled to hold her legs up. I lent her a hand and held them up myself, using them as leverage to pound her [gent1] faster."
            mel "Harder... I want more... give me everything you got!"
            mc "Yes, ma'am!"
            "My fingers dug into her fur as I pushed myself, slamming my hips against her butt. In her position it was hard to thrust back, so it was all up to me to push us both to orgasm."
            "But at this point, I'd had more than enough experience bringing these sexy mares to orgasm, and for cases like this, I had a special trick. I reached down and pressed a thumb against her clit, while barely moving it at all, I took advantage of the friction generated from each thrust to fill her with pleasure."
            mel "Uooohhh that's it! Right there!"
            "Works like a charm every time. This one small adjustment sent [mel] from her usual smug charades into mindless ecstasy."
            mel "I’m so close... oh God, I’m right there!"
            "It's almost amazing how well it works sometime. Within only a minute, I could already feel her pussy contracting around my shaft as she came. For me, this was a sign that I could let my guard down and push for my own orgasm."
            "But because I orgasm so frequently, I still need to thrust quite hard and fast to finish off. I completely bullied her [gent1] to reach my climax, leaving her in hysterics as she came harder and harder." 
            "It was hard, sweaty and relentless. [mel]'s orgasm seemed to draw on for almost an entire minute before I finally managed to reach mine and unleashed myself inside of her."
            play sound2 cum
            if gent1 == "pussy":
                show mel3b v2 cum
                show internalcreampie
            else:
                show mel3b a2 cum
            if gen3 == 1:
                show mel3b f2 
            with c
            play sound2 cum
            with c
            "The world narrowed to this moment, to the feel of her, the sound of her, the way she shattered beneath me. She could have orgasmed again, it was too hard to tell because the level of her intensity and passion didn't skip a beat, her pussy mercilessly squeezing me the entire time."
            play sound2 cum
            with c
            play sound2 cum
            with c
            "My release came like a storm, fierce and overwhelming, crashing through me as I thrust deep, holding her close as the pleasure took over. Her name was a moan on my lips, mingling with her own cries of pleasure, our bodies locked together in a final, glorious moments of ecstasy."
            show mel3b -v1 -v2 -a1 -a2 e3 -f1 -f2
            hide internalcreampie
            stop music fadeout 3
            call aftersex from _call_aftersex_15
            with d
            "When it was over, we collapsed together, spent, and breathless, her body still trembling beneath mine. I pulled out of her, feeling the last shudders of my climax."
            mel "That... that was unreal... I’ve never... that was... wow."
            mc "Ahaha, and who's the one always teasing me about being unable to keep up?"
            $ energy -=1 
            return

label hostesssexscenes:
    label rosmissionary:
            play music sextheme
            ros "Aahh, just what I need! Let's go, right now!"
            scene bg brothel3 with d
            "As we arrived at the private booth, I couldn't miss [ros] swooning from the sidelines, her eyes devouring me as I stepped inside."
            play moans1 moansmisc2
            call camerabreath from _call_camerabreath_46
            show rosa1a e1 with d
            ros "I'm so glad you're working here, hunk… I’m not even going to pretend I’m offering this as a host, I just straight up want your cock!"
            ros "Mmmhh... I want you to pump me full of puppies! I need it so bad!"
            "I stood naked before [ros], that irresistible canine goddess. Her fur glistened under the pink lights, inviting me into her soft, warm embrace. Her ample breasts heaved with anticipation, her tail wagging seductively, her eyes sparkling with desire."
            "As I stepped closer, my attention was drawn to the sight of her wet pussy, glistening with anticipation. With eyes on the prize, my erection throbbed with each step."
            ros "{i}Pant, pant{/i} Don’t hold back; I need a good pounding for the heat!"
            mc "Hehe, I can tell, but don’t worry, I know exactly how to make you squeal."
            "Gently, I moved over her on the soft cushions beneath us. Her ample ass lifted off the couch as I positioned myself between her thighs. I could see her quiver as I teased my tip against her engorged clit, sending waves of pleasure through her body."
            ros "Aaaahhhh… I’m ready for you!"
            play sound2 cum
            show rosa1a v1 e2 with d
            play moans1 moansmisc3
            "With a deep groan, I slid inside her, her tight pussy gripping my shaft as I impaled her with a single deep thrust. She was certainly wet and ready!"
            play ambience1 sex fadein 2
            "[ros] let out a loud whine of ecstasy as I began to thrust into her, her hands digging into my back as I claimed her body. The sound of my flesh and her fur slapping together filled the booth as I pumped her hard and deep."
            mc "Mmhhh, your pussy feels fucking incredible! It squeezes so tightly!"
            ros "Uoohhhh… Are you sure it’s not just your cock being massive? You’re filling me up completely! Nngghh!"
            "I reached out, my fingers brushing against her supple fur as I cupped her breasts, feeling her heartbeat race beneath her skin."
            "I could hardly contain my lust as I leaned down, my lips meeting hers in a passionate kiss that left us both breathless. Her tongue danced with mine, tasting of sweet animal desire as her hands found their way up to my neck."
            ros "Mmphhh… {i}Kiss, slurp{/i} Aaahhh, love your kisses~ {i}Kiss, lick{/i}"
            "It was easy to forget that we were in the middle of a club as she enveloped me in her erotic embrace, loudly moaning without a care in the world. Her hefty tits bounced with each powerful thrust, her whines growing louder with each passing moment."
            ros "Uuuuu! I’m getting really close! Aaahhh!"
            mc "Good girl, cum for me! I’m close too!"
            "As I called her a good girl, I felt her wet pussy clenching around my cock, milking me with every spasm of her inner muscles as I plowed into her relentlessly." 
            "I leaned down, my lips finding her ear, nibbling gently as I whispered filthy words of desire. She whimpered her approval, her body arching off the ground as her orgasm ripped through her like wildfire."
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
            ros "Uooohhhh, it feels so warm! Mmh... I can feel it filling me up..."
            "We continued rutting until the heightened pleasure of our orgasms finally faded."
            call stopbgs from _call_stopbgs_32
            call camerareset from _call_camerareset_13 
            play music clubtheme fadein 10
            hide internalcreampie
            show rosa1a -v2 
            with d
            "We lay there entwined, breathless and sated, our bodies glistening with sweat, and our juices mingling."
            "The afterglow of our carnal union enveloped us in a warm, comforting haze."
            scene bg brothel3 
            show ros horny 
            with d
            "And as expected, [ros] bounced up with more energy than ever."
            ros "Perfect, perfect, perfect! You're the best lover I've had! Thank you so much, thank you so much!"
            "She starts kissing me repeatedly, and I do have to wonder if she really means that, or if this is just in her nature as an affable dog. At least she's not licking me - oh, hang on, she definitely just licked my cheek."
            return
    label ros2:
            "[ros]'s tail was wagging before she even saw me, but with her fine sense of smell and hearing, she knew I was here already."
            "When her eyes did finally meet mine, it was with unrelenting brightness and an infectious smile."
            show ros horny with d
            if ros2 == 0:
                ros "Hey, you! I was hoping I'd get to see you tonight."
            else:
                ros "Oooohh, you're here to see me again?!"
            "Her tail was now moving so fast it was a blur."
            "I nodded and handed her the money like it was a mere formality, something required but irrelevant between us."
            "Her eyes flicked down at the bills, and for a moment, her tail stilled. She bagged them quickly, and when her eyes met mine again, the warmth in them burned just a little hotter."
            show ros laughing with d
            ros "C'mon, let's get away from all this!"
            stop music fadeout 15
            scene bg brothel3 with d
            "Her hand gripped mine as she pulled me over to last private booth in the hall. She was infused with boundless energy and excitement, it was impossible to not feel it flow over and seep into you."
            show ros horny with d
            "The second the curtains were pulled shut behind us, I felt her body press against mine, her face nuzzling against my chest."
            ros "You know, I find myself looking forward to seeing you lately."
            "Her fingers traced down my chest, getting lower, lower, lower..."
            ros "I think about you even when I'm not here..."
            "Her fuzzy hand wrapped around my growing erection and began to tug."
            ros "I mean.... you're not like the others."
            ros "Hehe, of course, I'm still in heat... maybe that's why I can't stop thinking about you."
            layeredimage ros2b:
                always:
                    "ros2bb"
                group eyes:
                    attribute e1:
                        "ros2e 1"
                    attribute e2:
                        "ros2e 2"
                    attribute e3:
                        "ros2e 3"
                group cum:
                    attribute cum:
                        "ros2cum"
                group sex1:
                    attribute v1:
                        "ros2v1"
                    attribute a1:
                        "ros2a1"
                group sex2:
                    attribute v2:
                        "ros2v2"
                    attribute a2:
                        "ros2a2"
            show ros2b e1 
            play moans1 moansmisc2
            call camerabreath from _call_camerabreath_59
            $ textbox = 2
            play music sextheme
            with d
            "Once satisfied with my fully erect cock, [rosa] turned without a word, her body lying into the couch with a furred leg lifted up with casual ease."
            "The curve of her ass was soft, inviting. Her eyes were half-lidded, gazing at me longingly."
            ros "Come on, hunk. Don't make me wait~"
            "I moved into position next to her butt. The heat of her body hit me first, radiating off her in waves, especially as I reached down and began to rub her swollen clit."
            "She arched into my touch, her breath hitching and eyes closing to brace herself against the sudden surge of pleasure."
            "Her tail flicked against me, a subtle request for more."
            $ gent1 = "pussy"
            if ros2 == 1:
                ros "Hmm... There's some lube over there. Would you like to try my butt this time?"
                menu:
                    "Vaginal":
                        $ gent1 = "pussy"
                        play sound2 cum
                        show ros2b v1 e2 with d
                    "Anal":
                        $ gent1 = "ass"
                        "I reached over and dripped a generous amount of lube against her tight pucker. The sudden coolness caused her to shiver with anticipation."
                        ros "Ooohh, here we go~!"
                        play sound2 cum
                        show ros2b a1 e2 with d
            else:
                play sound2 cum
                show ros2b v1 e2 with d
            "Angling my cock against her wet entrance, her [gent1] practically sucked me straight inside. She almost howled out in pleasure as she felt herself getting filled up, and I quickly realized why she chose the booth furthest down the hall."
            play moans1 moansmisc4
            play ambience1 sex
            camera:
                linear 0.1 zpos -12
                linear 0.4 xpos -6
                linear 0.1
                linear 0.3 xpos 6
                repeat
            "As I began to thrust, her butt pushed back against me, urging me deeper, faster. There was no adjustment period, no build up, just instant animalistic mating."
            "Every movement of her body was desperate for more. I gripped onto her tightly as I tried my best to deliver. She trembled under the pressure, her cute moans shattering the quiet as her instincts took over."
            ros "I needed this so bad... Nngghh, aahhh... I needed you~"
            "I answered her plea by driving into her harder, deeper, loving the way her [gent1] responded by tightening at the perfect times."
            "The room grew hotter, the scent of our sex thick in the air, mingling with the soft sounds of flesh against fur, and the loud moans of pleasure that escaped her with every thrust."
            "Her body pressed harder into mine, moving faster, more desperate, as if the climax she chased was just out of reach."
            "I could feel it building in her, the tension winding tighter, her breath coming in quick, shallow bursts."
            ros "Uooohhhh, sweet [aur]! I... I can't hold on!"
            "And then she broke, her body tensing, arching against me, a cry spilling from her lips as she reached her peak."
            ros "Aaahhh, [mc]! I'm cumming!"
            "My world seemed to contract in that moment, every sensation heightened, every thrust a step toward the same inevitable end."
            ros "Oooohhhhh, cum inside me! Give me your puppies! Nngghhh!"
            play sound2 cum
            if gent1 == "pussy":
                show ros2b v2 cum with c
            else:
                show ros2b a2 cum with c
            play sound2 cum
            with c
            "And when I felt her tighten around me, felt the shuddering release of her climax, I followed, a wave of pleasure crashing through me, pulling me under."
            play sound2 cum
            with c
            play sound2 cum
            with c
            if gent1 == "pussy":
                "I shot countless loads of virile cum deep into her fertile pussy. If we were sexually compatible, she'd surely get pregnant from this."
            else:
                "I shot countless loads of hot cum deep into her ass."
            show ros2b -v1 -v2 -a1 -a2 e3 
            call aftersex from _call_aftersex_16
            with c
            "After I pulled out, there was nothing but the sound of our panting... That is, until [ros]'s tail began to wag again."
            ros "Aaahhh... You're incredible! I always know it'll be good with you, but... wowsers!"
            "I just held her and enjoyed the afterglow of our passion until we finally parted and made our way to the showers."
            show black with d
            "..."
            if ros2 == 0:
                play sound2 item
                "([ros]'s services are now available at a discount! The anal version of this scene is now available!)"
            $ ros2 = 1
            return
    label cla1:
            if cla1 == 0:
                cla "Oh my, so you really are going to be one of my clients."
            else:
                cla "You enjoyed it so much the first time? I'd be more than happy to serve you again."
            mc "What can I say? The conversation we had earlier sold me on the idea. There's something particularly erotic about the setup."
            show cla wink with d
            cla "Fuhuhu... In that case, come this way."
            stop music fadeout 2
            scene bg bedroom3 with d
            "With amusement lacing her tone, she led me to her sound proof performance room. It was in the opposite side of the building to the other private booths, and a lot more elaborate. This one felt like an five star hotel room."
            "Everything was included, a bathroom with a jacuzzi, a queen sized bed, a variety of furniture designed for certain sex positions. There was even a window with a gorgeous, expansive view of the western side of the city. I could see everything from here."
            "And I suppose I shouldn't have been surprised when I saw the instruments in an adjacent room, polished and gleaming under the low lights."
            mc "I had no idea something like this existed in the brothel!"
            show cla happy with d
            cla "Mhm, everything is included for maximum comfort and privacy. With me, you get what you pay for."
            play music butterstheme1 
            "She sat by a cello, pausing for a moment before she began to play."
            mc "But given that your real position is such a tightly wrapped secret, surely people only come here for the performance."
            show cla happy2 with d
            cla "This isn’t just about the music. It never is."
            cla "People come here, they think they want to hear something, to be entertained. But really, they’re looking for something else. Something they can’t quite name."
            mc "And what is that?" 
            show cla wink with d
            cla "Connection. Understanding. They want to feel something. Anything, really."
            cla "Do you feel the weight of it? How it settles in your chest?"
            "I wasn't entirely sure, but her words alone seemed to manifest something deep inside me."
            show cla horny blush with d
            "[cla] rose from the cello and walked over to me. She stopped in front of me."
            cla "I can give you what you’re looking for, but it's not just in the music."
            "Her hand reached out, fingers brushing my cheek lightly, a touch that felt like it carried more weight than it should have. Her eyes held mine, and for a moment, the room felt like it was spinning."
            show cla happy with d
            cla "You’re not the first to come here like this, and you won’t be the last. But for tonight, this is yours."
            "She leaned in, her breath warm against my skin, and for a moment, everything else fell away... If it wasn't for her pelvis purposely tapping against my erection, I wouldn't have noticed how effortlessly she got me rock hard."
            stop music fadeout 8
            "The music wasn't her performance, {b}this{/b} was her performance. This is the experience I had paid for, and not even an expectation of it was able to fully prepare me for the experience." 
            show cla horny with d
            cla "Do you want this?"
            mc "Y-Yes..."
            show cla wink with d
            cla "Good. Then let's begin."
            scene bg bath with d
            "She took my hand and led me deeper into the bathroom as she began to run the jacuzzi."
            "While it took a few minutes to run, I took the opportunity to appreciate the view from the window. Beyond the class, the city spread out in a tapestry of lights and shadows."
            play music sextheme
            layeredimage cla1:
                always:
                    "cla1b"
                group eyes:
                    attribute e1:
                        "cla1e 1"
                    attribute e2:
                        "cla1e 2"
                    attribute e3:
                        "cla1e 3"
                group cum:
                    attribute cum:
                        "cla1cum"
                group sex1:
                    attribute v1:
                        "cla1v1"
                    attribute a1:
                        "cla1a1"
                group sex2:
                    attribute v2:
                        "cla1v2"
                    attribute a2:
                        "cla1a2"
            show cla1 e1 
            $ textbox = 5
            call camerabreath from _call_camerabreath_60
            play moans1 moansmisc2
            with d
            "[cla] glanced back at me, her eyes glinting with something that wasn't quite desire but wasn't far from it either. Then she bent over, the curve of her body framed by the window, her tail swaying lazily as if to draw my gaze. It didn’t have to work hard."
            "The view outside might’ve been stunning, but the one she offered now took its place, made it irrelevant."
            "I followed her into the jacuzzi, the heat wrapping around us both, sinking deep into my muscles."
            "Her silence continued as I moved closer, my hands leaving her fluffy flank damp as my cock dangled tantalizingly close to her dripping wet pussy. For some reason, the silence combined with her knowing expression just made it even hotter."
            "And I feel like I could have blown my casket right then and there when I felt her butt lean back into me, her pussy slick and warm as it prodded against my shaft."
            $ gent1 = "pussy"
            if ros2 == 1:
                cla "Psst, I do more than just vaginal~"
                menu:
                    "Vaginal":
                        $ gent1 = "pussy"
                        play sound2 cum
                        show cla1 v1 e3 with d
                    "Anal":
                        $ gent1 = "ass"
                        "I followed her eyes and saw some conviniently placed lubrication on the side of the tub. I spread a generous amount of lube against her tight pucker."
                        cla "Mmmhh... Ravish me~"
                        play sound2 cum
                        show cla1 a1 e3 with d
            else:
                play sound2 cum
                show cla1 v1 e3 with d
            "Taking the hint, I angled my cock up, and slid inside. It wasn't like there was a lot of teasing or foreplay, but despite that, the initial experience of filling her up was immensely gratifying and pleasureful."
            play ambience1 sex
            play moans1 moansmisc3
            camera:
                linear 0.1 zpos -12
                linear 0.4 ypos -6
                linear 0.1
                linear 0.3 ypos 6
                repeat
            "I found myself thrusting with an enthusiasm that surprised even me. She'd managed to rile me up and appeal to my male instincts so effortlessly." 
            "She truly was a professional escort in every sense of the word, and I really feel like I could have cum inside her almost immediately. Fortunately, just before I was about to erupt inside her prematurely, she brought me back down to earth with a few words."
            if cla1 == 0:
                show cla1 e1 with d
                cla "Tell me... How is it?"
                mc "Mmhh, amazing! You feel so tight!"
                show cla1 e2 with d
                cla "Hehe, no, I mean... I lead men into this... what we're doing now, with so little effort sometimes. It's a routine I've perfected over time."
                cla "Do you think I did a good job? Was it convincing?"
            else:
                show cla1 e1 with d
                cla "Am I still doing a good job~?"
            "My hands moved to her hips and clung onto them as leverage as I continued to pound her [gent1], causing moans to slip out between her words."
            mc "Nnggh, you're doing a damn good job!"
            "Although, even as I was fucking her, there was something else on my mind now."
            if cla1 == 0:
                mc "But I'm starting to wonder... How much of it's sincere? How much of this is you?"
                show cla1 e3 with d
                cla "Mmhh... It's all me. But not in the way you think."
            "Her body rocked back against mine for the first time, the movements slow at first, causing gentle ripples in the water in contrast to my frantic splashes."
            if cla1 == 0:
                show cla1 e2 with d
                cla "Aahhh, ooohhh... I wouldn't do this if I didn't enjoy it~!"
                cla "But there's more to it... I'd never tell other clients this, but I've got a girlfriend called Ivy."
            else:
                mc "Does your girlfriend know all the details of what you do here?"
                show cla1 e1 with d
                cla "Mhm, every single salacious detail~"
            "Her hips rolled back against me, her movements picking up pace as the pacing built up."
            show cla1 e3 with d
            if cla1 == 0:
                cla "This... what we're doing? It's even more exciting and liberating because of that."
            else:
                cla "She encourages me to recount every experience I have here. She already knows about our first time together."
                cla "Of course, that goes both ways in our relationship~"
            "I could feel the tension around my cock now, the way her [gent1] tightened and relaxed in time with her words, as if she was actively getting aroused as the thoughts alone."
            show cla1 e1 with d
            cla "Aahhh, I love her~ But, this life... being here, mmhhh, it makes me feel truly alive."
            show cla1 e2 with d
            cla "Even if she knows, it's like I'm breaking all the rules."
            show cla1 e3 with d
            "Her words had long began to falter, caught between gasps and soft moans. I gripped her tighter, pulling her closer, feeling her insides tighten around my shaft as our bodies moved harder, faster, the water sloshing around us in waves."
            "Eventually, there were no more words. Just the sound of moaning and waster splashing along with the raw, hot sensation of our passionate sex."
            "[cla]'s movements grew more insistent, her body meeting mine with a wild urgency that seemed to strip away everything else — her practiced poise, her carefully chosen words, they didn't matter now. There was nothing left but the raw, electric connection that pulled us together, each breath growing sharper, each movement more frantic."
            "Until she gasped, her back arching as her body tensed against mine, her orgasm hitting her like a flood."
            play sound2 cum
            if gent1 == "pussy":
                show cla1 v2 cum with c
            else:
                show cla1 a2 cum with c
            play sound2 cum
            with c
            "As her [gent1] twisted and squeezed my cock, I soon followed, my mind melting in a blur of light and heat and my grip on her ass tightening as I let go."
            play sound2 cum
            with c
            play sound2 cum
            with c
            "My grip on her tightened as I lost myself to the bliss. A blur of orgasmic pleasure as I filled her endlessly."
            show cla1 -v1 -v2 -a1 -a2 
            call camerabreath from _call_camerabreath_61
            call stopbgs from _call_stopbgs_38
            with d
            "Only once the pleasure had fully passed, I pulled out and appreciated her flank."
            show cla1 e1 with d
            cla "Fuhuhu. You can wash me clean now~"
            mc "Haha, who said you could drop the act?"
            cla "{i}Pout{/i}"
            mc "Fiiine, stick your butt out."
            show black
            call aftersex from _call_aftersex_17
            with d
            "..."
            if cla1 == 0:
                play sound2 item
                if event3 != 1:
                    "([cla]'s services are now available at a discount!)"
                "(The anal version of this scene is now available!)"
            $ cla1 = 1
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
#Forest
label forestsexscenes:
    label buttailjob:
        scene bg forest2 with d
        "While in the caves again, I'd often see her curvy butt from behind, and I couldn't resist asking to see some more."
        if succ == 1:
            $ gent1 = "succubus"
            show but succ smug with d
            but "Fuhuhu, you want to see my behind again? It's all yours, if you think you can handle it~"
            show but1b wings t1 
        else:
            $ gent1 = ""
            show but happy with d
            but "My rear? Okay, darling, how's this?"
            show but1b
        play music sextheme
        $ textbox = 2
        call camerabreath from _call_camerabreath_62
        play moans1 moansmisc2
        with d
        "She turns her back to me, her movements slow and teasing, as if knowing too well the effect it will have. She leans over a jagged rock, her hands bracing against the rough surface."
        if succ == 1:
            "Her [gent1] tail, a thing that usually sways gently in the air like a lazy pendulum, now curls and flicks with a restless energy. It moves with a life of its own, serpentine, twisting in the space between us, beckoning me closer."
            but "I'll be honest, I've barely been holding back myself... You're such a delectable little treat."
        else:
            "Her tail, usually swaying gently in the air, was curling and flicking excitedly."
            but "Mmmhh... Do you see how wet I am? It's a little embarassing, but I always seem to get like this around you."
        show but1b pp1 with d
        mc "Haha, let's see if I can help with that."
        if succ == 1:
            "There's no hesitation in my movement as I step closer; however subtle, the pull of her succubus powers is still strong."
        "As I close the distance between us, the sight of her body hits me first—her perfect, gorgeous ass framed by the curve of her back, rising as an offering."
        but "Any extras you'd like before we get started?"
        $ gen1 = 0
        $ gen2 = 0
        menu btailjobm:
            "Stockings (Needs Pantyhose)" if pantyhose == 0:
                jump btailjobm
            "Stockings" if pantyhose == 1:
                if gen1 == 0:
                    $ gen1 = 1
                    show but1b stockings with d
                    but "Aahhh, subtle but effective!"
                else:
                    $ gen1 = 0
                    show but1b -stockings with d
                jump btailjobm
            "Plug (Needs Purchasing)" if buttplug == 0:
                jump btailjobm
            "Plug" if buttplug == 1:
                if gen2 == 0:
                    $ gen2 = 1
                    "I reach into our bag of supplies and take out the plug. I press its cold metal tip against her anus until it relaxes and pops in."
                    show but1b plug with d
                    but "Ooohhh... That's going to make it feel so much tighter."
                else:
                    $ gen2 = 0
                    show but1b -plug with d
                jump btailjobm
            "Continue":
                pass
        but "And I suppose there's only one more thing to consider."
        menu btailjobm2:
            "Vaginal":
                $ gent2 = "pussy"
            "Anal (Needs Lubrication)" if lubrication == 0:
                jump btailjobm2
            "Anal" if lubrication == 1:
                $ gent1 = "ass"
                if gen2 == 1:
                    show but1b -plug with d
                    "Before I get to business, I pop the plug back out of her ass. It was in just long enough for her to be ready for my cock."
            "Tail Job (Succubus Only)" if succ == 0:
                jump btailjobm2
            "Tail Job (Succubus Only)" if succ == 1:
                show but1b -t1 t2 with d
                play sound2 darkness
                with p
                "I can immediately feel her charming [gent1] touch flow through me, enhancing all my pleasure sensors."
                "Even a tailjob from a succubus can be one of the most pleasurable thing you’ll ever feel."  
                play ambience1 handjob2
                camera:
                    linear 0.2 zpos -12
                    block:
                        linear 0.4 ypos 6
                        linear 0.3 ypos -2
                        repeat
                "But I don’t have time to think on it long. Her tail begins to move, its soft caresses and firm strokes expertly calibrated to pull me deeper into the sensation, coaxing out pleasure with each motion. It’s a rhythm that she sets, and I follow, powerless to resist."
                mc "Mmhh, that feels incredible."
                "I can’t help it, the sound escapes me as her tail works its magic. My body tingles, alive with both natural and unnatural pleasures. It’s overwhelming, a flood of sensation that threatens to sweep me away."
                "Through her motions alone, I can feel the pull of her hunger, the way her need claws at the edges of her restraint."
                but "Aahhh, I can't wait to drink up your energy, [mc]."
                "Her voice is breathy, filled with both urgency and a strange kind of relief. I grit my teeth, fighting to stay present, but it’s a losing battle."
                mc "I won't hold back. As soon as I’m about to cum, I'll let it blast all over your fine ass."
                but "Oooohh, don't threaten me with a good time~!"
                "Her tail moves faster now, its rhythm inhuman, and with it, the pleasure builds, swelling inside me like a tide that can’t be held back. It rises higher and higher until there’s nothing left but the intensity of it, and then—"
                mc "That’s it! I’m about to cum!"
                play sound2 cum
                show but1b pp2 cum with c
                play sound2 cum
                with c
                "The release hits me like a storm, a wave of pleasure so intense it takes my breath away. My cum spills freely from me, thick and hot, coating her ass in ropes of white, the energy of it pouring out in a rush."
                play sound2 cum
                with c
                play sound2 cum
                with c
                " Every drop is soaked up by her skin, as if her body were starving for it. The glow of satisfaction that washes over her is immediate, her eyes gleaming with renewed strength as she absorbs it all."
                "Her body shudders as the last of my release is taken in, and for a moment, there’s silence between us, broken only by the sound of our heavy breathing."
                stop ambience1 fadeout 2
                stop moans1 fadeout 2
                call camerareset from _call_camerareset_17
                show but1b -pp2 -pp1 -t2 t1 with d
                mc "{i}Pant, pant…{/i} How was that?"
                scene bg forest2
                show but horny succ blush
                camera:
                    ypos -150 zpos -400
                with d
                "The glow of satisfaction is in her eyes, yes, but I could tell that the night was long from over."
                but "That'll keep me sated... for now~"
                but "But first, let's finish here and return home, shall we?"
                $ energy -= 1
                return
        "She’s waiting for me to make the next move, and I’m not one to disappoint. I pull her closer, my hands gripping her waist as I get into position. The soft, desperate moan she makes in reaction is enough to send a shiver down my spine."
        play sound2 cum
        if gent2 == "pussy":
            show but1b v1 -pp1 with d
        else:
            show but1b a1 -pp1 with d
        "I pressed my cock against her [gent2] and slowly eased myself in, my body taking over as instinct pushes everything else aside. The heat inside her is amazing, pulling me deeper, until all I can think about is her."
        play moans1 moansmisc3
        play ambience1 sex
        camera:
            linear 0.1
            linear 0.4 ypos -6
            linear 0.1
            linear 0.3 ypos 6
            repeat
        "All that’s left is the feeling of her [gent2] wrapped around me, the sound of her breath quickening as I begin to move."
        "Mmmhhh, your [gent2] feels incredible!"
        "She’s panting now, her breaths ragged as the tension in her body builds."
        if succ == 1:
            but "Oh, your fat cock feels absolutely perfect. Don't stop... just keep going like that!"
        else:
            but "Mmhh, sweetie... You feel so perfect. Please don't stop~"
        "I lipbite back a groan, my mind swimming in the sensations, but her words keep me anchored."
        if succ == 1:
            but "Faster… don’t you dare hold back now. Give me every drop of energy you’ve got."
        else:
            but "You don't need to hold back for me, sweetie. Give me everything you can."
        "Her movements speed up, urgent for pleasure, her hips rocking back against me with a force that matches my own. It's a real testament to her surprising agility and strength that she can keep up pace from below like this."
        if succ == 1:
            "Succubus magic surges through me, enhancing every single sensation while invigorating my movements with unfounded strength and speed. I truly couldn't stop even if I wanted to."
        else:
            "Even though she's not in her succubus form, I can feel faint tinges of the magic reverberate through me, empowering my movements and enhancing the pleasure. Perhaps this is a capability of 'normal [but]' that only comes out during sex?"
        "The passion between us builds like a wildfire, spreading fast, until the pleasure is all-consuming. Each thrust brings me closer to the edge, the air thick with the smell of sweat and sex."
        if succ == 1:
            but "Ooohhhh! Right there, yes — I'm almost there. Don’t let up now, I need this!"
        else:
            but "Aaahhh! Right there, sweetie! Mmmhhh, mommy is getting really close! {i}Pant, pant{/i}"
        "The pleasure climbs, higher and higher, until it reaches that point of no return, and there’s nothing left to do but let it take me."
        but "Uooohhhh I’m cumming, I can’t hold it—oh, yes... yes!"
        mc "Aahhh, I'm cumming too!"
        play sound2 cum
        if gent2 == "pussy":
            show but1b v2 cum with c
        else:
            show but1b a2 cum with c
        play sound2 cum
        with c
        "The release hits like a tidal wave, crashing through me with a force that leaves me gasping. My body shudders, the sensation ripping through every nerve as I spill myself inside her, my hands still gripping her hips tight as I ride out the last waves of pleasure."
        play sound2 cum
        with c
        play sound2 cum
        with c
        "She lets out an intensely satisfied moan, her entire body shaking as she feels the warmth of my release, upgrading her own orgasm from mere pleasure to pure full-bodied ecstasy."
        show but1b -v1 -v2 -a1 -a2 cum 
        call aftersex from _call_aftersex_18
        with c
        "There’s a moment of stillness, the only sound our heavy breathing, the world outside slowly creeping back in. Her body softens against me, her muscles finally relaxing as the tension drains away. I can feel her fur cooling beneath my touch, the fire in her dulled, but not extinguished."
        mc "How are you feeling?"
        if succ == 1:
            but "Satisfied for now, I think~ Hehehe."
        else:
            but "It felt amazing, [mc]. Although I do think I'd rather partake in such activities in the bed, yes? Hehe."
        "Her smile widens, playful, but there’s no mistaking the truth behind it. This was only the beginning, and whatever fire I'd just stoked, it wasn’t done burning yet."
        call aftersex from _call_aftersex_19
        $ energy -= 1
        return
    label butblowjob:
        stop music fadeout 3
        scene bg forest2 with d
        "While in the caves again, we wandered through an area of aphrodisiacal activity, causing me to get a slight erection. This 'slight' erection quickly turned hard when [but] turned her attention to it."
        if succ == 1:
            show but succ smug with d
            but "Fuhuhu, you think I'm going to let you off that easy? Come here~"
            show but1c succ e1 
        else:
            show but happy with d
            but "It's okay, sweetie. Let mommy help."
            show but1c e1 
        play music sextheme
        call camerabreath from _call_camerabreath_63
        play moans1 moansmisc3
        $ textbox = 3
        with d
        "Her eyes locked onto mine for just a moment, something feral and vulnerable flickering in the depths of them before she sank slowly to her knees."
        "Each movement lower was graceful in its submission, yet there was nothing weak about it. The shadow of my cock fell across her face as she knelt before me, her lips parted. The sight of her like this, a power in her vulnerability, was all the convincing I needed to go through with this."
        play ambience1 blowjob
        "She looked up, her gaze never leaving mine as she leaned forward, her mouth open, her tongue flicking out to taste my precum."
        if succ == 1:
            "The warmth of her lips around my tip sent a jolt of succubi magic through my body, a slow-burning fire that spread out from my core, igniting everything in its path."
            but "Fuhuuh. I can feel you trembling already... does it really feel that good?"
        else:
            "The warmth of her lips around my tip sent a jolt of pleasure through my body, a slow-burning fire that spread out from my core, igniting everything in its path."
            but "Mmmhh... You're so tense... let mommy take care of everything."
        "Her tongue moved in slow circles, generating a pleasure so deep I could feel it in my bones."
        mc "Mmhh! Oh, god, that’s good."
        show but1c e2 with d
        "She moved with hunger, her lips and tongue working with a rhythm that felt both practiced and instinctual, like she was born knowing exactly how to drive a man to the brink."
        if succ == 1:
            but "Aahhh... I love how you react to me, like you're losing control. Well, thanks to my magic, I suppose you have~"
        else:
            but "Every time I touch you like this, you get even harder... it's addictive."
        "The cave around us seemed to dissolve, the walls fading into darkness, the world shrinking until all that existed was her mouth, her touch, the heat between us."
        "It was overwhelming, the sensation of her lips sliding up and down my throbbing shaft, her tongue flicking the underside of my glans in perfect time with the pressure building inside me, each moment bringing me closer to the point where I couldn't hold back anymore."
        mc "[but], I-I'm getting close…"
        "She didn't pause, didn’t slow, only hummed around me, the vibration of it sending a shockwave through my entire body."
        if succ == 1:
            but "I want all of your energy... don’t hold back on me now."
        else:
            but "I can feel how close you are? It's okay, you can just let go inside my mouth."
        play sound2 cum
        show but1c cum with c
        play sound2 cum
        with c
        "My climax hit me like a freight train, the release tearing through me. Her lips pulled away just in time, and I felt the warm rush of release coat her face, her chest, her backside. She didn't flinch, didn’t shy away—if anything, she seemed to welcome it, her eyes closed in something like reverence."
        play sound2 cum
        with c
        play sound2 cum
        with c
        "But she didn’t stop, not yet. Her mouth found me again, her lips and tongue working with a new urgency, a determination to milk every last drop from me, to pull every ounce of pleasure I had left."
        play sound2 cum
        with c
        play sound2 cum
        with c
        "It was too much—too intense—and I could feel the pleasure edging into discomfort, the kind of raw sensitivity that makes your muscles twitch and ache."
        call aftersex from _call_aftersex_20
        if succ == 1:
            "As a succubus, she was relentless, though, her hunger insatiable, her powers pushing me beyond the point where I could handle it. My body trembled, overstimulated, every nerve on fire."
            mc "Ngghh, [but] that’s… that’s enough!"
        else:
            "However, unlike her succubus side, she knew when to hold back."
        "She pulled away, finally, her breath ragged, her face flushed and glistening in the low light of the cave."
        if succ == 1:
            but "Aahh... So delicious! That's just the boost of energy I needed to get through the rest of today."
        else:
            but "Mmmmhh... Cum isn't supposed to taste this good, is it?"
            mc "I've heard it's terrible, but maybe your succubi side is enough to influence your taste buds."
            but "I do wonder just how close this form is to my succubus one. I hope it isn't possible for them to both fully corrupt into full succubi."
        $ energy -= 1
        return
    label butpaizuri:
        stop music fadeout 3
        play music sextheme
        if succ == 1:
            but "You'd like to service me with your breasts? Mmmmhh... Don't mind if I do~"
            scene but2c succ e1 
            show night:
                alpha 0.15
                blend "multiply"
            show red:
                alpha 0.15
                blend "multiply"
        else:
            but "Of course, darling. Just sit down and leave everything to me."
            show but2c e1 
        call camerabreath from _call_camerabreath_64
        play moans2 moansmisc2
        $ textbox = 4
        with d
        "Her breasts grazed against my hips as she positioned herself beneath me. There was a reverence to the way she touched me, a softness in her fingers, her eyes never leaving mine." 
        "The fire between us burned hotter than the cauldron, but it was tempered by a tenderness, a connection that felt as much spiritual as it did physical."
        if succ == 1:
            but "Hehe, did I really make you this hard already? Mmmhhh... You really know how to spoil a girl."
        else:
            but "I can already tell... you’ve been needing this, haven’t you? Let me make you forget everything, just for a little while."
        but "Is there anything else you'd like before we go any further?"
        call genreset from _call_genreset_19
        $ gent2 = "cock"
        menu bpaizurim:
            "Milky (Requires Milky Potion)" if pregpotion == 0:
                jump bpaizurim
            "Horsecock (Requires Lewd Spellbook)" if lewdspellbook == 0:
                jump bpaizurim
            "Milky" if pregpotion == 1:
                if gen1 == 0:
                    $ gen1 = 1
                    but "Ah, I recognize this potion anywhere! I hope you won't mind all the extra mess."
                    show but2c milk with d
                    "[but] drinks a single dose and within seconds her breasts spray with milk."
                    but "Wow! The potion wasn't this fast acting back in my day."
                else:
                    $ gen1 = 0
                    show but2c -milk with d
                jump bpaizurim
            "Horsecock" if lewdspellbook == 1:
                if gen2 == 0:
                    $ gen2 = 1
                    $ gent2 = "horsecock"
                    but "What a novel idea. Let's try it!"
                    show but2c horse with d
                    "[but] uses a magical catalyst and tries the spell for herself. It takes a little trial and error, but before I know it, I have a raging horse cock."
                else:
                    $ gen2 = 0
                    $ gent2 = "cock"
                    show but2c -horse with d
                jump bpaizurim
            "Continue":
                pass
        show but2c e2 
        play ambience1 handjob2
        camera:
            linear 0.1
            linear 0.4 ypos -6
            linear 0.1
            linear 0.3 ypos 6
            repeat
        with d
        "Her voice was a soft murmur, a contrast to the intense heat between us. She adjusted herself, her breasts pressing around my [gent2], enveloping it in their warmth. Her hands cupped them, pressing them closer, creating a snug, almost perfect fit."
        "The sensation was exquisite. Her fur was so soft in a way that felt both comforting and electric. The rhythm of her movements was slow at first, unpracticed, as she was getting used to these unique movements." 
        "But what she lacked in technique, she made up for in enthusiasm, and there was something almost maternal in the way she approached the task. She was patient, each motion deliberate, calculated to bring me the most pleasure."
        show but2c e1 with d
        if succ == 1:
            but "I can tell by your breathing. You reeaally like this, don’t you? Ahaha, let's keep going!"
        else:
            but "So soft, so warm. You’re melting right into my hands. I love how responsive you are."
        "It wasn’t long before her movements became smoother, more fluid. Perhaps it was her nature, the succubus in her coming alive, taking over as she learned how to work my [gent2] like it was a wind instrument."
        "Her hands pressed her breasts tighter around me, and the friction of her fur against my shaft was almost unbearable in its sweetness. Her eyes stayed locked on mine, studying my reactions, watching for every little tremor and shudder with a mix of curiosity and affection."
        but "You look so cute right now… Mmhh…"
        "The room was filled with the soft sounds of her steady breathing, punctuated by the occasional hum of satisfaction. My own breaths came quicker now, each one hitching in my throat as she moved faster, the pressure building with every stroke."
        "I couldn’t hold back the moans that slipped from my lips, each one pulled from me with every push and pull of her body. She had always been skilled in her craft, like any succubus worth her name, but this time there was something more, something deeper. The affection in her touch, the care in her movements, elevated everything."
        if succ == 1:
            but "Mmm, there we go. You’re starting to feel it now, aren’t you? Why don't we add a little more of my succubus magic into the mix~ {i}Zap{/i}"
        else:
            but "That’s it, honey. Breathe with me. I can feel how close you are. Don’t rush, take your time. Let it all build up slow. You deserve to savor this moment."
        show but2c e2 with d
        "Her words were a balm, their softness wrapping around me just as tightly as her body, and I felt the last of my control slip away. Her movements quickened, more fervent, her hands pressing her breasts tighter around my [gent2] as I reached the brink." 
        "There was no hesitation in her now, no doubt. She knew exactly what I needed, and she was going to give it to me."
        if succ == 1:
            but "Come on, don’t hold back! I know you’re close. Don’t try to hide it from me. I’ve got you wrapped around my finger, and you love it, don’t you?"
        else:
            but "Almost there, my sweet. Just a little more. I’m right here with you, feeling every bit of you. You're so strong, so beautiful. Let it happen when you’re ready."
        play sound2 cum
        if gen2 == 1:
            show but2c c1 c2 with c
        else:
            show but2c c1 with c
        play sound2 cum
        with c
        "The release, when it came, was sudden and all-consuming. I gasped, my body shuddering, my mind lost to the pleasure. Her movements never faltered, her voice a constant hum of encouragement as the last waves of my climax rolled through me."
        play sound2 cum
        with c
        play sound2 cum
        call camerabreath from _call_camerabreath_65
        with c
        "She continued fucking me with her breasts through it, even as they got repeatedly splattered with cum."
        if succ == 1:
            but "That’s it, let it all out. Every last drop, just for me. You were so easy to break, weren’t you? I knew you couldn’t last long."
        else:
            but "There we go, good boy. Let it all out, every last bit. You’ve done so well for me."
        show but2c e3 with d
        call aftersex from _call_aftersex_21
        "When it was over, she looked up at me, her expression one of quiet satisfaction. There was a hint of amusement in her eyes."
        mc "You really enjoy doing that, don't you?"
        but "Hehe, it's growing on me."
        $ energy -= 1
        return
    label butdoggystyle:
        if succ == 1:
            but "Fuhuhu, you don't have to ask twice."
            scene but2b succ e1 
        else:
            but "Oh my! It's such a lewd pose, but... it'll be okay."
            scene but2b e1 
        call camerabreath from _call_camerabreath_66
        play music sextheme fadein 3
        play moans1 moansmisc2
        $ textbox = 2
        with d
        call genreset from _call_genreset_20
        "Turning her back to me, she sank onto the bed. Her back arched elegantly, her head bowed, and her rounded, plush ass was presented high. It was a posture as old as time itself, embodying a blend of submission and demand that held its own timeless allure."
        if succ == 1:
            but "Ready for a little fun? I promise you won’t be disappointed."
        else:
            but "Is this okay, dear? I want everything to be just right for you."
            mc "It's perfect. You're perfect."
        menu bdoggym:
            "Stockings (Needs Purchasing)" if pantyhose == 0:
                jump bdoggym
            "Plug (Needs Purchasing)" if buttplug == 0:
                jump bdoggym
            "Thong (Needs Lingerie)" if lingerie == 0:
                jump bdoggym
            "Pregnant (Needs Milky Potion)" if pregpotion == 0:
                jump bdoggym
            "Stockings" if pantyhose == 1:
                if gen1 == 0:
                    $ gen1 = 1
                    show but2b stockings with d
                    but "Very cute!"
                else:
                    $ gen1 = 0
                    show but2b -stockings with d
                jump bdoggym
            "Plug" if buttplug == 1:
                if gen2 == 0:
                    $ gen2 = 1
                    show but2b plug with d
                    "I gently pressed the tip of the plug against her pucker, and she eased around it until it slipped in."
                    but "Mmmhh... It feels better than I thought."
                else:
                    $ gen2 = 0
                    show but2b -plug with d
                jump bdoggym
            "Thong" if lingerie == 1:
                if gen3 == 0:
                    $ gen3 = 1
                    show but2b thong1 with d
                else:
                    $ gen3 = 0
                    show but2b -thong1 with d
                jump bdoggym
            "Pregnant" if pregpotion == 1:
                if gen4 == 0:
                    $ gen4 = 1
                    but "Ah, I recognize this potion anywhere! If this is something you like, I don't mind drinking it."
                    show but2b pregnant with d
                    "[but] drinks a single dose and within seconds her belly swells up and her breasts drip with milk."
                    but "Wow! The potion wasn't this fast acting back in my day."
                else:
                    $ gen4 = 0
                    show but2b -pregnant with d
                jump bdoggym
            "Continue":
                pass

        but "If you're ready.. Mmhhh, take me~"
        "It was a voice that bore no command, but rather a plea born of deep, unspoken need. It was as if the very air was charged with her desire, thick and palpable."
        if succ == 1:
            "The murmur of her need echoed through me. I felt a pull that was more than physical, as if her succubi magic was reaching out, its tendrils creeping through the haze of my thoughts. It was a subtle invasion at first, almost imperceptible, but it soon swelled into a relentless and inevitable force."
            "Her magic entwined with my very essence, blurring the lines between my own wishes and her demands until they merged into a singular, undivided drive."
        else:
            "The murmur of her need echoed through me. I felt a pull that was more than physical. Even if it was weaker in this form, her succubi magic reached out, its tendrils creeping through the haze of my thoughts."
        "As I advanced towards her, my hands sought the firm curve of her ass, her body trembling beneath my touch as if it had been in waiting for an eternity."
        "Her body responded with an eagerness that bordered on desperation, pressing back against me with a fervor that left no room for subtlety."
        if succ == 1:
            "Her magic, once a gentle caress, now tightened its grip on my psyche, entwining around my thoughts and pulling me ever closer to her. Each movement of her body was a command, a plea wrapped in the guise of passion."
        else:
            "Her magic, subtle as it was in this form, tightened its grip on my psyche, entwining around my thoughts and pulling me ever closer to her. Each movement of her body was a command, a plea wrapped in the guise of passion."
        if succ == 1:
            but "Go on, don’t be shy. Show me how badly you want me. How badly you need me~"
            but "Say, if you have some lubrication, I hear succubi are just as effective from the back door if you're feeling adventurous."
        else:
            but "Whenever you’re ready, darling. I want you to feel every bit of the warmth and pleasure I have to offer."
            but "Oh, and, uhm... Where do you want to put it?"
        menu bdoggym2:
            "Vaginal":
                $ gent1 = "pussy"
            "Anal (Needs Lubrication)" if lubrication == 0:
                jump bdoggym2
            "Anal" if lubrication == 1:
                $ gent1 = "ass"
                if gen2 == 1:
                    show but2b -plug with d
                    "Before I get to business, I pop the plug back out of her ass. It was in just long enough for her to be ready for my cock."
        if gen3 == 1:
            show but2b thong2 with d
            "I take the strap of her thong and slip it out of the way. Her wetness is obvious as it leaves a trail."
        play sound2 cum
        if gent1 == "pussy":
            show but2b v1 e2 with d
        else:
            show but2b a1 e2 with d
        "I watched as my hand wrapped around my cock, aligning it with her waiting [gent1]. Despite the wetness, her entrance was initially tight, a barrier that yielded only after a firm push. As I pressed forward, her folds parted slowly, granting me entry into the depths."
        "As my shaft sank into her depths, and the world seemed to fall away. There was nothing but the feel of her, the heat of her, the way her [gent1] clenched around my cock, her insides pulling me deeper, urging me on." 
        but "Uuoohhh, I’ve waited so long for this… It’s perfect, just like I dreamt."
        mc "Don’t you worry, I’m going to make all your dreams come true."
        camera:
            linear 0.1
            linear 0.4 xpos -6
            linear 0.1
            linear 0.3 xpos 6
            repeat
        "I began thrusting immediately – wouldn’t have been able to stop myself if I tried, and it was more than just the magic that contributed to that. The feeling of her [gent1] was euphoric, gracing every inch of my shaft with unparalleled bliss."
        "Her body clenched around my shaft, pulling me deeper and urging me."
        if succ == 1:
            "Deep inside her, the flare of her succubus power surged anew, a vibrant energy that coursed through me and heightened every sensation. Each touch, each movement, was magnified, made more intense. Her control was absolute, guiding the rhythm and pace, leaving just the two of us locked in an all-consuming dance."
        if succ == 1:
            but "Almost there already, huh? I can see it in your eyes. Don’t hold back now~"
        else:
            but "I'm so close now, my dear. Just let go and fill me up~ Being filled by you is more than enough to push me over the edge."
        play sound2 cum
        if gent1 == "pussy":
            show but2b cum v2 
        else:
            show but2b cum a2
        show internalcreampie
        with c
        play sound2 cum
        with c
        "The first wave of my climax came with a ferocity that was almost explosive, splattering her insides white. It that took everything I had and left me trembling in awe."
        play sound2 cum
        with c
        play sound2 cum
        with c
        "It was a raw, unfiltered eruption that crashed over me, sweeping me away in its wake. And she absorbed it all, her body drinking in every drop with a hunger that seemed insatiable."
        play sound2 cum
        with c
        play sound2 cum
        with c
        "As she came it seemed to draw even more from me, like her innate powers were artificially extending my orgasm just to squeeze as much from me as she could."
        hide internalcreampie
        show but2b e1 -v1 -v2 -a1 -a2 
        call aftersex from _call_aftersex_22
        with c
        "When I finally managed to pull out, it was with an additional spray of cum all over her fluffy butt. I only just managed to fight the pull of her succubi powers flaring up and preparing to start a second round."
        if succ == 1:
            but "Awh, and I was just getting started~"
            mc "{i}Pant, pant{/i} If you paced me, you can get more of me. You know that."
            but "{i}Pout{/i} But I want you all now!"
        else:
            but "Oh dear! It seems I got a little carried away there."
            mc "{i}Pant, pant{/i} That's okay! I still enjoyed every second of it."
        $ energy -=1 
        return
#Bakery


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
        "[mox] was a little more hesitant, but quickly got over it to start focusing on my balls. Her warm breath sent shivers down my spine as she licked them softly with the tip of her tongue before engulfing them completely into her mouth."
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
        "Their equine tongues were considerably larger than a humans', with a slightly rougher texture that combined a wider surface area with a constantly higher stimulation. I’d almost say it felt twice as good, and I was dealing with two girls at once!" 
        pen "God, the smell is intoxicating."
        "Subtly under the sounds of their tongues were the wet sounds of masturbating, as both girls began to pleasure themselves. [pen] sank two fingers deep into her pussy and curled them upwards to tease at her g-spot, while [mox] rubbed her needy clit back and forth."
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