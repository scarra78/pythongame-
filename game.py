import sys
from time import sleep
import random

loop = 0 # Increments by 1 when an area is completed. Game is completed and the ending sequence plays when loop == 4
answer = None #Answer to puzzles (does this need to be set to None here?)
finished_mountain = False #Set to True once a player has completeted an area, to prevent them returning to that area.
finished_swamp = False
finished_desert = False
finished_forest = False
game_loop = None
dead = False 

def typew(text):
     for c in text:         #for each char in line
         print(c, end="")   #print single chr
         sys.stdout.flush() #flush buffer
         sleep(0.00)        #time to make letters display

def main_room():
    global loop
    global finished_mountain
    global finished_swamp
    global finished_desert
    global finished_forest
    global dead

    while loop != 4 and dead == False:     # Runs while all rooms have not been completed and player is not dead
        
        ship_pic()# Display art

        uncompleted_areas = ["north", "south", "west"]  #generates a list of directions the module tracker is pointing to, based on whether the area has been completed
        if finished_mountain == True: uncompleted_areas.remove("north") #when an area is completed, remove it from the list
        if finished_swamp == True: uncompleted_areas.remove("south")
        if finished_forest == True: uncompleted_areas.remove("west")
        if len(uncompleted_areas) == 3: #add formatting (commas, spaces, and "and"s) as appropriate to the number of directions listed
            uncompleted_areas.insert(1, ", ")
            uncompleted_areas.insert(3, ", and ")
        if len(uncompleted_areas) == 2:
            uncompleted_areas.insert(1, " and ")
        tracker_pointing = "" #initialise tracker_pointing as a string
        for i in uncompleted_areas: # convert list into a string so it can be displayed with the correct formatting
            tracker_pointing = tracker_pointing + i
            
        if finished_mountain != True or finished_swamp != True or finished_forest != True: #if the tracker is still pointing to an area, display which areas it is pointing to.
            typew(f"""\n
            Behind you is your surprisingly intact but non-functional ship (apparently someone forgot to put “def”).
            You see four paths heading to the north, south, east, and west. The module tracker is pointing to the {tracker_pointing}.
            You can't wait to eat your sandwich.""")

        if finished_mountain == True and finished_swamp == True and finished_forest == True and finished_desert != True: #if the tracker is not pointing to any areas, display a different message.
            typew(f"""\n
            Behind you is your surprisingly intact but non-functional ship (apparently someone forgot to put “def”).
            You see four paths heading to the north, south, east, and west. The module tracker is no longer pointing anywhere.
            You still haven't found a replacement watyamacallit module. You guess you should try heading east now.""")

        uncompleted_areas = None #reset list of areas the tracker is pointing to after they have been displayed, so they can be re-determined next time the room is entered.
        tracker_pointing = None

        direction =(input("""\n
            Which direction would you like to go?  """).lower())   # Travel to the room the user inputs (N, S, E, or W)                                                                                                                     
    
        if direction == "north" or direction == "n":
      
            if finished_mountain == True:           # Do not let the user return to a room they've already completed
                print(""" \n 
                 You have all ready been there and there is no point going back. Like an ex just 
                 leave it alone! \n""")
            else:
                mountain()                          # Travel to Mountain room
                loop += 1                           # Add 1 each time a room is completed
        
        elif direction == "south" or direction == "s":
            if finished_swamp == True:
                print(""" \n 
                 You have all ready been there and there is no point going back. Like an ex just 
                 leave it alone! \n""")
            else:
                swamp()
                loop += 1
        
        elif direction == "east" or direction == "e":
            if finished_desert == True:
                 print(""" \n 
                 You have all ready been there and there is no point going back. Like an ex just 
                 leave it alone! \n""")
            
            else:
                desert()
                loop +=1
       
        elif direction == "west" or direction == "w":
            if finished_forest==True:
                print(""" \n 
                 You have all ready been there and there is no point going back. Like an ex just
                 leave it alone! \n""")
            else:
                forest()
                loop += 1
        else:                               # Produce error message on invalid input.
            typew("""\n
                 We have given you four choices. Please choose one as it was hard enough programming this
                 without you trying to take the p***, excuse my programming language. \n""")
