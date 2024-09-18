﻿label farmwork:
    play music rainytheme
    scene bg greenhouse with d
    if farmtut == 0:
        $ farmtut = 1
        show hon laughing with d
        hon "So glad decided to work here! Let me show you the ropes!"
        "(Working at the farm is simple. All you need to do is plant some seeds, they'll take three days to grow.)"
        "(Once grown, you'll see a notification on the map, you can then come and collect the plants and plant new ones.)"
        "(The base sell price of the plants is $40, but you can water the plants once per day to earn an additional 5%% for each plant.)"
        hon "It's very simple once you get the hang of it. Good luck, stud!"
        hide hon with d
    layeredimage farmwork:
        always:
            "farmworkpots"
        if fup3 == 1:
            "farmworkpot4"
        if fdaysleft == 0 and seeds > 0:
            "farmworkplants"
        if fup3 == 1 and fdaysleft == 0 and seeds > 0:
            "farmworkplant4"
        if watered >= seeds and seeds > 0:
            "farmworkwateringcan"
    show black:
        alpha 0.5 blend "multiply"
    show farmwork
    with d
    menu farmworkmenu:
        "Work":
            if fdaysleft == 0 and seeds > 0:
                $ gent1 = "Ready"
            else:
                $ gent1 = "Not Ready"
            menu farmworkmenu2:
                "Days Left: [fdaysleft] - Base Value: [plantsellvalue] - Quality: [plantquality:.2f]x"
                "Plant Seeds [seeds]/[pots]":
                    if seeds > 0 and seeds != pots:
                        play sound2 item
                        $ fdaysleft += 1
                        $ seeds = pots
                        "You planted these extra seeds a little late, but I'm sure peer pressure will help it catch up. (+1 Days Left Added)"
                    elif seeds != pots:
                        play sound2 item
                        $ fdaysleft = fdaysleftbase
                        $ seeds = pots
                        "[pots] seeds have been planted. Don't forget to water them."
                    else:
                        play sound2 error
                    jump farmworkmenu2
                "Watered [watered]/[pots]" if fdaysleft > 0:
                    if watered < seeds:
                        play sound2 item
                        $ watered += 1
                        $ plantquality += waterbonus/100
                    else:
                        play sound2 error
                    jump farmworkmenu2
                "Harvest ([gent1])":
                    if fdaysleft == 0 and seeds >= 1: 
                        play sound2 shop2
                        $ gen1 = int(plantsellvalue*seeds*plantquality)
                        $ seeds = 0
                        $ plantquality = 1
                        $ money += gen1
                        $ gent1 = "Not Ready"
                        "Earned $[gen1] for a successful harvest!"
                    else:
                        play sound2 error
                    jump farmworkmenu2
                "Finish":
                    scene black with d
                    if fup6 == 0:
                        "After working for a few hours, I return home."
                        jump newday
                    else:
                        "Thanks to the sprinklers, I'm in and out in only a few minutes."
                        jump worldmap
        "Upgrades":
            menu fupgradesmenu:
                "Money: $[money] \nDays to Grow: [fdaysleftbase] - Base Sell Value: [plantsellvalue] - Watering Bonus: [waterbonus]%% \nPots: [pots]."
                "Fertilizer ($40): {i}+5%% Watering Quality" if fup1 == 0:
                    if money >= 40:
                        play sound2 shop2
                        $ fup1 = 1
                        $ fups += 1
                        $ money -= 40
                        $ waterbonus += 5
                "Tier 2 Seeds ($80): {i}+1 Day to Grow. +$20 per Plant (Toggleable)" if fup2 == 0:
                    if money >= 80 and fup2 == 0:
                        play sound2 shop2
                        $ fup2 = 1
                        $ fups += 1
                        $ money -= 80
                        $ fdaysleftbase += 1
                        $ plantsellvalue += 20
                        $ fup2toggle = 1
                "The Fourth Pot ($160): {i}+1 Pot" if fup3 == 0 and fups >= 1:
                    if money >= 160:
                        play sound2 shop2
                        $ fup3 = 1
                        $ fups += 1
                        $ pots += 1
                        $ money -= 160
                "Magical Water ($260): {i}+5%% Watering Quality. +$6 Sell Value" if fup4 == 0 and fups >= 2:
                    if money >= 260:
                        play sound2 shop2
                        $ fup4 = 1
                        $ fups += 1
                        $ money -= 260
                        $ waterbonus += 5
                        $ plantsellvalue += 6
                "Tier 3 Seeds ($320): {i}+1 Day to Grow. +$24 per Plant (Toggleable)" if fup5 == 0 and fups >= 3:
                    if money >= 320 and fup5 == 0:
                        play sound2 shop2
                        $ fup5 = 1
                        $ fups += 1
                        $ money -= 320
                        $ fdaysleftbase += 1
                        $ plantsellvalue += 24
                        $ fup5toggle = 1
                "Sprinkler System ($400): {i}Working at the Farm no longer takes up an entire night" if fup6 == 0 and fups >= 4:
                    if money >= 400:
                        play sound2 shop2
                        $ fup6 = 1
                        $ fups += 1
                        $ money -= 400
                "Purchased Upgrades":
                    menu fupgradesmenu2:
                        "Fertilizer: {i}+5%% Watering Quality" if fup1 == 1:
                            jump fupgradesmenu2
                        "Tier 2 Seeds ([fup2toggle]): {i}+1 Day to Grow. +$20 per Plant (Toggleable)" if fup2 == 1:
                            play sound click
                            if fup2toggle == "Off":
                                $ fup2toggle = "On"
                                $ fdaysleftbase += 1
                                $ plantsellvalue += 20
                            elif fup2toggle == "On":
                                $ fup2toggle = "Off"
                                $ fdaysleftbase -= 1
                                $ plantsellvalue -= 20
                        "The Fourth Pot: {i}+1 Pot" if fup3 == 1:
                            jump fupgradesmenu2
                        "Magical Water: {i}+5%% Watering Quality. +$5 Sell Value" if fup4 == 1:
                            jump fupgradesmenu2
                        "Tier 3 Seeds ([fup5toggle]): {i}+1 Day to Grow. +$24 per Plant (Toggleable)" if fup5 == 1:
                            play sound click
                            if fup5toggle == "Off":
                                $ fup5toggle = "On"
                                $ fdaysleftbase += 1
                                $ plantsellvalue += 24
                            elif fup5toggle == "On":
                                $ fup5toggle = "Off"
                                $ fdaysleftbase -= 1
                                $ plantsellvalue -= 24
                        "Sprinkler System ($400): {i}Working at the Farm no longer takes up an entire night" if fup6 == 1:
                            jump fupgradesmenu2
                        "Back":
                            jump fupgradesmenu
                                            
                "Back":
                    jump farmworkmenu
            jump fupgradesmenu
        "Back":
            jump farm
