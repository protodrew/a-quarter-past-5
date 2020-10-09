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
    pc "… Rosie?"
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
    "{cps=25}4 Days Remain{/cps}"
    jump day2_start

label day2_start:
    scene bg_newsroom
    show ch_nm_frown
    play music "audio/newssong.ogg" fadeout 1
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
    play music "audio/Day2.ogg" fadeout 1
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
    jump day2_done

label day2_gg:
    play music "audio/Day2.ogg" fadeout 1
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

    jump day2_done


label day2_hb:
    play music "audio/Day2.ogg" fadeout 1
    scene bg_corner_day2
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
    jump day2_done

    label day2_done:
        scene bg_black
        "{cps=25}3 Days Remain{/cps}"
        jump day3_start

label day3_start:
    scene bg_newsroom
    show ch_nm_frown
    play music "audio/newssong.ogg" fadeout 1

    nm "I wanted to dedicate today’s morning segment to a few words on what it means to regret."

    nm "I’m sure we all find ourselves mired in thoughts about regret right now, whether they’re small dredges on fights that left a bad taste in our mouth or a general tiredness at what was accomplished in our life."

    nm "It goes without saying, but we can’t change life. We can’t go back in time, and choices made in imaginary arguments certainly don’t hold any weight."

    nm "In the past, we could say things like ‘keep moving forward’ and ‘make the most of what’s left in your life’, but…"

    nm "What do you say when there’s only two days left? Can you say anything at all?"

if route == "hb":
    jump day3_hb
elif route == "gg":
    jump day3_gg
elif route == "mf":
    jump day3_mf
    return



label day3_hb:
    play music "audio/Day3.ogg" fadeout 1
    scene bg_corner_day3
    show ch_hb_angry
    "Rosa greets me as usual when I enter the arcade, stifling a yawn despite the fact that it’s half past noon. I suppose I shouldn’t be nitpicking her when I only woke up an hour ago myself."
    "I find Herbert fairly quickly, which is expected; we did agree to do so yesterday, after all."
    "But what I don’t expect is the handful of boys that surrounds him, towering over him like playground bullies."
    "To his credit, he tries to pull himself together when he sees me."
    hb "Uh, heyyyyyy. PRO."
    hb "What. Is up."
    pc "Who’re these people?"
    "Even though my acknowledgement shouldn’t be anything unexpected, he still flinches as if I’ve ripped a bandaid off of him. He glances at the other people as if to speak, but they don’t say anything. He swallows thickly."
    hb "I guess, uh… they wanted to have a chance at beating me."
    hb "So, I guess we can’t have our duel today, right? Sorry, kid, you’re not going to be able to play with me today. Better luck next time!"
    hb "If there even is a next time, heh. I-I’m sure you’ll be dead before then, though."
    "Kid…?! I’m not a--"
    "...he glares at me anyway, brows knit together with all the pathetic force of someone trying to recall what it means to look threatening. If I didn’t have a pit growing in my stomach, I’d find the strength to comment on it."

    menu:
        "STAY":
            jump day3_stay
        "DON'T STAY":
            jump day3_ds


label day3_stay:
    scene bg_corner_day3
    show ch_hb_angry
    pc "No, I don’t think I will."
    hide ch_hb_angry
    show ch_hb_shocked
    hb "...what?"
    "Determinedly, I grip at his arm, pulling him closer to me as I blink as sweetly as I can at the other boys."
    pc "Sorry, can you guys all leave? Herbert and I have business to attend to."
    "He struggles for just a moment before something clicks in that dumb skull of his, growing limp as I negotiate with the other boys. Soon enough, they walk off in grumbled protest, leaving me and Herbert alone together."
    hb "...you can let go, now."
    pc "Why? Are you afraid you’ll get cooties?"
    hide ch_hb_shocked
    show ch_hb_embarrassed
    hb "N-no…"
    "I let go obediently nonetheless, laughing to myself with how flustered he looks."
    hb "You gotta learn to respect personal space, alright?"
    pc "Sorry, sorry. Didn’t think it would bother you so much."
    hb "Jeez… I don’t know why I hang out with you."
    pc "Because the alternative is hanging out with those guys. Or being alone, I guess, which also sucks, especially when the world is ending."
    pc "What was their deal, anyway?"
    hide ch_hb_embarrassed
    show ch_hb_guilty
    hb "Oh. Uh."
    "Herbert scuffs his foot on the ground."
    hb "They heard that… you beat me."
    pc "Huh?"
    hb "In Pong, y’know. I always bragged to them about how good I am-- How. How good I was at video games. And now they wanted to harass me over the fact that I couldn’t beat you."
    hb "I guess… I had it coming, y’know? Haha."
    hb "It was almost cathartic, before you came. Relieving, really. Needed someone to frickin’, yell at me for a bit. Remind me of the sort of person I am. Keeping me humble."
    pc "...Herbert, that’s really not--"
    hb "…"
    hb "...did you really fall for that? Me sayin’ sappy shit like that?"
    hide ch_hb_guilty
    show ch_hb_angry
    "Trying to save face, Herbert pulls himself back up to his full height, chest puffed out."
    hb "Man, I bet you’d believe it if I told you ‘gullible’ was written on the ceiling."
    pc "I don’t think it’s a secret at this point that you hinge your entire identity on being good at video games."
    "Herbert blinks at me incredulously before scowling."
    hb "Man, buzz off. I’m gonna be dead too soon to waste my time on this."
    hide ch_hb_angry
    "He shoulders past me, causing me to stumble for a moment before he storms out of the arcade."
    "I… wonder if I’ll see him tomorrow."

    jump day3_end

