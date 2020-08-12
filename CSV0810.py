import csv
csv_path = r'C:\Users\heke\Documents\WPS Cloud Files\262005716\mychart123.csv'

with open(csv_path, 'r', encoding='utf8') as csvfile:
    mpg = list(csv.DictReader(csvfile))

# print(mpg[:3])
# print(len(mpg))
# print(mpg[0].keys())  # 第一行的标题内容
# print(sum(float(d['height']) for d in mpg) / len(mpg))  # 求 某一键值的平均数
Ctysalary = []  # 建立目标list、
print(1)
city = set(d['location'] for d in mpg)  # 这里要用set，排除重复的元素
print(city)
for c in city:  # iterate over all the cylinder levels
    sumsalary = 0
    personcount = 0
    for d in mpg:  # iterate over all dictionaries
        if d['location'] == c:  # if the cylinder level type matches,
            sumsalary += float(d['salary'])  # add the cty mpg
            personcount += 1  # increment the count
    # append the tuple ('cylinder', 'avg mpg')
    Ctysalary.append((c, sumsalary / personcount))

print(Ctysalary)  # 计算出每个城市的平均薪水
Ctysalary.sort()
print(Ctysalary)
