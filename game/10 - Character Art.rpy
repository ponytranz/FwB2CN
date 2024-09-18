﻿## CHARACTER ART:
init:
    $ moxb = 1
    $ penb = 1
    $ lilb = 1
    $ rubb = 1
    $ honb = 1
    
    #sisters
    $ melb = 1
    $ blob = 1 #haha blob

    #currently unusused
    $ creb = 1
    $ rikb = 1
    $ butb = 1 #butt b

    #royalty
    $ aurb = 1
    $ selb = 1

    $ moxblush = 0
    $ penblush = 0
    $ lilblush = 0
    $ rubblush = 0
    $ honblush = 0
    $ melblush = 0
    $ blobblush = 0


    $ lilcoat = 0
    $ lilglasses = 0

layeredimage mox:
    always:
        "moxieb[moxb].png"
    group blush:
        attribute blush:
            "moxieblush.png"
    group face:
        attribute angry:
            "moxiee angry.png"
        attribute awkward:
            "moxiee awkward.png"
        attribute bashful:
            "moxiee bashful.png"
        attribute happy:
            "moxiee happy.png"
        attribute horny:
            "moxiee horny.png"
        attribute laughing:
            "moxiee laughing.png"
        attribute neutral:
            "moxiee neutral.png"
        attribute sad:
            "moxiee sad.png"
        attribute satisfied:
            "moxiee satisfied.png"
        attribute smug:
            "moxiee smug.png"
        attribute surprised:
            "moxiee surprised.png"
        attribute wink:
            "moxiee wink.png"
    group clothing:
        attribute lingerie:
            "moxielingerie"

layeredimage pen:
    always:
        "penelopeb[penb].png"
    group collar:
        attribute collar:
            "penelopecollar.png"
    group cum:
        attribute cum:
            "penelopecum.png"
    group blush:
        attribute blush:
            "penelopeblush.png"
    group face:
        attribute angry:
            "penelopee angry[penb].png"
        attribute awkward:
            "penelopee awkward[penb].png"
        attribute bashful:
            "penelopee bashful[penb].png"
        attribute happy:
            "penelopee happy[penb].png"
        attribute horny:
            "penelopee horny[penb].png"
        attribute laughing:
            "penelopee laughing[penb].png"
        attribute neutral:
            "penelopee neutral[penb].png"
        attribute raised:
            "penelopee raised[penb].png"
        attribute sad:
            "penelopee sad[penb].png"
        attribute surprised:
            "penelopee surprised[penb].png"
        attribute wink:
            "penelopee wink[penb].png"

layeredimage lil:
    always:
        "lilyb[lilb].png"
    if lilb >= 0:
        "lilybow [lilb]"
    group blush:
        attribute blush:
            "lilyblush.png"
    group glasses:
        attribute glasses:
            "lilyglasses"
    group coat:
        attribute coat:
            "lilylabcoat"
    group face:
        attribute angry:
            "lilye angry[lilb].png"
        attribute awkward:
            "lilye awkward[lilb].png"
        attribute bashful:
            "lilye bashful[lilb].png"
        attribute happy:
            "lilye happy[lilb].png"
        attribute horny:
            "lilye horny[lilb].png"
        attribute laughing:
            "lilye laughing[lilb].png"
        attribute neutral:
            "lilye neutral[lilb].png"
        attribute sad:
            "lilye sad[lilb].png"
        attribute satisfied:
            "lilye satisfied[lilb].png"
        attribute smug:
            "lilye smug[lilb].png"
        attribute shocked:
            "lilye shocked[lilb].png"
        attribute raised:
            "lilye raised[lilb].png"
        attribute wink:
            "lilye wink[lilb].png"

