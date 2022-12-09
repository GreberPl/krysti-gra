
define Marysia = Character("Marysia", image="marysia", color="#51ff00")
define Krystian = Character("Krystian", color="#f70000")
define narrator = Character("narrator", color= "#fffb00ff") 
define Sayori = Character ("Sayori", image="Sayori")
define Chadian = Character ("Czadian", image="Chadian", Color="#4c00ffff")
define Nikt = Character (" ", Color="#0000")
define Wuja = Character ("Wujek", image="wuja", color="#00f7ffff")
default Stando = "Stend" 
default EndingAnimu = "Endingani2"


label start:
"Witaj Podróżniku"
play music "audio/bgm_pierwszy.mp3" fadein 1.0 volume 0.5
"Jesteś Przegrywem? Szukasz Miłości? Źle trafiłeś ale pobawie się twoimi uczuciami"
scene bg class
        
"Ta którą jako ci zaprezentuje to Marysia chodzicie razem do klasy zapisała się w tym roku. Dla świętego spokoju uznajmy że masz na imię Krystian"
show marysia horny 
Marysia "H-hejj"
Marysia "Mam 17 lat"
Marysia "Lubię piłkę nożną i anime"
Marysia "Lubisz anime?"
menu:
  "lubisz anime?"
  "tak":
    $EndingAnimu = "Bezpieczny"
    jump pytanieAnimeTak
  "nie":
    $EndingAnimu = "Niebez"
    jump pytanieAnimeNie




label pytanieAnimeTak:
    hide marysia horny 
    "wiedziałem że jesteś popsuty, ale że aż tak. Może wrócę do bycia narratorrem"
    show marysia horny
Marysia "Może obejrzymy jak. . ." 
stop music
play sound "audio/dzwonek-szkolny.mp3"  volume 0.15 fadein 1.0


"w tym momencie zadzwonił dzwonek"
stop sound
Krystian "poczeka..."
Marysia "pogadamy później"
"przerwała mu marysia"
". . ."
"na lekcji marysia poczuła się źle i już nie pogadali później"
scene bg room2
menu:
    "Napisać do niej?"
    "Tak":
        jump PisanieTakv2
    "Nie":
        jump bieganie

label pytanieAnimeNie:
    "może masz mózg"
Marysia "No spoko nie każdy musi lubić :3"
Marysia "Spo"
stop music
play sound "audio/dzwonek-szkolny.mp3" volume 0.25
"w tym momencie zadzwonił dzwonek"
stop sound
play music "audio/bgm_pierwszy.mp3" fadein 1.0 volume 0.5
Krystian "Pogadajmy później Oki?"
Marysia "oki"
"na lekcji marysia poczuła się źle i już nie pogadali później"
scene bg room2
menu:
    "Napisać do niej?"
    "Tak":
        jump PisanieTakv2
    "Nie":
        jump bieganie

label PisanieTakv2:
    
menu:
    "Jak zaczniesz rozmowe?"
    "Ruchasz się czy trzeba z tobą chodzić":
        if EndingAnimu == "Bezpieczny":
            Marysia "yyyy XD? A tak wogóle co tam?"
            jump Bezpieczny 
        else:
            play sound "audio/sfx_koniecgry.mp3"  volume 1.0
            "Sheeeeeeheeeer zostałeś zablokowany XDDDD Koniec gry worst Ending "
            stop sound
            " "
            return
    "Hejka":
        Marysia "Hej co tam"
        jump Bezpieczny

label Bezpieczny:
    
Krystian "Całkiem git a tam?"
Marysia "Dobrze słyszałeś, że Sayori umarła?"
"W tym momencie Krystian się zasmucił"
Krystian "Szkoda byłem jej fanką"
"mimo że krystian udawał niezasmuconego w sercu płakał i popadł w depresje"
menu :
    "Co robisz"
    "Dołączasz do idolki z powodu depresji uwu":
        play sound "audio/sfx_koniecgry.mp3"  volume 1.0
        "Krystian Umiera na pogrzeb przybywa cała klasa dzięki niemu nie ma sprawdzianu z matmy. Wreszcie się przydał~Powiedzieli niektórzy"
        play sound "audio/sfx_koniecgry.mp3"  volume 1.0
        "Average 12 ending"
        return
    "Miej wywalone":
        "Żyjesz dalej a rozmowa trwa dalej"
        Marysia "Szkoda mi cię idziemy na kolacje jutro?"
