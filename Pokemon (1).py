#Date
#Pokemon Evolution Game

#Initalize
global pokemon_level
global pokemon_name
global trade
global day
import random
day = 1
pokemon_level = 5
pokemon_name = "Gastly"
trade = random.randint(1,2)





#Functions
def draw_Gengar():
    print("""⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜
⬛⬛⬜⬜⬜⬜⬜⬛🟪⬛⬜⬛⬛⬜⬜⬜⬜⬛⬛🟪⬛⬜⬜⬜
⬛🟪⬛⬛⬜⬜⬛⬛🟪⬛⬛🟪⬛⬜⬜⬛⬛🟪🟪🟪⬛⬜⬜⬜
⬛🟪🟪🟪⬛⬛🟪⬛🟪🟪⬛🟪🟪⬛⬛🟪🟪🟪🟪🟪⬛⬜⬜⬜
⬛🟪🟪🟪🟪⬛⬛🟪🟪🟪🟪⬛🟪⬛🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜
⬜⬛🟪🟪⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜
⬜⬛🟪⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜
⬜⬛🟪⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛🟪🟪🟪🟪🟪🟪⬛⬛⬛🟪🟪🟪🟪⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛⬛🟪🟪⬛⬛⬛🟥🟥⬛🟪🟪⬛⬛⬛🟪⬛⬜⬜⬜⬜
⬜⬛⬛⬛🟪🟪🟪🟪🟥⬛🟥🟥⬛🟪🟪⬛⬛⬛🟪⬛⬜⬜⬜⬜
⬜⬛⬛🟥🟪🟪🟪🟪🟥🟥🟥⬛⬛⬛⬛🟪🟪🟪⬛🟪⬛⬜⬜⬜
⬛🟪⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🌫️⬛🟪🟪🟪🟪🟪⬛⬛⬜⬜⬜
⬛🟪⬛⬛⬜⬛🌫️🌫️🌫️⬛🌫️⬛⬛🟪🟪🟪🟪🟪🟪🟪⬛⬛⬜⬜
⬛🟪🟪⬛⬛⬛⬜⬜⬜⬛⬜⬛🟪🟪⬛⬛🟪🟪🟪⬛🟪🟪⬛⬜
⬜⬛⬛⬛🟪⬛⬛⬛⬛⬛⬛🟪🟪🟪🟪🟪⬛⬛⬛⬛🟪🟪🟪⬛
⬜⬜⬜⬛⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛🟪🟪🟪🟪⬛
⬜⬜⬜⬜⬛⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛🟪🟪⬛⬛⬜
⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛🟪🟪🟪🟪🟪🟪🟪⬛⬛⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬛🟪🟪🟪⬛⬜⬛⬛🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜""")

def draw_Haunter():
    print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬛🟪🟪🟪⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛🟪🟪🟪🟪🟪🟪🟪🟪⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬛
⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬛⬛⬛⬛🟪🟪🟪⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪⬛🟪🟪🟪🟪⬛⬛⬛⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪⬛🟪🟪🟪🟪🟪🟪⬛⬛🟪🟪🟪🟪⬛🟪🟪🟪🟪⬛
⬜⬜⬜⬜⬛⬛⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪⬛⬛⬜⬜🟪🟪🟪🟪🟪🟪🟪⬛⬛⬜
⬜⬜⬛⬛🟪🟪⬛⬜⬜⬛🟪🟪🟪🟪⬛⬜⬛⬜⬜⬜🟪🟪🟪🟪⬛⬛⬛⬜⬜⬜
⬜⬛🟪⬛🟪🟪🟪⬛⬛⬜⬛🟪⬛🟪🟪🟪🟪⬜⬜⬜🟪⬛🟪🟪🟪⬛⬜⬜⬜⬜
⬛🟪⬛🟪🟪🟪🟪🟪🟪⬛⬜⬛🟪⬛🟪⬛⬛🟪⬛⬛⬛🟪🟪🟪🟪🟪⬛⬜⬜⬜
⬛🟪⬛🟪🟪⬛🟪🟪🟪⬛⬜⬜⬛🟪⬛🟪🟪⬛🟪🟪⬛🟪🟪🟪⬛⬛⬛⬜⬜⬜
⬜⬛🟪⬛⬛🟪🟪🟪⬛⬜⬜⬛⬛🟪🏻🏻🏻🟪🟪⬛🟪🟪🟪🟪🟪🟪🟪⬛⬛⬜
⬜⬛⬛⬜⬛🟪🟪⬛⬜⬜⬜⬜⬛⬛⬛🏻🏻🏻⬛🟪🟪🟪⬛⬛🟪🟪🟪🟪🟪⬛
⬜⬜⬜⬜⬜⬛🟪⬛⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛🟪🟪⬛⬛🟪🟪⬛🟪🟪🟪⬛⬜
⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬛🟪🟪🟪⬛🟪🟪🟪🟪🟪⬛⬛⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟪🟪⬛🟪🟪🟪🟪⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛🟪🟪⬛🟪🟪⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟪🟪⬛🟪🟪⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬜⬛🟪⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬛⬜⬜⬜⬜""")

def draw_gastly():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⠒⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⠶⠞⠉⠀⠀⠀⠉⠙⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣄⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠈⠉⠛⣦⠀⣠⣤⣄⣀⣠⠤⠞⠋⠛⠛⠛⠉⠙⠛⢶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⢀⣤⣄⡀⢀⣶⢤⣀⣉⣯⣍⡁⠀⠙⡆⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⢿⡀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡆⠀⠀⠀⠀
⠀⠀⠀⠀⣠⠞⠋⠉⠉⠛⣾⣇⡀⠙⠋⠁⠀⠈⠁⠀⠈⠙⠒⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀
⠀⠀⠀⢰⠏⠀⠀⠀⠀⢀⣾⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⠴⠚⠛⠛⠛⠛⠛⠓⠲⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀
⠀⠀⠀⢸⣄⠀⢠⡴⠶⣫⡷⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⣰⠀⠀⠀⠀⠀⠀⠀⢀⣾⠀⠀⠀
⠀⠀⠀⠀⠻⠷⠋⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣠⡟⣧⠀⠀⠀⠀⢾⡗⠛⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⢧⣀⣀⣀⣀⡀⠀⠀⠀⣠⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠀⠙⣆⠀⠀⠀⠈⢷⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⡀⠀⠈⣿⠀⠀⢰⡏⠈⠙⠶⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠃⠀⠀⢹⡄⠀⠀⠀⠀⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠙⠓⠒⠋⠀⢠⣿⡇⠀⠀⠀⠀⠙⠲⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠸⣇⠀⠀⢀⡼⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⣾⢸⡇⠀⠀⠀⠀⠀⠀⠈⠙⠷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠏⡀⠀⠀⠀⠀⢹⠀⠀⣿⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠙⠶⣄⡀⠀⠀⠀⠀⠀⠀⣰⠏⢸⡇⠀⠀⠀⠀⢸⡇⠀⠈⠻⣇⠀⠀⠀⠀
⣠⡶⠶⠖⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⠙⢶⣄⠀⠀⠀⢼⣟⠀⠈⠉⠀⠀⠀⢀⣾⠀⠀⠀⠀⠙⠳⢶⣄⠀
⢿⡇⠀⠀⠀⣠⠞⠛⠻⣦⠀⠀⠀⠀⠘⣷⠀⠈⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⣸⠏⠁⠀⠀⠀⢻⣄⠀⠀⠀⠀⣤⣾⡇⠀⠀⠀⠀⠀⠀⣠⡿⠀
⠈⠛⠒⠶⢿⣥⣄⣀⡀⣿⠀⠀⠀⠀⠀⢹⡄⠀⠀⠙⠷⣄⡀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠙⠳⠶⢾⣟⡇⣸⠃⢠⡾⣆⠀⠀⢀⣿⠁⠀
⠀⠀⠀⣼⠉⠀⠀⠉⣧⠙⣦⡀⠀⠀⠀⠈⢧⡀⠀⠀⠀⠈⠉⠓⠲⠶⠶⠶⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⣀⣠⡴⣾⣟⡇⣰⠏⠀⣼⣀⠿⣄⠀⣰⡟⠀⠀
⠀⠀⠀⢻⣄⠀⢀⣼⠃⠀⢸⠇⠀⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⢾⣄⡀⠀⠀⠀⠀⠀⣀⣠⣤⡤⠶⠚⠋⠁⣤⠴⠋⢹⣿⠟⠀⠀⠈⠙⣻⡎⠙⠃⠀⠀⠀
⠀⠀⠀⠀⠈⢛⣉⡀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠈⠛⢿⡉⣿⣋⡉⠉⠁⣀⣀⣀⡤⠶⠚⠋⠀⠀⢀⡾⠋⠀⠀⢠⣶⡿⠛⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠉⠙⠓⠶⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⠀⠀⠈⠿⠋⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⣠⡴⠋⠀⣴⣦⣀⡾⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠴⠛⠁⠀⠀⠀⠻⣦⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢦⣀⣀⣀⣀⡤⠴⠶⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠻⣆⣀⣠⡴⠶⠦⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⢶⣦⠀⠀⠈⢷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣵⠛⠛⠳⡆⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⡾⠁⠀⠀⠀⠀⣽⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢠⡟⡴⠛⠋⠀⠀⠀⢀⣤⠞⠛⠛⠛⠛⠦⣤⡀⢠⡟⣧⠀⢀⣤⠼⠞⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢦⣀⣠⠾⠀⣧⣀⡤⠖⠒⠊⠉⠁⠀⠀⠀⠀⠀⠀⠀⠙⠋⠀⠙⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")





#Main
print("Welcome to Pokemon Evolution Simulator")
while True: #Infinite Loop that allows the player to continously make decision with their pokemon.
    print("What would you like to do with " +str(pokemon_name)+ " today?")
    print("Choose an activity. Day: "+str(day))
    day = day + 1
    print("""1. Train
