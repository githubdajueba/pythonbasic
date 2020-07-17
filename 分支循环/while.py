"""

 while 循环
"""
num = 10
while num > 0:
    num -= 1
    if num == 5:
       continue
        #
       # break
    print(num)
else:
    print("循环结束")

num = 100
while num > 0:
     num -= 1
     if num % 2 != 0:
         continue
     print(num)

