from . import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.rakingcards = [dict]
        self.id = {}

    def register_card(self, card: TournamentCard) -> str:
        card.name
        self.id[card.name] = self.id.get(card.name, 0) + 1
        self.rakingcards.append({"card": card, "id": self.id[card.name]})
        return f"{card.name}{self.id[card.name]}"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        pass

    def get_leaderboard(self) -> list:
        pass

    def generate_tournament_report(self) -> dict:
        pass
