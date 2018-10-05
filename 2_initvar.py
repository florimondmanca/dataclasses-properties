"""Attempt 2: leveraging InitVar."""

from dataclasses import dataclass, InitVar


@dataclass
class Vehicle:

    wheels: InitVar[int]
    _wheels: int = None

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