menu:
        "Zgadzasz się? "
        "Tak":
            jump Kolacja
        "Nie":
            "kurwa zły wybór"
            jump PisanieTakv2
          


label bieganie:
scene bg park
show Sayori
Krystian "Co tu się mogło stać. A ona nie żyje. Jaka szkoda byłem jej fanatykiem"
menu :
    "Co robisz"
    "Zabierasz ciało i przetrzymujesz je w domu":
        play sound "audio/sfx_koniecgry.mp3"  volume 1.0
        "Po tygodniu zaczynasz być piwniczakiem wychodzisz tylko po 18 gwałcić kobiety. Kacper Ending"
        return
    "Dzwonisz po policje":
        "Oskarżają cię o zabójstwo trafiasz do paki żadna cię nie chcę jak IRL. Jednak przychodzi do ciebie Neo z matrixa i oferuje dać ci tabletkę która cofnie cię w czasie co robisz "
menu:
        "co robisz"
        "Cofasz się do początku":
            jump start
        "nic(Sad Ending)":
            play sound "audio/sfx_koniecgry.mp3"  volume 1.0
            "Siedzisz tu na dożywociu umierasz w wieku 80 lat"
            stop sound
            return
            
label Kolacja:
scene bg burgerking
"Przychodzisz na Kolacje w najlepszej koszuli diversea po tacie jaką znalazłeś."
show marysia horny
"a tu taki Chuj ona w bluzie"
Marysia "na chuj się tak ubrałeś do burger kinga"
Krystian "robie to dla ciebie"
"Japierdole"
Marysia "miło"
Krystian "Co zamawiamy?"
Marysia "zastanawiam się pomiędzy King's Chimichurri Zestaw a Steakhouse Bacon King Zestaw Maxi. Pomożesz?"
menu:
    "Co wybierasz?"
    "Steakhouse Bacon King Zestaw Maxi":
        Marysia "dzięki krystian"
        $ Stando = "Steakhouse Bacon King"
    "King's Chimichurri Zestaw":
        Marysia "dzięki krystian też skłaniałam się ku temu"
        $ Stando = "King's Chimichurri"
    "i’ll have two number 9s, a number 9 large, a number 6 with extra dip, a number 7, two number 45s, one with cheese, and a large soda.":
        Marysia "O tym naprawde marzyłam "
        "Zostajecie parą gdy kończysz 20 lat pobieracie się a 4 lata później bierzecie ślub. Macie 4 dzieci w tym 3 w lodówce"
        play sound "audio/sfx_koniecgry.mp3"  volume 1.0
        "Happy Grox Ending"
        return
"Krystian zamówił to samo po odebraniu zasiedli do stolika i zaczeła się rozmowa" 
Krystian "Co sądzisz o kurwach?"  
Marysia "np. tede?"
Krystian "tak czy ty też jesteś fanką peji?"
Marysia "Tak jest moim Crushem ale moim top 2 jest Jonathan Joestar"
Krystian "Ty też lubisz JoJo?"
Marysia "YES!!!"
Krystian "Obejrzałaś juz nowe odcinki partu 6?"
Marysia "jeszcze nie"
Krystian "możemy razem u ciebie pooglądać"
Marysia "Jasne czemu Nie :3"
Krystian "to jedzmy szybko i choćmy"
"Po tych słowach poszli do domu Marysi"
jump dommarysi

label dommarysi:
scene bg room 
show marysia horny
Marysia "Krystian co robisz? To mój pokój"
Krystian "Sram na razie"
"Po chwili"
Marysia "To co oglądamy JoJo?"
Krystian "Jasne"
"Po Kilku chwilach"
". . ."
". . ."
". . ."
"Marysia otuliła go i zapytała"
Marysia"ruchasz się czy trzeba z tobą chodzić"
menu :
    "Co robisz"
    "Ruchasz":
        "Uprawiacie Stosunek przy JoJo"
        Marysia "Jesteś dobry"
        Krystian"Wiem, Do jutra"
        jump dzien3
    "Musi z tobą chodzić":
        Marysia "zostaniesz moim chłopakiem?"
