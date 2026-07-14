"""
musical_instruments.py
======================
Five standalone instrument classes for a music store inventory system.
Each class uses name-mangled private attributes exposed through properties
with full validation — no inheritance used.

Generate with Claude Sonnet 4.6 with the prompt 'Please write 5 classes.
Do not use inheritance.  Write in Python.  Use proper data protection 
techniques and properties.  The classes will be for Musical Instruments 
sold at a music store.  Have Guitar, Four string Bass Guitar, Twelve String 
Guitar, Seven String Guitar, and Five string bass.'
"""


# ---------------------------------------------------------------------------
# 1. Guitar  (standard 6-string)
# ---------------------------------------------------------------------------

class Guitar:
    """A standard 6-string guitar (acoustic or electric)."""

    VALID_TYPES = {"acoustic", "electric", "semi-hollow"}

    def __init__(
        self,
        brand: str,
        model: str,
        price: float,
        color: str,
        body_wood: str,
        neck_wood: str,
        guitar_type: str = "acoustic",
    ) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.body_wood = body_wood
        self.neck_wood = neck_wood
        self.guitar_type = guitar_type
        self.__num_strings: int = 6          # fixed; not publicly settable

    # --- brand ---
    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("brand must be a non-empty string.")
        self.__brand = value.strip()

    # --- model ---
    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("model must be a non-empty string.")
        self.__model = value.strip()

    # --- price ---
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("price must be a non-negative number.")
        self.__price = float(value)

    # --- color ---
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("color must be a non-empty string.")
        self.__color = value.strip()

    # --- body_wood ---
    @property
    def body_wood(self) -> str:
        return self.__body_wood

    @body_wood.setter
    def body_wood(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("body_wood must be a non-empty string.")
        self.__body_wood = value.strip()

    # --- neck_wood ---
    @property
    def neck_wood(self) -> str:
        return self.__neck_wood

    @neck_wood.setter
    def neck_wood(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("neck_wood must be a non-empty string.")
        self.__neck_wood = value.strip()

    # --- guitar_type ---
    @property
    def guitar_type(self) -> str:
        return self.__guitar_type

    @guitar_type.setter
    def guitar_type(self, value: str) -> None:
        if value.lower() not in self.VALID_TYPES:
            raise ValueError(f"guitar_type must be one of {self.VALID_TYPES}.")
        self.__guitar_type = value.lower()

    # --- num_strings (read-only) ---
    @property
    def num_strings(self) -> int:
        return self.__num_strings

    def __str__(self) -> str:
        return (
            f"Guitar | {self.__brand} {self.__model} | {self.__guitar_type.title()} | "
            f"{self.__num_strings} strings | {self.__color} | "
            f"Body: {self.__body_wood}, Neck: {self.__neck_wood} | ${self.__price:,.2f}"
        )

    def __repr__(self) -> str:
        return (
            f"Guitar(brand={self.__brand!r}, model={self.__model!r}, "
            f"price={self.__price}, color={self.__color!r}, "
            f"body_wood={self.__body_wood!r}, neck_wood={self.__neck_wood!r}, "
            f"guitar_type={self.__guitar_type!r})"
        )


# ---------------------------------------------------------------------------
# 2. FourStringBassGuitar
# ---------------------------------------------------------------------------

class FourStringBassGuitar:
    """A standard 4-string bass guitar."""

    VALID_SCALE_LENGTHS = {"short", "medium", "long", "extra-long"}

    def __init__(
        self,
        brand: str,
        model: str,
        price: float,
        color: str,
        body_wood: str,
        neck_wood: str,
        scale_length: str = "long",
        is_active: bool = False,
    ) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.body_wood = body_wood
        self.neck_wood = neck_wood
        self.scale_length = scale_length
        self.is_active = is_active
        self.__num_strings: int = 4

    # --- brand ---
    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("brand must be a non-empty string.")
        self.__brand = value.strip()

    # --- model ---
    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("model must be a non-empty string.")
        self.__model = value.strip()

    # --- price ---
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("price must be a non-negative number.")
        self.__price = float(value)

    # --- color ---
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("color must be a non-empty string.")
        self.__color = value.strip()

    # --- body_wood ---
    @property
    def body_wood(self) -> str:
        return self.__body_wood

    @body_wood.setter
    def body_wood(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("body_wood must be a non-empty string.")
        self.__body_wood = value.strip()

    # --- neck_wood ---
    @property
    def neck_wood(self) -> str:
        return self.__neck_wood

    @neck_wood.setter
    def neck_wood(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("neck_wood must be a non-empty string.")
        self.__neck_wood = value.strip()

    # --- scale_length ---
    @property
    def scale_length(self) -> str:
        return self.__scale_length

    @scale_length.setter
    def scale_length(self, value: str) -> None:
        if value.lower() not in self.VALID_SCALE_LENGTHS:
            raise ValueError(f"scale_length must be one of {self.VALID_SCALE_LENGTHS}.")
        self.__scale_length = value.lower()

    # --- is_active (active electronics) ---
    @property
    def is_active(self) -> bool:
        return self.__is_active

    @is_active.setter
    def is_active(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError("is_active must be a boolean.")
        self.__is_active = value

    # --- num_strings (read-only) ---
    @property
    def num_strings(self) -> int:
        return self.__num_strings

    def __str__(self) -> str:
        electronics = "Active" if self.__is_active else "Passive"
        return (
            f"4-String Bass | {self.__brand} {self.__model} | {electronics} | "
            f"{self.__num_strings} strings | {self.__color} | "
            f"Body: {self.__body_wood}, Neck: {self.__neck_wood} | "
            f"Scale: {self.__scale_length} | ${self.__price:,.2f}"
        )

    def __repr__(self) -> str:
        return (
            f"FourStringBassGuitar(brand={self.__brand!r}, model={self.__model!r}, "
            f"price={self.__price}, color={self.__color!r}, "
            f"body_wood={self.__body_wood!r}, neck_wood={self.__neck_wood!r}, "
            f"scale_length={self.__scale_length!r}, is_active={self.__is_active})"
        )


# ---------------------------------------------------------------------------
# 3. TwelveStringGuitar
# ---------------------------------------------------------------------------

class TwelveStringGuitar:
    """A 12-string guitar — each standard string is paired with a doubled course."""

    VALID_TYPES = {"acoustic", "electric", "semi-hollow"}

    def __init__(
        self,
        brand: str,
        model: str,
        price: float,
        color: str,
        body_wood: str,
        neck_wood: str,
        guitar_type: str = "acoustic",
        has_cutaway: bool = False,
    ) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.body_wood = body_wood
        self.neck_wood = neck_wood
        self.guitar_type = guitar_type
        self.has_cutaway = has_cutaway
        self.__num_strings: int = 12

    # --- brand ---
    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("brand must be a non-empty string.")
        self.__brand = value.strip()

    # --- model ---
    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("model must be a non-empty string.")
        self.__model = value.strip()

    # --- price ---
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("price must be a non-negative number.")
        self.__price = float(value)

    # --- color ---
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("color must be a non-empty string.")
        self.__color = value.strip()

    # --- body_wood ---
    @property
    def body_wood(self) -> str:
        return self.__body_wood

    @body_wood.setter
    def body_wood(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("body_wood must be a non-empty string.")
        self.__body_wood = value.strip()

    # --- neck_wood ---
    @property
    def neck_wood(self) -> str:
        return self.__neck_wood

    @neck_wood.setter
    def neck_wood(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("neck_wood must be a non-empty string.")
        self.__neck_wood = value.strip()

    # --- guitar_type ---
    @property
    def guitar_type(self) -> str:
        return self.__guitar_type

    @guitar_type.setter
    def guitar_type(self, value: str) -> None:
        if value.lower() not in self.VALID_TYPES:
            raise ValueError(f"guitar_type must be one of {self.VALID_TYPES}.")
        self.__guitar_type = value.lower()

    # --- has_cutaway ---
    @property
    def has_cutaway(self) -> bool:
        return self.__has_cutaway

    @has_cutaway.setter
    def has_cutaway(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError("has_cutaway must be a boolean.")
        self.__has_cutaway = value

    # --- num_strings (read-only) ---
    @property
    def num_strings(self) -> int:
        return self.__num_strings

    def __str__(self) -> str:
        cutaway = "Cutaway" if self.__has_cutaway else "No Cutaway"
        return (
            f"12-String Guitar | {self.__brand} {self.__model} | "
            f"{self.__guitar_type.title()} | {self.__num_strings} strings | "
            f"{self.__color} | Body: {self.__body_wood}, Neck: {self.__neck_wood} | "
            f"{cutaway} | ${self.__price:,.2f}"
        )

    def __repr__(self) -> str:
        return (
            f"TwelveStringGuitar(brand={self.__brand!r}, model={self.__model!r}, "
            f"price={self.__price}, color={self.__color!r}, "
            f"body_wood={self.__body_wood!r}, neck_wood={self.__neck_wood!r}, "
            f"guitar_type={self.__guitar_type!r}, has_cutaway={self.__has_cutaway})"
        )


# ---------------------------------------------------------------------------
# 4. SevenStringGuitar
# ---------------------------------------------------------------------------

class SevenStringGuitar:
    """A 7-string guitar — adds a low B string below the standard 6."""

    VALID_TYPES = {"electric", "acoustic", "semi-hollow"}
    VALID_TUNINGS = {"standard", "drop-A", "drop-G#", "custom"}

    def __init__(
        self,
        brand: str,
        model: str,
        price: float,
        color: str,
        body_wood: str,
        neck_wood: str,
        guitar_type: str = "electric",
        tuning: str = "standard",
        num_frets: int = 24,
    ) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.body_wood = body_wood
        self.neck_wood = neck_wood
        self.guitar_type = guitar_type
        self.tuning = tuning
        self.num_frets = num_frets
        self.__num_strings: int = 7

    # --- brand ---
    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("brand must be a non-empty string.")
        self.__brand = value.strip()

    # --- model ---
    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("model must be a non-empty string.")
        self.__model = value.strip()

    # --- price ---
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("price must be a non-negative number.")
        self.__price = float(value)

    # --- color ---
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("color must be a non-empty string.")
        self.__color = value.strip()

    # --- body_wood ---
    @property
    def body_wood(self) -> str:
        return self.__body_wood

    @body_wood.setter
    def body_wood(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("body_wood must be a non-empty string.")
        self.__body_wood = value.strip()

    # --- neck_wood ---
    @property
    def neck_wood(self) -> str:
        return self.__neck_wood

    @neck_wood.setter
    def neck_wood(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("neck_wood must be a non-empty string.")
        self.__neck_wood = value.strip()

    # --- guitar_type ---
    @property
    def guitar_type(self) -> str:
        return self.__guitar_type

    @guitar_type.setter
    def guitar_type(self, value: str) -> None:
        if value.lower() not in self.VALID_TYPES:
            raise ValueError(f"guitar_type must be one of {self.VALID_TYPES}.")
        self.__guitar_type = value.lower()

    # --- tuning ---
    @property
    def tuning(self) -> str:
        return self.__tuning

    @tuning.setter
    def tuning(self, value: str) -> None:
        # Preserve original casing for matching (e.g. "drop-A" not "drop-a")
        if value not in self.VALID_TUNINGS:
            raise ValueError(f"tuning must be one of {self.VALID_TUNINGS}.")
        self.__tuning = value

    # --- num_frets ---
    @property
    def num_frets(self) -> int:
        return self.__num_frets

    @num_frets.setter
    def num_frets(self, value: int) -> None:
        if not isinstance(value, int) or not (18 <= value <= 30):
            raise ValueError("num_frets must be an integer between 18 and 30.")
        self.__num_frets = value

    # --- num_strings (read-only) ---
    @property
    def num_strings(self) -> int:
        return self.__num_strings

    def __str__(self) -> str:
        return (
            f"7-String Guitar | {self.__brand} {self.__model} | "
            f"{self.__guitar_type.title()} | {self.__num_strings} strings | "
            f"{self.__color} | Body: {self.__body_wood}, Neck: {self.__neck_wood} | "
            f"Tuning: {self.__tuning} | {self.__num_frets} frets | ${self.__price:,.2f}"
        )

    def __repr__(self) -> str:
        return (
            f"SevenStringGuitar(brand={self.__brand!r}, model={self.__model!r}, "
            f"price={self.__price}, color={self.__color!r}, "
            f"body_wood={self.__body_wood!r}, neck_wood={self.__neck_wood!r}, "
            f"guitar_type={self.__guitar_type!r}, tuning={self.__tuning!r}, "
            f"num_frets={self.__num_frets})"
        )


# ---------------------------------------------------------------------------
# 5. FiveStringBass
# ---------------------------------------------------------------------------

class FiveStringBass:
    """A 5-string bass guitar — adds a low B string below the standard 4."""

    VALID_SCALE_LENGTHS = {"short", "medium", "long", "extra-long"}

    def __init__(
        self,
        brand: str,
        model: str,
        price: float,
        color: str,
        body_wood: str,
        neck_wood: str,
        scale_length: str = "long",
        is_active: bool = True,
        num_frets: int = 24,
    ) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.body_wood = body_wood
        self.neck_wood = neck_wood
        self.scale_length = scale_length
        self.is_active = is_active
        self.num_frets = num_frets
        self.__num_strings: int = 5

    # --- brand ---
    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("brand must be a non-empty string.")
        self.__brand = value.strip()

    # --- model ---
    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("model must be a non-empty string.")
        self.__model = value.strip()

    # --- price ---
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("price must be a non-negative number.")
        self.__price = float(value)

    # --- color ---
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("color must be a non-empty string.")
        self.__color = value.strip()

    # --- body_wood ---
    @property
    def body_wood(self) -> str:
        return self.__body_wood

    @body_wood.setter
    def body_wood(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("body_wood must be a non-empty string.")
        self.__body_wood = value.strip()

    # --- neck_wood ---
    @property
    def neck_wood(self) -> str:
        return self.__neck_wood

    @neck_wood.setter
    def neck_wood(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("neck_wood must be a non-empty string.")
        self.__neck_wood = value.strip()

    # --- scale_length ---
    @property
    def scale_length(self) -> str:
        return self.__scale_length

    @scale_length.setter
    def scale_length(self, value: str) -> None:
        if value.lower() not in self.VALID_SCALE_LENGTHS:
            raise ValueError(f"scale_length must be one of {self.VALID_SCALE_LENGTHS}.")
        self.__scale_length = value.lower()

    # --- is_active ---
    @property
    def is_active(self) -> bool:
        return self.__is_active

    @is_active.setter
    def is_active(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError("is_active must be a boolean.")
        self.__is_active = value

    # --- num_frets ---
    @property
    def num_frets(self) -> int:
        return self.__num_frets

    @num_frets.setter
    def num_frets(self, value: int) -> None:
        if not isinstance(value, int) or not (18 <= value <= 30):
            raise ValueError("num_frets must be an integer between 18 and 30.")
        self.__num_frets = value

    # --- num_strings (read-only) ---
    @property
    def num_strings(self) -> int:
        return self.__num_strings

    def __str__(self) -> str:
        electronics = "Active" if self.__is_active else "Passive"
        return (
            f"5-String Bass | {self.__brand} {self.__model} | {electronics} | "
            f"{self.__num_strings} strings | {self.__color} | "
            f"Body: {self.__body_wood}, Neck: {self.__neck_wood} | "
            f"Scale: {self.__scale_length} | {self.__num_frets} frets | ${self.__price:,.2f}"
        )

    def __repr__(self) -> str:
        return (
            f"FiveStringBass(brand={self.__brand!r}, model={self.__model!r}, "
            f"price={self.__price}, color={self.__color!r}, "
            f"body_wood={self.__body_wood!r}, neck_wood={self.__neck_wood!r}, "
            f"scale_length={self.__scale_length!r}, is_active={self.__is_active}, "
            f"num_frets={self.__num_frets})"
        )


# ---------------------------------------------------------------------------
# Quick demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    guitar = Guitar(
        brand="Gibson", model="Les Paul Standard", price=2_499.99,
        color="Sunburst", body_wood="Mahogany", neck_wood="Maple",
        guitar_type="electric",
    )

    bass_4 = FourStringBassGuitar(
        brand="Fender", model="Precision Bass", price=1_299.99,
        color="Olympic White", body_wood="Alder", neck_wood="Maple",
        scale_length="long", is_active=False,
    )

    guitar_12 = TwelveStringGuitar(
        brand="Taylor", model="254ce", price=1_799.00,
        color="Natural", body_wood="Spruce", neck_wood="Walnut",
        guitar_type="acoustic", has_cutaway=True,
    )

    guitar_7 = SevenStringGuitar(
        brand="Ibanez", model="RG80F", price=999.99,
        color="Iron Pewter", body_wood="Basswood", neck_wood="Maple",
        guitar_type="electric", tuning="drop-A", num_frets=24,
    )

    bass_5 = FiveStringBass(
        brand="Music Man", model="StingRay 5", price=2_199.00,
        color="Vintage Tobacco", body_wood="Ash", neck_wood="Maple",
        scale_length="long", is_active=True, num_frets=22,
    )

    instruments = [guitar, bass_4, guitar_12, guitar_7, bass_5]
    print("=" * 70)
    print("  MUSIC STORE INVENTORY")
    print("=" * 70)
    for instrument in instruments:
        print(instrument)
    print("=" * 70)
