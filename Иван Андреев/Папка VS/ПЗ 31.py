######################################

new_item = {
    "title": "Маршрутизатор",
    "quantity": 12,
    "price": 4500,
    "temp_note": "Требует проверки"
}

print(f"Товар: {new_item['title']} | Начальное количество: {new_item['quantity']} шт.")

item_location = new_item.get("location", "Сектор не назначен")
print(f"Проверка сектора: {item_location}")

new_item["quantity"] = 15
new_item["location"] = "Сектор А-1"

if "temp_note" in new_item:
    removed_note = new_item.pop("temp_note")
    print(f"Удалена временная пометка: {removed_note}")

print("--- Карточка нового товара ---")
for key, value in new_item.items():
    print(f"{key}: {value}")

########################################

warehouse = [
    {"title": "Коммутатор", "quantity": 4, "price": 8200, "location": "Сектор Б-2"},
    {"title": "Сервер", "quantity": 2, "price": 65000, "location": "Сектор В-1"},
    {"title": "Монитор", "quantity": 9, "price": 14000, "location": "Сектор А-3"}
]

warehouse.append(new_item)
total_items = len(warehouse)
print(f"Всего позиций в базе склада: {total_items} шт.")

print(f"Первая позиция: {warehouse[0]['title']} | Последняя позиция: {warehouse[-1]['title']}")

warehouse[0]["title"] = "Управляемый коммутатор L3"
print(f"Обновленная первая позиция: {warehouse[0]['title']}")

max_item = warehouse[0]
min_item = warehouse[0]
total_cost = 0

for item in warehouse:
    total_cost += item["quantity"] * item["price"]
    if item["price"] > max_item["price"]:
        max_item = item
    if item["price"] < min_item["price"]:
        min_item = item

print(f"Общая стоимость склада: {total_cost} руб.")
print(f"Минимум по цене: {min_item['title']} ({min_item['price']} руб.) | Максимум по цене: {max_item['title']} ({max_item['price']} руб.)")

low_stock = []
for item in warehouse:
    if item["quantity"] < 10:
        low_stock.append(item["title"])

#######################################

print(f"Позиций с малым остатком (<10 шт.): {len(low_stock)} шт. -> {low_stock}")

with open("warehouse_report.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО СКЛАДУ ОБОРУДОВАНИЯ\n")
    for item in warehouse:
        file.write(f"Позиция: {item['title']} | Кол-во: {item['quantity']} шт. | Цена: {item['price']} руб. | Сектор: {item['location']}\n")

with open("warehouse_report.txt", "a", encoding="utf-8") as file:
    file.write("--- ИТОГИ АНАЛИТИКИ ---\n")
    file.write(f"Всего наименований: {total_items} шт. | Общая стоимость: {total_cost} руб.\n")
    file.write(f"Самый дорогой товар: {max_item['title']} ({max_item['price']} руб.)\n")
    file.write(f"Самый доступный товар: {min_item['title']} ({min_item['price']} руб.)\n")
    file.write(f"Требуют закупки (<10 шт.): {len(low_stock)} поз.\n")

with open("warehouse_report.txt", "r", encoding="utf-8") as file:
    saved_text = file.read()

print("--- Прочитано из файла warehouse_report.txt ---")
print(saved_text)