menu:
    "Co robisz?"
    "Tak":
        "Zaczynacie z sobę chodzić"
        "Uprawiacie Stosunek przy JoJo"
        Marysia "Jesteś dobry"
        Krystian"Wiem, Do jutra"
        jump dzien3
    "Nie":
        play sound "audio/sfx_koniecgry.mp3"  volume 1.0
        "Marysia wyciąga nóż i zabija krystiego przetrzymuje go w lodówce"
        "Marysia zostaje piwniczanką i wychodzi tylko po 18 by gwałcić mężczyzn"
        play sound "audio/sfx_koniecgry.mp3"  volume 1.0
        "Divorced Kacper Ending"
        return
label dzien3:
scene bg class
show marysia horny 
Marysia "Patrz co zrobiłam z twoich resztek z kolacji i twoich plemników oraz 20 mg dicka Rasputina"
show minecraft
"Krystian wiedział co to za strzała to strzała z JOJO"
Krystian "Marysia? Czy ty to sobie wbiłaś?"
Marysia "Tak"
Krystian "Ho Ho, Podchodzisz do mnie?"
Marysia "Nie mogę ci zrobić epickiej lepy bez podejścia bliżej"
Marysia "ARA, ARA, ARA, ARA, ARA, ARA"
Marysia "..."
Marysia "! NANI!?"
Krystian "Nie spodziewałaś się tego to mój potężny stand, BRRRRRRAKAMONOGA!"
Marysia "I tak nie pokonasz mojego standa [Stando]"
"Krystian wiedział, że nie może jej uderzyć by nie być patologiczną rodziną musi unikać"
jump stando_fight

label przegrane:
"Imagine przegrać XDDDDDDDDDDDDDDDDD"
play audio "audio/clangberserk.mp3"
scene black
". . ."
scene bg piwnica
"Hey you are finaly awake"
Krystian "Wracaj do bycia narratorem nie tak sobie schizofrenie wyobrażałem"
"Nie a teraz oddawaj ciało"
show marysia horny
Krystian "Nieeeee..."
Nikt "Od teraz jesteś Marysią"
hide marysia horny
show gigachad 
Chadian "Siema Marycha"
Chadian "Wybierz Wypuszczasz mnie lub śmierć" 
Marysia "Zobaczymy czy dasz mi rade"
jump czadian_fight


label przegrane_czadian:
Krystian "Nie..."
jump wygrane_czadian

label wygrane_czadian:
Nikt "Czadian jest najpotężniejszą istotą żyjącą na ziemi nikt nawet ze Standem go nie powstrzyma"
Chadian "Marysio, WYBIERZ albo Jesteś moją służbą i zostajemy Panami tego świata lub ŚMIERĆ"
$ pisiont = renpy.random.choice (["Tak", "Nie"])
if pisiont == "Tak":
    Nikt "Marysia wybrała została służbą i dziewczyną Czad"
    Chadian "Dobry wybór"
    Nikt "..."
    scene bg zamek
    Nikt "Po 20 latach Chadian z marysią mieli pod sobą Całą Europe, Azje, Całą Oceanie, Afrykę Amerykę łacińską. Bronią się Ameryki północne i południowe"
    Nikt "Chadian z Marysią mają 8 Dzieci Każde z nich uczy się użytkowania Standa Każdy z nich ma potencjał na bycie silniejszym od CHADIANA"
    Nikt "Tym czasem w głowie Chadiana/Krystiana"
    Krystian "Heeeeey... Chadian, Pamiętasz Umowę? Został ci rok"
    Chadian "Rok to aż za dużo by zdobyć Reszte świata. Mam pod swoim władaniem 1000 użytkowników Standa"
    Krystian "Nie wątpie "
    Nikt "11 miesięcy Później"
    Chadian "Krystianie Zdobyłem cały świat Wygrałem"
    Chadian "Mam Propozycje"
    Chadian "To ciało mnie nie chcę"
    Chadian "Ja dam ci Życie oddając ci połowe naszego w pełni rozwiniętego Standa"
    Chadian "Zostało mi 12 lat życia"
    Chadian "Wiesz do Czego zmierzam"
    Krystian "Tak Wiem"
    Chadian "Czy chcesz się odrodzić?"
    menu:
        "Chcesz?"
        "Tak":
            Nikt "Rodzisz się, po 12 Latach wyprzedzasz ojca. 2 miesiące później Chadian Umiera i oddaje ci 2 część Standa. Maryasia dowiaduje się prawdy o Tobie"
            Nikt "Rządzisz światem przewyższasz Chadiana 10 krotnie"
            Nikt "Marysia Umiera 10 lat Po Chadianie"
            Nikt "Rozpoczyna się wojna Przez Bunt 1 z Braci"
            play sound "audio/sfx_koniecgry.mp3"  volume 1.0
            Nikt "The Real Ending"
            Nikt ".--. .- .-. - / ..--- / .. ... / -.-. --- -- .. -. --.?"
            jump DLC1
            return
        "Nie":
            Nikt "Chadian po 12 latach umiera i świat dzieli się na 4"
            Nikt "Każde państwo jest pośrednio zależne od Marysi"
            Nikt "W roku 2090 wybucha III wojna światowa"
            play sound "audio/sfx_koniecgry.mp3"  volume 1.0
            Nikt "Neutral Ending"
            return
        
