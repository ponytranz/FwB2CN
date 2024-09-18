label brothelwork:
    menu brothelworkmenu:
        "Current Rank: [rank], [rankn]."
        "Start Work":
            $ satis = basesatis
            "Today's customer is..."
            $ gen1 = renpy.random.randint(1,rank)
            if gen1 == 2 or penhosted == 0 and rank >= 2:
                show pen happy with d
                pen "You're my host? Maybe I'll let myself have even more fun than planned~"
                $ current_customer1 = customerpen1
                $ current_customer2 = customerpen2
                $ penhosted += 1
            elif gen1 == 1:
                show mox happy with d
                mox "Oh my. Do take care of me, cutie."
                $ current_customer1 = customermox1
                $ current_customer2 = customermox2
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
                "[sexposition2]":
                    $ satis += current_customer2[gen2]
                "[sexposition3]":
                    $ satis += current_customer2[gen3]
                "[sexposition4]" if bup4 == 1:
                    $ satis += current_customer2[gen4]
            stop moans1 fadeout 2
            stop ambience2 fadeout 2
            if current_customer1 == customermox1:
                show mox laughing with d
                mox "That was excellent! Thank you for your service, [mc]!"
                if spabilitytut == 0:
                    $ spabilitytut = 1
                    "(All characters have special abilities when you're hosting them, but you'll only be able to discover what they are by purchasing information from the bartender.)"
                    "(But here's a freebie! [mox]'s special ability: For you, it's impossible to not satisfy [mox]. Minimum satisfaction increased to 50.)"
                if satis < 50:
                    $ satis = 50
                if satis > maxsatis:
                    $ satis = 100
                mox "I'll see you back at home, alright?"
            if current_customer1 == customerpen1:
                show pen laughing with d
                pen "This has been a pretty interesting experience! I'm glad you were my host."
            play sound2 item
            "(Customer Satisfaction: [satis]/[maxsatis])"
            $ gen1 = int((satis + satisbonusflat)*satisbonus/2)
            $ money += int((gen1 + tipsbonusflat)*tipsbonus)
            play sound2 shop2
            "(Earned $[gen1] in tips for your shift!)"
            $ totalsatis += satis
            if totalsatis > 50 and rank == 1:
                play sound2 item
                $ rank += 1
                "(You've gained a rank! New customer and upgrades unlocked!)"
            elif totalsatis > 150 and rank == 2:
                "(The next rank is currently in development!)"
            scene black with d
            "After a four-hour shift, I return home."
            jump newday
        "Upgrades":
            $ gen1 = rank + 1
            menu brothelworkugprades:
                "Money: $[money]. Base Satisfaction: [basesatis]. Max Satisfaction: [maxsatis]"
                "Ice Machine for Drinks - $40 - +20%% Satisfaction" if bup1 == 0 and rank >= 1:
                    if money >= 40:
                        $ bup1 = 1
                        $ money -= 40
                        $ basesatis += 20
                        $ maxsatis += 20
                "Ice Machine for Drinks {i}(Purchased){/i} - +20%% Satisfaction" if bup1 == 1:
                    pass
                "Fancy Cologne - $75 - +$12 Tips" if bup2 == 0 and rank >= 2:
                    if money >= 75:
                        $ bup2 = 1
                        $ money -= 75
                        $ tipsbonusflat += 12
                "Fancy Cologne {i}(Purchased){/i} - +$12 Tips" if bup2 == 1:
                    pass
                "Hosting Classes - $100 - Gain +1 Choice of Conversation Topics" if bup3 == 0 and rank >= 2:
                    if money >= 100:
                        $ bup3 = 1
                        $ money -= 100
                "Hosting Classes {i}(Purchased){/i} - Gain +1 Choice of Conversation Topics" if bup3 == 1:
                    pass
                "Stronger Booze - $100 - Gain +1 Choice of Sex Acts" if bup4 == 0 and rank >= 2:
                    if money >= 100:
                        $ bup4 = 1
                        $ money -= 100
                "Stronger Booze {i}(Purchased){/i} - Gain +1 Choice of Sex Acts" if bup4 == 1:
                    pass
                "More Upgrades Available at Rank [gen1]":
                    pass
                    #Table Service 
                    #Live Entertainment
                    #Premium Decor
                    #Loyalty Program
                    #VIP Lounge
                "Back":
                    jump brothelworkmenu
            jump brothelworkugprades
        "Bartender":
            $ misc = "Bartender"
            misc "I've been keeping a close eye on your customers. Let me know if you want any information."
            menu brothelbartender:
                "After you've hosted them, here you can purchase information on customer preferences to improve your services the next time they visit."
                "Information on [mox] (50 G)" if moxinfo == 0 and moxhosted >= 1:
                    label moxinfo:
                        $ moxinfo = 1
                    "[mox]: The {i}Great and Powerful{/i} [mox] loves talking about 'Cooking', 'Cuisine', and 'Accomplishments'."
                    "The first day you met her, she could have given you a blowjob, and you ate pizza together. She sold her wagon to [rosa]. Her most sensitive body part are her nipples, she doesn't need to masturbate because you're around, and she's turned on by loving sex."
                    "Her favourite sexual acts are vanilla, romantic positions, particularly ones with eye contact, because she likes to look at you. Highlights include 'Missionary', 'Cowgirl', 'Spooning'."
                    "Finally, her special ability: She likes you so much that her satisfaction won't go lower than 50."
                "Information on [mox]" if moxinfo == 1:
                    jump moxinfo
                "Information on [pen] (75 G)" if peninfo == 0 and penhosted >= 1:
                    label peninfo:
                        $ peninfo = 1
                    "[pen]: Loves talking about 'Books', 'TV', 'Concerts', and 'Philosophy'."
                    "This girl was a morphling in your previous universe, and she studies enchantments here too. Her favourite genre of music is indie, and she can play the bass guitar. She's a kinky one, the first sex act she could perform on you here was a blowjob. She loves being choked, and consistently masturbates three times a day even outside of heat."
                    "Her favourite sex acts are rough ones, including: 'Edging', 'BSDM', 'FFM Threesome', 'Deep Throat', 'Spanking', 'Bondage', 'Giving/Receiving Pain', and 'Pet Play'. I told you she liked a lot of them."
                    "Finally, her special ability: Not only does she love a lot of sex acts, but selecting one she loves will give an additional 10 satisfaction."
                "Information on [pen]" if peninfo == 1:
                    jump peninfo
                "Back":
                    jump brothelworkmenu
            jump brothelbartender
        "Back":
            jump brothelmenu

