import timeit
import pandas as pd  # 文件命名问题，擦，不能用pandas命名
import numpy as np

pd.Series
animals = ['Tiger', 'Bear', 'Moose']
numbers = [1, 2]  # 这里加了none，就会变成float64
print(pd.Series(numbers))
print(pd.Series(animals))
print(np.nan == None)
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
print(s)
s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
print(s)
s = pd.Series(np.random.randint(0, 1000, 10000))
s = np.random.randint(0, 1000, 10000)
print(s)
# print(s.head(8))

s = pd.Series(np.random.randint(0, 1000, 10000))
print(dir(pd))
% % timeit - n 10
for label, value in s.iteritems():
s.loc[label] = value+2
