import csv
import hashlib

raw_deliveries = [
    ["code", "title", "category", "qty", "price"],
    [" sw-01 ", "Коммутатор; 24 порта", "Сеть", "4", "12500"],
    ["srv-02", "Сервер стоечный", "Серверы", "2", "95000"],
    ["cab-03", "Патч-корд 5м", "Сеть", "20", "ошибка_цены"],
    ["ups-04", "ИБП модульный; 3000VA", "Питание", "3", "32000"],
    [" srv-05 ", "Дисковая полка", "Серверы", "1", "64000"]
]

with open("incoming_stock.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerows(raw_deliveries)

with open("incoming_stock.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file, delimiter=";")
    header = next(reader)
    loaded_rows = list(reader)





print(f"Шапка таблицы: {header} | Строк данных: {len(loaded_rows)}")

clean_items = []
quarantine_log = []

for row in loaded_rows:
    try:
        qty = int(row[3])
        price = int(row[4])
        code = row[0].strip().upper()
        title = row[1].strip()
        category = row[2].strip()
        total = qty * price
        clean_items.append({
            "code": code,
            "title": title,
            "category": category,
            "qty": qty,
            "price": price,
            "total": total
        })
    except ValueError:
        quarantine_log.append(row[0].strip())

print(f"Принято позиций: {len(clean_items)} | В карантине (ошибка данных): {quarantine_log}")

clean_items.sort(key=lambda item: item["total"], reverse=True)

leader = clean_items[0]
print(f"Лидер по стоимости: {leader['code']} ({leader['title']}) -> {leader['total']} руб.")

priority_codes = []
for item in clean_items:
    if item["total"] > 60000:
        priority_codes.append(item["code"])

print(f"Крупные поставки (>60000 руб.): {priority_codes}")

category_totals = {}
for item in clean_items:
    category = item["category"]
    category_totals[category] = category_totals.get(category, 0) + item["total"]

print(f"Сводка по категориям: {category_totals}")





try:
    with open("backup_archive.csv", "r", encoding="utf-8") as file:
        backup_data = file.read()
except FileNotFoundError:
    print("Проверка защиты: файл backup_archive.csv не найден, работа продолжена")

fields = ["code", "title", "category", "qty", "price", "total"]

with open("verified_stock.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields, delimiter=";")
    writer.writeheader()
    writer.writerows(clean_items)

restored_items = []
with open("verified_stock.csv", "r", encoding="utf-8", newline="") as file:
    for row in csv.DictReader(file, delimiter=";"):
        restored_items.append({
            "code": row["code"],
            "title": row["title"],
            "category": row["category"],
            "qty": int(row["qty"]),
            "price": int(row["price"]),
            "total": int(row["total"])
        })

assert clean_items == restored_items

print(f"Тест целостности Round-Trip: УСПЕШНО ({len(restored_items)} из {len(clean_items)} записей идентичны)")

with open("verified_stock.csv", "rb") as file:
    file_hash = hashlib.sha256(file.read()).hexdigest()

print(f"Контрольная сумма SHA-256 (первые 16 симв.): {file_hash[:16]}")