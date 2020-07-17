"""
 for
"""
# list = ["1q","2q","3q","4q","5q"]
# for i in list:
#     if i == "2q": # == 相当于 equals
#         #continue
#         break
#     print(i)
#
# for i in range(5): #0-4
#     print(i)
# for i in range(2,5): # 2-4
#     print(i)
# for i in range(0,10,3):  #步长3
#     print(i)

#################
# 9 * 9
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(j,i,i*j),end='\t')
    print()
