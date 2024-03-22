print("Welcome to deadly Game!")
side = input("'left' or 'Right' :")
side = side.lower()
if side=="right":
    print("There is a river.")
    river_cross = input("Do you want to 'wait' or 'swim' :")
    river_cross = river_cross.lower()
    if river_cross=="wait":
        color = input("Red or green or blue? :")
        color = color.lower()
        if color =="red" or color=="blue":
            print("Game is over")
        else: 
            print("YOU WON!!!!")
    else:
        print("There is a crocodile, you are finished")
else:
    print("Game is Over, A lion has eaten you")
