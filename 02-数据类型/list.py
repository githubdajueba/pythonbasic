"""
   list 列表
"""
# 类似字符串 与其操作方式
my_list = [1,"a",1.1,[1,2,3]]
 # 矩阵 多用于图片相关
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(type(my_list))
print(my_list[1])
print(my_list[3][1])

my_list = [1,2,3,4,5,6,7]
print(my_list[3:6])
print(my_list[::-1])

# 增加元素 list可变
my_list.append(8)
print(my_list)
my_list.insert(4,"and")
print(my_list)

# 删除元素 pop 默认最后一个
my_list.pop()
print(my_list)
my_list.pop(0)
print(my_list)
# del 删除某一个对象,不可恢复,可删除一切,默认的关键字
del my_list[1]
# del my_list
print(my_list)
# remove 根据具体内容删除
my_list.remove("and")
print(my_list)
try:
    my_list.remove(5)
    my_list.remove("annd")
except ValueError as ve:
    print(ve)

print(my_list)
# 修改
my_list[2] = 99
print(my_list)

print("ee" in my_list)
print("ee" not in my_list)

list1 = [1,2,3]
list2 = [1,2,3,4,5]
print(list1+list2)
print(list1*3)

print(list1.count(3))

print(my_list[::-1])
my_list.reverse()
print(my_list)


my_list = ["B","D","C","A"]
my_list.sort()
print(my_list)
my_list.clear()
print(my_list)

a_list = [1,2,3,4,5]
b_list = a_list
c_list = a_list.copy()
a_list.remove(2)
b_list.append(6)
print(a_list)
print(b_list)
print(c_list) # 不变


