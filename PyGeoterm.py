# mimi is a nice cat 🐱

# github : https://github.com/MultiRight

# import libraries


import math
import sys

# Enable ANSI escape codes on Windows (not needed on Linux/Mac)
if sys.platform == "win32":
    import os
    os.system("")


# color variables

color_red = "\033[31m"
color_green = "\033[32m"
color_orange = "\033[33m"
color_light_blue = "\033[94m"
color_pink = "\033[95m"
color_reset = "\033[0m"

# Program lifecycle flag — controls the main loop execution

running = True

# ---------------------------------------------------------------------------



# CORE


while running :

    # Welcome to the user
    print(f"{color_light_blue}====================Welcome to PyGeoterm===================={color_reset}")
    print()

# Holds the active selection from the main menu

    user_q = input(f"{color_light_blue}Press enter to start use PyGeoterm or enter '--help' to help for use PyGeoterm : {color_reset}")
    print()
    # help menu

    if user_q == "--help" :
        print(f"{color_green}Definition of the tool :{color_reset}")
        print()
        print(f"{color_orange}PyGeoterm is a terminal calculator to compute geometric areas and handle errors.{color_reset}")
        print()
        print(f"{color_green}Explanation of error messages : {color_reset}")
        print()
        print(f"{color_orange}err101 : Invalid input. (Letters/symbols entered instead of numbers).{color_reset}")
        print(f"{color_orange}err102 : Invalid shape. (Choice is not in the geometric menu).{color_reset}")
        print(f"{color_orange}err103 : Invalid action. (Choice is not 'r' or 'q'){color_reset}")
        print()

# geometric menu

    else :
        print()
        print(f"{color_light_blue}Choose a geometric shape to calculate its area : {color_reset}")
        print()
        print(f"{color_orange}+----------------------------------------------------------+{color_reset}")
        print(f"{color_orange}|                 Choose a Geometric Shape                 |{color_reset}")
        print(f"{color_orange}+----------------------------------------------------------+{color_reset}")
        print(f"{color_orange}|   [1] - Square         |   [4] - Circle                  |{color_reset}")
        print(f"{color_orange}|   [2] - Rectangle      |   [5] - Parallelogram           |{color_reset}")
        print(f"{color_orange}|   [3] - Triangle       |   [6] - Trapezoid               |{color_reset}")
        print(f"{color_orange}|   [7] - Rhombus        |                                 |{color_reset}")
        print(f"{color_orange}+----------------------------------------------------------+{color_reset}")
        print()

        while running :
            # user choose
            user_choose = input(f"{color_pink}Enter the number of the shape to calculate its area : {color_reset}")
            print()
            # unit question
            unit = input(f"{color_pink}Enter a metric unit (cm, km, or m) : {color_reset}")
            print()

        # ---------------------------------------------------------------------------
        # DECISION ENGINE : Handle geometric calculations based on menu choice
        # ---------------------------------------------------------------------------

        # Calculate the area of a Square

            if user_choose == "1" :
                while True :
                    try :
                        side = float(input(f"{color_light_blue}Enter the length of the side : {color_reset}"))

                        area = side * side

                        print()

                        print(f"{color_green}The area of The square is : {area}{unit}²{color_reset}")

                        running = False
                        break

                    except ValueError :
                        print(f"{color_red}err101 : your input is invalid please try again{color_reset}")
                        print()

            # Calculate the area of a Rectangle
            elif user_choose == "2" :
                while True :
                    try :
                        length = float(input(f"{color_light_blue}Enter the length of the rectangle : {color_reset}"))
                        width = float(input(f"{color_light_blue}Enter the width of the rectangle : {color_reset}"))

                        area = length * width

                        print()

                        print(f"{color_green}The area of The rectangle is : {area}{unit}²{color_reset}")

                        running = False
                        break

                    except ValueError :
                        print(f"{color_red}err101 : your input is invalid please try again{color_reset}")
                        print()

            # Calculate the area of a Triangle
            elif user_choose == "3" :
                while True :
                    try :
                        base = float(input(f"{color_light_blue}Enter the base of the triangle : {color_reset}"))
                        height = float(input(f"{color_light_blue}Enter the height of the triangle : {color_reset}"))

                        area = 0.5 * base * height

                        print()

                        print(f"{color_green}The area of The triangle is : {area}{unit}²{color_reset}")

                        running = False
                        break

                    except ValueError :
                        print(f"{color_red}err101 : your input is invalid please try again{color_reset}")
                        print()

            # Calculate the area of a Circle
            elif user_choose == "4" :
                while True :
                    try :
                        radius = float(input(f"{color_light_blue}Enter the radius  of the circle : {color_reset}"))
                        area = math.pi * (radius ** 2)

                        print()

                        print(f"{color_green}The area of The circle is : {area}{unit}²{color_reset}")

                        running = False
                        break

                    except ValueError :
                        print(f"{color_red}err101 : your input is invalid please try again{color_reset}")
                        print()

            # Calculate the area of a Parallelogram
            elif  user_choose == "5" :
                while True :
                    try :
                        base = float(input(f"{color_light_blue}Enter the base of the parallelogram : {color_reset}"))
                        height = float(input(f"{color_light_blue}Enter the height of the parallelogram : {color_reset}"))

                        area =  base * height

                        print()

                        print(f"{color_green}The area of The parallelogram is  : {area}{unit}²{color_reset}")

                        running = False
                        break

                    except ValueError :
                        print(f"{color_red}err101 : your input is invalid please try again{color_reset}")
                        print()

            # Calculate the area of a Trapezoid
            elif user_choose == "6" :
                while True :
                    try :
                        base1 = float(input(f"{color_light_blue}Enter the first base of the trapezoid : {color_reset}"))
                        base2 = float(input(f"{color_light_blue}Enter the second base of the trapezoid : {color_reset}"))
                        height = float(input(f"{color_light_blue}Enter the height of the trapezoid : {color_reset}"))

                        area = 0.5 * (base1 + base2 ) * height

                        print()

                        print(f"{color_green}The area of The trapezoid  is  : {area}{unit}²{color_reset}")

                        running = False
                        break

                    except ValueError :
                        print(f"{color_red}err101 : your input is invalid please try again{color_reset}")
                        print()

            # Calculate the area of a Rhombus
            elif user_choose == "7":
                while True :
                    try:
                        diagonal1 = float( input( f"{color_light_blue}Enter a first diagonal of the Rhombus : {color_reset}"))
                        diagonal2 = float( input( f"{color_light_blue}Enter a second diagonal of the Rhombus : {color_reset}"))

                        area = (diagonal1 * diagonal2) / 2

                        print()

                        print(f"{color_green}The area of The Rhombus  is  : {area}{unit}²{color_reset}")

                        running = False
                        break

                    except ValueError:
                        print(f"{color_red}err101 : your input is invalid please try again{color_reset}")
                        print()
            else :
                print(f"{color_red}err102 : your input is invalid please try again{color_reset}")
        print()

# ---------------------------------------------------------------------------


    # Thank you user
    print(f"{color_orange}Thank you for using PyGeoterm!{color_reset}")
    print(f"{color_orange}Author : https://github.com/MultiRight{color_reset}")
    print()

    # quit or restar the programme

    while True :
        user_action = input(f"{color_green}Type 'r' to restart or 'q' to quit : {color_reset}")

        if user_action == "q" :
            print()
            print(f"{color_orange}goodbye{color_reset}")
            running = False
            break



        elif user_action == "r" :
            print("\033c" , end="")

            running = True
            break

        else :
            print(f"{color_red}err103 : your input is invalid please try again{color_reset}")