label day3_ds:
    scene bg_corner_day3
    show ch_hb_angry
    "His glare is enough to chase me off, and so I do it, ducking my head as I turn away from the group."
    hide ch_hb_angry
    "I justify it to myself as the fact that it’s what we both wanted: to stay uninvolved, to keep anyone from getting involved. I can understand that sort of a shame; respect it, even."
    "But it doesn’t leave any less of a bad taste in my mouth as I leave the arcade, head too busy to acknowledge Rosa’s calls after me as I make my way back home."
    "The phantom feeling of Herbert’s gaze boring into my back doesn’t leave, though, not when I make it home, not when I lay in bed and toss and turn for hours, listening to the radio discuss the end of all time"
    "I resolve, then, not to go to the arcade again; or at least, not tomorrow."

    jump day3_end2

label day3_gg:
    play music "audio/Day3.ogg" fadeout 1
    scene bg_long_day3
    show ch_gg_neutral
    pc "Heyyyyy, Jade!"

    "I wave wildly at her before I’ve even made it to the entrance, tackling her with a hug before she can make a move to escape."

    hide ch_gg_neutral
    show ch_gg_surprised
    gg "H-hey, watch it! There are other people in line, here--!"

    "She flounders underneath my grip as she struggles to get her bearing again. Despite how flustered she looks, though, she doesn’t look angry, so I chalk it up to a win."

    pc "I was so excited to hang out with you again today! "

    gg " R… really?"

    pc "Why do you sound so surprised? You’re a fun person to be around, you know!"

    gg " I don’t think that’s necessarily…"

    pc "Uh uh uh! Is that a lack of confidence in your voice that I’m detecting? Not allowed!"
    hide ch_gg_surprised
    show ch_gg_flustered
    "Jade laughs nervously, but her eyes dart from side to side. She looks nervous; about what, I can’t tell--"

    "...or maybe it’s something to do with the fact that the world is ending soon. I guess I’m the abnormal one for being so okay with my inevitable death in that regard."

    "I resolve to grab her hand instead, eliciting a different sort of nervousness from her."

    pc "C’mon! Let’s spend some time together in the arcade, alright? Maybe we can play that game again."

    gg " ...are you sure that’s a good idea?"

    pc "Oh, if you don’t want to play a game, then we can just, like, chill, or otherwise eat some really greasy and probably way past it’s expiration date pizza--"

    gg "No, I mean… hanging out with me."

    "She pulls her hand away from mine, and I let it go."

    pc "Why wouldn’t it be? Is something wrong?"

    pc "Even if you’ve actually got some deadly disease or something, the world ends too soon for me to care about that."

    gg "No, that’s not…"

    gg "...okay, yeah, whatever. You talk way too casually about stuff like that for it to be something that most people could brush off, I hope you realize."

    pc "Well, I guess you’re just not like other girls, huh?"
    hide ch_gg_flustered
    show ch_gg_neutral
    gg "Ghrk."

    "Jade stifles something that’s either a cough or a laugh or both. I smile cheekily and move to the game that I had played with her beforehand."

    "INSERT ANOTHER ROUND OF MINIGAME HERE; DOESNT MATTER OUTCOME"

    "It’s as I’m finishing up the game that I feel a tug on my jacket."

    "Initially, I think it’s just that it’s been caught on something; it’s an old jacket with tons of loose threads, after all. I guess I just got way more into the game than I had initially realized."

    "Without looking, I pull on it to try and get it unstuck. The tugging stops, just for a moment, before returning to a staticked pulling pattern at my side."

"I frown, turning to properly unstick the jacket from whatever it’s stuck to when I pause and realize the real problem."

"It isn’t stuck; Jade is trying to steal it."

menu:
    "Call her out on it":
        jump day3_co
    "let her have it":
        jump day3_lh


label day3_ns:
scene bg_long_day3
show ch_gg_neutral

pc "Hey, what the hell?"

"I jerk back from Jade, gripping onto the charm as I frown at her. Her fingers grasp the space in the air where the charm had been."

pc "Were you… stealing from me?"
hide ch_gg_neutral
show ch_gg_flustered

