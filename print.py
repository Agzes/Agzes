import time

text = """
 ________  ________  ________  _______   ________      
|\   __  \|\   ____\|\_____  \|\  ___ \ |\   ____\     
\ \  \|\  \ \  \___| \|___/  /\ \   __/|\ \  \___|_    
 \ \   __  \ \  \  ___   /  / /\ \  \_|/_\ \_____  \   
  \ \  \ \  \ \  \|\  \ /  /_/__\ \  \_|\ \|____|\  \  
   \ \__\ \__\ \_______\\\\________\ \_______\____\_\  \ 
    \|__|\|__|\|_______|\|_______|\|_______|\_________\\
     https://agzes.netlify.app/             \|_________|
"""

def animate_text(text, char_delay=0.01, line_delay=0.1):
    for line in text.splitlines():
        for char in line:
            print(char, end='', flush=True)
            time.sleep(char_delay)
        print() 
        time.sleep(line_delay) 

animate_text(text, char_delay=0.02, line_delay=0.2)
