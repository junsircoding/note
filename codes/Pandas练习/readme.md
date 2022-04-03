#### 基本

##### 创建 Dataframe

```python
import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
            "John, Mr. Peter Parker"
        ],
        "Age": [22, 35, 58, 24],
        "Sex": ["male", "male", "female", "male"],
        "Fare": [1500, 1600, 1550, 3345],
        "Pclass": [2, 2, 3, 3],
        "Location": [
            "China",
            "America",
            "Africa",
            "Japan"
        ]
    }
)
```

```shell
                       Name  Age     Sex  Fare  Pclass Location
0   Braund, Mr. Owen Harris   22    male  1500       2    China
1  Allen, Mr. William Henry   35    male  1600       2  America
2  Bonnell, Miss. Elizabeth   58  female  1550       3   Africa
3    John, Mr. Peter Parker   24    male  3345       3    Japan
```

##### 创建 Series

```python
ages = pd.Series([22, 35, 58], name="Age")
```

```shell
0    22
1    35
2    58
Name: Age, dtype: int64
```

##### 选取一列

```python
df["Age"]
```

```shell
0    22
1    35
2    58
3    24
Name: Age, dtype: int64
```

##### 预览前几行

```python
df.head() # 默认5行
df.head(8) # 可指定行数
```

##### 预览后几行

```python
df.tail() # 默认5行
df.tail(8) # 可指定行数
```

##### 查看每一列数据类型

```python
df.dtypes
```

```shell
Name        object
Age          int64
Sex         object
Fare         int64
Pclass       int64
Location    object
dtype: object
```

##### 查看行列数

```python
df.shape
```

```shell
(4, 6)
```

##### 求最大值

> 仅对数字类型数据有效

```python
df["Age"].max()
```

##### 罗列基本统计信息

```python
df.describe()
```

```shell
            Age         Fare   Pclass
count   4.00000     4.000000  4.00000
mean   34.75000  1998.750000  2.50000
std    16.52019   898.428025  0.57735
min    22.00000  1500.000000  2.00000
25%    23.50000  1537.500000  2.00000
50%    29.50000  1575.000000  2.50000
75%    40.75000  2036.250000  3.00000
max    58.00000  3345.000000  3.00000
```

##### 罗列全部数据类型

```python
df.info()
```

```shell
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 6 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   Name      4 non-null      object
 1   Age       4 non-null      int64 
 2   Sex       4 non-null      object
 3   Fare      4 non-null      int64 
 4   Pclass    4 non-null      int64 
 5   Location  4 non-null      object
dtypes: int64(3), object(3)
memory usage: 320.0+ bytes
```

#### 文件

##### 读取文件

```python
df = pd.read_csv("path.csv")
df = pd.read_csv("path.csv", index_col=0, parse_dates=True)
# index_col=0 以第 0 列 为索引
# parse_dates=True 将时间类型的列转义为时间戳类型
```

##### 将数据导出为 Excel

```python
df.to_excel(
    "data.xlsx",
    sheet_name="some_data",
    index=False
)
```

#### 筛选

##### 大于某值

```python
df[
    df["Age"] > 35
]
```

```shell
                       Name  Age     Sex  Fare  Pclass Location
2  Bonnell, Miss. Elizabeth   58  female  1550       3   Africa
```

##### 指定枚举值列表

```python
df[
    df["Fare"].isin(
        [1500, 1600]
    )
]
```

```shell
                       Name  Age   Sex  Fare  Pclass Location
0   Braund, Mr. Owen Harris   22  male  1500       2    China
1  Allen, Mr. William Henry   35  male  1600       2  America
```

##### 多个条件并集

```python
df[
    (df["Pclass"] == 2) | (df["Pclass"] == 3)
]
# 只能用 | 或 &，不能用 or 或 and
```