"Jade’s face distorts for a second before settling on a smug, vaguely nervous expression."

gg "Jeez, I got cocky, huh? Should’ve waited for a better time to do that."

gg "Yeah, I sure was. And what’re you gonna do about it?"

gg "Cry? Pee your pants, maybe? Throw a fit?"

pc "Well, I’m certainly not going to hang out with you anymore, that’s for sure."

"I tug my jacket closer around my shoulders as I take a few nervous steps away from her, brow furrowed as I make sure that the path between me and the exit is clear."

"It… it really does hurt. I’m not sure what Jade was planning to do all this time, but I find myself wondering… was this the real her, all along?"

"For a moment, she looks… hurt."

"But what was she expecting to happen? Surely, nothing other than this?"

gg "Fine, then. Didn’t want to hang out with a loser like you, anyway."

gg "See ya."

"With that, she flips her hair almost defiantly at me before making her way off."

"Nervous, I decide not to go to the arcade tomorrow."
jump day3_end2

label day3_lh:
    scene bg_long_day3
    show ch_gg_neutral
    pc "Oh, did you want this? Lemme help you with that."

    "I reach down to unfasten the honeybee charm from my jacket before handing it over to her."

    pc "Here you go! Take good care of it, alright?"
    hide ch_gg_neutral
    show ch_gg_surprised
    "Jade’s hands hang limp at her side as she stares at me, expression impossible to read."

    gg "I was… stealing that from you, dumbass."

    pc "Oh, I realized. Did you just want to steal it? Do you not actually want it?"

    gg "That shouldn’t be what you’re concerned about, here!"

    gg "Shouldn’t you be mad at me? Angry? Upset? At the very least, betrayed by me?"

    gg "Why are you still talking to me so casually?! Is this a joke?"

    pc  "No, I just don’t really care."

    pc "And I think it’s pretty obvious now that you were doing that just to get a reaction out of me."

    "Jade’s eyes widen for a moment before turning back into an angry, almost begging expression."

    gg "Right? So aren’t you mad at me for manipulating you?!"

    pc "Again, I don’t really care."

    pc "You wanna go get some ice cream?"
    hide ch_gg_surprised
    show ch_gg_eyeroll
    gg "...you can’t be serious."

    pc "If you really want me to be mad, then, uh, grr. I’m angry so you need to be the one that pays."

    "Jade stares at me incredulously before shaking her head."

    gg "I don’t… I don’t get you. What the hell is your problem?"

    "With that, Jade shoulders past me, causing me to drop the charm."

    pc "Ah--"

    "I bend over to pick it up, rubbing it to clean it of dust. By the time I look up again, she’s gone."

    "I hope I’ll see her again tomorrow..."

jump day3_end

label day3_mf:
    scene bg_desk_day3
    play music "audio/Day3.ogg" fadeout 1

    "I find myself in the same space I was yesterday, sitting prettily on the stool and pressing two-sided tape onto the back of ‘END OF THE WORLD SALE’ posters."

    "It feels like a bit overkill, especially when the business model for the end of the world doesn’t really seem sustainable, but I think I get the sentiment."

    "I flip the poster over. The smiling red meteor on the front feels like a mockery of the one that hangs heavy in the sky above."

    "Yeah, it’s kinda dumb to be encouraging more stress on myself, I know."

    "As if she had read my mind, Rosa sighs from besides me, rubbing the back of her neck. I blink in surprise."

    show  ch_owner_tired

    pc "I-I mean… I wasn’t going to say it, but… yeah."

    mf "Well, not just anyone could do this."

    "I can’t really tell whether she’s talking more to me or herself, but I let her run her mouth anyway."

    mf "After all, when you’ve got young kids, running these things at the same time tends to be a hard thing to do."

    mf "So it’s a good thing that I can do this now."

    "So she’s… got a kid?"

    "I’m about to ask her more on the subject when she swears profusely, waving her hand in the air."
    hide  ch_owner_tired
    show  ch_owner_mean
    pc "W-what is it?"

    mf "Agh, dammit— "

    mf"I just-- It’s nothing, I just think one of those kids pulled one over on me."

    "She gestures at a coin in her hand. Sure enough, it’s oozing something brown and sticky; likely some chocolate candy."

    mf "Cheeky lil’ bastards…"

    "Huh."

    mf "Yeah? What is it?"

    pc "Nothing, I’m just… I’m surprised how foul your mouth tends to be."
    hide  ch_owner_mean
    show  ch_owner_smug
    mf "Why? Are you one of those kids who thinks anyone over the age of fifty isn’t allowed to swear unless they’re some grizzled ol’ mafia boss?"

    pc "Well, no, but..."

    pc "Not to fall in cliches, but I think it’s kind of… motherly, how you look after the arcade like this. Touching, even."

    pc "A-and my mom isn’t really… one that swears, so I guess it’s a little jarring."

    pc "But not a bad thing, or anything!"

    "Rosa laughs a little at that."
    hide  ch_owner_smug
    show  ch_owner_laugh
    mf "Motherly, huh..."

    mf "I mean, it’s not like someone like me would ever want to be a mother anyways. So I guess that this arcade is the replacement I’ve got to deal with."

    "...that’s not right, is it?"

    "Maybe I was recounting the conversation wrong in my head, but didn’t she say she had a kid a little bit ago?"

    "But… it feels like such a rude thing to bring up, so maybe I shouldn’t. I’m probably just overthinking this anyway, right?"

    "People don’t like to be called out when they contradict themself, after all..."

    menu:
        "Call her out on it":
            jump day3_co
        "Let it slide":
            jump day3_ls

