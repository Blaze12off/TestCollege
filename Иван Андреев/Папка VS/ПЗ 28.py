import random
import time

a = random.randint(-50,15000)
b = random.randint(300,500)
c = random.randint(4000,6000)
d = random.randint(100,200)
e = random.randint(-10000,8000)
f = random.randint(20,600)

def calculate_cashback(purchases, min_amount=600):
    total_cashback = 0
    for amount in purchases:
        if amount <= 0:
            continue
        if amount >= 12000:
            break
        if amount >= min_amount:
            total_cashback += amount * 0.07
    return total_cashback

checks = [a, b, c, d, e, f]
result = int(calculate_cashback(checks))
print("")
print(f"               Начислен кешбек в размере: {result} баллов!")
print("")

time.sleep(2.0)

assert int(calculate_cashback([600])) == 42, "Тест 1: чек ровно 600 не дал кешбек верно."
assert calculate_cashback([-12300, 0, -1000]) == 0, "Тест 2: возвраты не были проигнорированы."
assert calculate_cashback([13700, 12000, 39999]) == 0, "Тест 3: остановка после 12к не выполнилась."
assert calculate_cashback([]) == 0, "Тест 4: ошибка пустого ввода."
print("'''Все 4 тест-кейса пройдены! Функция calculate_cashback работает правильно.'''")
print("")
print("")
print("")
print("")

time.sleep(2.0)