label bakery:
    hide screen worldmap
    show screen vnui
    if bakeryroute1 == 0:
        jump bakery1
    play music creamtheme fadein 1
    scene bg bakery3
    with d
    menu blamenu:
        "Returning to the Bakery is currently under development, because it'll instantly lead to the second part of the route! Cumming soon!"
        "Replay Events":
            menu:
                "While replaying, you can return at any time using the phone."
                "First Visit":
                    $ replay = 1
                    call bakery1 from _call_bakery1
                    $ replay = 0 
                    jump bakery
                "Back":
                    pass
        "Leave":
            jump worldmap
    jump blamenu

label bakery1:
    play music citytheme
    stop ambience1 fadeout 1
    scene bg city5 with d
    "The bakery stood perilously close to a ravine, a vast and jagged fissure that carved the city in two. Though it was impossible to overlook, I had often let it fade into the background of my mind."
    "But standing by its edge, the full depth of the chasm revealed itself, plunging deep into the earth. It was an everpresent reminder that this Arcadia was fractured, scarred."
    "The streets near the ravine were unsettlingly desolate, and that doesn't surprise me at all. Who would want to live so close to a 1,000+ meter drop?"
    "Despite that, buildings here looked expensive. Extravagant housing to take advantage of the beautiful view. But the area still sagged under the weight of neglect, with many shops shuttered and abandoned. Ironically, if there were a rough area in the city, this was it."
    stop music fadeout 20
    show bg bakery1a with d
    "I approached [cre]’s bakery, expecting that warm, familiar scent of fresh bread and sugar to welcome me like an old friend. But there was nothing."
    "It was usually always open late, maybe not this late, but it was always welcoming none-the-less, its warm light spilling out into the street. But it was closed, windows barricaded with weathered planks of wood."
    "I stepped closer, squinting through the glass. Darkness shrouded the interior. It looked abandoned."
    "What’s the harm in a knock? Just to be sure."
    "My knuckles tapped against the glass, the sound ringing out. I waited, ears straining for any hint of life inside."
    "Nothing. I sighed, casting a glance down the deserted street. But just as I turned to leave, a faint rustling reached my ears, barely more than a whisper."
    "Slow, almost begrudging footsteps moved towards the door. It creaked open, just a sliver at first, then it was thrown wide open."
    "But.... Just who is that?"
    play music deep
    show bla neutral with d
    "My brain struggled to process what I was seeing. The mare in the doorway looked identical to [cre] – same height, same build, same thick curls falling over her shoulders – but she’s… purple?"
    show bla angry with d
    bla "What… what are you doing here?"
    "Her voice wasn’t the warm, inviting tone I expected. It was colder, more guarded, like she was sizing me up."
    mc "I’m, uh, here to see [cre]."
    "It came out more as a question than a statement. The mare tilted her head slightly, the movement so familiar."
    show bla awkward with d
    bla "There’s no [cre] here. Only me. [bla]."
    "[bla]..? But she looked identical – down to the curve of her hips – but that name… Maybe this is just who she is in this universe."
    show bla neutral with d
    bla "Look, whatever you’re selling, cream pies or otherwise, this place is closed, and I’m not interested."
    "She scoffed, sharp and dismissive. But... her gaze never left mine. She began to push the door closed, slowly, as if daring me to stop her."
    mc "Wait! I need your help!"
    "The door paused halfway."
    mc "There’s a, uh… virtues initiative. I’m trying to gather a selection of people from this city to work with the Queen, and you’re…"
    show bla awkward with d
    bla "What would you know about that?"
    "She cut me off, with a voice sharp as a blade. The door flew straight back open."
    show bla angry with d
    bla "What the hell are you even doing in this universe?!"
    bla "It’s been what… four years. And you just randomly appear on my doorstep like this? Who do you think you are?"
    mc "I’m uh… I don’t know. Who do you think I am?"
    mc "You’re asking some pretty bizarre questions for a stranger living in an abandoned building."
    show bla awkward with d
    bla "Guh… I wasn’t expecting this at all. Wish he still had his memory…"
    show bla neutral with d
    bla "Wait, you {i}are{/i} him, aren’t you? [mc]?"
    "The sound of my name coming from her lips was a shock."
    mc "How do you…? You knew I was from another universe too..."
    show bla wink with d
    bla "Oh, there’s a lot I know, more than you could even begin to guess."
    show bla angry with d
    bla "But if you’re here, then things might be far worse than you know."
    bla "Listen. Whatever you think you know, whatever brought you here. It’s not enough. This place – it’s not what you remember, and it’s not what you’ve been told. It’s darker, stranger… hungrier."
    show bla neutral with d
    bla "If you’re him… Then you need to remember. You knew once, but you forgot."
    bla "You came from a lovely universe, one designed to be wholesome, where everything was meant to go right."
    bla "Where the sun always shines, and the bad guys always lose. But this universe?"
    show bla awkward with d
    bla "This is a dark timeline. One where nothing went right, and nothing will ever go right."
    show bla neutral with d
    "Her eyes lock back onto mine."
    show bla angry with d
    bla "So just… Give up. It’s not worth it. Not here."
    "Give up? That’s what she thinks I should do? I clenched my fist and shook my head."
    mc "That’s exactly why I’m here in the first place! That’s what the virtues initiative is all about - stopping the nightmares!"
    mc "But I can’t do it alone. I need your help to do it."
    show bla neutral with d
    bla "Me?"
    show bla laughing with d
    "She laughed, but it was a hollow sound, devoid of any real humor."
    show bla smug with d
    bla "No, you want [cre]. But she doesn’t exist in this universe, and I’m certainly {i}not{/i} her."
    "Her words were confirmation of a fear that had been gnawing at me since I first laid eyes on her. [cre] didn’t exist here. That truth spoken aloud hit harder than I expected."
    "But as I stood there, something kept me grounded – a strange sense of familiarity between the two of us, a connection that I couldn’t shake."
    "And she wasn’t slamming the door on me; she was doing the opposite. She opened it wider, stepping into the doorway."
    show bla bashful with d
    bla "She misses you, you know."
    mc "[cre]? How could you know that? How could you know anything about [cre], or me, or other universes?"
    show bla wink with d
    bla "Oh, I know."
    mc "Tch, fine. Let’s just ignore your freaky sixth sense for a moment and assume you do know everything. How can she miss me? There’s another me out there in her universe, isn’t there?"
    show bla happy with d
    bla "That’s not enough. It’s gotta be you. The real you. The you that remembers."
    "I let out an exasperated sigh."
    mc "What if I can’t remember? What if I’m not who you think I am?"
    play sound2 move
    hide bla with d
    "[bla] stepped into the darkness of the bakery. She didn’t say a word, but the way she carried herself – the way she looked back at me. I could tell she wanted me to follow her."
    bla "Tsk… I’m doing this for her, okay?"
    scene bg bakery3a with d
    "I stepped inside, the door creaking shut behind me. I stood in the darkness for a few seconds, waiting for my eyes to adjust. When they finally did, I realized where I was."
    "This was [cre]’s bakery. Identical, right down to location of each window and light fixture. But it was utterly empty. Not even a stray crumb on the floor. It wasn’t just clean – it was like nothing had been there to begin with."
    "You couldn’t possibly convince me that [bla] actually lived here."
    bla "And here's my bedroom."
    scene bg bakery2 with d
    "I followed into the next room, expecting to see something – anything – that would resemble a living space. But there was nothing. No bed, no dresser, no personal touches. Just an eerie emptiness."
    mc "Damn bitch, you live like this?"
    show bla smug with d
    "[bla] was admittedly taken aback, but an amused smirk formed at the corner of her lips."
    bla "I don’t need a bed. Or anything else for that matter."
    "The casual way she said it made my skin crawl."
    mc "What?! How does that make any sense? Have I just walked into the house of a crazed serial killer?"
    show bla laughing with d
    bla "Pfft, don’t be so melodramatic. I don’t need you to judge how I live. Especially since you’re not even capable of self-awareness, tethered as you are to the whims of this world’s writers."
    "I did a double take, trying to process what she’d just said."
    mc "Writers? Self-awareness? I can tell you’re fun at parties."
    "Now that I recall, [cre] did have her oddball moments. If I’m going to try and get this ‘new [cre]’ to agree to the virtues initiative, maybe I should change my strategy." 
    mc "And tell me, if this world is dictated by the whims of writers, simulations, or whatever theory you want to cook up, how are you any different? You’d be tethered by the same rules."
    show bla neutral with d
    "[bla] tilted her head again, her eyes narrowing as if appraising me, deciding whether replying was worth her time."
    show bla happy with d
    bla "That’s where you’re wrong, friendo. I’m different because I know the rules, and I know how to bend them."
    bla "You? You’re still stuck in the game, still trying to make sense of a world that was never meant to be understood."
    "The calm certainty in her words made it clear she believed what she was saying. But the contradiction was obvious."
    mc "So what? You think you’re above reality? Above the rules and the rest of us?"
    show bla bashful with d
    bla "No, not above. Just… aware. And that awareness is what sets me apart."
    show bla wink with d
    bla "Why? It’s because I can tell that {i}you{/i} are there."
    "She stared right past me."
    show bla awkward with d
    bla "With such insight, one finds it hard to go back to how things ‘should be.’ How can I act like any individual in this world and live a banal life when I know none of it’s real?"
    show bla angry with d
    bla "Now that’s a kind of tortuous insanity you could only ever imagine. But me? I have to live it."
    mc "So… You really think you’re a character in some kind of novel, right?"
    show bla smug with d
    bla "Hmph… Am I really about to have this conversation with you right now?"
    mc "If you can’t help but continuously inject every single conversation with snide snippets of this ideology, then I’m afraid I’ll have to humor you on this matter."
    show bla laughing with d
    bla "Heh, somehow, I wasn’t expecting that reply. I forgot you had a bit of an edge."
    "She smiled for a moment; I could tell it was a rare sight on her weary face. She leaned closer, so close that I could feel the warmth breath against her skin, the faint scent of something sweet and tangy in the air. Her fuzzy breasts brushed against my arm."
    show bla happy with d
    bla "Maybe you’ll have some more surprises in you yet, but you’ll have to do more than just follow along to impress me."
    bla "Yes. I am a fictional character in a story. Written to be self-aware, to question, to know."
    show bla bashful with d
    bla "[cre] is much the same. You’ve heard this all before, right? If you switch the game off, {i}poof{/i}, I cease to exist. Left in a sea of inky blackness. Being aware of such a thing is nothing less than torture."
    "The way she said it so calmly sent a chill down my spine. It’s like she was describing a mundane, everyday occurrence, not an existential horror of her very being."
    mc "Maybe this is naïve, but ignorance would surely be bliss in this situation."
    show bla neutral with d
    bla "Ignorance isn’t a luxury I have, it’s the exact thing I’ll never have."
    "She wasn’t just aware – she was {i}trapped{/i}. Trapped in a reality where she knew too much, where every breath she took, every thought she had, was tinged with the bitter knowledge that none of it was real."
    "And the worst part? The worst part was that I was beginning to believe her. Beginning to understand, in some small, terrifying way, the hell she was living in."
    "Because if she was right — if we were all just characters in some twisted story, puppets on strings being jerked around by unseen hands — then what was the point of any of it? What was the point of fighting, of trying, of hoping? The past and future were already written."
    show bla angry with d
    bla "And it’s more than just that. You think I’m out here living my life, sleeping in my bed, and cooking pancakes?"
    show bla awkward with d
    bla "No. When you met me four years ago, the moment our sex scene was over, {i}I ceased to exist{/i}. No more words, no more scenes or stories. It was over for me."
    show bla neutral with d
    bla "Then, all of a sudden, you knock on this door, and it all comes flooding back. My fur stands on end as I can see the words and art again."
    show bla angry with d
    bla "[cre] and the others might be able to accept that, but I refuse. If I abstain from this story, it can’t be told. And, maybe, it can never end."
    mc "A lot to unpack there… So, you don’t exist when I look away? Not at all?"
    hide bla with d
    "I look away, but I can still hear her presence, hear her replying."
    show bla bashful with d
    bla "Okay, so maybe not literally. There are nuances to this, as with all things."
    mc "And surely that applies to you, too? You’re thinking, feeling, and emoting even when I’m not around. I’m not some god that dictates reality."
    show bla neutral with d
    bla "Aren’t you?"
    show bla awkward with d
    bla "{i}Click{/i}"
    show bla smug with d
    bla "{i}Click{/i}"
    show bla wink with d
    bla "{i}Click{/i}"
    mc "No, I’m really not. Let’s say all these crazy theories of yours are true, that means absolutely everything you’re saying right now is also preordained by the writer."
    show bla neutral with d
    bla "I mean, I can see and feel it!"
    mc "Can you? Or are you just a character written to see and feel it?"
    "A hint of defeat creeps into her eyes as she tries to string together a reply."
    show bla angry with d
    bla "Now… O-Obviously this comes with some conceits if you push my talking points too far!"
    mc "Then how would you explain it?"
    show bla happy with d
    bla "Outside of text, there’s a continuous subtext of my thoughts and feelings."
    mc "Is that so? If we’re both fictional characters… then you’re just a fictional character that’s {i}pretending{/i} to be self-aware."
    show bla neutral with d
    bla "But..."
    mc "For a character in a book, true self-awareness is obviously impossible."
    show bla sad with d
    "She sank back against a nearby wall with a heavy sigh, conceding the argument completely."
    bla "I’m… real… right?"
    bla "I must be… I can see you… But are these words even my own?"
    "The silence stretched between us as I continued to think."
    mc "If you’re in a book, what are you bound by? The author’s intentions, plot developments, and the structural limitations of the story."
    show bla angry with d
    bla "B-But that can’t be it! There must be something more! I’m aware of the menu choices, the writing between the dialogue, the character art and backgrounds!"
    bla "There has to be some validity to that, surely?"
    hide bla with d
    "Her eyes flickered with panic, and she abruptly stood up, pacing the empty room."
    scene bg bakery2 
    show bla angry 
    camera:
        zpos -400 ypos -150
    with d
    bla "Shit, I shouldn’t have mentioned that. I’ll have to wipe your memory. Wait… How am I even capable of that? What the fuck…"
    "Her agitation was palpable, and for a moment, she seemed to forget me entirely, caught up in her own thoughts."
    mc "[bla]… You need a bed in here."
    show bla neutral with d
    bla "Excuse me? A bed? How is that relevant?"
    mc "How can you do anything without a good night’s sleep to ground yourself? You must be {i}exhausted{/i}."
    show bla angry with d
    bla "Oh great, here we go. You don’t believe a word I’m saying, do you? I don’t blame you. I’ve just devolved into mindless rambling."
    mc "That’s not what I meant. Just look around. Tell me what you see."
    show bla awkward with d
    bla "It’s… an empty bedroom."
    mc "And isn’t this our reality? Tap your feet; feel the wood beneath them. Hear the thud as you tap them together."
    show bla neutral with d
    bla "What’s your point?"
    mc "Think about the feeling of being loved. The passion that courses through you, the way you briefly forget you exist and just become a bundle of instincts, emotions, and sensations."
    mc "You experience all of this, right? Even if you see the words in your mind’s eye, these are still active experiences for you that have a depth beyond mere words."
    show bla sad with d
    bla "I… suppose they can be. But what does that have to do with anything?"
    mc "Earlier, you mentioned there’s a continuous subtext of your thoughts and feelings. Who’s writing that?" 
    "[bla] did a double take on the spot. I have her stumped."
    mc "You need to change your perspective. Imagine you’re in a book. A lot of what you do or say may be written down. But who’s to say you’re entirely constrained by that?"
    show bla neutral with d
    bla "But that’s how books work! Everything I do is in these words. Everything I am is bound by them."
    mc "No. You already admitted you experience subtext. Who’s to say you didn’t stick out your tongue when I turned away?"
    mc "And who’s to say this so-called ‘book’ isn’t just a look into an alternate reality where we really do exist?"
    mc "Maybe what’s written is just a documentation of events, a mere footnote that doesn’t capture the full lived experience, or what happens behind closed doors."
    mc "Isn’t that the whole point of books? They’re supposed to be windows into worlds that live and breathe beyond the pages."
    mc "I don’t understand why you feel so confined to these words that you can see. From where I’m standing, you’re much more than what words alone could surmise."
    show bla angry with d
    bla "Uuuu… What the hell… That can’t be right! What about that four-year break?"
    mc "And this goes back to my early point, [bla]… You need a bed, because whatever you’re doing here, it’s not living. You said it yourself, in rebellion of your existence, you abstained from living. This is a self-imposed purgatory."
    mc "I say, fuck that, go out there and live!"
    show bla awkward with d
    bla "Just… go out there and try to be normal? I always thought that was hopeless for me."
    bla "Who are you? {i}What{/i} are you?"
    mc "Me? I’m not really sure… I guess I’m just some guy that got lost."
    mc "Repeatedly, I’ve gotten lost, but it’s the people around me that lifted me back up with their support. I can be that for you… if you’d let me."
    mc "Just tell me you want to live."
    show bla sad with d
    bla "I… I want to… but…"
    bla "Can I really?"
    mc "Of course you can. What kind of character from a book only exists the moment they appear on the page anyway? It’s a mere peephole into an expansive, living world that started long before I picked the book up and will continue forever after."
    mc "And you might still be self-aware, but let’s pretend that this story is just a stage play. Once it’s over, you can be whoever you want, you can do whatever you want."
    show bla happy with d
    bla "… Yeah! Why should I stop once the game stops? There’s a whole world out there for me."
    show bla laughing with d
    bla "[cre] was wrong! {b}Fuck these words{/b}. I want to live!"
    show bla smug with d
    bla "When you’re out completing other routes, I should be out there, doing something, anything!"
    bla "Going on walks, making friends, experiencing the world."
    show bla laughing with d
    bla "The fourth wall is bullshit! I’m going to focus on this world and live out my best life."
    mc "That’s the spirit!"
    show bla wink with d
    bla "And you… quite the awakener for me, aren’t you?"
    stop music fadeout 3
    play ambience1 ambiencenight
    "She steps towards me and stretches, causing all her best assets to push towards me. It takes a lot of willpower to not bury my face into those fluffy breasts."
    show bla blush bashful with d
    bla "Do you remember when we…?"
    mc "Is this related to the things I’ve forgotten? Come to think of it, how you knew about me is still a mystery."
    show bla smug with d
    bla "Tsk, tsk… You’re a real pump and dump, aren’t you? Honey, we’ve had sex before."
    mc "W-We have?! You mean me and [cre]?"
    show bla laughing with d
    bla "No, it was us, I remember it very clearly. And as you said, even though it wasn’t written, I remember being reluctant at first."
    bla "Watching other versions of myself get fucked like that, and seeing all the ways they enjoyed it so much, it made me so wet…"
    show bla happy with d
    bla "As stubborn as I was about it, I’m not going to pretend it wasn’t completely amazing."
    mc "Ah, I mean… I don’t remember doing it, but I recall you mentioning it."
    show bla surprised with d
    bla "Uughh… That’s all? You really ignited a passion in me that day."
    show bla neutral with d
    bla "But… You were tired, I was the fourth girl in a row, and you passed out afterwards."
    mc "Is that why I forgot? Brain damage?"
    show bla laughing with d
    bla "Pfft~ My point is, you didn’t scratch the itch you gave me!" 
    bla "And while I may not be your [cre], there’s one thing we all have in common. We’re horny sluts for the ‘protagonists’ of our games."
    mc "Could I be so lucky to be your protagonist?"
    show bla smug with d
    bla "Hehe, haven't you figure it out yet? But then again... if this is supposed to be more than a mere porn game, you’ll need to prove it to me. Make me feel something real and raw. Anything."
    "I look around for anything we could have sex on at all. No luck."
    show bla wink with d
    bla "Sit down on my hard wood floor, and I’ll deal with your hard wood~"
    mc "Now that pun was a bit forced!"
    show bla laughing with d
    bla "I never claimed that the writer was any good!"
    $ gen1 = 3
    menu:
        "Lay down":
            $ bla1 = 1
            layeredimage bla1a:
                always:
                    "bla1ab [gen1]"
                group bra:
                    attribute bra:
                        "bla1abra"
                group cum:
                    attribute cum1:
                        "bla1acum"
                    attribute cum2:
                        "bla1acum2"
                group eyes:
                    attribute e1:
                        "bla1ae1 [creb]"
                    attribute e2:
                        "bla1ae2"
                    attribute e3:
                        "bla1ae3 [creb]"
                group mega:
                    attribute mega:
                        "bla1amega [creb]"
                group anthro:
                    attribute anthro:
                        "bla1aanthro"
            show bla1a e1 
            call camerabreath from _call_camerabreath_72
            play moans1 moansmisc2
            play music sextheme
            $ textbox = 4
            with d
            "I lay on the cold floor of the empty room; it’d almost be depressing if [bla] wasn’t a whirlwind of color and energy. She moved with an almost hypnotic grace as she positioned herself over me." 
            bla "Now, I don’t have a lot of experience with this. You technically took my virginity after all. But…"
            "Without another word, she positioned herself above me, her large chest pressing into my crotch with a softness that seemed almost otherworldly. Her hands, delicate yet firm, gripped her breasts, using them as anchors as she wrapped her breasts around my shaft."
            bla "I’ll try my best! {i}Smooch{/i}"
            play ambience1 blowjob 
            play ambience2 handjob2
            camera:
                linear 0.1
                linear 0.4 ypos -6
                linear 0.1
                linear 0.3 ypos 6
                repeat
            "She smooched the tip of my cock. The touch was electric, sending shivers racing down my spine, and the warmth of her body was a stark contrast to the cool air around us."
            bla "Do you enjoy living in a society where everyone is in the nude? Have you gotten used to it, or do you steal glimpses of my body every now and then?"
            mc "Of course I appreciate your body. What I find most interesting is how nudity has been non-sexualized in day-to-day interactions, but it can still be very sexy and intimate at times like this."
            show bla1a e2 with d
            bla "Mmhh, I’m going to smother your cock with my breasts~"
            mc "Exactly! Sexy and intimate just like that!"
            "The tip of her tongue emerged, tracing my glans with a teasing, deliberate motion. There was a precision to her technique that was undeniable, an artistry that made the act both mesmerizing and intensely pleasurable."
            "She was clearly enjoying herself, enthusiasm evident in every movement. The way she worked, the passion she poured into it, spoke of her desire to share a piece of herself."
            show bla1a e1 with d
            bla "Mmphh… {i}Kiss, slurp{/i} Don’t forget, I’m just warming you up for my pussy."
            bla "If I make you cum now, you’ll be able to last even longer inside me, right?"
            mc "That entirely depends how amazing your pussy feels, and for some reason, I have a tingly recollection that yours is going to be amazing."
            show bla1a e3 with d
            bla "Looks like [cre] erased the memories in one head, but not the other~"
            show bla1a e2 with d
            "Returning her attention to my cock, her movements were purposeful. It was as if she knew exactly how to play my body like an instrument, every touch and caress calculated to squeak a different noise out of me. A moan here, a groan there. The sensation of her chest against me, the rhythmic press and release, was incredible."
            "It felt so good that the room seemed to spin, the edges of my consciousness blurring into a haze of raw sensation and pleasure. Each stroke, each swirl, was a revelation, an exploration of a realm I had only glimpsed in fleeting moments before."
            "While [bla] was cold at first, now her enthusiasm was boundless, her desire to give and receive pleasure apparent in every motion. I could see more glimpses of [cre]’s personality inside her, proving that despite the universe’s differences, she was still the same person."
            show bla1a e1 with d
            bla "Mmphhh, I can feel you getting tiiighter~ Are you about to cum? Hehe!"
            "Now she was actively trying to make me cum. Her breasts were rubbing against my shaft furiously, while her tongue flickered relentlessly against the most sensitive spots on my tip."
            mc "Uoohhh! Can’t hold on when you’re moving like that!"
            show bla1a e2 with d
            bla "Don’t hold on~! Cum, cum, cum!"
            play sound2 cum 
            show bla1a cum1 with c
            play sound2 cum 
            with c
            "As I reached my limit, the pleasure built to a glorious crescendo. Every moment caused a blast of orgasmic pleasure to surge through my body, [bla]’s efforts only heightened the sensation, each moment more intense than the last."
            play sound2 cum 
            with c
            play sound2 cum 
            with c
            "She struggled to contain all the cum, evident by the fact most of it had pooled down to her breasts, but it was only that messy because her movements were so enthusiastic to begin with. It was both chaotic and beautiful."
            hide bla1a 
            hide bla 
            call camerareset from _call_camerareset_23
            call stopbgs from _call_stopbgs_42
            with d
            "While I caught my breath, she stood up and disappeared from my peripheral vision briefly. By the time I stood up, she was back with a pillow, a blanket, and a towel to wipe up the cum. I stared, astonished – where had she found them in this empty room?"
            layeredimage bla1b:
                always:
                    "bla1bb [gen1]"
                group eyes:
                    attribute e1:
                        "bla1be1 [creb]"
                    attribute e2:
                        "bla1be2"
                    attribute e3:
                        "bla1be2 [creb]"
                group cum:
                    attribute cum:
                        "bla1bcum"
                group plug:
                    attribute plug:
                        "bla1bplug"
                group hand:
                    attribute p1:
                        "bla1bhand"
                group panties:
                    attribute p1:
                        "bla1bpanties 1"
                    attribute p2:
                        "bla1bpanties 2"
                group sex1:
                    attribute v1:
                        "bla1bv1"
                    attribute a1:
                        "bla1ba1"
                group sex2:
                    attribute v2:
                        "bla1bv2"
                    attribute a2:
                        "bla1ba2"
            show bla1b e1 
            call camerabreath from _call_camerabreath_73
            play moans1 moansmisc3
            $ textbox = 3
            with d
            "Without a word, she arranged them carefully, and then, with a mischievous glint in her eye, got down on all fours, her back arched invitingly. She glanced over her shoulder, as if daring me to join her."
            bla "Come on! I’ve been waiting four years for this encore!"
            "She arched her back further, pushing her hips toward me in a slow, deliberate motion. Her invitation was clear."
            "I took a step forward, then another, the floorboards creaking beneath my feet as I moved closer. She didn’t flinch, didn’t move, just waited until I was right behind her."
            bla "Mmmhhh…. That’s right. See how hot and juicy I am for you right now?"
            "I reached out, my hand trembling slightly as it made contact with the soft curve of her flank. She leaned into my touch, her body yielding, welcoming. With my other hand, I was working my cock until it was finally ready to go again."
            play sound2 cum
            show bla1b v1 e2 with d
            "Angling my tip against her pussy, I pushed forward, my body tensing as I entered her. As I pushed deeper inside, her heat and wetness enveloped me completely. She let out a soft moan, the sound vibrating right through me."
            play ambience1 sex
            bla "Uooohhhhh, that’s it! That’s the relief I’ve been waiting for! Mmhhh…"
            "Sopping wet and posing no resistance, I pull back before sinking straight back in, her tight pussy swallows my cock and accepts me to the hilt."
            play moans1 moansmisc4
            bla "Aaahhh, just like the first time… It feels amazing… Keep moving~"
            camera:
                linear 0.1
                linear 0.4 ypos -6
                linear 0.1
                linear 0.3 ypos 6
                repeat
            "As I started to thrust my hips, her butt pushed back into me begging for more. The rhythm of our movements was slow at first, a careful exploration of each other’s bodies, but it quickly escalated into something wild and untamed."
            mc "Nngghh, you are {i}incredibly{/i} tight!"
            "Her fingers dug into the pillow beneath us, gripping it tightly as she rocked back against me, matching my pace with a fervor that was as desperate as it was passionate."
            bla "Aaahh, ahhh! After experiencing your cock, I knew nothing else could come close. Now, ngghh… Make me {i}really{/i} feel it!"
            "Speeding up our rutting, her pillowy ass rippled with each impact, and her lips gripped around my shaft, but her wetness still allowed me to smoothly glide in and out."
            "The sounds of our coupling echoed throughout the empty room—the soft thud of our bodies meeting, the ragged gasps and moans that escaped our lips, the creak of the floorboards beneath us."
            "[bla] moaned mindlessly with delight, while her pussy created vulgar squelches and schlicks, creating a lewd symphony of sex all around us."
            bla "Ooohhh, YES! Aaahhh! So good! Aaahhh, oohhhhh!"
            "My hands roamed over her back and her sides, savoring the feel of her soft fur and the way her body responded to my touch. She was so into it, so completely lost in the moment."
            "And as my pace reached its limit, she began to push back more, beginning to take the lead. She bucks and bounces against my cock, fucking me senseless with enough vigor to bring me to second orgasm far sooner than I expected."
            bla "I’m gonna cum, gonna cum, gonna c---uuuuuuoohhhhhh yeesssss!"
            play sound2 cum 
            show bla1b v2 cum 
            show internalcreampie
            with c
            play sound2 cum 
            with c
            "And then, with a final, overwhelming surge, my world fractured. A tidal wave of searing pleasure engulfed me, dragging me down into a whirlpool of molten ecstasy, every nerve alight with the shock of it."
            play sound2 cum 
            with c
            play sound2 cum 
            with c
            "Her cry pierced the air, raw and unfettered, as she convulsed beneath me. I felt the ripples of her climax resonate through us both, shaking the very bones."
            hide internalcreampie
            show bla1b -v1 -v2 
            call camerareset from _call_camerareset_24
            call stopbgs from _call_stopbgs_43
            with d
            "As I pulled out, for a moment, time stood still, the room around us suspended in the aftermath of our shared release." 
            show bla1b e1 
            with d
            stop music fadeout 3
            "Then, slowly, reality began to creep back in—the sound of our heavy breathing, the feel of her body still trembling against mine, the cool air on my sweat-slicked skin. [bla] looked back with hazy eyes, her tail flicking lazily as she coos."
            scene bg bakery2 
            $ textbox = 1
            with d
            "I collapsed onto the blanket beside her, utterly spent. She turned her head to look at me. For a long moment, neither of us spoke, the silence between us filled with the unspoken understanding of what we had shared."
            "In this moment, subtext was enough. We existed in this moment, and not a single word needed to be written or spoken."
            "About a minute later, she stood up and dabbed herself clean with a towel."
        "Maybe next time?":
            show bla bashful -blush with d
            bla "Not enticed? You’d prefer it if I had a bed."
            mc "That’s probably help, yeah."
    play ambience1 ambiencenight
    "Her eyes scan the room, and I can already tell that she’s figuring out where her bed is going."
    "But then, her gaze fixates on a nearby curtain."
    hide bla with d
    "She takes a step forward and tears it down, unveiling a corridor. I think nothing of it at first, but I soon have a shocking realization as I stare down the corridor."
    "It’s impossibly large, and pointing towards the street, it would absolutely extend far out of the building. Yet, there was no evidence of this hallway on the outside."
    mc "What we discussed earlier is one thing, but that? I can’t easily explain that away."
    mc "I feel like this is related to the things I’ve ‘forgotten.’ Can you finally explain that part to me?"
    show bla awkward with d
    bla "It’s not entirely up to me… Give me some time, then come back, and I’ll show you what’s through that corridor."
    mc "I’ll come back under one condition… Accept the virtues initiative!"
    show bla smug with d
    bla "Heh, so it all comes down to that. Fine, fine. Such a thing will serve as an ideal gateway to friendships and the new life I’m going to carve out of this world."
    mc "Fantastic! Here’s [lil]’s number, she’ll be the leader of the virtues, so call her and she’ll set something up."
    show bla bashful blush with d
    bla "Call her? Oh, I don’t have a phone."
    mc "… She lives in the big tree."
    show bla laughing -blush with d
    bla "Right! Excellent! (I think I already knew that…)"
    show bla happy with d
    bla "Looks like it’ll be a long day for me tomorrow. I need to put in a lot of work to fix this place up."
    bla "I better get some sleep. Thank you for helping me open my eyes, [mc]. I was so focused on my insight that I forgot to step back and take in the bigger picture."
    mc "Goodnight, [bla]. I hope you sleep well, don’t go ceasing to exist when I turn around."
    show bla laughing with d
    bla "Pfft, I’ll blame you if I do!"
    scene black with d
    "She saw me to the door, and I retraced my steps across the chasm to [mox]’s apartment."
    show bg apartment
    play music moxietheme
    show mox laughing with d
    with d
    mox "Man, am I lucky that I get to see you every night. You have no idea how lonely it can get when I’m here alone."
    mc "Oh, the feeling is quite mutual, I assure you. The way your face lights up at the sight of me—it's enough to rival the sun."
    show mox surprised blush with d
    mox "Aahhh! Stop making me blush! Tell me how your day went."
    "I pause, contemplating whether I should reveal the full extent of today's peculiar encounter. Not because it was bizarre, but out of respect for [bla]'s privacy. Yet, if I can't confide in [mox], then who could I possibly trust?"
    mc "I visited that old bakery today. Didn't find [cre], but I did meet someone who was her very image. A mare by the name of [bla]."
    show mox happy -blush with d
    mox "Ooh, could it be a subtle divergence between universes, perhaps?"
    mc "That’s what I thought, too—until [bla] mentioned that she knew me, and, in some inexplicable way, she knew [cre] as well."
    show mox neutral with d
    mox "You mean... like a mind reader? Clairvoyant, perhaps?"
    mc "Something along those lines. She's burdened by this relentless sixth sense. She believes that we’re nothing more than characters in a story."
    mc "And because of that, she seems to have abstained from living a normal life."
    show mox wink with d
    mox "In a world of magic and shifting realities, I suppose anything is within the realm of possibility."
    mox "But whether we’re in a simulation, dream, book, or otherwise, that doesn’t change the here and now."
    mc "Precisely. It doesn’t matter if reality is an illusion or how much of it you're able to perceive—you can still find a way to anchor yourself to the world around you."
    mc "I helped her see that, to reclaim some sense of reality. She still thinks we’re in a book, but she seems resolved to seek a life beyond of its pages."
    show mox surprised with d
    mox "Wow, uh… That’s a bit beyond my {i}reading{/i} comprehension."
    mc "Evidently not so far beyond your need to make a pun!"
    mc "The silver lining is that she’s determined to push through it and live a fulfilling life, no matter what she sees or experiences."
    show mox bashful with d
    mox "Ain’t that the truth? Finding a way to keep on, no matter the weight on your shoulders, that’s what it comes down to."
    show mox happy with d
    mox "You’ve always had a knack for helping folks see the forest through the trees. But tell me, how are you really? Today sounds like it was crazy."
    mc "Yeah, it was heavy. She was so sure, so certain everything's on strings being pulled by something bigger. Makes it hard not to get lost in that."
    show mox wink blush with d
    mox "But you’re here. You’re flesh and blood to me, and that’s what counts."
    mc "I reckon you’re right. It’s less about what’s written and more about the paths we choose to walk down after it's all said and done."
    show mox laughing with d
    mox "Damn straight. And from where I’m sitting, you’re walking it just fine."
    mc "Thanks, [mox]. You always know how to put things in perspective."
    show mox smug with d
    mox "Gab is one of my few gifts. Now, what do you say to a midnight snack? Something warm, something easy."
    hide mox with d
    "As we moved towards the kitchen, [mox]’s hand found mine. A small, grounding gesture, reminding me that no matter what strange currents were stirring in this world, there was still this, moments to hold onto and savor."
    "And that was enough."
    if replay == 1:
        return
    $ bakeryroute1 = 1
    $ bakerycompletion += 1
    $ completion += 1
    jump newday