label day3_co:
    scene bg_desk_day3
    show ch_owner_laugh
    "I stutter a glance over in her direction, but she doesn’t seem to be particularly bothered by the direction she’s taken the conversation."

    "I turn the words over in my mind a few times before daring to call out:"

    "So I can’t tell… do you have a kid or not?"
    hide ch_owner_laugh
    show ch_owner_mean
    "She doesn’t… freeze, per se, but her fingers fumble with the bills she’s counting. It’s a small enough hiccup that if I hadn’t been paying close attention, I don’t think I would’ve caught sight of it."

    mf "Isn’t that a little rude to ask, kid?"

    pc "If you don’t want to talk about it, that’s fine. You just contradicted yourself, so… I was a little confused."

    mf "…"

    mf "Well, good on you for calling me out on it, huh!"

    mf "In that case, lemme ask you another thing:"

    mf "What do you think it would make more sense for me to hide? The fact that I’ve had a kid, or the fact that I never had one?"

    mf "Either could be an ample source of shame. Either could be proof that I’m incompetant as a person, if you look too hard."

    mf "Or maybe I’m just giving you a tough time. That’s totally the sort of person I am, right?"

    mf "Must grind your gears, having to call me out. Piss you off a little bit, maybe."

    pc "I don’t think it matters, actually."
    hide ch_owner_mean
    show ch_owner_neutral
    "To her credit, Rosa at least looks surprised."

    pc "Whatever your ‘truth’ is… you’re not interested in what you actually say, right? It’s a little more messed up than that."

    mf "…"
    hide ch_owner_neutral
    show ch_owner_mean
    mf "You really like to just say shit, huh."

    pc "I’m sorry, w-was that a little too--"
    hide ch_owner_mean
    show ch_owner_laugh
    "Rosa cuts me off with a wave of her hand, laughing lightly."

    mf "No need to apologize. I’ll give you the same shtick that I did yesterday."

    mf "Make sure you show up tomorrow, right? Or else I’ll think you’re a ‘loser’ or whatever."

    mf "I need to chew on some stuff, now that I realize that you have some balls, and I think you do, too."

    "Thus saying so, Rosa makes a shooing motion with her hands. Obediently, I leave the arcade."

    "I hope she’ll actually be here tomorrow..."

    jump day3_end

label day3_ls:
    scene bg_desk_day3
    show ch_owner_laugh
    "I opt not to press any further. It’s not my business, nor should it be; this woman has offered me nothing but kindness. Isn’t privacy the smallest kindness that I could grant her?"

    "There are a few awkward moments of silence as I flounder with what to say before Rosa mutters something under her breath."
    hide ch_owner_laugh
    show ch_owner_mean
    mf "So you’re that sort of a coward too, huh…"

    pc "I’m… sorry?"

    mf "Oh, nothing, nothing. Listen, kiddo."

    mf "You’ve offered me a great deal of entertainment, but I think it’d be in your best interests to hang out with more interesting people from now on, alright? And not in the arcade. You really should be expanding your range of entertainment; experience things that you hadn’t really had a chance to beforehand."

    pc "It’s fine! I really enjoy talking with y--"

    mf "That wasn’t a suggestion."

    "I swallow thickly under her gaze, feeling somehow as if I’ve messed up very, very seriously."

    "Nodding politely, I duck my head and head out of the arcade."

    "I don’t think I’ll come here again; at least, not tomorrow."

    jump day3_end2

label day3_end:
    scene bg_black
    "{cps=25}2 days remain{/cps}"
    jump day4_start

label day3_end2:
    scene bg_black
    "{cps=25}2 days remain{/cps}"
    jump day4_end

label day4_start:
        scene bg_newsroom
        show ch_nm_frown
        play music "audio/newssong.ogg" fadeout 1

nm " It’s less than 48 hours till it’s over, right? I don’t know about you all, but…"

nm " I’m surprisingly… calm about this whole matter. For a while, I was incredibly stressed over the things I’d done."

nm " Or what I didn’t do, or if I made the right choice… which makes what I said yesterday pretty hypocritical, right?"

