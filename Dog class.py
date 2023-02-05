class Human:
    def __init__(self, name='Dog',
                 home=None, toy=None):
        self.name = name
        self.home = home

        self.gladness = 50  # Щастя
        self.satiety = 50  # Ситість

        def get_home(self):
            self.home = House()

        def eat(self):
            if self.food <= 0:
                self.search('food')

            else:
                if self.satiety > 100:
                    self.satiety = 100
                self.satiety += 5
                self.home.food -= 5

        def searching(self, manage):
            if self.food < 20:
                print('I am going to search food')

            elif manage == 'food':
                    print('I found food')
                    self.home.food += 10
                    self.satiety += 2


        def is_alive(self):
            pass


        def live(self, day):
            pass

        class House:
            def __init__(self):
                self.mess = 0
                self.food = 0