define pc = Character("Player", color="#d44e8e")
define gg = Character("Goth Girl", color="#4f12b2")
define hb = Character("Hat Boy", color="#f45578")
define mf = Character("Owner", color="#37c1d3")
define nm = Character("News", color="#60d67b")


label start:

    scene bg_newsroom
    show ch_nm_frown

    nm "with grim faces that the world’s greatest minds have told us to wrap up any unfinished business that we might be having."
    nm "Hug your loved ones, confess to those that you never had the chance to. Eat the foods you always were curious about, visit that place you’ve been meaning to."
    nm "H***, maybe try and beat that high score you’ve always been meaning to. God knows you won’t have another chance to once Friday arrives."
    nm "...am I allowed to say that on air? H***?"

    scene bg_black

    "I wanted to keep watching, but my thoughts were interrupted as the lady at the counter finished counting up the bills I had given her."

    scene bg_desk_day1

    show ch_milf_tired

    mf "I mean, I appreciate the business, hun, but are you sure you want to be spending your time here?"
    pc "{cps=25}Should I… not be?{/cps}"
    pc "{cps=25}You make it sound kind of… sketchy.{/cps}"


    hide ch_milf_tired
    show ch_milf_smug

    mf "Here? The ol’ NAMEOFARCADE? No, this place is as solemnly serious and trustworthy as it was twenty years ago, and I’d appreciate it if you treated it as such."
    pc "{cps=25}...okay, uhm. Mrs…{/cps}"
    "My eyes trail down to her nametag, though it was hard to make out the lettering what with the vomit’s worth of Lisa Frank stickers encasing it."
    pc "… namebutslightlywrongspelled?"
    mf "It's name, dearie, and you already paid."
    pc "Then why did you ask if I was sure I should be going here?"
    hide ch_milf_smug
    show ch_milf_laugh
    "M laughs, my confusion evidently hilarious to her."
    mf "Just have fun, hun. There are a bunch of other kids here who I’m sure you’ll get along with well."
    pc "It’s kind of late to be making friends."
    hide ch_milf_laugh
    show ch_milf_neutral
    mf "Oh, it's never too late."
    mf "But if you’re feeling shy, you’re free to hang out with me some more, alright?"

    menu:
        "GO TO ARCADE ROOM1":
            jump day1_hb
        "GO TO ARCADE ROOM 2":
            jump day1_gg
        "STAY at enterance":
            jump day1_m

label day1_hb:
    scene bg_corner_day1

    "I decided to make my way over to ARCADEROOM1. A lot of the PvP games are over here, and I figured it might be fun to try those out."
    "There weren’t many people milling about, most of them enamored in doing their own thing or playing in pairs, but there was one guy who seemed to be…"
    pc "Are you… playing with yourself?"
    show ch_hb_angry
    hb "Haa? You got a problem with that?"
    "The boy turns away from his game of Pong, his shoulders raising as he channels all the energy of the angry, wet kitten that he seems to be."
    pc "N-no, that’s fine, I just was--"
    hb "Fu-- F-frick off, man."

    menu:
        " FU-FRICK OFF":
            jump day1_fo
        "DO NOT FU-FRICK OFF":
            jump day1_dnfo

    jump day1_done

label day1_gg:
    scene bg_long_day1

    "ARCADEROOM2 is a lot more single-player centric, so you don’t really see people interacting with each other here. I thought it would be easier to breathe and do my own thing, and yet…"
    "What stands out to me, more than anything else, is the comically large platypus doll plopped on top of the SHOOTERGAME console in the middle of the room."
    "The most shocking thing, really, is that it hasn’t been plucked up and taken away yet, but closer inspection reveals that it’s been chained down to the console in order to prevent such highway robberies."
    show ch_gg_neutral
    gg "You’ve got to beat the high score to get it."
    pc "Huh?"
    gg "Trust me, if it was that easy, that platypus would be gone by now. But it’s not."
    gg "You’re welcome to try your hand at the game if you’d like. Hell knows that it’d make me feel better seeing someone else fail."

    menu:
        "Try The Game":
            jump day1_tg
        "Go Somewhere else":
            jump day1_gse

