"""Option 4: using init=False on _wheels."""

from dataclasses import dataclass, field


@dataclass
class Vehicle:
    wheels: int
    _wheels: int = field(init=False, repr=False)

    @property
    def wheels(self) -> int:
        print('getting wheels')
        return self._wheels

    @wheels.setter
    def wheels(self, wheels: int):
        print('setting wheels to', wheels)
        self._wheels = wheels
