import random

class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.satiety = 50
        self.gladness = 50

    def get_home(self):
        pass
    def get_car(self):
        pass
    def get_job(self):
        pass

    def eat(self):
        pass
    def work(self):
        pass
    def shopping(self):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass
    def to_repair(self):
        pass

    def days_indexes(self):
        pass
    def is_alive(self):
        pass
    def live(self):
        pass

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_of_car[self.brand]['fuel']
        self.strength = brand_of_car[self.brand]['strength']
        self.consumption = brand_of_car[self.brand]['consumption']



brand_of_car = {'BMW': {'fuel': 100, 'strength': 100, 'consumption': 6},
                'Lada': {'fuel': 50, 'strength': 40, 'consumption': 10},
                'Volvo': {'fuel': 70, 'strength': 150, 'consumption': 8},
                'Ferrari': {'fuel': 80, 'strength': 120, 'consumption': 14}}