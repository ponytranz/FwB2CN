label start:
    ##version stuff
    $ buttersnamed = 1
    $ rikunamed = 1
    $ creamnamed = 1
    $ aurnamed = 1
    $ selnamed = 1
    $ clairenamefix = 1
    ##

    scene black
    show space1:
        alpha 1
        linear 8 alpha 0.2
        linear 9 alpha 1
        repeat
    show space2:
        alpha 0
        linear 10 alpha 0.8
        linear 11 alpha 0
        repeat
    with d
    camera:
        perspective True
        zpos 0 xpos 0 ypos 0
    play music intro
    $ textbox = 2
    show cre happy with d
    "Before we start the game, there are a few key choices you'll need to make to customize your experience." 
    "First, are you interested in customizing the style and names of characters?"
    menu:
        "Default Names and Colours":
            $ default = 1
        "Custom Names and Styles":
            $ default = 0
            "Let's handle these now so they don't interrupt the story later." 
    if persistent.intro == True:
        "Secondly, I can tell that this isn't the first time you've started a new game. Would you like to skip the introduction?"
        menu:
            "Replay Introduction (4 Sex Scenes and ~45 Min Reading Time)":
                pass
            "Skip Introduction":
                jump introskip
    $ persistent.intro = True
    "Let's start with you! What's your name?"
    $ mc = renpy.input("What is your name?")
    if mc == "":
        $ mc= "Anon"
    $ mc = mc.strip()
    "Ah, [mc]! I remember now! You've had quite an adventure, haven't you?"
    menu:
        "That’s right! {i}(Played FwB 1){/i}":
            $ fwb1 = 1
        "I don’t remember {i}(Didn’t Play FwB 1){/i}":
            $ fwb1 = 0
            "Interesting! Don't worry, I'll catch you up to speed real quick!"
    label intro:
        scene black with d
        show intromoxie 1
    $ textbox = 1
    with d
    "When you first arrived in this world, two mares welcomed you and showed you around."
    show intromoxie 2 with d
    "It didn’t take long for you to get balls deep."
    if default == 0:
        "The memories are a bit hazy... Do you recall their names and what they looked like?"
        #Moxie Name and Art
        $ gen1 = 1
        $ gen2 = 1
        call screen characterchoice
        screen characterchoice ():
            imagemap:
                if gen1 == 1:
                    ground "characterchoicemoxie.png"
                    hover "characterchoicemoxieh.png"
                elif gen1 == 2:
                    ground "characterchoicepenelope.png"
                    hover "characterchoicepenelopeh.png"
                elif gen1 == 3:
                    ground "characterchoicehoneycrisp.png"
                    hover "characterchoicehoneycrisph.png"
                elif gen1 == 4:
                    ground "characterchoiceruby.png"
                    hover "characterchoicerubyh.png"
                elif gen1 == 7:
                    ground "characterchoicelily.png"
                    hover "characterchoicelilyh.png"
                elif gen1 == 11:
                    ground "characterchoicemelody.png"
                    hover "characterchoicemelodyh.png"
                elif gen1 == 12:
                    ground "characterchoiceblossom.png"
                    hover "characterchoiceblossomh.png"
                hotspot (252, 71, 664, 941) action [Return("characterchoice"), SetVariable("gen2", 1)] 
                hotspot (980, 102, 751, 886) action [Return("characterchoice"), SetVariable("gen2", 2)] 
            image "characterchoiceui.png"
        $ moxb = gen2
        show mox happy
        with d
        menu:
            "What was her name?"
            "Default: Moxie":
                $ moxie = "Moxie"
            "Custom":
                $ moxie = renpy.input("What was her name?")
                if moxie == "":
                    $ moxie= "Moxie"
                $ moxie = moxie.strip()
        #Penelope Name and Art
        hide mox with d
        $ gen1 = 2
        $ gen2 = 1
        call screen characterchoice
        $ penb = gen2
        show pen happy
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
    hide intromoxie 2
    show introhoneycrisp 1 
    hide pen
    with dissolve
    "You visited a farm and helped a girl cope with her grief over losing a loved one."
    show introhoneycrisp 2 with d
    "Turns out, they weren’t kidding about how good cow girls are on top."
    if default == 0:
        #Honeycrisp Name and Art
        hide introhoneycrisp with d
        $ gen1 = 3
        $ gen2 = 1
        call screen characterchoice
        $ honb = gen2
        show hon happy
        menu:
            "What was her name?"
            "Default: Honeycrisp":
                $ honeycrisp = "Honeycrisp"
            "Custom":
                $ honeycrisp = renpy.input("What was her name?")
                if honeycrisp == "":
                    $ honeycrisp= "Honeycrisp"
                $ honeycrisp = honeycrisp.strip()
    show introruby 1 
    hide hon
    with d
    "You stopped by a struggling boutique and gave the lady there the support she needed to turn her business around."
    show introruby 2 with d
    "She was more than happy to show her appreciation. You still remember the feeling of her fluffy butt in your hands."
    if default == 0:
        #Ruby Name and Art
        hide introruby with d
        $ gen1 = 4
        $ gen2 = 1
        call screen characterchoice
        $ rubb = gen2
        show rub happy
        menu:
            "What was her name?"
            "Default: Ruby":
                $ ruby = "Ruby"
            "Custom":
                $ ruby = renpy.input("What was her name?")
                if ruby == "":
                    $ ruby= "Ruby"
                $ ruby = ruby.strip()
    show introbutters 1 
    hide rub
    with d
    "In the forest, you found a girl dealing with deadly succubus powers and helped her cure them."
    show introbutters 2 with d
    "Once she was no longer dangerous, the real fun began!"
    if default == 0:
        menu:
            "What was her name?"
            "Default: Butters":
                $ butters = "Butters"
            "Custom":
                $ butters = renpy.input("What was her name?")
                if butters == "":
                    $ butters= "Butters"
                $ butters = butters.strip()
    #Butters Name and Art
    show introriku 1 
    hide introbutters
    with d
    "Back in the city centre, you met a girl running a bar. She was struggling and uncertain, but you offered the support she needed to find herself."
    show introriku 2 with d
    "And in the process, discovered she was quite the butt slut."
    if default == 0:
        menu:
            "What was her name?"
            "Default: Riku":
                $ riku = "Riku"
            "Alternative: Prisma":
                $ riku = "Prisma"
            "Custom":
                $ riku = renpy.input("What was her name?")
                if riku == "":
                    $ riku= "Riku"
                $ riku = riku.strip()
    #Riku Name and Art
    show introlily 1 
    hide introriku 
    with d
    "At the tree library, you helped the queen's timid student break out of her shell."
    show introlily 2 with d
    "With explosive results as all that pent-up frustration was unleashed on you!"
    if default == 0:
        #Lily Name and Art
        hide introlily with d
        $ gen1 = 7
        $ gen2 = 1
        call screen characterchoice
        $ lilb = gen2
        show lil happy
        menu:
            "What was her name?"
            "Default: Lily":
                $ lily = "Lily"
            "(Custom Name)":
                $ lily = renpy.input("What was her name?")
                if lily == "":
                    $ lily= "Lily"
                $ lily = lily.strip()
    show introbutters 1 
    hide lil
    show introcream 1
    with d
    "And who could forget the amazing party we had at my bakery?"
    show introcream 2 with d
    "Although I wonder if there’s anything else we forgot there? Hehe, probably not!"
    if default == 0:
        menu:
            "What was her name?"
            "Default: Cream":
                $ cream = "Cream"
            "Custom":
                $ cream = renpy.input("What was her name?")
                if cream == "":
                    $ cream= "Cream"
                $ cream = cream.strip()
    #Cream Name and Art
    show introprincess 2 with d
    "After all that fun, the next step was meeting the princess and queen themselves!"  
    if default == 0:
        menu:
            "What was the name of the Sun Queen?"
            "Default: Aurora":
                $ aurora = "Aurora"
            "Custom":
                $ aurora = renpy.input("What was her name?")
                if aurora == "":
                    $ aurora = "Aurora"
                $ aurora = aurora.strip()
        menu:
            "What was the name of the Moon Princess?"
            "Default: Selene":
                $ selene = "Selene"
            "Custom":
                $ selene = renpy.input("What was her name?")
                if selene == "":
                    $ selene = "Selene"
                $ selene = selene.strip()
    show introfinale 1 with d
    "However, this was all part of an evil plan by Morrigan, the Morphling Queen, ever since you arrived in Arcadia."
    "Only once [mox] received enough power was she able to separate and defeat them."
    show introfinale 2 
    $ textbox = 2
    with d
    show introfinale 2b with sd
    "Leading to a lifetime of peace!"
    stop music fadeout 10
    show introfinale 3:
        ypos 1080
        pause 0.8
        linear 10 ypos 3225
    with sd
    $ renpy.pause(12, hard=True)
    #city scape appears from below
    play ambience1 rain volume 0.3 fadein 5
    play music sad
    show bg skyline:
        xalign 0.5
        ypos 0
    with ssd
    camera:
        linear 6 ypos 500
        linear 5 zpos 800 
    $ renpy.pause(10, hard=True)
    with dissolve
    $ textbox = 1
    "The first thing I noticed about this universe was the rain."
    "The sound of heavy rainfall on glass was so foreign to me. It was proof that I was no longer home." 
    "But one comforting thing remained the same... the ponies here don't wear clothes either."
    scene bg apartment
    show mox neutral
    camera:
        xpos 0 ypos 0 zpos 0
    with d
    mox "Pardon me, but what did you say your name was again?"
    "I looked over to who should be the most familiar person to me in any universe. She was my lover, my best friend, and a complete stranger."
    mc "[mc]."
    show mox surprised with d
    mox "Nope, I've never heard of you! I thought you were just a familiar. I can't believe you have a name and a history! Have we really met before?"
    mc "Calling it a meeting would be an understatement."
    "In a flash of bright purple light, I was teleported here. An all-too-familiar experience."
    "With an interdimensional spell, I was torn from my reality and transported to a new dimension. [mox] must have cast the spell. I never imagined this would happen again."
    show mox sad with d
    mox "I… I can hardly believe it! I'm really sorry if that's true!"
    mc "I'm struggling to believe it myself. I spent so long building my life in Arcadia, making friends, and making love."
    mc "Could all that really be gone... just like that?"
    show mox surprised blush with d
    "[mox] blushes slightly as she focuses on the ‘making love’ part. Her reaction snaps me back to reality."
    mc "There has to be a way to get back!"
    show mox neutral -blush with d
    mox "Hang on! I have a friend arriving any second! We were going to summon a familiar, you know, a magical puppet that just follows orders."
    play sound1 doorbell
    play sound2 move1
    hide mox with d
    "The doorbell rang, and [mox] skipped to another room to answer it."
    "A… doorbell? [mox] doesn’t have a doorbell. This is all different. My senses were a mess, so I had barely taken the time to analyse my surroundings." 
    "This wasn't just a wagon; if this was [mox]'s home, it was a full apartment. Clean and well-lived in."
    "What kind of world is this anyway?"
    "Another character entered the room, her eyes widening in surprise when she saw me. I wish I could say I was equally surprised."
    "I whispered her name under my breath as soon as I saw her..."
    show pen neutral with d:
        xpos 300
    pen "That’s me! But… who are you?"
    show mox surprised with d:
        xpos 900
    mox "Wha!? I didn’t even tell him your name!"
    mc "No need, [mox]. I wasn't kidding when I said I knew you and many others from another universe." 
    "Taken aback, [pen] took a moment to compose herself before continuing."
    show pen happy with d
    pen "Hmm… [mox], put the wine back in the fridge. We’ll need clear heads for this."
    scene bg apartment with d
    "The three of us sat down, sipping tea and discussing how this could be possible."
    "I'd been in many debates and discussions about this topic before, and my knowledge quickly impressed the two mares."
    show pen neutral:
        xpos 300
    show mox awkward:
        xpos 900
    with d
    pen "To summarize... [mox] tried to summon a familiar, but instead brought you from an alternate dimension where you were close friends with another version of [mox]."
    pen "If you really are from an alternate dimension, please prove it by sharing a unique piece of information about me that you would know."
    menu:
        "You’ve pretended to be a lesbian but you’re actually bisexual.":
            show pen wink with d
            pen "No, I’m quite open about my bisexuality. However, given my history of partners, I can see why you’d think that. So, I’ll allow it."
        "You live in a tree with [lil].":
            show pen happy with d
            pen "Huh… That is indeed an incredibly specific, albeit correct fact about me."
        "You and [mox] have a physical relationship.":
            pen "[mox], did you tell him that?"
            show mox awkward with d
            mox "N-No way!"
            show pen laughing with d
            pen "While it’s possible you could have intuited that… I’ll accept it for now." 
        "You’re studying enchantments in college.":
            $ gen1 = 1
            show pen laughing with d
            pen "Correct! That’s quite the passion of mine."
            mc "You’ve already chewed my ear off many times talking about your studies. I hope you figure out that luck magic sometime."
            show pen surprised with d
            pen "Holy shit… You… know about that?"
            "Looks like I got a perfect score."
    if gen1 == 0:
        show pen neutral with d
        pen "You could have prior knowledge of myself or [mox], but for now we’ll accept what you’re telling us for the sake of forwarding the conversation."
    else:
        show pen happy with d
        pen "I must say, I’m rather convinced by what you’re saying, even though I’m struggling to understand how this happened."
    show pen laughing with d
    pen "Could you tell me what the other universe is like?"
    show pen happy with d
    mc "I need to spend more time here to fully understand the differences, otherwise I’ll end up listing a bunch of things you already know." 
    mc "Honestly, I’m still surprised that [mox] lives in an apartment and not a wagon. Are you still a performer?"
    show mox neutral with d
    mox "Oh, yes, I'm a well-known performer. But when I first moved to Arcadia a few years ago, I did live in a wagon."
    mc "So you've been here for a few years instead of a few months. That's quite a surprise."
    mc "A part of me wonders what other subtle differences there are in this universe… But another part of me dreads those differences."
    show pen neutral with d
    mc "Can I really rebuild all those friendships? Will the people here even be the same as in my world?"
    mc "Or am I doomed to be pulled from universe to universe, never settling? It makes me want to shut myself in a room and never leave."
    show mox awkward with d
    mox "[mc]..."
    show pen neutral with d
    pen "You suggested that you were ‘copied’ and ‘pasted’ into this universe, right? There's a chance there's a version of you here."
    pen "And that version might be equine, unlike your unique appearance as a hairless ‘human’."
    mc "That’s unlikely. From my time in the other Arcadia, I learned that [mox] summoned me because I didn’t exist in that universe."
    pen "Huh… So, in every universe where you don’t exist, but [mox] does, she somehow summons you?"
    mc "That’s right, I once lived in a third ‘human’ world that I relinquished to live a fulfilling new life in Arcadia. I never expected to be torn away into a new world again."
    mc "I naively thought it’d be a single hop for every version of me. But if there are infinite universes with infinite possibilities, then... there will always be versions of me pulled into different universes."
    show mox sad with d
    mox "Oh no! I’m so, so sorry! I don’t even know how I did this!"
    mc "You don't have to apologize."
    show pen awkward with d
    pen "I have my doubts too, [mox]. Spells have strict rules."
    show pen neutral with d
    pen "But [mc], let’s say you’re right. Your theory of infinite dimensions and the ability to interact between them contradict each other."
    mc "Really? Why’s that?"
    show pen happy with d
    pen "Simple. If there are infinite universes and possibilities, there would be a universe capable of destroying every other universe."
    "And just like that, my theory is shattered..."
    "But I know multiple universes exist. Some with humans, others with anthropomorphic creatures, and many more..." 
    "Could that all really… not exist?"
    show pen neutral with d
    pen "I hate to erase your existence, [mc], but I’m going to come to my conclusion based on the information so far…"
    pen "In my opinion, it seems far more likely that you’re a familiar that was somehow implanted with memories. You know a lot of things [mox] knows, who’s to say you’re not a fictional character that her brain concocted?"
    show mox neutral with d
    mox "Does that mean he’s going to disappear soon? The spell only lasts sixty minutes, and with my limited abilities, I can’t imagine it lasting even thirty."
    show pen awkward with d
    pen "That certainly remains to be seen."
    "A feeling of dread rises from within me. This can't be right, can it? I know I lived with another [mox] in a wagon. I didn’t disappear then... but if my memories are fake..."
    mc "No way! My memories can't be fake; I know things that even [mox] doesn’t know."
    show pen neutral with d
    pen "You’ve yet to actually prove that yet."
    "Hmm… I need to say something that [mox] doesn’t know but [pen] does… But what? They’re such close friends that anything surface-level won’t work."
    "[pen] loves movies, doesn’t she? No, [mox] would obviously know that too… Maybe something about [lil]? No, [mox] knows her as well." 
    "Wait, that's it! The other five girls! I just need to prove I know something about them."
    mc "[but]! I can tell you something about her that [mox] definitely doesn’t know, and we can confirm it with her."
    show pen surprised with d
    pen "[but]...? Who’s that?"
    mc "... Eh? You don’t know who [but] is?"
    "That’s odd… Did these two not interact at all in the other world? Let’s try someone a bit closer, another unicorn."
    mc "Okay, what about [rub]? I know quite a few secrets about her!"
    show pen neutral with d
    pen "[rub]? Never heard of her."
    show mox happy with d
    mox "That name sounds familiar though…"
    mc "W-Wait… Seriously? [rik], then! [mox] has definitely met her before; she owns a nearby bar!"
    show pen surprised with d
    pen "You mean the star flier of the Storm Chasers? Maybe your memories are just a dreamlike jumble. Nothing you’re saying reflects this reality."
    mc "You’re… kidding… You don’t know these people? [hon]? [cre]?"
    show pen neutral with d
    pen "Nope…"
    show mox neutral with d
    mox "Nuh-uh… Sorry…"
    "I can’t believe this… What kind of crazy universe did I stumble into? They exist…  r-right?"
    mc "Hold it, [pen]! You said my memories don’t reflect reality, but I guarantee these girls all exist. That's my proof that I’m from a parallel reality that mirrors this one."
    show pen happy with d
    pen "We can check that, but… what are the odds? Who gets flung into another universe with the exact same people?"
    mc "I… don’t know… I can only hope."
    show pen neutral with d
    pen "I’m willing to help and give you the benefit of the doubt. But there's one big thing confusing me… How can [mox], who is an excellent magician, but far from an expert in magic, perform this impossible feat?"
    mc "That’s easy. She’s a distant relative of the princess."
    show pen awkward
    show mox awkward
    with d
    "The room goes quiet, and the two mares share a confused glance."
    show pen neutral with d
    pen "What did you say…?"
    mc "The princess of the moon? [sel]?"
    show mox surprised with d
    mox "I’ve never heard of anyone like that. As far as I know, the Queen is an only child."
    mc "What..? But…"
    "Have I made a mistake? A feeling of dread spreads through my gut, my body growing numb. Is this universe really so different? I need to find out."
    "If I could access the mirrors in the castle… A secret collection of portals to other universes. Could I return that way?"
    mc "Would it be possible for me to visit Queen [aur]? There’s a chance I could go back home through her." 
    show pen awkward
    show mox awkward
    with d
    "Once again, the girls look completely baffled."
    show pen neutral with d
    pen "Getting an audience with the Queen is no small feat. The security to the inner city is tight, and you don’t have a pass."
    show mox neutral with d
    mox "Can't [lil] get off her ass and help?"
    show pen happy with d
    pen "Maybe? I could try talking to her... Still, it'd be asking a lot."
    stop music fadeout 5
    scene bg apartment with d
    "Overwhelmed and confused, I take a moment to look out the window and absorb the landscape. This isn't a village, suburb, or fantasy castle. It's a cityscape. With the sky overcast and rain pouring down, it feels grim."
    "Ah… How could I forget? [mox] might be possessed by Morrigan! I could be in danger right now."
    mc "[pen]... You’re a morphling, aren’t you?"
    show pen neutral with d:
        xpos 300
    pen "Huh?! Where did you get that idea? I’m just a regular unicorn. The morphlings and their Queen were defeated a long time ago."
    mc "Seriously? So [mox] isn’t…"
    show mox laughing with d:
        xpos 900
    mox "I’m just [mox]!"
    show pen angry with d
    pen "Tch, seriously… If all this is true, your universe sounds crazy."
    "That’s the tipping point. I can't rely on any of my existing knowledge or expectations about this universe. We're in completely uncharted territory."
    show mox awkward with d
    mox "I want to help you fit into this new universe, especially since I might be the one who brought you here. I feel guilty about this, so…"
    show pen neutral with d
    pen "You’re such a softy! But, ahh… I kind of see what you mean."
    show pen happy with d
    pen "Alright, I’m extremely busy with college, but I’ll try my best to contact the mares you mentioned. I can’t promise anything."
    pen "I still don’t know what you are—a familiar based on [mox]’s memories, a philosophical zombie of your original self, or merely an interdimensional copy. But whatever and whoever you are, there’s a chance you might exist here for the rest of your life."
    pen "We can debate existential topics and get nihilistic, and sure, there could be a version of you copied and faxed over to another universe every second. But right now, you exist here and will always exist in this world."
    show mox happy with d
    mox "That’s right! You need to make the most of it, and I’ll do my best to help you!"
    mc "As you can imagine, this isn’t the first time you both have been so helpful and kind to me. I really appreciate you saving my ass again."
    show pen neutral with d
    pen "There’s only one slight problem left. You were summoned about forty minutes ago, right? There’s a chance you might disappear soon."
    pen "I admit, we actually had some specific reasons for summoning you."
    mc "Oh don’t tell me… It’s mating season?"
    camera:
        linear 40 zpos -350 ypos -100
    show mox surprised blush with d
    with d
    mox "{i}Gasp{/i} He really does know everything!"
    show pen happy blush with d
    pen "Ahaha, if you really have prior experiences with us, then I can only say that we've summoned the right partner."
    pen "Given the circumstances, you may disappear, so it only seems fair that you get to join in."
    show pen horny with d
    pen "And if you don't, let's call it a wild start to your new life."
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
                    $ moxpen1 = 0
                    show pen neutral with d
                    pen "Hm… given the circumstances, that’s fair enough…"
                    show pen wink with d
                    pen "Let’s give this another shot later, lover boy."
                    show mox laughing with d
                    mox "Yeah! – Uh, I mean, r-right…"
                    "These two seem pent up!" 
                    jump intropostblowjob
    $ moxpen1 = 1
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
    layeredimage moxpen1a:
        always:
            "moxpen1abase.jpg"
        always:
            "moxpen1apen [penb].png"
        always:
            "moxpen1amox [moxb].png"
        group eyes:
            attribute 1:
                "moxpen1apene [penb].png"
            attribute 1:
                "moxpen1amoxe 1.png"
            attribute 2:
                "moxpen1ae closed.png"
        always:
            "moxpen1asfx.png"
        group cum:
            attribute cum1:
                "moxpen1acum 1"
            attribute cum2:
                "moxpen1acum 2"
    play music sextheme volume 0.6 fadein 2
    play ambience1 rain volume 0.1 fadein 2
    show moxpen1a 1
    call camerareset2 from _call_camerareset2_7
    $ textbox = 2
    play ambience2 blowjob
    play moans1 moansmisc2
    with d
    call camerabreath from _call_camerabreath_9
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
    layeredimage moxpen1b:
        always:
            "moxpen1bbase.jpg"
        always:
            "moxpen1bpen [penb].png"
        always:
            "moxpen1bmox [moxb].png"
        group eyes:
            attribute 1:
                "moxpen1bpene [penb].png"
            attribute 1:
                "moxpen1bmoxe 1.png"
            attribute 2:
                "moxpen1be closed.png"
        always:
            "moxpen1bsfx.png"
        group cum:
            attribute cum:
                "moxpen1bcum"
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
    call stopbgs from _call_stopbgs_6
    mox "Aahh… {i}Pant, pant{/i} I’ve never actually done that before, was I any good?"
    mc "You were perfect, [mox]."
    pen "Took the words right out of my mouth, [mc]."
    mc "Do you two want more? It’s no fun if only I get attention."
    pen "To be honest, I already came, pretty hard too~"
    mox "Me too. That was enough for me, and…"
    label intropostblowjob:
        $ textbox = 1
        play sound2 equip
        scene bg apartment
        show mox bashful:
            xpos 900
        call camerareset2 from _call_camerareset2_8
        with d
        mox "I’m actually a little nervous about doing anything sexual." 
    play ambience1 ambiencenight
    show pen laughing with d:
        xpos 300
    pen "Hehe, we’ll build you up to it, [mox]." 
    show mox happy with d
    mox "Say, [mc], what was the nature of your relationship with all these girls you mentioned?"
    mc "Uhm, well... they all reached sexual intimacy too. Friends with benefits, or something like that?"
    show mox laughing with d
    mox "Then we shall get you back up to those heights once again! You have my word."
    mox "It’s only natural that your new life should be similar to your old one, right?"
    "While I admit that a part of me is still trying to get back, it’s funny that the [mox] of both universes is sweet and open this way."
    "I have to remember that the equine race is majority female and has a natural tendency to desire an ‘alpha’ partner that they share." 
    "But I can’t help but wonder if it’ll really be as simple as reliving the life I led in Arcadia."
    "Is [but] still a succubus? Did [rik] ever get into that accident? Is [rub]’s clothing business a financial success?"
    "What about [hon]’s father? Is [cre] still the wild party pony running a bakery? And what kind of life could [lil] be living in this strange, new world?"
    scene black with d
    "I only have one way to find out."
    scene bg apartment with d
    "[mox], [pen] and I continued to chat throughout the night; she agreed to look into the names of the mares I mentioned and find leads for their potential locations. For curiosity, if nothing else."
    "But with nothing else to go off, not much else could be solved tonight. [pen] returned home, and it was just [mox] and I once again."
    mc "Are you really okay letting me stay here? We’re technically strangers."
    show mox happy with d
    mox "I’m of two, maybe three minds. For one, you were supposed to be my familiar, and I would have let a familiar stay here, wouldn’t I?"
    show mox bashful with d
    mox "Secondly, I’m curious. This seems impossible to me! There must be some greater meaning to it, wouldn’t you think? Especially with those things you mentioned about a princess."
    show mox neutral with d
    mox "Thirdly, I feel guilty. This is my fault, right?"
    mc "You don’t need to feel guilty; the fact you’re so willing to help me alone alleviates you of any responsibility."
    show mox sad with d
    mox "But still… I do feel responsible. I really empathize with your story—having your entire life uprooted and taken from you like that."
    show mox wink with d
    mox "And we were roommates in that other universe anyway, right? I trust my own judgement, and it sounds like we got a long, pretty well!"
    mc "Heh, you don’t even know the half of it."
    show mox laughing with d
    mox "Then I hope I learn both halves~"
    mox "Now, you must be exhausted. Why don’t we hit the hay and think about this more tomorrow? My bed is extremely comfy!"
    mc "That sounds perfect."
    stop ambience1 fadeout 3
    scene bg moxiebedroom2 with d
    "She wasn’t kidding; her bed was like floating on a cloud. Even though I’ve only been here a few hours, I drifted off to sleep immediately…"
    scene black with d
    "..."
    play ambience1 staticlong volume 0.2 fadein 5
    show space1:
        alpha 0.3
        linear 10 alpha 0
        linear 11 alpha 0.3
        repeat
    show space2:
        alpha 0
        linear 12 alpha 0.3
        linear 13 alpha 0
        repeat
    show silhouette1
    $ textbox = 2
    with d
    "…ve… me… {w=1}{nw}"
    show static with fd
    play sound1 staticshort1
    hide static with fd
    "Help… {w=1}{nw}"
    "You need to… {w=1}{nw}"
    show static with fd
    play sound1 staticshort2
    hide static with fd
    "… Bring the virtues back… {w=1}{nw}"
    "Save… [mc]… Save the… {w=1}{nw}"
    play ambience1 staticlong volume 0.5
    show static with sd
    pause 0.1
    stop ambience1 fadeout 1
    scene bg moxiebedroom 
    $ textbox = 1
    camera:
        zpos -650 ypos -275
    with dissolve
    play ambience1 ambienceday
    "I wake up with dread and anxiety looming over me. A dream, but any remnants of it quickly faded from my mind."
    "What a frustrating experience. How could I have forgotten my dream already, but still feel the effects?" 
    "Virtues… the virtues…"
    "I need to bring them back … But what does that mean?"
    play sound2 equip
    show mox happy with d
    "I turn to my side and spot [mox], staring back at me with the usual adorable look."
    "In this brief moment of time, I could almost forget that this was a different world. Even the familiar sounds of morning birds and wind blowing through leaves were here."
    "Actually… It’s not morning at all; it’s early afternoon!"
    show mox wink with d
    mox "Good afternoon!"
    mc "We woke up so late!"
    show mox laughing with d
    mox "Ahaha, Arcadia is a city that never sleeps! For my work, waking up at this time and working until early in the morning is the norm."
    mc "That’ll take some adjustment…"
    scene bg apartment2 
    camera:
        xpos 0 ypos 0 zpos 0
    with d
    "After showering and breakfast, we settled down in her living room and began to create a plan."
    show mox happy with d
    mc "My goal is the mirror room of the castle."
    mc "To get this, I not only need an audience with the Queen, but I need her to trust me."
    show mox neutral with d
    mox "That’s not all; you’ll need to get a pass into the city first, which is hard enough as it is."
    mc "That’s where [lil] comes in. Thankfully, she’s still the Queen’s student in this universe, so if I befriend her and tell her my situation, that’s my opportunity."
    show mox awkward with d
    mox "I’m not exactly sure how you’re going to do that; the girl’s a total recluse, although maybe that’ll make it easier."
    show mox neutral with d
    mox "What about those other girls you mentioned?"
    mc "They’ll be undoubtedly helpful, but I’m not entirely sure if I want to get too attached to this world in the circumstance that I end up returning."
    show mox happy with d
    mox "Okay, [lil] it is! Head to the giant tree, and I’ll meet you there a bit later. I have a few work-related things I need to do this afternoon."
    mc "I’ll be there."
    scene black with d
    "By the time I was ready to head out, the sun had already set. Operating at night wasn’t entirely illogical considering everyone would be occupied by work during the day, but it was harder to find my way around the city like this."
    show bg tree with d
    "Fortunately, the giant tree was easy to find; even if I got lost, I could always just ask someone to point me in the right direction."
    "Strangely, I found it in the same ‘corner’ of the city; admittedly, everything was so much larger in scale, but despite that, it’s about where I expected it to be."
    "I approach the tree and knock on its door."
    "No response… Of course. But there’s a good chance that the room right above the entrance is [lil]’s bedroom."
    "I look up and call out…"
    mc "Hey, is [lil] there?"
    "I hear the sound of a window opening above, and a pony peeks out."
    lil "Ah, you must be [mc]! I’ll let you in!"
    "A purple aura of magic appears around the handle, and I hear a distinct click as it unlocks."
    play sound1 move
    scene bg library with d
    "And as I step in, I’m at once surprised. While the exterior of the tree was identical to what I remembered, the interior couldn’t be any different." 
    "In fact… is this even a library? This is more like a laboratory!" 
    play music lilytheme
    show lil happy coat glasses with d
    lil "Welcome to my laboratory!"
    mc "Ah, that’ll explain why it looks like a laboratory."
    show lil neutral with d
    lil "Pardonnez-moi?" 
    mc "Oh, it’s just… I was kind of expecting a library."
    show lil laughing with d
    lil "Yes, yes, [pen] said you knew me and that you’d mention a few unusual things like that, but she refused to go into detail… Consider my interest thoroughly piqued."
    lil "Just who are you? What are you?"
    mc "That’s a long story. Let’s start from the beginning. My name’s [mc], and it’s nice to meet you."
    show lil bashful with d
    lil "Heh, it’s a pleasure to – uh- meet you too."
    "She offers a handshake, which I take just like the first time; if I recall correctly, she did this specifically to trick me into touching her so she could feel the texture of my skin."
    show lil happy with d
    lil "Mmhh… Hmm… What species are you? Some kind of… dragon?"
    mc "Dragon? That’s quite an ambitious guess. Have you ever heard of a monkey?"
    show lil shocked with d
    lil "Can’t say I have, but is that what you are, a ‘mon’-‘key’?"
    mc "Ahaha, no, I’m a human, and likely the only one that exists in this universe."
    show lil happy with d
    "[lil]’s eyes gleam with excitement." 
    lil "Fascinating! You came to the right place, [mc]."
    lil "If you would allow me to indulge my inquisitive nature and ‘study’ you, I’d be more than happy to lend my help. Just tell me what you need." 
    mc "Perfect, my main aim is to meet with your Queen. Is that within reason?"
    show lil awkward with d
    lil "Ooohhh… Uhm… That may take some time…"
    lil "Tell you what, I bet you don’t have a city pass, do you? Let’s start with something small like that first, then we’ll negotiate a meeting like that."
    "This [lil] is a little more cunning out the gate than the last! I’ll have to keep my eye on this one."
    "She guides me upstairs, past [pen]’s room and straight into her cluttered office."
    "After navigating around equipment and stepping over books, we finally reach her bedroom."
    scene bg lilybedroom with d
    show lil laughing coat glasses with d
    lil "Take a seat wherever."
    hide lil with d
    "As she fetches a notebook and pen, I glance around… It's a total mess!"
    mc "So, this is where the magic happens?"
    show lil bashful blush with d
    lil "Magic? … Oh, you mean sex! No, never, um…"
    mc "Ahah, my apologies for the awkward pun. I just thought it fit since you’re a unicorn."
    show lil awkward with d
    lil "N-no, I’m the one being awkward… It’s just, well, you just made me realized I’ve never had a male in here with me before." 
    "[lil] falls silent as the realization sinks in."
    show lil happy with d
    lil "Uhm, ah… would you like a drink?"
    mc "Sure, I know that the peppermint tea here is to die for."
    show lil smug with d
    lil "Huh… When I get back, you need to tell me exactly how you know so much!"
    mc "You got it, cutie."
    hide lil with d
    "My teasing remark causes her to leave with a wide blush, by the time she returns, her nipples are a little perkier too."
    "Her natural instincts are kicking in a little, but let’s not get ahead of ourselves. There’s a lot to talk about first." 
    show black with d
    "I give her a brief rundown of my situation. She takes notes the entire time and seems to accept everything with an open mind."
    hide black 
    show lil happy -blush -coat -glasses
    with dissolve
    lil "I’ve never heard of any alternative universes, but you’ve already let enough hints slip to imply that you know me and this tree well enough."
    lil "It’s no wonder [pen] was tight-lipped about you. Unwrapping an enigma like yourself is a present in itself!" 
    lil "I’m curious, what was my other self like?"
    mc "The other [lil] was an alicorn and a princess-in-training by the time I left, but prior to that-"
    show lil shocked with d
    lil "What?! I was an alicorn?!"
    "Her attention is ripped away from her pad and pen and she turns towards me."
    mc "Oh, yes, fresh off your success defeating Morrigan with the help of [mox] and the other five Virtues."
    show lil neutral with d
    lil "Huh… This is starting to sound like some kind of fanfiction. [mox] is a clown whose usage of magic makes a mockery of all unicorns, and Morrigan was defeated before I was even born! And what’s this about five others?"
    mc "Well, the virtues were your closest friends. Together you made up the six Virtues of Concord, a powerful force that, when combined, had the power to rival even the Queen. This power was entrusted to you six in case of emergencies."
    show lil bashful with d
    lil "This tale you’re spinning sounds fun, but… I don’t think I can believe you."
    mc "How is that story harder to believe than me being from another universe?"
    show lil wink with d
    lil "Eh, I wasn’t quite sure if I could believe that part either."
    mc "Proving that part is easy. All I need to do is mention something I shouldn't know about you."
    show lil smug with d
    lil "And what might that be?"
    mc "That you have a dildo… Right here!"
    play sound2 equip
    "I open her bedside drawer, and a pink dildo hastily hidden inside springs out."
    show lil shocked with d
    lil "Aaaaahhh! How did you…?!"
    show lil shocked with d:
        linear 0.3 xalign 0.75
    "She pushes past me and clumsily tries to pick up the dildo, but accidentally kicks it, causing it to roll away further until she finally catches it."
    show lil bashful with d:
        linear 0.3 xalign 0.5
    lil "Fine, fine, I believe you!"
    lil "Your story… It just seemed too good to be true." 
    "[lil] places her dildo back in the drawer, pouting."
    show lil smug with d
    lil "Me, a princess… How do we make it happen? I’m willing to follow the actions from that other universe step-by-step!"
    "I scratch my head awkwardly, thinking for a few moments."
    mc "Do you even know [hon], [but], [cre], [rub], and [rik]?"
    show lil happy with d
    lil "Never heard of them, but judging by the fact you mentioned five names, I can only assume that they were the other Virtues." 
    mc "That’s a problem. You six were already friends before I met you in the other universe. I’m not entirely sure what went wrong here." 
    show lil awkward with d
    lil "Friends, eh? I was never good at making friends, socializing only ever impedes progress with my studies and work."  
    mc "Shy in this world too, hm?"
    show lil angry with d
    lil "N-No!  I never needed friends. People are exhausting, I just like being alone."
    mc "Don’t you get lonely?"
    show lil sad with d
    lil "Sure, sometimes… But there’s not much I can do about it."
    show lil bashful with d
    lil "Even when I was at college, I tried making friends, but I always fell short." 
    show lil awkward with d
    lil "I’m just a boring, unlikable, vacuum of charisma. I never know what to say, and people never talk to me, so…"
    show lil sad with d
    lil "Whether I'm here alone in my lab or in a room full of people, I'm always alone. So why not stay here?"
    mc "{i}Sigh{/i} I like you."
    show lil neutral blush with d
    lil "Y-You do?"
    mc "Yes, you're sweet and always ready to help those you care about."
    mc "Sure, you struggle to make friends, but when you do, you're a true friend."
    show lil awkward with d
    lil "I… uh… I see…"
    mc "In the Arcadia I knew, Queen [aur] noticed that weakness and encouraged you to overcome it as the suburbs ambassador."
    show lil happy -blush with d
    lil "Really? [aur] is usually busy, so she lets me work at my own pace."
    mc "This universe… It’s like there was one pivotal event that spiralled out, causing almost everything to be different."
    show lil neutral with d
    lil "Hmm, but what? I wonder…"
    show lil happy with d
    lil "If we bring all these special girls together, Queen [aur] will definitely want to meet with us."
    mc "Once I’ve met the others, we can arrange a meeting for all six of you."
    show lil wink with d
    lil "And I’ll get that pass for you to enter the city as soon as I can. Some of your friends might be in there."
    mc "You’re amazing, as always, [lil]."
    show lil bashful blush with d
    lil "O-Oh… I am?"
    mc "Of course, and I haven’t forgotten about my side of the bargain. You mentioned wanting to ‘study’ me?"
    show lil laughing -blush with d
    lil "I got so caught up in your stories that I forgot."
    mc "You want to study my DNA, yes?"
    show lil smug with d
    lil "… Wait a second, ahaha… This has all happened to you before, hasn’t it?"
    mc "I wondered how long it’d take you to notice."
    show lil shocked blush with d
    lil "Oh my god… Oh my god! Just how far did you go with the other me?"
    menu:
        "Balls-Deep.":
            "I gently push her against the wall, looking serious."
            mc "Balls-deep."
            lil "Ooohhhh myyyy gooood…"
            show lil bashful with d
            lil "B-But… I’m a, uh, v-virgin…"
            mc "Wouldn’t be the first time I’ve taken it."
            show lil shocked with d
            lil "{i}Gulp{/i}"
            lil "Now hold on a minute! Just because it's mating season doesn’t mean I’m some floozy who has sex with the first man she sees, and I bet my other self didn’t sleep with you immediately."
            mc "You’ve got me there."
        "(Lie) Not much.":
            show lil wink with d
            lil "Really? That means anything we do together is new." 
            mc "Hey, that was pretty smooth for you."
            show lil bashful with d
            lil "What do you mean {i}for me?!{i}"
            mc "I’d genuinely like you to study my DNA, just to see if there’s an identical match in this universe. You never know."
    menu:
        "Want to lend a hand?":
            show lil awkward with d
            lil "Hmph, I believe you’re more than capable of doing such a thing yourself!" 
            mc "Ooo~ Looks like this [lil] has some sass."
            show lil wink with d
            lil "Hah, that’s right! Wait here, I’ll grab a vial for your ‘DNA’."
            hide lil with d
            "Little does she know, the DNA extraction with the other [lil] started like this too. I bet she’ll offer to help in a few moments."
        "Here goes nothing…":
            pass
    stop music fadeout 3
    show lil neutral 
    show povmasturbation:
        ypos 200
    with d
    "She hands me a vial and watches expectantly. With newfound confidence, I get to work, holding the vial in one hand and my dick in the other." 
    "[lil] defiance melts into profound curiosity. Even my technique intrigues her. The human penis is quite an oddity to her."
    show lil bashful with d
    lil "Uhm, I… Uh… Wow…"
    "The arousal builds, and my erection grows. I make no attempt to hide my glances at [lil]’s breasts and crotch."
    "She can’t help but bite her lip, her eyes fixed on the prize." 
    show lil awkward with d
    lil "{i}Gulp{/i} (He’s… totally masturbating to me right now, isn’t he?)"
    "Her thighs begin to brush back and forth, an almost instinctive move to try and sooth the natural itch building up in her loins."
    "I slow down a little, pacing myself to enjoy this experience longer, not that [lil] would know."
    show lil smug with d
    lil "{i}Eh-hem{/i} I shouldn’t be watching, should I? I’m just… going to excuse myself and go over… here… right."
    play music sextheme
    show lily1a 1
    $ textbox = 4
    call camerabreath from _call_camerabreath_19
    play moans1 moansmisc2 volume 0.4
    with d
    "[lil] turns tail and wanders off to a nearby desk. I was almost disappointed until I noticed her tail flicking from side to side, giving a glorious view of her ass."
    "Too shy to ask, so she tries to be subtle, eh?"
    "The light hits her pussy in such a way that I can see it starting to glisten. Because of the exciting view, my hands start to naturally speed up, catching her attention as she peeks back behind her shoulder." 
    "My eyes linger on her rear as she bends over further, her tight ass practically begging for attention."
    $ lily1 = 0
    $ lily1spank = 0
    menu:
        "{i}Move in!{/i}":
            $ lily1 = 1
        "{i}Finish here{i}":
            mc "Ohh, that’s a good view… Out the window, I mean~"
            lil "Yes, uhm, quite!"
            lil "I wouldn’t mind if you… {i}Eh-hem{/i} Had a closer look…"
            menu:
                "{i}Take a few steps closer{/i}":
                    $ lily1 = 1
                "I’m already close!":
                    mc "I’m getting pretty close! I’ll be able to cum in the vial any second!"
                    lil "A-Already?! (Is my ass that nice?)"
                    jump lilybuttjob3
    play sound1 move
    "I took a few steps closer, and she feigned inattention as she turned back to her notebook."
    show lily1a hands with d
    "But before long, I was already lightly squeezing her soft flanks, causing her to squirm slightly."
    lil "(Ooohhh, he's actually touching me! Nngghh, so close to my pussy too... I'm getting so wet, aahhh...)"
    show lily1a 2 with d
    "She continued ignoring me, almost blatant permission to go further, while her tail seductively flickered back and forth."
    lil "(Get a hold of yourself [lil]! You barely know this guy!)"
    menu:
        "Slide your cock between her cheeks.":
            show lily1a buttjob1 with d
            "I couldn’t help but position myself lower, sliding my cock between her fluffy cheeks and making slight contact with both her dripping wet labia and tight pucker."
            "The contact immediately made her jolt up, but rather than pulling away, she turned back towards me."
        "Press your cock against her pussy.":
            hide lily1ahands with d
            "I started to rub my tip up and down her labia. She felt incredibly hot to the touch; with how aroused she is right now, I respect her for holding back this much."
            "As my tip grew more slick, I angled it closer to her pussy, causing her to squirm and move her hips away slightly."
    show lily1a 1 with d
    lil "Don’t put it inside… Because, uh-uhm - It’ll mess up the DNA."
    mc "Relax; your ass is more than enough for me."
    show lily1a buttjob1
    with d
    "I gripped her hips firmly and began to thrust back and forth between her tight ass cheeks; in response, she let out a moan mixed with pleasure and embarrassment."
    camera:
        linear 0.1
        linear 0.5 xpos -5 ypos -5
        linear 0.1
        linear 0.4 xpos 5 ypos 5
        repeat
    play moans1 moansmisc3
    play ambience2 handjob2
    "Only a few blissful seconds later, she began to move too – slowly at first – rocking back and forth against me. My cock glides against her anus and virgin pussy with ease."
    show lily1a 2 with d
    lil "Ooohhhh… This is… depraved… but... so hot…"
    mc "It’s amazing; that’s what it is." 
    "We both began to pick up speed, the juices dripping from her pussy lubricating my shaft and creating slick friction between our genitals."
    "With her ass at my mercy, I get a naughty idea."
    menu:
        "{i}Spank her{/i}":
            play sound1 spank
            show lily1aspanked:
                alpha 0.3
            with d
            "With a clean hit, I give [lil] a crisp smack which causes her to yelp with a delight that seems to take even her by surprise."
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
                    lily "Uuuoohhh... I'm getting so wet! Nnghh..."
                    mc "You love that, don't you? Naughty slut~"
                "{i}Show mercy{/i}":
                    jump lily1amercy
        "{i}Show mercy{/i}":
            label lily1amercy:
                "I brush my fingers through her fluffy butt, causing a shiver up her spine."
            lil "Mmmhh... Your hands feel so firm."
    "I started angling my cock increasingly into her, not only creating more friction but also creating more of a risk of entry. Every time I slid over her vaginal entrance and pucker, my tip would get caught and push inside ever-so-slightly."
    "And each time it did, I could feel [lil] tense up, more impassioned moans slipping from her lips." 
    lil "F-Fuck!"
    "She let out an ecstatic whinny that sounded like she was enjoying this perverse act even more than I was. Her pace didn’t falter; it intensified, each powerful thrust driving me closer to climax." 
    "I could feel it building up inside me, getting ready to erupt – an unstoppable force of pleasure threatening to engulf me completely."
    mc "I’m – I’m close!"
    "She looked back and gasped, her body shivering with pleasure as she began to grind her ass against me harder than ever, leaving me teetering on the brink of release."
    play sound2 cum
    show lily1a buttjob2
    with c
    label lilybuttjob3:
        play sound2 cum
        show lily1a cum
        with c
    mc "Oohhh, I’m cumming!"
    play sound2 cum
    with c
    play sound2 cum
    with c
    "I moaned out in ecstasy as I reached climax, my body convulsing after a wave of hot cum shot forth from the tip of my cock, painting her ass white with my seed."
    play sound2 cum
    with c
    play sound2 cum
    with c
    lil "Nngghhh, so much! {i}Pant, pant{/i}"
    call camerareset1 from _call_camerareset1_5 
    call stopbgs from _call_stopbgs_16 
    show lily1a 1 cum -buttjob2
    with d
    "After countless loads, the intensity of my orgasm began to slowly subside, and I reveled in the afterglow of this sudden, depraved experience."
    "[lil] takes the vial and scoops up some of the cum from her butt. Skimming the top to avoid her fur."
    lil "Perfect! Well, not entirely perfect…"
    stop music fadeout 3
    scene bg lilybedroom 
    show lil bashful 
    $ textbox = 1
    with d
    "She pouts and turns back to my flaccid penis."
    if lily1 == 1:
        lil "(I was so close to cumming! Ugh, but the grinding wasn’t enough… Eugh, so frustrating!)"
    else:
        lil "(That was a close one... I might have let him thrust it in then and there... I need to keep my impulses in check.)"
    if lily1spank == 1:
        show lil horny with d
        lil "(It was so hot when he spanked me though... I didn't know I'd actually enjoy something like that...)"
    mc "Something wrong?"
    show lil smug with d
    lil "N-no, everything is fine."
    show lil neutral with d
    lil "Hm? It’s happening again."
    play sound1 earthquake volume 0.7
    camera:
        linear 0.3 zpos -16
        block:
            linear 0.2 xpos 4 ypos -4
            linear 0.1 xpos -3 zpos -12
            linear 0.3 ypos 4 
            linear 0.2 xpos 4 ypos -3 zpos -16
            linear 0.2 ypos -4
            linear 0.1 xpos -3 zpos -24
            linear 0.3 xpos 4 
            linear 0.2 ypos 3 zpos -16
            repeat
    "The building starts to tremble, vibrations resonating through the floor and sending shivers up my legs. The walls shake, ceiling lights swing, and various ornaments clatter around."
    mc "E-Earthquake?!"
    lil "This happens a few times a week. Not normal where you’re from?"
    mc "Absolutely not!" 
    call camerareset from _call_camerareset
    "Eventually, the tremors cease, and the dust settles. The room remains intact, evidently designed to handle this on a regular occurrence."
    show lil bashful with d
    lil "Well, I have a busy day of study and work ahead of me though, so…"
    "Her eyes dart to the drawer where her dildo is stored. Is she really so casually accepting of an earthquake like that? It really must be normal here."
    show lil happy -blush with d
    lil "Come back sometime, I’ll have the results of your DNA and your city pass."
    mc "You’re a lifesaver, [lil]!" 
    play sound2 move
    scene bg library with d
    "I step out of her room, feeling hopeful. Now I just need to find the other five."
    play music penelopetheme
    play ambience1 ambienceday
    show pen happy with d
    pen "Ah, there you are! I thought I heard some chattering in [lil]’s room."
    pen "You’d think a big tree like this would muffle the sound, but actually it just causes it to echo and spread like crazy."
    mc "Did you hear anything?"
    show pen laughing with d
    pen "Oh, nothing specific. Just mumbled talking, not the words themselves."
    if lily1 == 1:
        "That probably also means she heard mumbled moaning."
    show pen happy with d
    pen "Out of curiosity, I looked up a few of those people you mentioned last night."
    show pen neutral with d
    pen "What can I really say? I’m shocked. Every person you mentioned seems to have existed at some point."
    pen "So unless this is some elaborate prank by [mox], you’ve proven you’re from another universe."
    mc "I like how you disbelieve the concept so much that your mind briefly considered it to be a prank."
    show pen wink with d
    pen "It still seems more likely than anything else, but at this point, why shouldn’t I accept the situation at face value and ride the wave. Sounds more fun to me."
    "She hands me a piece of a set of crisp, freshly printed papers."
    mc "Directions to… a farm, a brothel, an abandoned bakery… and that’s it?"
    show pen happy with d
    pen "Let me break it down. [hon] is the sole owner of the nearby farmlands to the north, that was easy to find."
    show pen laughing with d
    pen "Same with your friend [rub] at the brothel; she’s the madam there. Something about intellectual lusts, seemed like my kind of place, to be honest."
    mc "Interesting… And the others?"
    show pen neutral with d
    pen "Well, those were the tough ones. I found a bakery business that might be associated with [cre], but as you can see from the pictures, it’s been shut down for at least a year."
    pen "I knew I’d heard the name [rik] before. She’s the star flier of the Storm Chasers and one of the most famous people in the city. Meeting her might be even harder than meeting the Queen."
    mc "Hah, I knew she had it in her. She loves booze, maybe I can frequent her favourite bar and run into her that way."
    show pen awkward with d
    pen "Right, well… The only thing I had on [but] was the name of someone that lived over fifty years ago. That couldn’t possibly be your girl, right?"
    mc "That should be the one. What happened to her?"
    show pen neutral with d
    pen "No information past a certain point. All I know is she lived in Nevermore Forest and was doted on by a minotaur prince from Lendal. He died around the same time records on [but] disappeared. But you probably knew that already."
    mc "Vaguely… It’s worth checking the forest to see if her cottage is there."
    show pen surprised with d
    pen "You want to go into Nevermore Forest? That one’s all yours, that place has terrified me since I was a filly."
    show pen neutral:
        linear 0.3 xalign 0.25
    show mox surprised:
        xalign 0.75
    with d
    mox "I hear there are monsters in there!"
    show pen angry with d
    pen "There are. Feral monster girls, who have a taste for men."
    mc "I’ve dealt with those types before; they’re more harmless than not."
    show pen surprised with d
    pen "Is there anything you haven’t done?! – Also, hey [mox]."
    show mox laughing with d
    mox "Hiya!"
    mc "Life in Arcadia is never boring, that’s for sure."
    show mox happy with dissolve
    mox "Ooo, ooo! Fill me in on what I missed!"
    pen "C’mon, let’s head to my room and we’ll recap."
    stop music fadeout 3
    stop ambience1 fadeout 3
    scene bg black with d
    "Fifteen minutes later…"
    play music casual1 fadein 5
    show bg peneloperoom
    show pen neutral:
        xalign 0.25
    show mox happy:
        xalign 0.75
    camera:
        zpos -350 ypos -100
    with d
    pen "How can we guarantee that the Queen will help you with these ‘mirrors’? What’s so special about them?"
    mc "I wish I could tell you, but the Queen I know placed a spell on me that literally prevents me from explaining what those mirrors do."
    mc "What I can say is that they’re my best bet to get back."
    show mox surprised with d
    mox "Consider my curiosity piqued."
    show pen happy with d
    pen "Try talking about the mirrors."
    mc "I mean… I can’t. It’s not like my words go silent; I just genuinely can’t talk about them."
    show pen neutral with d
    show mox happy with d
    pen "Then try talking about… my mirror over there!"
    "I look over to a nearby wall mirror hanging over a mantelpiece."
    mc "Hm... If I were to walk through that... I... Hm... Seems like I can't say anymore. The Queen’s magic cannot be easily fooled."
    show pen laughing with d
    pen "You’re from another universe, talking about walking into a mirror – I get it."
    show mox laughing with d
    mox "It’s a metaphor! They’re not mirrors at all!"
    show pen neutral with d
    pen "Exactly~ Although I find the idea of the castle having portals to other universes highly unusual."
    show pen happy with d
    pen "That being said, I’m totally in. I’ll help you under one condition."
    show mox happy with d
    mox "Yeah, me too! What’s your condition, [pen]?"
    play music comical
    show pen horny blush with d
    pen "I want to feel that thick cock of yours spreading me out…"
    show mox surprised blush with d
    "[pen]’s lustful declaration takes both [mox] and me by surprise."
    show mox awkward with d
    mox "I’m horny too, but damn, [pen]!"
    show pen wink with d
    pen "Why pretend he’s not hot? His cock looks amazing. His smell alone is making my clit tingle."
    pen "I masturbated into a stupor last night. I don’t think I’ll be able to concentrate and help properly until my pussy gets a pounding."
    mc "Consider me flattered."
    show mox surprised with d
    mox "But we’re in heat! We might get pregnant…"
    show pen laughing with d
    pen "Pfft… Don’t you see the golden goose for its eggs? Our friend here isn’t a stallion, and that is a rare commodity this time of year."
    show mox horny with d
    mox "Ooohh… fuck… Now I get why you’re…"
    show pen horny with d
    pen "Yep."
    menu:
        "You’ve got a deal.":
            $ moxpen2 = 1
        "Let’s do this another day.":
            $ moxpen2 = 0
            show pen neutral with d
            pen "Awh, really?"
            show mox wink with d
            mox "You could always use a familiar, [pen]."
            show pen awkward with d
            pen "Sure, but we know that doesn’t feel the same. Maybe it’ll be enough to tide me over... You owe me.~"
            mc "Thanks for understanding. I just need some time to adjust to this world. It still hasn’t been twenty-four hours."
            pen "When you put it like that, wild sex does seem a little inappropriate."
            jump intropart3
    show pen laughing with d
    pen "Let me show you to my room…"
    stop music fadeout 3
    scene black with d
    call camerareset2 from _call_camerareset2_9
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
    call camerabreath from _call_camerabreath_11
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
    layeredimage moxpen2c:
        always:
            "moxpen2cb"
        always:
            "moxpen2cmox [moxb]"
        always:
            "moxpen2cpen [penb]"
        group meyes:
            attribute m1:
                "moxpen2cmoxe 1"
            attribute m2:
                "moxpen2cmoxe 2"
        group peyes:
            attribute p1:
                "moxpen2cpenea [penb]"
            attribute p2:
                "moxpen2cpeneb"
        group cum:
            attribute cum:
                "moxpen2ccum"
    scene moxpen2c m1 p1
    call camerabreath from _call_camerabreath_12
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
    "—I exploded, unloading copious amounts of hot, thick cum deep into her womb, filling her up to overflowing."
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
    call camerabreath from _call_camerabreath_13
    call stopbgs from _call_stopbgs_8
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
    play sound2 equip
    scene bg bedroom2 
    $ textbox = 1
    call camerareset from _call_camerareset_1
    with d
    "The girls hop off my body and instead snuggle up to my sides. [mox] on my left shoulder, [pen] on my right."
    "Huh… How did I end up here? I was transported into this universe only about 12 hours ago." 
    label intropart3:
        show pen neutral:
            xalign 0.25
        show mox happy:
            xalign 0.75
        with d
        show black:
            alpha 0
            linear 60 alpha 0.25
        stop music fadeout 3
        play ambience1 ambiencenight fadein 10
    pen "There’s been a thought nagging at me..."
    pen "Let’s say you do get back, [mc]… What if there are two of you?"
    mc "I figured this would come up. What if I was ‘copied’ instead of ‘pasted,’ right? The original me probably still exists."
    mc "I've thought about it. Even if there are two of me, I think my Arcadia would be open and accepting of that. Might even be fun."
    show pen raised with d
    pen "You’ve got me there, but let’s take my example to its next logical conclusion... What if there are three of you? Four of you? Infinite universes, infinite you. Or so the theory goes."
    show mox wink with d
    mox "Mmm… I wouldn’t mind infinite of him."
    mc "That’s probably the exact problem, [mox]! So you're saying this issue is bigger than me?"
    show pen sad with d
    pen "How can you ever rest knowing that you could get torn into yet another universe, and another, and another, forevermore?"
    pen "The thought alone haunts me."
    mc "It could be happening to us all, though."
    show pen neutral with d
    pen "Maybe – but we know it’s definitely happening to you."
    pen "If I were you, I’d do everything to anchor myself to this reality, so you never have to go through this again."
    pen "If all this interdimensional magic is real, there should be a way to nullify it. Ordinary magic has such counters."
    mc "Now that’s some real food for thought."
    show mox laughing with d
    mox "And I’m starving!"
    "[pen] and I glance over at [mox], whose stomach growls."
    show mox neutral with d
    mox "Sorry, hearing ‘food’ sent me over the edge there."
    show pen laughing with d
    pen "Hah, all right. You two scoot off now and keep me in the loop with your progress finding those ladies."
    mc "Will do. Thanks again, [pen]."
    play sound2 move
    call camerareset2 from _call_camerareset2_17
    scene map night
    "[mox] and I leave the treehouse and head to one of her favourite restaurants. The food is excellent but far more expensive than I’m used to."
    "This may be the perfect opportunity to try and learn some historic and cultural differences between the Arcadias."
    "Once back at her place, we settle on the couch to talk."
    play music moxietheme fadein 3
    scene bg apartment
    show mox happy:
        xalign 0.75
    with d
    mox "I wasn't just completely goofing off this afternoon, I picked up something you could use at work!"
    "[mox] takes something out of a nearby drawer and hands it to me. It's a device I certainly recognize but of a type I haven't seen in a long time."
    show phonebg:
        xpos -500
    mc "A mobile phone? A smart phone no less."
    mox "Correct! Are you familiar with how to work it?"
    mc "More or less, let's see..."
    play sound2 phonestart
    show phonemenu:
        xpos -500
    with d
    "I press the button on the right and it turns on."
    mox "This is an old phone of mine, I thought it'd be a lot more useful for you than gathering dust in my drawer."
    mox "I already have a bunch of things already installed on there. I'm not sure what you do know and what you don't, so just ask me anything!"
    menu introphonetut:
        "About MSGs":
            mox "If you give your number to others, they'll be able to send you handy messages from wherever, whenever. I'd make a habit of sharing your number with everyone you meet."
        "About To-Do":
            mox "I use this app all the time! It keeps me on track for what I have to do next."
            mc "Good idea. I'll add all my leads and goals in here so I can stay focused."
        "About the Gallery":
            mox "If you take any pictures, they'll appear here. You can browse them again on your phone whenever you want."
            mox "I think there might already be a few in there already!"
        "What's Friendship Feed?":
            mox "That's a social website where people post general updates. You can use it to keep up to date with your friends, or things happening around the city." 
            mox "Like the other apps, you'll see a notification if there's a new post there."
        "What are Enchanted Threads and Midnight Emporium?":
            mox "Enchanted Threads is a favorite online store of mine. It typically sells clothing. It's handy for me because I wear a cape and hat when performing."
            mox "And Midnight Emporium, uhm... is a little embarrassing. It's an online sex shop that sells whatever your imagination can conjure, and worse!"
        "About Music":
            mox "Here you can listen to any music. This phone is already full of music, so feel free to give it a listen."
        "About Cheats":
            show mox wink with d
            mox "Ah, that's just some silly app I forgot to remove. It promised to add 'cheats' to reality, like infinite money, and out of curiosity I installed it. Obviously I never got it to work. Maybe you'd have better luck? Ahaha."
            show mox happy with d
        "About Settings":
            mox "Here you can change the phone's background, various sound settings, text size, and other things. You know."
        "I think I got it (Continue)":
            jump introphonetut2
    jump introphonetut
    label introphonetut2:
        hide phonemenu
        hide phonebg
        with d
        show mox bashful with d:
            linear 0.3 xalign 0.5
    show screen vnui
    mox "Oh, and you'll be able to open your phone up almost whenever you want! I won't blame you for being rude! Although some may~"
    mox "Why don't you give it a try now? I'll send you a message!"
    play sound2 phonenotification
    $ unread += 1
    $ unreadmox += 1 
    $ moxmsg1 = 1
    label moxmsgloop:
        "(You just received a message! See that notification in the top right? Try pressing the phone icon!)"
    if moxmsg1 == 1:
        show mox happy with d
        mox "Aren't you going to check it?"
        jump moxmsgloop
    else:
        mc "Wow, that was quite a forward message!"
        show mox bashful blush with d
        mox "Haha, it's easier to be more forward when it's over text instead of face-to-face."
        mc "But I'm right here!"
        show mox laughing -blush with d
        mox "Hey, don't apply logic to the stuff I say!"
    mc "Thank you so much, I only have one question... Where am I supposed to put this? I have no pockets."
    show mox laughing with d
    mox "Ahah, don't worry, I thought about that too! Here, take one of my satchels."
    mc "You're too good for me."
    show mox wink with d
    mox "I know you'll return the favor for all my help eventually, right? Ehehe."
    mc "That's a tall order considering how much you've done for me already. But I will try my best."
    show mox horny with d
    mox "Awh, I was only kidding! Well, actually I was trying to make a naughty joke."
    mc "Ahaha, if that's the case, I can deliver!"
    show mox laughing with d
    mox "Oh I bet you can, Mr. Biggus Dickus."
    mc "I've been wondering, the [mox] I know had only recently moved to Arcadia, but you seem to be comfortably settled here. How long have you been living in Arcadia so far?"
    camera:
        linear 10 zpos -350 ypos -150
    show mox happy with d
    mox "I’ve been living here for a couple of years now, moved in from a village to the west."
    mc "You were originally in a wagon, right?"
    mox "Yep! My magic act took off, so I sold the wagon last year and bought this apartment."
    mc "Wait… {i}bought{/i}? Not rented?"
    show mox laughing with d
    mox "Correct! You could say I’m rolling with the dough."
    mc "I think the saying ‘rolling {i}in{/i} the dough’. Or is that yet another subtle change in this universe?"
    show mox wink with d
    mox "No, you’re right, but I mean by ‘with,’ is that I’m caught in the same rolling pin as the money. Rather than riding the money wave, I’m swept up in it."
    mox "Honestly, I was hoping for company like you. It’s a great reason to try all the places I wouldn’t go alone."
    mc "If you don’t mind me asking, why do you think you’re so successful? You were always moderately successful in my universe, but this is unprecedented."
    show mox neutral with d
    mox "Every time you’ve described your world, it’s seemed a little brighter and happier than this one. Maybe an entertainer like me isn’t needed as much there."
    mc "Yeah… I’ve noticed a gloom over this Arcadia. What exactly is it?"
    show mox awkward with d
    mox "Where do I start? We're in a nice part of town, but the poverty line is rising, refugees from the dark lands are flooding in. Imports have stopped, and we're facing food shortages as crop yields fall."
    mox "The Queen’s rule is becoming more oppressive. I can’t blame her entirely."
    show mox sad with d
    mox "The ground quakes, nights grow darker. They say the end times are near."
    hide screen vnui
    menu introhistorym:
        "Poverty and Refugees?":
            show mox neutral with d
            mox "The world is changing rapidly, becoming more perilous by the day. When a region is abandoned and becomes uninhabitable, we consider it part of the 'dark lands.'"
            mox "Initially, the influx of refugees boosted Arcadia's growth and economy. But now, we've reached a tipping point. The city can't keep up with the demand, and poverty is casting a shadow over everything we've built."
            jump introhistorym
        "The Queen’s Impatience.":
            show mox awkward with d
            mox "Queen [aur], in her efforts to maintain control and order, has resorted to harsher methods. Stricter laws, greater punishments, and an unyielding grip on power."
            mox "Arcadia has been under her rule for thousands of years and was once considered a utopia. But in such demanding times, no ruler can come out looking good."
            mox "That’s not to say she’s been perfect. The weight of the world’s troubles has hardened her heart."
            jump introhistorym
        "Quakes and the Giant Ravine":
            show mox angry with d
            mox "I wish I could explain the earthquakes, but no one really knows why they happen. They're incredibly disruptive, though the city is built with safeguards against them."
            mox "Then there's the massive, jagged scar of a ravine cutting through the city. It's been part of Arcadia as far back as history goes."
            mox "Conspiracy theories suggest it's not a natural formation."
            jump introhistorym
        "Darker Nights?":
            show mox sad with d
            mox "Yes, the nights seem to be getting darker, but only in the dark lands."
            mox "It’s not due to a lack of moonlight, sun, or stars – it’s like the very essence of night is growing deeper, more oppressive."
            mox "Some say the sun is weakening, but even that doesn’t fully explain it. It’s enough to make you wonder if the end times are really near." 
            jump introhistorym
        "(Continue)":
            show screen vnui
            "I sit back and ponder everything [mox] has said for a few quiet moments."
    stop music fadeout 10
    mc "I wonder, what could be causing all these changes? What's the key difference between this universe and the other?"
    show mox awkward with d
    mox "Well…"
    show mox angry with d
    mox "Your world… I bet it doesn’t have {i}them{/i}."
    mc "Who are ‘they’?"
    show mox awkward with d
    mox "It's taboo to talk about them. People say that even thinking about them can summon them... But since you’re new, they’re..."
    play ambience1 ambiencerain volume 0.5
    play sound thunder
    show black:
        alpha 0.2
    with d
    with c
    mox "…{i}Nightmares{/i}."
    mox "Strange shadowy creatures that have been slowly consuming the land, maybe even the planet."
    mox "The only place that seems safe is under the Queen's light, as the sun shines less elsewhere."
    "As I try to piece together the puzzle in my mind, it all starts to click."
    mc "That may explain the population density, rapid technological advancement, the Queen’s attitude, and why the Virtues never met."
    mc "It even explains why you moved here so much sooner."
    show mox sad with d
    mox "Yeah, my village is dark now." 
    mc "In the ‘dark lands’?"
    show mox awkward with d
    mox "Yeah…"
    mc "I’m sorry to hear that."
    play sound2 equip
    hide mox with d
    "I huddle in close, wrapping my arm around her shoulder. She reciprocates, leaning in on me."
    mc "It makes sense why you’re so determined to make sure no one else has to endure such hardships."
    show mox happy with d
    mox "Hehe, you’ve got me figured out. That's the fourth reason I wanted you to stay, because you’re just like me."
    scene bg skyline
    camera:
        xpos 0 ypos 0 zpos 0
    with d
    camera:
        linear 15 zpos 250 ypos -500
    "My gaze drifts toward the bustling city outside the window as rain starts to trickle, soon pouring down."
    mox "Arcadia is rough around the edges, but it truly is a beacon of hope."
    "[mox] leans closer to me, seeking comfort. She feels warm."
    mc "I wonder if my meddling could help this world. If I bring the power of the Virtues together, maybe that could stop this encroaching darkness."
    "Despite my ambitious claim, [mox] smiles widely."
    mox "Then I promise you, [mc], I won’t let you face these challenges alone."
    "As if on cue, thunder rumbles in the distance. The cityscape outside transforms into a blurred painting of neon lights struggling against the relentless downpour."
    scene bg apartment
    show mox happy 
    camera:
        zpos 0 ypos 0 xpos 0
        linear 20 zpos -350 ypos -150
    with d
    mc "You really are the one for me, aren’t you?"
    mox "Hmm?"
    mc "No matter what universe you’re from, or what factors have affected you, you always seem to be the perfect girl for me."
    show mox bashful blush with d
    mox "Aahhh… Really, now?"
    "After a few more moments of silence, I feel her hand gliding across my chest, and she turns to face me."
    show mox happy with d
    mox "You know…"
    "She hesitates for a moment, her gaze softening even more. Her breath brushes against my ear, sending shivers down my spine. The warmth of her closeness is comforting yet electrifying."
    show mox bashful with d
    mox "It’s not just about helping each other. There are… other things that are important too." 
    "Her voice is a gentle caress, carrying a weight of unspoken emotions. Her hand trails slowly down my chest, tracing lazy circles over my abdominal scar."
    "The sensation of her touch is both soothing and tantalizing, each movement sending ripples of warmth through my body. She lingers for a moment, her fingers exploring the contours of my skin with a delicate curiosity."
    show mox happy with d
    "Her eyes lock with mine, and the space between us seems to disappear. Her gaze briefly flickers to my lips."
    camera:
        linear 1.5 zpos -500 ypos -200
    pause 1
    hide mox with dissolve
    "I lean in, and our lips touch softly at first, but as the kiss lingers, passion grows. Soon, I feel her tongue slipping into my mouth. Our tongues dance and duel as our hands begin to roam across each other’s bodies."
    "My hands grip her lithe frame firmly yet lovingly, my fingers digging into her soft fur. She moans into the kiss, her hands gripping my shoulders tightly."
    play sound2 equip
    camera:
        linear 1.5 xpos -100 ypos 0
    "With a gentle push, we end up on the couch, her body beneath mine in a passionate embrace."
    show moxie1a e1
    camera:
        linear 10 xpos 0 ypos 0 zpos -16
        block:
            linear 1.8 ypos 6
            linear 0.4 ypos 6
            linear 0.8 ypos -2
            linear 0.2 ypos -2
            repeat
    $ textbox = 2
    play moans1 moansmisc2
    stop ambience1 fadeout 30
    with d
    "Another thunderbolt, but that could barely match the electricity between us; our bodies were practically crackling with desire and lust. Despite the two passionate bouts I’ve already had today, my cock was fully erect once again, and now precariously pressed between her legs, I could feel the inside of her thigh against my shaft."
    mox "Aahh~ I wonder what it’d feel like to have that beast inside me."
    mox "But I admit, I’ve been nervous every time I’ve seen it so far."
    mox "And since it’s my first time… I wanted to wait for the right moment. [pen] is a lot of fun, but… I wanted you alone for this."
    mc "Is now the moment?"
    show moxie1a e2 with d
    mox "I’m certainly wet enough for it. Certainly horny enough for it…"
    mox "We’re going to have {i}a lot{/i} of sex in here, aren’t we?"
    mc "Yep, on every piece of furniture, in every position you can imagine."
    mox "Mmm… Well… In that case..."
    "[mox]’s breath hitched in anticipation, her heart pounding against her chest."
    "She spread her legs."
    "No, more than that. She held her legs high, securing them in place with her hands. An unbridled invitation."  
    "My cock was no longer pressed between her thighs, but now hovering over her lips, the tip occasionally brushing against them."
    "With each passing heartbeat, my tip delved in just a little deeper."
    mc "Tell me what you want me to do. Tell me that you’re ready for me, [mox]."
    mox "I…"
    "She had never felt such desire before, not even close. It wasn’t just lust that filled her body; there was something deeper, more profound, that made her tremble with anticipation."
    mox "I want you inside me."
    mox "Please… make love to me." 
    play music sextheme
    play sound2 cum
    show moxie1a e3 v1
    play moans1 moansmisc4
    with c
    "Guiding myself in with my hand, I slowly slid my cock into [mox]’s tight, wet entrance, feeling her body shiver with pleasure as she accepted each inch."
    "A shuddering moan tore from her throat at the mind-blowing sensation of being filled up for the first time while in her desperate heat. Her walls tightened around my shaft, squeezing me mercilessly yet oh-so-deliciously."
    camera:
        zpos -20
        linear 0.5 ypos 8
        linear 0.1
        linear 0.2 ypos -8
        linear 0.2
        repeat
    with vpunch
    play ambience2 sex
    "Her pussy was already dripping wet, her flank trembling underneath me as I began to thrust into her."
    mc "Nngghh, damn, you’re tight!"
    mox "Ooohhh, that’s because your cock is so big! Mmh… and it feels so good!"
    with vpunch
    "Her pussy squeezed and spasmed as precum oozed deep inside. I grabbed hold of her hips tightly, using them as leverage to drive myself deeper into her body." 
    mox "Yes! Ohhh, yes! This is everything I wanted it to be and more!"
    "[mox] moaned out loudly, not caring if the neighbours might hear. She continued to beg for more, urging me on with each breathy moan that escaped her lips. She was completely lost to her primal desires, her normal demeanour replaced by wanton lust." 
    mc "I can’t believe how good you feel! So wet and hot!"
    with vpunch
    "I increased the pace of my thrusts, each one harder than the last. The sounds of our bodies colliding filled the apartment, - the slapping of flesh against flesh, the wet squelching sound of my cock sliding against her wet, mare pussy, accompanied by her moans and gasps of pleasure."
    "I leaned forward, burying my face into her mane as I continued to ravage her tight hole. I nibbled on her earlobe, biting down gently as I felt myself getting closer to climax."
    show moxie1a e4 with d
    mox "Oh gods! I can feel you getting even larger! Uoohhhh, you’re going to make me cum!"
    "[mox] whimpered out between moans, her body growing tense in anticipation of her climax. She arched her ass upwards, pushing herself harder against my cock, begging for more of that incredible sensation."
    "I could feel myself teetering on the edge as well. The tightness of her pussy around me was almost too much to bear."
    mox "Aahhh, I-I’m almost…!"
    "I reached down between us, finding her sensitive clit with one of my hands. I began to rub it rhythmically as I continued to thrust into her tight hole. This was the final straw for both of us—we both exploded together."
    play sound2 cum
    show moxie1a e3 cum v2
    with c
    play sound2 cum
    show internalcreampie 
    with c
    mox "I’m cumming!" 
    play sound2 cum
    with c
    play sound2 cum
    with c
    "I let out a roar of pleasure as I came inside of her, filling her womb with hot cum. My cock throbbed inside of her tight hole, pulsing with each spurt of seed that spilled into her depths."
    play sound2 cum
    with c
    play sound2 cum
    with c
    "Meanwhile, [mox] screamed out in ecstasy as wave after wave of orgasmic bliss washed over her body. Her pussy clenched tightly around me, milking every last drop of cum from me before finally loosening its vice-like grip on my cock."
    hide moxie1avaginal
    show moxie1a e5 -v2 cum
    call camerabreath from _call_camerabreath_14
    play moans1 moansmisc2
    stop ambience2 fadeout 2
    hide internalcreampie
    with d
    "My cock was slick with their combined juices, throbbing gently from our intense lovemaking. I looked down at her well-fucked pussy oozing with cum, her legs trembling slightly. But she was also already in the process of flipping over and moving into the next position."
    mox "You aren’t out of steam already, are you? This night’s only just started~"
    scene moxie1b e1 cum0
    with d
    "I bite my lip and masturbate back to a full erection as I get back into position behind [mox]’s fat ass."
    mc "You read my mind. Let’s fuck that heat completely out of you, for a few days at least~"
    play sound2 cum
    show moxie1b e2 v1
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
    "I take a few seconds to spread and admire her well-fucked, deflowered pussy, before guiding the tip of my cock straight back inside."
    mox "Oh god, you feel so fucking good."
    "She moans deeply as I begin slowly thrusting, savouring the tightness of her pussy as I fill it up once again." 
    mc "You’re all mine now, aren’t you?"
    "Her body shivers slightly, her ass pushing back against me with more vigour and enthusiasm, her hips grinding back and forth."
    mox "Y-Yes~! All yours! Mmhhh... How could I not be when you feel this good inside me?"
    "Pleased with her response, my cock tightens and throbs. I pick up the pace, and my thrusts become harder and faster. Each time I slammed into her tight pussy, her walls squeezed me tighter and tighter."
    mox "Ah, ah! Haaahhh… It feels so good! I want to keep doing this forever…"
    "Her long, silky hair continued to swish and flicker against her back, giving me the perfect opportunity to grab it and pull it. [mox] responded passionately, her pussy tightening and back arching as she loved absolutely everything I did to her."
    "Gripping her hair firmly, I pulled her head back enough to expose her delicate neck to my hungry lips. I started to kiss and nibble at a sensitive spot, drawing out low moans of pleasure from her." 
    mc "Cum for me, cutie~"
    "I growled against her neck, thrusting myself balls-deep inside her once more."
    play moans1 moansmisc1
    mox "Ooohhh, fuck! I-I’m… cumming! S-So hard!"
    "[mox]’s entire body tensed up violently as she came hard around my cock. Her insides clenched so tightly around me that I thought I might cum too. But I held on, savouring this moment for just a little longer." 
    play sound2 cum
    show moxie1b cum v2
    with c
    play sound2 cum
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
    call camerareset1 from _call_camerareset1_2
    play sound2 cum
    show moxie1b e3 -v2
    hide internalcreampie
    play moans1 moansmisc2
    stop ambience2 fadeout 2
    with d
    "Breathing heavily, I pulled out slowly, watching as our combined fluids trickled down [mox]’s wet pussy lips and dripped onto the couch below us. "
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
    mox "Sorry…"
    mc "Hm? ‘Sorry’?"
    show mox bashful with d
    mox "For being selfish, I mean… You have so much to do and must have so much on your mind, yet here I am asking for sex."
    mc "Heh, you’re acting like I didn’t thoroughly enjoy it."
    mc "You’re right, though; it does sound like I’ll have my hands full in the coming days, maybe weeks."
    mc "However, down time and relaxation are always extremely important~ so thank you for helping me."
    play sound2 equip
    camera:
        linear 0.3 zpos -500 ypos -200
    show mox satisfied with d
    "I roll on top of [mox] and kiss her snout. She giggles and responds with another kiss."
    show mox happy with d
    mox "Heh, I don’t know why, but for some reason I could tell you were the one for me."
    mc "More than you know, [mox]."
    mc "And just to cover my bases, you don’t mind if I sleep with others?"
    show mox wink with d
    mox "Pfft, of course not. Having the manliest stud in the city live in my apartment makes me pussy weep~"
    show mox horny with d
    mox "Speaking of which… Are you ready to go again?"
    mox "Let’s tag out; this time I’ll be on top so you can recover for our fourth session."
    mc "Damn, we really will be fucking your heat into next week at this rate."
    stop ambience1 fadeout 10
    scene bg moxiebedroom2 
    call camerareset1 from _call_camerareset1_3
    with dissolve
    "[mox] and I continued to rut long into the evening, only taking a break to eat pizza and watch a movie before we just kept going."
    "We bounced from cuddling, to sex, to snuggling, to more fucking."
    "Thankfully, I already knew [mox] very well, so I guided her through a variety of positions and even suggested a few spells to try."
    hide screen vnui
    scene bg black with d
    "But…"
    "Try as I might…"
    show intromoxie 2 with d
    "My heart felt heavy as I remembered my [mox]. It all feels the same, but can I really pretend that this is the same?"
    hide intromoxie with d
    "These thoughts kept me restless as I cuddled with the new [mox] under the blankets. My mind stirred with memories of my two past lives and what my future may entail. But eventually, it all came to a stop as I slept."
    "…"
    play ambience1 staticlong volume 0.2 fadein 5
    show space1:
        alpha 0.3
        linear 10 alpha 0
        linear 11 alpha 0.3
        repeat
    show space2:
        alpha 0
        linear 12 alpha 0.3
        linear 13 alpha 0
        repeat
    show silhouette1
    $ textbox = 2
    "…Save… me…{w=1}{nw}"
    show static with fd
    play sound1 staticshort1
    hide static with fd
    "Help… You need to…{w=1}{nw}"
    "… Bring the virtues back…{w=1}{nw}"
    show static with fd
    play sound1 staticshort2
    hide static with fd
    "Save me… [mc]… Save the…{w=1}{nw}"
    "Mul—{w=1}{nw}"
    camera:
        zpos -15
    play ambience1 staticlong volume 0.4
    play sound staticsequence
    show black with dissolve
    show static with dissolve:
        alpha 0.3
    show eyes:
        alpha 0
        linear 3.5 alpha 0.5
    with sshake
    show static with sd
    stop ambience1 fadeout 1
    scene bg moxiebedroom 
    $ textbox = 1
    label introend:
        stop sound1
        $ renpy.block_rollback()
        $ _history_list = []
        show screen vnui
        $ intro2 = 1
        $ moxmsg2 = 1
        $ unread += 1
        $ unreadmox += 1
        call camerareset2 from _call_camerareset2_10 
        "I sit up in a panic, my eyes quickly scanning around the room to ensure nothing is watching me."
    "The first thing I notice is that [mox] is gone; she already mentioned she was working this afternoon."
    "Standing up, I try to remember that dream. I don’t remember its contents, but I remember how it made me feel. I need to find the virtues and have them meet as fast as I can."
    "It’s intimidating, but I can’t help but feel slightly excited to meet all my friends again. I hope everyone has succeeded in this world as [mox] and [pen] have."
    "The only question is, where shall I start today?"
    if replay == 1:
        $ replay = 0
        return
    jump worldmap

