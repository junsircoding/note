Python 面试必考考点

深拷贝、浅拷贝
装饰器
get、post区别
套接字文件游标互斥锁

range(a, b)
左闭右开
random.randInt(a, b)
左右闭
a="abcdef"
a[2:4:1]
切片是左闭右开
这个输出 cd 取不到e

面试题：
python2和python3输出列表形式不同
因为python3对内存做了优化，它输出的列表是压缩过的

得到字典的元素，可以用my_dict['key']也可以用my_dict.get('key')
区别是：若不存在该元素，get()不报错，而[i]报错


VA_HOME%\jre\bin;C:\Program Files\Git\cmd

切片：
str[a:b:c]
a是开始下标（从0开始，即1是第2个）
a可不写，默认为0
b是结束下标（从0开始，即5是第6个）
b可不写，默认为最后
b若为负数，表示倒数第几个
c是步长，可不写，默认为1步。
[a, b)是左闭右开
重要：
快速将字符串倒序输出：print(str[::-1])
理解：
切片内在相当于一个遍历器，遍历方向取决于“步长”参数的符号，+则向右遍历，-则向左遍历。“上标”或“下标”的符号意为在0下标的基础上在+方向或-方向的某个值。所以填写切片参数的时候，注意方向要符合实际，否则不出结果。

字符串对象重要API
find("子串")检测p是否在串内，是return 下标， 否return -1
index("子串")同find，唯一不同：若不存在，报错
count("子串")统计出现子串的次数，若没有return 0

replace("改谁", "改成啥", "替换几次") 
不改变原数据，拷贝一份，再改
若设定的替换次数超过程序统计出的次数，以程序统计为准

split("分割标识", "分割几次")
若主串内有多个分割标识，返回列表

"连接符".join(集合类)合并
集合类可以是：列表，元组，字典，集合

capitalize()
只有第一个首字母大写

title()
所有单词首字母大写

lower()
所有单词首字母变小写

upper()
所有字母小写变大写

lstrip()/rstrip()/strip() 删除字符串左/右侧/全部空白符

ljust/rjust/center(长度, "填充字符") 填充"填充字符",结果源字符串在左/右/中间

startswith/endwith("检测字符") 返回bool 判断是否已"检测字符"开始/结束

isalpha() 判断是否包含字母

isdigit() 判断是否包含数字

isalnum() 判断串元素是否单纯(都是数字或字母等等)

isspace() 判断串内是否都是空格

8个老师随机分配到3个办公室
c = [‘1’, ‘2’, ’3’, ‘4’, ‘5’, ‘6’, ‘7’, ‘8’]
d = [‘A’, ‘B’, ‘C’]
# a返回随机选出的老师的下标
a = random.randInt(0, len(c))
# b返回随机选出的办公室下标
b = random.randInt(0, 3)
list = []
list.append(c[a])
list.append(d[b]) 
del c[a]


2019年2月24日上午所讲内容大部分是已学过的内容。
大体上讲了这些：
python变量名的起名规则：
* 		只能由字母、下划线、数字组成，就是说这样的不行：“a-1”，“a,1”
* 		不能由数字开头
* 		不能与关键字重名，比如“int”，“float”等
* 		命名应遵循“见名知意”的规则，形式尽量是“驼峰”样式，比如：MyName，myName。
type()函数：返回变量类型
    code：
console：

eval()函数：返回字符串内元素的本来类型，注意它的类型不是“str”，而是其专有类型“type”
    code：
console：

有三种新的“集合类”类型，之前没见过
* 		tuple    形式：(3, 4, 5)
* 		list        形式：[3, 4, 5]
* 		set        形式：{3, 4, 5}
* 		dict       形式：{'username':'Tom', 'age':20}
一种新的格式化输出语句：
print(f'我是第{a}名')

下午没有上课。
做完了WonderfulSong的登录和注册功能，以及表单验证。

区间判断与数学写法一致：
    18 <= age <= 20
debug方法
if，elif
注意缩进（猜拳游戏）
运算符有“幂运算”：
    a ** 2 = a * a
三目运算符 
    a if a > b else b

print('*' * 3)  意为输出3个*
python里有for--else和while--else

