class Terrain:
    def __init__(self, name, unit_effects=None, equipment_effects=None):
        self.name = name
        self.unit_effects = unit_effects or {}
        self.equipment_effects = equipment_effects or {}

# Определение местностей и их эффектов
terrains = {
    "Пустота": Terrain("Пустота"),  # Без эффектов
    "Лес": Terrain(
        "Лес",
        unit_effects={
            "Дунны": {"health": 1}
        },
        equipment_effects={
            "Двуручный меч": {"attack": -2},
            "Сабля": {"attack": -1},
            "Цеп": {"attack": -2},
            "Двуручная булава": {"attack": -3},
            "Копьё": {"attack": -1},
            "Алебарда": {"attack": -2},
            "Пика": {"attack": -3},
            "Кавалерийское копьё": {"attack": -1},
            "Двуручный топор": {"attack": -3},
            "Лошадь": {"defense": -2},
            "Саламандра": {"defense": -3},
            "Дуффало": {"defense": -3},
            "Верблюд": {"defense": -3},
        },
    ),
    "Город": Terrain(
        "Город",
        unit_effects={
            "Рунны": {"health": 1},
            "Кентавры": {"health": -1},
        },
        equipment_effects={
            "Меч": {"attack": 1},
            "Двуручный меч": {"attack": -2},
            "Рапира": {"attack": 1},
            "Цеп": {"attack": -2},
            "Двуручная булава": {"attack": -3},
            "Копьё": {"attack": -1},
            "Алебарда": {"attack": -2},
            "Пика": {"attack": -3},
            "Кавалерийское копьё": {"attack": -1},
            "Двуручный топор": {"attack": -3},
        },
    ),
    "Тайга": Terrain(
        "Тайга",
        unit_effects={
            "Свартаальхи": {"health": 1},
            "Баргесты": {"health": 1},
        },
    ),
    "Корабль": Terrain(
        "Корабль",
        unit_effects={
            "Альхи": {"attack": 1},
            "Сатиры": {"attack": 1},
        },
        equipment_effects={
            "Латный доспех": {"health": -1},
            "Рапира": {"attack": 1},
            "Цеп": {"attack": -2},
            "Двуручная булава": {"attack": -3},
            "Копьё": {"attack": -1},
            "Алебарда": {"attack": -2},
            "Пика": {"attack": -3},
            "Кавалерийское копьё": {"attack": -1},
            "Двуручный топор": {"attack": -3},
            "Лошадь": {"defense": -2},
            "Гигантский волк": {"defense": -3},
            "Саламандра": {"defense": -3},
            "Дуффало": {"defense": -3},
            "Верблюд": {"defense": -3},
        },
    ),
    "Горы": Terrain(
        "Горы",
        unit_effects={
            "Гномы": {"health": 1},
            "Саламандра": {"health": 1},
        },
        equipment_effects={
            "Алебарда": {"attack": -2},
            "Пика": {"attack": -3},
            "Кавалерийское копьё": {"attack": -1},
            "Лошадь": {"defense": -2},
            "Гигантский волк": {"defense": -3},
            "Дуффало": {"defense": -3},
            "Верблюд": {"defense": -3},
        },
    ),
    "Болота": Terrain(
        "Болота",
        unit_effects={
            "Орки": {"health": 1},
        },
        equipment_effects={
            "Пехотный доспех": {"health": -1},
            "Латный доспех": {"health": -1},
            "Двуручная булава": {"attack": -3},
            "Алебарда": {"attack": -2},
            "Пика": {"attack": -3},
            "Кавалерийское копьё": {"attack": -1},
            "Двуручный топор": {"attack": -3},
            "Лошадь": {"defense": -2},
            "Саламандра": {"defense": -3},
            "Дуффало": {"defense": -3},
            "Верблюд": {"defense": -3},
        },
    ),
    "Пустыня": Terrain(
         "Пустыня",
        unit_effects={
            "Ящеролюды": {"attack": 1},
            "Верблюд": {"health": 1},
            "Трогглодиты": {"health": 2, "attack": 2},  # Добавлены бонусы для Трогглодитов
        },
        equipment_effects={
             "Латный доспех": {"health": -1},
         },
),
    "Равнины": Terrain(
        "Равнины",
        unit_effects={
            "Кентавры": {"health": 1},
        },
    ),
    "Холмы": Terrain(
        "Холмы",
        unit_effects={
            "Кентавры": {"health": 1},
        },
    ),
}