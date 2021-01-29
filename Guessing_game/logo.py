logo = """
  ________                            .__                                                                   __   
 /  _____/ __ __   ____   ______ _____|__| ____    ____      _________    _____   ____                      \ \  
/   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\    / ___\__  \  /     \_/ __ \    ______   ______   \ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  >  / /_/  > __ \|  Y Y  \  ___/   /_____/  /_____/   / / 
 \______  /____/  \___  >____  >____  >__|___|  /\___  /   \___  (____  /__|_|  /\___  >                    /_/  
        \/            \/     \/     \/        \//_____/   /_____/     \/      \/     \/                          

"""


def content_printing():
    print("Welcome to the Number Guessing Game ! 😀 ")
    print("I'm thinking of number between '1' to '100' .")
    print("------------------------------------------------")


def win():
    win = """
    __  __                          _____             
    _ \/ /_________  __   ___      ____(_)______      
    __  /_  __ \  / / /   __ | /| / /_  /__  __ \     
    _  / / /_/ / /_/ /    __ |/ |/ /_  / _  / / /     
    /_/  \____/\__,_/     ____/|__/ /_/  /_/ /_/      
                                                      
    """
    print(win)


def loose():
    loose = """
       _   _   _     _   _   _   _   _  
  / \ / \ / \   / \ / \ / \ / \ / \ 
 ( Y | o | u ) ( l | o | o | s | e )
  \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ 
    """
    print(loose)


def low():
    print("Too low  🤣 ")
    print("Guess again.")
    print("......................")


def high():
    print("Too high  😂 ")
    print("Guess again.")
    print("......................")