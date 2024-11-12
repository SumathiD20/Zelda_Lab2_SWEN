#This is the python script checks the number of lives available and pop up to see the Guide when the turns decreases.


def check_lifelines(number):
    if lives > 4:
        print("Player has {number} lives. Please continue to search the seeds!")
    elif 1 <= lives <= 3:
        print("Player has {number} lives. You have very less lives, Better to refer the guide")
    elif number == 0:
        print("No chances left. Sorry the is Game Over!")
    else:
        print("No. of lives is not valid")



turns = input("Input the number of turns:")
check_lifelines(turns)
