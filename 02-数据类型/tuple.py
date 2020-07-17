"""
 元组
"""
my_list = [1,2,3]
my_tuple = ("hello",2002,my_list)
print(my_tuple)
print(type(my_tuple))

# 取前半部分
my_list = (1,2,3,4,5,6,7,8,9)
print(my_list[0:len(my_list) // 2])
# (9, 8, 7, 6, 5) 必须指定方向-1,默认是1(正向)
print(my_list[-1:-6:-1])

my_tuple = (1,2,3,4,5)
my_list = list(my_tuple)
my_list.remove(2)
print(my_list)
print(my_tuple)

my_tuple = tuple(my_list)
#del my_tuple
print(my_tuple)

male_list = []
female_list = []
tuple_gender = (male_list,female_list)
tuple_gender[0].append("张深证")
tuple_gender[0].append("刘玉江")
tuple_gender[0].append("董长春")
tuple_gender[1].append("刘沛霞")
print(tuple_gender)

a = ()
b = ("hello")
print(type(a))
print(type(b)) # string
b = ("hello",)
print(type(b)) # tuple