```shell
                       Name  Age     Sex  Fare  Pclass Location
0   Braund, Mr. Owen Harris   22    male  1500       2    China
1  Allen, Mr. William Henry   35    male  1600       2  America
2  Bonnell, Miss. Elizabeth   58  female  1550       3   Africa
3    John, Mr. Peter Parker   24    male  3345       3    Japan
```

##### 筛选非空值

```python
df[
    df["Age"].notna()
]
```

##### 筛选后返回指定列

```python
adult_names = df.loc[df["Age"] > 35, "Name"]
```

##### 指定行区间、列区间

```python
df.iloc[2:3, 1:4]
```

```shell
   Age     Sex  Fare
2   58  female  1550
```

##### 查看对限定条件的满足情况

```python
0    False
1    False
2     True
3    False
Name: Age, dtype: bool
```

#### 更改

##### 更改数据

```python
df["Age"] = "Mike"
```

##### 创建新列

```python
df["new_age"] = df["Age"] * 1.882
df["age_fare"] = (df["Age"] / df["Fare"])
```

```shell
                       Name  Age     Sex  Fare  Pclass Location  new_age  age_fare
0   Braund, Mr. Owen Harris   22    male  1500       2    China   41.404  0.014667
1  Allen, Mr. William Henry   35    male  1600       2  America   65.870  0.021875
2  Bonnell, Miss. Elizabeth   58  female  1550       3   Africa  109.156  0.037419
3    John, Mr. Peter Parker   24    male  3345       3    Japan   45.168  0.007175
```

##### 重命名列名

```python
df_renamed = df.rename(
    columns={
        "Age": "X_Age",
        "Fare": "X_Fare",
        "Name": "X_Name",
    }
)
```

##### 将列名全转为小写

```python
df_lower = df.rename(
    columns=str.lower
)
```

#### 数据分析

##### 求平均值

```python
df["Age"].mean()
```

##### 求中位数

```python
df["Age"].median()
```

##### 求最值

```python
df["Age"].max()
df["Age"].min()
```

##### 求偏度

```python
df["Age"].skew()
```

##### 一次性计算多列

```python
df[
    ["Age", "Fare"]
].median()
```

##### 一次性计算多列的多种统计类型

```python
df.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"]
    }
)
```

```shell
              Age     Fare
min     22.000000  1500.00
max     58.000000  3345.00
median  29.500000  1575.00
skew     1.368208      NaN
mean          NaN  1998.75
```

##### 对全部数据分组

```python
df.groupby("Age").mean()
```

```shell
       Fare  Pclass
Age                
22   1500.0     2.0
24   3345.0     3.0
35   1600.0     2.0
58   1550.0     3.0
```

##### 对指定几列分组

```python
df[
    ["Fare", "Age"]
].groupby("Age").mean()
```

```shell
       Fare
Age        
22   1500.0
24   3345.0
35   1600.0
58   1550.0
```

##### 分组后再筛选

```python
df.groupby("Sex")["Age"].mean()
```

```shell
Sex
female    58.0
male      27.0
Name: Age, dtype: float64
```

```python
df.groupby(
    ["Sex", "Pclass"]
)["Fare"].mean()
```

```shell
Sex     Pclass
female  3         1550.0
male    2         1550.0
        3         3345.0
Name: Fare, dtype: float64
```

##### 枚举值计数

```python
# 常规方法
df.groupby("Pclass")["Pclass"].count()
# 内置方法
df["Pclass"].value_counts()
```

```shell
Pclass
2    2
3    2
Name: Pclass, dtype: int64
```

#### 排序

##### 指定某列排序

**默认升序**

```python
df.sort_values(
    by="Age"
).head()
```

```shell
                       Name  Age     Sex  Fare  Pclass Location
0   Braund, Mr. Owen Harris   22    male  1500       2    China
3    John, Mr. Peter Parker   24    male  3345       3    Japan
1  Allen, Mr. William Henry   35    male  1600       2  America
2  Bonnell, Miss. Elizabeth   58  female  1550       3   Africa
```

