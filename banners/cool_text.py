import os
import random
import time
colors = {'HEADER' : "\033[95m",
    'OKBLUE' : "\033[94m",
    'RED' : "\033[91m",
    'YELLOW' : "\033[93m",
    'GREEN' : "\033[92m",
    'LIGHTBLUE' : "\033[96m",
    'FAIL' : "\033[91m",
    'END' : "\033[0m",
    'BOLD' : "\033[1m",
    'UNDERLINE' : "\033[4m" }
liste=[
"figlet -c Moriarty -f banners/sblood.flf  ","figlet -c Moriarty -f banners/3-d.flf  ","figlet -c Moriarty -f banners/avatar.flf  ","figlet -c Moriarty -f banners/bell.flf  ","figlet -c Moriarty -f banners/big.flf  ","figlet -c Moriarty -f banners/bigchief.flf  ","figlet -c Moriarty -f banners/kban.flf  "
]
colors_list=[
"OKBLUE",
"RED",
"YELLOW",
"GREEN",
"FAIL",
"LIGHTBLUE",


]



def cool_t():
    random_color=colors[random.choice(colors_list)]


    print(random_color+"""                   ███████                           ╙███████""")
    time.sleep(0.3)
    print(random_color+"""                   ██████                             ╙██████""")
    time.sleep(0.3)
    print(random_color+"""                   ████▌   ╓████▄╖,       ,▄▄█████▄    ╫█████""")
    time.sleep(0.3)
    print(random_color+"""                   ████▌  ┌████████████████████████    ╟█████""")
    time.sleep(0.3)
    print(random_color+"""                   ████   █████████████████████████▌   ██████""")
    time.sleep(0.3)
    print(random_color+"""                   ████   █████████████████████████    ██████""")
    time.sleep(0.3)
    print(random_color+"""                   █████  ╟████████████████████████    ██████""")
    time.sleep(0.3)
    print(random_color+"""                   █████▌ ▓█████████████████████████  ███████""")
    time.sleep(0.3)
    print(random_color+"""                   ██████ ██████████████████████████ ████████""")
    time.sleep(0.3)
    print(random_color+"""                   ██████████████████████████████████████████""")
    time.sleep(0.3)
    print(random_color+"""                   ▌ «▓, ╙▌ '▌ ┌▓╖ ╙████  ▀ ,█Γ ▄█┐ ╙▌ ▐██ '█""")
    time.sleep(0.3)
    print(random_color+"""                   ▌ ║██  ▌ '▌ '██  █████  á██  ███  ▌ ]██  █""")
    time.sleep(0.3)
    print(random_color+"""                   █,,,,▄██,▐█,,,,▄██████▌,████▄,,,▄██▓,,,▄██""")
    time.sleep(0.3)
    print(random_color+"""                   █▀▀██▀▀█▀▀█▀▀▀██▀▀▀▀████▀▀██▀▀█▀▀▀▀▀█▀▀▀██""")
    time.sleep(0.3)
    print(random_color+"""                   ▌      █ '▌ ^▀██  ▀▀████      ╫  ▀▀▀██▀ ,█""")
    time.sleep(0.3)
    print(random_color+"""                   ▌ ╟▄█  █ '█▀▀⌐ ╫▀▀▀ ,███  █▄▌ ╫  ▀▀▀██"███""")
    time.sleep(0.3)
    print(random_color+"""                   ██████████████████████████████████████████""")
    time.sleep(0.3)
    print(random_color+"""                   █████████▀╙██████████████████▀╙███████████""")
    time.sleep(0.3)
    print(random_color+"""                   ███████▀    ╙██████████████▀    └█████████""")
    time.sleep(0.2)
    print(random_color+"""                   ██████        └▀█████████▀        ╙███████""")
    time.sleep(0.2)
    print(random_color+"""                   ██████           ╙▀███▀           ████████""")
    time.sleep(0.2)
    print(random_color+"""                   ███████            ,█          , ┌████████""")
    print(random_color+"""                   ███████▌  .      ,████┐       ^  █████████""")
    print(random_color+"                                  Moriarty  v1.1")
    print(random_color)
    os.system(random.choice(liste))
    print("           ******************************************************************")
    print("                 #Github:https://www.github.com/AzizKpln")
    print("                 #Facebook:https://www.facebook.com/aziz.kaplan.96387")
    print("                 #Instagram:https://www.instagram.com/aziz.kpln")
    print("                 #Youtube:Cybersploitable TR"+colors["END"])
    print(random_color+"           *******************************************************************")



    time.sleep(3)
