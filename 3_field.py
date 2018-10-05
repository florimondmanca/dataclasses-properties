"""Attempt 3: introducing field()."""

from dataclasses import dataclass, InitVar, field


@dataclass
class Vehicle:

    wheels: InitVar[int]
    _wheels: int = field(default=None, repr=False)

    def __post_init__(self, wheels: int):
        self._wheels = wheels

    @property
    def wheels(self) -> int:
        print('getting wheels')
        return self._wheels

    @wheels.setter
    def wheels(self, wheels: int):
        print('setting wheels to', wheels)
        self._wheels = wheels
