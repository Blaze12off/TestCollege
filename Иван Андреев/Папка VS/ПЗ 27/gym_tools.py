# Расчёт стоимости абон со скидкой
def calc_sub(price, discount=10):
    return price * (1 - discount / 100)

# Рекурс таймер подходов
def rep_timer(n):
    if n == 0:
        print("Подход завершён!")
        return
    print(n)
    rep_timer(n - 1)
