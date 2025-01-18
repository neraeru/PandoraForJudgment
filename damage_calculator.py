import tkinter as tk
import threading
from tkinter import ttk
from unit import unit_types
from armor import armor_types
from melee_weapon import melee_weapons 
from ranged_weapon import ranged_weapons
from shields import shields  
from mounts import mounts  
from terrain import terrains  
from weather import weathers 

# Интерфейс
root = tk.Tk()
root.title("Калькулятор Боя")
root.geometry("1050x600") 

# Поля для ввода данных и выбора модификаторов
tk.Label(root, text="Количество раундов:", font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=10)
rounds_entry = tk.Entry(root)
rounds_entry.grid(row=0, column=2, padx=5, pady=5)

# Выпадающий список для выбора местности и погоды
tk.Label(root, text="Местность:", font=("Arial", 12)).grid(row=1, column=1, padx=10, pady=10)
terrain_dropdown = ttk.Combobox(root, values=["Лес", "Город", "Тайга", "Корабль", "Горы", "Болота", "Пустыня", "Равнины", "Холмы"])
terrain_dropdown.set("Лес")  # По умолчанию
terrain_dropdown.grid(row=1, column=2, padx=5, pady=5)

tk.Label(root, text="Погода:", font=("Arial", 12)).grid(row=2, column=1, padx=10, pady=10)
weather_dropdown = ttk.Combobox(root, values=["Ясно", "Дождь", "Туман", "Ливень"])
weather_dropdown.set("Ясно")  # По умолчанию
weather_dropdown.grid(row=2, column=2, padx=5, pady=5)

