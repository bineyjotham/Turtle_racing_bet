import time
import turtle
import random
from playsound import playsound


WIDTH, HEIGHT = 500, 500
COLOR = ['red', 'blue', 'cyan', 'brown', 'pink', 'green', 'yellow', 'black', 'orange', 'purple']
MAX_BET = 100
MIN_BET = 1


def get_number_of_racers():
    while True:
        racer_no = input(f"\n\t\t\tEnter the number of racers(2-10) ")
        if racer_no.isdigit():
            racer_no = int(racer_no)
        else:
            print(f"\t\t\tInput is not numeric.... Try again")
            continue

        if 2 <= racer_no <= 10:
            return racer_no
        else:
            print("\t\t\tNumber is not in range 2-10. Try again!!")


def racing(colors):
    try:
        turtle.TurtleScreen._RUNNING = True
        turtles = create_turtle(colors)
        while True:
            for racer in turtles:
                distance = random.randrange(1, 20)
                racer.forward(distance)
                x, y = racer.pos()
                if y >= HEIGHT//2 - 10:
                    ref_no = turtles.index(racer)
                    return colors[turtles.index(racer)], ref_no
    finally:
        turtle.Terminator()


def create_turtle(colors):
    turtles = []
    spacing_x = WIDTH / (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacing_x, (-HEIGHT//2 + 10))
        racer.pendown()
        turtles.append(racer)
        turtle.TurtleScreen._RUNNING = True
    return turtles


def deposit():
    while True:
        amount = input("\t\t\tHow much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("\t\t\tAmount must be greater than 0.")
        else:
            print("\t\t\tPlease enter a number!")

    return amount


def get_bet(balance):
    racers = get_number_of_racers()
    while True:
        amount = input("\t\t\tHow much would you like to bet on this race? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= balance:
                bet = amount * racers
                print(f"\t\t\tPotential winnings: {bet}")
                return bet, racers, amount
            else:
                print(f"\t\t\tAmount must be between ${MIN_BET} - ${balance}.")
        else:
            print("\t\t\tPlease enter a number!")


def play(balance):
    bet, racers, amount = get_bet(balance)
    random.shuffle(COLOR)
    colors = COLOR[:racers]
    turtle_list = [list((i, colors[i])) for i in range(len(colors))]
    print(f"\n\t\t\t{turtle_list}")
    while True:
        choice = input(f"\t\t\tChoose which turtle will win the race by inputting the value assigned to the turtle: ")
        if choice.isdigit():
            choice = int(choice)
            if choice in range(len(colors)):
                winner, ref_no = racing(colors)
                time.sleep(5)
                turtle.Screen().bye()
                print(f"\t\t\tThe winner is {winner}")
                if choice == ref_no:
                    print(f"\t\t\tCONGRATULATIONS, YOU ARE AMAZING!!!")
                    print(f"\t\t\tYou won: ${bet}")
                    new_amount = balance + bet
                    playsound("2021-12-14_-_Space_Adventure_Intro_-_David_Fesliyan.mp3")
                    return new_amount
                else:
                    rest_of_amount = balance - amount
                    print(f"\t\t\tSORRY, YOU LOST!! YOU CAN TRY AGAIN NEXT TIME")
                    return rest_of_amount
            else:
                print(f"\t\t\tPlease enter a number that falls within the list available!!\n")
                continue
        else:
            print(f"\t\t\tPlease input a valid number!!\n")
            continue


def main():
    print(f"\n\t\t\t\t\t********************************")
    print(f"\t\t\t\t\tWELCOME TO THE TURTLE RACING BET")
    print(f"\t\t\t\t\t********************************")
    while True:
        balance = deposit()
        while balance > 0:
            print(f"\n\t\t\tCurrent balance is ${balance}")
            decision = input("\t\t\tPress enter to bet ('q' to quit) ")
            if decision == "q":
                break
            balance = play(balance)
        print(f"\t\t\tYou are left with ${balance}\n")
        choice = input(f"\t\t\tType 'y' to deposit and continue or type 'q' to exit!!! ")
        if choice == "q":
            break
        elif choice == "y":
            continue


main()
