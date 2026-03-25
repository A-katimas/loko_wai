YELLOW = "\033[93m"
RESET = "\033[0m"
skip = True
try:
    import pydantic
except ImportError:
    print(YELLOW + "Pydantic not installed" + RESET)
    skip = False


class SpaceStation(pydantic.BaseModel):
    station_id: str = pydantic.Field(..., min_length=3, max_length=10)
    name: str = pydantic.Field(..., min_length=1, max_length=50)
    crew_size: int = pydantic.Field(..., ge=0, le=120)
    power_level: float = pydantic.Field(..., ge=00.0 ,le=100.0 )
    oxygen_level: float= pydantic.Field(...,ge= 0.0 ,le=100.0)
    last_maintenance: DateTime field
    is_operational: bool : , defaults to True
    notes: Optional string, pydantic.Field max 200 characters

def main():

    pass


if __name__ == "__main__":
    if skip:
        main()
