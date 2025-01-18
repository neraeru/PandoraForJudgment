class Mount:
    def __init__(self, name, attack_bonus=0, health_bonus=0):
        self.name = name
        self.attack_bonus = attack_bonus
        self.health_bonus = health_bonus

# Список скакунов
mounts = {
    "Без скакуна": Mount("Без скакуна"),  # Если скакун не используется
    "Лошадь": Mount("Лошадь"),
    "Гигантский волк": Mount("Гигантский волк", attack_bonus=1),
    "Саламандра": Mount("Саламандра", attack_bonus=2),
    "Дуффало": Mount("Дуффало", health_bonus=2),
    "Верблюд": Mount("Верблюд"),
}