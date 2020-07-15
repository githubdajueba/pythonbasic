"""
字符創
"""
a = "hello 1"
b = "hello 2"
c = """hello 3"""
d = '''hello 4'''
print(a+b+c+d)
# 可以用轉義符 \ ,或在前面加 r
e = r'i\ am dongcc'
print(e)
# *在字符串使用中表示使字符串翻倍
print("hello"*10)
print("="*20)
print(c*10)
# 會輸出換行
c = """c
"""
print(c*10)

"""
字符串的下標及截取
"""
tedu = "wwww.tedu.cn"
print(tedu[0])
print(tedu[4])
print(tedu[0:3]) # 左閉右開,不包括末尾的值
print(tedu[0:5:2])
print(tedu[::2])
print(tedu[::-1])
print("8"*5)
print(tedu[-1:-4:-2])
print(tedu[-4:-1])

i = 10
name = "lpx"
print("我叫%s,今年%d歲"%(name,i))