# Первая сторона
tk.Label(root, text="Первая сторона", font=("Arial", 14)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
tk.Label(root, text="Юниты первой стороны:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
attacker_units_entry = tk.Entry(root)
attacker_units_entry.grid(row=4, column=1, padx=5, pady=5)

first_side_unit_type_dropdown = ttk.Combobox(root, values=[""] + list(unit_types.keys()))
first_side_unit_type_dropdown.set("")
first_side_unit_type_dropdown.grid(row=5, column=1, padx=5, pady=5)

# Вторая сторона
tk.Label(root, text="Вторая сторона", font=("Arial", 14)).grid(row=3, column=2, padx=10, pady=10, sticky="e")
tk.Label(root, text="Юниты второй стороны:").grid(row=4, column=2, padx=5, pady=5, sticky="e")
defender_units_entry = tk.Entry(root)
defender_units_entry.grid(row=4, column=3, padx=5, pady=5)

second_side_unit_type_dropdown = ttk.Combobox(root, values=[""] + list(unit_types.keys()))
second_side_unit_type_dropdown.set("")
second_side_unit_type_dropdown.grid(row=5, column=3, padx=5, pady=5)

# История раундов
tk.Label(root, text="История раундов:", font=("Arial", 14)).grid(row=3, column=4, padx=10, pady=10)

history_text = tk.Text(root, width=40, height=10, wrap="word", relief="solid", bd=2)
history_text.grid(row=4, column=4, rowspan=7, padx=10, pady=5)

history_scrollbar = tk.Scrollbar(root, orient="vertical", command=history_text.yview)
history_scrollbar.grid(row=4, column=5, rowspan=7, sticky="ns")

history_text.config(yscrollcommand=history_scrollbar.set)

# История раундов
round_history = []

def update_round_history(round_result):
    global round_history
    round_history.insert(0, round_result)
    if len(round_history) > 20: 
        round_history.pop() 

    # Обновление текста
    history_text.delete(1.0, tk.END) 
    history_text.insert(tk.END, "\n".join(round_history)) 

import math

# Функция для расчета боя
def calculate_battle():
    try:
        # Сброс состояния перед расчетом
        global first_side_units, second_side_units
        first_side_units = int(attacker_units_entry.get())  # Первая сторона
        second_side_units = int(defender_units_entry.get())  # Вторая сторона
        rounds = int(rounds_entry.get())

        if first_side_units <= 0 or second_side_units <= 0:
            results_text.set("Ошибка: количество юнитов должно быть больше 0.")
            return

        # Получаем типы юнитов для каждой стороны
        first_side_unit_type = unit_types[first_side_unit_type_dropdown.get()]
        second_side_unit_type = unit_types[second_side_unit_type_dropdown.get()]

        # Инициализируем базовые значения атаки
        first_side_total_attack = first_side_unit_type.attack
        second_side_total_attack = second_side_unit_type.attack

        # Инициализируем базовые значения здоровья
        first_side_total_health = first_side_unit_type.health
        second_side_total_health = second_side_unit_type.health

        # Применяем модификаторы от местности
        terrain_type = terrain_dropdown.get()
        terrain = terrains.get(terrain_type)
        if terrain:
            if first_side_unit_type.name in terrain.unit_effects:
                first_side_effects = terrain.unit_effects[first_side_unit_type.name]
                first_side_total_attack += first_side_effects.get("attack", 0)
                first_side_total_health += first_side_effects.get("health", 0) 

            if second_side_unit_type.name in terrain.unit_effects:
                second_side_effects = terrain.unit_effects[second_side_unit_type.name]
                second_side_total_attack += second_side_effects.get("attack", 0)
                second_side_total_health += second_side_effects.get("health", 0) 

        # Применение модификаторов от погоды
        weather_type = weather_dropdown.get()
        weather = weathers.get(weather_type)
        if weather:
            if first_side_unit_type.name in weather.unit_effects:
                first_side_effects = weather.unit_effects[first_side_unit_type.name]
                first_side_total_attack += first_side_effects.get("attack", 0)
            if second_side_unit_type.name in weather.unit_effects:
                second_side_effects = weather.unit_effects[second_side_unit_type.name]
                second_side_total_attack += second_side_effects.get("attack", 0)

        # Получаем защиту для каждой стороны
        first_side_total_defense = max(first_side_unit_type.defense, 0)
        second_side_total_defense = max(second_side_unit_type.defense, 0)

        # Применяем броню и щиты
        first_side_armor = armor_types.get(first_side_armor_dropdown.get())
        second_side_armor = armor_types.get(second_side_armor_dropdown.get())
        first_side_shield = shields.get(first_side_shield_dropdown.get())
        second_side_shield = shields.get(second_side_shield_dropdown.get())

        # Защита = защита юнитов + бонус от брони и щита
        if first_side_armor:
            first_side_total_defense += first_side_armor.defense_bonus
        if first_side_shield:
            first_side_total_defense += first_side_shield.defense_bonus

        if second_side_armor:
            second_side_total_defense += second_side_armor.defense_bonus
        if second_side_shield:
            second_side_total_defense += second_side_shield.defense_bonus

        # Применение бонусов от скакунов
        first_side_mount = mounts.get(first_side_mount_dropdown.get())
        second_side_mount = mounts.get(second_side_mount_dropdown.get())

        if first_side_mount and first_side_mount.health_bonus:
            first_side_total_health += first_side_mount.health_bonus
        if second_side_mount and second_side_mount.health_bonus:
            second_side_total_health += second_side_mount.health_bonus

        # Применение бонусов от оружия ближнего и дальнего боя
        first_side_melee_weapon = melee_weapons.get(first_side_weapon_dropdown.get())
        second_side_melee_weapon = melee_weapons.get(second_side_weapon_dropdown.get())

        if first_side_melee_weapon:
            first_side_total_attack += first_side_melee_weapon.attack_bonus
        if second_side_melee_weapon:
            second_side_total_attack += second_side_melee_weapon.attack_bonus

        first_side_ranged_weapon = ranged_weapons.get(first_side_ranged_weapon_dropdown.get())
        second_side_ranged_weapon = ranged_weapons.get(second_side_ranged_weapon_dropdown.get())

        if first_side_ranged_weapon:
            first_side_total_attack += first_side_ranged_weapon.attack_bonus
        if second_side_ranged_weapon:
            second_side_total_attack += second_side_ranged_weapon.attack_bonus

        # Симуляция раундов
        results = []
        for round_num in range(1, rounds + 1):
            if first_side_units <= 0 or second_side_units <= 0:
                results.append("Бой завершён досрочно!")
                break

            # Расчет урона для каждой стороны
            first_side_effective_attack = max(1, first_side_total_attack - second_side_total_defense)
            second_side_effective_attack = max(1, second_side_total_attack - first_side_total_defense)

            total_damage_to_second_side = first_side_effective_attack * first_side_units
            total_damage_to_first_side = second_side_effective_attack * second_side_units

            # Потери юнитов (округляем в большую сторону)
            second_side_losses = min(second_side_units, math.ceil(total_damage_to_second_side / second_side_total_health))
            first_side_losses = min(first_side_units, math.ceil(total_damage_to_first_side / first_side_total_health))

            # Обновляем оставшиеся юниты
            second_side_units -= second_side_losses
            first_side_units -= first_side_losses

            # Добавление информации о раунде
            results.append(f"Раунд {round_num}: Первая сторона потеряла {first_side_losses}, Вторая сторона потеряла {second_side_losses}")
            update_round_history("\n".join(results))

        # Итоги
        results.append("\nИтоги:")
        results.append(f"Первая сторона: {first_side_units} выжило, {int(attacker_units_entry.get()) - first_side_units} погибло.")
        results.append(f"Вторая сторона: {second_side_units} выжило, {int(defender_units_entry.get()) - second_side_units} погибло.")

        # Отображение результатов
        results_text.set("\n".join(results))

    except ValueError:
        results_text.set("Ошибка ввода. Проверьте данные.")

# Поля для ввода данных и выбора модификаторов
tk.Label(root, text="Количество раундов:", font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=10)
rounds_entry = tk.Entry(root)
rounds_entry.grid(row=0, column=2, padx=5, pady=5)

# Выпадающий список для выбора местности и погоды
tk.Label(root, text="Местность:", font=("Arial", 12)).grid(row=1, column=1, padx=10, pady=10)
terrain_dropdown = ttk.Combobox(root, values=["Лес", "Город", "Тайга", "Корабль", "Горы", "Болота", "Пустыня", "Равнины", "Холмы"])
terrain_dropdown.set("Лес")  # По умолчанию
terrain_dropdown.grid(row=1, column=2, padx=5, pady=5)

tk.Label(root, text="Погода:", font=("Arial", 12)).grid(row=2, column=1, padx=10, pady=10)
weather_dropdown = ttk.Combobox(root, values=["Ясно", "Дождь", "Туман", "Ливень"])
weather_dropdown.set("Ясно")  # По умолчанию
weather_dropdown.grid(row=2, column=2, padx=5, pady=5)

tk.Label(root, text="Первая сторона", font=("Arial", 14)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
tk.Label(root, text="Вторая сторона", font=("Arial", 14)).grid(row=3, column=2, padx=10, pady=10, sticky="e")

# Метки для выпадающих списков с юнитами и оборудованием
tk.Label(root, text="Юниты первой стороны:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
attacker_units_entry = tk.Entry(root)
attacker_units_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Юниты второй стороны:").grid(row=4, column=2, padx=5, pady=5, sticky="e")
defender_units_entry = tk.Entry(root)
defender_units_entry.grid(row=4, column=3, padx=5, pady=5)

# Юниты
tk.Label(root, text="Вид юнита:").grid(row=5, column=0, padx=5, pady=5)
first_side_unit_type_dropdown = ttk.Combobox(root, values=[""] + list(unit_types.keys()))
first_side_unit_type_dropdown.set("")
first_side_unit_type_dropdown.grid(row=5, column=1, padx=5, pady=5)

second_side_unit_type_dropdown = ttk.Combobox(root, values=[""] + list(unit_types.keys()))
second_side_unit_type_dropdown.set("")
second_side_unit_type_dropdown.grid(row=5, column=3, padx=5, pady=5)

# Остальные метки и выпадающие списки
tk.Label(root, text="Броня:").grid(row=6, column=0, padx=5, pady=5)
first_side_armor_dropdown = ttk.Combobox(root, values=[""] + list(armor_types.keys()))
first_side_armor_dropdown.set("")
first_side_armor_dropdown.grid(row=6, column=1, padx=5, pady=5)

second_side_armor_dropdown = ttk.Combobox(root, values=[""] + list(armor_types.keys()))
second_side_armor_dropdown.set("")
second_side_armor_dropdown.grid(row=6, column=3, padx=5, pady=5)

tk.Label(root, text="Ближний бой:").grid(row=7, column=0, padx=5, pady=5)
first_side_weapon_dropdown = ttk.Combobox(root, values=[""] + list(melee_weapons.keys()))
first_side_weapon_dropdown.set("")
first_side_weapon_dropdown.grid(row=7, column=1, padx=5, pady=5)

second_side_weapon_dropdown = ttk.Combobox(root, values=[""] + list(melee_weapons.keys()))
second_side_weapon_dropdown.set("")
second_side_weapon_dropdown.grid(row=7, column=3, padx=5, pady=5)

tk.Label(root, text="Дальний бой:").grid(row=8, column=0, padx=5, pady=5)
first_side_ranged_weapon_dropdown = ttk.Combobox(root, values=[""] + list(ranged_weapons.keys()))
first_side_ranged_weapon_dropdown.set("")
first_side_ranged_weapon_dropdown.grid(row=8, column=1, padx=5, pady=5)

second_side_ranged_weapon_dropdown = ttk.Combobox(root, values=[""] + list(ranged_weapons.keys()))
second_side_ranged_weapon_dropdown.set("")
second_side_ranged_weapon_dropdown.grid(row=8, column=3, padx=5, pady=5)

tk.Label(root, text="Щиты:").grid(row=9, column=0, padx=5, pady=5)
first_side_shield_dropdown = ttk.Combobox(root, values=[""] + list(shields.keys()))
first_side_shield_dropdown.set("")
first_side_shield_dropdown.grid(row=9, column=1, padx=5, pady=5)

second_side_shield_dropdown = ttk.Combobox(root, values=[""] + list(shields.keys()))
second_side_shield_dropdown.set("")
second_side_shield_dropdown.grid(row=9, column=3, padx=5, pady=5)

tk.Label(root, text="Скакуны:").grid(row=10, column=0, padx=5, pady=5)
first_side_mount_dropdown = ttk.Combobox(root, values=[""] + list(mounts.keys()))
first_side_mount_dropdown.set("")
first_side_mount_dropdown.grid(row=10, column=1, padx=5, pady=5)

second_side_mount_dropdown = ttk.Combobox(root, values=[""] + list(mounts.keys()))
second_side_mount_dropdown.set("")
second_side_mount_dropdown.grid(row=10, column=3, padx=5, pady=5)

# Кнопка для расчета
calculate_button = tk.Button(root, text="Рассчитать", command=lambda: threading.Thread(target=calculate_battle).start())
calculate_button.grid(row=11, column=2, columnspan=2, pady=10, sticky="nsew")

# Результаты
results_text = tk.StringVar()
results_label = tk.Label(root, textvariable=results_text, justify="left", anchor="w")
results_label.grid(row=12, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()