#
#Base:
#Earnings: $50
#
#Upgrade 1: +20% for $40
#Max Earnings $60 (+$10 bonus, takes x4 to profit)
#
#Upgrade 2: +25% for $75
#Max Earnings: $75 ($15 bonus, takes 5x to profit)
#
#Upgrade 3: 
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
    'Voyerism', 'Group Sex', 'Foot Fetish', 
    'Bondage', 'Pegging', 'Giving/Receiving Pain', 
    'Shower Sex', 'Fisting', 'Femdom', 
    'Bimboification', 'Pet Play', 'Cuckoldry', 
    'Non-Con']
    $ moxhosted = 0
    $ customermox1 = [10, 10, 10, 10, 15, 25, 20, 5, 35, 25, 20, 15, 20, 5, 10, 20, 5, 20, 15, 5, 25, 35, 5, 10, 5, 5, 10, 20, 25, 10, 10, 15, 5, 15, 15, 25, 35, 20, 25, 20, 15, 10, 15, 20, 20, 25, 10, 5, 10, 20]
    $ customermox2 = [35, 25, 35, 35, 15, 15, 20, 10, 5, 5, 5, 30, 0, 10, 30, 25, 20, 10, 5, 30, 5, 10, 0, 5, 15, 0, 5, 5, 5, 0, 0]
    $ penhosted = 0
    $ customerpen1 = [5, 15, 35, 30, 35, 10, 25, 25, 5, 10, 30, 0, 5, 15, 10, 15, 10, 35, 25, 25, 15, 10, 10, 30, 30, 25, 20, 10, 10, 30, 5, 10, 35, 10, 10, 10, 15, 15, 20, 30, 10, 20, 15, 20, 10, 20, 10, 30, 25, 15]
    $ customerpen2 = [10, 25, 30, 10, 30, 15, 15, 20, 45, 45, 25, 45, 20, 45, 5, 30, 45, 5, 5, 20, 5, 45, 10, 45, 5, 25, 0, 5, 45, 0, 30]

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

    $ bup1 = 0
    $ bup2 = 0
    $ bup3 = 0
    $ bup4 = 0

    $ moxinfo = 0
    $ peninfo = 0

    $ spabilitytut = 0