#йоу
name_pasajir = input("Введите своё Имя ")
posadka_prise = float(input("Введите стоимость Посадки "))
km_prise = float(input("Введите стоимость одного километра "))
km_tall = float(input("Введите расстояние поездки (в км) "))
waiting_prise_min = float(input("Введите стоимость ожидания за минуты "))
waiting_number_min = int(input("Введите количество минут ожидания "))

# Скучные расчеты и тд тп бтв кд хз ТЗ ПЗ ПВЗ дз ЦДЗ мэш
doroga = posadka_prise + (km_prise * km_tall)
waiting_main = waiting_prise_min * waiting_number_min
objaya_summa = doroga + waiting_main
full_ten_km = int(km_tall) // 10
videlenie_km = km_tall % 10

# ЫЫЫЫ ПРИНТЫЫЫЫ
print()
print("===========ТЕКСТ КОРОЧЕ ТИПО ЗАГОЛОВОК==========")
print("Пассажир", name_pasajir, sep=":", end="\n")
print(f"Стоимость поездки: {doroga:.2f} руб.")
print(f"Стоимость ожидания: {waiting_main:.2f} руб.")
print(f"Итоговая сумма: {objaya_summa:.2f} км.")
print(f"Кол-во полных 10-км-ых отрезков: {full_ten_km:.2f} шт.")
print(f"Кол-во минут: {videlenie_km:.2f} км.")
print("===============================================")