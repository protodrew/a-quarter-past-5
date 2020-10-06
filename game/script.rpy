define pc = Character("Player", color="#d44e8e")
define gg = Character("Jade", color="#4f12b2")
define hb = Character("Herbert", color="#f45578")
define mf = Character("Rosa", color="#37c1d3")
define ow = Character("Arcade Owner", color="#37c1d3")
define nm = Character("News", color="#60d67b")
define route = "none"


label start:

    scene bg_newsroom
    show ch_nm_frown
    play music "audio/newssong.ogg"
    nm "with grim faces that the world’s greatest minds have told us to wrap up any unfinished business that we might be having."
    nm "Hug your loved ones, confess to those that you never had the chance to. Eat the foods you always were curious about, visit that place you’ve been meaning to."
    nm "H***, maybe try and beat that high score you’ve always been meaning to. God knows you won’t have another chance to once Friday arrives."
    nm "...am I allowed to say that on air? H***?"

    scene bg_black

    "I wanted to keep watching, but my thoughts were interrupted as the lady at the counter finished counting up the bills I had given her."

    scene bg_desk_day1
    play music "audio/Day1.ogg" fadeout 1
    show ch_owner_tired
    ow "I mean, I appreciate the business, hun, but are you sure you want to be spending your time here?"
    pc "{cps=25}Should I… not be?{/cps}"
    pc "{cps=25}You make it sound kind of… sketchy.{/cps}"
    hide ch_owner_tired
    show ch_owner_smug
    ow "Here? The ol’ NAMEOFARCADE? No, this place is as solemnly serious and trustworthy as it was twenty years ago, and I’d appreciate it if you treated it as such."
    pc "{cps=25}...okay, uhm. Mrs…{/cps}"
    "My eyes trail down to her nametag, though it was hard to make out the lettering what with the vomit’s worth of Lisa Frank stickers encasing it."
    pc "… Poca?"
    ow "It's Rosa, dearie, and you already paid."
    pc "Then why did you ask if I was sure I should be going here?"
    hide ch_owner_smug
    show ch_owner_laugh
    "Rosa laughs, my confusion evidently hilarious to her."
    mf "Just have fun, hun. There are a bunch of other kids here who I’m sure you’ll get along with well."
    pc "It’s kind of late to be making friends."
    hide ch_owner_laugh
    show ch_owner_neutral
    mf "Oh, it's never too late."
    mf "But if you’re feeling shy, you’re free to hang out with me some more, alright?"

    menu:
        "GO TO ARCADE ROOM 1":
            jump day1_hb
        "GO TO ARCADE ROOM 2":
            jump day1_gg
        "STAY at entrance":
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

    jump game_gg

label game_gg:
    scene bg_black
    "This is a placeholder for the shooter arcade game that you will be playing. You'll actually win or lose the game, but for now you can pick."
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
    show ch_gg_surprised
    $ route = "gg"

    gg "Oh… You actually. Won, huh."
    "With that, the metal clasp that had been holding the platypus down comes unhinged, letting it fall easily into my hands. It feels nice to have won something, but after hugging it tightly for a few seconds, I realize that I don’t actually want to lug this thing home."
    pc "Do you, uh, want this…?"
    hide ch_gg_surprised
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
    hide ch_gg_smug

    menu:
        "GO TO ARCADEROOM1":
            jump day1_hb
        "GO TO ENTRANCE":
            jump day1_m
        "TRY AGAIN":
            jump game_gg

    jump day1_done

label day1_m:
    scene bg_desk_day1
    show ch_owner_guilt
    mf "Oh? You decided you want to hang out with me some more?"
    hide ch_owner_guilt
    show ch_owner_laugh
    mf "Well, that’s just fine, hun. I’m flattered you want to spend some more time with an old coot like me."
    hide ch_owner_laugh
    show ch_owner_neutral
    mf "Unless you’re just being nice and sticking around for a bit? Are you sure that you don’t want to go play some games?"

    menu:
        "STICK AROUND":
            jump day1_sa
        "NAW I’M GAMING MAN":
            jump day1_ng

