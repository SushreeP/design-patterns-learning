from StrategyPattern.strategy_pattern import fly_with_wings


class gobble_behaviour:
    def gobble(self):
        print("")


class gobble_class(gobble_behaviour):
    def gobble(self):
        print("Grr! Grr!")


class turkey:
    def __init__(self):
        self.gobbling = gobble_class()
        self.flying = fly_with_wings()
        self.mytype = "I am a turkey"

    def __str__(self):
        return self.mytype


class wild_turkey(turkey):
    def __init__(self):
        super()
        self.mytype = "I am a wild turkey"


turkey1 = wild_turkey()
print(turkey1)
