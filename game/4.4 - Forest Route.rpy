label forest:
    hide screen worldmap
    show screen vnui
    if forestroute1 == 0:
        if rikunamed == 0 or buttersnamed == 0 or creamnamed == 0 or aurnamed == 0 or selnamed == 0:
            call v3renames from _call_v3renames_1
        jump forest1
    elif forestroute2 == 0:
        jump forest2
    play music butterstheme1 fadein 1
    scene bg forest5
    show night:
        alpha 0 
        blend "multiply"
    show red:
        alpha 0 
        blend "multiply"
    show but happy
    with d
    $ succ = 0
    but "Good evening, sweetie. Would you like a drink?"
    menu butmenu:
        "Active Succubus Mode" if succ == 0:
            play sound2 darkness
            show but succ smug
            play music danger
            show night:
                alpha 0.5
            show red:
                alpha 0.5
            with p
            but "You called?"
            $ succ = 1
        "Deactivate Succubus Mode" if succ == 1:
            play sound2 darkness
            show but -succ happy
            play music butterstheme1
            show night:
                alpha 0
            show red:
                alpha 0
            with p
            but "Did you need me, sweetie?"
            $ succ = 0
        "Sex":
            menu butsexmenu:
                "Energy: [energy]/[maxenergy]\nThere is a normal and succubus version of each scene."
                "No Energy Left" if energy == 0:
                    jump butsexmenu
                "From Behind/Tail Job" if energy > 0:
                    call buttailjob from _call_buttailjob
                "Blowjob" if energy > 0:
                    call butblowjob from _call_butblowjob
                "Breastjob" if energy > 0:
                    call butpaizuri from _call_butpaizuri
                "Doggystyle" if energy > 0:
                    call butdoggystyle from _call_butdoggystyle
                "Back":
                    jump butmenu
            play music butterstheme1 fadein 1
            scene bg forest5
            show night:
                alpha 0 
                blend "multiply"
            show red:
                alpha 0 
                blend "multiply"
            show but happy
            with d
            $ succ = 0
            jump butmenu
        "Replay Events":
            menu:
                "While replaying, you can return at any time using the phone."
                "Forest Visit 1":
                    $ replay = 1
                    stop music fadeout 1
                    scene bg black with d
                    call forest1 from _call_forest1
                    $ replay = 0 
                    jump forest
                "Forest Visit 2":
                    $ replay = 1
                    stop music fadeout 1
                    scene bg black with d
                    call forest2 from _call_forest2
                    $ replay = 0 
                    jump forest
                "Back":
                    pass
        "Leave":
            jump worldmap
    jump butmenu