label day1_sa:
    scene bg_desk_day1
    $ route = "mf"

    show ch_owner_neutral
    pc "No, I want to hang out and talk with you for a bit, if that’s okay."
    mf "Oh, I’m most certainly okay with it. I’m just not sure if spending your time with a rackety ol’ woman like me is a wise investment on your part."
    pc "I dunno. You seem nice enough."
    show ch_owner_smug
    mf " I seem it, huh. But am I actually it… who’s to say, ufufu."
    hide ch_owner_smug
    show ch_owner_guilt
    "We stare at each other for a few awkward, palpable seconds."
    pc "...you sound like some sort of cartoon villain."
    hide ch_owner_guilt
    show ch_owner_smug
    mf "That’s kind of the point though, right? Isn’t it funny?"
    hide ch_owner_smug
    show ch_owner_neutral
    pc " Uhm… if that’s what you want to believe."
    pc "All that aside… Do you know why this place is still open during. Well, this whole mess?"
    hide ch_owner_neutral
    show ch_owner_laugh
    mf "Well, I’m the owner, so I’d hope I know. And I just decided I wanted to keep this place open, so that’s what I’m managing these last few days. So that’s that."
    hide ch_owner_laugh
    show ch_owner_tired
    mf "Don’t worry, I’m not making any employees work. S’just me, though that means if there are any D*rito crumbs around, you can’t get mad at me, ‘kay?"
    pc "All… by yourself? That feels like a pretty awful way to live your last few days."
    hide ch_owner_tired
    show ch_owner_smug
    mf "Just ‘cause the meteor’s gonna destroy earth doesn’t mean I’m gonna die with it. Ya never know. Gotta plan for that long term."
    pc "I don't think that's..."
    pc "{cps=10}...{/cps}"
    pc " ...well, I guess I can’t complain."
    mf "Tell ya what. If you keep on coming here consistently, we can hang out more and I can let you in on a few more trade secrets, huh?"
    hide ch_owner_smug
    show ch_owner_solemn
    mf "It gets pretty lonely when you’re as old as me, anyway. Be nice to your elders and spend some time with ‘em."
    pc "How old are you, anyway?"
    hide ch_owner_solemn
    show ch_owner_flirty
    mf "Isn’t it a cardinal sin to ask a woman her age?"
    "Then why do you keep bringing it up so often…"
    "But she’s an entertaining enough person to talk to. It’s not like I have anywhere better to be, so I guess I’ll see her tomorrow."

    jump day1_done

label day1_ng:
    scene bg_desk_day1
    show ch_owner_neutral
    pc "I just, uh… wanted to check in on you. I’ll be playing some more games."
    mf "Oh, that’s quite alright. Hope you have fun!"

    menu:
        "GO TO ARCADEROOM1":
            jump day1_hb
        "GO TO ARCADEROOM2":
            jump day1_gg

label day1_fo:
    scene bg_black
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
    hide ch_hb_shocked
    show ch_hb_smug
    hb "No, if you want me to beat your ass to a pulp, I’m more than glad to do some public service. Might even count as a good deed, teaching you a lesson."
    "I just want to play some games, man…"

    jump game_hb

label game_hb:
    scene bg_black
    "This is a placeholder for the pong arcade game that you will be playing. You'll actually win or lose the game, but for now you can pick."
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

    menu:
        "TRY AGAIN":
            jump game_hb
        "GO TO ARCADEROOM 2":
            jump day1_gg
        "Go TO ENTRANCE":
            jump day1_m

label day1_wp:
    scene bg_corner_day1
    $ route = "hb"

    pc "Oh! I won!"
    show ch_hb_shocked
    hb "No… No way…"
    " I turn to the other boy, expecting to exchange some sort of firm handshake or at least an awkward acknowledgment that I’d won, but he looks like he’s on the verge of throwing up."
    hide ch_hb_shocked
    show ch_hb_tears
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
    "{cps=25}Transition to day 2{/cps}"
    jump day2_start

label day2_start:
    scene bg_newsroom
    show ch_nm_frown
    play music "audio/newssong.ogg"
    nm "While the phrase ‘new beginnings’ might make one feel a little nihilistic at a time like this, that doesn’t necessarily mean that it’s unable to be applied to current circumstances."
    nm "We have a unique situation, now, where we’re able to take the initiative and not worry about repercussions if only because there isn’t ample time to receive them."
    nm "I’d say something like “take a chance to talk to that one guy in your office you’ve never been brave enough to talk to before”, but hopefully your boss isn’t keeping you there during the end of the world."
    nm "So do what you can; take that leap."
    nm "It’s not like you have enough time to reach the bottom if you end up falling, anyway."

    if route == "hb":
        jump day2_hb
    elif route == "gg":
        jump day2_gg
    elif route == "mf":
        jump day2_m

