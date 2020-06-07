class fly_behaviour:
    def fly(self):
        print("")


class fly_with_wings(fly_behaviour):
    def fly(self):
        print("I can fly")


class fly_noway(fly_behaviour):
    def fly(self):
        print("I can't fly")


class quack_behaviour:
    def sounds(self):
        print("")


class quack(quack_behaviour):
    def sounds(self):
        print("I quack!")


class squeak(quack_behaviour):
    def sounds(self):
        print("I squeak!")


class mute(quack_behaviour):
    def sounds(self):
        print("I am shy!")


class duck:
    def __init__(self):
        self.flying = fly_behaviour()
        self.quacking = quack_behaviour()
        self.mytype = "I am a normal duck."

    def perform_swim(self):
        print("I can swim!")

    def __str__(self):
        self.flying.fly()
        self.quacking.sounds()
        return self.mytype


class mallard_duck(duck):
    def __init__(self):
        super()
        self.flying = fly_with_wings()
        self.quacking = quack()
        self.mytype = "I am a mallard duck."


class rubber_duck(duck):
    def __init__(self):
        super()
        self.flying = fly_noway()
        self.quacking = mute()
        self.mytype = "I am a rubber duck."


mallrd = mallard_duck()
print(mallrd)

toy = rubber_duck()
print(toy)
