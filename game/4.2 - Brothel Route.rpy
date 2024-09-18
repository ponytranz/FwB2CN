label brothel:
    hide screen worldmap
    if brothelroute1 == 0:
        jump brothel1
    play music clubtheme fadein 1
    scene bg brothel1
    with d
    menu brothelmenu:
        "Work (Ask [rub] for an Interview)" if brothelroute2 == 0:
            jump brothelmenu
        "Work" if brothelroute2 == 1:
            jump brothelwork
        "Choose a Hostess (In Development)":
            play sound2 error
        "Visit [rub]":
            scene bg brothel5
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
                    show rub wink
                    rub "Oh my, you're going to take me right here?"
                    menu rubsexmenu:
                        "Energy: [energy]"
                        "No Energy Left" if energy <= 0:
                            "I feel exhausted!"
                            jump rubmenu
                        "Thighjob (In Development - Planned for 0.3)" if energy > 0:
                            jump rubsexmenu
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
        "Visit [mel]":
            scene bg brothel2
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
                            play music clubtheme
                            scene bg brothel2
                            show mel happy
                            with d
                        "Booth Blowjob" if energy > 0:
                            call melblowjob from _call_melblowjob
                            play music clubtheme
                            scene bg brothel2
                            show mel happy
                            with d
                        "Cowgirl (In Development - Planned for Later)" if energy > 0 and brothelroute2 == 1:
                            "The reason this scene is in development, is because [mel] is currently a virgin, and this scene will have additional sex variants once she's lost her virginity."
                            jump melsexmenu
                        "Reverse Cowgirl (In Development - Planned for Later)" if energy > 0 and brothelroute2 == 1:
                            "The reason this scene is in development, is because [mel] is currently a virgin, and this scene will have additional sex variants once she's lost her virginity."
                            jump melsexmenu
                        "Back":
                            show mel happy with d
                            mel "Tch, I was joking."
                    jump melmenu
                "Back":
                    scene bg brothel1 with d
                    jump brothelmenu
                "Leave":
                    jump worldmap
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
        group thighjob:
            attribute t1:
                "ruby1athighjob 1"
        group thighjob:
            attribute t2:
                "ruby1athighjob 2"
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
            show chloe
            with d
            if chloenamed == 0:
                $ chloenamed = 1
                menu:
                    "I think I recognzie her. What was her name?"
                    "Default: Chloe":
                        $ chloe = "Chloe"
                    "Custom":
                        $ chloe = renpy.input("What was her name?")
                        if chloe == "":
                            $ chloe= "Chloe"
                        $ chloe = chloe.strip()
            rub "Over there is [chl], a musical genius. She's one of our most expensive and sought-after hostesses. She has a private, soundproof booth where she performs live music."
            rub "Even though she plays in a private booth, she's not interested in the sexual side of services. I once heard she turned down 5,000 monies for such a request."
            hide chloe
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
                    "I think I recognzie her. What was her name?"
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
                    "I think I recognzie her. What was her name?"
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
                    "I think I recognzie her. What was her name?"
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
        group clothes:
            attribute goth:
                "mel2aclothes [melb]"
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
        group cum:
            attribute cum:
                "mel2acum"
        group hj:
            attribute hj:
                "mel2ahj"
        group sex:
            attribute sex1:
                "mel2asex"
        group cum2:
            attribute hj2:
                "mel2ahjcum"
            attribute sex2:
                "mel2asexcum"
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
            mel "Mmphhhhh... Fuck... Are you getting even harder now you know the truth~?"
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
