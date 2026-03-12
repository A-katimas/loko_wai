from abc import ABC

class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str)
        self.name = name
        self.cost = cost
        self.rarity = rarity