#base:
# B 30*3 15% -> 103.5 -> 34.5/day
# U1 (+5%) 30*3 30% -> 117 -> 39/day
# U2 (+1 Day. +$20) 50*3 30% -> 195 -> 48.75/day
# U3 (+1 Pot) 50*4 30% -> 260 -> 65/day
# U4 (+5% Water. +$6) 56*4 45% -> 324.8 -> 81.2/day
# U5 (+1 Day. +$24) 80*4 45% -> 464 -> 92.8/day


init:
    $ plantsellvalue = 30

    $ seeds = 0
    $ pots = 3
    $ watered = 0
    $ waterbonus = 5

    $ plants = 0
    $ plantquality = 1

    $ fdaysleft = 0
    $ fdaysleftbase = 3
    
    $ fup1 = 0
    $ fup2 = 0
    $ fup2toggle = "On"
    $ fup3 = 0
    $ fup4 = 0
    $ fup5 = 0
    $ fup5toggle = "On"
    $ fup6 = 0
    $ fup7 = 0
    $ fup8 = 0
    $ fup9 = 0
    $ fups = 0



    $ farmtut = 0

label brothelwork:
    play music rainytheme
    stop ambience1 fadeout 3
    menu brothelworkmenu:
        "Current Rank: [rank], [rankn]."
        "Start Work":
            call genreset from _call_genreset_13
            $ satis = basesatis
            "Today's customer is..."
            $ gen1 = renpy.random.randint(1,bwchars)
            if gen1 == 5 or gen1 == 6 or penhosted == 0 and rank >= 5:
                show lil happy with d
                lil "Uhm, this place isn't exactly my comfort zone, but it's like I said, I'm trying to branch out." 
                $ current_customer1 = customerlil1
                $ current_customer2 = customerlil2
                $ customer = "{}".format(lil)
                $ lilhosted += 1
            elif gen1 == 4 or rubhosted == 0 and rank >= 4:
                show rub happy with d
                rub "Show me what you've got, darling, and I'll put in a good word for you to the boss~"
                $ current_customer1 = customerrub1
                $ current_customer2 = customerrub2
                $ customer = "{}".format(rub)
                $ rubhosted += 1
            elif gen1 == 3 or honhosted == 0 and rank >= 3:
                show hon happy with d
                hon "Thought I'd give this place a try! Imagine my surprise when I find out y'all work here, sugarcube!"
                $ current_customer1 = customerhon1
                $ current_customer2 = customerhon2
                $ customer = "{}".format(hon)
                $ honhosted += 1
            elif gen1 == 2 or penhosted == 0 and rank >= 2:
                show pen happy with d
                pen "You're my host? Maybe I'll let myself have even more fun than planned~"
                $ current_customer1 = customerpen1
                $ current_customer2 = customerpen2
                $ customer = "{}".format(pen)
                $ penhosted += 1
            elif gen1 == 1:
                show mox happy with d
                mox "Oh my. Do take care of me, cutie."
                $ current_customer1 = customermox1
                $ current_customer2 = customermox2
                $ customer = "{}".format(mox)
                $ moxhosted += 1
            "What will you talk about?" 
            label randomtopicrr:
                $ gen1 = renpy.random.randint(0,49)
                $ gen2 = renpy.random.randint(0,49)
                $ gen3 = renpy.random.randint(0,49)
                $ gen4 = renpy.random.randint(0,49)
                $ topic1 = topics[gen1]
                $ topic2 = topics[gen2]
                $ topic3 = topics[gen3]
                $ topic4 = topics[gen4]
                if topic1 == topic2 or topic1 == topic3 or topic2 == topic3 or topic1 == topic4 or topic2 == topic4 or topic3 == topic4:
                    jump randomtopicrr
            menu:
                "[topic1]":
                    $ satis += current_customer1[gen1]
                "[topic2]":
                    $ satis += current_customer1[gen2]
                "[topic3]":
                    $ satis += current_customer1[gen3]
                "[topic4]" if bup3 == 1:
                    $ satis += current_customer1[gen4]
            "Now let's see how well you know your customer!"
            call randomquestion from _call_randomquestion
            scene bg brothel3 with d
            play moans1 moansmisc3
            play ambience2 sex
            "Finally, let's take her to a private booth... How are you going to please your customer?"
            label sexpositionrr:
                $ gen1 = renpy.random.randint(0,30)
                $ gen2 = renpy.random.randint(0,30)
                $ gen3 = renpy.random.randint(0,30)
                $ gen4 = renpy.random.randint(0,30)
                $ sexposition1 = sexpositions[gen1]
                $ sexposition2 = sexpositions[gen2]
                $ sexposition3 = sexpositions[gen3]
                $ sexposition4 = sexpositions[gen4]
                if sexposition1 == sexposition2 or sexposition1 == sexposition3 or sexposition2 == sexposition3 or sexposition1 == sexposition4 or sexposition2 == sexposition4 or sexposition3 == sexposition4:
                    jump sexpositionrr
            menu:
                "[sexposition1]":
                    $ satis += current_customer2[gen1]
                    $ gen5 = gen1
                    $ gent2 = "{}".format(sexposition1)
                "[sexposition2]":
                    $ satis += current_customer2[gen2]
                    $ gen5 = gen2
                    $ gent2 = "{}".format(sexposition2)
                "[sexposition3]":
                    $ satis += current_customer2[gen3]
                    $ gen5 = gen3
                    $ gent2 = "{}".format(sexposition3)
                "[sexposition4]" if bup4 == 1:
                    $ satis += current_customer2[gen4]
                    $ gen5 = gen4
                    $ gent2 = "{}".format(sexposition4)
            if current_customer1 == customerhon1:
                if current_customer2[gen5] <= 10 and gen6 != 1:
                    $ gen6 = 1
                    hon "Hold on, stud. I feel like trying something else tonight."
                    jump sexpositionrr
            if current_customer1 == customerlil1 and magicroute3 == 0:
                lil "W-Wait a second! There's no way I'm having sex here! I'm still a virgin!"
                jump bskipsex
            image bmox:
                "bmox [gen5]"
            show bmox:
                xalign 0.5 yalign 0.4 alpha 0.9 zpos -100
            show hearts1:
                alpha 0.4
                linear 1 yalign 0.55 alpha 0
                linear 1 yalign 0.45 alpha 0.4
                repeat
            show hearts2:
                alpha 0
                linear 1 yalign 0.55 alpha 0.4
                linear 1 yalign 0.45 alpha 0
                repeat
            $ textbox = 2
            with d
            "You and [customer] tried [gent2]"
            stop moans1 fadeout 2
            stop moans2 fadeout 2
            stop ambience2 fadeout 2
            hide bmox
            label bskipsex:
                $ textbox = 1
            if current_customer1 == customermox1:
                show mox laughing 
                with d
                mox "That was excellent! Thank you for your service, [mc]!"
                if spabilitytut == 0:
                    $ spabilitytut = 1
                    "(All characters have special abilities when you're hosting them, but you'll only be able to discover what they are by purchasing information from the bartender.)"
                    "(But here's a freebie! [mox]'s special ability: For you, it's impossible to not satisfy [mox]. Minimum satisfaction increased to 50.)"
                if satis < 50:
                    $ satis = 50
                mox "I'll see you back at home, alright?"
            if current_customer1 == customerpen1:
                show pen laughing 
                with d
                pen "This has been a pretty interesting experience! I'm glad you were my host."
            if current_customer1 == customerhon1:
                show hon laughing 
                with d
                hon "Y'all sure know how to show a gal a good time! Might just come back if I get the chance!"
            if current_customer1 == customerrub1:
                show rub laughing 
                with d
                rub "A delightful experience as always, darling. If you weren't here, I wouldn't have left the office at all."
                $ totalsatis += int(satis/5)
            if current_customer1 == customerlil1:
                show lil laughing 
                with d
                lil "My head is still spinning! Don't tell anyone I was here, o-okay?"
            if satis > maxsatis:
                $ satis = 100
            play sound2 item
            "(Customer Satisfaction: [satis]/[maxsatis])"
            $ gen1 = int((satis + satisbonusflat)*satisbonus/2)
            $ money += int((gen1 + tipsbonusflat)*tipsbonus)
            play sound2 shop2
            "(Earned $[gen1] in tips for your shift!)"
            $ totalsatis += satis
            if totalsatis > 50 and rank == 1:
                play sound2 item
                $ bwchars = 2
                $ rank += 1
                "(Rank Up! [pen] is now available as a customer, and two new upgrades are available!)"
            elif totalsatis > 150 and rank == 2:
                play sound2 item
                $ bwchars = 4
                $ rank += 1
                $ rankn = "Junior Host"
                "(Rank Up! You're now a Junior Host. [hon] and [rub] are now available as a customers, and a new upgrade is available!)"
            elif totalsatis > 250 and rank == 3:
                play sound2 item
                $ bwchars = 6
                $ rank += 1
                $ rankn = "Rising Host"
                "(Rank Up! You're now a Rising Host. [lil] is now available as a customer (in a later update, this rank will be replaced with two other characters) and a new upgrade is available!)"
            elif totalsatis > 400 and rank == 4:
                play sound2 item
                "(Next rank is in development!)"
            elif totalsatis > 600 and rank == 5:
                play sound2 item
                "(Next rank is in development!)"
            scene black with d
            "After a four-hour shift, I return home."
            jump newday
        "Upgrades":
            $ gen1 = rank + 1
            menu brothelworkugprades:
                "Money: $[money] \nBase Satisfaction: [basesatis] - Max Satisfaction: [maxsatis] - Bonus Tips: $[tipsbonusflat]"
                "Ice Machine for Drinks ($40): {i}+20 Starting and Max Satisfaction" if bup1 == 0 and rank >= 1:
                    if money >= 40:
                        play sound2 shop2
                        $ bup1 = 1
                        $ money -= 40
                        $ basesatis += 20
                        $ maxsatis += 20
                "Fancy Cologne ($75): {i}+$12 Tips" if bup2 == 0 and rank >= 2:
                    if money >= 75:
                        play sound2 shop2
                        $ bup2 = 1
                        $ money -= 75
                        $ tipsbonusflat += 12
                "Hosting Classes ($100): {i}+1 Choice of Conversation Topics" if bup3 == 0 and rank >= 2:
                    if money >= 100:
                        play sound2 shop2
                        $ bup3 = 1
                        $ money -= 100
                "Stronger Booze ($100): {i}+1 Choice of Sex Acts" if bup4 == 0 and rank >= 2:
                    if money >= 100:
                        play sound2 shop2
                        $ bup4 = 1
                        $ money -= 100
                "Table Service ($125): {i}+30 Starting Satisfaction" if bup5 == 0 and rank >= 3:
                    if money >= 125:
                        play sound2 shop2
                        $ bup5 = 1
                        $ money -= 125
                        $ basesatis += 30
                "Live Entertainment ($150): {i}+30 Max Satisfaction" if bup6 == 0 and rank >= 4:
                    if money >= 150:
                        play sound2 shop2
                        $ bup6 = 1
                        $ money -= 150
                        $ maxsatis += 30
                "More Upgrades Available at Rank [gen1]":
                    pass
                    #Premium Decor - Ranking increases faster
                    #Loyalty Program - Allows you to select a customer
                    #Study Politics - Allows you to reroll conversation topics once
                    #Second Cumming - Allows you to reroll sex positions once
                "Purchased Upgrades":
                    menu:
                        "Ice Machine for Drinks: {i}+20 Base and Max Satisfaction" if bup1 == 1:
                            pass
                        "Fancy Cologne: {i}+$12 Tips" if bup2 == 1:
                            pass
                        "Hosting Classes: {i}+1 Choice of Conversation Topics" if bup3 == 1:
                            pass
                        "Stronger Booze: {i}+1 Choice of Sex Acts" if bup4 == 1:
                            pass
                        "Table Service: {i}+30 Starting Satisfaction" if bup5 == 1:
                            pass
                        "Live Entertainment: {i}+30 Max Satisfaction" if bup6 == 1:
                            pass
                        "Back":
                            jump brothelworkugprades
                "Back":
                    jump brothelworkmenu
            jump brothelworkugprades
        "Bartender":
            $ misc = "Bartender"
            misc "I've been keeping a close eye on your customers. Let me know if you want any information."
            menu brothelbartender:
                "After you've hosted a girl, you can purchase information here on their preferences to improve your services the next time they visit."
                "Information on [mox] ($40)" if moxinfo == 0 and moxhosted >= 1:
                    if money >= 40:
                        play sound2 shop2
                        $ money -= 40
                        label moxinfo:
                            $ moxinfo = 1
                        "[mox]: The {i}Great and Powerful{/i} [mox] loves talking about 'Cooking', 'Cuisine', and 'Accomplishments'."
                        "The first day you met her, she could have given you a blowjob, and you ate pizza together. She sold her wagon to [rosa]. Her most sensitive body part are her nipples, she doesn't need to masturbate because you're around, and she's turned on by loving sex."
                        "Her favourite sexual acts are vanilla, romantic positions, particularly ones with eye contact, because she likes to look at you. Highlights include 'Missionary', 'Cowgirl', 'Spooning'."
                        "Finally, her special ability: She likes you so much that her satisfaction won't go lower than 50."
                    else:
                        play sound2 error
                "Information on [mox]" if moxinfo == 1:
                    jump moxinfo
                "Information on [pen] ($60)" if peninfo == 0 and penhosted >= 1:
                    if money >= 60:
                        play sound2 shop2
                        $ money -= 60
                        label peninfo:
                            $ peninfo = 1
                        "[pen]: Loves talking about 'Books', 'TV', 'Concerts', and 'Philosophy'."
                        "This girl was a morphling in your previous universe, and she studies enchantments here too. Her favourite genre of music is indie, and she can play the bass guitar. She's a kinky one, the first sex act she could perform on you here was a blowjob. She loves being choked, and consistently masturbates three times a day even outside of heat."
                        "Her favourite sex acts are rough ones, including: 'Edging', 'BSDM', 'FFM Threesome', 'Deep Throat', 'Spanking', 'Bondage', 'Giving/Receiving Pain', and 'Pet Play'. I told you she liked a lot of them."
                        "Finally, her special ability: Not only does she love a lot of sex acts, but selecting one she loves will give an additional 10 satisfaction."
                    else:
                        play sound2 error
                "Information on [pen]" if peninfo == 1:
                    jump peninfo
                "Information on [hon] ($80)" if honinfo == 0 and honhosted >= 1:
                    if money >= 80:
                        play sound2 shop2
                        $ money -= 80
                        label honinfo:
                            $ honinfo = 1
                        "[hon]: Loves talking about 'Fitness', 'Gardening', and 'DIY'."
                        "This apple farmer, in your universe, was the virtue of loyalty, when you met her, she injured her hand by punching a tree." 
                        "In this universe, she greeted you with a potential thighjob, but what would really turn her on is milking her tits and treating her like a cow."
                        "Some fun facts about her, her hat is called Talluhah, and she has a bottomless appetite for apple fritters."
                        "She has strong feelings about sex acts, and it can be hard to get a read on what she does or doesn't like. But what she does love are: 'Cowgirl', 'MMF Threesome', 'Rope' and 'Bimboification'."
                        "Finally, her special ability: If you select a sex scene that she's not interested in, she'll reset your options and make you choose again."
                    else:
                        play sound2 error
                "Information on [hon]" if honinfo == 1:
                    jump honinfo
                "Information on [rub] ($80)" if rubinfo == 0 and rubhosted >= 1:
                    if money >= 80:
                        play sound2 shop2
                        $ money -= 80
                        label rubinfo:
                            $ rubinfo = 1
                            "[rub]: Loves talking about 'Travel', 'Holidays', 'Fashion' and 'Philosophy'."
                            "This cat loving mare also secretly has a crush on dragon boys. Not that it matters, because you stole her heart and she let you have vaginal sex the first time you met, and I bet she can't wait to try some roleplay with you next time. I hope you remember her safe word, 'Opal'!"
                            "Some fun facts about [rub]: She has a glasses prescription, but always wears lenses. She was once abducted by gemstone dogs many years ago for her magic, she escaped unharmed."
                            "She's picky about sex acts, but it's fairly obvious what she does and doesn't like. In particular, she loves: 'Doggy style', 'Roleplay', 'Erotic Massage' and 'Non-Con'."
                            "Finally, her special ability: Gains to your rank goes up by +20%% after serving [rub]."
                    else:
                        play sound2 error
                "Information on [rub]" if rubinfo == 1:
                    jump rubinfo
                "Information on [lil] ($100)" if lilinfo == 0 and lilhosted >= 1:
                    if money >= 80:
                        play sound2 shop2
                        $ money -= 80
                        label lilinfo:
                            $ lilinfo = 1
                            "[lil]: Loves talking about exactly what you'd expect: 'Books', 'Education', 'Science' and 'Sci-Fi'. Other than those topics, it can be pretty hard to get through to her,"
                            "This snake and goddess fearing unicorn loves turned based strategy and energy drinks a little too much."
                            "When you first met her, you discovered that she has a pink dildo and then offered you a buttjob. Of course, what she truly wants is to be filled up with some hot, virile cum of an interspecies man."
                            "She's still shy and exploring her sex options, but anything she's already explored with you, she seems really into: 'Missionary', 'FFM Threesome', 'Sex Toys' and 'Cuckoldry'."
                            "Finally, her special ability: Selecting a conversation topic she loves will give an additional 10 satisfaction."
                    else:
                        play sound2 error
                "Information on [lil]" if lilinfo == 1:
                    jump lilinfo
                "Back":
                    jump brothelworkmenu
            jump brothelbartender
        "Back":
            jump brothelmenu