**降序**

```python
df.sort_values(
    by="Age",
    ascending=False
).head()
```

```shell
                       Name  Age     Sex  Fare  Pclass Location
2  Bonnell, Miss. Elizabeth   58  female  1550       3   Africa
1  Allen, Mr. William Henry   35    male  1600       2  America
3    John, Mr. Peter Parker   24    male  3345       3    Japan
0   Braund, Mr. Owen Harris   22    male  1500       2    China
```

##### 按照行标签排序

```python
df.sort_index().head()
```

```shell
                       Name  Age     Sex  Fare  Pclass Location
0   Braund, Mr. Owen Harris   22    male  1500       2    China
1  Allen, Mr. William Henry   35    male  1600       2  America
2  Bonnell, Miss. Elizabeth   58  female  1550       3   Africa
3    John, Mr. Peter Parker   24    male  3345       3    Japan
```

#### 调整表格结构

##### 宽表变窄表

> 宽表就是把字段全都堆在一个表中，没有用多对多活其他更符合数据库三范式的方式加以设计。感官上看字段非常多，数据非常冗余，但是理解起来简单，一看就懂。宽表的存在是为了用空间换时间。
>
> 窄表是相对于宽表而言，更符合逻辑。是为了表述某个维度的信息，从宽表中提取出若干列，组成一个新的表，便于做分析。

一个宽表的示例如下：

```python
df = pd.DataFrame(
    {
        "phone": [
            "iPhone 13 Pro",
            "iPhone 13 Pro",
            "iPhone 13 Pro",
            "iPhone 13 Pro",
            "Huawei Mate 40 Pro",
            "Huawei Mate 40 Pro",
            "Huawei Mate 40 Pro",
            "Huawei Mate 40 Pro",
        ],
        "store": [
            "jingdong",
            "tianmao",
            "taobao",
            "pinduoduo",
            "jingdong",
            "tianmao",
            "taobao",
            "pinduoduo"
        ],
        "price": [
            7999,
            8399,
            6569,
            6754,
            7688,
            5499,
            6799,
            6588
        ]
    }
)
```

这个表格的数据描述了**京东**、**拼多多**、**淘宝**、和**天猫**四家平台的 **iphone 13 Pro** 和 **Huawei Mate 40 Pro** 的价格数据（数据是瞎写的），可以看到 `phone` 和 `store` 这两列稍显冗余，重复内容过多。

```shell
                phone      store  price
0       iPhone 13 Pro   jingdong   7999
1       iPhone 13 Pro    tianmao   8399
2       iPhone 13 Pro     taobao   6569
3       iPhone 13 Pro  pinduoduo   6754
4  Huawei Mate 40 Pro   jingdong   7688
5  Huawei Mate 40 Pro    tianmao   5499
6  Huawei Mate 40 Pro     taobao   6799
7  Huawei Mate 40 Pro  pinduoduo   6588
```

现在想要提取一个窄表，以 `phone` 为纵向索引，`store` 为横向字段，主体显示的值为 `price`。

```python
df.pivot(
    index="sex", # 索引
    columns="id", # 列名
    values="price" # 值
)
```

```shell
store               jingdong  pinduoduo  taobao  tianmao
phone                                                   
Huawei Mate 40 Pro      7688       6588    6799     5499
iPhone 13 Pro           7999       6754    6569     8399
```

对每行每列添加**总计**的数据。

```python
df.pivot_table(
    index="phone",
    columns="store",
    values="price",
    aggfunc="mean", # 函数名称
    margins=True # 显示开关
)
```

```shell
store               jingdong  pinduoduo  taobao  tianmao       All
phone                                                             
Huawei Mate 40 Pro    7688.0       6588    6799     5499  6643.500
iPhone 13 Pro         7999.0       6754    6569     8399  7430.250
All                   7843.5       6671    6684     6949  7036.875
```

##### 重置索引

