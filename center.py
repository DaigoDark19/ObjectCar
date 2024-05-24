from city import CityMap
from car_for_city import (
    Car,
    ColorClass,
    MarcasClass
)


# python archivo.py ---
def car_test():

    supra = Car(
                color=ColorClass.NEGRO.name,
                marca=MarcasClass.TOYOTA.name,
                modelo="supra",
                wheels_info=[
                    {
                        'MARCA': MarcasClass.TOYOTA,
                        'COLOR': ColorClass.AZUL
                    }
                    ],
                doors_info=[
                    {
                        'COLOR': ColorClass.AZUL
                    }
                ],
                tanq_gaso_max=100
            )

    corsa = Car(
                color=ColorClass.NEGRO.name,
                marca=MarcasClass.TOYOTA.name,
                modelo="corsa",
                wheels_info=[
                    {
                        'MARCA': MarcasClass.TOYOTA,
                        'COLOR': ColorClass.AZUL
                    }
                    ],
                doors_info=[
                    {
                        'COLOR': ColorClass.AZUL
                    }
                ],
                tanq_gaso_max=100
            )

    city = CityMap()

    city.create_base_2()

    city.init_car(2, 0, supra)
    city.init_car(2, 1, corsa)

    corsa.create_engine()
    corsa.create_doors()
    corsa.start()

    # Car
    supra.create_engine()
    supra.create_doors()
    supra.start()
    corsa.acelerar(10)
    corsa.arriba()

    city.update_map()
    print(city)


if __name__ == '__main__':
    car_test()