#Experienced Host 
#Senior Host
#Elite Host
#Star Host
#Premier Host
#Executive Host
#Master Host
#Legendary Host 
label randomquestion:
    if current_customer1 == customermox1:
        $ gen1 = renpy.random.randint(1,7)
        if gen1 == 1:
            menu:
                "What is [mox]'s signature catchphrase?"
                "All Powerful and Great!":
                    pass
                "The Great and Powerful [mox]!":
                    $ satis += 35
                "Magic is Mine to Command!":
                    pass
                "I'm gonna Mox!":
                    pass
        elif gen1 == 2:
            menu:
                "What was the first sexual act you could engage in with this [mox]?"
                "Blowjob":
                    $ satis += 35
                "Sixty-Nine":
                    pass
                "Missionary":
                    pass
                "Facesitting":
                    pass
        elif gen1 == 3:
            menu:
                "What food did you eat together during your first day out?"
                "Pasta":
                    pass
                "Ice Cream":
                    pass
                "Pizza":
                    $ satis += 35
                "Hay Burgers":
                    pass
        elif gen1 == 4:
            menu:
                "Who is the current owner of [mox]'s wagon?"
                "[pen]":
                    pass
                "[mox]":
                    pass
                "[chl]":
                    pass
                "[rosa]":
                    $ satis += 35
        elif gen1 == 5:
            menu:
                "Other than her pussy and clit, what is [mox]'s most sensitive body part?"
                "Breasts":
                    pass
                "Nipples":
                    $ satis += 35
                "Tongue":
                    pass
                "Ass":
                    pass
        elif gen1 == 6:
            menu:
                "How often does [mox] masturbate?"
                "Once a Week":
                    pass
                "Once a Day":
                    pass
                "3 Times a Day":
                    pass
                "Never when I'm around 8)":
                    $ satis += 35
        elif gen1 == 7:
            menu:
                "Out of the following, which would turn [mox] on the most?"
                "Vanilla Loving Sex":
                    $ satis += 35
                "Rough Fucking":
                    pass
                "Magical Experimentation Sex":
                    pass
                "Anal Sex":
                    pass
    if current_customer1 == customerpen1:
        $ gen1 = renpy.random.randint(1,7)
        if gen1 == 1:
            menu:
                "What was [pen]'s species in the other universe?"
                "Unicorn":
                    pass
                "Bug":
                    pass
                "Morphling":
                    $ satis += 35
                "Baneling":
                    pass
        elif gen1 == 2:
            menu:
                "What was the first sexual act you could engage in with [pen]?"
                "Cowgirl":
                    pass
                "Paizuri":
                    pass
                "Tied-Up":
                    pass
                "Blowjob":
                    $ satis += 35
        elif gen1 == 3:
            menu:
                "What is [pen] studying?"
                "Magic":
                    pass
                "Infusion":
                    pass
                "Enchantments":
                    $ satis += 35
                "Imbuements":
                    pass
        elif gen1 == 4:
            menu:
                "Which instrument can [pen] play?"
                "Drums":
                    pass
                "Harmonica":
                    pass
                "Bass":
                    $ satis += 35
                "None":
                    pass
        elif gen1 == 5:
            menu:
                "What of the following would turn [pen] on the most?"
                "Taking a Bath Together":
                    pass
                "Being Choked":
                    $ satis += 35
                "Kissing":
                    pass
                "Romantic Gestures":
                    pass
        elif gen1 == 6:
            menu:
                "How often does [pen] masturbate?"
                "Once a Day":
                    pass
                "Twice a Day":
                    pass
                "Thrice a Day":
                    $ satis += 35
                "Quice a Day?":
                    pass
        elif gen1 == 7:
            menu:
                "What is [pen]'s favourite genre of music?"
                "Metal":
                    pass
                "Pop":
                    pass
                "EDM":
                    pass
                "Indie":
                    $ satis += 35
    if current_customer1 == customerhon1:
        $ gen1 = renpy.random.randint(1,7)
        if gen1 == 1:
            menu:
                "What produce is [hon] most famous for producing?"
                "Wheat":
                    pass
                "Ass Kicking":
                    pass
                "Apples":
                    $ satis += 35
                "Potatoes":
                    pass
        elif gen1 == 2:
            menu:
                "What was the first sexual act you could engage in with [hon]?"
                "Cowgirl":
                    pass
                "Paizuri":
                    pass
                "Buttjob":
                    pass
                "Thighjob":
                    $ satis += 35
        elif gen1 == 3:
            menu:
                "What Virtue is [hon] within the Virtues of Concord?"
                "Compassion":
                    pass
                "Pride":
                    pass
                "Loyalty":
                    $ satis += 35
                "Bravery":
                    pass
        elif gen1 == 4:
            menu:
                "How did [hon] break her hand in your original universe?"
                "Punching a Tree":
                    $ satis += 35
                "Equipment Injury":
                    pass
                "Wolf Attack":
                    pass
                "Excessive Masturbation":
                    pass
        elif gen1 == 5:
            menu:
                "What of the following would turn [hon] on the most?"
                "Cowgirl Position":
                    pass
                "Milking her Tits":
                    $ satis += 35
                "Spanking her Butt":
                    pass
                "Exhibitionism":
                    pass
        elif gen1 == 6:
            menu:
                "What is the name of [hon]'s hat?"
                "Talia":
                    pass
                "Dalilah":
                    pass
                "Talluhah":
                    $ satis += 35
                "Wut? She named it?":
                    pass
        elif gen1 == 7:
            menu:
                "Which of the following is one [hon]'s absolute favourite food?"
                "Oranges":
                    pass
                "Caramel Apples":
                    pass
                "Apple Pie":
                    pass
                "Apple Fritters":
                    $ satis += 35
    if current_customer1 == customerrub1:
        $ gen1 = renpy.random.randint(1,7)
        if gen1 == 1:
            menu:
                "Which of the following is a true fun fact about [rub]?"
                "Can Perform a Standing Flip":
                    pass
                "Once Won a Hotdog Eating Contest":
                    pass
                "Has a Glasses Prescription":
                    $ satis += 35
                "Was Once a Ballerina":
                    pass
        elif gen1 == 2:
            menu:
                "What was the first sexual act you could engage in with [rub]?"
                "Anal Sex":
                    pass
                "Intercural Sex":
                    pass
                "Oral Sex":
                    pass
                "Vaginal Sex":
                    $ satis += 35
        elif gen1 == 3:
            menu:
                "Which animal does [rub] like the most?"
                "Snakes":
                    pass
                "Pandas":
                    pass
                "Cats":
                    $ satis += 35
                "Dogs":
                    pass
        elif gen1 == 4:
            menu:
                "What species does [rub] secretly have a crush on?"
                "Dragons":
                    $ satis += 35
                "Cat Boys":
                    pass
                "Wolf Men":
                    pass
                "Minotaurs":
                    pass
        elif gen1 == 5:
            menu:
                "What of the following would turn [rub] on the most?"
                "Outdoor Sex":
                    pass
                "Nurse Roleplay":
                    $ satis += 35
                "Receving Pain":
                    pass
                "Anal Sex":
                    pass
        elif gen1 == 6:
            menu:
                "What is [rub]'s safe word?"
                "Tangerine":
                    pass
                "Watermelon":
                    pass
                "Opal":
                    $ satis += 35
                "Diamond":
                    pass
        elif gen1 == 7:
            menu:
                "[rub] was once abducted by...?"
                "It was [but]":
                    pass
                "Slime Girls":
                    pass
                "Mining Minotaurs":
                    pass
                "Gemstone Dogs":
                    $ satis += 35
    if current_customer1 == customerlil1:
        $ gen1 = renpy.random.randint(1,7)
        if gen1 == 1:
            menu:
                "What specific phobia does [lil] have?"
                "Fear of Spiders":
                    pass
                "Fear of Dogs":
                    pass
                "Fear of Snakes":
                    $ satis += 35
                "Fear of Bears":
                    pass
        elif gen1 == 2:
            menu:
                "What was the first sexual act you could engage in with [lil]?"
                "Blowjob":
                    pass
                "Handjob":
                    pass
                "Intense Eye Contact":
                    pass
                "Buttjob":
                    $ satis += 35
        elif gen1 == 3:
            menu:
                "Where did [lil] get her bow from?"
                "[mc]":
                    pass
                "[pen]":
                    pass
                "Her Mother":
                    $ satis += 35
                "The Queen":
                    pass
        elif gen1 == 4:
            menu:
                "What genre of video games is [lil]'s favourite?"
                "Turn-Based Strategy":
                    $ satis += 35
                "First Person Shooters":
                    pass
                "Multiplayer Battle Arenas":
                    pass
                "Rougelikes":
                    pass
        elif gen1 == 5:
            menu:
                "What of the following would turn [lil] on the most?"
                "Getting cucked a clone":
                    pass
                "Getting filled with fertile, interspecies cum":
                    $ satis += 35
                "Experimenting with magic":
                    pass
                "Secretly getting corrupted":
                    pass
        elif gen1 == 6:
            menu:
                "What colour is [lil]'s dildo?"
                "Blue":
                    pass
                "Purple":
                    pass
                "Pink":
                    $ satis += 35
                "Black":
                    pass
        elif gen1 == 7:
            menu:
                "As unhealthy as it might be, what is [lil] addicted to?"
                "Chocolate":
                    pass
                "Alcohol":
                    pass
                "Dr. Bebba":
                    pass
                "Munster Cok Energy Drinks":
                    $ satis += 35
    return

