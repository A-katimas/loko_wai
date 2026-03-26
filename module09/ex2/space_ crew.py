from typing import List
from datetime import datetime
from enum import Enum

skip = True


def color(text: str, r: int, g: int, b: int) -> str:
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


try:
    from pydantic import Field, BaseModel, model_validator

except ImportError:
    print(color("Pydantic not installed", 255, 255, 0))
    skip = False


def bg_color(text: str, r: int, g: int, b: int) -> str:
    return f"\033[48;2;{r};{g};{b}m{text}\033[0m"


class Rank(Enum):
    CADET = "cadet"
    OFFICIER = "officier"
    LIEUTENANT = "lieutenant"
    COMMANDER = "commander"
    CAPTAIN = "captain"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field("planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validation_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("mission not star with M")
        has_captain = any(
            member.rank == Rank.CAPTAIN or Rank.COMMANDER
            for member in self.crew
        )
        if not has_captain:
            raise ValueError(color("no captain abord", 200, 40, 50))

        if self.duration_days > 365:
            experienced = [e for e in self.crew if e.experience_years > 5]
            if len(experienced) > len(self.crew) / 2:
                raise ValueError(
                    color("not engouht expriance for this mission", 50, 50, 50)
                )

        if any(not e.is_active for e in self.crew):
            raise ValueError(color("Someone is inactive", 60, 0, 150))
        return self


def main():
    crew_list: List[CrewMember] = [
        CrewMember(
            member_id="CM001",
            name="Alice",
            rank=Rank.CAPTAIN,
            age=42,
            specialization="Pilot",
            years_experience=18,
            is_active=True,
        ),
        CrewMember(
            member_id="CM002",
            name="flora",
            rank=Rank.COMMANDER,
            age=38,
            specialization="Engineer",
            years_experience=15,
            is_active=True,
        ),
        CrewMember(
            member_id="CM003",
            name="chloe",
            rank=Rank.CADET,
            age=35,
            specialization="Scientist",
            years_experience=12,
            is_active=True,
        ),
        CrewMember(
            member_id="CM004",
            name="paco",
            rank=Rank.OFFICIER,
            age=29,
            specialization="Medic",
            years_experience=7,
            is_active=True,
        ),
        CrewMember(
            member_id="CM005",
            name="julie",
            rank=Rank.LIEUTENANT,
            age=31,
            specialization="Technician",
            years_experience=10,
            is_active=True,
        ),
    ]
    try:
        mision = SpaceMission(
            mission_id="MISION R3",
            mission_name="go to europe",
            destination="venus",
            launch_date=datetime.now(),
            duration_days=300,
            crew=crew_list,
            budget_millions=5000.5,
        )
    except ValueError as e:
        print(color("Error", 255, 0, 0), e)
        return

    crew_str = "\n".join(
        f"\t- {e.name} ({e.rank.value}) - {e.specialization}"
        for e in mision.crew
    )

    print(
        f"""
            Space Mission Crew Validation
    =========================================
    Valid mission created:
    Mission: {mision.mission_name}
    ID: {mision.mission_id}
    Destination: {mision.destination}
    Duration: {mision.duration_days} days
    Budget: {mision.budget_millions}M
    Crew size: {len(mision.crew)}
    Crew members:
{crew_str}
    =========================================
            """
    )


if __name__ == "__main__":
    if skip:
        main()