对于这个 `DataFrame`，当前的索引列是 `phone` 的数据。

```shell
store               jingdong  pinduoduo  taobao  tianmao
phone                                                   
Huawei Mate 40 Pro      7688       6588    6799     5499
iPhone 13 Pro           7999       6754    6569     8399
```

将其索引重置为数字序号：

```python
df.pivot(
    index="phone",
    columns="store",
    values="price"
).reset_index()
```

```shell
store               phone  jingdong  pinduoduo  taobao  tianmao
0      Huawei Mate 40 Pro      7688       6588    6799     5499
1           iPhone 13 Pro      7999       6754    6569     8399
```

如果要丢弃原来的 `phone` 索引，加上 `drop` 参数：

```python
df.pivot(
    index="phone",
    columns="store",
    values="price"
).reset_index(drop=True)
```

```shell
store  jingdong  pinduoduo  taobao  tianmao
0          7688       6588    6799     5499
1          7999       6754    6569     8399
```

##### 联结 `datafame`

有这样两个结构相似的 `dataframe`：

```python
df1 = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry"
        ],
        "Age": [22, 35],
        "Sex": ["male", "male"],
        "Fare": [1500, 1600],
        "Pclass": [2, 2],
        "Location": [
            "China",
            "America"
        ]
    }
)
```

第一个表格是一个中国人和一个美国人的信息：

```shell
                       Name  Age   Sex  Fare  Pclass Location
0   Braund, Mr. Owen Harris   22  male  1500       2    China
1  Allen, Mr. William Henry   35  male  1600       2  America
```

```python
df2 = pd.DataFrame(
    {
        "Name": [
            "Bonnell, Miss. Elizabeth",
            "John, Mr. Peter Parker"
        ],
        "Age": [58, 24],
        "Sex": ["female", "male"],
        "Fare": [1550, 3345],
        "Pclass": [3, 3],
        "Location": [
            "Africa",
            "Japan"
        ]
    }
)
```

第二个表格是日本人和非洲人的信息：

```shell
                       Name  Age     Sex  Fare  Pclass Location
0  Bonnell, Miss. Elizabeth   58  female  1550       3   Africa
1    John, Mr. Peter Parker   24    male  3345       3    Japan
```

将他们合并成一个 `dataframe`：

```python
pd.concat(
    [df1, df2],
    axis=0 # 0 表示上下合并，1 表示左右合并
)
```

```shell
                       Name  Age     Sex  Fare  Pclass Location
0   Braund, Mr. Owen Harris   22    male  1500       2    China
1  Allen, Mr. William Henry   35    male  1600       2  America
0  Bonnell, Miss. Elizabeth   58  female  1550       3   Africa
1    John, Mr. Peter Parker   24    male  3345       3    Japan
```

##### 合并 `dataframe`

对于以下两个 `dataframe`：

```python
df1 = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry"
        ],
        "Age": [22, 35]
    }
)
```

```shell
                       Name  Age
0   Braund, Mr. Owen Harris   22
1  Allen, Mr. William Henry   35
```

```python
df2 = pd.DataFrame(
    {
        "Age": [22, 35],
        "Sex": ["female", "male"],
        "Fare": [1550, 3345],
        "Pclass": [3, 3],
        "Location": [
            "Africa",
            "Japan"
        ]
    }
)
```

```shell
   Age     Sex  Fare  Pclass Location
0   22  female  1550       3   Africa
1   35    male  3345       3    Japan
```

他们有相同的一列 `Age`，可以以 `Age` 为基准，将两个 `dataframe` 合并：

```python
df = pd.merge(
    df1,
    df2,
    how="left",
    on="Age" # 以 Age 为基准
)
```

```shell
                       Name  Age     Sex  Fare  Pclass Location
0   Braund, Mr. Owen Harris   22  female  1550       3   Africa
1  Allen, Mr. William Henry   35    male  3345       3    Japan
```

