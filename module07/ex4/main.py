from .TournamentPlatform import TournamentPlatform
from .TournamentCard import TournamentCard


card1 = TournamentCard("Dragon", 5, "Legendary", 7, 5)
card2 = TournamentCard("Goblin", 2, "Common", 2, 2)

platform = TournamentPlatform()

id1 = platform.register_card(card1)
id2 = platform.register_card(card2)
print(id2)
platform.create_match(id1, id2)

print(platform.get_leaderboard())
