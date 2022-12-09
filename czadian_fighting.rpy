default enemy_czadian = 1000
default enemy_max_czadian = 1000

screen czadian_fight():
    vbox:
        xalign .9
        yalign .05
        text _("Marycha") outlines [(2, "#00ff6a")]
        text _("[life]/[life_max] HP") outlines [(2, "#88ff00")]
    vbox:
        xalign .75
        yalign .05
        text _("Czadian") outlines [(2, "#ea00ff")]
        text _("[enemy_czadian]/[enemy_max_czadian] HP") outlines [(2, "#6200ff")]

label czadian_fight:

    show screen czadian_fight
    "Marysia wyzywa Cię do walki!"

label attack_czadian:

    $ defense_czadian = renpy.random.choice(['def_low', 'def_medium', 'def_high'])

    if life <= 0:

        jump fight_lost_czadian

    elif enemy_czadian <= 0:

        jump fight_won_czadian

    else:

        if defense_czadian == "def_low":

            "Przeciwnik jest wybity z rytmu!"

        elif defense_czadian == "def_medium":

            "Twój przeciwnik skupia się na obronie!"

        elif defense_czadian == "def_high":

            "Twój przeciwnik przyjął pozycję obronną!"

        menu:

            "Atakuj!"

            "Horny-Diva":

                if defense_czadian == "def_low":

                    $ enemy_czadian -= 25

                    "Zadałeś 25 damage!"

                    jump defense_czadian

                elif defense_czadian == "def_medium":

                    $ enemy_czadian -= 10

                    "Zadałeś 10 damage!"

                    jump defense_czadian

                elif defense_czadian == "def_high":

                    "Przeciwnik uniknął ataku!"

                    jump defense_czadian

            "Domination Dive":

                if defense_czadian == "def_low":

                    $ enemy_czadian -= 25

                    "Zadałeś 25 damage!"

                    jump defense_czadian

                elif defense_czadian == "def_medium":

                    $ enemy_czadian -= 10

                    "Zadałeś 10 damage!"

                    jump defense_czadian

                elif defense_czadian == "def_high":

                    "Przeciwnik uniknął ataku!"

                    jump defense_czadian




label defense_czadian:

    $ attack_czadian = renpy.random.choice(['atk_low', 'atk_medium', 'atk_high'])

    if life <= 0:

        jump fight_lost_czadian

    elif enemy_czadian <= 0:

        jump fight_won_czadian

    else:

        if attack_czadian == "atk_low":

            "Moc GigaChada aktywowana! Unikniesz następnego ataku przeciwnika, tak jak unikasz podludzi!"

        elif attack_czadian == "atk_medium":

            "Czadian przygotowuje atak"

        elif attack_czadian == "atk_high":

            "Czadian przygotowuje atak"


        menu:

            "Przeciwnik jest gotowy do ataku!"

            "Próbuj wykonać unik!":

                if attack_czadian == "atk_medium":

                    Chadian "ORAORAORA!"
                    $ life -= 250
                    "Chadian zadał 250 damage!"

                    jump attack_czadian

                elif attack_czadian == "atk_high":

                    Chadian "ORAORAORA!"
                    $ life -= 100
                    "Chadian zadał 100 damage!"
                    
                    jump attack_czadian

                else:

                    "Uniknąłeś ataku! Moc gigachada nie pozwala ci zostać dotkniętym przez podczłowieka!"

                    jump attack_czadian


label fight_lost_czadian:
    
    hide screen czadian_fight
    $ enemy_czadian = enemy_max_czadian
    $ life = life_max

    jump przegrane_czadian

label fight_won_czadian:

    hide screen czadian_fight
    $ enemy_czadian = enemy_max_czadian
    $ life = life_max

    jump wygrane_czadian