nm " But I think what I was so concerned about was what those things said about me, as a person. About what sort of ‘truth’ they were revealing about me, as if I was so concerned about whether or not people knew what the ‘real’ me really was."

nm " What I’ve realized is that the only person who has to be content with my actions is me, because I’m the only one who has to spend the rest of my life with me."

nm " So that begs the question; what does it mean for you to be alright with yourself? Have you been someone you - and I do mean you, not someone else - is proud of?"


if route == "hb":
    jump day4_hb
elif route == "gg":
    jump day4_gg
elif route == "mf":
    jump day4_mf
    return

label day4_mf:

    scene bg_desk_day1

" Rosa isn’t at the counter when I first walk in today. In her place is a handmade sign with an amount of glitter that’s comparable to the avalanche that was on her nametag. There’s the words “FREE 4 ALL, JUST DONT BREAK ANYTHING >>>:((” scrawled across it in sharpie."

" I’m tempted to leave right then and there, maybe cut my losses and cash in on some tooth rotting smoothies since I don’t need to worry about my health anymore, when I hear a firm “a-hem” from behind me."
show ch_owner_neutral
mf " Don’t think you could get rid of me that easily, champ. "

" I come closer and notice that she’s holding a lit cigarette in her hand. The smell makes my nose wrinkle instinctively, and she laughs."

mf " C’mon, let’s go inside. That’ll air out the smell."

pc " No… no I don’t think it will, actually."

mf " Haha oh noooo you got me. Here I was so confident my dastardly plan was foolproof."

" She delivers the line in complete monotone, but there’s still a smirk planted firmly on her face."

" Nonetheless, she walks into the arcade without looking to see if I follow or not; so of course, I do, casting a wary glance at the ‘no smoking’ sign that’s tacked up over the entrance."

" She doesn’t go very far in, and we sit at the cleanest table available under the fluorescent lights."

" Even then, I find myself brushing off crumbs as I make my way into the seat. We sit at opposite ends of the table, like a criminal and their interrogator, though as for who fills what role, I really wouldn’t be able to say."

mf " So."

pc " S-so."

mf " You had time to chew on stuff last night, so now’s your chance to ask whatever question you’d like."

mf " I’ve mentally prepared myself, so go ahead!"

pc " D… do you want me to just. Psychoanalyze you?"

mf " Why not? It’ll be fun."
mf " We can make it an, uh."

" She pauses, and I wonder if she’s trying to figure out my gender."

mf " ...friends’ night!"

pc " Yeah, haha…"

" We lapse into awkward silence, and I tease the charm I have attached to my jacket as I try to fight down the growing anxiety within me."

" I guess… if this is what she wants, then who am I to refuse, right?"

pc " I’m going to ask you this, because I don’t… I think you’d take it more personally if I didn’t ask this than if I did."

mf " Shoot, kid."
pc " Why do you seem to enjoy lying so much?"

pc " Maybe I’m reading this wrong, but…"

pc " You lie, and I notice, and I call you out on it. And you seem like you’d get upset if I didn’t, but I don’t even… really get why you lie in the first place."

" Rosa takes a moment of pause at that, pulling at her lip with yellowed teeth as she contemplates me for a second. I resist the urge to shudder underneath her gaze."

mf " Lemme tell you a lil’ tip I’ve learned over the years, kid."

" Rosa puts her hands out to the side as if she’s measuring a fish at the market, her cigarette ggburning out between her fingers."

mf " Lying is a two-way street. You need someone to tell the lie, and someone to accept the lie."

mf " Sure, there’s all that BS involved with lying to oneself, but that’s not what I’m talking about, ‘lright? I’m talking about an exchange of ideals, real or fake."

mf " Everyone wants to accept lies, if they think it’ll benefit them and won’t hurt anyone else in the long run. Doesn’t mean it smarts any less when you know something was a lie."

mf " So every lie has a payment: the truth of the matter. So here’s your due."

" She inhales deeply, crossing her arms."

mf " I’m a normal worker. I hate my job and when I go home, my feet hurt."

mf " I come back to a fridge full of beer and I’ve been tired for a really long time."

mf " “Before the world was announced to end?” Oh, long before that. But that’s fine, I think."

mf " My own personal happiness doesn’t really matter. Why do you think I’m runngging an arcade when I should be enjoying these last few days of my life? Seems kind of stupid, don’t you think?"

mf " But I don't care, not exactly. I can’t even really say that I enjoy seeing people being happy here. I told myself for a while that I do, but it’s probably not true anymore. The only thing keeping me here is the fact that the longer I work here, the longer I can stave off any guilt I feel."

mf " So in the end, it’s my son’s fault. Because he died, and I’m still here."

mf " ...so no matter what, I was telling the truth yesterday, right? If you really think about it. ‘Had’ a kid, ‘have’ a kid, it’s all semantics."

" With that, she leans back and throws her hands into her pockets."

mf " So how’s that. Are you alright with that sort of ‘payment’?"