label day2_m:
    scene bg_desk_day2
    show ch_owner_neutral
    pc "So... Do I still need to pay if I just want to hang out with you the entire day?"
    "To her credit, Rosa blinks a bit before laughing merrily at what I’ve said."
    mf "I didn’t think you’d actually take me up on my offer, champ. Seems like kind of a waste to spend these last few days hanging out with an old woman of a stranger you don’t know."
    pc "And it feels like kind of a waste to be running an arcade during a time like this, too, yet here you are."
    mf "Fair enough. Alrighty then, kid."
    hide ch_owner_neutral
    "She reaches over and pulls over a seat that I hadn’t seen before, some splintered stool thing that looks like it’ll collapse underneath my weight. Nonetheless, she pats it expectantly."
    "The day passes by a little tenser than yesterday’s had gone. It’s not as if she’s ignoring me, per se, but she prioritizes the customers at the desk instead, entertaining splintering conversations before waving them off indoors."
    "We barely exchange words for even an hour, what with how hard she’s working, and even then we only get a break because the morning rush has slowed down."
    show ch_owner_neutral
    mf "Haaa… I’m really getting too old for this sort of stuff, right?"
    mf "Good thing we’ll all be dead soon, heh!"
    "She laughs uproariously at this, and all I can do is blink. After a moment, she coughs into her hand."
    mf "S’just a little bit of black humor, right? You need to be open to jokes a lil’ more."
    pc "Well, no, I was just… thinking."
    mf "Oh."
    mf "Well, then. Penny for your thoughts?"
    pc "You’re tired by this, but you’re doing it anyway."
    mf "Huh… a good point, right?"
    mf "I mean, truly: why would a sane person even be doing this, right?"
    "She laughs at it as if her mortality is something incredibly funny, but I find the answer incredibly simple."
    pc "Well, it’s because you’re a good person, right?"
    "Rosa blinks owlishly at me."
    mf "You think I’m a good person, champ?"
    pc "Of course I do!"
    pc "I think it’s really nice that you find running an arcade fulfilling enough that you’re spending your last few days doing it."
    pc "Not many other people would be able to do that, and I think you’re making a lot of kids happy by doing this."
    mf "So I’d only be running this if it was something I really enjoyed or found fulfilling, huh…"
    "She looks incredibly wistful as she mutters that to herself, chin propped up on her hand as she looks away from me."
    mf "That’s probably the logical conclusion that one would make."
    pc "Am I… wrong?"
    "Rosa leans back, stretching her hands as she smiles cheekily at me."
    mf "Nope! Why else would I be doing something like this, right?"
    mf "Anyway, I have some tickets that need counting. If you’re sitting over here, the least you could do is make your hands as busy as your mouth."
    hide ch_owner_neutral
    "I spend the rest of the day hanging out with Rosa, counting out tickets and money as people come to visit the arcade."
    "When it starts getting dark, I wave her goodbye and start making my way home."
    "I wonder if I’ll see her tomorrow..."
    jump day3_start

