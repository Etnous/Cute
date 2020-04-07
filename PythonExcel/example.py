import pandas as pd

df = pd.read_excel('cities.xlsx') #读取表格
df1 = df[['中文名', 'adcode', 'citycode']] #读取表头
citylist = df1[['citycode']].values.T.tolist()[:][0] #获取citycode列的值
citylist = list(set(citylist)) #消除重复项
data_dict = {}
#遍历城市列表
for city_list in citylist:
    df2 = df1.loc[df1['citycode'] == city_list] #找出同一城市或地区

    city = df2[['中文名']].values.T.tolist()[:][0] #所有地区变成列表
    n = len(city) #获取城市列表长度
    if n != 1: #如果不为1则将list[0]值加在后面列表元素前
        for i in range(1, n):
            city[i] = city[0] + city[i]
    code = df2[['adcode']].values.T.tolist()[:][0]
    data = pd.DataFrame({'column1':city, 'column2':code}) #格式化

    dd = data.groupby('column1').column2.apply(list).to_dict() #转字典
    data_dict.update(dd)

data_dict = str(data_dict)

with open('city_lists.py', 'w', encoding='utf-8') as f:
    f.write(data_dict)