elif pisiont == "Nie":
    Chadian "A więc wybrałaś"
    Marysia "Wkrótce dołącze do Krysiana"
    Nikt "Po czym zabił ją ale chwile przed śmiercią marysia dowiedziała się"
    Chadian "Krystian żyje"
    Nikt "Chadian miał 5 dzieci, zdobył pół świata"
    Nikt "2 pokolenie zdobyło resztę świata"
    Nikt "Krystian i Chadian umierają w roku 2035"
    play sound "audio/sfx_koniecgry.mp3"  volume 1.0
    Nikt "Załamana Marysia Ending"
    return


label wygrane:
Krystian "Nie chciałem tego robić Marysia"
"Powiedział Krystian łamiącym się głosem"
play audio "audio/clangberserk.mp3"
"Poczym Uderzył Marysie" 
scene black
"dwa tygodnie później"
scene bg statek
show marysia horny
Krystian "Cześć Marysiu zastanawiasz się pewnie gdzie jesteś."
Marysia "Nie zupełnie"
Krystian "Jak kurwa nie zupełnie"
Marysia "No nie jestem ślepa widzę, że na statku płyniemy. Ale gdzie płyniemy?"
Krystian "Płyniemy na floryde"
Krystian "Mój wujek Grzegorz ma bardzo ładną rakiete kosmiczną, która zabierze nas na księżyc."
Marysia "Po chuj mamy na księżyc?"
Krystian "Wujek mnie poprosił żebym przetestował rakiete bo zrobioną z samochodów."
Marysia "Co może pójść nie tak... Dobra dawaj"
"4 tygodnie później"
". . ."
". . ."
". . ."
". . ."
scene bg warsztat
show Wuja
show marysia horny
Wuja "Witajcie"
Marysia "Dzień dobry Jestem Marysia"
Wuja "Witaj Marysia"
Wuja "Jak wybieracie jeszcze dziś lot czy jutro lot?"
menu:
    "Co wybierasz?"
    "Dziś":
        jump lot
    "Jutro":
        "Marysia zaszeptała do ucha Krystiana"
        Marysia "Chodźmy we 2 do pokoju"
        Krystian "Dobrze"
        hide wuja 
        scene black
        "5 minut później"
        scene bg hotel
        show marysia horny
        Krystian "nie dokończyliśmy JoJo Jeszcze"
        Marysia "Netflix and Chill?"
        Krystian "Zawsze"
        "Uprawiacie stosunek przy JoJo"
        "po czym poszliści spać i jutro z rana byli gotowi na lot"
        jump lot
label lot:
scene bg warsztat
Wuja "Gotowi?"
Krystian "Tak"
Wuja "lece z wami"
Wuja "W środku rakiety nie potrzebujecie nic"
Marysia "dobrze"
Wuja "start za godzine"
"Godzine później"
Wuja "Start za"
Wuja "5"
Wuja "4"
Wuja "3"
Wuja "2"
Wuja "1"
Wuja "Start"
"Nie dokończony Ending"
"Webcomic is coming"
show black
". . ."
". . ."
". . ."
". . ."
". . ."
". . ."
jump DLC2


label DLC1  



label DLC2  
Nikt "Murzyn"



return
