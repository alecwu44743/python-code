import random as rd
import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # def printList(self):
    #     temp = self.head
    #     while temp:
    #         print(temp.data)
    #         temp = temp.next

class Point:
    count = 0 # class attribute
    def __init__(self, x, y): # two underscores before and after
        self.x = x # save param x as atrribute of self
        self.y = y # save param y as atrribute of self
        self.serial = Point.count
        Point.count += 1    
        
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    @property
    def r(self):
        return math.sqrt(self.x **2 + self.y **2)
    
    @property
    def theta(self):
        return math.atan(self.y / self.x) * 180 / math.pi

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy
    
    radius = r

    @property
    def area_as_circle(self):
        return math.pi * self.r() ** 2

    @property
    def area_as_rectangle(self):
        return self.x * self.y

class DateTime:
    def __init__(self, year, month, day, hour, minute, second):
        self.set_year(year) 
        self.set_month(month) 
        self.set_day(day) 
        self.set_hour(hour) 
        self.set_minute(minute) 
        self.set_second(second)

    def set_year(self, year):
        if type(year) != int: 
            raise TypeError('year must be integer')
        self._year = year

    def set_month(self, month):
        check_range('month', month, 1, 12)
        self._month = month

    def set_day(self, day):
        if self._month in {1,3,5,7,8,10,12}:check_range('day',day,1,31) 
        elif self._month in {4, 6, 9, 11}: check_range('day',day,1,30) 
        # elif leap(self._year): check_range('day',day,1,29) 
        else: check_range('day',day,1,28) 
        self._day = day
    
    def set_hour(self, hour):
        check_range('hour', hour, 0, 23) 
        self._hour = hour

    def set_minute(self, minute):
        check_range('minute', minute, 0, 59)
        self._minute = minute
    
    def set_second(self, second):
        check_range('second', second, 0, 59)
        self._second = second
        
def check_range(field_name, field_value, L, U): 
    if not (L <= field_value <= U):
        raise ValueError(f'{field_name} must be {L}..{U}')

def proc_move_by(p, dx, dy):
    p.x += dx
    p.y += dy

def find_pi():
    pass

def rec_find(L, val):
    if type(L) in {list, tuple}:
        for i,v in enumerate(L):
            p = rec_find(v, val)
            if p == True:
                return (i, )
            if p != False:
                return p + (i,)
    return L == val

def indent_list(L, level=0): # L = ['1', ['4', '5', ['8']], '2', '3', 'a3', ['6', '7']]
    # base case : string => print indent before string
    # recursive case : string => increase indentation level by 1
    if L == None:
        return
    if type(L) in {list, tuple}:
        for child in L:
            indent_list(child, level+1)
    else:
        print(f'{" "*4*level}{L}')

def number_outline(L, prefix=()):
    if type(L) in {list, tuple}:
        # keep prefix[-1], extend by new dimension, string from 1
        i = 0
        for v in L:
            if type(L) in {list, tuple}:
                i += 1
            number_outline(v, prefix + (i,))
            # don't increamt if v is a list/tuple
    # otherwise, indent and join the prefix together by '.'
    else:
        s = ' ' * 4 * (len(prefix)-1)
        s += '.'.join(map(str, prefix))
        s += '. ' + L
        print(s)

def magicSquare():
    n = 5
    square = [[0]*n for i in range(n)]

    square[0][int((n-1)/2)] = 1
    value = 2
    i = 0
    j = int((n-1)/2)

    while value <= n**2:
        p = (i-1) % n
        q = (j-1) % n

        if p < 0: p = n-1
        if q < 0: q = n-1

        if square[p][q] != 0:
            i = (i+1) % n
        else:
            i = p
            j = q

        square[i][j] = value
        value += 1

    printSquare(square, n)

def printSquare(square, n):
    for i in range(n):
        for j in range(n):
            print(square[i][j], end=' ')
        print('\n')

def no(L, prefix=()):
    if type(L) in {list, tuple}:
        i = 0
        for v in L:
            if type(v) not in {list, tuple}:
                i += 1
            no(v, prefix + (i,))
    else:
        s = ' ' * 4 * (len(prefix)-1)
        s += '.'.join(map(str, prefix))
        s += '. ' + L
        print(s)

            
# try:
    # llist = LinkedList()

    # llist.head = Node(1)
    # second = Node(2)
    # third = Node(3)

    # llist.head.next = second
    # second.next = third

    # llist.printList()
    
L = ['Jack', ['Harry', 'Bob', ['Tom', 'Alice']], 'Kevin', ['Tony', ['Gina'], 'Jay']]


# L = ['01', ['04', '05', ['08']], '02', '03', 'a3', ['06', '07']]
print(L)
    # indent_list(L)
no(L)

    # magicSquare()

# p = Point(4, 3)
# print(str(p.r()))
# print(str(p.theta()))

# except:
#     print("Something went wrong...")