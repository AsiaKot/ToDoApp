from dataclasses import dataclass
from string import ascii_letters
from random import sample


@dataclass
class Config:
    DEBUG: bool = True
    SECRET_KEY: str = "".join(sample(ascii_letters, 10))
