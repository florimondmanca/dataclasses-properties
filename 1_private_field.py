"""Attempt 1: private _wheels field."""

from dataclasses import dataclass


@dataclass
class Vehicle:

    _wheels: int

    @property
    def wheels(self) -> int:
        print('getting wheels')
        return self._wheels

    @wheels.setter
    def wheels(self, wheels: int):
        print('setting wheels to', wheels)
        self._wheels = wheels
