class Weather:
    def __init__(self, name, unit_effects=None, equipment_effects=None):
        self.name = name
        self.unit_effects = unit_effects or {}
        self.equipment_effects = equipment_effects or {}

# Определение погоды и её эффектов
weathers = {
    "Дождь": Weather(
        "Дождь",
        equipment_effects={
            "Латный доспех": {"health": -1},
        },
    ),
    "Туман": Weather(
        "Туман",
        equipment_effects={
            "Лук": {"attack": -1},
            "Длинный лук": {"attack": -2},
            "Композитный лук": {"attack": -1},
            "Одноручный арбалет": {"attack": -1},
            "Лёгкий арбалет": {"attack": -1},
            "Тяжёлый арбалет": {"attack": -2},
            "Праща": {"attack": -1},
            "Аркебуза": {"attack": -1},
            "Пистоль": {"attack": -1},
        },
    ),
    "Ливень": Weather(
        "Ливень",
        equipment_effects={
            "Аркебуза": {"attack": -1},
            "Пистоль": {"attack": -1},
        },
    ),
}