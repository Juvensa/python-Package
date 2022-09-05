#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1）导入pandas库
import pandas as pd

#2）打印pandas版本信息
pd.__version__


# In[4]:


#3）打印pandas依赖包及其版本信息
pd.show_versions()


# In[6]:


#）创建一个如下图所示的DataFrame(df)，用data做数据，labels做行索引
import numpy as np
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
      'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
      'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
      'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data=data, index=labels)
df


# In[8]:


#5）显示有关此df及其数据的基本信息的摘要
df.describe()
# 或 df.info()


# In[9]:


#6）查看此df的前三行数据
df.head(3)#


# In[10]:


#7）选择df中列标签为animal和age的数据
df.loc[:, ['animal', 'age']]


# In[11]:


#8）选择行为[3, 4, 8]，且列为['animal', 'age']中的数据
df.iloc[[3, 4, 8]].loc[:, ['animal', 'age']]
# 或
df.loc[df.index[[3, 4, 8]], ['animal', 'age']]


# In[14]:


df[df['visits']>2]


# In[15]:


#10）选择age为缺失值的行
df[df['age'].isnull()]


# In[16]:


#11）选择animal为cat，且age小于3的行
df[(df['animal']=='cat') & (df['age']<3)]


# In[17]:


#12）将f行的age改为1.5
df.loc['f', 'age'] = 1.5
df


# In[18]:


#13）计算visits列的数据总和
df['visits'].sum()


# In[20]:


#）计算每种animal的平均age
df.groupby('animal')['age'].mean()


# In[21]:


#）计算每种animal的个数
df.groupby('animal').size()
#或
df['animal'].value_counts()


# In[26]:


#）先根据age降序排列，再根据visits升序排列
df.sort_values(by=['age', 'visits'], ascending=[False, True])


# In[37]:


#17）新增一列为时间序列，作为动物的出生时间，开始时间是“20210101”
df['time'] = pd.date_range('20210101','20210110')
df


# In[38]:


# 加载需要用到的包
import matplotlib.pyplot as plt
import numpy as np
# 定义数据
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
x = np.arange(len(labels))
width = 0.35  # 设置条的宽度

#2.绘制图表主体 
# 定义画布、轴域
fig, ax = plt.subplots()
# 分别绘制男女的条形图，注意横坐标要错开
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')
# 添加其他设置
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

#3.定义数据标签函数并添加标签，绘图
# 设置添加数据标签的函数
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 文本位置向上偏移三个单位
                    textcoords="offset points", # 相对xy进行偏移
                    ha='center', va='bottom')

# 对男女两个条形添加标签
autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.show()


# In[ ]:




