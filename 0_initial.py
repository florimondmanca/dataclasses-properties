"""Initial situation.

@dataclass with wheels field, no property used.
"""

from dataclasses import dataclass


@dataclass
class Vehicle:
    wheels: int
