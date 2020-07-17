"""
 if 分支
"""
input = int(input("请输入:"))
print(input)
print(type(input)) # string

if input % 2 ==0:
    print("偶数")
    if input > 100:
        print("大于")
elif input % 2 > 0:
    print("奇数")
else:
    print("其他")

