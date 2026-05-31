# mimi is a nice cat 🐱

# github : https://github.com/MultiRight

# import libraries 

import math


# color variables 

color_red = "\033[31m"
color_green = "\033[32m"
color_orange = "\033[33m"
color_light_blue = "\033[94m" 
color_reset = "\033[0m"



while True :
    
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
        print(f"{color_orange}err103 : Invalid action. (Choice is not 'reset' or 'exit'){color_reset}")

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
        print(f"{color_orange}+----------------------------------------------------------+{color_reset}")
        print()
        
        user_choose = input(f"{color_light_blue}Enter the number of the shape to calculate its area : {color_reset}")

        # ---------------------------------------------------------------------------
        # DECISION ENGINE : Handle geometric calculations based on menu choice
        # ---------------------------------------------------------------------------

        # Calculate the area of a Square
        if user_choose == "1" :
            try : 
                side = float(input(f"{color_light_blue}Enter the length of the side : {color_reset}"))

                area = side * side
                print(f"{color_green}The area of The square is : {area}²{color_reset}")
            except ValueError :
                print(f"{color_red}err101 : your input is invalid please restart the programme{color_reset}")

        # Calculate the area of a Rectangle
        elif user_choose == "2" : 
            try :
                length = float(input(f"{color_light_blue}Enter the length of the rectangle : {color_reset}"))
                width = float(input(f"{color_light_blue}Enter the width of the rectangle : {color_reset}"))

                area = length * width
                print(f"{color_green}The area of The rectangle is : {area}²{color_reset}")
            except ValueError :
                print(f"{color_red}err101 : your input is invalid please restart the programme{color_reset}")

         # Calculate the area of a Triangle        
        elif user_choose == "3" :
            try :
                base = float(input(f"{color_light_blue}Enter the base of the triangle : {color_reset}"))
                height = float(input(f"{color_light_blue}Enter the height of the triangle : {color_reset}"))

                area = 0.5 * base * height 
                print(f"{color_green}The area of The triangle is : {area}²{color_reset}")

            except ValueError :
                print(f"{color_red}err101 : your input is invalid please restart the programme{color_reset}")

         # Calculate the area of a Circle       
        elif user_choose == "4" :
            try :
                radius = float(input(f"{color_light_blue}Enter the radius  of the circle : {color_reset}"))
                area = math.pi * (radius ** 2)
                print(f"{color_green}The area of The circle is : {area}²{color_reset}")
            except ValueError :
                print(f"{color_red}err101 : your input is invalid please restart the programme{color_reset}")

        # Calculate the area of a Parallelogram        
        elif  user_choose == "5" :
            try :
                base = float(input(f"{color_light_blue}Enter the base of the parallelogram : {color_reset}"))
                height = float(input(f"{color_light_blue}Enter the height of the parallelogram : {color_reset}"))
                area =  base * height 
                print(f"{color_green}The area of The parallelogram is  : {area}²{color_reset}")
            except ValueError :
                print(f"{color_red}err101 : your input is invalid please restart the programme{color_reset}")

        # Calculate the area of a Trapezoid 
        elif user_choose == "6" :
            try :
                base1 = float(input(f"{color_light_blue}Enter the first base of the trapezoid : {color_reset}"))
                base2 = float(input(f"{color_light_blue}Enter the seconde base of the trapezoid : {color_reset}"))
                height = float(input(f"{color_light_blue}Enter the height of the trapezoid : {color_reset}"))
                area = 0.5 * (base1 + base2 ) * height
                print(f"{color_green}The area of The trapezoid  is  : {area}²{color_reset}")
            except ValueError :
                print(f"{color_red}err101 : your input is invalid please restart the programme{color_reset}")

        else : print(f"{color_red}err102 : your input is invalid please restart the programme{color_reset}")
    print()

    # Thank you user 
    print(f"{color_orange}Thank you for using PyGeoterm!{color_reset}")
    print(f"{color_orange}Author : https://github.com/MultiRight{color_reset}")
    print()

    # quit or restar the programme
    user_action = input(f"{color_green}Type 'reset' to restart or 'exit' to quit : {color_reset}")
    if user_action == "exit" :
        print()
        print("goodbye") 
        break
    elif user_action == "reset" :
        print("\033c" , end="")
        continue
    else :
        print(f"{color_red}err103 : your input is invalid please restart the programme{color_reset}")
        break



