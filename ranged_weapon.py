class RangedWeapon:
    def __init__(self, name, attack_bonus):
        self.name = name
        self.attack_bonus = attack_bonus

# Список оружия дальнего боя
ranged_weapons = {
    "Лук": RangedWeapon("Лук", 2),
    "Длинный лук": RangedWeapon("Длинный лук", 4),
    "Композитный лук": RangedWeapon("Композитный лук", 3),
    "Одноручный арбалет": RangedWeapon("Одноручный арбалет", 2),
    "Лёгкий арбалет": RangedWeapon("Лёгкий арбалет", 4),
    "Тяжёлый арбалет": RangedWeapon("Тяжёлый арбалет", 5),
    "Праща": RangedWeapon("Праща", 1),
    "Дротик": RangedWeapon("Дротик", 2),
    "Метательный топорик": RangedWeapon("Метательный топорик", 2),
    "Аркебуза": RangedWeapon("Аркебуза", 6),
    "Пистоль": RangedWeapon("Пистоль", 4),
}