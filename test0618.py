# #!/usr/bin/env python
# #!/usr/bin/env python
# # coding:utf-8

# # """
# # 请计算19+2*4-8/2
# # """
# # import operator
# # a = 19+2*4-8/2
# # print(a)
# # print("sgui\
# # yj")
# # print("tyu1111111 \r"+"pyh"+"hhh" + repr({"hukdh"}) + "ddd")
# # help(divmod)
# # # q = input("输入你想输入的：")
# # # print(q)
# # # print("www")
# # print("i like\n python")
# # path = r"www:\uu\df"
# # print(path)

# # # name = input("输入你的名字：")
# # # age = input("your Age：")
# # # print(name+"\000is\000" + age + "\000this year!")
# # help(input)
# # test = "study.python.while.drinking.gin!"
# # print(test.index("p"))
# # print(test[1])
# # print(test[0:3])
# # # print(dir(test))
# # print(test.split(".", 3)[0])
# # print(ord("a"))
# # print(operator.lt("z", "ab"))
# # test01 = "i have {0} {1} {2} juice!\000{xixi}".format(
# #     3, "bottles", "of", xixi="i wont give it to u")
# # print(test01)
# # test03 = {"i", "have", "a", "glass"}
# # print(dir(test03))
# # print(type(test03))
# # test04 = ["i", "have", "a", "glass"]
# # test05 = [2, 3, 2, 4]
# # print(test04.index("have"))
# # print(type(test04))
# # print(type(test05))
# # test06 = test05.copy()
# # print(test06)
# # list1 = [["历史", "2367364788g2323232", "222"], [1, 2, 2], [3], ["1", 2]]
# # print(list1[1][0])
# # list2 = list1[::-1]
# # print(list2)
# # str2 = "hjkshkdds"
# # list3 = ["你好吗", 232, "fmkl"]
# # list4 = str2.__add__("fmkl")
# # list5 = list1.sort(reverse=True)
# # print(list5)
# # str3 = str2[0]+"123"+str2[2:]
# # print(str3)
# # s = "I am, writing\npython\tbook on line"
# # print(s)
# # s1 = s.split()
# # print(s1)
# # s2 = "❤".join(s1)
# # print(s2)
# import copy
# app = ["facetune", "instgram", "alipay", "wechat"]
# functions = ["ps", "post selfish", "finance", "social"]

# print('{}:{}'.format(app[1], functions[1]))
# # 用list建立dict
# dailylife = (["facetune", "ps"],
#              ["instgram", "post selfish"], ["wechat", "chatting"])
# # tuple建立dict
# daily = dict(dailylife)
# print(daily["facetune"])
# # tuple建立dict
# dailylife2 = {}.fromkeys(("12", "123", "233"), ("city"))
# print(dailylife2)
# # 用tuple建立dict

# # print(len(dailylife2))
# print(("i like app facetune,cuz i can use it do {}").format(
#     daily["facetune"]))
# print(("i like app instgram,cuz i can use it do %(instgram)s") % daily)
# # dict 的两种骚操作用法

# list1 = {'cl': ['python', 'c++', "c++"], 'nihao': 'haixing'}
# list2 = list1.copy()
# list3 = copy.deepcopy(list1)
# print(list2)
# # 浅复制
# list1["cl"].remove(, "c++")
# del(list1["nihao"])
# print(list2)
# # 深复制
# print(list3)
# print(help(list.remove))
# set 就是集合,frozenset不能改变
# a_set = set("woshiset")
# b_set = frozenset("woyeshiset")
# a_set.update("aaab")
# print(a_set)
# print("i" in a_set)
# print(a_set > b_set)
# print(a_set.intersection(b_set))
# print(a_set)
# x = 5
# x += 1
# x = 5, "gdkldjf"
# print(x)
# x = int(input("请输入十:"))
# if x == 10:
#     print("wonderful")
# else:
#     print("youre wrong")
# # input 输入的值是字符串，需要转换成别的格式
# Y = "I LOVE U " if 1 > 2 else"i dont know you"
# print(Y)
# #x=a if bool else b的用法
# i = []
# string1 = "qwertyu"
# for i in string1:
#     print(i, end="")
# y = type(range(len(string1)))
# print(y)

