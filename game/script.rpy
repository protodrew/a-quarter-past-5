# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pc = Character("Player", color="#d44e8e")
define gg = Character("Goth Girl", color="#4f12b2")
define hb = Character("Hat Boy", color="#f45578")
define mf = Character("Milf", color="#37c1d3")
define nm = Character("News", color="#60d67b")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_newsroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ch_nm_smile

    nm "This is Channel 99 and you are tuning in to this mornings news"

    show ch_nm_frown

    nm "Unfortunately good news has been sparce this week as the omega meteor continues its descent towards the earth."

    nm "Riots have broken out and the world seems more grim than ever"

    nm "Viewers are encouraged to spend these last few days enjoying themselves and spending time with loved ones."

    show bg_5days

    "who would you like to spend your day with?"

    menu:
        "GG.":
            jump choice1_gg
        "HB.":
            jump choice1_hb
        "M.":
            jump choice1_m

label choice1_gg:
    scene bg_corner_day1
    show ch_gg_surprised
    gg "Yay I'm so glad you decided to hang out with me!"

    jump choice1_done

label choice1_hb:
    scene bg_corner_day1
    show ch_hb_smug
    hb "Come back to lose another round of pong huh?"

    jump choice1_done

label choice1_m:
    scene bg_desk_day1
    show ch_milf_smug
    mf "Hello darling, I do hope you are enjoying the arcade."

    jump choice1_done

label choice1_done:
    scene bg_corner_day1
    "This is a successful test of choices"


    return
