"""Module for representing a Spaceship with validated attributes."""


class Spaceship:
    """Represents a spaceship with a name, health points, and shield level.

    Attributes:
        name: A non-empty string of 3–20 characters identifying the ship.
        hp: Hull points representing remaining structural integrity; must
            be a positive integer.
        shield: Shield strength expressed as a percentage fraction
            between 0.0 (no shields) and 1.0 (full shields).

    Example:
        >>> ship = Spaceship(name="Avalon", hp=500, shield=0.75)
        >>> print(ship)
        Spaceship | Name: 'Avalon' | HP: 500 | Shield: 75.0%
        >>> ship.hp -= 100
        >>> ship.shield = 0.5
        >>> print(ship)
        Spaceship | Name: 'Avalon' | HP: 400 | Shield: 50.0%
    """

    MIN_NAME_LEN = 3
    MAX_NAME_LEN = 20
    MIN_SHIELD = 0.0
    MAX_SHIELD = 1.0

    def __init__(self, name: str, hp: int, shield: float) -> None:
        """Initializes Spaceship with validated attributes.

        Args:
            name: A non-empty string between 3 and 20 characters.
            hp: Hull points; must be a positive integer.
            shield: Shield percentage as a float between 0.0 and 1.0.

        Raises:
            TypeError: If any argument is of the wrong type.
            ValueError: If any argument fails its validation check.
        """
        self.name = name
        self.hp = hp
        self.shield = shield

    # --- name property -------------------------------------------------

    @property
    def name(self) -> str:
        """str: The name of the spaceship (3–20 characters)."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(
                f"name must be a str, got {type(value).__name__}."
            )
        stripped = value.strip()
        if not stripped:
            raise ValueError("name cannot be empty or whitespace.")
        if not (self.MIN_NAME_LEN <= len(stripped) <= self.MAX_NAME_LEN):
            raise ValueError(
                f"name must be between {self.MIN_NAME_LEN} and "
                f"{self.MAX_NAME_LEN} characters, got {len(stripped)}."
            )
        self.__name = stripped

    # --- hp property --------------------------------------------------

    @property
    def hp(self) -> int:
        """int: Hull points; reflects remaining structural integrity."""
        return self.__hp

    @hp.setter
    def hp(self, value: int) -> None:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(
                f"hp must be an int, got {type(value).__name__}."
            )
        if value <= 0:
            raise ValueError(f"hp must be a positive integer, got {value}.")
        self.__hp = value

    # --- shield property -----------------------------------------------------

    @property
    def shield(self) -> float:
        """float: Shield strength as a fraction between 0.0 and 1.0."""
        return self.__shield

    @shield.setter
    def shield(self, value: float) -> None:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(
                f"shield must be a float, got {type(value).__name__}."
            )
        value = float(value)
        if not (self.MIN_SHIELD <= value <= self.MAX_SHIELD):
            raise ValueError(
                f"shield must be between {self.MIN_SHIELD} and "
                f"{self.MAX_SHIELD}, got {value}."
            )
        self.__shield = value

    # --- Dunder Methods -----------------------------------------------------

    def __str__(self) -> str:
        """Returns a human-readable summary of the spaceship.

        Returns:
            A formatted string showing name, HP, and shield percentage.
        """
        return (
            f"Spaceship | Name: '{self.__name}' | "
            f"HP: {self.__hp} | "
            f"Shield: {self.__shield * 100:.1f}%"
        )

    def __repr__(self) -> str:
        """Returns an unambiguous developer-facing representation.

        Returns:
            A string from which an equivalent Spaceship can be reconstructed.
        """
        return (
            f"Spaceship("
            f"name={self.__name!r}, "
            f"hp={self.__hp!r}, "
            f"shield={self.__shield!r})"
        )

    def __eq__(self, other: object) -> bool:
        """Checks equality based on all three core attributes.

        Args:
            other: The object to compare against.

        Returns:
            True if other is a Spaceship with identical name, hp, and
            shield; False otherwise.
        """
        if not isinstance(other, Spaceship):
            return NotImplemented
        return (
            self.__name == other.__name
            and self.__hp == other.__hp
            and self.__shield == other.__shield
        )

    def __lt__(self, other: "Spaceship") -> bool:
        """Compares spaceships by HP (ascending).

        Args:
            other: The Spaceship to compare against.

        Returns:
            True if this ship has fewer HP than other.

        Raises:
            TypeError: If other is not a Spaceship.
        """
        if not isinstance(other, Spaceship):
            return NotImplemented
        return self.__hp < other.__hp

    def __le__(self, other: "Spaceship") -> bool:
        """Compares spaceships by HP (less than or equal).

        Args:
            other: The Spaceship to compare against.

        Returns:
            True if this ship has fewer or equal HP than other.

        Raises:
            TypeError: If other is not a Spaceship.
        """
        if not isinstance(other, Spaceship):
            return NotImplemented
        return self.__hp <= other.__hp

    def __gt__(self, other: "Spaceship") -> bool:
        """Compares spaceships by HP (greater than).

        Args:
            other: The Spaceship to compare against.

        Returns:
            True if this ship has more HP than other.

        Raises:
            TypeError: If other is not a Spaceship.
        """
        if not isinstance(other, Spaceship):
            return NotImplemented
        return self.__hp > other.__hp

    def __ge__(self, other: "Spaceship") -> bool:
        """Compares spaceships by HP (greater than or equal).

        Args:
            other: The Spaceship to compare against.

        Returns:
            True if this ship has more or equal HP than other.

        Raises:
            TypeError: If other is not a Spaceship.
        """
        if not isinstance(other, Spaceship):
            return NotImplemented
        return self.__hp >= other.__hp

    def __bool__(self) -> bool:
        """Evaluates the ship's operational status.

        Returns:
            True if the ship has positive HP and any shield remaining;
            False if shields are fully depleted.
        """
        return self.__shield > self.MIN_SHIELD

    def __hash__(self) -> int:
        """Returns a hash based on the ship's name, HP, and shield level.

        Returns:
            An integer hash value.
        """
        return hash((self.__name, self.__hp, self.__shield))
