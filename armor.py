class Armor:
    def __init__(self, name, defense_bonus):
        self.name = name
        self.defense_bonus = defense_bonus

# Список всех типов брони
armor_types = {
    "Тканая броня": Armor("Тканая броня", 0),
    "Кожаная броня": Armor("Кожаная броня", 1),
    "Кольчужная броня": Armor("Кольчужная броня", 2),
    "Пехотный доспех": Armor("Пехотный доспех", 3),
    "Латный доспех": Armor("Латный доспех", 4),
}