def mountain():
    global finished_mountain #Set to True when room is completed. Prevents you from re-enteritng the room
    global dead # Set to True when puzzle is failed. 
    
    yeti_pic() #Display art
    typew("""\n 
                 North looks as good a direction as any. You start walking, and after a while your device
                 starts beeping like mad. You see what looks like your lol module! Unfortunately, 
                 you see a yeti lounging next to it, in what must be its nest. Even more unfortunately, 
                 the yeti sees you as well, and starts running towards you. He looks pretty hungry... 
                 do you want to thow the burger to distract the yeti 'yes' or Do you want to try and out
                 run the yeti to its nest, take the module then do one 'no' \n""")

    answer = input("""\n
                 YES or NO?  """).lower()   
   
    if answer == "yes" or answer == "y": #Success. Obtain part.
        typew("""\n
                 You take one last look at your precious space burger, then toss it in the general 
                 direction of the yeti, who starts eating it and immediately contracts space worms and 
                 doubles over with tummy problems. Probably for the best you didn’t have a chance to eat it
                 yourself...
                 
                 While the yeti is distracted you run to the nest, grab the lol module,
                 and gracefully do one.\n""")
        finished_mountain = True
   
    elif answer == "no" or answer == "n": #Failure. Game over.
        dead_yeti() 
        typew("""
                 To the nest you go running! Or more to the point: not. The yeti is much too fast 
                 and catches you. As you’re being eaten alive, you wonder between screams 
                 if your burger has gone cold...In case you haven’t figured it out yet you are dead.\n""")
        dead = True
    else:  
        dead_yeti() 
        typew("""
                 Any answer that does not resuslt in a yes or a no will lead to your death!
                 please try again oh wait your dead. Thats what you get for thinking outside the box! 
                 The box always wins.\n """)
        dead = True

def swamp():
    global finished_swamp
    global dead

    adoy_pic()
    typew("""\n
                 You trek south and encounter a swamp. The tracker leads you to a hut, and out steps a 
                 small creature, holding the omg in its hands! The creature looks tiny and cute. Looks like
                 you’re finally getting a break. Suddenly the creature speaks: “Adoy is my name. 
                 What brings you to swamp?” You begin to explain about your missing module, and Adoy cuts
                 you off. “Answer a riddle you must. Then module receive, you shall”

                 “What always runs but never walks, often murmurs, never talks, has a bed but never sleeps,
                 has a mouth but never eats?”\n""")

    answer = (input("""\n
                 What is your answer?  """).lower())                                                                                                          
    if answer == "river":
    
     typew("""\n” 
                 ”Answered correctly, you have, hehehehehehe”. Adoy grins and waddles forwards to hand you
                 the omg module. You hold it up to the light to inspect it, and when you look back down
                 OMG he’s just vanished! The shock wears off quickly, and you shrug and head back to the
                 ship..\n""")
    
     finished_swamp = True
    else:
     dead = True
     dead_adoy()
     typew("""\n
                 Before you can say “wait, I mean—“  Adoy produces a glowing beam of light and swings it at
                 you. It’s apparently quite sharp because it cuts you in two. “How rude”, 
                 you think as you die.   \n """)
                                                  
