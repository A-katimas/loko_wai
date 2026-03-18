from ex0.Card import Card
from .Rankable import Rankable
from ex2.Combatable import Combatable


class TournamentCard(Card, Rankable, Combatable):

    def __init__(self, name, cost, rarity, attack, health):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        info = game_state
        info.update(
            {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield",
            }
        )
        game_state["mana"] -= self.cost
        return info

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update(
            {
                "card_played": self.name,
                "attack": self.attack,
                "health": self.health,
            }
        )
        return info

    def attack(self, target: "TournamentCard") -> dict:
        target.health -= self.attack

        if target.health <= 0:
            self.wins += 1
            target.losses += 1

        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack,
        }

    def defend(self, incoming_damage: int) -> dict:
        return {"incoming_damage": incoming_damage, "pv": self.health}

    def get_combat_stats(self) -> dict:
        return {"dega": self.attack, "health": self.health}

    def calculate_rating(self) -> int:
        return self.wins * 3 - self.losses

    def get_tournament_stats(self) -> dict:
        return self.get_rank_info()

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating(),
        }


# def play(self, game_state: dict) -> dict
# def attack(self, target) -> dict
# def calculate_rating(self) -> int
# def get_tournament_stats(self) -> dict

# def calculate_rating(self) -> int
# def update_wins(self, wins: int) -> None
# def update_losses(self, losses: int) -> None
# def get_rank_info(self) -> dict
