from game.guess import GuessGame

game = GuessGame()
while True:
    user_input = input("> ")
    output = game.guess(user_input)
    print(output.get("msg"))
    if output.get("code") == 0:
        break