def desert():

    global finished_desert
    global dead

    number_a = random.randint(0,10)
    number_b = random.randint(0,10)
    answer = str(number_a * number_b) #convert answer to string so it can be compared with your input

    ruin_pic() #Display art
    typew("""\n
                 You wander east. This area is a desert, but as you get trudge forwards you start to 
                 make out what looks like structures in the distance. If you’re lucky there’ll be 
                 civilisation here. As you get closer you see the structures are in ruins. 
                 There are piles of scrap metal here, even with the remains of electronics. 
                 Perhaps this was once the domain of some advanced civilisation. You wander around the 
                 rubble looking for anything useful. 
                 
                 Digging through a pile of scrap you uncover what looks like a working replicator!
                 It’s a bit banged up (well, more than a bit), but you should be able to use it to replicate the
                 parts you need! You fiddle with the dials on the device and manage to coax a burst of static out
                 of it. The screen flickers to life, cutting in and out, accompanied by a constant low buzzing noise.
                 Between flickers you can make out the words: “UNRECOGNISED USER SPECIES DETECTED.
                 TO ASCERTAIN SENTIENCE PLEASE COMPLETE THIS TEST:”""")
    print(f"""\n
                 {number_a} x {number_b} = ? """)

    if input(""" 
                 What is your answer? """) == answer: #if answer is correct, obtain part
        typew("""\n
                 “SENTIENCE ASCERTAINED. HAVE A NICE DAY” 
                 
                 Cool. You struggle with the controls and the
                 barely-functioning screen, but soon enough you find a blueprint for a compatible 
                 watyamacallit module. As you press the “replicate” button the buzzing noise coming from 
                 the replicator suddenly gets louder, and the whole thing starts shaking violently. 
                 You grimace and hold it at arm’s length, until it starts shooting sparks and black smoke, 
                 at which point you drop it in a panic and dive behind the nearest trash heap. 
                 
                 After a few minutes of cowering and double-checking your times tables on your fingers, 
                 you risk a peak from behind your hiding spot. The replicator looks to have settled down, 
                 but it’s half-melted and still emitting a thin stream of black smoke you probably shouldn’t
                 be breathing in. It must be completely busted now. However, lying next to it is a shiny 
                 new watyamacallit module! Well, it could be worse, you think to yourself. 
                 You pocket the watyamacallit module and head back to the ship.""")
        finished_desert = True
    else:                                           # if answer is incorrect, game over
        dead = True
        dead_desert()
        typew("""\n
                 You hear a violent “BEEP BEEP BEEP!”  uh oh, this doesn’t look good...
                                      “COMPUTER SAYS NO!”
                 With one last angry BEEP the replicator blows up and takes you with it. 
                 You wanted to fly off this planet but not like this, not like this at all. """)
     
def forest():
    global finished_forest
    global dead

    forest_pic()
    typew("""\n
                 You follow your tracker west into a foggy forest. The tracker may lead you towards your
                 module but it doesn’t help you see in the fog, and you stumble around for what must be
                 hours. Eventually you hear your tracker going mad, and soon you see two sets of 
                 blinking lights ahead of you, just like on your lmao module. Either one looks like it 
                 could be the module, but the fog is too thick to tell. 
                 \n
                 Do you move towards the light on the left OR the right ?  """)

    while finished_forest == False and dead == False:   #loop until valid input is given

        answer = input("""\n
                 Choose Right or Left: """).lower()

        if answer=="left" or answer == "l": #game over
                dead_forest()
                typew("""
                 You go to grab the lmao module(?), only to discover the lmao module(?) has bitten your
                 hand. Turns out the light was coming from some venomous creature that attracts its 
                 prey with bioluminescence.
                 Turns out the venom is very very deadly....... 
                 Turns out you are dead.............................\n""")
                dead = True

        elif answer == "right" or answer == "r": #part obtained

            typew("""
                 You reach out towards the blinking light and grab the lmao module. For a moment you wonder
                 what the other light could be, before tuning round and heading back to your ship.\n""")  

            finished_forest = True
        else: #invalid input. Causes the statement to loop
            typew("""
                 You literally have to choose between Right and Left. I mean I tried finding a picture 
                 but have not got that far in my coding development to display it...yet.""")   

