#!/home/app/python3.7.6
# _*_ coding: utf-8 _*_
print("Hello World")
# 单行
'''
 多行(少用)
'''
"""
 多行
"""
a = 10
if a > 10 and a <100:
    print('a>=10')
    if a < 20:
        print(20)
elif a == 10:
   print("a==10")
else:
   print("a<10")

# 變量名或函數名之間一般用 _
uaer_name = "dondcc"
"""
定義變量不需要指定類型,但python 是強類型語言
"""
a = 1
b = "one"
print(type(a))
print(b+str(a))
c = 1.1
print(type(c))
# 關鍵字不能作為變量名
import keyword as kw
print(kw.kwlist)
print(len(kw.kwlist)) # 35個
"""
數據類型6種:Number:int,float,complex,bool
"""
# a,b,c,d = 1,1,1, 6+3j,True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
a = 1
b = 1.1
c = 4+5j
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(1+2)
print(1-2)
print(1/2)
print(1*2)
print(1%2)
print(2**3) # 乘方
print(5//2) # 2
print(5/2)  # 2.5

a = 1
a += 1

