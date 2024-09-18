init python:
    from functools import partial # import the python function
    def beep(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

init 200:
    #Characters
    define gui.dialogue_text_outlines = [ (3, "#00000080", 2, 2) ]
    define gui.characters_text_outlines = [ (3, "#00000080", 2, 2) ]
    define gui.name_text_outlines = [ (3, "#00000080", 2, 2) ]
    define gui.menu_text_outlines = [ (3, "#00000080", 2, 2) ]
    style outlines:
        outlines [(2, "#00000080", 2, 2)]
    define narrator = Character("", what_color="#ffffff")
    define unk = Character("???", color="#ffffff", what_color="#ffffff", callback=beep)
    define mc = Character(_("[mcname]"), color="#ffffff", what_color="#ffffff", callback=beep)
    $ mcname = "Anon"
    define mox = Character(_("[moxie]"), color="#0077ff", what_color="#ffffff", callback=beep)
    $ moxie = "Moxie"
    define pen = Character(_("[penelope]"), color="#d457f3", what_color="#ffffff", callback=beep)
    $ penelope = "Penelope"
    define lil = Character(_("[lily]"), color="#ea95ff", what_color="#ffffff", callback=beep)
    $ lily = "Lily"
    define hon = Character(_("[honeycrisp]"), color="#ecca2f", what_color="#ffffff", callback=beep)
    $ honeycrisp = "Honeycrisp"
    define blo = Character(_("[blossom]"), color="#ec842f", what_color="#ffffff", callback=beep)
    $ blossom = "Blossom"
    define rub = Character(_("[ruby]"), color="#f89999", what_color="#ffffff", callback=beep)
    $ ruby = "Ruby"
    define mel = Character(_("[melody]"), color="#ffd7f8", what_color="#ffffff", callback=beep)
    $ melody = "Melody"
    define cre = Character(_("[cream]"), color="#fcf9cc", what_color="#ffffff", callback=beep)
    $ cream = "Cream"
    define bla = Character(_("[blackcurrant]"), color="#ba63ec", what_color="#ffffff", callback=beep)
    $ blackcurrant = "Blackcurrant"
    define rik = Character(_("[riku]"), color="#d14343", what_color="#ffffff", callback=beep)
    $ riku = "Riku"
    define but = Character(_("[butters]"), color="#d6b548", what_color="#ffffff", callback=beep)
    $ butters = "Butters"
    define aur = Character(_("[aurora]"), color="#e28bc5", what_color="#ffffff", callback=beep)
    $ aurora = "Aurora"
    define sel = Character(_("[selene]"), color="#423491", what_color="#ffffff", callback=beep)
    $ selene = "Selene"
    define mid = Character(_("[midnight]"), color="#1b1242", what_color="#ffffff", callback=beep)
    $ midnight = "Midnight"
    define misc = Character(_("[misc]"), color="#1b1242", what_color="#ffffff", callback=beep)
    $ misc = "???"
    define ros = Character(_("[rosa]"), color="#a1731f", what_color="#ffffff", callback=beep)
    $ rosa = "Rosa"
    define chl = Character(_("[chloe]"), color="#a1731f", what_color="#ffffff", callback=beep)
    $ chloe = "Chloe"
    define hil = Character(_("[hilda]"), color="#a1731f", what_color="#ffffff", callback=beep)
    $ hilda = "Hilda"
    define bas = Character(_("[bastet]"), color="#a1731f", what_color="#ffffff", callback=beep)
    $ bastet = "Bastet"
    define lil2 = Character(_("[lil2]"), color="#ea95ff", what_color="#ffffff", callback=beep)
    $ lil2 = "{} 2.0".format(lil)

    #BGM
    define blossomtheme = "audio/music/Blossom's Theme - Discovery - Purrple Cat.ogg"
    define casual1 = "audio/music/Casual 1 - Peritune - Quiet Ocean.ogg"
    define casual2 = "audio/music/Casual 2 - Peritune - Firmament Calm.ogg"
    define citytheme = "audio/music/City - Peritune - Sparkle.ogg"
    define clubtheme = "audio/music/Club - Mindvacy - delirium dreams.ogg"
    define comical = "audio/music/Comical - Purgatory Garden - Larry.ogg"
    define honeycrisptheme = "audio/music/Honeycrisp's Theme - Purrple Cat - Meterorites.ogg"
    define intro = "audio/music/mindvacy - microcosm.ogg"
    define lilytheme = "audio/music/Lily's Theme - Purrple Cat - Aether.ogg"
    define melodytheme = "audio/music/Melody's Theme - Sewerslvt - lorncloudshit.ogg"
    define moxietheme = "audio/music/Moxie's Theme - Artificial Music - Abstract Foilage.ogg"
    define penelopetheme = "audio/music/Penelope's Theme - Purrple Cat - Going With the Flow.ogg"
    define rainytheme = "audio/music/Rainy Day - Purrple Cat - Cold & Rainy.ogg"
    define rubytheme = "audio/music/Ruby's Theme - Sewerslvt - Toe Wizard.ogg"
    define sad = "audio/music/sewerslvt - hopelessness.ogg"
    define sextheme = "audio/music/Sex - Purrple Cat - Glowing Tides.ogg"
    define melodysextheme = "audio/music/Melody Sex Theme - Sewerslvt - Yandere Complex.ogg"

    #SFX
    define audio.click = "audio/Click1.ogg"
    define audio.cum = "audio/cum.ogg"
    define audio.move = "audio/move1.ogg"
    define audio.move2 = "audio/move2.ogg"
    define audio.doorbell = "audio/doorbell.ogg"
    define audio.impact1 = "audio/impact1.ogg"
    define audio.impact2 = "audio/impact2.ogg"
    define audio.item = "audio/item.ogg"
    define audio.attack1 = "audio/sword1.ogg"
    define audio.attack2 = "audio/sword2.ogg"
    define audio.attack3 = "audio/sword3.ogg"
    define audio.staticlong = "audio/staticlong.ogg"
    define audio.staticsequence = "audio/staticsequence.ogg"
    define audio.staticshort1 = "audio/staticshort1.ogg"
    define audio.staticshort2 = "audio/staticshort2.ogg"
    define audio.earthquake = "audio/earthquake.ogg"
    define audio.spank = "audio/spank.ogg"
    define audio.shop2 = "audio/shop2.mp3"
    define audio.thunder = "audio/thunder.ogg"
    define audio.phonestart = "audio/phonestart.ogg"
    define audio.phonenotification = "audio/phonenotification.ogg"
    define audio.notification = "audio/phonenotification.ogg"
    define audio.error = "audio/error.ogg"
    define audio.rip = "audio/rip.ogg"

    #BGS
    define audio.moansmisc1 = "audio/moansmisc1.ogg"
    define audio.moansmisc2 = "audio/moansmisc2.ogg"
    define audio.moansmisc3 = "audio/moansmisc3.ogg"
    define audio.moansmisc4 = "audio/moansmisc4.ogg"

    define audio.blowjob = "audio/blowjob.ogg"
    define audio.sex = "audio/sex1.ogg"

    define audio.city = "audio/ambiencecity.ogg"
    define audio.day = "audio/ambienceday.ogg"
    define audio.dungeon = "audio/ambiencecave.ogg"
    define audio.handjob = "audio/handjob.ogg"
    define audio.night = "audio/ambiencenight.ogg"
    define audio.rain = "audio/ambiencerain.ogg"
    define audio.wind = "audio/wind.ogg"
    define audio.river = "audio/river.ogg"

    #FX
    define fd = Dissolve(0.05)
    define d = Dissolve(0.3)
    define sd = Dissolve(0.8)
    define ssd = Dissolve(2.5)
    define c = Fade(.25, 0.0, .75, color="#fff")
    transform flip:
        xzoom -1.0
    define sshake = Shake((0, 0, 0, 0), 7.0, dist=13)


#variables
init 100:
    if renpy.variant("small"):
        default persistent.text_size = 26
    else:
        default persistent.text_size = 34
    $ quick_menu = True
    $ persistent.quick_menu = True
    $ gen1 = 0
    $ gen2 = 0
    $ gen3 = 0
    $ gen4 = 0
    $ gent1 = ""
    $ gent2 = ""
    $ textbox = 1
    $ bigmenu = 0
    $ default = 0

    $ day = 1
    $ completionpercent = 0
    $ save_name = "Day {} - {}%".format(day, completionpercent)
    $ money = 40
    $ time = "Night"
    $ energy = 2
    $ maxenergy = 2
    $ energytutorial = 0

    $ chloenamed = 0
    $ rosanamed = 0
    $ hildanamed = 0
    $ bastetnamed = 0

    #todo
    $ intro1 = 1 
    $ intro2 = 0
    $ magicroute1 = 0
    $ magicroute2 = 0
    $ brothelroute1 = 0
    $ brothelroute2 = 0
    $ farmroute1 = 0
    $ farmroute2 = 0
    $ forestroute1 = 0
    $ forestroute2 = 0
    $ bakeryroute1 = 0
    $ bakeryroute2 = 0
    $ barroute1 = 0
    $ barroute2 = 0
    $ castleroute1 = 0
    $ castleroute2 = 0

    $ magiccompletion = 0
    $ brothelcompletion = 0
    $ farmcompletion = 0
    $ forestcompletion = 0
    $ bakerycompletion = 0
    $ barcompletion = 0
    $ castlecompletion = 0

    $ postgame = 0
    $ percent_value = 0
    $ textboxalign = 90

    #secks
    $ moxpen1 = 0
    $ moxpen2 = 0
    $ mox1 = 1 #This scene can't be avoided

    $ lil1 = 0 
    $ lily1 = 0
    $ lily2 = 0
    $ lilyspank = 0
    $ lil2count = 2

    $ pen1 = 0
    $ petplay = 0
    $ tiedup = 0

    $ rub1 = 0
    $ rub2 = 0
    $ noncon = 0
    $ mel1 = 0
    $ mel2 = 0

    $ blo1 = 0
    $ hon1 = 0

    #misc
    $ v1complete = 0
    $ v2complete = 0
    

    # phone
    $ read = 0
    $ unread = 0 
    $ unreadmox = 0
    $ unreadpen = 0
    $ unreadlil = 0
    $ unreadrub = 0
    $ unreadmel = 0
    $ unreadhon = 0
    $ unreadblo = 0
    $ unreadbut = 0
    $ undreadrik = 0
    $ unreadcre = 0 

    $ moxmsg1 = 0
    $ moxmsg2 = 0

    $ penmsg1 = 0

    $ lilmsg1 = 0

    $ melmsg1 = 0
    $ melmsg2 = 0

    $ blomsg1 = 0

    $ gallery = 0
    
    $ feedupdate = 0

    $ phonebg = 1
    $ phoneenabled = 1


    #shops
    $ bunnygirl = 0
    $ punk = 0
    $ goth = 0

    $ pantyhose = 0
    $ lingerie = 0 

    $ buttplug = 0
    $ lubrication = 0
    $ lewdspellbook = 0
    $ futapill = 0 
    $ pregpotion = 0

    $ moxiebunnygirl = 0
    $ moxiepunk = 0
    $ moxiepantyhose = 0
    $ moxielingerie = 0 
    $ moxiebuttplug = 0
    $ moxielubrication = 0
    $ moxielewdspellbook = 0
    $ moxiefutapill = 0
    $ moxiepregpotion = 0
    $ moxgift = 0





#styles
style outline:
    outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
init python:
    import math

#images
image bg black = "black.png"

#misc
#common events
label camerabreath:
    camera:
        linear 0.5 zpos -12 ypos -2 xpos 0
        block:
            linear 2.4 ypos 5
            linear 0.8 ypos 5
            linear 1.8 ypos -2
            linear 0.8 ypos -2
            repeat
    return
label camerareset1:
    label camerareset:
        camera:
            linear 0.5 xpos 0 ypos 0 zpos 0
    return
label camerareset2:
    camera:
        xpos 0 ypos 0 zpos 0
    return

label stopbgs:
    stop moans1 fadeout 1
    stop moans2 fadeout 1
    stop ambience1 fadeout 1
    stop ambience2 fadeout 1
    stop ambience3 fadeout 1
    return

label genreset:
    $ gen1 = 0
    $ gen2 = 0
    $ gen3 = 0
    $ gen4 = 0
    $ gent1 = ""
    $ gent2 = ""

#text beep
define sounds = ['audio/clicks/A1.ogg', 'audio/clicks/A2.ogg', 'audio/clicks/A3.ogg', 'audio/clicks/A4.ogg', 'audio/clicks/A5.ogg', 'audio/clicks/B1.ogg', 'audio/clicks/B2.ogg', 'audio/clicks/B3.ogg', 'audio/clicks/B4.ogg', 'audio/clicks/B5.ogg']

#Avoid Clicking

##SHAKE SCRIPT
init python:
        import math
        class Shaker(object):
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child 
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move, time, child, add_sizes=True, **properties)

        Shake = renpy.curry(_Shake)
