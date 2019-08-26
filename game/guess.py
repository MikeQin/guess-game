import random


class GuessGame:
    def __init__(self):
        self.max = 5
        self.count = 0
        self.answer = random.randint(1, 20)
        print("Guess Game")
        print("Enter a number between 1 and 20")

    def guess(self, n_str):
        self.count += 1
        message = ""
        code = 1
        try:
            number = int(n_str)
        except ValueError:
            message = "Invalid number"
            return {"msg": message, "code": code}

        if number == self.answer:
            message = "You got it right!\n"
            message += "Thank you!"
            code = 0
        elif number > self.answer:
            message = "It's too big!"
        elif number < self.answer:
            message = "It's too small!"

        if self.count >= self.max:
            message += "\nGame is over."
            code = 0

        return {"msg": message, "code": code}