label forest1:
    "In the other universe, this was just a peaceful forest edging the suburbs—a benign sprawl of trees and greenery that barely caught the eye."
    play music danger
    scene bg forest1 with d
    "But here, this is the 'Nevermore Forest,' a melting pot of myths and tales. The conclusion of most of these stories is simple: those who enter the Nevermore Forest never come back."
    "At first, I was confident. Tales like this were always spun to scare children away from wandering too far. But the real kicker, the thing that made me second-guess myself, was the guard stationed at the gate between the city and the forest."
    $ misc = "Guard"
    misc "You can go in, but if you don’t come back, no one will come after you. We won’t even list you as missing; you’ll be marked as dead."
    mc "I… see… {i}Gulp{/i}"
    play sound2 move
    show black:
        blend "multiply"
        alpha 0
        linear 10 alpha 0.4        
    "The guard must be exaggerating, right? I switched on my flashlight and forged ahead down a path I’d walked a thousand times before."
    "This was no cheerful stroll through friendly woods, with bunnies hopping and deer prancing."
    "It was dark—no, not just dark, but a suffocating, almost sentient darkness. The trees pressed in on me, and each step was a careful negotiation with the beam of my flashlight."
    "[but]’s house was only about ten minutes into the forest from the entrance, but in these conditions, it felt endless. And what if I took a wrong turn? In this darkness, every shadow twisted and morphed into something unfamiliar."
    "A few minutes in, I made the decision to turn back. It was too dark, too dangerous. I’d need to come back in the daylight if I was ever going to make sense of this place."
    stop music
    play sound2 equip
    call camerabreath from _call_camerabreath_52
    "I hear the crunch of distant leaves, sending a shiver down my spine. An uncanny dread settles over me."
    "It’s an instinctual, indescribable feeling. I can tell that I’m being watched. I don’t know where, and I don’t know what, but I know."
    "No, it’s worse than that. Being watched by a stranger across the street is nothing compared to this. This is different—more primal, more visceral."
    "From the moment I stepped into this forest, the balance of power shifted. I was no longer at the top of the food chain. I’ve become prey. I’m being hunted."
    play sound2 move2
    camera:
        linear 0.1 zpos -100
    "Abruptly, something soars through the darkened trees—could be the wind, a bird, or something far more sinister."
    play sound2 equip
    call camerabreath from _call_camerabreath_53
    "Something's behind me. Leaving is no longer an option. My only choice now is to push forward, hoping to reach the clearing where the cottage waits."
    play sound2 move
    camera:
        linear 0.1 zpos -100
    pause 0.4
    play sound2 move
    camera:
        linear 0.1 zpos -200
    "But with each step, something closes in. The rustling intensifies, encroaching from all sides."
    play sound2 impact2
    scene black with d
    "Despite bracing myself for an attack, I’m still caught off guard when something drops from above, pinning me down with a force that drives the breath from my lungs."
    layeredimage but1a:
        always:
            "but1a 1"
        group 2:
            attribute 2:
                "but1a 2"
        group mark:
            attribute 3:
                "but1acursemark"
    play music butterstheme1 fadein 10
    show but1a
    $ textbox = 2
    call camerabreath from _call_camerabreath_54
    with d
    but "Lost, little boy?"
    "In any other context, the situation would be utterly terrifying. But right now, a flutter of relief washes over me."
    mc "Oh, thank [aur]. I thought you were a monster."
    but "Hehe, look closer."
    show but1a 2 
    $ textbox = 4
    with sd
    "My shaken eyes adjust to clearly see a [but] that’s purely succubus. Seemingly further gone than her other self, with features far more prominent and imposing."
    "It’s like she’s evolved to a more dangerous, higher form. Her wings were dark as night, with a span thrice her body."
    "Her tail snaked into view, pure black and lacking the warmth of its heart-shaped tip."
    "Curiously, she has no horns. I was struck by the realization that [but] was not the same kind of demon I had expected."
    but "It’s dangerous for you to wander these woods. If you run away now, I won’t start chasing you for at least ten seconds~"
    mc "I’m not going anywhere. I came here to find you."
    but "Oh dear, is my reputation preceding me? To think, I’ve gone to such lengths to cover my tracks. It looks like I’ll have to deal with you myself!"
    play sound2 darkness
    show but1a 3 with d
    "Her eyes flared with a sharp, unsettling red as she locked her gaze onto mine. For a few disorienting moments, I felt her attempt to ensnare me in a hypnotic grip."
    mc "[but], wait! I’m here to help you!"
    play sound2 move2
    scene bg forest1
    show but succ angry
    call camerareset from _call_camerareset_15
    $ textbox = 1 
    with d
    "Startled, [but] recoiled back, her face shifting to one of concern."
    but "You… really shouldn’t know my name. Nobody knows my name."
    mc "I think I know how to cure your affliction, your curse."
    show but laughing with d
    but "Ahaha, what makes you think I want to be cured? I’m a demon that feasts on the energy of men like you." 
    mc "I know you’re not a monster. You’re a succubus that could drain me dry in an instant, but you're clearly trying to get me to leave for my safety."
    show but neutral with d
    "[but]’s expression softened slightly, her ears twitching with a hint of curiosity."
    mc "And I understand that you’re wary of getting close to men because of the risks, the danger, and the compulsions you struggle with."
    show but awkward with d
    but "You’re right. It’s unbearable. But a cure? That would be like clipping the wings of a pegasus or sawing off a unicorn’s horn."
    mc "Let me rephrase: I know of a potion that can remove your ability to drain energy during sex."
    show but wink with d
    but "As tempting as that sounds, why should I trust you? Why should you trust me? I don’t know how long I’ll be able to control myself around such an... attractive... male specimen."
    mc "I’ll tell you the ingredients, and, uh…"
    "Shiiit, what were the ingredients again? I remember where we got them from, but the names are slipping through my mind."
    mc "There was some kind of gel from a slime girl… A leaf cutting from an aphrodisiacal alraune…"
    show but smug with d
    but "Sounds like you're a third-rate alchemist with fourth-rate ingredients. What you're describing would make a {i}permanent{/i} aphrodisiac. Can you imagine if you gave something like that to a {i}succubus{/i}?"
    mc "Ordinarily, yes, if not for the final ingredient. One you could never get yourself — the coveted Dewblossom."
    show but bashful with d
    show but neutral with d
    show but awkward with d
    "[but] slipped into a deep trance, her eyes darting back and forth as if chasing invisible threads of thought."
    show but neutral with d
    show but awkward with d
    show but bashful with d
    but "Classic Dewblossom reversal… with folium polypus… an anti-aphrodisiac… Could that counter the curse?"
    show but awkward with d
    show but bashful with d
    show but neutral with d
    but "But with a gelatinous base… a transformation potion. In theory, it would be a potion that dramatically quells all forms of arousal."
    but "Could such a thing really neutralize my draining abilities? Ah—of course! The Dewblossom’s anti-evil warding effects!"
    show but laughing with d
    but "This isn’t just an anti-aphrodisiac; this is an anti-sexual magic potion! I’ll be able to do whatever the fuck I want!"
    show but happy with d
    but "You… genius! What’s your name?"
    mc "You can call me [mc]. I’m not a genius. All I know are the ingredients. You’re the one who makes the magic happen."
    show but wink with d
    but "Thanks for the tip, [mc]. Now, get out of here before I pin you down again. Between you and me, my pussy is already... Well, I’m not sure how much longer I can keep up this ‘good girl’ act."
    stop music fadeout 3
    play sound2 move2
    hide but with d
    "With that, [but] turned to leave, her wings flaring out in a dramatic sweep. I just stood still and waited expectantly."
    show but neutral succ with d
    but "… Right, I can’t touch the Dewblossom, can I?"
    play sound2 move1
    camera:
        linear 1 zpos -550 ypos -200
    "She awkwardly skips back."
    show but bashful with d
    but "C-Can you come with me and help? I promise I’ll be a good girl!"
    show but horny blush with d
    but "And if this potion works, I’m going to fuck your balls dry once I’ve had it~ Deal?"
    mc "Well, that doesn’t quite sound like the behavior of a ‘good girl,’ but I’ll gladly accept."
    scene black with d
    stop ambience1 fadeout 3
    play music danger 
    call camerareset from _call_camerareset_16
    scene bg forest2 with d
    "[but] led me into the familiar labyrinth of caves. I must have explored this particular network at least a dozen times while searching for ingredients. Yet, it was rare for me to be here with [but] in her succubus form."
    mc "[but], I’m curious about your other self."
    show but neutral succ with d
    but "What are you talking about, newbie?"
    mc "Your other half, you know, before you became a…"
    show but awkward with d
    but "Don’t finish that sentence. There is no ‘other.’ This is who I’ve always been."
    show but wink with d
    but "You’re the last person who should be asking questions right now anyway. Tell me how you knew about me, and why you bothered to come here to help."
    mc "I’m searching for six special mares to become the Virtues of Concord. They’ll be allies to the Queen, with the power to potentially stop the looming threat of the nightmares."
    show but neutral with d
    but "Oh, is that all? Why on earth would you want someone like me on a team like that?"
    mc "Powerful, intelligent, resourceful… You’d make a great Virtue."
    show but awkward with d
    but "Looking like this? I’d never be accepted for the position. I’m a monster."
    hide but
    show pink:
        blend "add"
        alpha 0.1
        linear 5 alpha 0.2
    with d
    "We moved a few more steps deeper into the cave, the air thickening with an unforgettable sweet, flowery scent."
    show but neutral succ with d
    but "Careful. This is alraune territory, and they can release powerful aphrodisiacs if disturbed."
    show but wink with d 
    but "Cover your mouth - oh, you already are. Well, I'll be in and out in a zap." 
    play sound2 move2
    hide but with d
    "She dashed into the pink-tinted darkness. The only thing visible was the eerie glow of her red eyes as she moved with relentless precision."
    play sound2 pollen
    scene bg forest2
    show but succ angry blush
    show pink:
        blend "add"
        alpha 0.2
    with d
    "Despite her caution, the alraune sensed their presence and erupted in a cloud of fragrant pollen. [but] emerged victorious, but stumbled back, coughing, and waving her arms to disperse the pollen."
    play sound2 move2
    hide but 
    with d
    stop music fadeout 3
    "I rushed to her side, but she pushed past me into a part of the cave with better ventilation. Her breathing was ragged, her cheeks flushed as she fought to regain control."
    mc "[but], are you okay?"
    scene bg forest2 
    show but succ neutral blush
    with dissolve
    but "I… I’m fine! I just… need a moment…"
    show but horny with d
    "But it’s too late. Her eyes glaze over with a sudden, intense need."
    play music sextheme
    layeredimage but1b:
        always:
            "but1bb"
        group succ1:
            attribute wings:
                "but1bwings"
        group cum:
            attribute cum:
                "but1bcum"
        group stockings:
            attribute stockings:
                "but1bstockings"
        group plug:
            attribute plug:
                "but1bplug"
        group succ2:
            attribute t1:
                "but1btail 1"
        group pp1:
            attribute pp1:
                "but1bpp"
        group pp2:
            attribute pp2:
                "but1bppcum"
        group succ3:
            attribute t2:
                "but1btail 2"
        group s1:
            attribute v1:
                "but1bv1"
            attribute a1:
                "but1ba1"
        group s2:
            attribute v2:
                "but1bv2"
            attribute a2:
                "but1ba2"
    show but1b wings t1 
    $ textbox = 2
    call camerabreath from _call_camerabreath_55
    play moans1 moansmisc2
    with d
    "She turns her back to me, leaning over a rock for support. Her succubus tail, usually swaying gently, now moves with a life of its own, curling towards me seductively." 
    but "Please, I can’t let this control me. I need you to cum on me, it’s the only way I can calm down and keep going. Let me use my tail to help you."
    menu:
        "{i}Step closer to the fluffy butt!{/i}":
            label but1:
                $ but1 = 1
            show but1b pp1 with d
            "Understanding the urgency, I take a step closer without hesitation."
            show but1b -t1 t2 with d
            "The sight of her gorgeous ass is the first thing to get my blood flowing, but as her tail wraps around me, the touch is electrifying."
            play sound2 darkness
            with p
            "I can immediately feel the charming touch of a succubus flow through me, activating and enhancing all my pleasure sensors."
            "But I must remember the danger of this forbidden pleasure too, sex with a succubus is the most pleasurable thing you’ll ever feel, and the absolute last thing you’ll ever feel. I must focus and calm down [but] as fast as I can."  
            play ambience1 handjob2
            camera:
                linear 0.2 zpos -12
                block:
                    linear 0.4 ypos 6
                    linear 0.3 ypos -2
                    repeat
            "Her tail has immediately started moving. The sensation is unlike anything I’ve felt before, a mix of gentle caresses and firm strokes. The tail moves with expert precision, coaxing pleasure with every motion."
            mc "Mmhh, that feels incredible."
            "I can’t help but let out a moan as I feel cock tingle with both natural and unnatural pleasures. The intensity of it all overwhelming my senses." 
            but "Just… let go. I need your energy to calm down." 
            "Her voice is strained but filled with a hint of relief."
            mc "I’m not holding back at all. As soon as I’m about to cum, I’ll let it flow right through."
            but "Right! I’m going to speed up!"
            "Her tail rocks back and forth at inhuman speeds and the pleasure keeps building until I can’t hold back any longer."
            mc "That’s it! I’m about to cum!"
            play sound2 cum
            show but1b pp2 cum with c
            play sound2 cum
            with c
            "Accompanied by a mind-melting orgasm, cum spills freely from my tip, covering [but]’s ass with cum deeply saturated with my sexual energy."
            play sound2 cum
            with c
            play sound2 cum
            with c
            "Her body wastes no time gradually absorbing every drop as if it were a delicious nectar."
            "There’s a glow of satisfaction and renewed strength evident in her eyes." 
            stop ambience1 fadeout 2
            stop moans1 fadeout 2
            call camerareset from _call_camerareset_20
            show but1b -pp2 -pp1 -t2 t1 with d
            mc "{i}Pant, pant…{/i} Did that help?"
            scene bg forest2
            show but horny succ blush
            camera:
                ypos -150 zpos -400
            with d
            "She turns to face me, her eyes still clouded with an insatiable hunger. The brief taste of my cum has only ignited a deeper need within her."
            but "I’m feeling parched. A little drink couldn’t possibly hurt now, could it?"
            with hpunch
            "I try to take a step back, but her tail sneaks in from behind and prods me back forward. The cave's oppressive darkness seemed to grow thicker, the air more stifling."
            "I swallowed hard; my throat dry. The urgency in her voice, the primal hunger in her eyes—it was all too real, too immediate. I could feel the heat of her breath against my skin, her proximity a potent reminder of her succubus nature, and already capable of getting me hard once again."
            mc "Come on, we need to find the other ingredients."
            "She shook her head, a shudder running through her as she stepped closer. The cavern walls seemed to close in, the shadows deepening. She leaned in, her soft lips brushing against my ear."
            show but neutral with d
            but "Please, baby… I… I need more~"
            "Her plea was almost a whimper, a sound of pure desperation. She didn't wait for my response, her hands trembling as they reached for my hips, her touch sending a shiver up my spine. I could feel my resolve weakening."
            mc "Just… be careful, okay? You can’t get the dewblossom without me."
            layeredimage but1c:
                always:
                    "but1cb"
                group succ:
                    attribute succ:
                        "but1csuccubus"
                group cum:
                    attribute cum:
                        "but1ccum"
                group eyes:
                    attribute e1:
                        "but1ce1"
                    attribute e2:
                        "but1ce2"
            show but1c succ e1 
            call camerabreath from _call_camerabreath_56
            play moans1 moansmisc3
            $ textbox = 3
            with d
            "She nodded, her breath hot against my skin. Slowly, she sank to her knees before me, my cock casting a shadow over her face. The sight of her, so vulnerable and yet so powerful."
            play ambience1 blowjob
            "I could barely keep my voice steady as her tongue started moving, the warmth and wetness of her lips drawing a groan from deep within my chest. She moved with a kind of desperate grace, each motion sending waves of pleasure coursing through me."
            mc "Mmhh! Oh, god, that’s good."
            show but1c e2 with d
            "Her mouth and fingers worked expertly, the need in her eyes never diminishing. She was hungry, starving for my energy, and yet there was a tenderness in her movements, a careful precision that kept me on the edge of bliss without tipping over into pain."
            "The cave seemed to spin around us, the world narrowing to the point of contact between us. Her mouth, her tongue, the way she moved—it was overwhelming. I could feel the pressure building, the inevitable release drawing closer with each passing second."
            mc "[but], I’m getting close…"
            play sound1 earthquake volume 0.7
            "She hummed around me, the vibration sending a shockwave of pleasure through my body. I couldn't hold back any longer, my climax hitting me with the force of an earthquake – actually, there might have been an earthquake too."
            play sound2 cum
            show but1c cum with c
            play sound2 cum
            with c
            "I cried out, the sound echoing off the cave walls as she pulled out and let my cum release all over her face and backside."
            play sound2 cum
            with c
            play sound2 cum
            with c
            "She didn't stop, her lips and tongue working my shaft to milk every last drop from me. The intensity of the sensation was almost too much, but she was relentless, determined to take everything I had to give."
            play sound2 cum
            with c
            play sound2 cum
            with c
            "My orgasm lasted an unnaturally long amount of time, its strength enhanced by her powers, and eventually the pleasure turned to discomfort."
            mc "Ngghh, [but] that’s… that’s enough!"
            scene bg forest2 
            call camerareset2 from _call_camerareset2_27
            stop ambience1 fadeout 1
            stop moans1 fadeout 1
            $ textbox = 1
            stop music
            with d
            "I pulled her away, a satisfied smile on her lips as she swallowed."
            show but happy succ blush with d
            "The hunger in her eyes had dimmed, replaced by a calm, almost serene expression."
            "She wiped her mouth free from cum, her cheeks flushed with exertion and the lingering effects of the alraune’s pollen."
            show but wink with d
            but "Thank you. I feel much better now." 
            "I could only nod, my body still shivering from the aftershocks of our encounter."
        "{i}Surely there's another way!{/i}":
            stop moans1
            "I look around and spot a potential solution. A nearby, underground well of water, and a bucket placed next to it."
            menu:
                "{i}Dump a bucket of cold water on her{/i}":
                    "I dash over to the well and buck up the bucket of water. It's already full, fantastic!" 
                    "Just as [but] turns around to question my eratic actions, she gets a sudden face full of cold water."
                    scene bg forest2 with d
                    but "W-W-Whaaat the fuck was that?!"
                    mc "{i}Phew{/i} I bet that'll cool you down."
                    but "How did you even get a bucket down here?!"
                    mc "If you're focused on that, I think that means we exceeded."
                    "With an exasperated sigh, [but] squeezes some water out of her hair."
                    but "I'm not thanking you, but... I do feel better."
                "{i}Ah, forget that. Let's just get the tail job over and done with{/i}":
                    jump but1
    play ambience1 cave
    scene bg forest3 with d
    "We continued deeper into the cave, [but] clutching a clump of leaves in her hand."
    mc "That alraune—it wasn’t a monster girl?"
    show but succ awkward with d
    but "No, just a regular monster. You won’t find any feral monster girls around here. We're next to a city; it's too urbanized for them to thrive."
    show but wink with d
    but "Disappointed there’s no cute plant pussy for you to slide your cock in?"
    mc "I’d prefer to avoid the topic of sex right now."
    show but bashful with d
    but "Your loss~ The dewblossoms are just up ahead. If I step out of line, you can give me a poke with one of them to give me a nasty jolt!"
    scene bg forest2 at flip with d 
    "As I stepped into the dewblossom area, the sight was more lush than before. There were significantly more dewblossoms than last time, so I decided to gather a bundle."
    stop music fadeout 13
    show but neutral succ with d
    "Out of the corner of my eye, I saw [but] experimenting with one of the flowers, getting a taste of the jolt she’d mentioned."
    but "{i}Sigh{/i} This potion is going to be a real bitch to drink, isn’t it? I wonder if…"
    "She turned to me, a frown creasing her face as if she’d just had an epiphany."
    play music butterstheme2
    show but awkward with d
    but "Did you know my other self?"
    mc "In a way, you could say that. She’s the one who taught me this recipe."
    show but wink with d
    but "And here I was calling you a kid. Guess that makes you an old man."
    mc "Hey, I’m not old either!"
    show but neutral with d
    but "The other me, the ‘original’ self, if you will… She couldn’t come to terms with what happened."
    mc "When you were afflicted by the succubus curse?"
    show but angry with d
    but "That’s right. Before then, I was a different person. Loving, motherly innocent… She was tricked, betrayed, twisted."
    show but awkward with d
    but "She rejected reality and buried herself deep inside."
    but "Now I’m… this. And I’ve been like this far longer than I was ever my original self…"
    show but neutral with d
    but "This… new me… is it a ‘succubus’ side, or just a new personality created to distance her from the monster she’d become?"
    mc "Why did you refuse to tell me earlier?" 
    show but awkward with d
    but "{i}Sigh{/i} It’s just… I’m not sure if she’s there anymore…"
    but "A part of me feels like she might be lost forever. It’s not that I was hiding it from you; it’s just… I might be all that’s left."
    show but neutral with d
    but "I mourn for her. I always have."
    play sound2 equip
    show black with d
    "I drop the dewblossom and pull [but] into a tight hug. She clung to me like she never wanted to let go."
    hide black
    camera:
        ypos -150 zpos -400
    show but smug blush
    with d
    but "Hugging a succubus… You’re a stupid kind of brave."
    mc "You needed one. Doesn’t matter what you are."
    call camerareset1 from _call_camerareset1_16
    mc "Now come on, we’re almost there. We’ve only got one ingredient left to find."
    show but -smug happy with d
    but "Right, let’s get that gelatine."
    play music butterstheme1 fadein 3
    play ambience1 night
    scene bg forest3
    "I led us deeper into the cave, toward a damp, shadowy section where an underground lake lay hidden. It was the perfect habitat for the elusive slimes. It may take a while to find one hidden in this darkness."
    show but wink succ with d:
        xalign -2
        linear 1 xalign 0.2
    but "Got one."
    "[but] glides into view and lifts up a blue blob."
    mc "Wha— but we just got here!"
    show but smug with d
    but "Yeah, while you were busy marveling at the view, I went ahead and grabbed some."
    mc "Wow, alright then! Let’s head back to your cottage!"
    show but awkward with d
    but "Right… Let’s go."
    scene bg forest4 with d
    "[but] guided me back to her house. Despite the fact that [but] had been so different for so long, the cabin’s interior was brimming with familiarity and nostalgia."
    show bg forest5 with d
    "Quietly, [but] brushed past me, her demeanor subdued as she began to prepare her equipment. Since we got the gelatine, the chatter and banter had all but disappeared."
    show but succ awkward with d
    but "You can prepare the dewblossom for me."
    mc "Could you show me how?"
    show but smug with d
    but "Oh, you don’t know that part? I thought you knew everything."
    mc "Is something wrong?"
    show but neutral with d
    but "How did you know I had a house here? I can tell you knew the way. Hell, the interior of the caves too. You often wouldn’t even wait for my directions."
    show but angry with d
    but "I was focused on gathering ingredients, so I let you get away with vague answers, but too much has built up. I told you who I am; now I need to know who or what you really are." 
    mc "I’ve never been particularly good at lying, so I’ll give you the complete truth."
    mc "It’s because… I did know the way. I’ve been here countless times, hunting for ingredients in those very caves, all with a different you in another universe."
    show but neutral with d
    but "That’s the craziest thing I’ve ever heard, and yet, I’d be a fool to doubt it."
    show but bashful with d
    but "Even knowing the risks, you really came here to help me?"
    mc "How could I not? You’re [but], one of my best friends."
    show but awkward blush with d
    but "Nnghh… You’re going to make me blush…"
    show but happy -blush with d
    but "The me in the other universe—she was my ‘other self,’ wasn’t she? Can you tell me what she was like?"
    mc "You already know, perhaps better than I do. Because you are her; innocent, caring, motherly."
    mc "This house, it’s a mirror image of hers. You have a lot more in common with your original self than you realize."
    show but bashful with d
    hide but with d
    "[but] began to brew the potion, gesturing for me to drop the dewblossoms in whole."
    show but bashful succ with d
    but "Mmhh… I guess we’ll find out~"
    but "It’ll take a few hours to brew this, and even longer for it to take effect once I’ve drunk it."
    show but happy with d
    but "But you’ll come back, won’t you?"
    mc "To get my ‘balls completely drained’? Wouldn’t miss that for the world."
    show but laughing with d
    but "Thank you so much, [mc]. I better hurry up and escort you out before I lose control again~"
    stop music fadeout 4
    scene bg forest1 with dissolve
    "Ten minutes later, I stepped outside the forest, passing through the guarded gate once again."
    misc "Well, I’ll be damned. You actually made it back."
    mc "The stories are overrated, man. The forest isn’t that bad."
    misc "Guess you didn’t run into any giant bears."
    mc "Giant wha?!"
    play music moxietheme fadein 3
    scene bg apartment with d
    "Back in [mox]’s apartment…"
    show mox surprised with d
    mox "Yep, there are giant, nocturnal bears in the Nevermore Forest. I can’t believe you went in there alone!"
    mc "Luckily, I only walked a few minutes in before I made contact with [but]."
    show mox happy with d
    mox "Ah, you were just at the city outskirts, then. Phew! The Nevermore Forest stretches for miles. You’d have to walk a considerable distance before you encountered anything truly dangerous."
    mox "But I’ve heard that the real danger lies in the forest’s heart—an independent section of ‘dark lands’, where an ancient castle lies in ruins."
    mc "More about these ‘Dark Lands’? I’m still trying to wrap my head around it. Would it be alright if I asked a few questions?"
    show mox awkward with d
    mox "I lost my village to it, so I can give you an accurate account, though not a pleasant one."
    menu fo1m1:
        "What is the current state of the planet?":
            show mox neutral with d
            mox "The Dark Lands is like a creeping blight, a corruption slowly devouring the country. It covers about 10%% of the globe, and roughly 33%% of our island. The west is completely lost—cities like Maplewood and Cloud Harbor."
            mox "Right now, the darkness is encroaching further west across the seas, threatening other countries, and gradually moving towards Arcadia, which sits at the centre of the country, also called Arcadia – confusing, I know." 
            mox "[aur] pours a significant amount of her power into holding it back, but this only slows its advance. It’s like trying to stop an avalanche with a shovel."
            mox "Tensions are sky-high. The country is practically at war, and we’re even receiving international aid from the Dragon Lands."
            jump fo1m1
        "What happens inside the dark lands?":
            show mox awkward with d
            mox "The first thing that hits you is a suffocating darkness. It’s like a night that drags on forever, but not just any night. It’s an unnatural void that defies the sun."
            mox "And within those shadows, hostile nightmares appear and attack on sight." 
            mox "If you die in the shadow lands, you become one of those nightmares, twisted and..."
            show mox sad with d
            "[mox] faltered, breaking out in a cold sweat. She took a moment to compose herself."
            show mox neutral with d
            mox "Sorry. I can’t describe it properly."
            mox "Just know this: all those nightmares were once living beings—ponies, unicorns, pegasi."
            jump fo1m1 
        "You mentioned there’s darkness inside Nevermore Forest?":
            show mox neutral with d
            mox "Yeah, about ten miles in. For the past year, pegasi flying overhead have reported that the ruins of Old Arcadia are cloaked in darkness."
            mox "It’s supposed to be a secret, but [pen] told me that it’s become a focal point for Arcadian scientists trying to understand this darkness."
            mox "Why it’s there, of all places, I can’t say. But if they can eliminate it there, perhaps they can remove it everywhere."
            jump fo1m1
        "(Continue)":
            pass
    show mox happy with d
    mox "I don’t want to place any burdens on you, but I sincerely hope that the power of these virtues is enough to push back the darkness."
    mc "I’m with you on that. All I can do is put my faith in those who place their faith in me." 
    scene black with d
    "[sel], I hope you can help this world."
    "..."
    scene black with d
    if replay == 1:
        return
    $ forestroute1 = 1
    $ forestcompletion += 1
    $ completion += 1
    $ butmsg1 = 1
    $ unread += 1
    $ unreadbut += 1
    jump newday