label day1_tg:
    scene bg_long_day1
    show ch_gg_neutral
    pc "Yeah, I think I’ll give it a go."
    hide ch_gg_neutral
    show ch_gg_eyeroll
    gg "Pfft. Good Luck"

    menu:
        "win SHOOTERGAME":
            jump day1_wsg
        "lose SHOOTERGAME":
            jump day1_lsg


label day1_gse:
    scene bg_long_day1
    show ch_gg_neutral
    pc "U-uh, I think I’ll try going somewhere else for now…"
    hide ch_gg_neutral
    show ch_gg_smug

    menu:
        "GO TO ARCADEROOM1":
            jump day1_hb
        "GO TO ENTRANCE":
            jump day1_m

label day1_wsg:
    scene bg_long_day1
    show ch_gg_impressed

    gg "Oh… You actually. Won, huh."
    "With that, the metal clasp that had been holding the platypus down comes unhinged, letting it fall easily into my hands. It feels nice to have won something, but after hugging it tightly for a few seconds, I realize that I don’t actually want to lug this thing home."
    pc "Do you, uh, want this…?"
    hide ch_gg_impressed
    show ch_gg_flustered
    "The girl looks so genuinely startled that it makes me wonder if I accidentally said a slur or something, but recollects herself quickly enough."
    gg "You sure about that? You’ve got yourself a real good chunky boy right there. Maybe you shouldn’t be letting go of him that easily."
    pc "No, it’s fine. I don’t really mind."
    "I hand it over to her, and she blinks a few more times as she looks between me and the platypus plushie before clearing her throat."
    hide ch_gg_flustered
    show ch_gg_neutral
    gg "Well, such a noble sacrifice demands a name in payment, at the very least. I’m GG, but you can just call me NICKNAME."
    hide ch_gg_neutral
    show ch_gg_smug
    gg "Maybe I’ll see you again before I die. Or not. Heh."
    "As if it wasn’t a little morbid, GG laughs to herself, taking the platypus plushie and exiting the building. "
    pc "I wonder if I’ll see her tomorrow…"
    jump day1_done

label day1_lsg:
    scene bg_long_day1
    pc "Oh… I lost…"
    show ch_gg_smug
    gg "Eh, don’t feel too badly about it."
    jump day1_done

label day1_m:
    scene bg_desk_day1
    show ch_milf_guilt
    mf "Oh? You decided you want to hang out with me some more?"
    hide ch_milf_guilt
    show ch_milf_laugh
    mf "Well, that’s just fine, hun. I’m flattered you want to spend some more time with an old coot like me."
    hide ch_milf_laug
    show ch_milf_neutral
    mf "Unless you’re just being nice and sticking around for a bit? Are you sure that you don’t want to go play some games?"

    menu:
        "STICK AROUND":
            jump day1_sa
        "NAW I’M GAMING MAN":
            jump day1_ng

