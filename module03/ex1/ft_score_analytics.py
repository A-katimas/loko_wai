import sys

def main():
    print("=== Player Score Analytics ===")


    if len(sys.argv) < 1 :
        print(f"No scores provided. Usage: python3 {sys.argv[0]} <score1> <score2> ...")
    else:
        nombres = sys.argv[1:]
        nombres = [int(n) for n in nombres]

        print("Scores processed:",nombres)
        print(f"Total players: {len(sys.argv)-1}")
        a = sum(nombres)
        print("Total score:",a)

if __name__ == "__main__":
    main()















# Average score: 1930.0
# High score: 2300
# Low score: 1500
# Score range: 800