def ending():
    #Plays victory screen if all rooms have been completed. Plays game over message if all rooms have not been completed.
    if loop == 4:           #loop == if all roooms have been completed
         leave_planet()
         typew("""
                 You stumble into your ship with the last of your spare parts. You immediately install the 
                 last part, too sick of this planet to even rest for a moment. As you install the last module,
                 AAA space recovery come with all the spare parts(you forgot it was part of the spaceship lease).
                 Feeling annoyed you accept the call out charge tell them you have fixed everything
                 and without your space burger you head home.


                                              
                  
                           Credits: No-one wants to admit to this work, the shame is too much
                                (No yetis were harmed in the programming of this program) 

              
                     _________  ___  ___  _______            _______   ________   ________     
                    |\___   ___\\  \|\  \|\  ___ \           |\  ___ \ |\   ___ \|\   _ _   \    
                    \|___ \  \_\ \  \\\  \ \   __/|          \ \   __/|\ \  \\ \  \ \  \_\    \   
                         \ \  \ \ \   __  \ \  \_|/__        \ \  \_|/_\ \  \\ \  \ \  \ \\    \  
                          \ \  \ \ \  \ \  \ \  \_|\ \        \ \  \_|\ \ \  \\ \  \ \  \_\\    \ 
                           \ \__\ \ \__\ \__\ \_______\        \ \_______\ \__\\ \__\ \______  / 
                            \|__|  \|__|\|__|\|_______|         \|_______|\|__| \|__|\|_______|   """) 
                
    else:
        died_like()
        typew("""\nYou died like a pig!!! I hate you.\n""") 
                    
def intro():
     print("""\n
             ______   __    __  __    __  __    __  __    __  __    __         ______   __    __  ______  _______  
            /      \ /  |  /  |/  |  /  |/  |  /  |/  |  /  |/  |  /  |       /      \ /  |  /  |/      |/       \ 
           /$$$$$$  |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |      /$$$$$$  |$$ |  $$ |$$$$$$/ $$$$$$$  |
           $$ |  $$ |$$ |__$$ |$$ |__$$ |$$ |__$$ |$$ |__$$ |$$ |__$$ |      $$ \__$$/ $$ |__$$ |  $$ |  $$ |__$$ |
           $$ |  $$ |$$    $$ |$$    $$ |$$    $$ |$$    $$ |$$    $$ |      $$      \ $$    $$ |  $$ |  $$    $$/ 
           $$ |  $$ |$$$$$$$$ |$$$$$$$$ |$$$$$$$$ |$$$$$$$$ |$$$$$$$$ |       $$$$$$  |$$$$$$$$ |  $$ |  $$$$$$$/  
           $$ \__$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |      /  \__$$ |$$ |  $$ | _$$ |_ $$ |      
           $$    $$/ $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$    $$/ $$ |  $$ |/ $$   |$$ |      
            $$$$$$/  $$/   $$/ $$/   $$/ $$/   $$/ $$/   $$/ $$/   $$/        $$$$$$/  $$/   $$/ $$$$$$/ $$/       \n""")



     typew("""\n 
                 You are Bodger Bilko: space drifter extraordinaire, flying home from the space chippy.
                 Just as you settle into your pilot’s seat ready to bite into your juicy space burger, 
                 you hear a loud bang from somewhere on your ship. Warning sirens blare and the ship 
                 starts spinning out of control. In a panic you hold your space burger safely above your
                 head and wrestle with the ship’s joystick with your other hand, but it’s no good. It’s
                 going down. Lucky for you there’s a habitable planet nearby for it to crash into!
                 Giving up on the controls, you fasten your seatbelt and cling tightly to your space 
                 burger. If you’re lucky you’ll both survive the crash.

                 The ship lands violently but safely using its one-time emergency landing thrusters. 
                 Once you come to your senses you frantically look around for your space burger, and find
                 it safely nestled in your lap. Phew. Now that you’ve established the state of your lunch
                 you inspect your ship’s control panel. The diagnostic shows 3 crucial parts of the ship 
                 fell off and scattered around the planet’s surface during re-entry. You are now up the
                 creek without a module. In order to fly again you will need to replace your lost omg module,
                 lol module, and lmao module (which is like the lol module but makes more noise). Last but not
                 least, the diagnostic reports that your watyamacallit module has been irreparably damaged. 
                 Good news is you have a module tracker in your glove box to help locate your erstwhile 
                 components. As for your watyamacallit module…eh, you’ll figure something out.

                 Still a little dizzy, you pack your precious space burger into your bag and grab the module tracker
                 before climbing out of the ship to take a look around.\n""") 
