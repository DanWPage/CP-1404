
class Guitar:
    CURRENT_YEAR = 2017

    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = int(cost)

    def __str__(self):
        return '{} ({}), ${:.2f}'.format(self.name, self.year, self.cost)

    def get_age(self):
        return self.CURRENT_YEAR - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
