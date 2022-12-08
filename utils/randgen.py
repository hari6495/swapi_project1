import random


class randgen:  # randgen
    def __init__(self):
        self.start = 1
        self.stop = 82

    def __iter__(self):
        for i in range(15):
            yield random.randrange(1, 83)


ran = randgen()  # task_one
chars = []
for i in ran:
    chars.append(i)
print(chars)