label forest2:
    play music danger
    play ambience1 ambiencenight
    scene bg forest1 with d
    "The trees whisper in the wind, their leaves casting fleeting shadows in the pale light of the moon. There’s a solace in the solitude, a familiarity in the way the path snakes through the woods."
    "There’s nothing to fear this close to the bustling city. No creatures lying in wait, only the steady beat of my heart, the rhythm of my steps on the ground. Or so I tell yourself."
    "Last time, I ventured into the caves, those dark, damp places where actual monsters lurk. But this is different. This is the forest. This is safe."
    scene bg forest4 with d
    "The cabin comes into view, a warmth etched against the skeletal trees. The sight of it brings a small sense of relief."
    "[but] is waiting. Last time I saw her, she was still brewing that potion. For her sake, I hope it worked."
    scene bg forest5 with d
    "I push open the door and step inside. The cabin is lit by the warm glow of candles, the air thick with the scent of herbs and something darker, sweeter."
    play music butterstheme1 fadein 10
    show but2a 
    $ textbox = 2
    with dissolve
    "Following the scent, I find her."
    "She lies while toying with her hair, a lazy smile curling her lips. The potion must have worked, because she looks different now. There’s a glow to her, a vitality. Her eyes—deep, crimson—sparkle with something new. Hunger. Lust."
    "She’s brimming with life, with energy, and when she looks at me, it’s like I’m the only thing that matters in all the world."
    but "Well, well... Look who’s finally come back. I was starting to think you’d forgotten about me~"
    "She purred; her voice smooth as honey."
    mc "There’s no way I’d forget after what you promised last time. But more than that, I needed to see if the potion worked."
    but "Oh, it worked. Better than I ever could have dreamed."
    "She shifted on the bed, her body moving with a grace that was near feline. The firelight from the candles flickered across her curves, casting shadows that played on the texture of her fur, her pink locks spilling over her shoulders like liquid."
    mc "So… you’re finally free?"
    "Her smile wavered, just a flicker, and I caught a glimpse of hunger in her eyes."
    but "Free? Not quite. But I’m not dangerous anymore. I can finally… indulge."
    mc "You must’ve waited a long time for this."
    but "Mmhhmm. Fifty years. Fifty years of waiting, starving, holding it all back."
    but "But now…"
    play sound2 equip
    scene bg forest5 
    show but succ horny
    camera: 
        zpos -350 ypos -150
    $ textbox = 1
    with d
    "She sat up, quick and sure in the darkness, her form a silhouette of curves along with dramatically flaring wings and a coiled tail."
    but "Now, I can’t wait any longer."
    "She reached out and touched me, her body heat searing through my skin like a brand."
    mc "[but]…"
    "I tried to speak, but she silenced me with a finger to my lips."
    show but happy blush with d
    but "Shh…"
    "She leaned in close, her breath warm against my ear."
    show but horny with d
    but "I’ve waited long enough. I want you, and I’m going to have you. Every. Last. Drop."
    "There was no resisting her. She was a succubus, after all. She knew every trick, every way to make a man fall to his knees."
    "Her lips found mine, and I was lost. She was all heat and fire, her body pressed tight against me, her hands moving over me like she could never have enough."
    stop music fadeout 3
    scene black with d
    "She led me to the bed, and I followed, already beguiled and helpless to do anything else. She pushed me down, her body moving over mine with undeniable strength. She wasn’t cursed anymore, but she was still a succubus, and she was starving."
    layeredimage but2b:
        always:
            "but2bb"
        group eyes:
            attribute e1:
                "but2be1"
            attribute e2:
                "but2be2"
        group stockings:
            attribute stockings:
                "but2bstockings"
        group succubus:
            attribute succ:
                "but2bsuccubus"
        group spanked:
            attribute spanked:
                "but2bspanked"
        group cum:
            attribute cum:
                "but2bcum"
        group plug:
            attribute plug:
                "but2bplug"
        group pregnant:
            attribute pregnant:
                "but2bpregnant"
        group sex1:
            attribute v1:
                "but2bv1"
            attribute a1:
                "but2ba1"
        group thong:
            attribute thong1:
                "but2bthong1"
            attribute thong2:
                "but2bthong2"
        group sex2:
            attribute v2:
                "but2bv2"
            attribute a2:
                "but2ba2"
    scene but2b succ e1 
    call camerabreath from _call_camerabreath_69
    play music sextheme fadein 3
    play moans1 moansmisc2
    $ textbox = 2
    with d
    "Turning away from me, she lowered herself onto the bed, her back arched, her head down, and her glorious bubble butt raised high. It was an offering as old as time, a posture both submissive and demanding in equal measure."
    but "Take me~"
    "Her voice was a whisper, soft and urgent. There was no command in it. Only need. A deep, primordial need that rippled through the air between us, thick and heavy as smoke."
    menu:
        "You don’t have to ask twice.":
            pass
        "I was hoping we could do this another day.":
            "The words were on the tip of your tongue, but they don’t come."
            "{i}You walked into the home of a succubus, knowing full well what that meant. There’s no leaving now!{i}"
    "The words echoed through me, and I felt something. A sudden pull of her magic, creeping in, quiet at first, then swelling like a tide that could not be turned."
    "It wasn’t just desire. It was something deeper, something that reached into the core, took hold, and refused to let go. My thoughts grew cloudy, and my body moved of its own accord, as if guided by a will that wasn’t my own."
    "Her succubus magic entwined with my mind, pushing, pulling, until there was no distinction between what I wanted and what she demanded."
    but "Mmm… Good boy."
    "I moved towards her, my hands finding the curve of her ass, and she shivered under my touch. It was like she’d been waiting an eternity for this, holding back for so long that now it was like a dam breaking, inevitable and unstoppable."
    "Her body responded to mine with an eagerness that bordered on desperation, and she pushed back against me, urging me forward with unsubtle movements. Each second, her magic wound itself tighter around my mind, binding me to her."
    but "Now, slide it in~"
    play sound2 cum
    show but2b v1 e2 with d
    "Almost as if watching myself from the third person, I saw my hand wrap around my cock and align it with her pussy. She was initially very tight, but with enough force, her folds parted, and I pushed inside." 
    "As my shaft sank into her depths, and the world seemed to fall away. There was nothing but the feel of her, the heat of her, the way her pussy clenched around my cock, her insides pulling me deeper, urging me on." 
    but "Uuoohhh, I’ve waited so long for this… It’s perfect, just like I dreamt."
    mc "Don’t you worry, I’m going to make all your dreams come true."
    camera:
        linear 0.1
        linear 0.4 xpos -6
        linear 0.1
        linear 0.3 xpos 6
        repeat
    "I began thrusting immediately – wouldn’t have been able to stop myself if I tried, and it was more than just the magic that contributed to that. The feeling of her pussy was euphoric, gracing every inch of my shaft with unparalleled bliss."
    but "Yes, just like that! Let me feel every inch of you~"
    mc "Heh, I won’t stop until you’ve had your fill."
    "Now deep inside, her magic flared, a rush of energy that coursed through me, heightening everything, making every touch, every movement, more intense, more powerful. I could feel her guiding me, controlling the rhythm, the pace, until it was just the two of us, lost in that dark, consuming dance."
    but "Nngghh, you’re so close… I can almost taste it! Keep going, my love~"
    mc "Ooohhh, take it all, [but]! I’m all yours."
    play sound2 cum
    show but2b cum v2 
    show internalcreampie
    with c
    play sound2 cum
    with c
    "The first time I came, it was like an explosion, a release of everything I had, everything I was. It was raw and primal, a wave of pleasure that crashed over me, left me gasping, trembling." 
    play sound2 cum
    with c
    play sound2 cum
    with c
    "And she took it all, every last drop, her body drinking it in, pulling far more from me than I’d ever release in an ordinary orgasm."
    hide internalcreampie
    show but2b e1 
    with d
    "But she wasn’t done. Not by a long shot. Her power surged again, filling me with a renewed vigor, pushing me forward, demanding more."
    but "Don’t stop now, I need more. I need everything you’ve got. Feed me, until there’s nothing left to give."
    mc "I’m not stopping until you’ve drained me dry. You asked for it, and you’ll get it!"
    show but2b e2 with d
    "And I gave it to her, again and again. Each time, she took it all, draining me until I thought there was nothing left. Only for her to push me further, to pull more from me, her body a vessel of insatiable need." 
    play sound2 cum
    with c
    "The room was filled with the sounds of sex, the soft moans and gasps, cries of pleasure that spilled from our lips. It was endless, a cycle of give and take, of pleasure and pain, and I was lost in it, drowning in the sensation, in the feel of her, in the magic that held me in its grip." 
    play sound2 cum
    with c
    but "We’re not done, not even close. You’re mine, all mine, until we’re both too far gone to care."
    mc "{i}Pant, pant{/i} I’m right here with you, every second of it." 
    play sound2 cum
    with c
    "She came, again and again, each climax pushing me closer to another of mine, each release a fresh surge of energy that pulled me along with her."
    "I was caught in that endless spiral, lost to the world, to everything but the feel of her, the taste of her, the way she moved beneath me, around me, consuming me. Her body trembled with each wave of pleasure, and I could feel her magic pulling at me, taking everything I had to give." 
    play sound2 cum
    show black:
        alpha 0
        linear 1.5 alpha 0.5
    with c
    "And then, finally, it was too much. The last climax hit me like a freight train, a rush of pleasure so intense that I felt myself slipping, the world growing dim, as I gave her the last of what I had."
    scene black 
    call camerareset from _call_camerareset_21
    call stopbgs from _call_stopbgs_40
    stop music fadeout 1
    $ textbox = 1
    with d
    "The last thing I felt was her body, warm and soft beneath mine, her magic still wrapped around me, holding me close, pulling me deeper into a soothing sleep."
    "…"
    "I awoke to the soft creak of floorboards. My body was heavy after being wrung out let a wet rag. I was completely empty." 
    scene bg forest5 with d
    "As my eyes adjusted, the room came into focus. The candle fire had burned low, casting a dull glow across the walls. I was still in the bed, the sheets tangled around my legs."
    "I shifted, and the dull throb in my groin told me all I needed to know. My balls were drained, completely fuckin' drained."
    "But there was no fear, no regret. Just a strange sort of contentment."
    play music butterstheme2 fadein 2
    show but happy with d
    "The door creaked open, and I turned my head. [but] stood there, framed by the doorway, the light from the hall casting her in shadow."
    "She wasn’t the same as before, though. Her silhouette lacked wings and the additional tail. There was something different about her now, something softer, more familiar…"
    "She was no longer the succubus who had drained me hours ago. She was the ‘normal’ [but] again, or at least a gentler version of her."
    show but laughing with d
    but "Hello there."
    "Her voice was soft, carrying a warmth that eased some of the weariness in my bones. She stepped into the room, a steaming cup in her hands."
    show but wink with d
    but "I thought you may need this."
    "I lifted myself up on the bed, wincing slightly as the movement stirred the soreness in my body."
    mc "What is it?"
    show but bashful with d
    but "A little remedy I brewed. Should help restore your strength, and maybe get your... uhm, manhood back in working order. That part is untested, because I don’t… you know, hehe, here you go."
    mc "Ha, I’m sure the other women in my life will appreciate that. I was half-expecting to be shooting blanks for the rest of the week."
    "I took the cup from her, the warmth of it seeping into my fingers. I brought it to my lips, the aroma of herbs filling my nose. It tasted earthy and I could feel it working almost immediately, a slow warmth spreading through me."
    "[but] sat on the edge of the bed, observing with a quiet patience. There was a softness to her gaze, a tenderness that hadn’t been there before."
    show but laughing with d
    but "Looks like the potion worked! What a relief." 
    "I nodded, taking another sip of the tea. The weariness in my muscles was dissipating so actively I could feel them tingle."
    mc "Might be stating the obvious, but you seem different."
    "She smiled, wistful smile that spoke of long years."
    show but awkward with d
    but "I am different. I’m the original [but]."
    but "The introspection you gave me, combined with the potion… it’s helped me reconnect with an old part of myself. Though it’s strange, I don’t have all the memories—just shards, fragments."
    mc "So you’re back to sharing the same body with another self."
    show but neutral with d
    but "Two parts of a whole, yet not entirely the same. The memories don’t align perfectly, and sometimes it feels like I’m missing something."
    but "But there’s one thing that’s clear. When I gave myself over to my other side, I saw it as a monster. I thought it would destroy everything I’d built." 
    but "That’s why I fled, abandoning my past life and all the connections that came with it. She didn’t have full access to my memories, so I shut myself away forever to protect my loved ones."
    but "But… it didn’t hurt anyone."
    "I set the cup down on the bedside table, leaning back against the headboard."
    mc "So, what does that mean to you?"
    show but awkward with d
    but "It means that she wasn’t a monster at all…"
    but "She was still me. Just… more intense. But the love, the compassion, the care—they were still there."
    mc "I agree. Sure, she may have been a succubus, but your core, the part that defines who you are, hadn’t changed one bit."
    mc "If you ask me, you never really left. You were just wearing a different mask."
    show but angry with d
    but "You’re right, and I’m not in denial anymore. I buried myself for so long, hidden behind the trauma of what I was forced to become. But with this… this gift you’ve given me, I can see it now. I can see what I was missing."
    but "I was reckless. I tried to shut myself out, pretend I wasn’t there, to hide from what I’d become. And I wouldn’t blame her if she harbored hatred towards me because of that."
    "I shook my head, turning to face her fully."
    mc "But she didn’t, [but]. Not once did your succubus side show any bitterness towards you. If anything, there was a longing, like she knew something vital was missing. Like she was incomplete without you."
    "She took a deep breath, absorbing the words."
    show but neutral with d
    but "I’ve felt it too… That emptiness, that sense of something lost."
    but "But now, seeing it clearly, I can’t help but wonder why I didn’t embrace her sooner. We could have helped each other, made each other whole."
    mc "Now you can. Together, you can be more than just fragments of a life lost to circumstance. You can be whole again."
    show but happy with d
    but "Together! We can achieve so much more. I can use my ordinary form to visit the city again, to shop, to meet people like [lil] and the Virtues you spoke of."
    but "With my succubus form, I can defend myself, gather ingredients, even fly."
    mc "And let’s not forget the many other perks of being a succubus! {i}Wiiink{/i}"
    "There was a light in her eyes now, a spark that hadn’t been there before."
    show but laughing with d
    but "I don’t have to be a hermit witch, deep in the woods, forgotten by the world."
    mc "You can live again, [but]. Truly live."
    "Reaching out, her hand found mine and squeezed it with a loving passion."
    show but bashful with d
    but "It sounds absurd, doesn’t it?"
    "She said with a small, self-deprecating smile tugging at the corner of her lips."
    but "Wanting to sell potions and function in society like a normal person. But to me, connection with others is everything."
    but "And you... you’ve brought me back to life, [mc]. You’ve given me that chance."
    mc "Hey, you know my name. So, do you remember a few things from the other side?"
    show but laughing with d
    but "It’s a bit hazy. I grasp the important parts, but most importantly, I remember how you made me feel."
    "[but]’s gaze flickered downward. It was then that we both noticed a bulge under the blankets."
    "Her eyes widened as she realized the full extent of the effect her tea had on me. A soft blush crept up her cheeks, and she cleared her throat, her fingers moving to the edge the duvet."
    show but happy blush with d
    but "I see… It seems my potion may have been a touch more effective than I intended."
    mc "First, the power of a succubus, and now this. Quite the workout."
    "Her voice was low, almost playful. Despite the absolutely extraordinary sexual encounter I’d just had with her succubus side, everything was different right now."
    "I wondered if, despite her new-found softness, she would still exhibit that same confident, commanding presence."
    "[but] leaned over with curiosity as she unveiled my throbbing shaft."
    show but bashful with d
    but "T-This thing was {i}inside{/i} me?! But it’s enormous!"
    mc "Haha, I can take handle this myself if you prefer."
    show but wink with d
    but "Ah, but I have my own enormous assets to work with!"
    layeredimage but2c:
        always:
            "but2cb"
        group succ:
            attribute succ:
                "but2csuccubus"
        group eyes:
            attribute e1:
                "but2ce 1"
            attribute e2:
                "but2ce 2"
            attribute e3:
                "but2ce 3"
        group cum1:
            attribute c1:
                "but2ccum"
        group horse:
            attribute horse:
                "but2chorsecock"
        group cum2:
            attribute c2:
                "but2chorsecockcum"
        group milk:
            attribute milk:
                "but2cmilk"
    show but2c e1 
    call camerabreath from _call_camerabreath_70
    play moans2 moansmisc2
    $ textbox = 4
    with d
    "Her breasts brushed against my hips as she positioned herself below me. Her touch was gentle, almost reverent, and as she moved, her eyes locked onto mine, her expression a mix of focus and tenderness."
    but "I think I can help you with this."
    show but2c e2 
    play ambience1 handjob2
    camera:
        linear 0.1
        linear 0.4 ypos -6
        linear 0.1
        linear 0.3 ypos 6
        repeat
    with d
    "Her voice was a soft murmur, a contrast to the intense heat between us. She adjusted herself, making sure my cock was completely snug between her breasts, and then began to use her hands to smother my shaft in them."
    "The sensation was exquisite, the warmth and softness enveloping my shaft as her breasts moved. The rhythm was unpracticed, but that was easily made up for by enthusiasm and motherly care. She took her time, each motion calculated to maximize the pleasure."
    show but2c e1 with d
    "However, perhaps due to her time as a succubus, it didn’t take long for her movements to become fluid and experienced. Her gaze remained steady, watching my reactions with a mix of curiosity and affection."
    but "You look so cute right now… Mmhh… C-Could you call me mommy?"
    $ mommy = 0
    menu:
        "Of course, mommy.":
            $ gent1 = "mommy"
            $ mommy = 1
            but "Mmhhh… That’s so sweet on the ears~"
            "Her movements grew faster and visibly more excited."
        "Sorry, that’s not my thing.":
            $ gent1 = "me"
            but "That’s fine with me~"
    "The room was filled with the sound of her soft, steady breathing and the occasional murmur of satisfaction. My own moans were almost involuntary, escaping with each push and pull of her breasts. Succubus [but] had always been skilled in her craft, but now, there was an added layer of her affection and care that uniquely elevated the experience."
    show but2c e2 with d
    but "Just relax. Let [gent1] take care of you."
    "My shaft grew tense, the intensity growing with each passing second until finally, with a shuddering breath, I was on the edge of cumming."
    but "That’s it, good boy. Just let it all cum out for [gent1]."
    play sound2 cum
    show but2c c1 with c
    play sound2 cum
    with c
    "[but]’s movements became more fervent, her focus absolute as she guided me through the final stages. Her soft, encouraging whispers filled the air, and as I finished, the relief was profound, almost cathartic."
    play sound2 cum
    with c
    play sound2 cum
    call camerabreath from _call_camerabreath_71
    with c
    "As the last waves of pleasure subsided, [but] returned her gaze to me, her expression one of quiet satisfaction. She looked at me with a mixture of affection and amusement."
    show but2c e3 with d
    but "There, all better now."
    mc "Even with the wild passion of your succubus side, this was something else entirely. A different kind of wonder."
    but "Hehe, I’m glad we’re not competing for the same genre, then~"
    scene bg forest5 
    $ textbox = 1
    call camerareset from _call_camerareset_22
    call stopbgs from _call_stopbgs_41
    with d
    "She moved to retrieve a cloth, her movements calm and unhurried. When she finished cleaning up, she settled back beside me."
    show but laughing with d
    but "I hope that was good~! I know we're still somewhat strangers, but I’d like for us to become very close."
    "Her voice was calm, yet still carrying that trace of playful confidence."
    mc "That was more than good, [but]. It was exactly what I needed, and I can’t wait to see what else you can do."
    show but bashful blush with d
    but "Oh my, you’re not just interested in my succubus side?"
    mc "You’re offer something different. With her, it’s intense and raw. With you, it’s loving and serene. Both are great in their own ways."
    show but wink with d
    but "Fuhuhu, is that how you see me? I can’t claim to have the experience to judge, but we’ll discover that together, won’t we?"
    mc "Absolutely! By the way, how long was I out?" 
    show but happy -blush with d
    but "You’ve been asleep for a while and it's quite late now. Are you going to return home?"
    mc "Ack, nearly 2AM! [mox] will get worried if I don't check myself in."
    show but laughing with d
    but "Thank you, for everything. You’ve done more than you know. I’ll get in touch with [lil] soon. And remember, you’re always welcome here. Anytime."
    mc "Goodnight, [but]."
    show but happy with d
    but "Goodnight, sweetie! Safe travels."
    stop music fadeout 3
    play ambience1 ambiencenight fadein 2
    scene bg forest4 with d
    "I step out into the night, the cool air a sharp contrast to the warmth of her cabin. The forest outside is silent, the stars hanging low and heavy in the sky. My thoughts drift as I make my way back to the city."
    scene bg apartment with d
    "Back in the apartment, the city’s distant, ever-present hum is barely audible through the windows. [mox] is lounging on the couch, a book in her lap."
    play music moxietheme
    show mox happy with d
    mox "Late night for you too?"
    mc "Yup. Another trip into the woods. How’d your show go?"
    show mox laughing with d
    mox "Today was a smaller audience, so I took the opportunity to test some new tricks. They really enjoyed them! I’ll definitely weave them into my regular routine."
    mox "How was your adventure into the forest?"
    mc "Well… [mox], have you ever heard of a succubus?"
    show mox surprised with d
    mox "They’re seductive demonesses that drain energy from men in sex, right? Don’t tell me you met one!"
    mc "Kind of. [but] is a succubus, but I helped her brew a potion to stave off the deadly energy drain."
    show mox neutral with d
    mox "So, I take it you being alive means the plan worked? Sounds like it was a hell of a gamble."
    mc "The potion we used has always been reliable for me in the past. I had no reason to doubt its power."
    mc "Now, she’s not only capable of having sex again, but she can retract her succubus wings and tail and pass as a normal pony. She’ll be joining us with the other virtues."
    show mox bashful blush with d
    mox "Hmm… Does she still retain all her succubus abilities? You know, like... her prowess in the bedroom?"
    mc "Ehehe… She’s still got all the moves. Hypnosis, a pheromonal aura, seductive whispers, pleasure enhancement..."
    show mox surprised with d
    mox "Yikes! Sounds like I need to up my game to keep up with the likes of her!"
    mc "Don’t worry about that. My body can only handle her once every few weeks at most."
    scene black with d
    "[mox] and I drifted into talk of demons as the night wore on. The conversation made me realize that I hadn’t thought much about their existence and origin."
    "Demons just casually existing… Just what kind of secrets does this universe hold beyond my understanding?"
    scene black with d
    if replay == 1:
        return
    $ forestroute2 = 1
    $ forestcompletion += 1
    $ completion += 1
    jump newday