label day1_sa:
    scene bg_desk_day1
    show ch_milf_neutral
    pc "No, I want to hang out and talk with you for a bit, if that’s okay."
    mf "Oh, I’m most certainly okay with it. I’m just not sure if spending your time with a rackety ol’ woman like me is a wise investment on your part."
    pc "I dunno. You seem nice enough."
    show ch_milf_smug
    mf " I seem it, huh. But am I actually it… who’s to say, ufufu."
    hide ch_milf_smug
    show ch_milf_guilt
    "We stare at each other for a few awkward, palpable seconds."
    pc "...you sound like some sort of cartoon villain."
    hide ch_milf_guilt
    show ch_milf_smug
    mf "That’s kind of the point though, right? Isn’t it funny?"
    hide ch_milf_smug
    show ch_milf_neutral
    pc " Uhm… if that’s what you want to believe."
    pc "All that aside… Do you know why this place is still open during. Well, this whole mess?"
    hide ch_milf_neutral
    show ch_milf_laugh
    mf "Well, I’m the owner, so I’d hope I know. And I just decided I wanted to keep this place open, so that’s what I’m managing these last few days. So that’s that."
    hide ch_milf_laugh
    show ch_milf_tired
    mf "Don’t worry, I’m not making any employees work. S’just me, though that means if there are any D*rito crumbs around, you can’t get mad at me, ‘kay?"
    pc "All… by yourself? That feels like a pretty awful way to live your last few days."
    hide ch_milf_tired
    show ch_milf_smug
    mf "Just ‘cause the meteor’s gonna destroy earth doesn’t mean I’m gonna die with it. Ya never know. Gotta plan for that long term."
    pc "I don't think that's..."
    pc "{cps=10}...{/cps}"
    pc " ...well, I guess I can’t complain."
    mf "Tell ya what. If you keep on coming here consistently, we can hang out more and I can let you in on a few more trade secrets, huh?"
    hide ch_milf_smug
    show ch_milf_solemn
    mf "It gets pretty lonely when you’re as old as me, anyway. Be nice to your elders and spend some time with ‘em."
    pc "How old are you, anyway?"
    hide ch_milf_solemn
    show ch_milf_flirty
    mf "Isn’t it a cardinal sin to ask a woman her age?"
    "Then why do you keep bringing it up so often…"
    "But she’s an entertaining enough person to talk to. It’s not like I have anywhere better to be, so I guess I’ll see her tomorrow."

    jump day1_done

label day1_ng:
    scene bg_desk_day1
    show ch_milf_neutral
    pc "I just, uh… wanted to check in on you. I’ll be playing some more games."
    mf "Oh, that’s quite alright. Hope you have fun!"

    menu:
        "GO TO ARCADEROOM1":
            jump day1_hb
        "GO TO ARCADEROOM2":
            jump day1_gg

label day1_fo:
    scene
    "I decided I wasn’t going to deal with this when I didn’t have that many days left to live, and decided to go somewhere else. "

    menu:
        "GO TO ARCADEROOM2":
            jump day1_gg
        "GO TO ENTRANCE":
            jump day1_m

    jump day1_done

label day1_dnfo:
    scene bg_corner_day1
    hide ch_hb_angry
    show ch_hb_angry
    pc "Actually, I kind of… wanted to play a game with you?"
    hide ch_hb_angry
    show ch_hb_shocked
    "...huh?"
    pc "I-I mean, if you’re busy, that’s fine and everything--"
    hide ch_hb_schocked
    show ch_hb_smug
    hb "No, if you want me to beat your ass to a pulp, I’m more than glad to do some public service. Might even count as a good deed, teaching you a lesson."
    "I just want to play some games, man…"
    "GAME GOES HERE"
    menu:
        "Lose the game":
            jump day1_lp
        "Win the game":
            jump day1_wp


label day1_lp:

    scene bg_corner_day1
    pc "Oh… I lost…"
    show ch_hb_smug
    hb "Heh. Well, it’s to be expected, after all. Don’t, like, kill yourself over it. "

    "Gamers are weird… I wonder if I’ll see him tomorrow."

    jump day1_done

label day1_wp:

    pc "Oh! I won!"
    show ch_hb_tears
    hb "No… No way…"
    " I turn to the other boy, expecting to exchange some sort of firm handshake or at least an awkward acknowledgment that I’d won, but he looks like he’s on the verge of throwing up."
    hb "This… can’t be real."
    pc "...are you okay? I-it’s just a game."
    pc "I-I just had beginner’s luck, right? So you don’t need to look so… sick over all this."
    "The boy doesn’t respond for a bit, clutching the sides of his arms for a second and breathing funny before shaking his head."
    hide ch_hb_tears
    show ch_hb_embarrassed
    hb "Yeah, right… this was nothing. Didn’t even matter. Just dumb luck, heh."
    "Mumbling these things to himself, the boy began to stumble his way out of the arcade. I watched him go for a bit before shaking my head."
    hide ch_hb_embarrassed
    pc "Gamers are weird… I wonder if I’ll see him tomorrow."
    jump day1_done

label day1_done:
    scene bg_black
    "{cps=25}This is the end of the prototype!{/cps}"
    "{cps=25}We used some repetitve dialogue to wallpaper over future progression points, but we hope this gave you the jist of our game{/cps}"

    return
