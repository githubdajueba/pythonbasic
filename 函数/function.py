"""
 函数
"""
from functools import reduce

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
# 有多个返回值
def re_fun(name,age,gender):
    return name,age,gender
n,a,g = re_fun("dond",12,{1:2})
print(n)
print(a)
print(g)
# 可以返回多次  yield,又称生成器(generator) 返回值可迭代
def get_nums(n):
    for i in range(n):
        if i % 2 ==0:

            yield i
nums = get_nums(10)
print(type(nums))
print(next(nums))
# for i in nums:
#     print(i)
# 迭代一次后 就没值了,相当于...next()
list = [i for i in nums]
print(list)

name = "dongcc" #全局变量
def field():
    global name  #global不能直接赋值
    #表示修改全局的值
    name = "百威"
    age = 12
    print("%s今年%d岁了"%(name,age))

field()
print(name) #与有无global输出结果不同
"""
匿名函数:只用一次
高阶函数:reduce,map,filter
"""
f = lambda x,y:x+y
print(f(1,2))
#        传参:函数体
i = lambda i : i ** 2
print(i(2))
print("#"*30)
list = [1,2,3]
def sum(x,y):
    return x+y
print(reduce(lambda x, y: x * y, list))
print(reduce(sum,list))