label day2_gg:
    scene bg_long_day1
    show ch_gg_neutral at right
    "Jade’s in the same place where I saw her last, albeit minus the platypus plushie in her arms."
    hide ch_gg_neutral
    show ch_gg_angry at right
    "We make eye contact across the room only for her to flinch and look away."
    "Hey, that’s no way to treat a new friend, is it?"
    hide ch_gg_angry
    show ch_gg_surprised at right
    gg "W-wha…"
    gg "We’re not, we’re not friends--!"
    hide ch_gg_surprised
    show ch_gg_flustered at right
    "She cuts herself off as if she had broken some unspoken vow of not talking to me to herself, pulling at the fishnets on her arms as she looks away."
    gg "...thanks for the plush, again. He’s at home, if you were wondering."
    gg "N-not that you would, ‘cause that would be weird, right? Haa…"
    pc "Nah, I’m glad to hear he’s doin’ fine. Was real worried I’d sent him off to some awful home, and I don’t think I could deal with that sort of guilt on my shoulders when the world’s about to end."
    gg "He’s just a plush…"
    "She says that, but looks relieved as she pulls some hair behind her ear. Her eyes dart around, looking for a way to continue the conversation."
    hide ch_gg_flustered
    show ch_gg_neutral at right
    gg "Hey, uh… what’s that you’ve got on your jacket?"
    pc "Huh? Oh, you mean this thing I’ve got on my zipper?"
    gg "I pull the zipper up, getting a better look of the charm that’s fastened there. It’s a cheap little honeybee thing that I got as an extra from inside a cereal box."
    "I’m honestly impressed with how long it’s survived. One of the eyes has been worn off and the edges are frayed, but the honeybee smiles up at me with its misshaped smile nonetheless."
    pc "S’just a lil trinket, I guess. Why? Is it from some franchise you like or something?"
    "Jade leans in a little bit to take a closer look at the thing before shaking her head."
    gg "I guess… I don’t really expect people to be so open about liking stuff like this."
    gg "Isn’t it a little embarrassing?"
    pc "Eh, not really. Though it’s probably because I don’t really hang out with people enough to think it’s embarrassing."
    gg "…"
    gg "That’s just… really sad."
    "She says that, but some part of her looks… weirdly impressed by the fact that I can be so open about this. I think she wants to comment on it before someone else bursts through the door."
    show ch_hb_neutral at left
    hb "Where are-- Oh, there, huh?"
    hide ch_gg_neutral
    show ch_gg_eyeroll at right
    "A boy that I think I might’ve seen milling about the arcade yesterday marches forward to the two of us. Jade’s already sighing, massaging her temples prematurely."
    gg "I’m not going to play another round with you, Herbert."
    hide ch_hb_neutral
    show ch_hb_hello at left
    hb "W-who said I was going to ask you to fight me?"
    gg "Oh, I’m sorry. What is it that you needed me for?"
    hb "…"
    hb "...well,"
    gg "Yeah, I thought so."
    "Jade sighs deeply, then sighs again as she looks me up and down with a vague look of disdain on her face."
    gg "Herbert, I’m hanging out with someone, so I can’t be your punching bag to give you an ego boost."
    hide ch_hb_hello
    show ch_hb_angry at left
    hb "That’s not-- I play completely fair and square against you!"
    gg "But you know I’m really bad at this, so you just pick an easy target."
    gg "W-well…"
    hide ch_gg_eyeroll
    show ch_gg_neutral at right
    "Jade laughs as Herbert sulks, but ultimately pulls down his hat over his eyes playfully as she makes her way over to one of the arcade stations."
    gg "C’mon, I’ll play one round with you. For the road."
    hide ch_hb_angry
    show ch_hb_smug at left
    hb "Ah-- Hell yeah!!!"
    "Herbert perks up noticeably at that, and I watch the two of them play a few rounds of some generic fighting game."
    "I don’t know much about it, but I can tell Jade is… not that good. At the very least, her health bar goes down way faster than it does Herbert’s."
    "I think I should be impressed with how well Herbert handles the fight, but it might just be that “you look cooler when you’re next to someone bad at something” feeling."
    gg "Aaaand that’s where I’m going to call it."
    "Herbert is not subtle in his joy over winning, whooping and hollering obnoxiously. Still, he gives Jade a quick handshake and me a weak high-five before running off to entertain himself with something else."
    gg "There he goes. I don’t know how he has that sort of energy; he’s older than me."
    gg "Anyways. Sorry that I didn’t even end up talking to you much, but I think this is where I’m going to call it quits for today."
    hide ch_gg_neutral
    show ch_gg_flustered at right
    gg "I get it if you don’t want to hang out with me again, since I just kinda blew you off, haha."
    "She smiles somewhat self-deprecatingly."
    "She looks… lonely, to say the very least. I keep a stiff upper lip and decide to be as nice to her as I can."
    pc "Jade, hang out with me tomorrow again, okay?"
    gg "H-huh?"
    pc "I really like hanging out with you, and I want to do it again!"
    pc "Unless you’re uncomfortable around me, which, like, is a whole ‘nother issue altogether but I definitely understand and will respect your personal boundaries--"
    gg "No! I-I mean, no, that’s. Uh."
    gg "...that’s fine. I’d like hanging out with you, too. If you’d want to. I guess."
    pc "Ehh, you make it sound like hanging out with me is a chore! I’d like to think I’m at least a little entertaining to be around."
    gg "A-alright, alright, jeez. I’ll see you tomorrow, alright?"
    gg "‘Cause you’re fun to be around or whatever."
    pc "Man, you sound like every cliche of a tsundere to exist."
    gg "What… what does that even mean?"
    pc "Eh, don’t worry about it."
    pc "See you tomorrow, pal! Let’s hope the meteor doesn’t try to push up its schedule, right?"
    "With that, I wave her off. Despite everything, I really do hope I’ll see her again tomorrow."

    jump day3_start


