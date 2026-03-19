class TournamentPlatform:

    def __init__(self):
        self.cards = {}
        self.count = {}
        self.matches_played = 0

    def register_card(self, card):
        name = card.name.lower().replace(" ", "_")

        self.count[name] = self.count.get(name, 0) + 1
        card_id = f"{name}_{self.count[name]:03}"

        self.cards[card_id] = card

        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1 = self.cards.get(card1_id)
        c2 = self.cards.get(card2_id)

        if not c1 or not c2:
            return {"error": "Card not found"}

        result = c1.attack(c2)
        self.matches_played += 1

        return {
            "winner": card1_id if result["winner"] == c1.name else card2_id,
            "loser": card2_id if result["loser"] == c2.name else card1_id,
            "winner_rating": (
                c1.rating if result["winner"] == c1.name else c2.rating
            ),
            "loser_rating": (
                c2.rating if result["loser"] == c2.name else c1.rating
            ),
        }

    def get_leaderboard(self) -> list:
        return sorted(
            self.cards.values(), key=lambda c: c.rating, reverse=True
        )

    def generate_tournament_report(self) -> dict:
        ratings = [c.rating for c in self.cards.values()]

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": sum(ratings) // len(ratings) if ratings else 0,
            "platform_status": "active",
        }
