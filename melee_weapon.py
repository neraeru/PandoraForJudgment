class MeleeWeapon:
    def __init__(self, name, attack_bonus):
        self.name = name
        self.attack_bonus = attack_bonus

# Список оружия ближнего боя
melee_weapons = {
    "Меч": MeleeWeapon("Меч", 2),
    "Полуторник": MeleeWeapon("Полуторник", 3),
    "Двуручный меч": MeleeWeapon("Двуручный меч", 5),
    "Сабля": MeleeWeapon("Сабля", 3),
    "Рапира": MeleeWeapon("Рапира", 4),
    "Булава": MeleeWeapon("Булава", 3),
    "Цеп": MeleeWeapon("Цеп", 2),
    "Двуручная булава": MeleeWeapon("Двуручная булава", 6),
    "Копьё": MeleeWeapon("Копьё", 2),
    "Алебарда": MeleeWeapon("Алебарда", 3),
    "Пика": MeleeWeapon("Пика", 4),
    "Кавалерийское копьё": MeleeWeapon("Кавалерийское копьё", 3),
    "Одноручный топор": MeleeWeapon("Одноручный топор", 2),
    "Двуручный топор": MeleeWeapon("Двуручный топор", 5),
}