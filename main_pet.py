# все задания к "Дому питомца"

class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    # Метод для получения имени

    def get_name(self):
        return self.name

    # Метод для получения пола
    def get_sex(self):
        return self.sex

    # Метод для получения возраста
    def get_age(self):
        return self.age


class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"Клиент: {self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."

    def get_info(self):
        return f"{self.name} {self.surname}, {self.city}"


client_1 = Client("Вася", "Иванов", "Омск", 650)
client_2 = Client("Петя", "Жуков", "Вологда", 130)
client_3 = Client("Катя", "Миронова", "Москва", 200)
client_4 = Client("Катя", "Антонова", "Москва", 20)

clients = [client_1, client_2, client_3, client_4]


for client in sorted(clients, key=lambda cli: cli.surname):
    print(client.get_info())


class Guest (Client):
    def __init__(self, name, surname, city, balance, status):
        super().__init__(name, surname, city, balance)
        self.status = status

    def get_guest(self):
        return f"{self.name} {self.surname}, {self.city}, Статус: {self.status}"


guest_1 = Guest("Вася", "Иванов", "Омск", 650, "Наставник")
guest_2 = Guest("Петя", "Жуков", "Вологда", 130, "Тренер")
guest_3 = Guest("Катя", "Миронова", "Москва", 200, "Покупатель")
guest_4 = Guest("Катя", "Антонова", "Москва", 20, "Покупатель")

guests = [guest_1, guest_2, guest_3, guest_4]


for guest in sorted(guests, key=lambda gue: gue.surname):
    print(guest.get_guest())