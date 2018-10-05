"""Attempt 4: converting wheels into a proper field."""

from dataclasses import dataclass, field


@dataclass
class Vehicle:
    wheels: int
    _wheels: int = field(default=None, repr=False)

    def __post_init__(self):
        self._wheels = self.wheels

    @property
    def wheels(self) -> int:
        print('getting wheels')
        return self._wheels

    @wheels.setter
    def wheels(self, wheels: int):
        print('setting wheels to', wheels)
        self._wheels = wheels
