class House:

    def __init__(self, name, number_of_floors):
        """  Developer - не только разработчик  """
        self.name = name
        self.number = number_of_floors # количество этажей


    def go_to(self, new_floor):
        new_floor_1 = 0

        if new_floor > self.number or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)



h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h1.go_to(5)

h2.go_to(10)
