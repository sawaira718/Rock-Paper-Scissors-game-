#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']
Count_one = 0
Count_two = 0
"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        s = random.choice(['rock', 'paper', 'scissor'])
        return (s)

    def learn(self, my_move, their_move):
        pass


class user:
    def User_move(value):
        value = ""
        while (value != 'rock' and value != 'paper' and value != 'scissor'):
            value = input("Enter your move, ['rock' , 'paper' , 'scissor']").lower()
        return (value)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        global Count_one
        global Count_two
        move1 = self.p1.move()
        move2 = self.p2.User_move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print("tie")
        elif beats(move1, move2):
            print("Player One win")
            Count_one = Count_one + 1
        else:
            print("Player two win")
            Count_two = Count_two + 1
        self.p1.learn(move1, move2)

    def play_game(self):
        print("Game start!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
            print("Plyer one win=", Count_one, "Plyer two win=", Count_two)
        print("Game over!")

    def play_again(self):
        response = input("Would you like to play again? "
                         "Please enter 'y' or 'n'.\n")
        if "n" in response:
            print("OK, goodbye!")
        elif "y" in response:
            print("Very good.")
            if __name__ == '__main__':
                game = Game(Player(), user())
                game.play_game()
                game.play_again()


if __name__ == '__main__':
    game = Game(Player(), user())
    game.play_game()
    game.play_again()
