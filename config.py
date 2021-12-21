from dataclasses import dataclass
from string import ascii_letters
from random import sample


@dataclass
class Config:
    DEBUG: bool = True
    SECRET_KEY: str = "".join(sample(ascii_letters, 10))
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///db1.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
