

#!/usr/bin/env python
# coding=utf-8

import this
__metaclass__ = type


class Person:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def breast(self, n):
        self.breast = n

    def color(self, color):
        print(("%s is %s") % (self.name, color))

    def how(self):
        print(("%s breast is %s") % (self.name, self.breast))


girl = Person('canglaoshi')
girl.breast(90)

# girl.color("white")
# girl.how()

__metaclass__ = type


class DREAM:
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name

    def action(self, acts):
        self.action = "坚毅"

    def backg(self, hards):
        self.backg = "渺茫"

    def nums(self, n):
        self.nums = n

    def pr(self):
        print(("在%s的时候，%s依然%s的坚持了%s天的学习") % (self.backg,
                                             self.name, self.action, self.nums))


me = DREAM('Claire')
me.backg("1")
# me.action("g")
# 我的问题是，如果我不给这个me.action复制，他就会输出乱码，也不是我规定的内容，
# 这个问题可以解决？
me.nums(5)
me.pr()


class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCal(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCal()

    def __str__(self):
        return '\t'.join([self.name, str(self.value), str(self.calories)])


class Menu(object):
    def __init__(self):
        self.foodItems = []

    def add(self, foodItem):
        self.foodItems.append(foodItem)

    def __str__(self):
        """
             prints the food items
        """
        s = 'Item\tValue\tCalories'
        s += '
    '.join(str(f) for f in self.foodItems)
    return s


names = ['burger', 'fries', 'coke']
values = [1, 2, 3]
calories = [100, 200, 300]

m = Menu()
items = list(Food(n, v, c) for n, v, c in zip(names, values, calories))
m.foodItems = items
print(m)
