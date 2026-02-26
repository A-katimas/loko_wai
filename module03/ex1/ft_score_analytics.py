import sys


def main():
    print("=== Player Score Analytics ===")

    if len(sys.argv) < 2:
        print(
            f"No scores provided. Usage: python3 {sys.argv[0]} ",
            "<score1> <score2> ...",
        )

    else:
        nombres = sys.argv[1:]
        nombres = [int(n) for n in nombres]

        print("Scores processed:", nombres)
        print(f"Total players: {len(sys.argv)-1}")
        print("Total score:", sum(nombres))

        a = sum(nombres) / len(nombres)
        print("Average score:", a)
        print("High score:", max(nombres))
        print("Low score:", min(nombres))

        a = max(nombres) - min(nombres)
        print("Score range:", a)


if __name__ == "__main__":
    main()