pc " No, I think that’s all kind of… BS, honestly."

" Rosa startles, gaze stuttering over my face before she glances behind her as if she’s making sure it wasn’t someone else she was hearing."

" There's something oddly satisfying in seeing her taken genuinely off guard, in a way that’s different than when I merely startled her with cheap potshot comments."

pc " I don’t… I don’t know what happened with you and your son. I don’t think it’s my business to know, really."

pc " But using that as an excuse for what you’re doing now, how you’re feeling now… do you not see the flaws in that yourself?"

mf " …"

mf " ...that’s kinda cheeky of you to say that, kid. And I’m not sure I mean that as a compliment."

pc " ...I’m sorry, it was a bit out of line for me to--"

mf " No, I’m not pissed at you or anything. Just thinking, now."

mf " I’m sure other people would be, though."

" She just… sits there, for a bit, while I find my cheeks growing ever flushed as my anxiety coils up within me, ringing over and over like the muffled tongue of a bell."

" It’s only as she sighs and rubs her hands through her hair that I have the courage to blink and pull myself up properly, trying to find the same rush of courage that I had felt when throwing my words haphazardly in front of her."

mf " We’ll talk again tomorrow, alright?"

mf " The deal is, if you don’t die, and I don’t die, then we can speak again."

mf " That’s fair, right?"

" R… right."
hide ch_owner_neutral
" With that, she nods firmly, and I watch her head further into the arcade, likely to usher everyone out as she closes for the day."

" I don’t wait to see it happen, and leave as well."
scene bg_black
" I… have no choice but to see her tomorrow, right?"
jump day4_end

label day4_gg:
    scene bg_long_day4
    show ch_gg_neutral
" When I walk into the arcade and see Jade leaning against the wall, I begin waving excitedly at her almost immediately, grin wide and welcoming."

" In a worst case scenario, I expected her to scowl and run away. In a best case one, I expected her to run over and hug me. What I don’t expect is her marching over to me angrily, frown growing as she crosses her arms in front of me."

gg " We need to talk."

pc " O… kay?"

gg " P-privately."

pc " Yeah, sure where do you want to-- Oh, okay."

" Jade turns on her heel and begins making her way over to a darker corner of the arcade before I’ve even finished speaking, and I dog behind her obediently. "

" When she spins around to face me again, there’s something in her expression that’s seething."

gg " You need to leave me alone."

pc " Huh?"

pc " That’s not what I was expecting-- I mean, uh."

pc " Did I… do something to hurt you?"

gg " No, no, you’re-- You didn’t do anything."

gg " Or rather, you’re doing too much. It’s just--"

gg " Ugh."

" Jade pinches the bridge of her nose, and I try prodding further."

pc " Hey, if you need anything, I’m here, alright?"

pc " I get… uh, the end of the world is. Kinda stressful for everyone involved."

pc " And I don’t say this to sound obnoxious or conceited, but I’m really uh. Not that afraid about dying, haha. So if you need somewhere to explode, I can be a shoulder to lean on or whatever."

gg " No, that’s not it."

gg " That’s kinda creepy, but it’s not it."

pc " Then what’s it?"

gg " You can’t just--"

pc " You need to tell me what’s wrong for me to help."

gg " You’re so persistent, it makes me sick."

pc " I-- I-I can’t tell if that’s a bad thing or not, but I really just want to help--"

gg " Ugh! Why won’t you just abandon me--"

" Jade cuts herself off as her voice begins to rise in both intensity and volume, teeth worrying her bottom lip. She glances around nervously, as if to make sure that no one else had heard, before staring back at me as if I were some sort of grand decider of her fate."

" Maybe, in her mind, I am. The thought that someone would try and place that sort of responsibility on anyone, let alone me, makes my stomach turn."

pc " Why would I?"

pc " That seems like an excessively cruel and dramatic, especially at the end of the world. "

" Somehow, my statements only seem to provoke her more, her frustration quickly mounting."

gg " Because that’s what everyone else does, isn’t it?"

gg " If you’re just stringing me along because you think it’s fun to screw with someone’s feelings, then I’m sick of it! I’m tired of it and I’d rather you be honest with me now so I can rebound by tomorrow then have the last thought on my mind be how angry I am at myself for falling for this shit!"

gg " The first day, I could believe. Alright. Whatever. Maybe you’re one of those people who gets off doing random acts of kindness."

gg " Second day, okay. Pushing it, but that’s fine, too. You just didn’t know me super well yet, needed to realize how much I sucked before leaving."

gg " Third day was ridiculous. I couldn’t understand why you hadn’t-- why you didn’t leave. You should have left, after getting to know me, and after that, I was like “what the hell is wrong with you?” and decided to take matters into my own hands because at least then, I could believe that I had cut the connection off myself instead of you just tossing me to the side eventually."

