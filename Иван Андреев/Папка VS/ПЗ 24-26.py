import random
import time

time.sleep (2.0)

total_sum = 0
count = 0

for num in range(20, 71):
    if num % 5 == 0:
        total_sum += num
        count += 1

print(f"Диапазон [20, 70]:")
print(f"Количество найденных чисел: {count}")
print(f"Сумма чисел: {total_sum}")

time.sleep (4.0)

numbers = [random.randint(-30, 80) for _ in range(8)]
limit = 150
current_sum = 0

for item in numbers:
    if item <= 0:
        continue
    current_sum += item
    print(f"Добавлено число: {item}, текущая сумма: {current_sum}")
    if current_sum > limit:
        print(f"Лимит {limit} превышен! Остановка цикла.")
        break

print(f"Итоговая сумма: {current_sum}")

time.sleep (4.0)

def total_cost(price, count=4):
    cost = price * count
    return cost

order1 = total_cost(300)
print(f"Стоимость 1 товара (по умолчанию): {order1} руб.")

order2 = total_cost(300, count=2)
print(f"Стоимость 2 товаров: {order2} руб.")