from . import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.rakingcards = [dict]
        self.id = {}

    def register_card(self, card: TournamentCard) -> str:
        card.name
        self.id[card.name] = self.id.get(card.name, 0) + 1
        self.rakingcards.append({"card": card, "id": self.id[card.name]})
        return f"{card.name}_{self.id[card.name]}"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = card1_id.split("_")
        card2 = card2_id.split("_")
        fighteur1: TournamentCard
        fighteur2: TournamentCard
        for card in self.rakingcards:
            print(card["id"])
            if card["id"] == card1[1]:
                print("trouver")
                fighteur1 = card["card"]

        for card in self.rakingcards:
            if card["id"] == card2[1]:
                fighteur2 = card["card"]

        rank1 = fighteur1.get_rank_info()
        rank2 = fighteur2.get_rank_info()
        return {
            "winer": card1_id,
            "loser": card2_id,
            "winner_rating": rank1,
            "loser_rating": rank2,
        }

    def get_leaderboard(self) -> list:
        pass

    def generate_tournament_report(self) -> dict:
        pass
