import random

class Lottery:
    def draw_choice(self, choices):
        if not choices:
            return ("No data available for drawing.", "")
        return random.choice(choices)
