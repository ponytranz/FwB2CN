label farm:
    hide screen worldmap
    show screen vnui
    if farmroute1 == 0:
        jump farm1
    play music honeycrisptheme fadein 1
    scene bg farm4
    if weather == 4:
        show rain1:
            alpha 0.1
    with d
    menu farmmenu:
        "Work":
            jump farmwork
        "Visit [hon]":
            scene bg farm2 with d
            show hon happy
            with d
            menu honmenu:
                "Sex":
                    hon "Now you're talking!"
                    menu honsexmenu:
                        "Energy: [energy]"
                        "No Energy Left" if energy <= 0:
                            "I feel exhausted!"
                        "Thighjob" if energy > 0:
                            call honthighjob from _call_honthighjob
                        "Back":
                            show hon happy with d
                            hon "Y'all a tease!"
                    jump honmenu
                "Back":
                    scene bg farm4 with d
                    jump farmmenu
                "Leave":
                    jump worldmap
        "Visit [blo]":
            scene bg farm3 with d
            show blo happy
            with d
            if farmroute2 == 0:
                show blo bashful blush with d
                "Y-You uhm, got my m-message, right?"
            menu blomenu:
                "Yeah, I got your message (In Development)":
                    jump blomenu
                "Sex":
                    menu blosexmenu:
                        "Energy: [energy]"
                        "No Energy Left" if energy <= 0:
                            "I feel exhausted!"
                        "Buttjob" if energy > 0:
                            call blobuttjob from _call_blobuttjob
                            scene bg farm3 with d
                            show blo happy
                            with d
                        "Back":
                            show blo happy with d
                            mel "Oh, okay then!"
                    jump blomenu
                "Back":
                    scene bg farm4 with d
                    jump farmmenu
                "Leave":
                    jump worldmap
        "Replay Events":
            menu:
                "While replaying, you can return at any time using the phone."
                "Farm Visit 1":
                    $ gen3 = 10
                    $ replay = 1
                    show screen vnui
                    call farm1 from _call_farm1
                    $ replay = 0 
                    jump farm
                "Back":
                    jump farmmenu
        "Leave":
            jump worldmap
    jump farmmenu
