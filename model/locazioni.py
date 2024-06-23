from dataclasses import dataclass


@dataclass
class Locazione:
    location: str
    latitude: float
    longitude: float
    def __repr__(self):
        return f"{self.location} ({self.latitude}, {self.longitude})"
    def __hash__(self):
        return hash(self.location)