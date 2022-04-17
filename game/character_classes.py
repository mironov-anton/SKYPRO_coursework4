from abc import ABC
from typing import Dict, Type

from game.skills import Skill, ferocious_kick, powerful_thrust


class Character(ABC):
    name: str = NotImplemented
    max_health: float = NotImplemented
    max_stamina: float = NotImplemented
    attack: float = NotImplemented
    stamina: float = NotImplemented
    armor: float = NotImplemented
    skill: Skill = NotImplemented


class Warrior(Character):
    name: str = "Воин"
    max_health: float = 60.0
    max_stamina: float = 30.0
    attack: float = 1.5
    stamina: float = 0.8
    armor: float = 1.2
    skill: Skill = ferocious_kick


class Thief(Character):
    name: str = "Вор"
    max_health: float = 50.0
    max_stamina: float = 25.0
    attack: float = 0.8
    stamina: float = 1.5
    armor: float = 1.0
    skill: Skill = powerful_thrust


character_classes: Dict[str, Type[Character]] = {
    Warrior.name: Warrior,
    Thief.name: Thief,
}