def leave_planet():
    print(r"""
                                                
                                                        _.-''._:
                                                ,-:`-.-'    .:.|
                                                ;-.''       .::.|
                                _..------.._  / (:.       .:::.|
                            ,'.   .. . .  .`/  : :.     .::::.|
                            ,'. .    .  .   ./    \ ::. .::::::.|
                        ,'. .  .    .   . /      `.,,::::::::.;\
                      /  .            . /       ,',';_::::::,:_:
                     / . .  .   .      /      ,',','::`--'':;._;
                    : .             . /     ,',',':::::::_:'_,'
                    |..  .   .   .   /    ,',','::::::_:'_,'
                    |.              /,-. /,',':::::_:'_,'
                    | ..    .    . /) /-:/,'::::_:',-'
                    : . .     .   // / ,'):::_:','  ;
                     \ .   .     // /,' /,-.','    ./
                      \ . .  `::./,// ,'' ,'   .  /
                       `. .   . `;;;,/_.'' . . ,'
                       ,`. .   :;;' `:.  .  ,'
                         /   `-._,'  ..  ` _.-'
                        (     _,'``------''  
                        `--''                                  """)

def ship_pic():
 print(""" \n     
                                                `. ___
                                        __,' __`.                _..----....____
                            __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
                    _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
                    ,'________________                          \`-._`-','
                    `._              ```````````------...___   '-.._'-:
                        ```--.._      ,.                     ````--...__\-.
                                `.--. `-`                       ____    |  |`
                                `. `.                       ,'`````.  ;  ;`
                                    `._`.        __________   `.      \'__/`
                                    `-:._____/______/___/____`.     \  `
                                                |       `._    `.    \ 
                                                `._________`-.   `.   `.___
                                                                SSt  `------'`\n""")  
def ruin_pic():
                 print("""
                                            )\         O_._._._A_._._._O         
                                        \`--.___,'=================`.___,--'/
                                        \`--._.__                 __._,--'/
                                        \  ,. l`~~~~~~~~~~~~~~~'l ,.  /
                            __            \||(_)!_!_!_.-._!_!_!(_)||/            __
                            \\`-.__        ||_|____!!_|;|_!!____|_||        __,-'//
                                \\    `==---='-----------'='-----------`=---=='    //
                                | `--.                                         ,--' |
                                \  ,.`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',.  /
                                \||  ____,-------._,-------._,-------.____  ||/
                                    ||\|___!`======="!`======="!`======="!___|/||
                                    || |---||--------||-| | |-!!--------||---| ||
                        __O_____O_ll_lO_____O_____O|| |'|'| ||O_____O_____Ol_ll_O_____O__
                        o H o o H o o H o o H o o |-----------| o o H o o H o o H o o H o
                        ___H_____H_____H_____H____O =========== O____H_____H_____H_____H___
                                                /|=============|\ 
                        ()______()______()______() '==== +-+ ====' ()______()______()______()
                        ||{ } {_}||{_}{_}||{_}{_}/| ===== |_| ===== |\{_}{_}||{_}{_}||{_}{ }|| 
                        ||      ||      ||     / |==== s(   )s ====| \     ||      ||      ||
                        ======================()  =================  ()======================
                        ----------------------/| ------------------- |\----------------------
                                            / |---------------------| \ 
                        -'--'--'           ()  '---------------------'  ()
                                        /| ------------------------- |\    --'--'--'
                            --'--'     / |---------------------------| \    '--'
                                        ()  |___________________________|  ()           
                        --'-          /| _______________________________  |\ 
                        --'          / |__________________________________| \ """)
