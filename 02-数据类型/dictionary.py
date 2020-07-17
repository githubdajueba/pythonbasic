"""
 dictionary
 可变的
 无序的
 键:值  键唯一,是不可变类型,若相同会覆盖
"""
# list = [1,2,3]
# tuple = (1,2,3)
# my_dict = {"陈子枢":"总监","齐雷":"程序员","张深证":"鼓励师"}
# print(my_dict)
# print(type(my_dict))
#
# my_dict["刘沛霞"] = "扫地"
# print(my_dict)
#
# my_dict["张深证"] = "初级"
# print(my_dict)
#
# # del clear
# #my_dict.clear()
# del my_dict["陈子枢"]
# print(my_dict)
#
# list = ["k1","k2","k3"]
# my_dict = dict.fromkeys(list,100)
# print(my_dict)
# list = ["k1","k1","k3"]
# my_dict = dict.fromkeys(list,"value")
# print(my_dict)


my_dict = {"陈子枢":"总监","齐雷":"程序员","张深证":"鼓励师"}
print(my_dict.get("齐雷","wu"))
print(my_dict.get("刘沛霞"))
print(my_dict)

print(my_dict.keys())

my_dict.setdefault("刘沛霞","架构师")
print(my_dict)
print("&"*30)
print(my_dict.values())
print(type(my_dict.values()))
list = list(my_dict.values())
print(list)
print(type(list))

key_list = ["k1","k2","k3"]
value_list = ["v1","v2","v3"]
my_dict = {k:v for k in key_list for v in value_list}
print(my_dict)
my_dict = {key_list[k]:value_list[k] for k in range(0,len(key_list)) for k in range(0,len(value_list))}
print(my_dict)
# &, |, - ,in, not in
set1 = {1,2,3,4}
set2 = {1,3,5}
set = set1 | set2
print(set)
set = set1 & set2
print(set)
print(1 in set)
print(1 not in set)
