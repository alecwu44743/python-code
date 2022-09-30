class DateTime:
    year_from = -5000
    year_to = +4000
    def __init__(self, year, month, day, hour, minute, second):
        self.set_year(year) 
        self.set_month(month) 
        self.set_day(day) 
        self.set_hour(hour) 
        self.set_minute(minute) 
        self.set_second(second)

    def check_and_set(self, field_name, field_value, L, U):
        if not (L <= field_value <= U):
            raise ValueError('{} must be in range {}-{}'.format(field_name, L, U))
        self.__dict__['_'+field_name] = field_value

    def set_year(self, year):
        # if type(year) != int: 
        #     raise TypeError('year must be integer')
        # self._year = year
        self.check_and_set('year', year, self.year_from, self.year_to) # class attr

    @classmethod
    def set_year_range(cls, L, U):
        cls.year_from, cls.year_to = L, U

    def set_month(self, month):
        self.check_and_set('month', month, 1, 12)

    def get_month(self):
        return self._month

    month = property(lambda self: self.get_month(), \
                     lambda self, v: self.set_month(v))
    
    @staticmethod
    def leap(year):
        return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) # no self, no cls

    def set_day(self, day):
        if self._month in {1,3,5,7,8,10,12}: self.check_and_set('day', day, 1, 31)
        elif self._month in {4, 6, 9, 11}: self.check_and_set('day', day, 1, 30)
        elif leap(self._year): check_range('day', day, 1, 29)
        else: self.check_and_set('day', day, 1, 28)
    
    def set_hour(self, hour):
        self.check_and_set('hour', hour, 0, 23)

    def set_minute(self, minute):
        self.check_and_set('minute', minute, 0, 59)
    
    def set_second(self, second):
        self.check_and_set('second', second, 0, 59)

    
        
def check_range(field_name, field_value, L, U): 
    if not (L <= field_value <= U):
        raise ValueError(f'{field_name} must be {L}..{U}')