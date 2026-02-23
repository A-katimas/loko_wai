def garden_operations(error_type):
    if error_type == "value":
        int("abc")  # ValueError

    elif error_type == "zero":
        10 / 0  # ZeroDivisionError

    elif error_type == "file":
        open("missing.txt", "r")  # FileNotFoundError

    elif error_type == "key":
        garden = {"rose": 5}
        print(garden["missing_plant"])  # KeyError


def main():
    print("=== Garden Error Types Demo ===")

    # ValueError
    print("\nTesting ValueError...")
    try:
        garden_operations("value")
    except ValueError as e:
        print("Caught ValueError:", e)

    # ZeroDivisionError
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)

    # FileNotFoundError
    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)

    # KeyError
    print("\nTesting KeyError...")
    try:
        garden_operations("key")
    except KeyError as e:
        print("Caught KeyError:", e)

    # Catch multiple errors together
    print("\nTesting multiple errors together...")
    try:
        garden_operations("value")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