layeredimage lil2:
    always:
        "lilyaura.png" 
    always:
        "lilyb[lilb].png" 
    group blush:
        attribute blush:
            "lilyblush.png" 
    group glasses:
        attribute glasses:
            "lilyglasses" 
    group coat:
        attribute coat:
            "lilylabcoat" 
    group cum:
        attribute cum:
            "lilycum" 
    group face:
        attribute angry:
            "lilye angry1.png" 
        attribute awkward:
            "lilye awkward1.png" 
        attribute bashful:
            "lilye bashful1.png" 
        attribute happy:
            "lilye happy1.png" 
        attribute horny:
            "lilye horny1.png" 
        attribute laughing:
            "lilye laughing1.png" 
        attribute neutral:
            "lilye neutral1.png" 
        attribute sad:
            "lilye sad1.png" 
        attribute satisfied:
            "lilye satisfied1.png" 
        attribute smug:
            "lilye smug1.png" 
        attribute shocked:
            "lilye shocked1.png" 
        attribute raised:
            "lilye raised1.png" 
        attribute wink:
            "lilye wink1.png" 

layeredimage rub:
    always:
        "rubyb[rubb].png"
    group blush:
        attribute blush:
            "rubyblush.png"
    group cum:
        attribute cum:
            "rubycum"
    group lingerie:
        attribute lingerie:
            "rubylingerie"
        attribute lingerie2:
            "rubylingerie2"
    group dress:
        attribute dress1:
            "rubydress [rubb].png"
        attribute dress2:
            "rubydress2 [rubb].png"
    group face:
        attribute angry:
            "rubye angry[rubb].png"
        attribute awkward:
            "rubye awkward[rubb].png"
        attribute bashful:
            "rubye bashful[rubb].png"
        attribute happy:
            "rubye happy[rubb].png"
        attribute horny:
            "rubye horny[rubb].png"
        attribute laughing:
            "rubye laughing[rubb].png"
        attribute neutral:
            "rubye neutral[rubb].png"
        attribute sad:
            "rubye sad[rubb].png"
        attribute wink:
            "rubye wink[rubb].png"


layeredimage hon:
    always:
        "honeycrispb[honb].png"
    group blush:
        attribute blush:
            "honeycrispblush.png"
    group face:
        attribute angry:
            "honeycrispe angry.png"
        attribute happy:
            "honeycrispe happy.png"
        attribute horny:
            "honeycrispe horny.png"
        attribute laughing:
            "honeycrispe laughing.png"
        attribute neutral:
            "honeycrispe neutral.png"
        attribute satisfied:
            "honeycrispe satisfied.png"
        attribute wink:
            "honeycrispe wink.png"    

layeredimage mel:
    always:
        "melodyb[melb].png"
    group blush:
        attribute blush:
            "melodyblush.png"
    group goth:
        attribute goth:
            "melodygoth.png"
    group face:
        attribute angry:
            "melodye angry[melb].png"
        attribute bashful:
            "melodye bashful[melb].png"
        attribute happy:
            "melodye happy[melb].png"
        attribute laughing:
            "melodye laughing[melb].png"
        attribute neutral:
            "melodye neutral[melb].png"
        attribute sad:
            "melodye sad[melb].png"
        attribute smug:
            "melodye smug[melb].png"
        attribute death:
            "melodye death[melb].png"
        attribute wink:
            "melodye wink[melb].png"

layeredimage blo:
    always:
        "blossomb [blob].png"
    group blush:
        attribute blush:
            "blossomblush"
    group cum:
        attribute cum:
            "blossomcum"
    group face:
        attribute angry:
            "blossome angry[blob].png"
        attribute awkward:
            "blossome awkward[blob].png"
        attribute bashful:
            "blossome bashful[blob].png"
        attribute happy:
            "blossome happy[blob].png"
        attribute horny:
            "blossome horny[blob].png"
        attribute laughing:
            "blossome laughing[blob].png"
        attribute neutral:
            "blossome neutral[blob].png"
        attribute satisfied:
            "blossome satisfied[blob].png"


layeredimage ros:
    always:
        "rosab"
    group face:
        attribute happy:
            "rosae happy"
        attribute horny:
            "rosae horny"
        attribute laughing:
            "rosae laughing"
        attribute neutral:
            "rosae neutral"
        