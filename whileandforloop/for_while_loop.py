# logoReeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Hurdle 1 ✓🤖
#  World Info 
# Python
#  Reeborg's keyboard Additional options
# English
 

# reverse step run step pause stop reload 
#  120/120   
# Python CodelibraryA↑AA↓A
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
   
    
'''jump()
jump()
jump()
jump()
jump()
jump()'''
    

'''for steps in range(6):
    jump()'''
    
# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)
# =========================================================
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

