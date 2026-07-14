This is one possible solution to the refactoring code.


class Guitar(MusicalInstrument):
    VALID_TYPES = {"acoustic", "electric", "semi-hollow"}
 
    def __init__(
        self,
        brand,
        model,
        price,
        color,
        body_wood,
        neck_wood,
        guitar_type="acoustic",
        num_strings=6,
    ):
        super().__init__(
            brand,
            model,
            price,
            color,
            body_wood,
            neck_wood,
        )
 
        self.guitar_type = guitar_type
        self._num_strings = num_strings
 
    @property
    def guitar_type(self):
        return self._guitar_type
 
    @guitar_type.setter
    def guitar_type(self, value):
        if value.lower() not in self.VALID_TYPES:
            raise ValueError(
                f"guitar_type must be one of {self.VALID_TYPES}"
            )
        self._guitar_type = value.lower()
 
    @property
    def num_strings(self):
        return self._num_strings

class TwelveStringGuitar(Guitar):
    def __init__(self, *args, has_cutaway=False, **kwargs):
        super().__init__(
            *args,
            num_strings=12,
            **kwargs
        )
        self.has_cutaway = has_cutaway

class SevenStringGuitar(Guitar):

    VALID_TUNINGS = {
        "standard",
        "drop-A",
        "drop-G#",
        "custom"
    }

    def __init__(
        self,
        *args,
        tuning="standard",
        num_frets=24,
        **kwargs,
    ):
        super().__init__(
            *args,
            num_strings=7,
            **kwargs
        )

        self.tuning = tuning
        self.num_frets = num_frets

class BassGuitar(MusicalInstrument):

    VALID_SCALE_LENGTHS = {
        "short",
        "medium",
        "long",
        "extra-long"
    }

    def __init__(
        self,
        brand,
        model,
        price,
        color,
        body_wood,
        neck_wood,
        scale_length="long",
        is_active=False,
        num_strings=4,
    ):
        super().__init__(
            brand,
            model,
            price,
            color,
            body_wood,
            neck_wood,
        )

        self.scale_length = scale_length
        self.is_active = is_active
        self._num_strings = num_strings

class FourStringBassGuitar(BassGuitar):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            num_strings=4,
            **kwargs
        )

class FiveStringBass(BassGuitar):
    def __init__(
        self,
        *args,
        num_frets=24,
        **kwargs,
    ):
        super().__init__(
            *args,
            num_strings=5,
            **kwargs
        )

        self.num_frets = num_frets



