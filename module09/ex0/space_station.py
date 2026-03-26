from datetime import datetime

YELLOW = "\033[93m"
RESET = "\033[0m"


def color(text: str, r: int, g: int, b: int) -> str:
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


def bg_color(text: str, r: int, g: int, b: int) -> str:
    return f"\033[48;2;{r};{g};{b}m{text}\033[0m"


skip = True

try:
    from pydantic import Field, BaseModel, ValidationError

except ImportError:
    print(YELLOW + "Pydantic not installed" + RESET)
    skip = False


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=0, le=20)
    power_level: float = Field(..., ge=00.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = True
    notes: str = Field("base note", max_length=200)


def main():
    iss001 = SpaceStation(
        station_id="iss001",
        name="tracnard",
        crew_size=4,
        power_level=50,
        oxygen_level=77,
        last_maintenance=datetime.now(),
    )
    print(color("Space Station Data Validation", 0, 0, 255))
    print(
        bg_color(
            color("========================================", 40, 40, 40),
            10,
            10,
            10,
        )
    )
    print("Valid station created:")
    print("ID: ", color(f"{iss001.station_id}", 0, 100, 255))
    print("name", color(f"{iss001.name}", 255, 255, 0))
    print("crew:", iss001.crew_size, "people")
    print("power:", iss001.power_level, "%")
    print("oxygen:", iss001.oxygen_level, "%")
    print("status:", iss001.is_operational)
    print(color("========================================", 10, 10, 10))
    print(
        color(
            """
        bonjour
        je m'appele
        woufwouf
        """,
            0,
            255,
            0,
        )
    )
    print(color("Expected validation error:", 155, 0, 155))
    try:
        iss001 = SpaceStation(
            station_id="iss001",
            name="tracnard",
            crew_size=21,
            power_level=50,
            oxygen_level=77,
            last_maintenance=datetime.now(),
        )
    except ValidationError as e:
        print(color("Error : ", 205, 50, 50), color(f"{e}", 255, 0, 0))


if __name__ == "__main__":
    if skip:
        main()