label farm1:
    show screen vnui
    play music citytheme
    stop ambience1 fadeout 1
    scene bg city2 with d
    "The walk to the farm feels so much longer than usual. Instead of a relatively direct path in a modest village, I’m having to take various lefts and rights through dense urban sprawl."
    stop music fadeout 10
    scene bg farm1 with d
    "But once I finally get out of that cityscape, I have the glorious view of rolling hills and towering mountains as my reward. Without all the buildings in the way, I can also finally see the sunset, and it's a beautiful thing."
    "The farm in the distance looks identical; the buildings are all in the same places. The first building I pass is the barn, and even though it’s quite late, I can hear someone shuffling inside."
    "Seems like a good opportunity to introduce myself, so I pop my head in."
    scene bg barn1 with d
    "The barn is dense with a variety of farming equipment, produce, and stored materials, making it difficult to notice anyone at first, but I can still hear shuffling around."
    $ misc = "???"
    misc "Hello? Is anyone there?"
    "That sounded like it came from above! So naturally, I turn my gaze up only to spot…"
    if default == 0 and gen3 != 10:
        hide screen vnui
        $ gen1 = 12
        call screen characterchoice
        $ blob = gen2
    layeredimage blossom1a:
        always:
            "blossom1ab [blob]"
        group eyes:
            attribute e1:
                "blossom1ae1 [blob]"
            attribute e2:
                "blossom1ae2"
    play music comical
    show black:
        ypos 250
    show blossom1a e1
    camera:
        zpos -250 ypos 125
    $ textbox = 2
    with d
    "A butt!"
    "No, not just a butt; it’s connected to someone!"
    camera:
        linear 3.5 ypos -105
    "And as soon as my eyes scan upwards to her face, she spots me too."
    $ misc = "Butt"
    misc "Oh, uhm, sorry! I didn’t spot you down there!"
    if default == 0 and gen3 != 10:
        menu:
            "What was her name?"
            "Default: Blossom":
                $ blossom = "Blossom"
            "Custom":
                $ blossom = renpy.input("What was her name?")
                if blossom == "":
                    $ blossom= "Blossom"
                $ blossom = blossom.strip()
        show screen vnui
    camera:
        linear 5 zpos 0 ypos 0
    mc "No, no, I’m the one that should be apologizing. I came in here to greet you, but it looks like I was snooping about."
    show blossom1a e2 with d
    blo "Hehe, I wouldn’t suspect you of something like that! You must have heard me rummaging around."
    blo "(I haven’t seen in a man in ages, and this guy just walks into the barn! Who on earth is this cutie?)"
    mc "Yeah! What are you, uhm… What are you doing up there anyway?"
    "She has absolutely no idea that I can see everything, does she?"
    show blossom1a e1 with d
    blo "It’s nothing. I mean, it’s a little silly, really. I like coming up here to read because this spot has a great view from the window."
    "Why is there a glass pane up there anyway? You know what? This is just one of those situations where I won’t question it."
    mc "My name’s [mc]. I’m here to talk to your sister."
    show blossom1a e2 with d
    blo "I’m [blo]! {i}Yawn!{/i} We were just finishing up here a few moments ago, when [hon] said she’s –"
    show blossom1a e1 with d
    blo "Hold on a second… C-Can’t you see my butt from down there?!"
    mc "Uhm… A little…"
    play music blossomtheme fadein 3
    play ambience1 ambiencenight fadein 300
    scene image "bg barn1.jpg"
    show image "bg barn2.jpg":
        alpha 0 
        linear 120 alpha 1
    show blo awkward blush
    $ textbox = 1
    with d
    "[blo] quickly hops down, patting her butt down with a huge blush and tucking her tail between her legs."
    blo "Aahhh… I’m so sorry!"
    blo "(So embarrassing! How did I mess things up with this guy already?!)"
    show blo neutral with d
    blo "I didn’t mean to – {i}Yawn!{/i} flash you like that."
    hide screen vnui
    menu:
        "I enjoyed the view!":
            show blo bashful with d
            blo "O-Oh?"
        "That's quite alright.":
            show blo bashful with d
        "Next time, I'll flash you so we'll be even.":
            show blo bashful with d
            blo "Uhm, you're not exactly hiding anything."
            mc "Good... point..."
    show screen vnui
    mc "You've been yawning a lot, a long day?"
    show blo neutral with d
    blo "Exhausted, yeah. My sis and I work here from sunrise to sunset. Sometimes I’m so tired by the evening that I can barely think straight."
    mc "Wait, you’re a farmer too?"
    show blo awkward with d
    blo "Unfortunately, yes... I don't find it particularly satisfying, but that's the family business, and we need all the hands we can get here to try and reach our quota."
    "[blo] was always passionate about music and art more than farming and business management, so it’s a shame to see her potential held back..."
    show blo angry with d
    blo "Especially recently, work has really been kicking my butt."
    hide screen vnui
    menu:
        "Kicking it? But your butt was in such good shape!":
            blo "Maybe it's all the exercise!"
            "Genuinely, now that I look her up and down, her body does seem to be more firm and toned."
        "Does it need a massage?":
            show blo neutral with d
            blo "A massage sounds nice! Wait, you mean on m-mah butt?!"
            mc "The ache of the body doesn't discriminate, and neither do my massages~"
            show blo bashful with d
            blo "M-Maybe I will take you up on that, then."
        "Awh, bless you!":
            show blo happy with d
            blo "T-Thanks!"
    show screen vnui
    show blo bashful with d
    blo "Uhm… It was really embarrassing how you saw my butt like that!"
    hide screen vnui
    menu:
        "It was an amazing view!":
            mc "Talk about a good first impression! {i}Wink{/i}"
        "Relax, it's fine!":
            mc "We're all nude here anyway, it's not a big deal."
    show screen vnui
    show blo happy with d
    blo "Hehe, and here was me being really embarrassed! I thought I messed up."
    mc "Well, with an ass like that, it’s impossible to mess up."
    show blo bashful with d
    blo "I guess I didn’t mind you seeing it then… Hehe… I’m usually kind of insecure about my body."
    mc "Insecure? I don’t think there’s anything wrong with your body."
    show blo neutral with d
    blo "Really? You... like it?"
    blo "I’m petite and it's clearly holding me back on the farm... I’m not big and muscular like my sister."
    mc "There are plenty of guys out there that prefer your kind of body."
    show blo awkward with d
    blo "You think? I thought the bigger the boobs, the better for men, or something. What do you think?"
    hide screen vnui
    menu:
        "I love your body type.":
            show blo laughing with d
            blo "Ooohh, that makes me happy!"
        "Big and voluptuous is better.":
            show blo neutral with d
            blo "Aaahh, I thought so…"
            mc "But hey, your ass {b}is{/b} big and voluptuous, [blo]. I think you’re focusing on the wrong things."
        "All bodies are beautiful.":
            show blo laughing with d
            blo "That’s true. Maybe I just need a little more confidence."
        "In the wise words of [mel], who needs tits? You have a great ass!" if brothelroute1 == 1:
            show blo laughing with d
            blo "I’m not sure who that is, but I like her thinking."
    show screen vnui
    "There was a slight glisten between her thighs. She’s actually getting turned on!"
    show blo horny with d
    blo "If you want to see my b-butt again, I could, uhm... Turn around..."
    mc "What would happen then?"
    show blo bashful with d
    blo "I-I'm not sure... What would you like to happen?"
    hide screen vnui
    menu:
        "May I see your butt again?":
            $ blo1 = 1
            show screen vnui
            stop music fadeout 3
            blo "Y-Yeah… You can."
            
            play music sextheme
            play moans1 moansmisc2
            stop ambience1 fadeout 3
            show blossom1b 
            call camerabreath from _call_camerabreath_20
            $ textbox = 2
            with d
            "[blo] bends over a nearby crate, not even looking back as her legs stretch downward and provide a spectacular view of her ass."
            mc "God, you’re so hot…"
            blo "Mmmhh… I am? T-Thank you... No one has ever said something like that to me, so it's quite a confidence boost."
            "Her genitals were in clear view, and unlike before, there was now a distinct wetness. Not even cute, innocent girls like [blo] can escape their needs."
            mc "Can I touch it?"
            blo "P-Please do…"
            show blossom1b hand with d
            "I step forward and spread her left cheek, causing her gooey pussy to let out an audible schlick while her body shivered at the contact. I admire her cute anus too; she really has a perfect ass."
            "My cock was getting harder by the second. Even though I’ve just met her, I could take her right here, and she wouldn’t resist or complain."
            "She briefly peeks back and catches a glimpse of my cock, causing her to gasp. Her body language alone tells me how aroused she’s getting; she can’t stop grinding her hips." 
            mc "I promise I won’t put it inside. Well, maybe the tip~"
            blo "Hm? What are you?"
            show blossom1b -hand b1 with d
            "Removing my hand, I replace it with my cock instead, pressing the tip of my hard member against her ass cheeks, fighting the urge to claim her tight hole right now. She’s certainly wet enough for it."
            blo "Oouhhhh… T-That’s… your…"
            "Instead, I began to rub myself against her sensitive entrance, grinding my throbbing member against her dripping wet folds."
            "The heat emanating from her petite body ignited the raging fire within me, and I started furiously masturbating as my tip smushed and pushed against her virgin pussy."
            mc "Nnggh, you’re so wet, I feel like if I put any pressure against you at all, I’d slip straight inside!"
            blo "Uoohhh… [mc]…"
            "The contact sent waves of pure ecstasy coursing through me, I relished the feeling of each movement against her."
            "[blo]’s tail had begun a seductive dance, occasionally brushing against my chest or against my shaft. At this point, her whole body was shaking with pleasure."
            menu:
                "{i}Spank Her!{/i}":
                    play sound2 spank
                    show blossom1b spanked with d
                    "Unable to resist the temptation, I raised my hand and spanked her firm ass, eliciting a yelp of mixed pain and pleasure."
                    blo "Oooohhhhh, that was… good…"
                    mc "Want me to do it again?"
                    blo "Y-Yeah…"
                    play sound2 spank
                    show blossom1b spanked with d
                    "I spanked her once again, this time on the other cheek. This time the moan was almost entirely pleasure, her hips squirming with desperate need."
                "{i}Have Mercy{/i}":
                    pass
            mc "You feel so damn good… I won’t last much longer!"
            "She let out a soft moan of pleasure, her body arching backward into me unconsciously. Combined with my thrusting, it causes my tip to almost slide in. Feeling the warmth of her insides on my tip for even a fraction of a second was enough to push me over the edge."
            play sound2 cum
            show blossom1b b2 with c
            play sound2 cum
            with c
            "My voice strained with desire as the overwhelming pleasure consumed me completely. I let out an earth-shattering groan as hot, thick cum spurted out the head of my cock."
            play sound2 cum
            show blossom1b cum with c
            play sound2 cum
            with c
            "Hot loads of cum painted her behind white, plenty dripping down over her anus and pussy too."
            show blossom1b -b1 -b2 cum with d
            "My orgasm raged on for almost thirty seconds before finally subsiding, leaving me panting heavily as I pulled away from her cum-soaked flank."
            mc "{i}Pant, pant{/i} Incredible…"
            scene bg barn2 
            show blo neutral blush cum
            call camerareset2 from _call_camerareset2_16
            call stopbgs from _call_stopbgs_18
            play ambience1 night fadein 10
            $ textbox = 1
            with d
            blo "That felt so good, but… I can’t believe we just did that!"
            mc "What’s so hard to believe? I couldn’t resist when I saw you."
            show blo bashful with d
            blo "Ahh… Your flattery does work on me, but… we have only just met."
            mc "And that’s exactly why I made sure to leave a lot of the best parts for later~"
            show blo laughing with d
            blo "Ohh… Who on earth are you? You just… wandered into this barn, and everything else happened so fast I could barely keep up."
            mc "I’m just a friend looking for [hon]."
        "Where can I find [hon]?":
            show screen vnui
    show blo happy with d
    blo "Ah, I almost forgot! She told me she was going in the shower. Go right in!"
    mc "Excellent, thank you! I’m sure we’ll see each other again soon, [blo]."
    show blo bashful with d
    blo "R-Right! (Uwahhh, he’s so cuteeeeee!)"
    if blo1 == 1:
        blo "(But… Nnhhh… Even though I was so close, I didn’t get to cum… Next time, I need to be more proactive instead of just letting him do everything! I’ll show him what I can do instead of just being a good butt.)"
    stop music fadeout 3
    scene black with d
    "…"
    layeredimage honeycrisp1a:
        always:
            "honeycrisp1ab [honb]"
    scene bg farm2 with d
    "In [hon]’s house, I wander around the first floor until I catch exactly where I think she might be. The upstairs shower, naturally."
    play music honeycrisptheme
    play ambience2 rain volume 0.3
    show honeycrisp1a 
    $ textbox = 2
    with d
    "I’d only be polite to knock and inform her I’m here, so wander into the upstairs hallway, and I’m caught with a full frontal shot of [hon]’s bathroom, the shower cubical completely visible."
    hon "Ey? If you’re a burglar, you’re not a very good one! Bwahaha."
    mc "My apologies, [hon]! Your sister invited me in and I wanted to make myself known."
    hon "Wasn’t expecting a guest! Sorry for being rude; I just need to finish my hair."
    "She continues showering, not missing a beat in the process."
    "Is it just me, or is she even more muscular than in the previous world? You could grate cheese on those abs!"
    "I technically just walked in on her showering, but… because nudity is the norm here, I guess there’s technically nothing unusual about that."
    "There are just some aspects of the culture that’ll always surprise me. It feels weird to me, but she doesn’t mind at all."
    "I'm probably making it more awkward by watching her."
    hon "Bwahaha, you see something you like, sugarcube? If you wanted to join me, you shoulda let me know!"
    mc "Sorry! I was just lost in thought; I’ll excuse myself downstairs."
    hon "Nah, I was quite enjoying giving you a show!"
    mc "Haha, my apologies for staring. Your body is quite the spectacle."
    hon "Tsk, don’t be saying stuff like that in mating season, ya tease~"
    stop ambience2 fadeout 1
    scene bg farm2 
    $ textbox = 1
    with d
    "She finally hops out of the shower, and as soon as her hair’s dry, we move downstairs and continue our conversation."
    show hon laughing with d
    "Our chemistry is immediately a hit. [hon] is as outgoing and brimming with confidence as ever. It’s a relief to see that she’s doing so well in this more challenging reality."
    "With introductions out of the way, she offers me some fresh cider."
    show hon happy with d
    hon "I know it’s not a special occasion, but it’s been too long since I’ve had a guest, so you just haf’ta try some of my fresh cider! I gotta warn ya though; this is my special brew; it has more of an alcoholic kick than ya might expect." 
    "I took a sip of the cider, and she wasn’t kidding! The taste is top-notch, but the alcoholic aftertaste is like a slap in the face."
    show hon wink with d
    hon "Now, why come all the way over here? My farm is boooring!"
    mc "I’ll be straight with you: I’m trying to gather a group of six special people to become a powerful group that works under the Queen. The Virtues of Concord."
    show hon neutral with d
    hon "Bah, me? A virtue? Y’all must be crazy."
    mc "Wait, you speak as if you already know what a virtue is?"
    show hon wink with d
    hon "Sure do; it’s a story I heard from my grandfather. They’re the Queen’s personal elite, used as a last resort to enforce peace and order."
    show hon happy with d
    hon "Each virtue is trusted with a relic imbued with great power; when all six are aligned, it’s enough power to even challenge the Queen."
    hon "However, these were always just stories. It’s hard to tell what’s real or not these days." 
    mc "I don’t remember anything about relics from my experience, but I insist that it is real, and you have the full capability of becoming a virtue."
    show hon angry with d
    hon "Bah, I’m just a humble farmer. I don’t have any lofty ambitions like that, I’m just trying to make ends meet."
    hon "You should find someone else instead; I’m too busy to even leave."
    "That’s no good… I need to find a way to help her."
    show hon neutral with d
    hon "Guh, I need another drink. You want one?"
    "I’d barely gotten halfway through my first! Before I could think of a reply, a second cold tankard of cider clacked onto the wooden table before me, and as soon as I looked up, I could already see [hon] drinking deeply."
    show hon laughing with d
    hon "Aahhhh, can’t beat that freshness…"
    mc "[blo] also mentioned you two are working non-stop. What’s the issue?"
    show hon neutral with d
    hon "Demand for crops gone up, but prices have been dropping. Because of this, we’ve been unable to acquire the funds to appropriately scale the operations while having to work far more to compensate."
    hon "Basically, we don’t have the money to purchase expensive, new farming equipment, so we’re left doing everything by hand. It’s ridiculous; that’s what it is."
    hon "What we need is a few hunks like you working here. Now that’d be the dream."
    mc "Me, a hunk? You’re more muscular than me."
    show hon laughing with d
    hon "Bwaha, it’s not a competition. I’m just saying you’re doing a lot better than the average guy out there."
    mc "Thanks I appreciate that."
    mc "Are you working with Anna? I remember her being quite an ambitious businesswoman."
    show hon neutral with d
    hon "You know Anna? That damn cow. At this rate, we’ll get bought out, like she’s been doing to so much of the other farmland around the north."
    hon "She’s been threatening all the local farms by undercutting our prices. That’s exactly why the prices have dropped in the first place."
    hon "But I can’t lose this place… It’s all I have after my dad passed away a few years back."
    "A few years ago, hm? [hon] and [blo] have been alone a lot longer in this universe. Just as I was thinking, I spot [hon] finishing her second serving of cider and moving to get a third."
    mc "Sorry for bringing it up…"
    show hon angry with d
    hon "Nah, it’s fine... Maybe I’m just the one being stubborn and behind the times. I don’t know how long this is sustainable for, especially when I’m making [blo] work too."
    mc "Is there any way I can help out?"
    show hon neutral with d
    hon "I don’t think… Hm? Hm…"
    play sound2 equip
    camera:
        linear 0.5 zpos -300 ypos -125
    "[hon] sits down, takes a large swig, and thinks for a few moments."
    show hon happy with d
    "Her gaze then turns to me, the edges of her lips curling into a smile."
    show hon laughing with d
    hon "You know what, stud, I rushed to conclusions too fast."
    hon "I’m interested in your proposition about becoming a virtue, but only if it can help my farm get the support it needs."
    show hon wink blush with d
    hon "And seeing your physique, I think y’all would make an excellent farmhand too."
    mc "Farmhand? Tempting offer, but I’m often busy."
    play sound2 equip
    camera:
        linear 0.5 zpos -350 ypos -150
    "She leans over to me, brushing her soft hand against my shoulder and down to my chest. Is she… drunk? She’s tipsy at the very least."
    show hon wink with d
    hon "You sure? Y’all are just my type~"
    $ gen1 = 0
    hide screen vnui
    menu f1m1:
        "You're my type too.":
            show hon horny with d
            hon "There might be a place for you here if you impress me, stud~"
        "Are you trying to seduce me?":
            show hon horny with d
            hon "What would you do if I said yes?"
        "Sorry, I already came all over your sister's ass." if blo1 == 1 and gen1 == 0:
            $ gen1 = 1
            "Why on earth would you pick that?! I'm not saying that!"
            jump f1m1
        "I guess I could work sometimes.":
            mc "Well… I guess I can work here part time. The extra monies will go a long way." 
        "Nah, I'm seriously busy.":
            show hon neutral with d
            hon "Darn! Not even for a couple of hours in the evening?"
            "That's actually a very good offer. I need to take what I can get."
            mc "Fine, but only in the evenings."
    show screen vnui
    "Her tune changed quite suddenly, like a switch in her head flipped. While amicable before, now she’s making a much more proactive effort to be friendly and interested."
    "Seems she realized that I’m the solution to her problem. If I worked here, it could dramatically alleviate her burden. But that’s not all, I can get her in contact with the Queen, there’s a chance she could appeal for direct support."
    "Either that, or she's horny."
    show hon laughing with d
    hon "Then it’s settled! {i}Hic{/i} If ya came in the evening and took care of the livestock, that’d be a ton of help. It’d give me time to catch up on my record keeping."
    "While I absolutely want to help, I can’t help but wonder if there isn’t a better option by working with Anna. They were business partners in my universe, and I don’t see why that couldn’t happen again."
    "[hon] owns a lot of land but doesn’t have the equipment or manpower to effectively use it; an investment from Anna could benefit them both."
    "However, as lovely as [hon] is, I know she can be stubborn. It’s not something I’ll be able to easily convince her of."
    mc "Sure, I’d be happy to help out some evenings."
    show hon happy with d
    hon "Fantastic! Y’all are a lifesaver!"
    play sound2 equip
    camera:
        linear 0.5 zpos -400 ypos -170
    "She leaned closer, brushing her firm breasts against my arm in a deliberate yet playful move. I can feel her nipples slowly getting more erect during this, until the nubs are poking into my arm."
    show hon horny with d
    hon "And there are plenty of other things that can be done in the evenings~"
    hon "Perhaps I could show you some of the employee benefits?"
    hide screen vnui
    menu:
        "Employee benefits?": 
            show screen vnui
            show hon wink with d
            hon "Hehe, are you interested?"
            jump f1ebs
        "{i}Kiss her{/i}":
            show screen vnui
            show hon satisfied with d
            "I bring my lip to hers and she immediately melts into the kiss, her fur standing on end as her tongue darts into my mouth and dances with my own."
            hon "Mmphhh... Nghh... You're sexy..."
        "Are you drunk?":
            show screen vnui
            show hon neutral with d
            "I stuttered slightly under her flirtatious gaze, causing her to back away, where she seems to snap back into reality." 
            hon "Huh… I don’t know what came over me there. Sorry, stud, mating season and alcohol are a bad combination, especially around attractive men."
            mc "That’s quite alright, [hon]. I understand that mating season can get pretty… intense…"
    "Obviously, I found myself intrigued by [hon]’s flirtatious advances. Exploring our chemistry further was tempting. However, instead of directly reciprocating, I decided to play it cool." 
    mc "I admit, I’m quite interested in these employee ‘benefits’…"
    label f1ebs:
        "I subtly let my gaze drift downward once more, unable to resist admiring her figure."
    show hon wink with d
    hon "Your eyes have been drinking me in since I was in the shower, haven’t they, sugarcube?" 
    mc "How could I not? You’re gorgeous."
    
    play music sextheme fadein 3
    show honeycrisp1b e1 
    play moans1 moansmisc2
    call camerabreath from _call_camerabreath_21
    $ textbox = 2
    with d
    "In a flirtatious haze, [hon] shifts her butt from her chair straight onto my lap."
    "Like this, even the muscular mare seems like a delicate woman. Although, I can hardly call her ladylike when her butt started to rub back and forth against my crotch."
    hon "Haaahhhh… I’m getting really horny, stud…"
    hon "I'm just a dumb fucking horse in mating season, I can't help myself~ I’ll just sit here, and whatever happens, happens~"
    "The room seemed to grow hotter, the scent of lust thickening the air as our bodies pressed against each other."
    hide screen vnui
    menu:
        "{i}Squeeze her Butt!{/i}":
            show screen vnui
            "I couldn’t resist the temptation any longer; I reached out and caressed [hon]’s ass cheek, my fingers softly digging into her fur, causing a soft moan to slip from her lips."
            "In response, [hon] turned her head slightly, leaving our faces inches apart. Her eyes locked with mine, filled with desire and anticipation. She parted her lips slowly, invitingly."
            "Before I could think twice, our lips pressed together in an intense kiss, our tongues tangled passionately."
            "Breathless, but wanting more, we broke apart briefly. I couldn’t tear my eyes away from her flushed face. She looked utterly irresistible."
            hon "I can feel ya growing down there… It feels just as nice and big as I’d hoped~"
            "Since she was sitting on me, my growing erection was short of space, causing it to press against her butt with ever-increasing pressure. Every time she squirmed or adjusted herself, I could feel her wet folds brushing against my tip."
            mc "You’re driving me crazy!"
            hon "That’s the idea, sugar. Just sit back and enjoy what comes next~"
            show honeycrisp1b tj1 with d
            "She moans back, her voice husky with desire. With one swift motion, she adjusts her butt to free my throbbing cock from its confines by allowing it to nestle between her thighs."
            "But not just between her thighs; she also prominently pushed against the full length of her pussy lips."
            play moans1 moansmisc3
            play ambience2 handjob2 fadein 3
            camera:
                linear 0.2 zpos -15
                linear 0.6 ypos -7
                linear 0.2
                linear 0.3 ypos 7
                repeat
            show honeycrisp1b e2 with vpunch
            "With practiced ease, [hon] began to roll her hips up and down, massaging my twitching cock between her thighs and wet entrance."
            mc "Nnhhhh, you’re really good at that!"
            show honeycrisp1b e1 with d
            hon "It’s all in the hips, babe~"
            show honeycrisp1b e2 with d
            "Pleasure surged through me as I started to rock my hips too; before long, our hips began to move together as one, our moans and gasps mingling into one primal symphony of desire."
            "I could tell it was starting to feel really good for her too, as she gradually altered the angle of the grinding to focus on her clit more. Her ragged breaths turned into needy moans." 
            show honeycrisp1b e1 with d
            hon "Nnghh, that’s the spot! {i}Pant, pant{/i} Is this good for you?"
            mc "Ohhh yeah, it feels amazing!"
            show honeycrisp1b e2 with d
            "Our bodies were entwined tightly, sweat glistening on our skin as we moved together faster and harder. I couldn’t tell if she was close, but my orgasm was threatening to erupt at any moment."
            show honeycrisp1b e1 with d
            hon "I can feel you stiffening up; are you close?"
            mc "Yeah! I’m getting pretty close!"
            show honeycrisp1b e2 with d
            "Upon hearing that, she actively sped up, to the point where I could barely keep up. This was a sudden reminder of just how strong and fast these ponies can be. I helplessly sat there as she effortlessly milked me with just her thighs."
            hon "Mmhh, cum for me, stud!"
            mc "Fuck, yes! Cumming now!"
            play sound2 cum
            show honeycrisp1b e3 tj2 cum with c
            play sound2 cum
            with c
            "With a final thrust upwards, my hot cum spurted out of my tip and started spraying her body." 
            play sound2 cum
            with c
            play sound2 cum
            with c
            hon "There we go… Good boy~"
            show honeycrisp1b -tj2 
            call camerabreath from _call_camerabreath_22
            call stopbgs from _call_stopbgs_19
            stop music fadeout 10
            play ambience1 night fadein 10
            with d
            "It felt like an eternity before my orgasm finally subsided, leaving me breathless and limp. Although she remained seated on me, our hearts pounding in unison."
            "[hon] leaned closer to my chest, giving me a side hug before pulling apart to pat herself down with a tissue."
            mc "They weren’t kidding when they said cow girls were good on top."
            hon "Heh, you don’t even know the half of it."
            play sound2 equip
            scene bg farm2
            call camerareset1 from _call_camerareset1_6
            $ textbox = 1
            show hon wink with d
            hon "Sorry if that was a little forward or presumptuous of me; I can be quite an… aggressive lover."
            show hon horny with d
            hon "I know what I want, how to get it, and sometimes I really {b}need{/b} it."
            mc "Hoohh boy, I can tell that I’ll like it here."
        "{i}Turn her Down{/i}":
            show screen vnui
            mc "I think you’ve had quite a bit to drink."
            play sound2 equip 
            scene bg farm2
            call camerareset1 from _call_camerareset1_7
            stop music fadeout 3
            stop moans1 fadeout 3
            show hon neutral with d
            hon "Haaahhh… I guess you’re right; it’s a little early in our friendship for me to start grinding on you, isn’t it?"
            mc "But don’t consider this a rejection, maybe the next time I stumble upon you in the shower, I’ll join you."
            show hon wink with d
            hon "I’ll hold you to that, stud~"
    mc "Before I disappear, I’ll tell you about the plan. You’ll be contacting someone called [lil], who is the Queen’s student."
    "I exchange numbers with [hon] and give her the necessary information."
    show hon happy with d
    hon "Hm… [lil], eh? I’ll give her a ring."
    mc "Probably better just to text her, actually."
    show hon horny blush with d
    hon "Oh, and one more thing before you go…"
    play music comical
    layeredimage honeycrisp1c:
        always:
            "honeycrisp1c [honb]"
    show honeycrisp1c 
    $ textbox = 2
    call camerabreath from _call_camerabreath_23
    with d
    "Slowly, seductively, [hon] turned around so that she was facing away from me. Gracefully, she bent forward and presented her round, firm ass cheeks prominently. Her tail flickered upward to give a clear view."
    "God damn, what is with these two sisers having amazing asses? And they're both capable of weaponizing them to tease me too!"
    hon "Is this what you want?"
    hide screen vnui
    menu:
        "Yes please!":
            pass
        "Damn, you're soaking wet!":    
            hon "Nggh, that's right! I'm just a dumb, slutty horse in heat~"
        "Why me?":
            hon "Right person, right place, right time, stud!"
    show screen vnui
    "She purred playfully over her shoulder, her back arching slightly to accentuate her ass even more enticingly. Every moment she made was deliberately designed to tease and tantalize me further."
    hon "Like what you see? Work here and I can give this and more."
    mc "Sheesh, you don’t make it a hard choice, do you?"
    hon "Bwahaha, see you soon, sugarcube. You can show yourself out since you let yourself in~"
    stop music fadeout 3
    scene bg farm2 
    $ textbox = 1
    call camerareset from _call_camerareset_3
    with d
    "[hon] walks away, her ass continuing swaying seductively until she’s completely out of view."
    show black with d
    "Before I leave, I pay a quick visit to [blo]’s room upstairs."
    play music blossomtheme
    scene bg farm3 
    show blo neutral blush with d
    "I knock on the door, hearing a ‘wah!’ and some frantic stumbling around. Eventually, [blo] opens the door."
    blo "S-Sorry! You nearly gave me a heart attack – Wah! It’s you!"
    mc "Haha, sorry about that. May I come in?"
    show blo laughing with d
    blo "Of course!"
    scene bg farm3 with d
    "Closing the door behind me, I sit on [blo]’s half-made bed. It’s clear she made it but was recently ‘using’ it."
    mc "Oh dear, looks like I caught you with your pants down."
    show blo neutral with d
    blo "Pardon?"
    mc "Ah, that saying doesn’t work here at all, does it? Nevermind. I’m here to ask for your help."
    "I explain to [blo] that I’d like to send Anna a letter to invite her for a business meeting here at the Arcadian farm."
    "I’m sure if I can just get [hon] and Anna face-to-face, they’ll hit it off and plenty of opportunities will open up for [hon]."
    show blo happy with d
    blo "If you think this’ll genuinely help, I’ll do it."
    mc "Thank you so much. Worst case scenario, Anna and [hon] don’t reach an agreement, nothing gained nothing lost."
    show blo laughing with d
    blo "Thank you for trying to help us, that really means a lot." 
    mc "It’s the least I can do after you’ve both been such good hosts."
    show blo bashful blush with d
    "[blo] blushes and acts innocent."
    show blo awkward with d
    blo "If you, uh, if you- uhm… If you, ah…"
    show blo horny with d
    blo "Come back and see me again! Okay?"
    mc "I’m planning on it. Show me what you've got next time."
    show blo laughing with d
    blo "Yes, sir!"
    stop music fadeout 3
    scene black with dissolve
    "…"
    play music moxietheme
    play ambience1 night
    scene bg apartment with dissolve
    "Back in [mox]’s apartment, I finally sit down and take a rest."
    show mox happy with d
    mox "Good evening, [mc]! Where’d you find yourself today?"
    mc "All the way to the farms in the northwest, and let me tell you, those two sisters could probably power a small village with their sexual repression alone."
    show mox laughing with d
    mox "Mating season really can be like that sometimes. Especially when you think you’re handling it fine, but then an absolute hottie just appears out of nowhere."
    mc "And I also know that I’m both of their types. So, it does feel like I’m cheating with my prior knowledge sometimes." 
    show mox wink with d
    mox "You’re on new game plus! Do you also know the winning lottery numbers?"
    mc "I’m afraid it doesn’t quite work like that."
    show mox neutral with d
    mox "Darn… I guess you didn't appear here at the exact same time and day in both universes, right?"
    mc "You're right, I didn't. But you do bring up an interesting point. My universe and this universe have a substantial number of events in common, but sometimes they happen at distinct times."
    show mox happy with d
    mox "Any examples?"
    mc "Yeah, the most obvious one is that I teleported in at the wrong time. If that’s a fixed event in all these ‘types’ of universes, why happen months apart?"
    mc "With this in mind, if there’s anything that hasn’t happened yet, I might be able to predict it happening sometime in the future." 
    show mox laughing with d
    mox "Hummm… I’m going to keep my eyes and ears wide open then!"
    mc "You’re going to keep your ears wide open?"
    show mox bashful blush with d
    mox "I’m not so good with words, okay?"
    scene black with dissolve
    if replay == 1:
        return
    $ farmroute1 = 1
    $ completion += 1
    $ farmcompletion += 1
    $ blomsg1 = 1
    $ unread += 1
    $ unreadblo += 1
    jump newday

label farm2:
    jump newday