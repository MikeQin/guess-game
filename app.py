from game.guess import GuessGame
import sys

print(f"Python version: {sys.version}")

game = GuessGame()
while True:
    user_input = input("> ")
    output = game.guess(user_input)
    print(output.get("msg"))
    if output.get("code") == 0:
        break
