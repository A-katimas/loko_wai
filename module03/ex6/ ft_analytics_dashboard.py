def main():
    # ================================
    # Game Analytics Dashboard
    # ================================

    players = [
        {
            "name": "alice",
            "score": 2300,
            "active": True,
            "region": "north",
            "achievements": 5,
        },
        {
            "name": "bob",
            "score": 1800,
            "active": True,
            "region": "east",
            "achievements": 3,
        },
        {
            "name": "charlie",
            "score": 2150,
            "active": True,
            "region": "central",
            "achievements": 7,
        },
        {
            "name": "diana",
            "score": 1950,
            "active": False,
            "region": "north",
            "achievements": 2,
        },
    ]

    print("=== Game Analytics Dashboard ===")

    # ================================
    # List Comprehension Examples
    # ================================
    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    doubled_scores = [p["score"] * 2 for p in players]
    active_players = [p["name"] for p in players if p["active"]]

    print("\n=== List Comprehension Examples ===")
    print("High scorers (>2000):", high_scorers)
    print("Scores doubled:", doubled_scores)
    print("Active players:", active_players)

    # ================================
    # Dict Comprehension Examples
    # ================================
    player_scores = {p["name"]: p["score"] for p in players}

    score_categories = {
        "high": len([p for p in players if p["score"] >= 2000]),
        "medium": len([p for p in players if 1500 <= p["score"] < 2000]),
        "low": len([p for p in players if p["score"] < 1500]),
    }

    achievement_counts = {p["name"]: p["achievements"] for p in players}

    print("\n=== Dict Comprehension Examples ===")
    print("Player scores:", player_scores)
    print("Score categories:", score_categories)
    print("Achievement counts:", achievement_counts)

    # ================================
    # Set Comprehension Examples
    # ================================
    unique_players = {p["name"] for p in players}
    unique_regions = {p["region"] for p in players}
    active_regions = {p["region"] for p in players if p["active"]}

    print("\n=== Set Comprehension Examples ===")
    print("Unique players:", unique_players)
    print("Unique regions:", unique_regions)
    print("Active regions:", active_regions)

    # ================================
    # Combined Analysis
    # ================================
    total_players = len(unique_players)
    total_achievements = sum(p["achievements"] for p in players)
    average_score = sum(p["score"] for p in players) / len(players)
    top_player = max(players, key=lambda p: p["score"])

    print("\n=== Combined Analysis ===")
    print("Total players:", total_players)
    print("Total achievements:", total_achievements)
    print("Average score:", average_score)
    print(
        f"Top performer: {top_player['name']} "
        f"({top_player['score']} points, {top_player['achievements']}"
        " achievements)"
    )


if __name__ == "__main__":
    main()
