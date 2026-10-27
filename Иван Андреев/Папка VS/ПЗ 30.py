import time
#товары
print()
print() #для красоты)
print()
print()
time.sleep(2.0)
products = ["Ноутбук", "Монитор", "Клавиатура", "Мышь", "Наушники"]
print(f"Первый товар: {products[0]} | Последний товар: {products[-1]}")
print(f"Предпоследний товар: {products[-2]}")
products[2] = "Игровая клавиатура"
print(f"Всего товаров ({len(products)} шт.): {products}")
time.sleep(5.2)
print()
print() #след задание
print()
print()

#очередь
orders = ["Заказ #101", "Заказ #102", "Заказ #103"]
orders.append("Заказ #104")
orders.append("Заказ #105")
orders.insert(0, "VIP-Заказ #100")
print(f"После добавления: {orders}")
orders.remove("Заказ #102")
last_order = orders.pop()
print(f"Отдан курьеру с конца: {last_order}")
print(f"Осталось в очереди: {orders}")
time.sleep(6.66)
print()
print()#третье
print()
print()

sales = [30, 45, 50, 40, 65, 90, 80]
переменная = sales[4:]
first_three = sales[0:3]
workdays = sales[:5]
weekends = sales[5:]
reversed_sales = sales[::-1]
print(f"Первые 3 дня [0:3]: {first_three}")
print(f"Рабочие дни [:5]: {workdays}")
print(f"Выходные дни [5:]: {weekends}")
print(f"Обратный порядок: {reversed_sales}")
print(f"переменная для препода [4:]: {переменная}")

print()#4-е
print()
print()
print()
time.sleep(6.7)

checks = [1200, 450, 8500, 3200, 300, 15000, 900, 6400]
min_check = checks[0]
max_check = checks[0]
vip_checks = []
small_checks = []

for price in checks:
    if price > max_check:
        max_check = price
    if price < min_check:
        min_check = price
    if price >= 5000:
        vip_checks.append(price)
    if price < 1000:
        small_checks.append(price)

print(f"Самая дешевая покупка (минимум): {min_check} руб.")
print(f"Самая дорогая покупка (максимум): {max_check} руб.")
print(f"Крупные VIP-чеки (>= 5000 руб.): {vip_checks} (Всего: {len(vip_checks)} шт.)")
print(f"Мелкие чеки (< 1000 руб.): {small_checks} (Всего: {len(small_checks)} шт.)")

print()
print()
print() #пятое
print()
time.sleep(5.2)

temps = [-12, -18, -5, -25, -10, -30, -8]
min_t = temps[0]
max_t = temps[0]
frost_days = []

for t in temps:
    if t < min_t:
        min_t = t
    if t > max_t:
        max_t = t
    if t < -15:
        frost_days.append(t)

print(f"Минимум: {min_t} °C | Максимум: {max_t} °C | Сильные морозы (< -15 °C): {frost_days}")
print()
print() ###########theEnd################
print()
print()