from typing import Optional
from datetime import datetime
from enum import Enum

skip = True


def color(text: str, r: int, g: int, b: int) -> str:
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


try:
    from pydantic import Field, BaseModel, ValidationError, model_validator

except ImportError:
    print(color("Pydantic not installed", 255, 255, 0))
    skip = False


def bg_color(text: str, r: int, g: int, b: int) -> str:
    return f"\033[48;2;{r};{g};{b}m{text}\033[0m"


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class Contact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = Field(False)

    @model_validator(mode="after")
    def check_business_rules(self):
        # Contact ID doit commencer par "AC"
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                color("Contact ID must start with 'AC'", 150, 150, 0)
            )

        # Physical contact doit être vérifié
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError(
                color("Physical contact reports must be verified", 0, 155, 155)
            )

        # Telepathic contact nécessite au moins 3 témoins
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                color(
                    "Telepathic contact requires at least 3 witnesses",
                    155,
                    0,
                    155,
                )
            )

        # Signal fort (>7.0) doit avoir un message
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                color(
                    "Strong signals (>7.0) should include received messages",
                    50,
                    175,
                    40,
                )
            )

        return self


def main():

    contact = Contact(
        contact_id="AC_2024_001",
        timestamp=datetime.now(),
        location="Area 51, Nevada",
        contact_type="radio",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )

    print(color("Valid contact report:", 255, 215, 0))
    print(color("=" * 40, 100, 100, 100))
    print(f"ID: {color(contact.contact_id, 0, 255, 255)}")
    print(f"Type: {color(contact.contact_type.value, 255, 105, 180)}")
    print(f"Location: {color(contact.location, 173, 216, 230)}")
    print(f"Signal: {color(str(contact.signal_strength), 50, 205, 50)}/10")
    print(
        f"Duration: {color(str(contact.duration_minutes), 255, 140, 0)} ",
        "minutes",
    )
    print(f"Witnesses: {color(str(contact.witness_count), 147, 112, 219)}")
    print(f"Message: {color(repr(contact.message_received), 255, 69, 0)}")
    print(color("=" * 40, 100, 100, 100))
    try:
        human = Contact(
            contact_id="AC_2024_002",
            timestamp=datetime.now(),
            location="Mars Colony",
            contact_type="physical",
            signal_strength=8.0,
            duration_minutes=30,
            witness_count=1,
        )
        print(human.contact_id)
    except Exception as e:
        print(color("Error : ", 205, 50, 50), {e})


if __name__ == "__main__":
    if skip:
        main()