init:
    $ topics = ["Travel", "Hobbies", "Books", 
    "Childhood", "TV", "Holidays", 
    "Bucket List", "Recent News", "Cooking", 
    "Personal Milestones", "Music", "Pets", 
    "Fitness", "Technology", "Fashion", 
    "Self-Improvement", "Outdoor Activities", "Concerts", 
    "Social Media", "Volunteer Work", "Dream Jobs", 
    "Cuisine", "History", "Trivia", 
    "Future Predictions", "Gardening", "Weekend Activities", 
    "Role Models", "Different Cultures", "Video Games", 
    "Art", "Travel Tips", "Philosophy", 
    "Funniest Moments", "Podcasts/Radio", "Talents", 
    "Accomplishments", "Memorable Experiences", "Future Plans", 
    "Education", "Nature", "DIY", 
    "Local Events", "Ghosts", "Comedy", 
    "Life Lessons", "Favorite Quotes", "Science", 
    "Sci-Fi", "Motivation"]
    $ sexpositions = ['Missionary', 'Doggy style', 'Cowgirl', 
    'Spooning', 'Standing', '69', 
    'Oral Sex', 'Anal Sex', 'Edging', 
    'BDSM', 'Roleplay', 'FFM Threesome', 
    'MMF Threesome', 'Deep Throat', 'Erotic Massage', 
    'Sex Toys', 'Spanking', 'Exhibitionism', 
    'Voyeurism', 'Group Sex', 'Foot Fetish', 
    'Rope', 'Pegging', 'Giving/Receiving Pain', 
    'Shower Sex', 'Triple Penetration', 'Femdom', 
    'Bimboification', 'Pet Play', 'Cuckoldry', 
    'Non-Con']
    $ moxhosted = 0
    $ customermox1 = [10, 10, 10, 10, 15, 25, 20, 5, 35, 25, 20, 15, 20, 5, 10, 20, 5, 20, 15, 5, 25, 35, 5, 10, 5, 5, 10, 20, 25, 10, 10, 15, 5, 15, 15, 25, 35, 20, 25, 20, 15, 10, 15, 20, 20, 25, 10, 5, 10, 20]
    $ customermox2 = [35, 25, 35, 35, 15, 15, 20, 10, 10, 10, 10, 30, 10, 10, 30, 25, 20, 10, 10, 30, 10, 10, 10, 10, 15, 10, 10, 10, 10, 10, 10]
    $ penhosted = 0
    $ customerpen1 = [5, 15, 35, 30, 35, 10, 25, 25, 5, 10, 30, 0, 5, 15, 10, 15, 10, 35, 25, 25, 15, 10, 10, 30, 30, 25, 20, 10, 10, 30, 5, 10, 35, 10, 10, 10, 15, 15, 20, 30, 10, 20, 15, 20, 10, 20, 10, 30, 25, 15]
    $ customerpen2 = [10, 25, 30, 10, 30, 15, 15, 20, 45, 45, 25, 45, 20, 45, 5, 30, 45, 5, 5, 20, 5, 45, 10, 45, 5, 25, 0, 5, 45, 0, 30]
    $ honhosted = 0
    $ customerhon1 = [5, 10, 0, 25, 15, 20, 25, 5, 30, 30, 15, 35, 35, 0, 5, 15, 30, 10, 0, 30, 20, 30, 20, 5, 5, 35, 5, 25, 30, 0, 5, 20, 5, 10, 25, 15, 10, 30, 20, 10, 20, 35, 30, 25, 10, 30, 20, 0, 5, 20]
    $ customerhon2 = [5, 15, 35, 15, 30, 5, 5, 25, 10, 10, 5, 25, 35, 5, 15,  0, 10, 10, 10, 25, 5, 35, 30, 20, 30, 25, 20, 35, 30, 5, 0]
    $ rubhosted = 0
    $ customerrub1 = [35, 10, 20, 5, 10, 35, 10, 25, 20, 30, 25, 30, 10, 15, 35, 10, 0, 10, 20, 10, 20, 15, 10, 5, 10, 15, 10, 0, 5, 5, 25, 30, 35, 5, 5, 15, 20, 15, 25, 15, 10, 5, 30, 25, 10, 15, 5, 10, 5, 10]
    $ customerrub2 = [30, 35, 5, 20, 10, 5, 20, 20, 25, 30, 35, 5, 0, 30, 35, 25, 25, 5, 5, 0, 5, 20, 0, 30, 25, 5, 0, 20, 25, 10, 35]
    $ lilhosted = 0
    $ customerlil1 = [0, 10, 45, 25, 5, 0, 20, 20, 5, 20, 20, 5, 0, 30, 0, 15, 5, 5, 15, 0, 30, 10, 30, 25, 25, 15, 10, 30, 15, 30, 10, 0, 30, 10, 15, 20, 25, 10, 20, 45, 5, 0, 0, 25, 10, 15, 10, 45, 45, 20]
    $ customerlil2 = [35, 25, 15, 35, 30, 15, 15, 10, 15, 10, 5, 35, 10, 50, 10, 35, 30, 30, 30, 10, 15, 10, 10, 10, 20, 5, 0, 15, 15, 35, 0]

    $ customer = ""
    $ current_customer1 = [customermox1, customerpen1]
    $ current_customer2 = [customermox2, customerpen2]

    $ basesatis = 0
    $ satis = 0
    $ maxsatis = 100

    $ satisbonus = 1
    $ satisbonusflat = 0
    $ tipsbonus = 1
    $ tipsbonusflat = 0

    $ totalsatis = 0

    $ rank = 1
    $ rankn = "Rookie Host"
    $ bwchars = 1

    $ bup1 = 0
    $ bup2 = 0
    $ bup3 = 0
    $ bup4 = 0
    $ bup5 = 0
    $ bup6 = 0
    $ bup7 = 0

    $ moxinfo = 0
    $ peninfo = 0
    $ honinfo = 0
    $ rubinfo = 0
    $ lilinfo = 0

    $ spabilitytut = 0
    $ brothelimages = "On"
    $ brothelimagestut = 0