label introskip:
    if default == 0:
        "Let's quickly pick all the character designs and names!"
        hide cream with d
        $ gen1 = 1
        $ gen2 = 1
        call screen characterchoice
        $ moxb = gen2
        show mox happy
        with d
        menu:
            "What was her name?"
            "Default: Moxie":
                $ moxie = "Moxie"
            "Custom":
                $ moxie = renpy.input("What was her name?")
                if moxie == "":
                    $ moxie= "Moxie"
                $ moxie = moxie.strip()
        hide mox with d
        $ gen1 = 2
        $ gen2 = 1
        call screen characterchoice
        $ penb = gen2
        show pen happy
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
        hide pen with d
        $ gen1 = 3
        $ gen2 = 1
        call screen characterchoice
        $ honb = gen2
        show hon happy
        menu:
            "What was her name?"
            "Default: Honeycrisp":
                $ honeycrisp = "Honeycrisp"
            "Custom":
                $ honeycrisp = renpy.input("What was her name?")
                if honeycrisp == "":
                    $ honeycrisp= "Honeycrisp"
                $ honeycrisp = honeycrisp.strip()
        hide hon with d
        $ gen1 = 4
        $ gen2 = 1
        call screen characterchoice
        $ rubb = gen2
        show rub happy
        menu:
            "What was her name?"
            "Default: Ruby":
                $ ruby = "Ruby"
            "Custom":
                $ ruby = renpy.input("What was her name?")
                if ruby == "":
                    $ ruby= "Ruby"
                $ ruby = ruby.strip()
        hide rub with d
        $ gen1 = 7
        $ gen2 = 1
        call screen characterchoice
        $ lilb = gen2
        show lil happy
        menu:
            "What was her name?"
            "Default: Lily":
                $ lily = "Lily"
            "(Custom Name)":
                $ lily = renpy.input("What was her name?")
                if lily == "":
                    $ lily= "Lily"
                $ lily = lily.strip()
    scene bg black with d
    jump introend