gg " But you didn’t even leave then. Which means that you’re just lying to me through your teeth and this entire time you’ve been pretending, stringing me along because you wouldn’t be here otherwise."

gg " It’s not funny anymore."

" Exhausted, she exhales and leans back onto one of the arcade machines, the sweat on her skin apparent in the fluorescent light. "

pc " Jade…"

gg " Stop. I don’t-- If you’re gonna waste more time on me because you think I’m pathetic then you need to leave. "

pc " Well, uh…"

pc " I don’t mean this in a mean way, but you’re completely wrong, you know."

pc " I’m… I’m kind of ashamed to say it, but I really had no way you felt this way. I’m sorry about that. "

pc " I really enjoy hanging out with you. I don’t think I’d be doing anything else at the end of the world, given the choice."

pc " I mean, it’s not like I have the time to make any other friends--"

gg " Oh."

" There’s something in her mind that just… clicks, there. Something that elicits such a sigh of understanding from her that there’s something big I’m afraid I’ve missed."

gg " So you’re just hanging out with me because you’re as pathetic as me."

gg " You’re just hanging out with me because you don’t have any other friends, and I’m a good bottom o’ the barrel pick."

gg " Ha."

" There’s no humor in her voice, but she smiles anyway, gaze tracing circles in the ground as  she comes to some grand conclusion before looking back up at me with a look that I think is supposed to be cruel."

gg " Whatever. It’s not like I really wanted to be around you, anyway."

" She scoffs and flips her hair with such a violent pointedness that I’m taken aback a bit as she turns away, heels snapping against the carpeted floor."
hide ch_gg_neutral
" Despite her words, I feel more sorry for her than I feel hurt."

" I… really hope I’ll get to see her tomorrow, one last time."

jump day4_end

