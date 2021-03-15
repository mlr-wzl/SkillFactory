# задание 1.8.1
from main_pet import Cat

cat1 = Cat("Барон", "мальчик", 2)
cat2 = Cat("Сэм", "мальчик", 2)

print("Котик 1:", cat1.get_name(), "-", cat1.get_sex(), "-", cat1.get_age(), "года")
print("Котик 2:", cat2.get_name(), "-", cat2.get_sex(), "-", cat2.get_age(), "года")