from gym_tools import calc_sub, rep_timer

# Вызов 1. скидка по умолчанию 10%
sub1 = calc_sub(3000)
print(f"По умолчанию: {sub1:.0f} руб.")
# Вызов 2. скидка передана именованным аргументом
sub2 = calc_sub(3000, discount=20)
print(f"Со скидкой 20%: {sub2:.0f} руб.")

# Запуск рекурс таймера
print("Запуск таймера:")
rep_timer(5)