# list1 = ["nihao", "halo", "hello"]
# for i in list1:
#     print(i)
# from math import sqrt
# import random
# i = []
# x = range(0, 8, 2)
# for i in x:
#     print(i)
# test_list = ["1", "2", "rrrr"]
# x = range(len(test_list))
# print(x)

# i = []
# beiwuzhengchu = []
# x1 = range(0, 88)
# for i in x1:
#     if i % 5 == 0:
#         beiwuzhengchu.append(i)
#         print(i)
# print(beiwuzhengchu)
# dic1 = {"lag": "python", "tag": "free", "book": "dictoinary"}
# print(type(dic1))
# K = []
# V = []
# for K, V in dic1.items():
#     print(K, "==>", V)
# for 循环语句可用于list， tuple ，set和dict中，dict有些常用的要注意。
#  items，keys，values，itervalue

# list1 = [(1, 2), ("ert", 77), (12, 34)]
# set1 = ("qq", "ss", "wes")
# X = zip(*list1)
# print(X)
# for K in X:
#     print(K)
# string0 = "i like dog! doggy is so cute"
# Y = enumerate(string0)
# print(Y)
# for K, V in Y:
#     if "dog" in V:
#         Y[K] = "Dennis"


# for K in Y:
#     print(K)

# x = []
# squares = [x*(x+1) for x in range(1, 10)]
# print(squares)

# one = []
# mybag = [' glass', '    apple', 'green leaf ']

# l = ['01', '1.0', '[0.2]']
# l = [i.strip('[]') for i in l]
# print(l)
# newbag = [one.strip()for one in mybag]
# print(newbag)

# test = 123
# print(("lalala %d") % test)

# rightnum = random.randint(1, 100)
# guess = 0
# while True:
#     yournum = input("请输入你认为可能对的数字：")
#     guess = guess+1
#     if not yournum.isdigit():
#         print("请输入整数好吧，你是狗吧")
#         break
#     elif int(yournum) < 0 or int(yournum) > 100:
#         print("请输入100以内的数好吧···")
#     else:
#         if rightnum == int(yournum):
#             print(("你这个天才，答对了！才第 %d 次就猜对了") % guess)
#         elif rightnum > int(yournum):
#             print("你猜的小了")
#         elif rightnum < int(yournum):
#             print("你猜的大了")
# #数字游戏结束了哦！

#!/usr/bin/env python
# coding=utf-8

# import math
# for n in range(2, 1, -1):
#     root = math.sqrt(n)
#     if root == int(root):
#         print(n)
#         break

# # else:
#     # print("Nothing.")
# for 和else的用法

# import os
# path = "C:/Users/heke/Documents/WeChat Files/Mandy37forever/FileStorage/File/2020-06/test0714.txt"
# f = open(path, encoding="utf-8", errors="ignore")
# # for i in f:
# #     print(i)
# # f.close()
# fw = open(path, "w")

# fw.write("You Raise Me Up When I am down and, oh my soul, so weary;\n When troubles come and my heart burdened be;\n")
# fw.close()
# f = open(path)
# for a in f:
#     print(a)
# list1 = ["wdddd", 123, 344]
# iterss = iter(list1)
# a = iterss.__next__()
# print(a)
# while True:
#     LINE = f.readlines()
#     if not LINE:
#         break
#     print(LINE)
# f1 = f.readline()
# f2 = f.readline()
# print(f1)
# print(f2)
# f.seek(10)
# f3 = f.readline()
# print(f3)
# file_state = os.stat(path)
# print(file_state)
# 练习题，随机数给出40个数的列表。


# list1 = []
# bujige = []
# r_bujige = []
# for i in range(1, 40, 1):
#     a = random.randint(0, 100)
#     list1.append(a)
# print(list1)
# ava = numpy.average(list1)
# print(ava)
# for i in list1:
#     if i < ava:
#         bujige.append(i)
# print(bujige)
# bujige.sort(reverse=True)
# print(bujige)

# 有关字符串的练习：
# string1 = "i love code   !"
# list2 = string1.split()
# print(list2)
# string2 = "   ".join(list2)
# print(string2)

import random
import numpy
import A
print(A.main.__doc__)

print(A.main(1, 2))


def mian(a, b):
    y = a+b
    print(y)


mian(1, 2)
print("dfghjk=",)