label day2_hb:
    scene bg_corner_day1
    "I haven’t even finished buying a ticket for the day from Rosa when Herbert comes dashing around the corner, smoke smothered by the way his sneakers skid across the floor as he throws an accusatory finger in my direction."
    show ch_hb_angry at right
    hb "Y-you!!"
    pc "Me?"
    hb "You’re… here again. How dare you show your face, after all you did--!"
    pc "What is this, an anime?"
    hide ch_hb_angry
    show ch_hb_embarrassed at right
    "Herbert draws back, flustered."
    hb "W-wha…"
    pc "Like, are you challenging me to a duel or something? Are we destined to fight to the death?"
    pc "Or are you just a bitter rival sort of character that ends up dying early on to show how serious the real villain is?"
    hb "I, uh--"
    hb "I definitely don’t know what you’re talking about, but I’m guessing from… from c-context clues, I’d be the former, right?"
    hb "‘Cause I’m not gonna rest until you’re dead! Mark my words!"
    show ch_owner_neutral at left
    mf "You should be careful about sayin’ stuff like that, champ."
    "Rosa cuts into the conversation as she hands me my ticket back, looking at Herbert with a smile that doesn’t reach her eyes."
    mf "Let’s try and keep things nice and friendly here, right?"
    hide ch_hb_embarrassed
    show ch_hb_guilty at right
    hb "Y… yes ma’am."
    "Herbert pulls back like some sort of sullen puppy. I wave goodbye to Rosa before following Herbert into the arcade."
    hide ch_owner_neutral
    pc "So, what’s the plan for today?"
    hide ch_hb_guilty
    show ch_hb_neutral at right
    hb "The… the plan?"
    pc "I mean, are we gonna fight? Since I made you cry yesterday, I think it’s only fair that I hang out with you today to smooth things out."
    hb "I-I mean--"
    pc "You want to play some games or something? Since we’re in an arcade and all."
    pc "Unless yesterday got you so choked up n’ traumatized that you can’t look at a game console again. Which is, like, totally fair."
    hb "N-no! I can--"
    "Herbert stumbles over his words before frowning, stuck with newfound determination."
    hb "We’re playing Pong again."
    pc "Man, you sound so serious."
    hb "B-because I am! I refuse to let things end the way they did!"
    pc "And you say you aren’t an anime protag…"
    "Despite his words, we set upon the nearest game console in earnest. Though I defeated him soundly last time, he seems to have approached some sort of solace in his own head and doesn’t look like he’s going to cry this time around if I beat him."
    "(PONG GAME AGAIN outcome doesnt matter)"
    "When the game has finished, Herbert leans back and laughs heartily from besides me."
    pc "So I take it you had fun?"
    hb "Did I? Did I--"
    "He looks at me with such a look of genuine excitement that it feels physically painful when he remembers himself and coughs into his hand, collecting himself together and patting down his shirt as if it would keep him grounded."
    hb "Y-yeah. I had. A small amount of fun. A decent dollop of it, if you will."
    "I laugh and shove him playfully."
    pc "Who even speaks like that? What are you, from the 1800s?"
    hb "H-hey--!"
    "He says that, but he’s laughing too."
    pc "Anyway, I had fun. Is this how you play with people when you aren’t being an over competitive dick?"
    "His laughter dies off, and it’s as he looks at me all too guiltily that I wonder if I’ve pushed his buttons a little too accurately."
    hide ch_hb_neutral
    show ch_hb_guilty at right
    hb "I, uh…"
    hb "Don’t really. Play with people just casually, I guess."
    hb "I play against them, and I win, and that’s like… my thing?"
    "He laughs nervously, but there’s no humor in it."
    hb "So when you beat me, I kinda got super stressed over it and. I dunno, it kinda sucked."
    hb "S-so I’m trying to play more with you now, and not think about it too much."
    pc "Huh."
    pc "Well, I didn’t ask for your whole backstory or anything, but thanks for that, I guess--"
    hide ch_hb_guilty
    show ch_hb_embarrassed at right
    hb "A-a backstory?!"
    hb "Why would you call it th--"
    "I can’t help but laugh good naturedly at how flustered he looks."
    hide ch_hb_guilty
    "We manage to share a few more good small conversations over the next few hours, buying out all the snacks from a vending machine and dirtying up the game consoles with our chip dust covered fingers."
    "Despite everything, I feel closer to Herbert than I do to most people. He’s awkward, but ends up being genuine with his actions, even if he tries hard to be mean. Like some sort of pissed off kitten."
    "But the hours roll on by quickly enough, and before long, it’s time to head home."
    show ch_hb_neutral at right
    hb "So, uh…"
    "He hesitates to say it, but it comes out anyway."
    hb "See you tomorrow? For another round?"
    pc "Of course! If you’re not there, I’d be disappointed."
    "He smiles cheekily at me, relieved."
    "Guess I’ll see him tomorrow."
    jump day3_start

label day3_start:

    return
