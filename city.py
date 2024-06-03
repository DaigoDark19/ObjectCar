from car_for_city import (
    Car
    )

from core.city_exception import (
    InitCarError,
    LimitMapError
)

from linked_node import (
    LinkedList
)


class CityMap():
    def __init__(self) -> None:
        self.road: int = 0
        self.edifcio: int = 1
        self._base: list[list[list]] = []
        self.size_map: int = 20
        self.cars: LinkedList = LinkedList()
        self.cars_mov: LinkedList = LinkedList()

    def create_base_2(self):
        i: int = 1  # que es esto? -> Index
        i2: int = 0  # que es esto? -> Index2
        a: bool = True  # que es esto? -> auto
        for _ in range(self.size_map):
            lista: list[int | Car] = []
            for _ in range(self.size_map):
                if a:
                    n = self.road
                    if i == 4:
                        i = 0
                    if i >= 2:
                        n = self.edifcio
                    lista.append(n)
                    i += 1
                    continue
                lista.append(self.road)
            self._base.append(lista)

            i2 += 1
            i = 1
            if i2 == 2:
                a = not a

                i2 = 0

    def init_car(self, y: int, x: int, car: Car):

        car.init_x = x
        car.new_x = x
        car.x = x

        car.init_y = y
        car.new_y = y
        car.y = y

        if (
            self._base[car.init_y][car.init_x] == 1 or
            self._base[car.init_y][car.init_x] == Car
                ):
            raise InitCarError()
        self.cars.append(car)
        self._base[car.init_y][car.init_x] = car
        car.init = True

    def is_space_occupied(self, x: int, y: int) -> bool:
        return self._base[y][x] == 1 or isinstance(self._base[y][x], Car)

    def ver_x(self, car: Car) -> int:
        old_x: int = car.x
        new_x: int = car.new_x
        old_y: int = car.new_y

        if old_x > new_x:
            distancia: int = old_x - new_x
            contador: int = 0
            for _ in range(distancia):
                contador += 1
                if self.is_space_occupied(old_x - contador, old_y):
                    car.new_x = old_x - contador + 1
                    return old_x - contador + 1

        for e in range(old_x, new_x+1):
            if self.is_space_occupied(e + 1, old_y):
                car.new_x = e
                return e
        return car.new_x

    def ver_y(self, car: Car) -> int:
        old_y: int = car.y
        new_y: int = car.new_y
        old_x: int = car.new_x

        if old_y > new_y:
            distancia: int = old_y - new_y
            contador = 0
            for _ in range(distancia):
                contador += 1
                if self.is_space_occupied(old_x, old_y - contador):
                    car.new_y = old_y + contador - 1
                    return old_y - contador + 1

        for e in range(old_y, new_y+1):
            if self.is_space_occupied(old_x, e+1):
                car.new_y = e
                return e
        return car.new_y

    def check_mov(self):
        current = self.cars.head
        while current is not None:
            if current.data.mov is True:
                self.cars_mov.append(current.data)
            current = current.next

    def jump(self):
        self.check_mov()
        current = self.cars_mov.head
        while current is not None:
            current.data.mov = False
            x: int = current.data.x
            y: int = current.data.y
            new_x: int = self.ver_x(current.data)
            new_y: int = self.ver_y(current.data)

            if new_x >= self.size_map or new_y >= self.size_map:
                raise LimitMapError()

            if (current.data.init and self._base[current.data.init_y][current.data.init_x] != Car):
                self._base[current.data.init_y][current.data.init_x] = 0
                current.data.init = False

            self._base[y][x] = 0
            self._base[new_y][new_x] = current.data
            current.data.mov = False
            current = current.next
        self.cars_mov.delete_all()

    def __str__(self) -> str:

        for i in self._base:
            print(i)
        return ''