def adoy_pic():
    print("""                
                                        
                                        ____                  
                                        _.' :  `._               
                                    .-.'`.  ;   .'`.-.           
                        __      / : ___\ ;  /___ ; \      __  
                        ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,
                        :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;
                            `:-.._J '-.-'L__ `-- ' L_..-;'     
                                "-.__ ;  .-"  "-.  : __.-"       
                                    L ' /.------.\ ' J           
                                    "-.   "--"   .-"            
                                    __.l"-:_JL_;-";.__           
                                .-j/'.;  ;"" ""  / .'\-.         
                            .' /:`. "-.:     .-" .';  `.      
                            .-"  / ;  "-. "-..-" .-"  :    "-.   
                        .+"-.  : :      "-.__.-"      ;-._   \  
                        ; \  `.; ;                    : : "+. ;  
                        :  ;   ; ;                    : ;  : \: 
                        ;  :   ; :                    ;:   ;  : 
                        : \  ;  :  ;                  : ;  /  :: 
                        ;  ; :   ; :                  ;   :   ;: 
                        :  :  ;  :  ;                : :  ;  : ; 
                        ;\    :   ; :                ; ;     ; ; 
                        : `."-;   :  ;              :  ;    /  ; 
                        ;    -:   ; :              ;  : .-"   : 
                        :\     \  :  ;            : \.-"      : 
                        ;`.    \  ; :            ;.'_..--  / ; 
                        :  "-.  "-:  ;          :/."      .'  :
                        \         \ :          ;/  __        :
                            \       .-`.\        /t-""  ":-+.   :
                            `.  .-"    `l    __/ /`. :  ; ; \  ;
                            \   .-" .-"-.-"  .' .'j \  /   ;/ 
                                \ / .-"   /.     .'.' ;_:'    ;  
                                :-""-.`./-.'     /    `.___.'   
                                    \ `t  ._  /           
                                        "-.t-._:'      """)
def yeti_pic():
    print("""                 
                                                            ,--,  ,.-.
                              ,                   \,       '-,-`,'-.' | ._
                             /|           \    ,   |\         }  )/  / `-,',
                            [ ,          |\  /|   | |        /  \|  |/`  ,`      
                            | |       ,.`  `,` `, | |        (   (      .',
                            \  \  __ ,-` `  ,  , `/ |        Y     (   /_L\ 
                            \  \_\,``,   ` , ,  /  |         )         _,/
                             \  '  `  ,_ _`_,-,<._.<        /         /
                              ', `>.,`  `  `   ,., |_      |         /
                                \/`  `,   `   ,`  | /__,.-`    _,   `\ 
                            -,-..\  _  \  `  /  ,  / `._) _,-\`       \ 
                            \_,,.) /\    ` /  / ) (-,, ``    ,        |
                            ,` )  | \_\       '-`  |  `(               \ 
                           /  /```(   , --, ,' \   |`<`    ,            |
                          /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
                    ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
                    (-, \          ) \ ('_.-._)/ /,`    /
                    | /  `          `/ \\ V   V, /`     /
                ,--\(        ,       <_/`\\     ||      /
                (   ,``-     \/|          \-A.A-`|     /
                ,>,_ )_,..(    )\           -,,_-`  _--`
                (_ \|`   _,/_  /  \_            ,--`
                \( `   <.,../`     `-.._   _,-`    """)
def forest_pic():
                     print(r""" 
                                                  _-_
                                               /~~   ~~\                               
                                            /~~        ~~\
                                           {               }                        
                                               /~~   ~~\
                                            /~~        ~~\
                                           {               }
                                            \  _-     -_  /
                                                \\ //  ~~
                                                 | |
                             .":  .:""   "". (__)| |
                               :.:    .     "(oo)| |
                                :   ..:   .:..\/ | |
                                 :..')) ; .'))  )| |
                                ')))   )))      // \\ """)
def dead_desert():
        print(r"""
                            _.-^^---....,,--       
                        _--                  --_  
                        <                        >)
                       |                         | 
                        \._                   _./  
                            ```--. . , ; .--'''       
                               | |   |             
                            .-=||  | |=-.   
                            `-=#$%&%$#=-'   
                               | ;  :|     
                      _____.,-#%&$@%#&#~,._____
        """)                               
