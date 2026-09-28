# ИМПОРТЫ ИМПОРТЫ, КАНДИДАТЫ...
import math

# Шо видит пользователь
data = "TARGET=полигон сектор 4 # V0=150.0 m/s # ANGLE=45 DEG"

# Первое. Пополамим строку на несколько частей.
parts = data.split("#")

target = parts[0].split("=")[1].strip() # стрипы уберают по краям пробелы
v0 = float(parts[1].split("=")[1].replace("m/s", "").strip()) # флоаты делают из строки чсило с **.0
angle_deg = float(parts[2].split("=")[1].replace("DEG", "").strip()) # реплейсы заменяют части текста, а сплиты разделяют

# второе. Переводим из градусов в радианы
angle_rad = math.radians(angle_deg)

# Третье. Рассчитываем предельную дальность
# R = (V0^2  sin(2  angle)) / g
g = 9.81
distance = (math.pow(v0, 2) * math.sin(2 * angle_rad)) / g

# 