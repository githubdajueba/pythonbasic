"""
 函数
"""
sum ="1+2"
p = eval(sum)
print(eval(sum))
print(exec("print('python')"))

def print_name(name):
    """

    :param name:
    :return:
    """
    #print(name)
    return "我叫%s"%name

str = print("doncc")
print(str)

print_name("dondcc")

def comput(comp):
    """"
     小型计算器
    """
    return eval(comp)

# comp = input("输入表达式:")
# print(comput(comp))

# a = 1
# add = a._add_(2)
# print(add)

def print_info(name,age,gender):
    print("我叫%s,是一个%d岁的小%s孩"%(name,age,gender))
print_info("lpx",12,"male") # 参数必须传,称为 必备参数
print_info(age=11,name="jjj",gender="fe")
#默认值
def print_info(name,age,gender="male"):
    print("我叫%s,是一个%d岁的小%s孩"%(name,age,gender))
print_info("lpx",12,"female")
#可变参数 *
def print_args(name,*arg,**karg):
    print(name)
    print(*arg)
    print(*karg)
print_args("ll",11,23,4,"ff")