label day4_hb:
    scene bg_black
    "I’m afraid that I won’t see Herbert when I walk in the next day, but I find him scuffing his feet by the entrance, trying his damnedest to look disinterested with everything around him even as M talks his ear off."
    show ch_hb_neutral at left
    show ch_owner_neutral at right
    mf "Look, you can stay if you wanna stay or you can go if you wanna go but you need to make up your mind, champ. I can’t just have you loitering around here and pissin’ off custo--"
    hb "PRO!"
    "He perks up as he sees me approach before coughing in his hand like he’s embarrassed, rolling his shoulders back and glancing off to the side."
    hb "I-I mean, PRO. Hey. ‘bout time your sorry ass showed up."
    mf "If they’re the reason that you were being such a brat, then yes, I agree; it is about time they showed up."
    mf "Now come along you two. Go in and do some ‘gaming’ or whatever it is you kids like to waste your time doing during the end of the world."
    hb "You say this like you’re not running an arcade."
    mf "What’d I say? Scram!"
    "With that, M ushers us inside, making shooing noises with one hand and reaching for the pack of M*rlboro’s in her breast pocket with her other."
    "If nothing else, Herbert seems… out of it. For a second the flustered expression on his face makes me concerned, but he just spins around once he’s dragged me to a quiet enough corner of the arcade, plopping himself down on one of the seats. I sit next to him."
    hb "We need to. Uh. Talk."
    pc "Convenient that we’re already doing that, right now."
    hb "No, I-I mean-- About yesterday. Why…"
    hb "Why didn’t you leave me there? You probably should’ve done that."
    pc "I mean, I left to go home afterwards, so--"
    hide ch_hb_neutral
    show ch_hb_guilty at left
    hb "That’s not what I mean, and you know it! Ugh, I frickin’--"
    "Herbert groans and bites his thumbnail, eyes darting from side to side like he’s afraid of… something."
    hb "I’m gonna say two things, alright?"
    hb "One: I’m. I’m, uh."
    hb "…"
    hide ch_hb_guilty
    show ch_hb_embarrassed at left
    hb "I’msorryforblowingyouoffokthing number TWO."
    hb "What you did yesterday was dumb. And cringey."
    pc "I know, I’m disappointed in the lack of creativity in my insults as well."
    hb "What? No, that’s not--"
    "Herbert shakes his head."
    hide ch_hb_embarrassed
    show ch_hb_guilty at left
    hb "I just don’t think… I think what you did was a waste of time."
    hb "Especially since you beat me. They were all so happy about it."
    pc "Really? Why do they hate you so much?"
    hb "W-well, hate is a strong word--"
    pc "It’s your word, not mine."
    hb "But I’m sure you can figure, right? Since it’s me we’re talking about, if I’ve got nothing else good about me beyond gaming, and I can’t even do that--"
    pc "Well, who said that?"
    hb "Come on, grow a pair. Can you stop being so painfully dense?"
    pc "No, ‘cause right now, I think you just want me to confirm how you feel about yourself. So you can feel justified about that."
    hide ch_hb_neutral
    show ch_hb_angry at left
    "Herbert blinks and recoils like I’ve actually insulted him or something."
    hb "That’s…"
    hb "That’s just dumb! Why would I ever wanna hear someone insult me?"
    pc "I dunno. Either you’re a masochist or something worse."
    hb "Y-you’re the bad one here! Frickin, posing questions back at me as if that’ll make a difference--"
    pc "A difference for what? Why you don’t think you’re worth anything without gaming?"
    hb "I never said--"
    pc "Why do you think that?"
    hb "Cause when I go to sleep, I--"
    hb "Herbert cuts himself off, scowling."
    pc "You have nightmares? That’s nothing to be ashamed of. I get ggthe ol’ “teeth falling out of my mouth” one all the time. It definitely sucks, but it’s not--"
    hb "No. Shut up."
    pc "…"
    hb "…"
    pc "…"
    hb "…"
    pc "…"
    hb "…"
    pc "…"
    hide ch_hb_angry
    show ch_hb_guilty at left
    hb "...you can breathe, jeez."
    "I let out the breath I had been holding."
    hb "If you laugh, I’ll kill you, okay?"
    pc "Alright, duly noted, edgelor--"
    hb "In my dreams, when I look in a mirror or some shit, I see… myself. When I was a kid-- Like, nine, ten years old."
    hb "And he- I- whoever it is says to me, h-he says, uhm."
    hb "“...why are you this way? What did I do to become like you?”"
    hb "“I’m really scared to turn into you.”"
    hide ch_hb_guilty
    show ch_hb_tears at left
    hb "...that’s what he says."
    "Herbert sits there for a moment, pulling at his cuticles and staring at the shapes in the floor as if they’re who he’s speaking to instead of me."
    "I can’t do anything but gape for a moment, flustered as I fumble for words. All that I can force out, though, is an awkward:"
    pc "I’m… sorry?"
    hb "No, don’t, don’t frickin-- Don’t apologize."
    "Herbert pulls off his hat, toying at it with his hands instead of picking at his skin. His fingers tease the ends of his hat, fraying the already worn edges further."
    hb "That makes it weirder. I don’t want you to say sorry or any shit, I guess. I don’t want to spend my last full day alive feeling like some sort of loser."
    pc "Then… what do you want, if you don’t mind my asking?"
    pc "I can’t help if you don’t speak."
    "Herbert lets out a humorless snort."
    hb "That sure is the question, huh…"
    hb "...I don’t know. I guess…"
    hb "Part of me wants to ask you to just come out and tell me something like “it’s all going to be okay”, or “you’re not someone that your younger self would be ashamed of”, nothing cliche like that."
    hb "I don’t really like that sort of cheap positive talk. I’m sure people mean well when they say that shit, but it just comes off as generic feel good stuff that they just say because they know it’s what you want to hear."
    hb "Especially with the world ending tomorrow. People can say whatever they want to make you feel better and then give themselves a pat on the back after the fact like it means they’re a good person now, ‘cause they gave you ‘peace of mind’ that they don’t actually need to follow up on."
    hb "They can make promises because they don’t need to keep them. So that means I won’t believe that they’d keep them in any other scenario."
    pc "...that’s an awfully convoluted and pretentious way of saying ‘I don’t want to be comforted’."
    "Herbert startles a bit, caught off guard in the middle of his emo boy reverie."
    hb "I-I’m not--"
    pc "Have you ever considered that maybe now’s the perfect time for people to be most honest about how they feel?"
    pc "There’s no skin off my back if I told you that you suck. I didn’t need to spend time with you these last few days. I certainly had ample reason yesterday."
    pc "I didn’t even know your name until a few days ago. And maybe that means I don’t know you perfectly, and I don’t know you well enough to tell you whether you’re good or not, mostly ‘cause I don’t really know who qualifies for that label."
    pc "But if nothing else, you should take comfort in the fact that I made a conscious choice to hang out with you these last few days."
    hb "…"
    hb "…maybe you’re just doing that because you’re too lame to have people to hang out with yourself."
    pc "Huh, guess I can’t argue with that."
    "Saying so, I lift myself off from the cushioned arcade seat, wincing as it makes a noise too squishy to mean it’s clean."
    pc "Well, see ya tomorrow."
    hb "H-huh? You mean, you’re leaving?"
    pc "I mean, I’m just tired."
    pc "But more importantly, I think you are too. There’s no point in us milling around if you haven’t chewed on the words you need to chew on, right?"
    hb "…"
    hb "When did you become so…"
    "Herbert shakes his head."
    hb "N-nevermind. I’ll see you tomorrow, here, then."
    hb "If you break that promise, I’ll for real kill you. Meteor won’t even have a chance to."
    pc "Haha. I look forward to that, then."





label day4_end:
    scene bg_black
    "{cps=25}1 day remains{/cps}"
    jump day5_start

label day5_start:
    scene bg_newsroom
    show ch_nm_frown
    play music "audio/newssong.ogg" fadeout 1
