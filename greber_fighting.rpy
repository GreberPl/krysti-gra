default life = 100
default life_max = 100
default enemy = 100
default enemy_max = 100

screen stando_fight():
    vbox:
        xalign .9
        yalign .05
        text _("Ty") outlines [(2, "#00ff6a")]
        text _("[life]/[life_max] HP") outlines [(2, "#88ff00")]
    vbox:
        xalign .75
        yalign .05
        text _("[Stando]") outlines [(2, "#ea00ff")]
        text _("[enemy]/[enemy_max] HP") outlines [(2, "#6200ff")]

label stando_fight:

    show screen stando_fight
    "Marysia wyzywa Cię do walki!"

label attack:

    $ defense = renpy.random.choice(['def_low', 'def_medium', 'def_high'])

    if life <= 0:

        jump fight_lost

    elif enemy <= 0:

        jump fight_won

    else:

        if defense == "def_low":

            "Przeciwnik jest wybity z rytmu!"

        elif defense == "def_medium":

            "Twój przeciwnik skupia się na obronie!"

        elif defense == "def_high":

            "Twój przeciwnik przyjął pozycję obronną!"

        menu:

            "Atakuj!"

            "Loser Punch":

                if defense == "def_low":

                    $ enemy -= 25

                    "Zadałeś 25 damage!"

                    jump defense

                elif defense == "def_medium":

                    $ enemy -= 10

                    "Zadałeś 10 damage!"

                    jump defense

                elif defense == "def_high":

                    "Przeciwnik uniknął ataku!"

                    jump defense

            "Chastity belt":

                if defense == "def_low":

                    $ enemy -= 25

                    "Zadałeś 25 damage!"

                    jump defense

                elif defense == "def_medium":

                    $ enemy -= 10

                    "Zadałeś 10 damage!"

                    jump defense

                elif defense == "def_high":

                    "Przeciwnik uniknął ataku!"

                    jump defense

            "Simp Whine":

                if defense == "def_low":

                    $ enemy -= 25

                    "Zadałeś 25 damage!"

                    jump defense

                elif defense == "def_medium":

                    $ enemy -= 10

                    "Zadałeś 10 damage!"

                    jump defense

                elif defense == "def_high":

                    "Przeciwnik uniknął ataku!"

                    jump defense

            "Negative-Chad Cannon":

                if defense == "def_low":

                    $ enemy -= 25

                    "Zadałeś 25 damage!"

                    jump defense

                elif defense == "def_medium":

                    $ enemy -= 10

                    "Zadałeś 10 damage!"

                    jump defense

                elif defense == "def_high":

                    "Przeciwnik uniknął ataku!"

                    jump defense




label defense:

    $ attack = renpy.random.choice(['atk_low', 'atk_medium', 'atk_high'])

    if life <= 0:

        jump fight_lost

    elif enemy <= 0:

        jump fight_won

    else:

        if attack == "atk_low":

            "Moc piwniczaka aktywowana! Unikniesz następnego ataku przeciwnika, tak jak unikasz kobiet!"

        elif attack == "atk_medium":

            "Marysia przygotowuje atak Domination Dive"

        elif attack == "atk_high":

            "Marysia przygotowuje atak Horny-Diva"


        menu:

            "Przeciwnik jest gotowy do ataku!"

            "Próbuj wykonać unik!":

                if attack == "atk_medium":

                    Marysia "ARAARAARAARAARAARAARAARAARAARAARA!"
                    $ life -= 25
                    "Marysia zadała 25 damage!"

                    jump attack

                elif attack == "atk_high":

                    Marysia "ARAARAARAARAARAARAARAARAARAARAARA!"
                    $ life -= 10
                    "Marysia zadała 10 damage!"
                    
                    jump attack

                else:

                    "Uniknąłeś ataku! Moc prawiczka nie pozwala ci zostać dotkniętym przez kobietę!"

                    jump attack


label fight_lost:
    
    "Przegrałeś z kobietą, nic nowego, przegryw to przegryw"
    hide screen stando_fight
    $ enemy = enemy_max
    $ life = life_max

    jump przegrane

label fight_won:

    "Nie wiem jakim cudem, ale wygrałeś!"
    hide screen stando_fight
    $ enemy = enemy_max
    $ life = life_max

    jump wygrane