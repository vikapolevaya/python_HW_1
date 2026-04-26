from smartphone import Smartphone
catalog = []

phone1 = Smartphone("Марка1", "Модель1", "+79000000001")
phone2 = Smartphone("Марка2", "Модель2", "+79000000002")
phone3 = Smartphone("Марка3", "Модель3", "+79000000003")
phone4 = Smartphone("Марка4", "Модель4", "+79000000004")
phone5 = Smartphone("Марка5", "Модель5", "+79000000005")

catalog.extend([phone1, phone2, phone3, phone4, phone5])

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