2. Gym Battle
3. Rest
4. End
    """)
    pokemon = int(input("1-4) activity: ")) #Decides on the activity of what you want to do with your pokemon!
    if pokemon == 1:
        print("You have encountered a wild pokemon, your pokemon attacked it and the opposing pokemon has fainted")
        pokemon_level = pokemon_level + 1
        print("Your Pokemon Leveled up!")
        print("level: "+str(pokemon_level))

    if pokemon == 2:
        print("You have decided to fight a gym")
        outcome = random.randint(1,2)
        if outcome == 1:
            print("You have beaten the gym!")
            pokemon_level = pokemon_level + 2
            print("Your pokemon has Leveled up!")
            print("level " +str(pokemon_level))
        if outcome == 2:
            print("You lost to the gym, try again next time")
            print(pokemon_level)


    if pokemon == 3:
        print("Level: " +str(pokemon_level))
        print(pokemon_name)
        mood = random.randint(1,4)
        if mood == 1:
            print("Your pokemon is feeling happy and loves you")
        if mood == 2:
            print("Your pokemon is feeling sleepy")
        if mood == 3:
            print("Your pokemon is feeling gloomy")
        if mood == 4:
            print("Your pokemon is ready to train and battle!")

    if pokemon == 4:
        print("Thank you for playing Pokemon Evolution Game")
        break  #Ends infinite loop



#Evolution 
    if pokemon_level <= 25:
        draw_gastly()
    if pokemon_level > 25 and pokemon_level <= 27:
        print("Your Gastly has evolved!")
        draw_Haunter()
        pokemon_name = "Haunter"
    if pokemon_level > 27 and pokemon_level < 36:
        draw_Haunter()
        pokemon_name = "Haunter"
    if pokemon_level >= 36 and pokemon_level < 37:
        print("Your Haunter seem like its evolving!")
        draw_Gengar()
        pokemon_name = "Gengar"
    if pokemon_level >= 38 or pokemon_level == 37:
        draw_Gengar()
        pokemon_name = "Gengar"







