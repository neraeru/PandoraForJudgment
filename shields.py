class Shield:
    def __init__(self, name, defense_bonus):
        self.name = name
        self.defense_bonus = defense_bonus

# Список щитов
shields = {
    "Баклер": Shield("Баклер", 1),
    "Тарч": Shield("Тарч", 2),
    "Экю": Shield("Экю", 1),
    "Павеза": Shield("Павеза", 2),
    "Башенный щит": Shield("Башенный щит", 3),
}