class Address:
    def __init__(self, index, city, street, building, appart):
        self.index = index
        self.city = city
        self.street = street
        self.building = building
        self.appart = appart

    def __str__(self):
        return (f'{self.index}, {self.city}, {self.street}'
                f' {self.building}, {self.appart}')
