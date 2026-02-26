import sys

def main():

    file = "/home/jtardieu/Desktop/enovoie/loko_wai/module04/ex0/ancient_fragment.txt"

    try:
        with open(file, "r+") as fd:
            contenue = fd.write("caca")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)
        sys.exit(1)

    print(fd.read())


if __name__ == "__main__":
    main()
