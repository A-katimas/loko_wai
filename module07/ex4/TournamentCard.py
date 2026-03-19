from . import Rankable
from ex0.Card import Card
from ex2.Combatable import Combatable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name, cost, rarity, attack, health):
        super().__init__(name, cost, rarity)

        self.attack_power = attack
        self.health = health

        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_state: dict) -> dict:
        info = game_state
        info.update(
            {
                "card_played": self.name,
            }
        )
        return info

    def attack(self, target) -> dict:
        # simple combat
        if self.attack_power >= target.health:
            self.update_wins(1)
            target.update_losses(1)
            self.rating += 16
            target.rating -= 16
            winner = self
            loser = target
        else:
            target.update_wins(1)
            self.update_losses(1)
            target.rating += 16
            self.rating -= 16
            winner = target
            loser = self

        return {"winner": winner.name, "loser": loser.name}

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage
        alive = True
        if self.health <= 0:
            alive = False
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": self.health,
            "still_alive": alive,
        }

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack, "health": self.health}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
        }

    def get_tournament_stats(self) -> dict:
        return self.get_rank_info()
