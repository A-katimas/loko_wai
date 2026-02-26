import math


class Player:
    def __init__(self, position: str):
        pos = parse_coordinates(position)
        self.position = pos

    def find_other(self, spawn: tuple) -> None:
        print(round(distance_3d(self.position, spawn), 2))


def distance_3d(p1, p2) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(coord_str) -> tuple:
    try:
        parts = coord_str.split(",")
        return tuple(int(p) for p in parts)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None


def main():
    print("=== Game Coordinate System ===")

    spawn = Player("0,0,0")

    player1 = Player("1,2,3")
    # Create position
    position = (10, 20, 5)
    print(f"Position created: {position}")

    print(
        f"Distance between {spawn.position} and "
        f"{player1.position}: {player1.find_other(spawn.position)}"
    )

    # Parse valid coordinates
    player2 = Player("1,2,43")
    print(f'Parsing coordinates: "{player2.position}"')
    parsed = parse_coordinates("1,2,43")

    if parsed:
        print(f"Parsed position: {parsed}")
        distance_3d(spawn.position, parsed)
        print(
            f"Distance between {spawn.position} and {parsed}: "
            f"{player2.find_other(spawn.position)}"
        )

        # Tuple unpacking
        print("Unpacking demonstration:")
        x, y, z = parsed
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")

    # Parse invalid coordinates
    invalid_str = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{invalid_str}"')
    parse_coordinates(invalid_str)


if __name__ == "__main__":
    main()