def dead_yeti():
      print(r"""                                                                
                                                                                _( (~\
                        _ _                        /                          ( \> > \
                    -/~/ / ~\                     :;                \       _  > /(~\/
                    || | | /\ ;\                   |l      _____     |;     ( \/    > >
                    _\\)\)\)/ ;;;                  `8o __-~     ~\   d|      \      //
                   ///(())(__/~;;\                  "88p;.  -. _\_;.oP        (_._/ /
                  (((__   __ \\   \                  `>,% (\  (\./)8"         ;:'  i
                  )))--`.'-- (( ;,8 \               ,;%%%:  ./V^^^V'          ;.   ;.
                  ((\   |   /)) .,88  `: ..,,;;;;,-::::::'_::\   ||\         ;[8:   ;
                   )|  ~-~  |(|(888; ..``'::::8888oooooo.  :\`^^^/,,~--._    |88::  |
                   |\ -===- /|  \8;; ``:.      oo.8888888888:`((( o.ooo8888Oo;:;:'  |
                   |_~-___-~_|   `-\.   `        `o`88888888b` )) 888b88888P""'     ;
                   ; ~~~~;~~         "`--_`.       b`888888888;(.,"888b888"  ..::;-'
                    ;      ;              ~"-....  b`8888888:::::.`8888. .:;;;''
                        ;    ;                 `:::. `:::OOO:::::::.`OO' ;;;''
                   :       ;                     `.      "``::::::''    .'
                        ;                           `.   \_              /
                    ;       ;                       +:   ~~--  `:'  -';
                                                    `:         : .::/  
                        ;                            ;;+_  :::. :..;;;  
                                                    ;;;;;;,;;;;;;;;,;    """)
def died_like():
                 print("""
                        ____________
                        |____________|_
                        ||--------|| | _________
                        ||- _     || |(HA ha ha!)
                        ||    - _ || | ---------
                        ||       -|| |     //
                        ||        || O\    __
                        ||        ||  \\  (..)
                        ||        ||   \\_|  |_
                        ||        ||    \  \/  )
                        ||        ||     :    :|
                        ||        ||     :    :|
                        ||        ||     :====:O
                        ||        ||     (    )
                        ||__@@@@__||     | `' |
                        || @|..|@ ||     | || |
                        ||O@`=='@O||     | || |
                        ||_@\/\/@_||     |_||_|
                        ----------------   '_'`_`
                     /________________\-----------|
                     |   NOT ONE OF   |-----------|
                     |  OF MY BETTER DAYS         |
                     |____________________________|
                      Just trying to get a head!!!
                                                   """)    
def dead_adoy():
                 print(r"""
                                          ______
                                        .-"      "-.
                                      /             \
                                     |              |
                                     |,  .-.  .-.  ,|
                                     | )(__/  \__)( |
                                     |/     /\     \|
                                     (_     ^^     _)
                        -------\______\__|IIIIII|__/__________________________
                        @8@8{}<________|-\IIIIII/-|___________________________'
                                       \          /
                                        `--------` 
            """)
def dead_forest():
                    print(r"""        
                                         )/_
                               _.--..---"-,--c_
                          \L..'           ._O__)_
                  ,-.     _.+  _  \..--( /           
                    `\.-''__.-' \ (     \_      
                        `'''     `\__   /\
                                  ')     """)

while game_loop == None:
    #Reset all variables before restarting the game
    loop = 0
    answer = None
    direction = None
    finished_mountain = False
    finished_swamp = False
    finished_desert = False
    finished_forest = False
    dead = False

    intro()
    main_room()
    ending()

    answer = (input("""\n
Would you like to play again? Yes/No  """).lower())
    if answer =="yes" or answer == "y":
            game_loop=None
            dead = False
    elif answer=="no" or answer=="n":
        typew("""\n
BYE BYE SEE YOU IN THE SKY""")
        game_loop=True    
    else: 
        typew("""
Since you have chosen to be akward and not answer a simple yes or no question, 
yoooouuuu'rrrreeeeee out of here!""")
        game_loop=True





